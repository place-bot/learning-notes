# Noise T-matrix and objective function

## \(T_{c,g}(Q)\) for three question examples

continue to use

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix}
\]

and the non-zero attribute column \(10,01,11\).

If the row selects \(I_1,I_2,I_3,I_1\wedge I_2\), then

\[
T_{c,g}(Q)=
\begin{pmatrix}
c_1&g_1&c_1\\
g_2&c_2&c_2\\
g_3&g_3&c_3\\
c_1g_2&g_1c_2&c_1c_2
\end{pmatrix}.
\tag{3.6}
\]

Line by line explanation:

- Mode \(10\) can do question 1, but cannot do questions 2 and 3;
- Mode \(01\) can do question 2, but cannot do questions 1 and 3;
- Mode \(11\) can do all three questions;
- The row in question is multiplied element by element from the first two rows.

## Guess column for all-zero pattern

For the same four question groups, the probability of all zero attribute profiles is listed as

\[
\boldsymbol g_{\mathrm{joint}}
=
\begin{pmatrix}
g_1\\
g_2\\
g_3\\
g_1g_2
\end{pmatrix}.
\]

The saturation case continues to include the product of guess probabilities for all question sets.

## Overall moment mapping

Let the non-zero pattern probability be denoted as \(\boldsymbol p\) and the all-zero pattern probability as \(p_0\). rule

\[
\boldsymbol\mu
=
T_{c,g}(Q)\boldsymbol p
+p_0\boldsymbol g_{\mathrm{joint}}.
\]

The empirical moment satisfies

\[
\boldsymbol\alpha
\overset{\text{a.s.}}{\longrightarrow}
\boldsymbol\mu.
\]

There is no sample-by-sample exact equation here anymore. Conditional response randomness will cause sampling residuals, but the law of large numbers guarantees convergence of the empirical joint proportions.

## Fixed profile target for \(c,g,Q\)

Thesis definition

\[
S_{c,g}(Q)
=
\inf_{\boldsymbol p'}
\left\|
T_{c,g}(Q)\boldsymbol p'
+p_0'\boldsymbol g_{\mathrm{joint}}
-\boldsymbol\alpha
\right\|_2,
\tag{3.7}
\]

The constraint is

\[
p_{\boldsymbol A}'\in[0,1],
\qquad
\sum_{\boldsymbol A\in\{0,1\}^k}
p_{\boldsymbol A}'=1.
\]

Incorporating the all-zero pattern into the matrix can be written in a more compact form:

\[
\overline T_{c,g}(Q)
=
\left(
\boldsymbol g_{\mathrm{joint}},\,
T_{c,g}(Q)
\right),
\]

\[
S_{c,g}(Q)
=
\inf_{\boldsymbol p_0'}
\left\|
\overline T_{c,g}(Q)\boldsymbol p_0'
-\boldsymbol\alpha
\right\|_2.
\]

Among them, \(\boldsymbol p_0'\) contains all \(2^k\) pattern probabilities.

## Q estimator

\[
\widehat Q(\boldsymbol c,\boldsymbol g)
=
\arg\inf_{Q'}
S_{c,g}(Q').
\tag{3.9}
\]

\((\boldsymbol c,\boldsymbol g)\) in parentheses emphasizes that the estimator depends on these two known vectors.

## Augmented matrix

The proof requires simultaneously encoding probabilities that sum to 1. definition

\[
\widetilde T_{c,g}(Q)
=
\begin{pmatrix}
\boldsymbol g_{\mathrm{joint}}&T_{c,g}(Q)\\
1&\boldsymbol E
\end{pmatrix}.
\tag{6.2}
\]

So

\[
\widetilde T_{c,g}(Q)
\begin{pmatrix}
p_0\\
\boldsymbol p
\end{pmatrix}
=
\begin{pmatrix}
\boldsymbol\mu\\
1
\end{pmatrix}.
\]

The last line puts the probabilities and constraints directly into the linear map.

## The role of Euclidean distance

The original article Remark 3.1 points out that as long as the distance induces the same topology as the Euclidean space, the consistency idea can still be established. The reason why the author chooses Euclidean distance is that every fixed Q can be solved by mature quadratic programming.

Likelihood can also be used as a principled objective, but the calculation is more complex. The theoretical focus of this article is on the separability of Q, so moment distances that are easy to analyze and optimize are used.

[Next page: Theorem 3.1](12-theorem-3-1.md)
