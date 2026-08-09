# Intensive reading of official code and minimal implementation

The official repository is [bigdata-ustc/NCAT](https://github.com/bigdata-ustc/NCAT). The public snapshot commit checked on this page is `58f88b30cb6ecdcd7ed35a8ad9ce2aa23a9cd95f`. The warehouse is small in size and the core logic is concentrated in four places.

|File|Responsibilities|
|---|---|
| `functionApproximation/NCAT.py` |Dual-channel Q network, attention, TD MSE updates|
| `envs/env.py` |support/query environment, response model update, query reward|
| `agents/Train.py` |Trajectory collection, exploration, replay, Bellman target|
|`launch.py` and `model_train.sh`|Parameters, training entry and sample configuration|

## 1. From data to training entrance

The order given in the README is:

```bash
cd data/assist1213
python data_preprocess.py

cd ../..
python divide_data.py

cd envs/pre_train
python main.py

cd ../..
sh model_train.sh
```

After preprocessing is completed, `env.py` reads:

```text
data/<data_name>/log_data_filtered.json
```

And load pretraining IRT/NCDM from `envs/model_file/<data_name>/...`.

!!! warning "The warehouse is not a complete experimental package ready to run"

    The original data file, absolute path, pretraining model directory and GPU environment need to be completed by the user. `pwd_path = 'xxx/NCAT/...'` in `config.py` is a placeholder, and the core model also has CUDA hardcoded.

## 2. How to structure the environment support/query

`env.__init__` in:

```python
self.setup_train_test()
self.sup_rates, self.query_rates = self.split_data(ratio=0.5)
```

`split_data` Shuffle each student's items and cut them in half:

```python
sup_rates[u] = {
    item: self.rates[u][item]
    for item in all_items[:int(ratio * len(all_items))]
}
query_rates[u] = {
    item: self.rates[u][item]
    for item in all_items[int(ratio * len(all_items)):]
}
```

This is different from 70%/30% of the paper. `re_split_data()` is cut again at the end of each training epoch, which is consistent with the paper "recut every round".

The candidate set only comes from the student's support:

```python
@property
def candidate_items(self):
    uid = self.state[0][0]
    return set(self.sup_rates[uid].keys())
```

## 3. One environment step

The order of `env.step(action)` is:

1. Assert that the action belongs to support and has not been selected;
2. Call `reward(action)`;
3. Determine whether it reaches \(T\);
4. Write the action, reward, termination flag and indicator into the state;
5. Return to the new state.

`reward` is the code core of the entire NCAT target:

```python
items = selected_items + [action]
correct = [historical_response[it] for it in items]

dataset.add_record([uid] * len(items), items, correct)
model.update(dataset, learning_rate, epoch=1)

loss, pred = model.cal_loss(
    [uid] * len(query_items),
    query_items,
    query_answers,
    know_map,
)
model.init_stu_emb()
return -loss, ACC, AUC, correct[-1]
```

It first uses the accumulated selected questions to adapt to the student embedding, then calculates the loss on the query, and finally resets the student embedding. This reset means that the next step starts again from the global initial state and refits with all accumulated selected questions, instead of continuing a small step on the student parameters of the previous step.

## 4. Four input tensors

Q network forward accepts:

```python
p_0_rec, p_1_rec, p_0_target, p_1_target
```

The meaning is as follows:

| tensor | shape |meaning|
|---|---|---|
| `p_0_rec` | \(B\times L_0\) |Wrong answer question sequence, preceded by padding question 0|
| `p_1_rec` | \(B\times L_1\) |Correct question sequence, preceded by padding question 0|
| `p_0_target` | \(B\) |The last valid position index of each line|
| `p_1_target` | \(B\) |The last valid position index of each line|

`convert_item_seq2matrix` Complement sequences of different lengths into matrices:

```python
matrix = np.zeros((batch_size, max_length), dtype=np.int32)
target_index = [len(seq) - 1 for seq in item_seq]
```

Initially, both channels are `[0]`, so question number 0 serves as both padding and empty status token.

## 5. embedding and Performance Learning

The model defines two tables:

```python
self.q_embed_0 = nn.Embedding(n_question, d_model)
self.q_embed_1 = nn.Embedding(n_question, d_model)
```

Then generate a length mask and send it to two encoders respectively:

```python
item_emb_0 = self.q_embed_0(p_0_rec)
item_emb_1 = self.q_embed_1(p_1_rec)

src_mask_0 = mask(p_0_rec, p_0_target + 1).unsqueeze(-2)
src_mask_1 = mask(p_1_rec, p_1_target + 1).unsqueeze(-2)

item_per_0 = self.self_atten_0(item_emb_0, src_mask_0)
item_per_1 = self.self_atten_1(item_emb_1, src_mask_1)
```

`EncoderLayer` uses pre-norm residuals:

```python
x = x + dropout(self_attention(layer_norm(x)))
x = x + dropout(feed_forward(layer_norm(x)))
```

## 6. Code path of Contradiction Learning

The warehouse uses the original embedding as query/key and the Performance Learning output as value:

```python
input_01, input_10 = self.contradiction(
    item_emb_0,
    item_emb_1,
    item_per_1,
    item_per_0,
)
```

`MultiHeadedAttention_con` Calculate first

\[
\operatorname{softmax}
\left(
\frac{Q_0K_1^\top}{\sqrt{d_h}}
\right)V_1,
\]

Then use the transpose of this attention to aggregate the other direction:

\[
A^\top V_0.
\]

This is a set of two-way aggregations that share a pair score. The code does not pass the padding mask to the contradiction attention, and then directly:

```python
input_01 = input_01.mean(-2)
input_10 = input_10.mean(-2)
```

Therefore the padding length within the mini-batch may affect the cross-channel mean. Stable reproduction should construct pairwise masks for both directions and take the masked mean.

## 7. Pooling and output layer

The warehouse takes the last valid position for the self-attention channel:

```python
input_0 = item_per_0[batch_index, p_0_target]
input_1 = item_per_1[batch_index, p_1_target]
```

Take the mean of the cross channel and then concatenate:

```python
state_vector = torch.cat(
    [input_0, input_1, input_01, input_10],
    dim=-1,
)
q_values = self.policy_layer(state_vector)
```

`policy_layer` is:

```python
Linear(4 * d_model, 512)
ReLU()
Dropout()
Linear(512, n_question)
```

The four-way average pooling described in the paper and the "self takes the last position and cross takes the average" here should be reported separately.

## 8. How to block actions with behavioral strategies

When collecting trajectories, `Train.py` first calculates the Q values of all questions and then blocks them:

```python
for item in actions:
    policy[item] = -np.inf

for item in range(item_num):
    if item not in env.candidate_items:
        policy[item] = -np.inf

action = np.argmax(policy[1:]) + 1
```

This part correctly ensures:

- Do not select topics repeatedly;
- Select only support questions from current students;
- Question number 0 does not serve as an action.

Training exploration replaces the entire `policy` with random numbers through a certain probability, and then applies the same set of masks.

## 9. replay and Bellman target

Warehouse storage:

```python
[state, action, reward, done, next_state]
```

Use the next state to predict the maximum Q value after sampling:

```python
value = self.fa.predict(next_state_data)
value[:, 0] = -500

goal = reward + (
    np.max(value, axis=-1)
    * not_done
    * effective_gamma
)
```

There is an important implementation risk here: when finding the maximum value in the next state, only question number 0 is blocked, and the selected questions and support extra questions are not blocked. The legal action mask of the behavioral policy does not enter the TD target, and the network may be bootstrapped with a question that is not actually optional.

It is recommended to change it to:

```python
next_q = target_net(next_state)
next_q = next_q.masked_fill(~next_valid_mask, float("-inf"))
next_best = next_q.max(dim=1).values
target = reward + gamma * (~done).float() * next_best
```

## 10. optimizer life cycle

Official `optimize_model` Adam is recreated with every update:

```python
optimizer = optim.Adam(self.parameters(), lr=lr)
```

In this way, Adam's first-order and second-order momentum are lost after each batch, and the behavior is closer to single-step optimization with adaptive scaling. It is recommended to create the optimizer only once when initializing the model or trainer:

```python
optimizer = torch.optim.Adam(
    online_net.parameters(),
    lr=learning_rate,
)
```

The training loop continues to reuse it and checkpoint the optimizer state together.

## 11. Comparison of papers, warehouses and recommended reproduction

|components|Paper|Public warehouse snapshot|Recommended to reproduce|
|---|---|---|---|
| support/query | 70%/30% | 50%/50% |Configured by target protocol|
|Student segmentation|60%/20%/20%, 50% off|About 80%/10%/10%|Students isolate and record fold|
|four way pooling|average all|self last position, cross mean|Both ablation|
| contradiction padding |The formula is not expanded|Mask not passed| pairwise mask |
|TD next action|Collection of legal questions|Only block questions 0|Complete legal action mask|
| target network |Not clear|No independent target|Add target/Double DQN|
|replay capacity| 10,000 | 50,000 |hyperparameterization|
| optimizer |General training semantics|Rebuild Adam every batch|persistence optimizer|
|Equipment|GPU experiment|Hardcoded CUDA|`device` parameterization|

## 12. Make a verifiable minimal version first

Before introducing attention, you can first use the three-valued state vector to verify the environment:

\[
x_{t,j}
=
\begin{cases}
-1, & q_j\text{Wrong answer},\\
1, & q_j\text{Correct},\\
0, & q_j\text{Not answered yet}.
\end{cases}
\]

```python
class TinyQNetwork(torch.nn.Module):
    def __init__(self, n_items, hidden=128):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(n_items, hidden),
            torch.nn.ReLU(),
            torch.nn.Linear(hidden, n_items),
        )

    def forward(self, state):
        return self.net(state)
```

The minimal version must pass first:

1. After the item is selected, the corresponding position of the next state changes;
2. The selected topic will never be selected again;
3. Support foreign topics will never enter argmax;
4. Terminate sample target equal to reward;
5. Changing a real-time answer will change the next Q vector;
6. The query question does not enter the student parameter fitting;
7. Test students do not engage in response modeling or strategy training.

After passing these tests, `TinyQNetwork` was replaced with the NCAT encoder, and the environment, replay, and TD updates remained unchanged. This allows "reinforcement learning pipeline errors" and "attention representation errors" to be located separately.

## 13. Minimal NCAT interface

A clean network interface simply accepts a state tensor and outputs a Q value:

```python
class NCATQNetwork(torch.nn.Module):
    def forward(
        self,
        incorrect_ids,
        incorrect_mask,
        correct_ids,
        correct_mask,
    ):
        incorrect = self.incorrect_encoder(
            self.incorrect_embedding(incorrect_ids),
            incorrect_mask,
        )
        correct = self.correct_encoder(
            self.correct_embedding(correct_ids),
            correct_mask,
        )

        cross_incorrect, cross_correct = self.cross_encoder(
            incorrect,
            incorrect_mask,
            correct,
            correct_mask,
        )

        state = torch.cat(
            [
                masked_mean(incorrect, incorrect_mask),
                masked_mean(correct, correct_mask),
                masked_mean(cross_incorrect, incorrect_mask),
                masked_mean(cross_correct, correct_mask),
            ],
            dim=-1,
        )
        return self.policy_head(state)
```

The network is responsible for representation; the trainer is responsible for action legality, exploration, replay, target and optimization. After the separation of responsibilities, it is easier to do unit testing and ablation.

## 14. Complexity and performance bottlenecks

If the length of the two channels is \(k_0,k_1\), the main complexity of single-layer attention is approximately

\[
O(k_0^2d+k_1^2d+k_0k_1d).
\]

It is usually controllable when short measuring \(T\le20\). The bigger bottleneck often comes from re-fitting student parameters, traversing the entire query set and calculating rewards in each environment step. Consider:

- Batch local updates of multiple students;
- Cache item global representation;
- Use incremental local parameter updates instead of fitting from scratch at each step;
- Control query sample size and check reward variance;
- Parallel environment and vectorized legal action masks.

For the boundaries of the method and the next research space, see [Limitations, Method Comparison and Future Work](09-limitations-comparison-future.md).
