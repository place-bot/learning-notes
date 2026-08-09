# Theorem 3.1: Known consistency of \(c,g\)

## Theorem conditions

Assumptions:

1. \(\boldsymbol c,\boldsymbol g\) is known;
2. C1--C5 is established;
3. After the attributes are given, each question is generated independently;
4. response probability satisfies

\[
\Pr(R_r^i=1\mid\xi_r^i)
=
c_i^{\xi_r^i}g_i^{1-\xi_r^i};
\tag{3.10}
\]

5. For all questions,

\[
c_i\ne g_i;
\]

6. Vector

\[
T_{c-g}(Q)\boldsymbol p^*
\]

There are no zero components.

## Q Consistency

Let \(\widehat Q(\boldsymbol c,\boldsymbol g)\) be defined by equation (3.9), then

\[
\lim_{N\to\infty}
\Pr\!\left(
\widehat Q(\boldsymbol c,\boldsymbol g)\sim Q
\right)=1.
\]

## Attribute distribution consistency

definition

\[
\widetilde{\boldsymbol p}(\boldsymbol c,\boldsymbol g)
=
\arg\inf_{\boldsymbol p}
\left\|
T_{c,g}(\widehat Q)\boldsymbol p
+p_0\boldsymbol g_{\mathrm{joint}}
-\boldsymbol\alpha
\right\|_2^2,
\]

And constrain the sum of all mode probabilities to be 1. After arranging the columns of \(\widehat Q\) appropriately,

\[
\widetilde{\boldsymbol p}(\boldsymbol c,\boldsymbol g)
\overset{p}{\longrightarrow}
\boldsymbol p^*.
\]

## Changes with Theorem 2.4

|Noiseless| DINA |
| --- | --- |
|The sample loss for true Q is exactly 0|The loss of true Q almost certainly tends to 0|
|\(T(Q)\) is a 0/1 matrix|\(T_{c,g}(Q)\) including probability|
|All-zero modes do not contribute positive response moments|All-zero mode contribution guess probability column|
|Separate with Corollary 6.5|Separate with Proposition 6.6|
|\(T(Q)\) full rank|Augment \(\widetilde T_{c,g}(Q)\) full rank|

## Condition \(c_i\ne g_i\)

If a question is \(c_i=g_i\), then

\[
\Pr(R^i=1\mid\xi^i=1)
=
\Pr(R^i=1\mid\xi^i=0).
\]

The response to this question is not an indication of its ability, and the answer provides no information about the question's q-vector. Condition \(c_i\ne g_i\) ensures that each question still retains the attribute structure signal.

## Non-zero moment condition

\[
T_{c-g}(Q)\boldsymbol p^*
\]

Each component of is a "centralization ability signal" of a certain question group. If common

\[
c_i>g_i
\]

Established, combined with C4, all relevant products are positive, and this condition is naturally satisfied.

If certain \(c_i<g_i\) are allowed, the positive and negative contributions of different attribute profiles may offset to 0. The theorem rules out this degeneration.

## Core of the proof

The experience augmented moment satisfies

\[
\begin{pmatrix}
\boldsymbol\alpha\\
1
\end{pmatrix}
\overset{\text{a.s.}}{\longrightarrow}
\widetilde T_{c,g}(Q)
\begin{pmatrix}
p_0^*\\
\boldsymbol p^*
\end{pmatrix}.
\]

Proposition 6.6 shows that for any \(Q'\not\sim Q\) and any candidate \(\boldsymbol c'\), the right-hand true moment does not belong to

\[
\mathcal C\!\left(
\widetilde T_{c',g}(Q')
\right).
\]

Since \(\boldsymbol c'\in[0,1]^m\) is a compact set, the separation distance can take a uniform positive lower bound. After the empirical moments converge, the loss of the wrong candidate remains distant from 0.

## Why the theorem allows traversal in the proof \(c'\)

Theorem 3.1's estimator uses true \(\boldsymbol c\). The author's Proposition 6.6 gives a stronger separation: Error Q Even if \(\boldsymbol c'\) can be freely adjusted, it still cannot cover the true moments. This stronger result paves the way for the estimation of the unknown \(\boldsymbol c\) in Section 4.

[Next page: Estimated](13-unknown-c-estimation.md) for unknown \(c\)
