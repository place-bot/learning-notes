# Lemma 6.7 Matrix with guesswork elimination \(D\)

## Lemma 6.7

If

\[
T_1\boldsymbol p\in\mathcal C(T_2),
\]

Then there exists a certain \(\boldsymbol b\) such that

\[
T_1\boldsymbol p=T_2\boldsymbol b.
\]

Left multiplied by D that is compatible in any dimension:

\[
DT_1\boldsymbol p
=
DT_2\boldsymbol b
\in
\mathcal C(DT_2).
\]

So the converse proposition is:

\[
DT_1\boldsymbol p
\notin\mathcal C(DT_2)
\quad\Longrightarrow\quad
T_1\boldsymbol p
\notin\mathcal C(T_2).
\]

This allows for convenient row transformations of the matrix first.

## D's goal

The author constructs a matrix D that only relies on the known \(\boldsymbol g\), so that

\[
D\widetilde T_{c,g}(Q)
=
\left(
\boldsymbol0,\,
T_{c-g}(Q)
\right).
\]

The first column corresponds to the all-zero attribute profile. After the transformation it is exactly 0; the remaining columns become a T-matrix with no guesses and rows scaled to \(c_i-g_i\).

## Single question line

by

\[
B_{c,g,Q}(I_i)
=
g_i\boldsymbol E+(c_i-g_i)B_Q(I_i),
\]

available

\[
\left(
0,\,
B_{c-g,Q}(I_i)
\right)
=
\left(
g_i,\,
B_{c,g,Q}(I_i)
\right)
-g_i\boldsymbol E.
\tag{6.3}
\]

On the right side, only the single question row and the last full row in the augmented matrix are used, and the coefficient only depends on \(g_i\).

## Summary of question group lines

It is assumed that all centralized rows that do not exceed \(j\) questions can be linearly represented by augmented rows. For question \(j+1\),

\[
\left(
\prod_{h=1}^{j+1}g_{i_h},\,
B_{c,g,Q}(I_{i_1}\wedge\cdots\wedge I_{i_{j+1}})
\right)
\]

Is equal to the element-wise product of the single-question augmented row. Break each single question line into

\[
g_{i_h}\boldsymbol E
+
\left(0,B_{c-g,Q}(I_{i_h})\right)
\]

and expand:

- The last item is the required \(j+1\) question centering row;
- The remaining items only contain no more than \(j\) centralization factors;
- The induction assumption guarantees that the remaining terms already belong to the augmented matrix row space.

Therefore the target row also belongs to this row space. D can be formed by executing all non-empty question groups.

## Explicit inclusion and exclusion when there are two questions

press the whole

\[
1,\quad
\mu_1=E(R^1),\quad
\mu_2=E(R^2),\quad
\mu_{12}=E(R^1R^2)
\]

Arrange.

The centralized single question moment is

\[
E(R^1-g_1)=\mu_1-g_1,
\]

\[
E(R^2-g_2)=\mu_2-g_2.
\]

The moment of the centralization problem is

\[
\begin{aligned}
E[(R^1-g_1)(R^2-g_2)]
&=
\mu_{12}
-g_2\mu_1
-g_1\mu_2
+g_1g_2.
\end{aligned}
\]

The corresponding row transformation matrix can be written as

\[
D=
\begin{pmatrix}
-g_1&1&0&0\\
-g_2&0&1&0\\
g_1g_2&-g_2&-g_1&1
\end{pmatrix}.
\]

It is exactly polynomial expansion or inclusion-exclusion transformation.

## Why does the all-zero attribute column become 0?

The conditional accuracy rate of each question in all-zero mode is \(g_i\). So

\[
E(R^i-g_i\mid\boldsymbol A=\boldsymbol0)=0.
\]

The centered product of any non-empty question set is also 0. Therefore, the first transformed column is all 0.

## Why do other columns become \(T_{c-g}(Q)\)

Given a non-zero attribute profile,

\[
E(R^i-g_i\mid\boldsymbol A)
=
(c_i-g_i)\xi^i(\boldsymbol A).
\]

The product of the question group is given locally and independently:

\[
E\!\left[
\prod_{i\in S}(R^i-g_i)
\mid\boldsymbol A
\right]
=
\prod_{i\in S}(c_i-g_i)
\prod_{i\in S}\xi^i(\boldsymbol A).
\]

This happens to be the corresponding element of \(T_{c-g}(Q)\).

## What the transformation accomplishes

D converts the probability moment with baseline guess into a "net capability signal moment". The column space separation proposition can then be applied directly without guessing. D does not depend on Q or \(\boldsymbol c\), so the true model and all candidate models can be compared using the same transformation.

[Next page: Proof of the three main theorems](19-main-theorem-proofs.md)
