# Limitations, CAT interface and future work

## 1. The fundamental difference between this paper and CAT

Both types of systems make decisions step by step, but the objects changed by the actions are different.

### Adaptive learning

\[
\boldsymbol\theta_{t+1}
\sim
\mathcal P(
\cdot
\mid
\boldsymbol\theta_t,
a_t^{\text{material}}
).
\]

Teaching actions are designed to change real abilities.

### CAT

Classic CAT often assumes that ability is approximately fixed over the short test period:

\[
\boldsymbol\theta_{t+1}
\approx
\boldsymbol\theta_t.
\]

item \(q_t\) changes the system’s knowledge of capabilities:

\[
p(\boldsymbol\theta\mid H_{t+1})
\propto
p(y_t\mid q_t,\boldsymbol\theta)
p(\boldsymbol\theta\mid H_t).
\]

Therefore:

- Educational changes in the environmental state of adaptive learning;
- A measured change in the information status of the CAT.

## 2. How to combine two layers of closed loops

A complete intelligent learning system can be written as:

```text
Material strategy π_material
    │Choose study materials
    ▼
Changes in students’ real abilities
    │
    ▼
CAT strategy π_item measured item by item
    │ Estimating new capabilities and uncertainties
    ▼
Material strategy decision again
```

The two layers should be evaluated separately:

|layer|main goal|Common indicators|
|---|---|---|
|CAT measurement layer|Few questions, accurate estimates|bias, RMSE, coverage, length|
|Learning recommendation layer|Effective and rapid growth|Learning gain, time to target, load, exit|

The high accuracy of the measurement layer cannot alone prove that the teaching strategy is effective; the high simulation reward of the teaching strategy cannot prove that the ability estimate is unbiased.

## 3. Comparison with NCAT

|item|This article| NCAT |
|---|---|---|
|Status|continuous capability point estimation|Selected questions and correct/wrong answer history|
|action|study materials|test questions|
| reward |Each step that fails to meet the standard \(-1\)|held-out query The opposite of prediction loss|
|end point|ability to achieve goals|Fixed or given test length|
|transfer|Learning leads to changes in ability|New answer written into history|
|data|Artificial simulated students|Real historical response logs|
|network| MLP DQN |Dual-channel attention Q network|

The common denominator is that each step recalculates the action based on new feedback. The Q-value semantics learned by the two are different.

## 4. Comparison with BOBCAT

|item|This article| BOBCAT |
|---|---|---|
|Decision object|study materials|test questions|
|learning algorithm|DQN and TD|Two-layer optimization and meta-gradient|
|external evaluation|Number of steps to reach goal|Meta question prediction loss|
|student parameters|as status input|The inner layer adapts to obtain local parameters|
|environment model|Learnable transition model|The historical response matrix provides feedback on topic selection.|

The goals of BOBCAT and NCAT focus on "testing accurately"; this article focuses on "learning fast".

## 5. Limitations of point estimation state

The status of the paper is:

\[
s_t=\widehat{\boldsymbol\theta}_t.
\]

A student with the same two point estimates is likely to have:

- Different posterior variance;
- Different recent material histories;
- Different fatigue and motivation;
- Different prerequisite knowledge structures.

These differences affect the yield of the next material. Can be expanded to:

\[
s_t
=
\left(
\widehat{\boldsymbol\theta}_t,
\operatorname{Cov}(\boldsymbol\theta_t\mid H_t),
h_t,
f_t
\right).
\tag{1}
\]

## 6. POMDP expression

When the true latent ability cannot be directly observed, it can be defined:

- Hidden state \(S_t=\boldsymbol\theta_t\);
- Action \(A_t\) is learning material;
- Observe \(O_t\) for answers, response time and behavior;
- Observation model \(\mathcal Z(o_t\mid s_t)\);
- belief \(b_t(s)=\Pr(S_t=s\mid H_t)\)。

Strategy uses belief:

\[
a_t=\pi(b_t).
\tag{2}
\]

In the conclusion, the author clearly lists POMDP as a future research direction.

## 7. No regression assumption

\[
\theta_d^{(t+1)}
\ge
\theta_d^{(t)}
\]

The simulation is simplified and also excludes:

- forget;
- fatigue;
- interference;
- long intervals;
- Measurement regression.

Transfers with time intervals are available:

\[
\boldsymbol\theta_{t+1}
\sim
\mathcal P(
\cdot
\mid
\boldsymbol\theta_t,
a_t,
\Delta t_t
).
\tag{3}
\]

## 8. Group homogeneity

The paper treats a group of learners as sharing the same MDP. In reality, material effects can be affected by:

- Previous courses;
- Age and language;
- learning strategies;
- Barriers and accessibility needs;
- interests and preferences;
- Teacher support.

The author proposes to group learners first and then learn strategies for each group. More flexible solutions are hierarchical transition models or strategies with individual embedding.

## 9. transition model error

One-step predictor:

\[
R^2,\quad\operatorname{RMSE}
\]

Mainly evaluate local fitting. Policies care about long trajectories and action sequencing. Also evaluate:

- \(k\)-step rollout error;
- policy value error；
- Action condition calibration;
- Uncertainty coverage;
- Out-of-distribution state detection.

## 10. Only use simulated data

Both experiments in the paper are based on artificial beta transfer. The result proves that the algorithm is feasible in this environment, but it still lacks:

- Real log external validation;
- Online learning gains;
-Teacher and student acceptability;
- Educational side effects;
- Long-term retention and migration.

The author lists research on authentic online learning platforms as a top future direction.

## 11. Narrow reward target

Each step \(-1\) optimizes the number of material rounds. In reality a round might be a 5 minute practice session or a 90 minute session. The more direct time cost is:

\[
r_t=-\operatorname{minutes}(a_t).
\tag{4}
\]

Multi-target version can add:

\[
r_t
=
-\text{time}
-\lambda_1\text{load}
-\lambda_2\text{dropout risk}
+\lambda_3\text{retention}.
\tag{5}
\]

Weighting requires educational value judgment and empirical calibration.

## 12. Offline logs and causal identification

Material in the history log is selected by the old strategy. Observed:

\[
(s_t,a_t,s_{t+1}),
\]

But you can't see the results of the same student choosing other materials at the same time. The transition model learns data with a selection mechanism.

Need to check:

\[
\mu(a\mid s)>0
\]

Whether it is true in the state action area that the target policy will access. In the absence of overlap, neural networks can only extrapolate.

Follow-up directions include:

- Conservative offline RL;
- Causal and dynamic treatment rules;
- doubly robust off-policy evaluation；
- Random exploration or micro-random trials;
- Security policy improvements under teacher constraints.

## 13. Preference and educational effectiveness

The conclusion of the paper proposes to combine recommendation methods such as collaborative filtering and matrix decomposition with DRL. The value can be broken down into:

\[
Q_{\text{total}}
=
Q_{\text{learning}}
+\lambda Q_{\text{preference}}.
\tag{6}
\]

Preference helps engagement and persistence, but high preference does not necessarily lead to high learning gains. Multi-objective designs should report both.

## 14. Future work proposed by the authors

The papers list:

1. Evaluation on real online learning platforms;
2. Model the learning process directly from the reaction history to reduce the independent ability estimator;
3. Group learners first and then learn group strategies;
4. Integrate collaborative filtering and matrix decomposition to take into account optimization and preference;
5. Compare DQN, heuristics and random strategies under more scenarios and constraints;
6. Establish POMDP;
7. Incorporate modeled learning paths into historical states.

## 15. Interface for generative recommendation

Generative models can propose candidate learning paths or new material combinations, but real-time systems still need to perform in a closed loop:

\[
a_t
\sim
\pi_\phi(
\cdot
\mid
H_t,
\text{constraints}
),
\]

\[
H_{t+1}
=
H_t\cup
\{\text{This round of learning and measurement feedback}\}.
\]

Generative models are better suited to take on:

- Status coding;
- Candidate action generation;
- Draft long-term plan;
- Content semantics and prerequisite relationship modeling.

Replanning after each round of feedback ensures adaptability. When generating a fixed-length sequence at a time, a midway replanning point should be designed.

## 16. Inspiration for CAT research

This paper explains that the key object of sequence recommendation is the **strategy function**:

\[
\pi(\text{Current status})\rightarrow\text{next action},
\]

The fixed sequence is just the unfolding of the strategy on a certain feedback trajectory.

For generative CAT, you can study:

1. The model generates the next question or a set of candidate questions;
2. Update the ability posterior and content status after answering;
3. Regenerate each step;
4. Use long-term measurement, content balance, exposure and fairness to jointly evaluate;
5. Use a hard constraint layer to ensure that each action is feasible.
