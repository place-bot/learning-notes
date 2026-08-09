# Unknown \(c\): General estimation and moment estimation

## Settings for Section 4

The author further assumes:

- The guess probability \(\boldsymbol g\) is known;
- The correct probability of the master \(\boldsymbol c\) is unknown;
- Q is also unknown.

For open-response questions, \(g_i\) can be set approximately to 0. For multiple-choice questions, if each distractor item is equally attractive, the number of options can be used to give a rough guess rate. The original article also admits that this known hypothesis of \(g_i\) is strong.

## General profile estimator

Given candidate Q and known \(\boldsymbol g\), define

\[
\widetilde{\boldsymbol c}(Q,\boldsymbol g)
=
\arg\inf_{\boldsymbol c\in[0,1]^m}
S_{c,g}(Q).
\tag{4.1}
\]

It works for any Q structure. Calculation requires:

1. Outer layer search \(\boldsymbol c\);
2. Each time \(\boldsymbol c\) is given, inner optimization is performed on the attribute distribution \(\boldsymbol p\).

Therefore the original article calls it computationally intensive.

## Can quickly estimate the structural conditions of a certain \(c_i\)

For item \(i\), if there is a question group \(i_1,\ldots,i_\ell\) that does not contain \(i\), it satisfies

\[
B_Q(I_i\wedge I_{i_1}\wedge\cdots\wedge I_{i_\ell})
=
B_Q(I_{i_1}\wedge\cdots\wedge I_{i_\ell}),
\tag{4.2}
\]

Then the attribute set required by item \(i\) has been covered by other question groups.

Written as a set:

\[
\mathcal K_i
\subseteq
\mathcal K_{i_1}\cup\cdots\cup\mathcal K_{i_\ell}.
\]

Under true Q, people who can complete the remaining question sets must also have the attributes to complete question \(i\).

## Eliminate the guesswork first

Define augmented matrix

\[
\widetilde T_{c,g}(Q)
=
\begin{pmatrix}
\boldsymbol g_{\mathrm{joint}}&T_{c,g}(Q)\\
1&\boldsymbol E
\end{pmatrix}.
\]

The proof of Proposition 6.6 constructs a matrix \(D\) that only depends on \(\boldsymbol g\), satisfying

\[
D\widetilde T_{c,g}(Q)
=
\left(
\boldsymbol0,\,
T_{c-g}(Q)
\right).
\]

Let \(\boldsymbol a_g^\top\) be the corresponding question group in D

\[
I_{i_1}\wedge\cdots\wedge I_{i_\ell}
\]

row, \(\boldsymbol a_{*g}^\top\) is the row corresponding to the question group after adding \(I_i\).

## Ratio of two centralizing moments

Mapping by the overall moment,

\[
\boldsymbol a_g^\top
\begin{pmatrix}
\boldsymbol\alpha\\1
\end{pmatrix}
\overset{p}{\longrightarrow}
B_{c-g,Q}(I_{i_1}\wedge\cdots\wedge I_{i_\ell})
\boldsymbol p^*,
\]

\[
\boldsymbol a_{*g}^\top
\begin{pmatrix}
\boldsymbol\alpha\\1
\end{pmatrix}
\overset{p}{\longrightarrow}
B_{c-g,Q}(I_i\wedge I_{i_1}\wedge\cdots\wedge I_{i_\ell})
\boldsymbol p^*.
\]

Condition (4.2) makes the added question \(i\) only have one more factor \(c_i-g_i\), so the ratio between the two tends to

\[
c_i-g_i.
\tag{4.3}
\]

## Moment estimator

Thesis definition

\[
\overline c_i(Q,\boldsymbol g)
=
g_i+
\frac{
\boldsymbol a_{*g}^\top
\begin{pmatrix}\boldsymbol\alpha\\1\end{pmatrix}
}{
\boldsymbol a_g^\top
\begin{pmatrix}\boldsymbol\alpha\\1\end{pmatrix}
}.
\tag{4.4}
\]

Proposition 4.1 gives:

\[
\overline c_i
\overset{p}{\longrightarrow}
c_i.
\]

## Why is this estimate so fast?

Given Q and \(\boldsymbol g\):

- D can be pre-constructed;
- The numerator and denominator are affine transformations of empirical moments;
- No numerical optimization required;
- Each question that satisfies (4.2) can be calculated independently.

The trade-off is that it relies on an explicit attribute inclusion structure in candidate Q and will be unstable in finite samples if the denominator is too small.

[Next page: Combinatorial estimators with Theorem 4.2](14-combined-estimator-theorem-4-2.md)
