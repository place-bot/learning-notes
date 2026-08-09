# Two-tier goals, MDP and rewards

The main line of mathematics in NCAT can be condensed into one sentence:

> Select a small group of questions to estimate students, so that the estimated response model can accurately predict query questions that are not used for estimation; write the query prediction quality of each step as reward, and then use reinforcement learning to train the question selection strategy.

## 1. Binary cross-entropy

For the real answer \(a\in\{0,1\}\) and the predicted correct answer probability \(p\), the single-question binary cross-entropy is

\[
\ell(a,p)
=
-a\log p-(1-a)\log(1-p).
\]

If the student answers correctly and the model gives \(p=0.8\), then

\[
\ell(1,0.8)=-\log 0.8\approx 0.223.
\]

If the answer is still correct but the model only gives \(p=0.2\), then

\[
\ell(1,0.2)=-\log 0.2\approx 1.609.
\]

The smaller the loss, the more accurate the response prediction of the current student parameters to this question is.

## 2. Inner layer: Use selected questions to estimate current students

At step \(t\), the global item parameters of the response model are pretrained and frozen. The local parameters of student \(i\) are estimated by the cumulative support answers:

\[
\widehat\theta_i^{\,t}
=
\arg\min_{\theta_i}
\sum_{(q,a)\in\mathcal D_i^s(t)}
\ell\!\left(a,M(q\mid\theta_i)\right).
\tag{1}
\]

The input here only contains questions for which the answer has actually been selected and revealed. As \(t\) increases, \(\mathcal D_i^s(t)\) expands, and the student parameters are updated accordingly.

!!! info "What is the inner layer doing?"

    It answers: After having asked these questions and obtained these answers so far, what does the response model think this student's ability or knowledge mastery status is?

## 3. Outer layer: Evaluate the quality of generalization measurement at each step

The query set average loss of student \(i\) is defined as

\[
\mathcal L_M
\!\left(
\mathcal D_i^u,\widehat\theta_i^{\,t}
\right)
=
\frac{1}{|\mathcal D_i^u|}
\sum_{(q,a)\in\mathcal D_i^u}
\ell\!\left(a,M(q\mid\widehat\theta_i^{\,t})\right).
\tag{2}
\]

NCAT keeps the query loss low at each test step:

\[
\pi^*
=
\arg\min_{\pi}
\frac{1}{n}
\sum_{i=1}^{n}
\sum_{t=1}^{T}
\mathcal L_M
\!\left(
\mathcal D_i^u,\widehat\theta_i^{\,t}
\right),
\tag{3}
\]

Among them, \(\widehat\theta_i^{\,t}\) is constrained by formula (1), and \(\mathcal D_i^s(t)\) is gradually selected by the strategy \(\pi\).

Adding the losses over all \(t=1,\ldots,T\) has a practical implication: the test may stop at any step, so the strategy cannot perform well only at the last step.

## 4. Division of labor among three types of losses

Three losses often occur simultaneously in NCAT:

```text
support BCE
    │ Estimating student parameters
    ▼
Current θ_hat
    │ Predict on query question
    ▼
query BCE
    │ Take the opposite number
    ▼
reward
    │Construct Bellman target
    ▼
TD MSE
    │ Update
    ▼
Q network parameters φ
```

|loss|Optimization object|usage data|function|
|---|---|---|---|
| support BCE |Student local parameters \(\theta_i\)|Selected support question|Adapt the response model to the student|
| query BCE |Evaluation signals for topic selection strategies|held-out query question|Measure whether the selected questions help generalization|
| TD MSE |Q network parameters \(\phi\)| replay transition |Approaching long-term action value|

Confusing the three into one "model loss" will obscure the algorithm structure.

## 5. From minimizing loss to maximizing reward

Define step \(t\) reward:

\[
r_i^t
=
-\mathcal L_M
\!\left(
\mathcal D_i^u,\widehat\theta_i^{\,t}
\right).
\tag{4}
\]

Therefore, equation (3) can be written as maximizing the expected cumulative return:

\[
\max_\pi
\mathbb E_{i,\pi}
\left[
\sum_{t=1}^{T} r_i^t
\right].
\tag{5}
\]

Because the query BCE is non-negative, the reward defined in the paper is usually non-positive. "Better action" means reward is closer to 0.

!!! warning "reward is the opposite of absolute loss"

    The paper uses \(r_i^t=-\mathcal L_t\) and does not use the loss improvement amount \(\mathcal L_{t-1}-\mathcal L_t\). Therefore adjacent rewards are highly correlated. When doing follow-up research, you can compare designs such as absolute loss, loss reduction, posterior shrinkage of ability, and decision risk.

## 6. Written as MDP

A Markov decision process is denoted as

\[
\langle\mathcal S,\mathcal A,P,R,\gamma\rangle.
\]

In NCAT:

### Status

\[
s_t
=
\{(q_1,a_{i(1)}),\ldots,(q_{t-1},a_{i(t-1)})\}.
\tag{6}
\]

When implemented, it is usually split into a sequence of wrong answers and a sequence of correct answers, and is equipped with a padding mask.

### Action

\[
q_t\in\mathcal A_i^t.
\tag{7}
\]

Action is a legitimate candidate question. Answered questions, support questions, and questions that violate hard constraints must be masked.

### State transfer

After the student answered \(q_t\):

\[
s_{t+1}=s_t\cup\{(q_t,a_{i(t)})\}.
\tag{8}
\]

The uncertainty of transfer mainly comes from students' answers to the items.

### Reward

The reward is given by Equation (4). It is computed via query ground truth during offline training.

### Discount

\[
G_t
=
r_t+\gamma r_{t+1}
+\gamma^2r_{t+2}+\cdots.
\tag{9}
\]

\(\gamma\in[0,1]\) controls the weight of subsequent rewards.

## 7. Theoretical goals are similar to DQN training

Equation (5) gives equal weight to reward at each step, corresponding to the undiscounted cumulative return. If the DQN implementation uses \(\gamma<1\), it actually approximates

\[
\mathbb E_\pi
\left[
\sum_{t=1}^{T}
\gamma^{t-1}r_t
\right],
\tag{10}
\]

thus placing more emphasis on earlier rewards. This is a training approximation and also changes the weight target.

The public shell example is set to \(\gamma=0.8\), and the effective discount is also written in the epoch-related attenuation form in the warehouse. When reproducing the experiment, you should also report:

- Whether the outer objectives of the paper are equally weighted;
- \(\gamma\) actually used by the code;
- Whether there is additional epoch scheduling;
- Whether to reset the bootstrap item to zero when terminating the transition.

## 8. Why choose Q-learning

The question selection action is a discrete question number, and the value of a certain step depends on what else can be asked later. It is very difficult to directly backpropagate all discrete choice paths step by step. Q-learning decomposes long-term optimization into local TD updates through Bellman recursion:

\[
Q^*(s_t,q_t)
=
\mathbb E
\left[
r_t+\gamma\max_{q'\in\mathcal A_{t+1}}
Q^*(s_{t+1},q')
\right].
\tag{11}
\]

The next page will explain each item [Q-learning, TD target, experience playback and exploration](03-q-learning.md).
