#BOBCAT Reading Guide

BOBCAT (Bilevel Optimization-Based Computerized Adaptive Testing) is a data-driven topic selection method under the CAT column. It places each student's short test adaptation process in the inner layer, puts the predicted performance of items not used for adaptation in the outer layer, and jointly learns the response model and topic selection strategy.

## One sentence main line

\[
\underbrace{\text{Strategy topic selection}}_{\phi}
\longrightarrow
\underbrace{\text{Adapt to student parameters based on selected responses}}_{\theta_i^*}
\longrightarrow
\underbrace{\text{Predict the remaining meta questions}}_{\mathcal L}
\longrightarrow
\underbrace{\text{Update global models and strategies}}_{\gamma,\phi}.
\]

When deployed, this chain still runs question by question: after the real answer to question \(t\) enters the state, the system selects question \(t+1\)
question. Therefore, the "learning topic selection algorithm" in the paper is real-time adaptive; the entire question sequence will gradually unfold with the answers.

## Recommended reading order

1. [Basic preparation](01-foundations.md): Basic concepts of CAT, IRT, response model, state and meta-learning.
1. [Dual-layer optimization](02-bilevel.md): First understand the outer/inner problem and meta-gradient independently.
1. [Framework and Algorithm](03-framework.md): Explain the paper formula and three types of topic selection algorithms letter by letter.
1. [Hand calculation example](04-worked-example.md): Use a small item bank to complete the BOBCAT process.
1. [Experiments, conclusions and future work](05-experiments.md): data, comparison methods, indicators, all main results and their boundaries.
1. [Symbols and Derivation](06-symbols-and-derivations.md): Check symbols, dimensions and key derivatives.
1. [Official code intensive reading](07-implementation.md): Map the paper formulas to `arghosh/BOBCAT` paragraph by paragraph.
1. [Summary](08-summary.md): A quick review of the entire paper.
1. [Reference](references.md): Source of papers and related methods.

## Always grab three objects when reading

|object|Paper mark|questions it answers|
| --- | --- | --- |
|global response model| \(\gamma\) |How to express the common response pattern between students and items?|
|student local parameters| \(\theta_i\) |After looking at the answers to the current short test, how would you characterize student \(i\)?|
|Topic selection strategy| \(\Pi_\phi\) |Given the current answer history, which question should I choose next?|

The outer meta loss ties the three together: the value of a set of questions depends on whether it can help the local model predict the student's answers to other items.
