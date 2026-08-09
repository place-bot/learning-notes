# Reduction model and weight matrix

## Why weights are needed

Saturated G-DINA gives \(2^{K_j^*}\) probabilities, but the reduced model has only \(P\) parameters:

\[
2^{K_j^*}>P.
\]

Multiple reduction modes require joint determination of fewer parameters. If the posterior numbers of different models are very different, direct equal-weighted fitting will cause the rarer models to gain too much influence.

## Weight matrix

The paper uses reduced group expected number of people:

\[
W_j
=
\operatorname{diag}
\left(
I_{\boldsymbol\alpha^*_{1j}},
\ldots,
I_{\boldsymbol\alpha^*_{2^{K_j^*}j}}
\right).
\]

The weighted least squares estimate of the identity-link reduced model is

\[
\widehat{\boldsymbol\delta}_j
=
\left[
(M_j^{(r)})^\top
W_j
M_j^{(r)}
\right]^{-1}
(M_j^{(r)})^\top
W_j
\widehat{\boldsymbol P}_j.
\]

## Special reduction class defined in the paper

Let \(M_j^{(r-)}\) represent the design matrix after removing the intercept column. If

\[
(M_j^{(r-)})^\top
M_j^{(r-)}
\]

is a diagonal matrix, and the paper states that the model belongs to a special reduction class.

All two-parameter grouping models satisfy this condition, including:

- DINA；
- DINO；
- multiple-strategy DINA。

Some models that merge groups according to the "number of master attributes" are also satisfied.

## Group mean explanation

This special class divides \(2^{K_j^*}\) patterns into \(P\) non-overlapping groups \(g_{jp}\). The MLE for the group success probability is

\[
\widehat P(g_{jp})
=
\frac{
\sum_{\boldsymbol a\in g_{jp}}
R_{\boldsymbol a j}
}{
\sum_{\boldsymbol a\in g_{jp}}
I_{\boldsymbol a j}
}.
\]

It can also be written as the posterior number-weighted mean of the saturation probability:

\[
\widehat P(g_{jp})
=
\frac{
\sum_{\boldsymbol a\in g_{jp}}
I_{\boldsymbol a j}
\widehat P_j(\boldsymbol a)
}{
\sum_{\boldsymbol a\in g_{jp}}
I_{\boldsymbol a j}
}.
\]

The paper proves that this is consistent with the weighted least squares result above, and therefore belongs to MLE.

## Why does A-CDM require additional processing?

The main effect columns of A-CDM are not orthogonal to each other. A student who masters multiple attributes will contribute to multiple columns at the same time, so it does not belong to the special reduction category defined in the paper.

The paper recommends that given \(W_j\) and \(\widehat{\boldsymbol P}_j\), use numerical optimization estimation with probability boundaries on a problem-by-question basis:

\[
0\leq M_j^{(r)}\boldsymbol\delta_j\leq1.
\]

LLM and G-NIDA/R-RUM also need optimization under the corresponding link.

## Property boundary of two-step estimation

The paper clearly states:

- The saturated model transformation results in MLE;
- Weighted estimates of special reduction classes are also MLE;
- Problem-by-problem two-step estimation outside the special category, the asymptotic properties of which were not yet established at the time.

Therefore, computational convenience does not automatically translate into strict maximum likelihood guarantees.

## The benefits of problem-by-question fitting

If there are \(J^*\) multi-attribute questions and \(m\) candidate reduction models, refitting the entire test requires a large amount of full data estimation. The two-step framework first fits the saturated model once and then only

\[
J^*\times m
\]

Each item parameters layer is calculated, significantly reducing the cost of exploring hybrid model combinations.
