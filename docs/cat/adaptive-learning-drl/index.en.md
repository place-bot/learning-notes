# Deep RL adaptive learning: continuous capabilities, DQN and learning paths

This topic focuses on the paper **Deep Reinforcement Learning for Adaptive Learning Systems** by Xiao Li, Hanchen Xu, Jinming Zhang and Hua-hua Chang. The core cycle of thesis research is:

\[
\text{Measure current capabilities}
\longrightarrow
\text{Choose a study material}
\longrightarrow
\text{Students learn and develop abilities}
\longrightarrow
\text{Remeasure and select again}.
\]

The system only determines the current material each round. The new abilities after learning will be fed back to the strategy, so the same student will take different paths under different feedback.

## Citation details

|stage|Literature information|
|---|---|
|preprint|arXiv:2004.08410, submitted April 17, 2020|
|Publish online|*Journal of Educational and Behavioral Statistics*, November 3, 2022|
|official issue|April 2023, 48(2), 220–243|
| DOI | [10.3102/10769986221129847](https://doi.org/10.3102/10769986221129847) |

The equations (3)–(8) involved in this article follow the numbering of the 2020 arXiv first draft. The first page of the first draft was marked "Psychometrika Submission" and the final journal was *Journal of Educational and Behavioral Statistics*. Literature information is subject to the officially published version.

## Read the paper with a picture

```text
response data
   │
   ▼
IRT / MIRT ability estimator ──────────────┐
   │ Current continuous ability s_t │
   ▼                              │
DQN calculates Q(s_t, a) │ for each material
   │ ε-greedy select material a_t │
   ▼                              │
Real student or transition model ψ(s_t, a_t) │
   │                              │
   ├── Generate the next ability s_{t+1} ───────┘
   └── -1 for not reaching the goal, 0 for reaching the goal
```

The paper contains two complementary learning lines:

1. **Strategy Line**: DQN learns long-term action values from transfer samples and gradually forms a material selection strategy.
2. **Model Line**: The neural network learns the state transfer \(s_{t+1}\approx\psi(s_t,a_t)\), and then uses virtual students to expand the strategy training data.

## Core Research Questions

The paper should answer four questions:

1. Can continuous latent ability be used as a state of adaptive learning?
2. When student learning transfer is unknown, can DQN learn material selection strategies directly from interactive data?
3. When the number of students is insufficient, can we first learn the transition model and then use virtual interaction to improve data efficiency?
4. When the ability estimate contains noise, does the strategy still have an advantage?

## Positional relationship with NCAT

The action of this paper is **learning material**, and the goal is to change students' abilities; the action of [NCAT](../ncat/index.md) is **test item**, and the goal is to accurately measure students with fewer questions. Both use step-by-step feedback and Q-learning, but the meaning of state transition is different:

|Dimensions|Adaptive learning in this article| NCAT |
|---|---|---|
|action|Textbooks, videos, exercises or teaching support|a test question|
|Main changes|students’ real knowledge and abilities|Response evidence mastered by the system|
|target|Reach learning goals as quickly as possible|Improve measurement quality as quickly as possible|
|Feedback every step|New abilities measured after learning|Correct/wrong answer to the current question|
|Thesis experiment|Simulation on artificial transition model|Offline CAT on real response logs|

CAT assumes the measurement component in this system: after each round of learning, a short CAT can be used to estimate latent ability, and then the estimated value is given to the material recommendation strategy.

## Recommended reading route

First reading:

1. [Paper question, contribution and published version](01-publication-and-problem.md)
2. [Measurement model, capability status and assumptions](02-measurement-and-assumptions.md)
3. [MDP, Q function and Bellman equation](03-mdp-foundations.md)
4. [Write adaptive learning as MDP](04-adaptive-learning-mdp.md)
5. [From Bellman equation to DQN](05-bellman-and-dqn.md)
6. [Deep Q-learning complete algorithm](06-deep-q-learning-algorithm.md)
7. [Transition model estimator and virtual student](07-transition-model-estimator.md)

Keep reading when preparing to reproduce or research:

- [Complete hand calculation with step-by-step feedback](08-worked-example.md)
- [Simulation environment and experimental design](09-simulation-design.md)
- [Experimental result and evidence boundary](10-results-and-analysis.md)
- [Implementation Blueprint and Checklist](11-implementation-blueprint.md)
- [Limitations, CAT interface and future work](12-limitations-cat-comparison-future.md)
- [Symbol table, conclusion and reading map](13-symbols-summary.md)
