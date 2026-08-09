#BOBCAT official code intensive reading

This page reads the official repository [`arghosh/BOBCAT`](https://github.com/arghosh/BOBCAT)] and pins it to submission
[`e6b6245`](https://github.com/arghosh/BOBCAT/tree/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec), to avoid subsequent changes in the code causing mismatch between line numbers and behaviors.

!!! info "First remember the naming differences in the official code"

    The paper calls the low-variance approximation inspired by the influence function **Approx**. Official commands and branch judgment use
    `biased`, so `biirt-biased` and `binn-biased` correspond to
    BiIRT-Approx, BiNN-Approx. Here `biased` describes the statistical properties of gradient estimation, regardless of data bias.

## 1. Warehouse map

|File|Main responsibilities|position in paper|
| --- | --- | --- |
| [`dataset.py`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/dataset.py) |Training/meta partitioning within each student; constructing dense labels and masks| \(\Omega_i^{(1)}\)、\(\Gamma_i\) |
| [`model.py`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/model.py) |BiIRT/BiNN response model, local loss, state and Active/Random topic selection| \(g(j;\theta_i,\gamma)\)、\(\mathcal L'\) |
| [`policy.py`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/policy.py) |PPO topic selector and straight-through topic selector|Unbiased and Approx|
| [`train.py`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/train.py) |Inner layer adaptation, four training paths, validation, testing and early stopping|Double-layer optimized main loop|
| [`irt.py`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/irt.py) |Random/Active Baseline for Traditional 1PL IRT| IRT-Random、IRT-Active |
| [`utils/configuration.py`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/utils/configuration.py) |Data set size, learning rate, test length, batch and early stopping parameters|Experimental setup|
| [`utils/utils.py`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/utils/utils.py) |50% off student division, accuracy, AUC|Experimental evaluation|
| [`utils/preprocessing.py`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/utils/preprocessing.py) |Preprocessing of EdNet, Junyi, Eedi|Data preparation|

The main entrance is `train.py`. Only one combination of "response model × question selection method × data set × fold × test length" is trained in one run.

## 2. How does a sample enter the model?

### 2.1 Raw JSON

The preprocessed data is in students. Each record contains at least:

```json
{
  "q_ids": [12321, 17794, 17795],
  "labels": [1, 0, 1]
}
```

`q_ids[k]` and `labels[k]` together represent the student's historical answer to a question. The code only retains binary true and false labels,
The question stem, knowledge points, answer time or item text were not entered into the question selector.

### 2.2 80/20 split within students

[`Dataset.__getitem__`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/dataset.py#L21-L43)
First scramble all the observed answers of the student, and then use the last approximately \(20\%\) as a meta question:

```python
observed_index = np.arange(len(data["q_ids"]))
np.random.shuffle(observed_index)
target_index = observed_index[-N//5:]
trainable_index = observed_index[:-N//5]
```

The corresponding relationship is

\[
\texttt{trainable\_index}\leftrightarrow\Omega_i^{(1)},
\qquad
\texttt{target\_index}\leftrightarrow\Gamma_i.
\]

`seed=None` of the training set will be re-shuffled every time it is sampled, so the training/meta division will continue to change. verify and
When testing, set `seed` to `100,101,\ldots`, and the same student will get a definite division in the same repetition.

!!! warning "Small differences caused by Python subscripts"

    The code is written as `-N//5`. Python interprets it as \((-N)//5\), when \(N\) is not divisible by 5,
    The number of meta questions is equal to \(\lceil N/5\rceil\). Therefore, "about 80/20" is used here. The proportion of individual students will vary depending on the
    Rounding up is a slight change.

### 2.3 `collate_fn` becomes four dense tensors

A batch is organized into:

|Tensor|shape|meaning|
| --- | --- | --- |
| `input_labels` | \(B\times Q\) |Historical correctness of training candidates|
| `input_mask` | \(B\times Q\) |Which questions belong to the student's candidate set|
| `output_labels` | \(B\times Q\) |Historical correctness and incorrectness of meta questions|
| `output_mask` | \(B\times Q\) |Which questions belong to the student's meta set|

In the label tensor, incorrect answers and unobserved positions are written as 0; mask is responsible for distinguishing these two situations. This implementation facilitates element-wise
Multiplying the mask, the cost is that the memory grows with \(B\times Q\). Eedi-1 has 27,613 questions, and dense batches will occupy
Considerable CPU/GPU memory.

## 3. How does the code implement "choose the next question after each answer"

This is the key to understanding adaptability.

### 3.1 Three-valued response state

[`MAMLModel.reset`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/model.py#L66-L80)
First map the historical tag \(0/1\) to \(-1/+1\):

```python
obs_state = (input_labels - 0.5) * 2.0
train_mask = zeros(B, Q)
state = obs_state * train_mask
```

So the actual state seen by the strategy is

\[
x_{ij}^{(t)}=
\begin{cases}
+1,&\text{question}j\text{Selected and student}i\text{Correct answer},\\
-1,&\text{question}j\text{Selected and student}i\text{Wrong answer},\\
0,&\text{question}j\text{Not selected yet}.
\end{cases}
\]

`obs_state` already has historical answers to candidate questions in offline data; `train_mask` is like a mask, allowing only the currently selected
The answer to item enters the strategy.

### 3.2 Question-by-question closed loop

Approx path
[`pick_biased_samples`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/train.py#L95-L121)
Each step of is executed:

```python
state = model.step(env_states)
train_mask_sample, actions = st_policy.policy(state, action_mask)
action_mask[student_ids, actions] = 0
env_states["train_mask"] = train_mask + train_mask_sample.data
```

The process can be written as:

\[
x_i^{(t)}
\xrightarrow{\Pi_\phi}
j_i^{(t)}
\xrightarrow{\text{Query historical responses}}
Y_{i,j_i^{(t)}}
\xrightarrow{\text{write mask}}
x_i^{(t+1)}.
\]

After the item is selected in step \(t\), its \(+1/-1\) answer will enter the state in step \(t+1\). Correct and incorrect answers will form
In different states, strategies can give different next questions. The official implementation thus maintains the CAT structure of question-by-question real-time feedback.

!!! note "How to simulate on-site answers in offline experiments"

    The code can only select questions from the historical observed questions of `input_mask=1`. After selecting, directly from
    `input_labels` Query the answer, which is equivalent to playing back the student's past response matrix. During actual deployment, this query location should
    Replaced with "present the item to the student and wait for new responses". The strategy loop itself does not need to change.

### 3.3 What do the two masks do?

- `action_mask`: Questions that the student can still choose and have answers in offline data;
- `train_mask`: The question that has been selected in the current episode.

Topic logits plus

\[
\log m_j,\qquad m_j\in\{0,1\}.
\]

For optional questions, add \(\log 1=0\). For non-optional questions, add a value that is numerically approximate to \(-\infty\). After softmax, the probability is close to
0. After the item is selected, the corresponding position of `action_mask` is reset to zero to avoid repeated topic selection.

## 4. Response model: BiIRT and BiNN

### 4.1 Shared initialization and student local parameters

[`clone_meta_params`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/train.py#L19-L21)
Copy a global learnable vector to each student in the batch:

```python
meta_params[0]                 # [1, d]
    .expand(batch_size, -1)    # [B, d]
    .clone()
```

The corresponding relationship in the paper is:

\[
\texttt{meta\_params[0]}\leftrightarrow
\text{Global student parameter initialization},
\qquad
\texttt{new\_params[0]}\leftrightarrow
\theta_i^{(k)}.
\]

### 4.2 BiIRT

When `question_dim == 1`,
[`compute_output`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/model.py#L129-L135)
Return

```python
logit = student_embed - question_difficulty
```

That is

\[
g(j;\theta_i,\gamma)=\theta_i-b_j,
\qquad
p(Y_{ij}=1)=\sigma(\theta_i-b_j).
\]

`student_embed` is the local ability of each student updated in the inner layer, and `question_difficulty` is a global model parameter.
Updated by the outer optimizer.

### 4.3 BiNN

When `question_dim > 1`:

```python
h_i = Dropout(ReLU(Linear(theta_i)))
logits_i = Linear(h_i)  #Q logits of the questions
```

The student's partial representation \(\theta_i\in\mathbb R^d\) first passes through 256 hidden units, and then outputs the question \(Q\) at once
The answer logits. Each output coordinate is bound to a fixed item.

This structure can express more complex student-item interactions than 1PL, but also brings two limitations:

- The output layer size is bound to item bank \(Q\), and the new questions have no directly usable output nodes;
- The model does not have an item feature encoder and cannot rely on question stems or knowledge points to generate representations for cold-start questions.

## 5. Inner layer optimization row-by-row corresponding formula (6)

The core function is
[`inner_algo`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/train.py#L24-L35)：

```python
for _ in range(params.inner_loop):
    config["meta_param"] = new_params[0]
    res = model(batch, config)
    loss = res["train_loss"]
    grads = torch.autograd.grad(
        loss, new_params, create_graph=create_graph
    )
    new_params = [
        new_params[i] - inner_lr * grads[i]
        for i in range(len(new_params))
    ]
```

line by line correspondence

\[
\theta_i^{(k+1)}
=
\theta_i^{(k)}
-\alpha
\nabla_{\theta_i}
\mathcal L_i'
\left(\theta_i^{(k)};\,S_i\right).
\]

|code|mathematical meaning|
| --- | --- |
| `params.inner_loop` |\(K\), default 5 steps|
| `params.inner_lr` |\(\alpha\), local learning rate|
| `config["train_mask"]` |Currently selected collection \(S_i\)|
| `res["train_loss"]` |Selected question Binary cross-entropy \(\mathcal L_i'\)|
| `new_params[0]` |Student local parameters \(\theta_i^{(k)}\)|

`BCEWithLogitsLoss` directly receives logits and combines sigmoid and cross-entropy for calculation. `train_loss` for all selected questions
Sum; `output_loss` sums the meta questions of the batch and divides them by the number of students.

## 6. How to update γ and student initialization in the outer layer

With [`run_biased`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/train.py#L124-L144)
For example:

1. The strategy gradually obtains the final `train_mask`;
1. Copy each student’s `new_params` from shared initialization;
1. Use the final selected topic to do \(K\) step `inner_algo`;
1. Use the adapted student parameters to predict the meta question specified by `output_mask`;
1. `loss.backward()` updates response model and shared student initialization.

```python
inner_algo(batch, config, new_params)
res = model(batch, config)
loss = res["loss"]
loss.backward()
optimizer.step()
meta_params_optimizer.step()
```

`optimizer` is Adam responding to model parameters; `meta_params_optimizer` is SGD with shared student initialization.
Regular outer updates call `inner_algo(..., create_graph=False)`, so a first-order MAML-style approximation is used:
The gradient preserves a direct path from the final local parameters to the initialization, omitting the second derivative term of the inner layer gradient update.

## 7. Four topic selection paths

### 7.1 Random

[`pick_random_sample`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/model.py#L15-L21)
Use `torch.multinomial(..., replacement=False)` to extract \(n\) questions from the candidate questions at once. Then use the entire set of questions
Adapt to student parameters.

### 7.2 Active

[`pick_uncertain_sample`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/model.py#L119-L127)
Calculate

\[
s_{ij}=\min(p_{ij},1-p_{ij}),
\]

and select the maximum value. \(p_{ij}=0.5\) has the highest score, so this is the "choose difficulty closest to current ability" in 1PL
Uncertainty rules. Each time a question is selected, the code runs an inner update and then calculates the next question.

### 7.3 Unbiased: PPO path

[`ActorCritic`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/policy.py#L26-L85)
Contains actor and critic:

\[
x_i^{(t)}
\xrightarrow{\text{Linear}}
h_i^{(t)}
\xrightarrow{\text{Tanh MLP}}
\begin{cases}
\text{item logits},\\
V(x_i^{(t)}).
\end{cases}
\]

Actor is sampled from masked categorical distribution, `Memory` saves each step state, action, old
log probability and mask. After selecting all the questions \(n\),
[`run_unbiased`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/train.py#L67-L92)
Calculate code-level rewards per student:

\[
r_i
=
\operatorname{Accuracy}_{i,\text{policy}}
-
\operatorname{Accuracy}_{i,\text{random}}.
\]

The same endpoint reward is copied to every action in the episode. PPO uses probability ratio clipping, critic MSE and entropy
bonus, the default update is 4 epochs, and the clipping threshold is 0.2.

!!! warning "Thesis formula and reward writing method for open source implementation"

    The paper derives the score-function gradient from the outer loss; the open source code combines the "meta of relatively randomly selected topics"
    accuracy improvement” as a PPO reward. Both serve the same held-out prediction goal, but the numerical goal and
    The optimizer did not copy the paper formulas item by item. When reproducing a paper, it should be recorded whether the derivation version of the paper or the warehouse PPO version is used.

### 7.4 Approx: Code name `biased`

[`hard_sample`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/policy.py#L151-L156)
Implement straight-through one-hot:

```python
y_soft = softmax(logits)
index = argmax(y_soft)
y_hard = one_hot(index)
select = y_hard - y_soft.detach() + y_soft
```

When calculating forward:

\[
\texttt{select}=y_{\text{hard}},
\]

So only choose one question at each step. During backpropagation:

\[
\frac{\partial\,\texttt{select}}{\partial z}
=
\frac{\partial y_{\text{soft}}}{\partial z},
\]

The gradient can be passed from meta loss through softmax back to the policy parameters. This is where biased, low-variance approximation code falls.

In the training state, each time a question is selected, the following is executed:

```python
config["train_mask"] = previous_mask + train_mask_sample
inner_algo(..., create_graph=True)
meta_loss = model(batch, config)["loss"]
st_policy.update(meta_loss)
```

`create_graph=True` allows policy gradients to pass through the inner adaptation step. The strategy is updated individually at each topic selection step. Complete the entire article
After the sequence, the code redoes the inner adaptation using the hard mask, updating the response model and shared initialization.

!!! note "The code does not explicitly construct the Hessian inverse"

    The paper uses influence functions to explain Approx gradients and their low variance properties. The official implementation uses unrolled inner
    optimization plus straight-through estimator, automatic differentiation through the 5-step inner layer through PyTorch
    Update. There is no explicit calculation of \(H^{-1}\) or separate implementation of influence score in the repository.

## 8. The complete call chain of a training batch

```text
Dataset.__getitem__
  └─Each student is randomly selected 80% candidates / 20% meta
collate_fn
  └─ Construct input/output labels and masks
train_model
  ├─ random/active  → run_random
  ├─ unbiased       → run_unbiased → PPO.update
  └─ biased/Approx  → run_biased   → StraightThrough.update
         ├─ Strategies are selected question by question train_mask
         ├─ inner_algo: local adaptation to student parameters
         ├─ meta BCE: predict questions in output_mask
         └─ Update response model, shared initialization and corresponding strategy
test_model
  └─ Flatten all meta questions and calculate accuracy and AUC
```

From an algorithmic perspective, it can be compressed into the following pseudocode:

```python
for batch in students:
    candidates, meta = split_observed_answers(batch)
    state = all_unseen()

    for t in range(test_length):
        item = policy(state, available_items)
        answer = candidates[item]
        state = reveal(state, item, answer)

    local_student = adapt(global_init, selected_answers, steps=5)
    meta_logits = response_model(local_student)
    meta_loss = masked_bce(meta_logits, meta.answers)

    update_response_model_and_global_init(meta_loss)
    update_selection_policy(meta_loss_or_reward)
```

## 9. Validation, Testing and Early Stopping

[`data_split`](https://github.com/arghosh/BOBCAT/blob/e6b6245e23c1065ba8b8c56de5f051dfbcdd89ec/utils/utils.py#L38-L61)
First shuffle by student, then use adjacent folds as test and validation, and the remaining three folds as training:

\[
60\%\ \text{train}
+20\%\ \text{validation}
+20\%\ \text{test}.
\]

After each epoch, the code is repeatedly verified using several fixed seeds. Validation accuracy is updated when it reaches a new high
`best_epoch` and calculate test accuracy/AUC immediately. No new validation for more than `wait` epochs
accuracy recording stops.

accuracy is binarized at a 0.5 threshold; AUC uses `sklearn.metrics.roc_auc_score`. When evaluating, include all
All meta responses for students are flattened into a vector, so interaction-level metrics are reported.

!!! warning "Two points that should be improved when strictly reproducing"

    - `len(data)//5` will leave tail students who cannot be divided evenly by 5; these students always enter training and cannot enter
      validation/test. You can use `KFold` or `array_split` instead.
    - The code repeatedly checks test when validation hits a new high, and the best checkpoint is not saved/restored. more rigorous
      The process should only rely on validation to select checkpoints, and run test once after training.

## 10. Hyperparameter and real control items in code

|parameters|Code defaults|function|
| --- | ---: | --- |
| `inner_loop` | 5 |Number of gradient steps for each local adaptation \(K\)|
| `inner_lr` | 0.1 |Local adaptation step size \(\alpha\)|
| `lr` | \(10^{-4}\) |Response model Adam learning rate|
| `meta_lr` | \(10^{-4}\) |Shared student initialization SGD learning rate|
| `policy_lr` | \(2\times10^{-3}\) |PPO/straight-through strategy learning rate|
| `question_dim` | 4 |BiNN student local vector dimension|
| `n_query` | 10 |Fixed test length|

README lists `hidden_dim=256`, but `train.py` and `model.py` are not read
`params.hidden_dim`; the hidden layer is directly written to 256. The student vector dimension of BiNN is given by `--question_dim`
control. To verify the 256-dimensional student parameter settings reported in the paper, one needs to explicitly run
`--question_dim 256`, cannot rely on `--hidden_dim 256`.

## 11. Traditional IRT baseline `irt.py`

`irt.py` is independent of the two-tier training code. It first turns each answer into item one-hot plus student one-hot, using no intercept
Logistic regression jointly estimates item difficulty and training student ability:

\[
\operatorname{logit}p_{ij}=\theta_i-b_j.
\]

New student abilities updated with 1D root solver `brentq`. Active selects the question with the current predicted probability closest to 0.5 at each step.
Random selects questions directly. This file assumes the classic baseline functionality of IRT-Active/IRT-Random.

!!! warning "`policy_lr` is reused in the baseline file"

    The ability estimate derivative of `irt.py` treats `params.policy_lr` as the ability prior/regular strength, and traverses
    \(10,1,0.1,0.01,10^{-4},0\). It does not represent the neural topic selection strategy learning rate here. Read the experiment script or organize it
    Hyperparameters should be distinguished according to file context.

## 12. Conclusions supported by the official warehouse

This can be directly confirmed from the code:

1. The actions of BOBCAT are generated question by question, and the next step strategy input contains the true correctness or incorrectness of previously selected questions;
1. Offline experiments simulate real-time interaction through occlusion-revealing historical responses;
1. BiIRT and BiNN share the same two-layer training skeleton;
1. Unbiased uses PPO, Approx uses greedy hard action plus straight-through gradient;
1. The outer indicators come from meta responses not used for adaptation;
1. Fixed \(Q\) dimension status and action headers restricting cold start and cross-item bank migration of new questions.

The code also shows the unexplored engineering boundaries of the paper: relying on dense \(B\times Q\) tensors, using only question numbers and correct and incorrect,
Lack of content constraints and exposure control, the environment only plays back historical observations, and relies on the old version of PyTorch/Neptune interface.

## 13. Suggested revisions before reappearance

### Environment

The README only declares `torch==1.7.1`, and the source code also relies on NumPy, SciPy, pandas, scikit-learn and
Neptune. It is recommended to create a complete lock file and set the Neptune log as an optional dependency.

### Data and Evaluation

- Cover every student with a standard 50% discount;
- Fixed and saved student divisions, intra-student divisions and random seeds;
- only evaluate test on the final selected checkpoint;
- Report interaction-level and student-level indicators simultaneously;
- Record each question exposure, test paper overlap, content coverage and group differences.

### Model

- Explicitly write `question_dim`, hidden layer width and dropout into the configuration;
- Add unit tests for model, mask, inner gradient and policy branches;
- Use sparse/set representation to reduce large item bank memory;
- Introduce item encoder so that the strategy can score new questions based on item characteristics;
- Add content blueprint, exposure and stopping constraints to formal CAT.

### The most valuable diagnostic volume to print

- Each step policy entropy, top-\(k\) action probability and selected question number;
- The number of \(-1/0/+1\) in `state` and its consistency with `train_mask`;
- Whether each student only chooses from the questions of `input_mask=1`, and whether there are duplications;
- Each step of the inner layer train loss and \(\lVert\nabla_{\theta_i}\mathcal L_i'\rVert\);
- meta loss, accuracy, AUC and calibration;
- \(\lVert\nabla_\phi\mathcal J\rVert\) and
  \(\lVert\nabla_\gamma\mathcal J\rVert\)；
- PPO ratio, advantage, or straight-through soft/hard action;
- Exposure rate of each question, overlap rate of test papers among students, and content coverage.
