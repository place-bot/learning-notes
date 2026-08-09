# ideal response, B-vector and T-matrix

## Column: non-zero attribute profile

\(T(Q)\) in Section 2 has

\[
2^k-1
\]

columns. Each column corresponds to a non-zero attribute profile

\[
\boldsymbol A\in\{0,1\}^k\setminus\{\boldsymbol0\}.
\]

The all-zero pattern is tentatively excluded because its contribution to the probability of any "correct" event is 0 when there is no noise and at least one attribute is required per question.

For example, when \(k=2\), the column can be

\[
(1,0),\ (0,1),\ (1,1)
\]

Arrange.

## Single question B-vector

Use \(I_i\) to represent the event "Question \(i\) is answered correctly". definition

\[
B_Q(I_i)
\]

is a row vector of length \(2^k-1\). The corresponding component of its attribute profile \(\boldsymbol A\) is

\[
\left\{B_Q(I_i)\right\}_{\boldsymbol A}
=
\prod_{j=1}^k(A^j)^{Q_{ij}}
=
\xi^i(\boldsymbol A).
\]

So this line is answering:

> For each attribute profile, does it have all the attributes required to answer question \(i\)?

## Question group B-vector

\(I_{i_1}\wedge\cdots\wedge I_{i_\ell}\) means all these questions are answered correctly. Thesis definition

\[
B_Q(I_{i_1}\wedge\cdots\wedge I_{i_\ell})
=
\mathop{\Upsilon}_{h=1}^{\ell}B_Q(I_{i_h}),
\tag{2.3}
\]

Where \(\Upsilon\) represents element-wise multiplication.

If

\[
\boldsymbol W
=
\mathop{\Upsilon}_{h=1}^{\ell}\boldsymbol V_h,
\]

Then the \(a\) component is

\[
W^a=\prod_{h=1}^{\ell}V_h^a.
\]

The question group row takes 1 under a certain attribute profile if and only if this mode can complete all questions in the group at the same time.

## Row: non-empty item subset

Each row corresponds to a non-empty item subset:

\[
\{i_1,\ldots,i_\ell\}
\subseteq
\{1,\ldots,m\}.
\]

Possible lines include, in order:

- All single questions \(I_1,\ldots,I_m\);
- All question pairs \(I_i\wedge I_j\);
- All three question combinations;
- Until all \(m\) question combinations.

If all combinations are included, the number of rows is

\[
\sum_{\ell=1}^m {m\choose \ell}
=2^m-1.
\]

The paper calls such \(T(Q)\) **saturated**.

## A specific B-vector

take

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix},
\]

The column order is \(10,01,11\).

Question 1 only requires attribute 1:

\[
B_Q(I_1)=(1,0,1).
\]

Question 2 only requires attribute 2:

\[
B_Q(I_2)=(0,1,1).
\]

Question 3 requires two attributes:

\[
B_Q(I_3)=(0,0,1).
\]

The row for question \(I_1\wedge I_2\) is

\[
(1,0,1)\odot(0,1,1)
=(0,0,1).
\]

Here \(\odot\) means element-wise multiplication.

## Meaning of T-matrix

Stack selected B-vectors row by row:

\[
T(Q)=
\begin{pmatrix}
B_Q(I_1)\\
\vdots\\
B_Q(I_{i_1}\wedge\cdots\wedge I_{i_\ell})\\
\vdots
\end{pmatrix}.
\]

It is a design matrix determined by Q:

- Column enumeration of potential attribute profiles;
- Line enumeration of observable joint correct events;
- The element indicates whether a certain mode has the ability to complete the question set.

## Why is T-matrix more informative than question-by-question accuracy?

When looking only at the accuracy of a single question, two candidates Q may obtain the same marginal probability by adjusting the attribute distribution. Added joint restrictions between latent classes for question pairs and higher-order question groups.

For example, the third question and "Answer the first and second questions simultaneously" have the same row in the ideal structure of the above example:

\[
B_Q(I_3)=B_Q(I_1\wedge I_2).
\]

This type of structural equality imposes additional constraints on the joint probability of observations and helps distinguish candidate Qs in the proof.

[Next page: Empirical moment \(\boldsymbol\alpha\) and overall mapping](04-alpha-and-moment-map.md)
