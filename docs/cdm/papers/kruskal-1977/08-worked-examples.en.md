# Complete hand calculation example

## A decomposition of \(R=3\) that meets the conditions

take

\[
A=
\begin{bmatrix}
1&0&1\\
0&1&1\\
1&1&0
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{bmatrix},
\]

\[
C=
\begin{bmatrix}
1&2&1\\
0&1&1\\
1&0&1
\end{bmatrix}.
\]

All three matrices are \(3\times3\), and all determinants are non-zero:

\[
\det(A)=-2,\qquad
\det(B)=-2,\qquad
\det(C)=2.
\]

Therefore they all have full column rank:

\[
k_A=k_B=k_C=3.
\]

Kruskal condition is

\[
k_A+k_B+k_C
=9
\ge
8
=2R+2.
\]

So

\[
\mathcal X=[A,B,C]
\]

The tensor rank of is 3, and this three-term decomposition is intrinsically unique.

## Count a tensor element

The value of location \((1,1,1)\) is

\[
x_{111}
=
\sum_{r=1}^{3}
a_{1r}b_{1r}c_{1r}.
\]

Substitute three lines:

\[
x_{111}
=
(1)(1)(1)
+
(0)(1)(2)
+
(1)(0)(1)
=1.
\]

The entire \(3\times3\times3\) array is obtained by the same component-wise product.

## Construct an equivalent decomposition

Circularly replace the three components and take

\[
\Lambda
=\operatorname{diag}\left(2,\frac12,1\right),
\]

\[
M
=\operatorname{diag}\left(3,1,\frac13\right),
\qquad
N
=\operatorname{diag}\left(\frac16,2,3\right).
\]

Check ingredient by ingredient:

\[
2\cdot3\cdot\frac16=1,
\]

\[
\frac12\cdot1\cdot2=1,
\qquad
1\cdot\frac13\cdot3=1.
\]

Let \(P\) represent the same loop permutation, and define

\[
\bar A=AP\Lambda,\qquad
\bar B=BPM,\qquad
\bar C=CPN.
\]

Each new triad comes from an old triad, and the scaling product in the three directions is 1, so

\[
[\bar A,\bar B,\bar C]=[A,B,C].
\]

These two sets of matrices have different numerical values, but belong to the same essential decomposition.

## A construct that fails a condition and indeed has multiple solutions

Take \(R=2\):

\[
A=B=I_2,
\qquad
C=
\begin{bmatrix}
1&1
\end{bmatrix}.
\]

The two columns of the third factor are the same,

\[
k_C=1,
\]

And

\[
k_A=k_B=2.
\]

So

\[
k_A+k_B+k_C=5<6=2R+2.
\]

At this time, the three-way array has only one third-direction slice:

\[
\mathcal X(:,:,1)
=
\boldsymbol e_1\boldsymbol e_1^\mathsf T
+
\boldsymbol e_2\boldsymbol e_2^\mathsf T
=I_2.
\]

The problem has been reduced to a rank-one decomposition of the matrix \(I_2\).

Take any invertible matrix

\[
Q=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix}.
\]

Order

\[
\bar A=Q,
\qquad
\bar B=Q^{-\mathsf T}
=
\begin{bmatrix}
1&0\\
-1&1
\end{bmatrix},
\qquad
\bar C=C.
\]

Then

\[
\bar A\bar B^\mathsf T
=QQ^{-1}
=I_2,
\]

Thus

\[
[\bar A,\bar B,\bar C]=[A,B,C].
\]

This \(Q\) is not the product of permutation and diagonal scaling, so the two-group decomposition does not fall within the inherent ambiguity allowed by Kruskal. Changing \(Q\) also results in infinite group decompositions.

## What do the two examples illustrate together?

|situation|\(k\)-rank sum|Conclusion|
| --- | ---: | --- |
|Three \(3\times3\) factors full column rank| \(9\ge8\) |Theorem verification is essentially unique|
|The third factor and the two columns are the same| \(5<6\) |The theorem is invalid, and the construction does have multiple solutions|

The second line shows a real counterexample, but it cannot be generalized to "all decompositions that do not satisfy the condition have multiple solutions". The conclusion after failure of sufficient conditions still needs to be analyzed model by model.
