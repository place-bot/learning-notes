# Combining estimators with Theorem 4.2

## Divide \(c\) into two parts

For fixed candidate Q, let

\[
\boldsymbol c
=
(\boldsymbol c^*,\boldsymbol c^{**})
\]

Grouping:

- \(\boldsymbol c^*\): corresponds to the item that meets the condition (4.2);
- \(\boldsymbol c^{**}\): Corresponds to items whose moment ratio cannot be used directly.

## Part 1: Moment Estimation

Use element by element

\[
\overline{\boldsymbol c}^{\,*}(Q,\boldsymbol g).
\]

Proposition 4.1 guarantees that these components are consistent under true Q.

## Part 2: Conditional Profile

After fixing \(\overline{\boldsymbol c}^{\,*}\), optimize the remaining components:

\[
\widetilde{\boldsymbol c}^{\,**}(Q,\boldsymbol g)
=
\arg\inf_{\boldsymbol c^{**}}
S_{(\overline{\boldsymbol c}^{\,*},\boldsymbol c^{**}),g}(Q).
\]

After combining, we get

\[
\widehat{\boldsymbol c}(Q,\boldsymbol g)
=
\left(
\overline{\boldsymbol c}^{\,*}(Q,\boldsymbol g),
\widetilde{\boldsymbol c}^{\,**}(Q,\boldsymbol g)
\right).
\]

Any component greater than 1 is rounded to 1, and any component less than 0 is rounded to 0, so

\[
\widehat{\boldsymbol c}(Q,\boldsymbol g)\in[0,1]^m.
\]

## Q estimator

Substitute the \(\widehat{\boldsymbol c}(Q,\boldsymbol g)\) corresponding to each candidate Q into:

\[
\widehat Q_{\widehat c}(g)
=
\arg\inf_{Q'}
S_{\widehat c(Q',g),g}(Q').
\]

The algorithm is conceptually:

1. Enumerate candidate \(Q'\);
2. Check whether each question is satisfied (4.2);
3. Available components to calculate moment estimates;
4. The remaining components are profiled together with the attribute distribution;
5. Compare the final moment distances of candidate Qs.

## Theorem 4.2: Consistency of Q

Assuming that \(\boldsymbol g\) is known and the conditions of Theorem 3.1 hold, then

\[
\lim_{N\to\infty}
\Pr\!\left(
\widehat Q_{\widehat c}(g)\sim Q
\right)=1.
\]

This is the strongest Q recovery conclusion of the article: the master’s correct probability can be unknown.

## Additional conditions for attribute distribution consistency

Define final attribute distribution estimates

\[
\widetilde{\boldsymbol p}_{\widehat c}(g)
=
\arg\inf_{\boldsymbol p}
\left\|
T_{\widehat c(\widehat Q,g),g}(\widehat Q)\boldsymbol p
+p_0\boldsymbol g_{\mathrm{joint}}
-\boldsymbol\alpha
\right\|_2.
\]

If the general estimator

\[
\widetilde{\boldsymbol c}(Q,\boldsymbol g)
\]

It is also consistent under true Q, then after appropriately arranging the attribute columns,

\[
\widetilde{\boldsymbol p}_{\widehat c}(g)
\overset{p}{\longrightarrow}
\boldsymbol p^*.
\]

## Why Q consistency does not require all \(c_i\) to be consistent

Proposition 6.6 gives a strong conclusion:

\[
Q'\not\sim Q
\]

, no matter how the wrong candidate is selected

\[
\boldsymbol c'\in[0,1]^m,
\]

None of its augmented column spaces can contain true total moments.

Therefore, as long as the combination corresponding to the true Q is estimated to reduce the loss to 0, the wrong Q cannot catch up even with the inconsistent \(\boldsymbol c'\).

## Why \(\boldsymbol p\) consistent requires \(c\) consistent

Given Q, \(\boldsymbol p\) is obtained by

\[
\widetilde T_{c,g}(Q)\boldsymbol p_0
\]

Reflected. If the used \(\widehat{\boldsymbol c}\) converges to the error value, the design matrix itself will converge to the error matrix; full column rank can only guarantee that the solution under the error matrix is ​​unique, but cannot guarantee that the solution is equal to the true \(\boldsymbol p^*\).

## An example of unrecognizable dimensions

Original text Remark 4.1 taken

\[
Q=I_k.
\]

\(k\) The joint distribution of two binary questions is

\[
2^k-1
\]

degrees of freedom, and the parameter dimension of \((\boldsymbol p^*,\boldsymbol c)\) is

\[
(2^k-1)+k.
\]

This reaction table alone cannot generally identify both \(\boldsymbol p^*\) and \(\boldsymbol c\). Additional structures, parametric models, or a priori information may help.

[Next page: Total line](15-proof-roadmap.md) for all proofs
