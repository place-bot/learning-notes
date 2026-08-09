# Complete Q matrix and ideal response

## Let’s look at noiseless DINA first

in an ideal situation

\[
R_j=\xi_{j,\boldsymbol\alpha},
\qquad
\xi_{j,\boldsymbol\alpha}
=
\mathbb I(\boldsymbol\alpha\succeq\boldsymbol q_j),
\]

The item parameters are known, and the only unknown quantity is the attribute distribution \(\boldsymbol p\).

If the ideal response vectors of the two attribute profiles are the same:

\[
\left(
\xi_{j,\boldsymbol\alpha}:j=1,\ldots,J
\right)
=
\left(
\xi_{j,\boldsymbol\alpha'}:j=1,\ldots,J
\right),
\]

They correspond to the same columns in the \(T\)-matrix. Data can only be identified

\[
p_{\boldsymbol\alpha}
+
p_{\boldsymbol\alpha'},
\]

The two proportions cannot be recognized separately.

## Definition of integrity

A Q matrix is called complete if each attribute has a question asking only for that attribute. Equivalently, several rows of Q are sorted to form

\[
I_K.
\]

That is

\[
\{\boldsymbol e_1^\top,\ldots,\boldsymbol e_K^\top\}
\subseteq
\{\boldsymbol q_1,\ldots,\boldsymbol q_J\}.
\]

## Why can a unit array distinguish ideal patterns?

In the unit block, the ideal response for question \(k\) is

\[
\xi_{k,\boldsymbol\alpha}
=
\mathbb I(\alpha_k=1)
=
\alpha_k.
\]

The ideal response vector of this \(K\) question is

\[
(\alpha_1,\ldots,\alpha_K)^\top
=
\boldsymbol\alpha.
\]

Different attribute profiles naturally have different vectors. Therefore, in an ideal DINA where the item parameters are known, the completeness is sufficient to distinguish all potential classes.

## Incomplete example

The paper gives

\[
Q=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

Yes

\[
\boldsymbol\alpha=(1,0)^\top
\quad\text{with}\quad
\boldsymbol\alpha'=(0,0)^\top,
\]

The first question both lacks attribute 2, and the second question both lacks attribute 2, so the ideal responses are both

\[
(0,0)^\top.
\]

So the two columns are indistinguishable, and \(\boldsymbol p\) is not identifiable.

## Known item parameters and unknown item parameters

|situation|The role of a \(I_K\)|
| --- | --- |
|Ideal DINA, \(\Theta\) Known|Distinguish all attribute profiles and identify \(\boldsymbol p\)|
|Noisy, \(\Theta\) unknown|It is also necessary to separate the item probability and class proportion at the same time, which is not complete enough.|

The paper quotes the existing DINA result and points out: When guessing, slipping and \(\boldsymbol p\) are all unknown, each attribute must be asked by at least three questions before it is possible to identify all parameters.

## From integrity to C1

Xu adopts two unit blocks for general RLCM:

\[
\begin{pmatrix}
I_K\\
I_K
\end{pmatrix}.
\]

Two blocks allow the proof to construct selective nonzero lines with one set of questions, while filling in the symmetry positions with another set of questions. But two blocks only let each attribute appear twice; Proposition 2 shows that this may still leave a family of continuously equivalent parameters, so C2 is also required.

## Integrity is a structural condition

Checking whether Q is complete simply checks whether each unit vector appears. It has nothing to do with sample size, estimation algorithm and goodness of fit. If Q is incomplete, adding participant data with the same structure will not produce missing distinguishing information.
