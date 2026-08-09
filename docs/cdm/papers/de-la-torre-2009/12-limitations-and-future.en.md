# Limitations and future work

## The limitations clearly stated in the paper itself

### \(2^K\) Exponential complexity

The E-step of saturated DINA enumerates all attribute profiles. When \(K\) is slightly larger, both memory and computation increase rapidly.

The paper gives two types of mitigation ideas:

1. HO-DINA uses high-order capabilities to reduce the attribute distribution parameters to \(K+1\);
2. Use the theoretical attribute hierarchy to delete disallowed patterns.

If the attributes form a linear hierarchy, the number of allowed modes can be from

\[
2^K
\]

down to

\[
K+1.
\]

### Fixed pattern distribution

The appendix algorithm uses the same \(\pi_l\) at each E step. The paper proposes an empirical Bayes update:

\[
\widehat\pi_l
=
\frac1I\sum_iw_{il}.
\]

When the assumed prior differs significantly from the true student population, updating the mode distribution may improve estimates.

### item calibration is only the first step

Teaching applications ultimately require classifying students. The paper lists four research directions:

- attribute profileidentifiability;
- Classification methods such as MLE, MAP, EAP;
- test length requirements;
- Q matrix specifications.

## Limitations seen from experimental design

The simulation has only one combination of conditions:

\[
I=2000,\quad
J=30,\quad
K=5,\quad
g_j=s_j=.20.
\]

All attribute profiles are equally likely, Q is completely correct. result cannot be directly extrapolated to:

- Small sample size;
- short quizzes;
- high slip/guess;
- Strong imbalance mode;
- Highly relevant attributes;
- Q matrix error;
- Missing response.

## Limitations of real data evidence

Fractional subtraction analysis shows parameter interpretation and similarity of the two estimates, not provided:

- Global or item fit test;
- Comparison with DINO, G-DINA and other models;
- external standards;
- Classification consistency;
- teaching intervention result;
- Q matrix sensitivity.

Parameter similarity is part of model comparison and is not a substitute for full model evaluation.

## Q matrix is treated as known

This article does not estimate or verify \(Q\). If Q is wrong:

- ideal response \(\eta\) will be wrong;
- Alternative strategies may be absorbed into \(g_j\);
- slip may also absorb unmodeled property effects;
- Students will be classified according to their misperception structures.

This explains the need for the subsequent de la Torre (2008) and numerous Q-matrix validation papers.

## Model restrictions

DINA compresses the required attributes of the item into two states: "all mastered/not fully mastered". On the same topic:

\[
P(X_j=1\mid\eta_j=0)=g_j
\]

Same for all incomplete patterns.

It cannot express:

- The progressive difference between mastering one and mastering two required attributes;
- Main effect with different attributes;
- Different strengths of attribute interactions;
- Multiple explicit problem-solving strategies.

G-DINA relaxes these restrictions by saturating the item response function.

## identifiability boundary

The paper writes the model and estimation algorithm in a pedagogical manner, without giving the necessary and sufficient identifiable conditions for DINA parameters and Q matrices.

EM convergence indicates that the algorithm has found a stable point; it does not itself prove:

- Parameters are unique at the overall level;
- Q matrix is recoverable;
- Attribute tags have unique meanings;
- Finite sample likelihood has only one local extremum.

These issues belong to the subsequent RLCM and DINA identifiability theories.

## Reproducibility Boundary

Original Ox code obtained by request, real data not published with the paper, HO-DINA MCMC details are in the 2004 paper. A complete reproduction of Table 4 therefore requires additional material.

This site can be fully reproduced:

- Q with \(\eta\);
- marginal likelihood;
- EM update;
- A15 standard error;
- Analog design.

Value-by-value reproduction of Table 4 still requires raw reaction data and corresponding MCMC settings.
