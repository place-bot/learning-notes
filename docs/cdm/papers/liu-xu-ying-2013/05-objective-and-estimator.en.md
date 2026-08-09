# Objective function, Q estimator and calculation

## Fixed candidate Q: fit attribute distribution first

for any candidate

\[
Q'\in\{0,1\}^{m\times k},
\]

definition

\[
S(Q')
=
\inf_{\boldsymbol p\in[0,1]^{2^k-1}}
\left\|
T(Q')\boldsymbol p-\boldsymbol\alpha
\right\|_2,
\tag{2.6}
\]

and request

\[
0\le
\sum_{\boldsymbol A\ne\boldsymbol0}p_{\boldsymbol A}
\le1.
\]

The missing probability mass corresponds to an all-zero attribute profile:

\[
p_{\boldsymbol0}
=
1-
\sum_{\boldsymbol A\ne\boldsymbol0}p_{\boldsymbol A}.
\]

## Geometric interpretation of \(S(Q')\)

\(T(Q')\boldsymbol p\) changes with \(\boldsymbol p\) to form a set of moment vectors that the candidate Q can generate. The probabilistic constraints make it the convex hull of the columns of \(T(Q')\) with respect to the origin.

\[
S(Q')
=
\operatorname{dist}
\left(
\boldsymbol\alpha,\,
\{T(Q')\boldsymbol p:\boldsymbol p\ge0,\ \mathbf1^\top\boldsymbol p\le1\}
\right).
\]

So:

- \(S(Q')=0\): Candidate Q can accurately explain the sample moments with a certain attribute distribution;
- \(S(Q')>0\): Any legal attribute distribution leaves residuals;
- The smaller the distance: the closer the moment structure of candidate Q is to the data.

## Outer layer Q estimate

Thesis definition

\[
\widehat Q
=
\arg\inf_{Q'}S(Q').
\tag{2.7}
\]

This is a two-level discrete optimization:

1. Inner layer: fixed \(Q'\), optimized continuous \(\boldsymbol p\);
2. Outer layer: Compare all binary matrices \(Q'\).

The inner layer is quadratic programming with linear constraints. If we minimize the square distance,

\[
\frac12
\left\|T(Q')\boldsymbol p-\boldsymbol\alpha\right\|_2^2,
\]

The target is a convex quadratic function with respect to \(\boldsymbol p\).

## True Q Why is it always the minimizer?

Noiseless samples satisfy

\[
T(Q)\widehat{\boldsymbol p}
=\boldsymbol\alpha.
\]

And \(\widehat{\boldsymbol p}\) satisfies the probability constraint, so

\[
S(Q)=0.
\]

The distance will never be less than 0, so true Q must belong to the global minimization set.

The question then becomes:

> What other \(Q'\) can also make the distance 0?

Candidates for column permutation equivalence must reach 0. The main theorem is to prove that under C1--C5, as the sample size increases, other candidates cannot continue to reach the minimum value.

## Why the minimizer may not be unique

If \(Q'\) only exchanges the attribute columns of Q, then its \(T\)-matrix only exchanges the attribute profile columns. Rearrange \(\boldsymbol p\) in the same way and the product remains unchanged.

Therefore

\[
Q'\sim Q
\quad\Longrightarrow\quad
S(Q')=S(Q).
\]

The paper treats the entire equivalence class as correctly restored.

## Calculation scale

The candidate space contains at most

\[
2^{mk}
\]

a binary matrix. If all zero item rows are excluded, each row has \(2^k-1\) choices, and the number of candidates is still

\[
(2^k-1)^m.
\]

Saturated \(T\)-matrix again

\[
2^m-1
\]

OK. Therefore well-defined global estimators are computationally expensive at large \(m,k\).

## Practical mitigations proposed in the paper

Remark 2.6 recommends splitting the \(m\) question into several question groups that may overlap, estimating each smaller Q sub-matrix separately, and then merging the results.

Remark 2.7 also recommends keeping only:

- Single question combination;
- Correct question;
- A question set up to a certain highest order \(j\).

This reduces computational and sampling noise, but the saturation condition of the main theorem no longer holds as is. A clear distinction needs to be made between practical algorithms and theoretical estimators.

[Next page: Complete hand calculation of three questions and two attributes](06-worked-example.md)
