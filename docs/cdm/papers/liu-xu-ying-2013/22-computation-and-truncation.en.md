# Saturation moment, search complexity and practical truncation

## Three exponential scales

### attribute profile

\[
2^k
\]

potential attribute profile.

### Saturated question group moments

\[
2^m-1
\]

A non-empty item subset.

### Q Candidate

All binary matrices have

\[
2^{mk}
\]

. If all zero rows are excluded, then we have

\[
(2^k-1)^m
\]

.

The three make the theoretical estimator quickly exceed the direct exhaustive ability.

## Inner question for each candidate

Given Q, \(\boldsymbol c,\boldsymbol g\), the attribute distribution passes

\[
\min_{\boldsymbol p_0}
\left\|
\overline T_{c,g}(Q)\boldsymbol p_0
-\boldsymbol\alpha
\right\|_2^2
\]

obtain, constrain

\[
\boldsymbol p_0\ge0,\qquad
\mathbf1^\top\boldsymbol p_0=1.
\]

This is a convex quadratic programming. The difficulties mainly come from:

- Combination search of outer Q;
-Storage and calculation of saturation moment;
- Additional continuation optimization when \(\boldsymbol c\) is unknown.

## Only keep low-level question groups

If the highest level is retained to \(d\), the number of rows becomes

\[
L_d
=
\sum_{\ell=1}^{d}
\binom m\ell.
\]

For example \(m=20\):

|Highest level \(d\)|Number of lines \(L_d\)|
| ---: | ---: |
| 1 | 20 |
| 2 | 210 |
| 3 | 1,350 |
| 4 | 6,195 |
|saturated| 1,048,575 |

Low-order truncation reduces costs significantly.

## Truncated statistical tradeoff

Higher-order joint accuracy is contributed by fewer students, especially when the item is difficult:

\[
\widehat\alpha_S
=
\frac1N\sum_{r=1}^N\prod_{i\in S}R_r^i
\]

Probably close to 0, the relative sampling error is large.

So increasing the number of rows also brings:

- More structural constraints;
- Higher computational load;
- Sparse and more relevant empirical moments;
- Possibly worse numerical conditions.

The saturation moment in theory mainly serves general identification proof. In practice, the highest order should be selected in combination with sample size and item difficulty.

## Block estimation

Original text Remark 2.6 It is recommended to split the item into several groups that may overlap:

\[
\mathcal I_1,\ldots,\mathcal I_L.
\]

Estimate the corresponding Q sub-matrix for each sub-question group, and then splice the results together. Overlapping items can help align attribute columns and detect conflicts.

There are still two practical problems with this solution:

1. The attribute column replacement of each sub-problem needs to be unified;
2. Blocking may lose cross-group joint moment information.

The original article only gives conceptual suggestions and does not formulate a complete merging algorithm.

## Expert Q as search constraint

Discussion suggested that the expert matrix \(Q_0\) should be included in the penalty:

\[
S(Q)+\lambda\,d(Q,Q_0).
\]

If the expert information is reliable, you can only search the neighborhood of \(Q_0\) to reduce the amount of calculation and improve the stability of limited samples. The row-by-row local search in the 2012 paper can be seen as one of the specific routes in this practical direction.

## The gap between the theory of this article and the scalable algorithm

The main theorem requires finding a global minimizer. Blocking, low-order truncation, neighborhood search, and local hill climbing all change the estimator. To transfer consistency to these algorithms, additional proofs are required:

- The truncation moment can still separate candidate Q;
- The search area contains true Q;
- The optimizer reaches the correct global or equivalent solution;
- Blocked column labels can be aligned consistently.

The original article clearly lists efficient computing as future work.

[Next page: Experiment and original evidence](23-experiment-and-evidence.md)
