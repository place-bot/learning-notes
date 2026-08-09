# Why limit the posterior to the identifiable space?

## One-to-one mapping and posterior averaging

In the identified model, except for attribute column label permutation of Q, parameter values have a unique correspondence with the observed distribution. So the calculation of the posterior average for \(s_j,g_j\) has a clear meaning:

\[
\widehat s_j
=
E(s_j\mid\boldsymbol Y),
\qquad
\widehat g_j
=
E(g_j\mid\boldsymbol Y).
\]

If multiple different parameter sets produce the same likelihood, the chain may wander between multiple modes. Direct averaging mixes the patterns, and the average does not even correspond to any clear model interpretation.

## How constraints enter the posterior

\[
p(Q\mid-)
\propto
p(\boldsymbol Y\mid Q,-)
I(Q\in\mathcal Q).
\]

For \(Q\notin\mathcal Q\), the posterior density is 0. The algorithm does not need to filter out illegal states after sampling because proposals and element-wise updates already prevent the chain from leaving \(\mathcal Q\).

## Consistent conditionals

The logic of the original text is:

1. Assume true \(Q_0\in\mathcal Q\);
2. The conditions of Chen et al. (2015) ensure that DINA parameters are identifiable;
3. The Bayesian estimation in this article has a consistent basis on this correct support set.

If the true Q does not satisfy these restrictions, the restricted model suffers from support set misspecification:

\[
P(Q_0\mid\boldsymbol Y)=0
\]

This holds true for any sample size.

The original paper, based on comments from an anonymous reviewer, explicitly acknowledges this and suggests that unconstrained exploratory methods can be used to examine whether the data tend toward out-of-constraint structures.

## Statistical benefits brought by constraints

In simulation, unconstrained Gibbs has access to Q whose item parameters are not recognized. The restricted method concentrates the probability mass into a smaller legal set, and the item parameters MSE is usually lower, especially when \(K=4\).

This benefit comes from two sources:

- Exclude structurally illegal Q;
- Avoid \(s_j,g_j\) being averaged across multiple equivalent modes.

## Computational cost caused by constraints

Before each change of Q, it is necessary to determine whether the new matrix still satisfies:

- all rows are non-zero;
- sum of all columns is at least 3;
- Each unit vector appears at least twice.

MH's DS2 pre-constructs a legal configuration for an entire block; restricted Gibbs attempts flips and invokes legality checks on each element.

## Explorability and constraints do not conflict

"Exploratory" means that every \(q_{jk}\) does not need to be given first. It can still impose structural priors on the candidate space. This article explores

\[
\mathcal Q
\subset
\{0,1\}^{J\times K},
\]

Not all bare binary matrices are explored.

## Practical explanation

When the test blueprint cannot support two pure questions and at least three question coverage for each attribute, the method in this article is not suitable for direct application. Possible practices include:

- Adjust item bank design;
- Fixed some Qs confirmed by experts;
- Use subsequent models with weaker identification conditions;
- Treat the results of this article as a sensitivity analysis that satisfies strong design conditions.

[Next page: Conditional posterior and uniform prior of Q](09-q-posterior.md)
