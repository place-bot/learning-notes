# Three-way array, triad and rank

## Three-way array

Set

\[
\mathcal X=(x_{ijk})
\in\mathbb F^{I\times J\times K},
\]

Among them:

- \(i=1,\ldots,I\) is the first direction;
- \(j=1,\ldots,J\) is the second direction;
- \(k=1,\ldots,K\) is the third direction;
- \(\mathbb F\) In the original text, it mainly takes the field of real numbers, and the modern version also discusses more general fields.

Think of \(\mathcal X\) as \(K\) \(I\times J\) matrices stacked together, or sliced in the other two directions.

## triad: three-way rank one array

given

\[
\boldsymbol a\in\mathbb F^I,\qquad
\boldsymbol b\in\mathbb F^J,\qquad
\boldsymbol c\in\mathbb F^K,
\]

their outer product

\[
\boldsymbol a\otimes\boldsymbol b\otimes\boldsymbol c
\]

The element at position \((i,j,k)\) is

\[
x_{ijk}=a_i b_j c_k.
\]

Kruskal calls this form of multiplication a **triad**. Modern literature often calls it rank-one tensor.

## Rank of three-way array

\[
\operatorname{rank}(\mathcal X)
=
\min\left\{
R:
\mathcal X
=\sum_{r=1}^{R}
\boldsymbol a_r\otimes
\boldsymbol b_r\otimes
\boldsymbol c_r
\right\}.
\]

Here \(R\) is the minimum number of rank one three-way arrays. It belongs to a different object from the ordinary matrix rank calculated after expanding the array into a matrix.

### Why "expand the rank of the matrix" can only give a lower bound

Expand \(\mathcal X\) along the first direction as

\[
X_{(1)}\in\mathbb F^{I\times JK}.
\]

Each triad is still a rank-one matrix after expansion, so any \(R\) term decomposition satisfies

\[
\operatorname{rank}(X_{(1)})\le R.
\]

In the same way,

\[
\max\left\{
\operatorname{rank}(X_{(1)}),
\operatorname{rank}(X_{(2)}),
\operatorname{rank}(X_{(3)})
\right\}
\le
\operatorname{rank}(\mathcal X).
\]

Expansion will lose part of the three-way structure, so this lower bound may not be tight.

## slab and slab-space

Fixing an indicator results in a two-dimensional matrix. For example, fix \(i\):

\[
X_{i::}
=
(x_{ijk})_{j,k}
\in\mathbb F^{J\times K}.
\]

The original text calls this two-dimensional slice slab. The dimension of the matrix space formed by all slabs in the first direction is expressed as

\[
\dim_1(\mathcal X)
=
\dim\operatorname{span}\{
X_{1::},\ldots,X_{I::}
\}.
\]

\(\dim_2(\mathcal X)\) and \(\dim_3(\mathcal X)\) can be defined similarly.

Under modern expansion notation,

\[
\dim_1(\mathcal X)
=\operatorname{rank}(X_{(1)}),
\]

It depends on whether the slabs are arranged in rows or columns when unfolding. The original text emphasizes:

\[
\dim_\ell(\mathcal X)
\quad\text{with}\quad
\operatorname{rank}(\mathcal X)
\]

There is generally no simple equation of "row rank equals column rank equals rank" in the matrix case.

## Linear transformation in mode direction

Suppose \(U\) acts in the first direction and \(W\) acts in the third direction. can be written as

\[
U*_{1}\mathcal X,
\qquad
W*_{3}\mathcal X.
\]

If

\[
\mathcal X=[A,B,C],
\]

rule

\[
U*_{1}\mathcal X=[UA,B,C],
\qquad
W*_{3}\mathcal X=[A,B,WC].
\]

This makes it possible to "compress or project in a certain direction first, and then examine the remaining ranks."

## Original Theorem 1’s idea of rank lower bound

The original article gives several tensor rank lower bounds. A special case listed in the abstract can be written as

\[
\operatorname{rank}(\mathcal X)
\ge
\dim_1(U*_{1}\mathcal X)
+
\operatorname{rank}(W*_{3}\mathcal X)
-
\dim_1\!\left(U*_{1}W*_{3}\mathcal X\right).
\tag{1}
\]

In the formula:

- The first item looks at how many independent slabs are left in the first direction after \(U\) transformation;
- The second item looks at the three-way rank after \(W\) transformation;
- The third term deducts the part that is double-counted after undergoing two transformations at the same time.

It has a structure similar to "two sources of information are added, subtracted and overlapped" and generalizes a matrix rank inequality of Frobenius.

!!! note "Relationship with CDM Mainline"
    CDM identifiability most often uses the decomposition uniqueness theorem in the second half of the paper. The rank lower bound is still important because uniqueness first requires that the terms written \(R\) actually constitute a shortest decomposition; modern Kruskal's theorem usually states "the tensor rank is equal to \(R\)" together with "the decomposition is essentially unique".
