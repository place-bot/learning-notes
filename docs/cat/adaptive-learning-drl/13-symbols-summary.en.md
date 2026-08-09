# Symbol table, conclusion and reading map

## 1. Main symbols

|symbol|meaning|
|---|---|
| \(\mathcal S\) |state space|
| \(s,s'\) |Current state and next state|
| \(S^{(t)}\) |Step \(t\) state random variable|
| \(\mathcal A\) |action space|
| \(a,a'\) |Current action and candidate next action|
| \(A^{(t)}\) |Step \(t\) action random variable|
| \(\mathcal P(s'\mid s,a)\) |state transfer kernel|
| \(\mathcal R(s,a,s')\) |reward function|
| \(r,R^{(t)}\) |Reward value and reward random variable|
| \(\gamma\) |discount factor|
| \(\pi\) |Material selection strategy|
| \(Q^\pi(s,a)\) |Action value under strategy \(\pi\)|
| \(Q^*(s,a)\) |optimal action value|
| \(\widehat Q(s,a;\mathbf w)\) |DQN approximation to the optimal Q value|
| \(\mathbf w\) |DQN parameters|
| \(D\) |Ability dimension|
| \(L\) |Material quantity|
| \(\boldsymbol\theta\) |latent ability vector|
| \(\widehat{\boldsymbol\theta}\) |Estimating ability|
| \(h_d\) |Target capability of dimension \(d\)|
| \(\mathbf1_D\) |\(D\) Dimension 1 target vector|
| \(\|\cdot\|_\infty\) |The maximum value of the absolute value of a vector component|
| \(\Delta\boldsymbol\theta\) |Ability increment after one round of learning|
| \(\varepsilon\) |epsilon-greedy exploration probability|
| \(\alpha\) |DQN learning rate|
| \(\mathcal H\) |Historical experience replay pool|
| \(\mathcal M\) |An updated mini-batch|
| \(M\) |mini-batch size|
| \(E\) |Number of training episodes|
| \(y\) | Bellman/TD target |
| \(\delta\) |TD error|
| \(\psi_v(s,a)\) |Next state prediction of transition model|
| \(v\) |transition model parameters|
| \(b_t(\theta)\) |belief or posterior distribution of potential states|

## 2. Main line of formula

### Measurement

\[
\Pr(U=u\mid\boldsymbol\theta)
=
f(\boldsymbol\theta,\boldsymbol\eta,u).
\]

### Status and Action

\[
s=\boldsymbol\theta\in[0,1]^D,
\qquad
a\in\{1,\ldots,L\}.
\]

### Transfer

\[
s'\sim\mathcal P(\cdot\mid s,a).
\]

### Reward

\[
r
=
\begin{cases}
-1,
&
\|s'-\mathbf1_D\|_\infty\ge10^{-3},
\\
0,
&
\|s'-\mathbf1_D\|_\infty<10^{-3}.
\end{cases}
\]

### Q function

\[
Q^\pi(s,a)
=
\mathbb E
\left[
\sum_{t=0}^{\infty}
\gamma^tR^{(t)}
\mid
S^{(0)}=s,
A^{(0)}=a;
\pi
\right].
\]

### Bellman equation

\[
Q^*(s,a)
=
\mathbb E
\left[
R+\gamma\max_{a'}Q^*(S',a')
\mid s,a
\right].
\]

### TD target

\[
y
=
r+\gamma\max_{a'}\widehat Q(s',a';\mathbf w).
\]

The termination status uses \(y=r\).

### transition model

\[
\widehat s'=\psi_v(s,a),
\]

\[
\min_v
\sum_i
\|\psi_v(s_i,a_i)-s_i'\|_2^2.
\]

## 3. Algorithmic closed loop of the paper

```text
current ability estimate
    │
    ▼
DQN calculates the long-term value of all materials
    │
    ▼
epsilon-greedy Select a material
    │
    ▼
Real students learn, or the transition model generates the next state
    │
    ▼
If the target is not met, you will get -1; if you meet the target, you will get 0.
    │
    ▼
transition into replay buffer
    │
    ▼
TD Update DQN
    │
    └────────► Next round of re-decision
```

## 4. Six core conclusions

1. Adaptive learning is a closed-loop sequence decision-making problem, and each round of feedback will change the next action.
2. Continuous capability vectors provide fine-grained status to DQN and can be measured by IRT/MIRT.
3. Each step \(-1\) turns "reaching the goal as quickly as possible" into maximizing long-term returns.
4. DQN uses Bellman target to learn from transfer samples and does not require knowing the real transfer kernel in advance.
5. The transition model can reuse a small amount of real student data, but it will introduce model bias and long trajectory errors.
6. The results of the paper come from two-dimensional artificial simulation, and the actual effectiveness of education still requires offline causal evaluation and online testing.

## 5. Quick check of experimental numbers

|item|result|
|---|---|
| DQN reward | \(-13.49\pm4.59\) |
|heuristic reward| \(-21.55\pm4.76\) |
|random reward| \(-24.85\pm5.59\) |
|About the number of episodes required for stability|about 600|
|transition model test \(R^2\)| 0.95–0.97 |
|transition model RMSE| 0.08–0.11 |
|virtual model obviously favorable range|No more than about 200 real students|

These numbers belong to the simulated environment set in the paper.

## 6. From thesis to research questions

If this paper is used as the starting point for generative CAT or educational recommendation research, it can be advanced along four levels:

### Status layer

- Point estimation is upgraded to posterior distribution;
-Incorporate response history, material history, time and fatigue;
- Use sequence models or large models to represent semantic states.

### Action layer

- Expand from material numbering to semantic content;
- Generate candidate questions or candidate materials;
- Guaranteed feasibility through mask, shadow test or constrained optimization.

### Target layer

- Learning gain;
- Measurement accuracy;
- Content balance;
- Study time;
- Cognitive load;
- Exposure, fairness and safety.

### Evaluation layer

- Simulation verification;
- Offline strategy evaluation;
- transition model calibration;
- Small traffic online test;
- Long-term retention and migration.

## 7. Recommended cross-topic reading

- [NCAT: Q-learning for question-by-question CAT strategies](../ncat/index.md)
- [BOBCAT: Double-layer optimization learning CAT topic selection](../bobcat/index.md)
- [CAT Overview](../index.md)
- [Reference for this topic](references.md)

## 8. Final image

\[
\boxed{
\begin{aligned}
\text{student feedback}
&\longrightarrow
\text{ability measurement}
\\
&\longrightarrow
\text{Closed Loop Materials Strategy}
\\
&\longrightarrow
\text{real ability changes}
\\
&\longrightarrow
\text{Feedback and re-planning again}.
\end{aligned}
}
\]

The core product of the paper is a decision rule that can be called repeatedly. The learning sequence that students actually experience is generated by this rule together with round-by-round authentic feedback.
