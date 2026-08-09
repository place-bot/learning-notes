# Research questions, contributions and boundaries

## Research questions

Row \(j\) of Q matrix

\[
\boldsymbol q_j=(q_{j1},\ldots,q_{jK})
\]

Record what attributes are required for item \(j\). In practice, Q is usually given by experts first, and then used as a fixed input to fit the CDM. If a certain \(q_{jk}\) is written incorrectly, item parameters, attribute profile posterior and student classification may be affected.

The 2008 method has been able to verify Q under DINA. It relies on DINA's two-group structure:

\[
\eta_j=0
\quad\text{or}\quad
\eta_j=1.
\]

For G-DINA, A-CDM, DINO and mixed reaction processes, the same multi-attribute question can have multiple different success probabilities. Comparing only the “fully mastered” and “not fully mastered” groups would lose these differences. The 2016 paper therefore proposes a metric that is less restrictive on the reaction function.

## Core Observation

Assume that the item really needs the attribute \(1,2,3\). After grouping with the correct q-vector, the success probability in each group is the same; when attribute 1 is omitted, categories with different success probabilities will be mixed into the same group, and the differences between groups will be averaged out; when an additional irrelevant attribute 4 is added, the homogeneous group will only be further divided, and the variance between groups will not increase.

Therefore the correct q-vector simultaneously satisfies:

1. The probability of success within the group after grouping is homogeneous;
2. Retain the maximum success probability variance between groups;
3. Use the fewest attributes in the vector that achieves the maximum variance.

## Four contributions

1. Define G-DINA discrimination index:

   \[
   \varsigma_j^2
   =
   \operatorname{Var}_w
   \left\{
   E(Y_j\mid\boldsymbol\alpha_{\boldsymbol q})
   \right\}.
   \]

2. Prove that the GDI of any missing, added, or both missing and added candidates does not exceed the correct q-vector.
3. Construct exhaustive search rules using PVAF and minimalism.
4. Test the method on five reduction models, unconstrained G-DINA, and fractional subtraction data.

## The difference between "verification" and "learning from scratch"

The paper starts with a complete provisional Q, and the default expert version is mostly correct. This Q is used to estimate the posterior weight of the student's attribute profile, and then propose modification suggestions on a question-by-question basis.

Without Q at all, the research question expands to:

- Whether the number of attributes \(K\) is known;
- Whether Q and item parameters are identifiable;
- How to search the combination space of \(2^{JK}\) Q;
- How to handle label replacement.

These problems belong to exploratory Q-matrix estimation. The empirical validation process of this article does not cover complete structure discovery from scratch.

## Evidence Boundary

Papers provided:

- Variance theorem at the overall level;
- Monte Carlo result under fixed design;
- A set of 11 real data examples.

The paper does not provide:

- Proof of consistency of estimates under arbitrary initial Q;
- Universal optimality of \(\varepsilon=.95\);
- Comprehensive experimentation for large \(K\), small samples or long quizzes;
-Original Ox source code;
- Automatic adjudication rules when pure data suggestions conflict with content expert opinions.

These boundaries were central discussions in the 2017 comments and responses.
