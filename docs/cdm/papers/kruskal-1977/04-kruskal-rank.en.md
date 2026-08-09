# Kruskal rank

## Definition

For a matrix with \(R\) columns

\[
A=
\begin{bmatrix}
\boldsymbol a_1&\cdots&\boldsymbol a_R
\end{bmatrix},
\]

Kruskal rank, referred to as \(k\)-rank, is defined as

\[
k_A
=
\max\left\{
q:
\text{Any \(q\) column of \(A\) is linearly independent}
\right\}.
\tag{5}
\]

The key word is "any". Ordinary matrix rank only requires the existence of a set of maximally independent columns.

## Relationship with ordinary matrix rank

\[
0\le k_A\le\operatorname{rank}(A)\le\min(I,R).
\]

- If \(A\) has zero columns, then \(k_A=0\);
- If there is no zero column, but there are two proportional columns, then \(k_A=1\);
- If each set of \(q\) columns of \(A\) is independent and at least one set of \(q+1\) columns is related, then \(k_A=q\);
- If \(A\) has full rank, then \(k_A=R\).

## Two matrices with the same ordinary rank

consider

\[
A_1=
\begin{bmatrix}
1&0&1\\
0&1&1
\end{bmatrix},
\qquad
A_2=
\begin{bmatrix}
1&1&0\\
0&0&1
\end{bmatrix}.
\]

Both have a common rank of 2.

For \(A_1\):

- Any single column is non-zero;
- Any two columns are independent;
- The three columns are located in two-dimensional space and must be related.

So

\[
k_{A_1}=2.
\]

For \(A_2\), the first two columns are identical, so there is a set of two columns that are related:

\[
k_{A_2}=1.
\]

Kruskal's condition differentiates the two matrices, ordinary ranks do not.

## Why uniqueness requires "arbitrary subset"

Uniqueness proofs continue:

1. Select some ingredients;
2. Use projection to eliminate another part of the component;
3. Repeat the argument on the remaining columns.

If only a certain set of columns is independent, the columns that happen to remain after projection may come from another set of related subsets. \(k\)-rank guarantees that no matter which set of columns no larger than \(k_A\) is left by the proof process, they remain independent.

## Relationship with spark

In compressed sensing notation,

\[
\operatorname{spark}(A)
=
\min\left\{
q:
\text{There is a linear correlation in the \(q\) column}
\right\}.
\]

As long as there is a linearly dependent column set for \(A\),

\[
k_A=\operatorname{spark}(A)-1.
\]

The two describe the same combination property in terms of "the maximum size that guarantees independence" and "the minimum size that may be relevant for the first time" respectively.

## How to calculate accurately

Small matrices can enumerate subsets of columns:

1. Starting from \(q=1\);
2. Enumerate all \(\binom{R}{q}\) \(q\) column submatrices;
3. Check whether the ordinary rank of each sub-matrix is \(q\);
4. The maximum \(q\) before the first failure is \(k_A\).

The amount of calculation will explode with the \(R\) combination. In large-scale problems, it may be difficult to accurately verify \(k\)-rank itself, and theoretical papers often establish lower bounds through matrix structures, subformal polynomials, or pan-full rank arguments.

## Row version and column version

Kruskal's original text and modern CP literature usually place ingredients in columns, thus defining the column \(k\)-rank.

Allman et al.'s latent class notation often places latent classes in rows. At this time they use the "any number of rows are independent" row Kruskal rank. The two versions correspond exactly by transposition:

\[
\operatorname{rank}_K^{\text{row}}(M)
=
k_{M^\mathsf T}.
\]

When reading the CDM literature, first confirm "whether the latent class is in a row or a column" before applying the inequality.
