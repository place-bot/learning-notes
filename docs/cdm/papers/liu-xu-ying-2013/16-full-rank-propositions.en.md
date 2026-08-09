# Propositions 6.1--6.2: full column rank

## Proposition 6.1

If Q is complete and \(T(Q)\) is saturated, the ranks of Q and \(T(Q)\) can be rearranged so that

\[
T(Q)_{1:(2^k-1)}
\]

It is a square matrix of full rank. Therefore, the entire \(T(Q)\) has full column rank.

## Step one: Put the unit matrix item in front

Integrity allows

\[
Q_{1:k}=I_k.
\]

Therefore, the anchor question \(i\) only requires the attribute \(i\).

## Step 2: Arrange the rows of T according to the size of the question group

Take the first \(2^k-1\) rows and correspond to:

1. \(k\) single anchor questions;
2. \(\binom{k}{2}\) two-anchor question combinations;
3. \(\binom{k}{3}\) three-anchor question combinations;
4. Go to all \(k\) anchor questions in sequence.

The total number of rows is

\[
\sum_{h=1}^k\binom{k}{h}
=2^k-1.
\]

Saturation ensures that all these rows exist.

## Step 3: Arrange the columns of T according to the number of mastered attributes

The columns correspond in turn:

1. Master the pattern of exactly 1 attribute;
2. Master the pattern of exactly 2 attributes;
3. Go to the mode that masters all \(k\) attributes.

The number of columns in each group is also \(\binom{k}{h}\).

## Block upper triangular structure

Sorted as above, the submatrix has

\[
\begin{pmatrix}
I_k & * & * & \cdots & *\\
0 & I_{\binom{k}{2}} & * & \cdots & *\\
0 & 0 & I_{\binom{k}{3}} & \cdots & *\\
\vdots & \vdots & \vdots & \ddots & *\\
0 & 0 & 0 & \cdots & I_{\binom{k}{k}}
\end{pmatrix}.
\tag{6.1}
\]

Why is the bottom left corner 0? A model that only masters \(h\) attributes cannot complete anchor question combinations that require more different attributes.

Why can diagonal blocks be arranged in a unit array? The anchor question combination that requires a certain \(h\) meta-attribute set can only be accurately covered by the same \(h\) meta-control set at this layer; the columns are properly arranged to form a unit matrix.

## The specific structure of \(k=3\)

Column by

\[
100,010,001\mid110,101,011\mid111
\]

Arrange; arrange in rows

\[
I_1,I_2,I_3
\mid
I_1I_2,I_1I_3,I_2I_3
\mid
I_1I_2I_3
\]

Arrange. The corresponding matrix is

\[
\begin{pmatrix}
1&0&0&1&1&0&1\\
0&1&0&1&0&1&1\\
0&0&1&0&1&1&1\\
0&0&0&1&0&0&1\\
0&0&0&0&1&0&1\\
0&0&0&0&0&1&1\\
0&0&0&0&0&0&1
\end{pmatrix}.
\]

It is an upper triangular matrix with all 1's on the diagonal, so the determinant is 1.

## Proposition 6.2

If Q is complete, \(T(Q)\) is saturated, and each \(c_i\ne0\), then

\[
T_c(Q)
\]

and its first \(2^k-1\) sorted rows all have full column rank.

by

\[
T_c(Q)=D_cT(Q),
\]

And \(D_c\) is a diagonal matrix. The scaling factor for any question group row is the product of \(c_i\) within the group. When all \(c_i\ne0\), all diagonal elements are nonzero, so

\[
\operatorname{rank}(T_c(Q))
=
\operatorname{rank}(T(Q))
=2^k-1.
\]

## Statistical problems solved by full column rank

If

\[
T_c(Q)\boldsymbol p_1
=
T_c(Q)\boldsymbol p_2,
\]

rule

\[
T_c(Q)(\boldsymbol p_1-\boldsymbol p_2)=0.
\]

Full column rank means that the zero space contains only zero vectors, so

\[
\boldsymbol p_1=\boldsymbol p_2.
\]

This ensures that given Q and item parameters, the saturation moment uniquely determines the non-zero attribute profile distribution. It does not yet compare different Q's by itself; the column space separation on the next page accomplishes that task.

[Next page: Column space separation](17-column-space-separation.md)
