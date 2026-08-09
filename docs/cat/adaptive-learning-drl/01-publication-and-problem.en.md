# Paper questions, contributions and published versions

## 1. Where was the original article later published?

This paper went through a clear publication chain:

1. On April 17, 2020, uploaded to arXiv as **Deep Reinforcement Learning for Adaptive Learning Systems**, numbered [2004.08410](https://arxiv.org/abs/2004.08410).
2. The header of the preprint PDF reads “Psychometrika Submission April 21, 2020”, indicating that the submission goal or manuscript template at that time is related to *Psychometrika*.
3. The paper was published online in the *Journal of Educational and Behavioral Statistics* on November 3, 2022.
4. Issue 48(2), April 2023, pages 220–243, DOI [10.3102/10769986221129847](https://doi.org/10.3102/10769986221129847).

Therefore, the canonical quote is:

> Li, X., Xu, H., Zhang, J., & Chang, H.-H. (2023). Deep reinforcement learning for adaptive learning systems. *Journal of Educational and Behavioral Statistics, 48*(2), 220–243.

## 2. Formula version and full text structure

This topic follows the formula numbering in the “Markov Decision Process Formulation” section of the 2020 arXiv draft:

- Formula (3): one-step state transition probability;
- Formula (4): Markov property;
- Formula (5): time homogeneity;
- Formula (6): Action value under the strategy;
- Formula (7): Bellman optimal equation;
- Formula (8): The reward for each step before reaching the goal is \(-1\).

The complete method and evidence chain of the paper also includes four parts:

1. IRT/MIRT ability measurement;
2. DQN function approximation and deep Q-learning;
3. Neural network transition model estimator;
4. Two sets of numerical simulations and their results.

Subsequent pages are expanded in the order of measurement model, MDP, DQN, transition model and experimental verification; the formula number uses the arXiv draft version, and the literature information uses the officially published version.

## 3. The practical problem to be solved by the paper

Traditional classrooms often arrange the same teaching materials, the same pace, and the same activities for a group of students. Learners have different starting points, weak dimensions, and learning speeds. The same material may be too difficult for some people and too easy for others.

Adaptive learning systems want to repeatedly perform:

\[
\widehat{\boldsymbol\theta}^{(t)}
\longrightarrow
a^{(t)}
\longrightarrow
\widehat{\boldsymbol\theta}^{(t+1)},
\]

Among them:

- \(\widehat{\boldsymbol\theta}^{(t)}\) is the capability vector measured in the \(t\) round;
- \(a^{(t)}\) is the learning material selected in this round;
- \(\widehat{\boldsymbol\theta}^{(t+1)}\) is the ability to be re-measured after learning.

The result pursued by the system can be expressed in two ways:

- At a given target level, shorten the number of learning rounds required to reach the target;
- Increase the final ability level when the number of learning rounds is fixed.

The paper chooses the first expression and writes it as a reinforcement learning goal through the cost of each step.

## 4. Why sequence decision-making is needed

If only the immediate improvement of materials is evaluated, the strategy may ignore prerequisite relationships and cross-competency transfer. For example:

- Material A currently only slightly improves algebra, but it establishes a foundation for subsequent comprehensive material C;
- Material B is currently improving significantly, but will soon enter a plateau;
- Comprehensive material C is generally effective for low-ability students and outstanding for middle- and high-ability students.

Material value is determined by the complete subsequent path:

\[
\text{Current material value}
=
\text{current impact}
+
\text{the subsequent opportunities it brings in the next state}.
\]

This is exactly the task of the action value function \(Q(s,a)\).

## 5. The research gap in which the paper falls

The paper summarizes existing work into several routes:

- Use explicit learning models to describe changes in abilities;
- Use the learning trajectory model to track knowledge acquisition;
- Use modeled recommendations to generate course sequences;
- Use model-free method to learn strategies, but the state mostly adopts discrete mastery mode.

The authors focus on two gaps.

### Continuous latent ability

The discrete mastery vector writes each skill as 0/1. For complex, multidimensional measurements, continuous capabilities can express finer level differences and directly interface with IRT/MIRT.

### Small sample interaction

DQN typically requires a large number of state transfers. Real student interaction is expensive and time-consuming, so the paper proposes a transition model estimator to fit the virtual student environment with limited student data.

## 6. Four main contributions

### Contribution 1: MDP with continuous capabilities

The author defines state as continuous latent ability:

\[
s=\boldsymbol\theta\in[0,1]^D.
\]

Actions are limited learning materials:

\[
a\in\{1,\ldots,L\}.
\]

### Contribution 2: DQN under unknown transfer

How students are affected by the material is often unknown. The authors use model-free deep Q-learning from

\[
(s,a,r,s')
\]

Directly learning long-term value from transferred samples.

### Contribution 3: Neural transition model

author fitting

\[
\widehat s'=\psi_v(s,a),
\]

Then let DQN interact with the virtual students generated by \(\psi_v\), thereby repeatedly utilizing limited real transfer.

### Contribution 4: Simulation verification

The paper constructs a nonlinear random transfer environment for two-dimensional continuous capabilities and three types of materials, compares DQN, heuristics and random strategies, and studies the impact of the ability estimate error and the number of real students.

## 7. The exact boundaries of innovation

The key advancements of the paper focus on:

- Continuous ability representation;
- model-free DQN；
- Assisted training of transition model under small sample conditions.

All experiments are from the simulation environment constructed by the author, and there are no randomized controlled experiments on real online learning platforms. The paper proves the feasibility and algorithm performance of the method in the set environment. Realistic learning gain, security and fairness still require empirical research.

## 8. Three systems to separate when reading

|system|input|output|training objectives|
|---|---|---|---|
|ability estimator|test answer| \(\widehat{\boldsymbol\theta}\) |Measure model fit|
|DQN strategy|Current capability \(s\)|Q value of each material|TD error|
|transition model| \(s,a\) |Next status \(\widehat s'\)|next state prediction error|

The three can be combined into a closed loop, but the parameters, data and error sources are different.
