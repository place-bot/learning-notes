# Unknown \(c,g,p\) and DINA EM

The original article said that \((\widehat{\boldsymbol c},\widehat{\boldsymbol g},\widehat{\boldsymbol p})\) can be efficiently calculated by EM, but it did not write the update formula step by step. The following completes the standard DINA EM when Q is fixed.

## E step

For student \(i\) and attribute profile \(\boldsymbol\alpha\), the posterior weight

\[
\tau_{i\boldsymbol\alpha}
=
\Pr(\boldsymbol\alpha_i=\boldsymbol\alpha
\mid \boldsymbol R_i,Q,\boldsymbol c,\boldsymbol g,\boldsymbol p)
\]

satisfy

\[
\tau_{i\boldsymbol\alpha}
=
\frac{
p_{\boldsymbol\alpha}
\prod_j
\pi_{j\boldsymbol\alpha}^{R_i^j}
(1-\pi_{j\boldsymbol\alpha})^{1-R_i^j}
}{
\sum_{\boldsymbol\alpha'}
p_{\boldsymbol\alpha'}
\prod_j
\pi_{j\boldsymbol\alpha'}^{R_i^j}
(1-\pi_{j\boldsymbol\alpha'})^{1-R_i^j}
}.
\]

## M step: attribute distribution

\[
p_{\boldsymbol\alpha}^{\text{new}}
=
\frac1N\sum_{i=1}^N\tau_{i\boldsymbol\alpha}.
\]

## Step M: Master the correct answer rate of the group

Let \(\xi_{j\boldsymbol\alpha}\) be the ideal response,

\[
c_j^{\text{new}}
=
\frac{
\sum_i\sum_{\boldsymbol\alpha}
\tau_{i\boldsymbol\alpha}
\xi_{j\boldsymbol\alpha}R_i^j
}{
\sum_i\sum_{\boldsymbol\alpha}
\tau_{i\boldsymbol\alpha}
\xi_{j\boldsymbol\alpha}
}.
\]

## Step M: Correct answer rate of non-mastery group

\[
g_j^{\text{new}}
=
\frac{
\sum_i\sum_{\boldsymbol\alpha}
\tau_{i\boldsymbol\alpha}
(1-\xi_{j\boldsymbol\alpha})R_i^j
}{
\sum_i\sum_{\boldsymbol\alpha}
\tau_{i\boldsymbol\alpha}
(1-\xi_{j\boldsymbol\alpha})
}.
\]

## From EM to \(\widehat S(Q)\)

For each candidate Q:

1. Construct all \(2^K\) attribute profiles;
2. Run EM to get \(\widehat c,\widehat g,\widehat p\);
3. Construct \(T\) from candidate Q and \(\widehat c,\widehat g\);
4. Calculate \(T\widehat p\);
5. Find the Euclidean distance from the fixed sample \(\boldsymbol\beta\).

## Calculation Notes

- Use log-sum-exp to calculate the posterior to avoid underflow of a large number of item probabilities;
- Avoid \(\log0\) when \(p_{\boldsymbol\alpha}\) is close to 0;
- If q-vector is all zeros, all modes enter the ideal mastering group, and the \(g_j\) of this question cannot be identified by the data;
- EM may rely on initial values, and fair comparison of candidate Q requires consistent initialization and convergence rules;
- These project settings are not reported in the original article.

The script of this website implements this part as `fit_dina_em()`, and `profiled_objective()` completes the combination of equation (17).
