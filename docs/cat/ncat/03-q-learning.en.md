# Q-learning and experience playback: from a topic selection to a network update

Let’s temporarily put aside our attention on this page and only study one question:

> How does NCAT learn to choose the next question when it is known which questions the student has answered so far, and whether each question was answered correctly or incorrectly?

Q-learning is located inside NCAT’s Question Selector. It is not responsible for estimating student abilities; student abilities are still updated by response models such as IRT, NCDM, etc. Q-learning is responsible for comparing the **long-term value of each candidate question**.

The entire training chain is:

```text
Current answer history
    ↓
The Q network gives each question a long-term value
    ↓
Choose a question from legal candidates
    ↓
Read the student's historical answers to this question
    ↓
The response model updates the student parameters
    ↓
Calculate prediction loss on query question
    ↓
Negative loss as reward
    ↓
Put this interaction into the replay buffer
    ↓
Update Q network with TD target
```

The following is always the same small example, stringing together each letter and each step of calculation.

## 1. Start with a CAT interaction

### 1.1 First look at a complete interaction record

Assume that the item bank only has five questions:

\[
\mathcal J=\{q_1,q_2,q_3,q_4,q_5\}.
\]

Students have:

- Correct answer \(q_2\);
- Wrong answer \(q_5\);
- \(q_1,q_3,q_4\) has not been answered yet.

Before making a decision at step \(t\), the state mastered by the system is

\[
s_t=\{(q_2,1),(q_5,0)\}.
\]

Among them:

- \(s\) is state, that is, state;
- The subscript \(t\) indicates that the current is the \(t\) decision moment;
- \((q_2,1)\) indicates that the question \(q_2\) is correct;
- \((q_5,0)\) indicates that the answer to question \(q_5\) is wrong.

The current legal candidate question set is

\[
\mathcal A_t=\{q_1,q_3,q_4\}.
\]

Suppose NCAT chooses

\[
q_t=q_3.
\]

Offline logs show that the student's answer to \(q_3\) is 0. The system adds this answer to history:

\[
s_{t+1}
=
\{(q_2,1),(q_5,0),(q_3,0)\}.
\]

The response model uses these three selected questions to re-estimate the student parameters, and then obtains

\[
\mathcal L_{t}=0.42.
\]

NCAT uses the opposite of the query loss as a reward:

\[
r_t=-\mathcal L_t=-0.42.
\]

If the test is not over yet, then

\[
d_t=0.
\]

This step ultimately forms a transition:

\[
\left(
s_t,q_t,r_t,s_{t+1},d_t
\right)
=
\left(
s_t,q_3,-0.42,s_{t+1},0
\right).
\tag{1}
\]

**The meaning of each quantity in a transition**

|mark|full name|The value in the example|what does it mean|
|---|---|---|---|
| \(s_t\) | current state | \(\{(q_2,1),(q_5,0)\}\) |Answer history known before selecting the question|
| \(q_t\) | action | \(q_3\) |The real choice question in this step|
| \(r_t\) | reward | \(-0.42\) |Measurement quality obtained after selecting topics and updating students|
| \(s_{t+1}\) | next state |Then add \((q_3,0)\)|New status after student answers|
| \(d_t\) | done | 0 |Is the test over after this step?|

The student's answer to \(q_3\) is already included in \(s_{t+1}\), so the simplest transition is usually no longer saved separately for \(a_t\). In actual implementation, answers can also be saved additionally for debugging.

!!! tip "Be sure to remember the chronological order clearly"

    \(s_t\) is the state **before** the answer to \(q_t\); \(s_{t+1}\) is the state **after** the answer to \(q_t\). Q network uses \(s_t\) to decide \(q_t\) and cannot see \(s_{t+1}\) in advance.

### 1.2 reward What exactly is being rewarded?

The reward of NCAT at step \(t\) is defined as

\[
r_t
=
-\mathcal L_M
\left(
\mathcal D_i^u,\widehat\theta_i^{\,t}
\right).
\tag{2}
\]

Take it apart one by one:

|mark|meaning|
|---|---|
| \(i\) |Current training students|
| \(\mathcal D_i^u\) |query set of student \(i\)|
| \(\widehat\theta_i^{\,t}\) |Student parameters estimated using previously selected questions \(t\)|
| \(M\) |Response models such as IRT and NCDM|
| \(\mathcal L_M\) |The average BCE of the response model on the query question|
| \(r_t\) |query the opposite of BCE|

Assume that the results of the two topic selections are as follows:

|Topic selection for this step|Updated query BCE| reward |
|---|---:|---:|
|Select \(q_3\)| 0.42 | \(-0.42\) |
|Select \(q_4\)| 0.55 | \(-0.55\) |

Compare reward:

\[
-0.42>-0.55.
\]

Therefore, the result of this step of \(q_3\) is better. Although reward is a negative number, the size relationship is completely normal:

- The smaller the query loss is;
- The closer reward is to 0;
- The result is better.

**reward evaluates the accumulated selected questions**

Query loss at step \(t\) is used

\[
\mathcal D_i^s(t)
=
\{(q_1,a_1),\ldots,(q_t,a_t)\}
\]

Estimate students. Therefore, \(r_t\) evaluates "the measurement result of this set of questions so far", and does not only evaluate the effect of the isolated question \(t\).

The previous questions have changed the student parameters and current status, so the same question may get different rewards in different states.

## 2. How does the Q value represent the long-term value of topic selection?

### 2.1 Why should immediate reward and Q value be separated?

reward \(r_t\) only describes the result after **this topic selection**. The Q value also needs to consider what new state this question will bring the system to, and how other questions can be selected later.

Suppose there are currently two candidate actions.

**Path A: Now multiple choice question 3**

The reward for the next three steps is

\[
-0.42,\quad -0.30,\quad -0.24.
\]

**Path B: Now Multiple Choice 4**

The reward for the next three steps is

\[
-0.35,\quad -0.50,\quad -0.45.
\]

Looking only at the first step, path B's \(-0.35\) is greater than path A's \(-0.42\). But Path B puts students into a state where subsequent measurements are less effective.

Let the discount factor be

\[
\gamma=0.8.
\]

The discounted cumulative reward of path A is

\[
G_t^{A}
=
-0.42
+0.8(-0.30)
+0.8^2(-0.24)
=
-0.8136.
\]

The discounted cumulative reward of path B is

\[
G_t^{B}
=
-0.35
+0.8(-0.50)
+0.8^2(-0.45)
=
-1.038.
\]

because

\[
-0.8136>-1.038,
\]

When considering the entire subsequent path, it is better to choose \(q_3\).

This is the core motivation of Q-learning: **Compare long-term results when selecting topics, not just the immediate results of the next second. **

### 2.2 Define Q value from cumulative reward

The cumulative discount reward starting from step \(t\) is recorded as return:

\[
G_t
=
r_t
+\gamma r_{t+1}
+\gamma^2r_{t+2}
+\cdots
+\gamma^{T-t}r_T.
\tag{3}
\]

The action value function is defined as

\[
Q^\pi(s_t,q)
=
\mathbb E_\pi
\left[
G_t
\;\middle|\;
s_t,\ q_t=q
\right].
\tag{4}
\]

Substituting equation (3) back:

\[
Q^\pi(s_t,q)
=
\mathbb E_\pi
\left[
\sum_{k=t}^{T}
\gamma^{k-t}r_k
\;\middle|\;
s_t,\ q_t=q
\right].
\tag{5}
\]

**Formula (5) paragraph by paragraph translation**

|fragment|Chinese meaning|
|---|---|
| \(Q^\pi(s_t,q)\) |In the state \(s_t\), first select the topic \(q\), and then follow the strategy \(\pi\) The long-term value of the action|
| \(q_t=q\) |Force this step to choose multiple choice questions first \(q\)|
| \(\pi\) |Topic selection strategies to use from the next step|
| \(r_k\) |reward for step \(k\)|
| \(\gamma^{k-t}\) |Discount weight of reward at step \(k\)|
| \(T\) |test end step|
| \(\mathbb E_\pi\) |Averaging prospective student answers and subsequent question paths|

The reason for the expectation \(\mathbb E\) is that the future has not happened yet:

- Students may answer the next question correctly or incorrectly;
- Different answers will produce different states;
- Strategies may include random exploration or temperature sampling;
- Different future paths will produce different rewards.

The Q-value summarizes the long-term results of these possible paths into an expectation score.

### 2.3 Relationship between three types of Q notation

When reading papers and codes, I often see three ways of writing.

**The true value of a given strategy**

\[
Q^\pi(s,q)
\]

Represents the true expected value when the specified strategy \(\pi\) is followed.

**BEST VALUE**

\[
Q^*(s,q)
=
\max_\pi Q^\pi(s,q)
\]

Indicates the value that can be achieved when \(q\) is selected first in this step, and then the best topic selection method is always used.

**Approximation of neural network**

\[
Q_\phi(s,q)
\approx
Q^*(s,q).
\]

\(\phi\) is the neural network parameter. At the beginning of training, \(Q_\phi\) is basically a random prediction; after a large number of transition TD updates, it gradually approaches \(Q^*\).

**Look together with other scores in CAT**

|Quantity|who counts|numerical meaning|
|---|---|---|
| \(M(q\mid\theta)\) |response model|The probability that a student correctly answers question \(q\)|
|Fisher information| IRT criterion |The local measurement information provided by this question at a certain ability position|
| \(r_t\) |Offline training environment|The opposite number of query loss after updating in this step|
| \(Q_\phi(s_t,q)\) |NCAT topic selection network|The estimated long-term cumulative reward after choosing \(q\) now|

These four quantities can be ordered differently because they answer different questions.

### 2.4 How does the discount factor gamma affect long-term value?

The value range of \(\gamma\) is usually

\[
0\le\gamma\le1.
\]

It controls how much future reward accounts for the current Q value.

| \(\gamma\) |explain|
|---:|---|
| 0 |Only view this step reward|
| 0.5 |For each subsequent step further, the weight is multiplied by 0.5.|
| 0.8 |Retain more long-term information|
| 1 |All future steps are non-discounted|

Assuming that future rewards are all \(-0.4\), the three-step return is:

**When gamma equals 0**

\[
G_t=-0.4.
\]

**When gamma equals 0.5**

\[
G_t
=
-0.4+0.5(-0.4)+0.5^2(-0.4)
=
-0.7.
\]

**When gamma equals 1**

\[
G_t
=
-0.4-0.4-0.4
=
-1.2.
\]

!!! warning "NCAT Theory Goals and Code Discounts"

    The double-layer outer target of the paper adds equal weights to the query loss from steps 1 to \(T\), corresponding to the undiscounted target. If DQN is set to \(\gamma<1\), earlier steps will receive higher weight. The public shell example uses \(\gamma=0.8\), so when reproducing it you should treat \(\gamma\) as a hyperparameter that changes the target weight.

## 3. How does the Bellman equation break down long-term problems?

### 3.1 Where does Bellman’s recursion come from?

return can separate the first step:

\[
\begin{aligned}
G_t
&=
r_t+\gamma r_{t+1}+\gamma^2r_{t+2}+\cdots\\
&=
r_t+\gamma
\left(
r_{t+1}+\gamma r_{t+2}+\cdots
\right)\\
&=
r_t+\gamma G_{t+1}.
\end{aligned}
\tag{6}
\]

This sentence is very crucial:

> The long-term result from now = current reward + the long-term result of the next state after discount.

If the optimal action is adopted after the next step, the Bellman optimal equation is obtained:

\[
Q^*(s_t,q_t)
=
\mathbb E
\left[
r_t
+
\gamma
\max_{q'\in\mathcal A_{t+1}}
Q^*(s_{t+1},q')
\right].
\tag{7}
\]

**Each symbol in equation (7)**

|symbol|meaning|
|---|---|
| \(s_t\) |The status before selecting the topic in this step|
| \(q_t\) |Questions selected in this step|
| \(r_t\) |The reward the student gets after answering and updating the response model|
| \(s_{t+1}\) |The status after adding the real answer to this question|
| \(\mathcal A_{t+1}\) |The set of legal candidate questions for the next state|
| \(q'\) |A question that may be chosen next|
| \(\max_{q'}\) |Take the highest value among all legal questions in the next step|
| \(\gamma\) |Discount on next state value|
| \(\mathbb E\) |Get expectations for unknown student reactions and state transitions|

The Bellman equation allows us to study without having to wait for the entire test to be over. Each one-step transition can generate a training signal.

### 3.2 Q How does the network evaluate all questions at the same time?

NCAT's Q network inputs the current state \(s_t\) and outputs a vector with a length of item bank size:

\[
Q_\phi(s_t,\cdot)
=
\left[
Q_\phi(s_t,q_1),
Q_\phi(s_t,q_2),
\ldots,
Q_\phi(s_t,q_5)
\right].
\tag{8}
\]

Continuing the previous five-question example, assume that the network output

\[
Q_\phi(s_t,\cdot)
=
[-0.62,-0.31,-0.44,-0.28,-0.57].
\]

Currently \(q_2,q_5\) has been answered, so the legal set is

\[
\mathcal A_t=\{q_1,q_3,q_4\}.
\]

After blocking illegal questions:

\[
\widetilde Q_\phi(s_t,\cdot)
=
[-0.62,-\infty,-0.44,-0.28,-\infty].
\]

The maximum value is

\[
-0.28,
\]

Corresponding question \(q_4\). If the greedy strategy is currently adopted, choose

\[
q_t=q_4.
\]

"Max" here means closest to 0. Since rewards come from negative losses, questions with smaller long-term losses usually get larger Q values.

## 4. How does a transition update the Q network?

### 4.1 How to generate training data after selecting a question

Assume that \(q_4\) is selected in this step. The offline training environment is run in the following sequence.

**Step one: Query historical answers**

Student's historical answer to \(q_4\) is:

\[
a_t=1.
\]

**Step 2: Update status**

\[
s_{t+1}
=
s_t\cup\{(q_4,1)\}.
\]

**Step 3: Update student parameters**

The response model only uses the cumulative selected support questions:

\[
\widehat\theta_i^{\,t}
=
\arg\min_{\theta_i}
\sum_{(q,a)\in\mathcal D_i^s(t)}
\ell
\left(
a,M(q\mid\theta_i)
\right).
\]

**Step 4: Evaluate on the query set**

Assume query BCE is

\[
\mathcal L_t=0.35.
\]

**Step 5: Construct reward**

\[
r_t=-0.35.
\]

**Step Six: Judgment of Termination**

If the maximum number of questions has not been reached:

\[
d_t=0.
\]

**Step 7: Save to replay buffer**

\[
\left(
s_t,q_4,-0.35,s_{t+1},0
\right).
\]

So far, only one training experience has been generated. The next step is to convert this experience into the supervision target of the Q network.

### 4.2 TD target: Create a learning target for the current Q prediction

We don't know the real \(Q^*(s_t,q_t)\), so we can't get the label directly like ordinary supervised learning. TD learning uses the Bellman equation to make a temporary target:

\[
y_t
=
r_t
+
\gamma(1-d_t)
\max_{q'\in\mathcal A_{t+1}}
Q_{\bar\phi}(s_{t+1},q').
\tag{9}
\]

This \(y_t\) is called temporal-difference target, or TD target for short.

**Equation (9) explained item by item**

|item|meaning|
|---|---|
| \(y_t\) |Hopefully the current Q prediction is close to the target value|
| \(r_t\) |Really observed immediate reward|
| \(Q_{\bar\phi}\) |The target network used to make the target|
| \(\bar\phi\) |Parameters of target network|
| \(\max_{q'}\) |The highest estimated value among all legal actions in the next state|
| \(1-d_t\) |kill switch|

**Why is it called bootstrap**

Part of the target \(y_t\) comes from the real observed \(r_t\), and part of it comes from the model's own estimate of the next state:

\[
\underbrace{r_t}_{\text{real observation}}
+
\underbrace{
\gamma\max_{q'}Q_{\bar\phi}(s_{t+1},q')
}_{\text{Use existing estimates to push forward the next step}}.
\]

This kind of "using current estimates to help construct new learning goals" is called bootstrap.

### 4.3 done Why enter TD target?

If the test continues after this step:

\[
d_t=0,
\]

So

\[
1-d_t=1,
\]

The target contains the next state value.

If this step is already the last question:

\[
d_t=1,
\]

So

\[
1-d_t=0.
\]

At this time

\[
y_t=r_t.
\tag{10}
\]

There is no next question after termination, and continuing to add the next state Q value will create non-existent future rewards out of thin air.

### 4.4 A TD update is counted completely

Continuing with the example of selecting \(q_4\).

**Known quantity**

The current network’s prediction for the selected action is

\[
Q_\phi(s_t,q_4)=-0.28.
\]

Real instant reward is

\[
r_t=-0.35.
\]

Set

\[
\gamma=0.8,
\qquad
d_t=0.
\]

In the new status \(s_{t+1}\), \(q_4\) has also answered. Assume that the target network outputs the next state:

\[
Q_{\bar\phi}(s_{t+1},\cdot)
=
[-0.50,-0.40,-0.26,-0.33,-0.61].
\]

In the next state, only \(q_1,q_3\) is legal, so the mask is

\[
[-0.50,-\infty,-0.26,-\infty,-\infty].
\]

The maximum value among legal questions is

\[
\max_{q'\in\mathcal A_{t+1}}
Q_{\bar\phi}(s_{t+1},q')
=
-0.26.
\]

**Calculate TD target**

\[
\begin{aligned}
y_t
&=
r_t+\gamma(1-d_t)(-0.26)\\
&=
-0.35+0.8(1)(-0.26)\\
&=
-0.35-0.208\\
&=
-0.558.
\end{aligned}
\]

**Calculate TD error**

definition

\[
\delta_t
=
y_t-Q_\phi(s_t,q_t).
\]

Substitute the values:

\[
\delta_t
=
-0.558-(-0.28)
=
-0.278.
\]

**Calculate square loss**

\[
\mathcal L_t^{\mathrm{TD}}
=
\left(
y_t-Q_\phi(s_t,q_t)
\right)^2
=
(-0.278)^2
=
0.077284.
\tag{11}
\]

The current prediction \(-0.28\) is higher than the target \(-0.558\), so the gradient update will adjust the prediction of \(q_4\) in this state in a more negative direction.

**If this step has been terminated**

If

\[
d_t=1,
\]

rule

\[
y_t=-0.35.
\]

The loss at this time is

\[
\left(
-0.35-(-0.28)
\right)^2
=
0.0049.
\]

The goals of terminating and non-terminating transitions are different, and the code must handle `done` on a sample-by-sample basis.

### 4.5 Why only train the questions that are really selected this time?

The network outputs five Q-values at a time:

\[
Q_\phi(s_t,\cdot)
=
[-0.62,-0.31,-0.44,-0.28,-0.57].
\]

The real choice this time is \(q_4\). The environment only observes "what happens after selecting \(q_4\)", so this transition directly supervises:

\[
Q_\phi(s_t,q_4).
\]

The counterfactual results of the remaining four questions in this state did not occur and cannot be supervised by the same \(y_t\).

PyTorch uses `gather` to get the value corresponding to the actual action of each sample:

```python
all_q = online_net(state)                         # [B, J]
q_taken = all_q.gather(1, action[:, None])       # [B, 1]
q_taken = q_taken.squeeze(1)                     # [B]
```

Among them:

- \(B\) is the batch size;
- \(J\) is the item bank size;
- `action[b]` is the question number actually selected by transition \(b\).

### 4.6 Why does target network make training more stable?

If the same network does two things at the same time:

1. Generate the current prediction \(Q_\phi(s_t,q_t)\);
2. Generate the next state value in the learning goal;

Then every time the parameters are updated, the prediction and target will move at the same time. The model looks like it is chasing a target that is constantly moving quickly.

DQN copies a network that updates slowly:

|network|parameters|Purpose|
|---|---|---|
| online network | \(\phi\) |Generate current Q prediction, accept gradient updates|
| target network | \(\bar\phi\) |Calculate TD target, temporarily fixed|

**Hard Sync**

Updated every \(C\) times:

\[
\bar\phi\leftarrow\phi.
\]

For example, copy every 500 gradient steps.

**Soft Sync**

Make small movements with each step:

\[
\bar\phi
\leftarrow
\tau\phi+(1-\tau)\bar\phi,
\]

Among them, \(\tau\) often takes a very small number, such as 0.005.

The output of the target network should stop the gradient when calculating \(y_t\):

```python
with torch.no_grad():
    next_q = target_net(next_state)
```

The official NCAT repository snapshot does not have a separate target network. It should be retained faithfully when forking the warehouse; it is recommended to add and ablate it when building a more stable modern version.

## 5. How to organize training data for experience playback

### 5.1 What is stored in experience replay?

replay buffer is recorded as

\[
\mathcal B
=
\left\{
(s_t,q_t,r_t,s_{t+1},d_t)
\right\}.
\tag{12}
\]

It can be understood as a "transactive memory bank" with limited capacity.

When training a student, the following may occur:

```text
transition 1: empty state → select q2 → correct answer
Transition 2: Given that q2 is answered correctly → choose q5 → answered incorrectly
transition 3: It is known that q2 is correct and q5 is incorrect → choose q4 → answer correctly
transition 4: add q4 pair → select q1 → answer incorrectly and terminate
```

Continue adding transitions to the same buffer when training the next student. When the capacity is full, the oldest experience is removed.

A minimal implementation:

```python
from collections import deque
import random


class ReplayBuffer:
    def __init__(self, capacity):
        self.data = deque(maxlen=capacity)

    def add(self, state, action, reward, next_state, done):
        transition = (
            state,
            action,
            reward,
            next_state,
            done,
        )
        self.data.append(transition)

    def sample(self, batch_size):
        return random.sample(self.data, batch_size)

    def __len__(self):
        return len(self.data)
```

### 5.2 Why not train directly in the order of production?

Successive transitions are highly correlated.

For example, the adjacent status of the same student:

\[
s_{t+1}
=
s_t\cup\{(q_t,a_t)\}.
\]

They only differ by one answer; adjacent rewards are calculated on the same query set. If the network continuously only looks at this one trajectory of this student, the gradient will be overly affected by recent local data.

Experience replay random sampling:

\[
(s,q,r,s',d)\sim\mathcal B.
\]

A mini-batch can contain both:

- different students;
- Different test steps;
- Different correct/wrong answer combinations;
- different actions;
- Terminating and non-terminating transitions.

Experience replay brings three direct effects:

1. **Break up correlation**: Adjacent trajectories no longer enter the network continuously in the original order;
2. **Improve data utilization**: An expensive environment interaction can be extracted multiple times;
3. **Smooth update**: The gradient of a batch comes from multiple states instead of a local path.

!!! info "replay buffer does not create new answers"

    It only reuses transitions that have already occurred. Old logs are not overwritten—action combinations will not appear automatically due to experience replay, and offline support domain restrictions still exist.

### 5.3 How to update a mini-batch

Assume that \(B\) transitions are randomly extracted from the buffer:

\[
\left\{
(s_b,q_b,r_b,s'_b,d_b)
\right\}_{b=1}^{B}.
\]

Calculate separately for each sample:

\[
y_b
=
r_b
+
\gamma(1-d_b)
\max_{q'\in\mathcal A'_b}
Q_{\bar\phi}(s'_b,q').
\tag{13}
\]

Batch average TD loss:

\[
\mathcal L_{\mathrm{TD}}(\phi)
=
\frac1B
\sum_{b=1}^{B}
\left[
y_b-Q_\phi(s_b,q_b)
\right]^2.
\tag{14}
\]

Complete code skeleton:

```python
all_q = online_net(state)                          # [B, J]
q_taken = all_q.gather(1, action[:, None]).squeeze(1)

with torch.no_grad():
    next_q = target_net(next_state)                # [B, J]
    next_q = next_q.masked_fill(
        ~next_valid_mask,
        float("-inf"),
    )
    next_best = next_q.max(dim=1).values           # [B]
    next_best = torch.where(
        done,
        torch.zeros_like(next_best),
        next_best,
    )
    target = reward + gamma * next_best

loss = torch.nn.functional.mse_loss(
    q_taken,
    target,
)

optimizer.zero_grad()
loss.backward()
torch.nn.utils.clip_grad_norm_(
    online_net.parameters(),
    max_norm=5.0,
)
optimizer.step()
```

Note:

- The shape of `target` is `[B]`;
- The shape of `q_taken` should also be `[B]`;
- `next_valid_mask` belongs to \(s_{t+1}\), not \(s_t\);
- Sample `done=True` sets `next_best` to 0.

## 6. Legal action mask: both the current selection and future valuation must be legal.

Let the set of legal actions under state \(s\) be \(\mathcal A(s)\). The Q value after shielding is defined as

\[
\widetilde Q_\phi(s,q)
=
\begin{cases}
Q_\phi(s,q), & q\in\mathcal A(s),\\
-\infty, & q\notin\mathcal A(s).
\end{cases}
\tag{15}
\]

At the maximum value, \(-\infty\) will never win.

**First time: Select current action**

In \(s_t\), already answered \(q_2,q_5\):

\[
\mathcal A_t=\{q_1,q_3,q_4\}.
\]

The current behavioral strategy can only be chosen from these three questions.

**Second time: Calculate TD target**

If \(q_4\) is selected again in this step, the next legal set of states becomes

\[
\mathcal A_{t+1}=\{q_1,q_3\}.
\]

Therefore, the maximum value of bootstrap can only be calculated in \(q_1,q_3\).

**What constraints can mask express simultaneously**

In offline training, illegal questions usually include:

- Questions that the student has answered;
- Except for the student’s support, there are no questions for which historical answers can be queried;
- padding question number.

In formal deployment, you can also block:

- Questions that exceed the upper limit of the content category;
- Questions that are rival questions to the selected question;
- Questions that have reached the exposure quota;
- Questions that cannot be completed within the time budget;
- Questions that do not meet question type, language, or accessibility requirements.

A general function:

```python
def apply_action_mask(q_values, valid_mask):
    if q_values.shape != valid_mask.shape:
        raise ValueError("Q values and mask must have the same shape")

    if not valid_mask.any(dim=1).all():
        raise ValueError("Every active state needs a legal action")

    return q_values.masked_fill(
        ~valid_mask,
        float("-inf"),
    )
```

!!! warning "The next state mask is a high-risk implementation point"

    Just because a mask is used when selecting a behavioral topic does not mean that the TD target is automatically correct. If the next state maximum value comes from an answered question or a support question, the target will be based on a future action that cannot actually be executed. The TD target of the official warehouse snapshot only blocks question number 0, so reproduction and improved versions need to clearly record this difference.

## 7. Explore, exploit and test randomization

### 7.1 epsilon-greedy: How to actively explore during training

At the beginning of training, the Q network parameters are random and the highest Q value usually has no real meaning. If the current argmax is selected at each step, the model will repeatedly take a few early and accidentally high paths, making it difficult to collect the results of other actions.

epsilon-greedy is defined as

\[
q_t
=
\begin{cases}
\text{from}\mathcal A_t\text{Uniform random selection of topics},
& \text{Probability}\varepsilon,\\
\displaystyle
\arg\max_{q\in\mathcal A_t}
Q_\phi(s_t,q),
& \text{Probability}1-\varepsilon.
\end{cases}
\tag{16}
\]

**Probability examples of three legal questions**

Assumptions:

\[
|\mathcal A_t|=3,
\qquad
\varepsilon=0.30.
\]

There is a 30% probability of entering a random branch. Each of the three questions in the random branch accounts for one-third, so each question is obtained from the random branch.

\[
\frac{0.30}{3}=0.10.
\]

The current greedy question also gets a 70% deterministic branch. Therefore:

|item type|Probability of being selected|
|---|---:|
|Current maximum Q value question| \(0.70+0.10=0.80\) |
|Other legal questions 1| 0.10 |
|Other legal questions 2| 0.10 |

**How to schedule epsilon**

Common practices:

```text
Early training: epsilon close to 1, extensive exploration
Mid-training: epsilon gradually decreases
Late stage of training: epsilon is close to 0, mainly using learned strategies
```

Paper report \(\varepsilon\) decays from 1 to 0. The public code uses another stochastic action probability curve that varies with training count.

Regardless of taking a random branch or a greedy branch, the legal action mask must be applied first. Random exploration simply randomizes among legitimate candidates.

### 7.2 Temperature Sampling: How to Disperse Paths during Evaluation or Deployment

The NCAT paper converts the Q-values of legal questions into probabilities during the test phase:

\[
\Pr(q\mid s_t)
=
\frac{
\exp
\left(
Q_\phi(s_t,q)/\nu_t
\right)
}{
\displaystyle
\sum_{q'\in\mathcal A_t}
\exp
\left(
Q_\phi(s_t,q')/\nu_t
\right)
}.
\tag{17}
\]

\(\nu_t>0\) is temperature.

For stable calculation, you can first subtract the maximum Q value in legal questions. Assume that the Q values of the three legal questions are

\[
[-0.62,-0.44,-0.28].
\]

Subtract the maximum value \(-0.28\):

\[
[-0.34,-0.16,0].
\]

**Temperature equals 1**

\[
\exp([-0.34,-0.16,0])
\approx
[0.712,0.852,1].
\]

After normalization, it is approximately

\[
[0.278,0.332,0.390].
\]

All three questions have obvious probabilities and the paths are scattered.

**Temperature equals 0.2**

\[
\exp([-0.34,-0.16,0]/0.2)
\approx
[0.183,0.449,1].
\]

After normalization, it is approximately

\[
[0.112,0.275,0.613].
\]

The highest Q-value questions already account for the majority of the probability.

**Temperature equals 0.05**

The normalized probability is approximately

\[
[0.001,0.039,0.960].
\]

The selection almost degenerates into argmax.

**Thesis Temperature Scheduling**

Paper setting

\[
\nu_t=2^{-0.1t}.
\tag{18}
\]

The temperatures of several test steps are:

|test step|temperature|
|---:|---:|
| \(t=1\) |About 0.933|
| \(t=10\) | 0.5 |
| \(t=20\) | 0.25 |

The early stages of the test are more spread out, and the later stages are more focused on high Q-value questions.

Temperature sampling can reduce the average exposure, but the maximum exposure rate, content blueprint and item security still require hard constraint mechanisms.

### 7.3 The difference between epsilon and temperature sampling

Both generate random actions, but have different probability structures and usage phases.

|Contrast| epsilon-greedy | temperature softmax |
|---|---|---|
|main stage|Q network training|Thesis evaluation/deployment topic selection|
|random part|Uniformly random among legal questions|Still prefer questions with higher Q value|
|Core parameters| \(\varepsilon\) | \(\nu_t\) |
|Parameters become smaller|Reduce random branches|Probabilities are more concentrated around argmax|
|main purpose|Exploration state—action space|Spread test paths and item exposure|

For example, when the question with the second highest Q value is very close to the question with the highest Q value:

- epsilon random branch does not care how close the two are;
- temperature softmax will give a higher probability to the second-ranked question.

### 7.4 Distinguish gamma, epsilon and temperature at once

|parameters|questions it answers|where does it change|Whether to change TD target|
|---|---|---|---|
| \(\gamma\) |How much emphasis is placed on future rewards?| Bellman target |Yes|
| \(\varepsilon\) |What is the probability of random exploration during training?|training behavioral strategies|No direct changes to the formula|
| \(\nu_t\) |How sharp does the Q value translate into the probability of selecting a topic?|Evaluation/deployment action distribution|No direct changes to the formula|

You can remember three sentences:

- \(\gamma\) controls "how much it will be worth in the future";
- \(\varepsilon\) is responsible for "trying many untravelled roads during training";
- \(\nu_t\) controls "how concentrated the probability of selecting questions is when administering the test".

## 8. Put all steps back into NCAT

### 8.1 A student’s entire training trajectory

Connecting all the previous parts, a history student's episode is as follows.

```text
Initialize empty state s1
Initialize legal support candidate set A1
Reset the student's local parameters

Step 1:
    Q network read s1
    epsilon-greedy selects q1 from A1
    Environmental reading q1 historical answers
    form s2
    The response model updates student parameters with selected questions
    Calculate loss in the query set and get r1
    store (s1, q1, r1, s2, done1)

Step 2:
    Q network read s2
    Legal set delete q1
    Select q2
    Read the real answer and form s3
    Update student parameters and query reward
    store (s2, q2, r2, s3, done2)

Continue until stopped:
    done = True for the last transition

If the replay buffer samples are enough:
    Randomly draw mini-batch
    Calculate masked TD target
    Update online Q network
    Synchronize target network on schedule
```

Note that the status read at each step of the strategy already contains the student’s actual feedback from the previous question. Therefore, even if two students have the same first two questions, as long as the answers to a certain step are different, the subsequent Q vector and item paths may bifurcate.

### 8.2 At which step are training and real testing separated?

**Offline training**

Offline environments have access to historical logs and held-out query answers, so they can:

- Query historical responses to selected support questions;
- Calculate query BCE;
- Construct reward;
- save transition;
- Updated Q network.

**Real implementation test**

When new students are deployed:

- The answers to the next questions are submitted in real time by students;
- System updates status and student parameters;
- Q network reselects the next question;
- No hidden query truth value;
- Do not calculate training reward;
- No replay buffer or TD updates required.

The trained \(Q_\phi\) has encoded the topic selection rules in historical data into parameters. The deployment phase only executes the policy.

## 9. More stable DQN version

### 9.1 What is Double DQN changing?

The maximum value of the next state of ordinary DQN is

\[
\max_{q'}
Q_{\bar\phi}(s_{t+1},q').
\]

The same set of noisy values participates in both "picking the largest one" and "evaluating the largest one", which is prone to max bias.

Double DQN separates the two tasks.

**online network is responsible for selecting question numbers**

\[
q^{\mathrm{select}}
=
\arg\max_{q'\in\mathcal A_{t+1}}
Q_\phi(s_{t+1},q').
\tag{19}
\]

**target network is responsible for evaluating this question**

\[
y_t
=
r_t
+
\gamma(1-d_t)
Q_{\bar\phi}
\left(
s_{t+1},
q^{\mathrm{select}}
\right).
\tag{20}
\]

The action mask must be applied before argmax in (19). Double DQN mainly improves the valuation bias and stability of Q-learning without changing the status representation, query reward or question-by-question feedback structure of NCAT.

### 9.2 A more stable NCAT-DQN training configuration

It is recommended to implement and unit test the following components separately:

1. **online Q network**: Read the correct/wrong answer status and accept the gradient;
2. **target Q network**: slow synchronization, making TD target;
3. **response model**: Update student parameters with accumulated selected questions;
4. **offline environment**: Read historical answers and calculate query reward;
5. **replay buffer**: save the transition and randomly select batches;
6. **current valid mask**: controls the behavior of this step;
7. **next valid mask**: Control the maximum bootstrap value;
8. **epsilon schedule**: training exploration;
9. **temperature schedule**: evaluation or deployment randomization;
10. **gradient clipping**: Limit the gradient explosion caused by abnormal TD error;
11. **checkpoint**: Save network, target, optimizer and training counts at the same time.

## 10. Implementation inspection and final summary

### 10.1 The most common implementation errors

**Mistake 1: Treating the Q value as the probability of correct answer**

Check if: Q network is forced through sigmoid. Standard DQN output usually does not require a sigmoid; the Q value can be any real number.

**Mistake 2: Reverse the reward symbol**

NCAT was originally defined as

\[
r_t=-L_t.
\]

If positive BCE is used directly, maximizing reward will bias towards larger prediction loss.

**Error 3: Query question enters student parameter update**

query can only be used for outer evaluation. If the query answer participates in the estimation of \(\widehat\theta_i^{\,t}\), information leakage will occur in reward.

**Error 4: The current action is masked, but the maximum value of the next state is not done**

This will make the TD target rely on questions that have been answered or have no historical answers.

**Mistake 5: Terminating sample is still bootstrap**

For `done=True`:

\[
y_t=r_t.
\]

**Error 6: The target does not stop the gradient**

The branch where the target is made should be placed in `torch.no_grad()`.

**Mistake 7: The training status contains the answer to this question in advance**

When selecting \(q_t\), the input must be \(s_t\), and the answer can only appear in \(s_{t+1}\).

**Error 8: `gather` got the wrong question number**

The one-to-one correspondence between `action` and `q_taken` of each batch sample should be checked, and whether the question number starts from 0 or 1 should be unified.

**Error 9: The legal collection is empty**

If the hard constraint blocks all questions, `argmax` will be meaningless. Deployment systems need to detect constraint feasibility in advance and design fallbacks.

### 10.2 Complete mental model after reading this page

Q-learning makes four layers of connections in NCAT:

1. **One real answer** Change \(s_t\) into \(s_{t+1}\);
2. **Response model and query set** turn the new state into reward \(r_t\);
3. **Bellman target** synthesizes the immediate reward and the next state value into \(y_t\);
4. **TD loss and replay** allow the Q network to gradually learn the value of long-term topic selection.

The core updates can be condensed into:

\[
\boxed{
\text{current forecast}
\quad
Q_\phi(s_t,q_t)
\quad
\longleftarrow
\quad
\underbrace{r_t}_{\text{Current measurement result}}
+
\underbrace{
\gamma(1-d_t)
\max_{q'\in\mathcal A_{t+1}}
Q_{\bar\phi}(s_{t+1},q')
}_{\text{Value of future topic selection}}
}
\]

\(s_{t+1}\) contains the answers just submitted by students, so this update is always based on a closed loop of real-time feedback on a question-by-question basis.

The next page goes inside the Q network and explains how it encodes correct and incorrect answers into state vectors: [State encoding and dual-channel attention](04-neural-encoder.md).
