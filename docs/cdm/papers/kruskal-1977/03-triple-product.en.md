# Triple products and inherent ambiguity

## Three factor matrices

Arrange \(R\) vectors into columns:

\[
A=
\begin{bmatrix}
\boldsymbol a_1&\cdots&\boldsymbol a_R
\end{bmatrix}
\in\mathbb F^{I\times R},
\]

\[
B=
\begin{bmatrix}
\boldsymbol b_1&\cdots&\boldsymbol b_R
\end{bmatrix}
\in\mathbb F^{J\times R},
\qquad
C=
\begin{bmatrix}
\boldsymbol c_1&\cdots&\boldsymbol c_R
\end{bmatrix}
\in\mathbb F^{K\times R}.
\]

Kruskal defines triple product

\[
[A,B,C]
=
\sum_{r=1}^{R}
\boldsymbol a_r\otimes
\boldsymbol b_r\otimes
\boldsymbol c_r.
\]

Written element by element

\[
[A,B,C]_{ijk}
=
\sum_{r=1}^{R}
a_{ir}b_{jr}c_{kr}.
\tag{2}
\]

Modern literature refers to this as CP or CANDECOMP/PARAFAC decomposition.

## "Column-wise pairing" in triple product

Item \(r\) is for fixed use

\[
\boldsymbol a_r,\quad
\boldsymbol b_r,\quad
\boldsymbol c_r.
\]

So triple products have a special rule for column order:

- The three matrices exchange the \(r\) and \(s\) columns at the same time, and the arrays remain unchanged;
- Swapping only two columns of one of the matrices usually changes the array.

This is where "co-displacement" comes into play.

## Replacement ambiguity

Let \(P\) be the \(R\times R\) permutation matrix. rule

\[
[AP,BP,CP]=[A,B,C].
\]

It only changes the order in which the summed terms are sorted.

In the latent class model, column \(r\) corresponds to the \(r\)th latent class, so \(P\) corresponds to class label exchange.

## Scaling ambiguity

Set

\[
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_R),
\]

\[
M=\operatorname{diag}(\mu_1,\ldots,\mu_R),
\qquad
N=\operatorname{diag}(\nu_1,\ldots,\nu_R),
\]

and

\[
\lambda_r\mu_r\nu_r=1
\quad
\text{to all}r.
\tag{3}
\]

Then

\[
[A\Lambda,BM,CN]=[A,B,C],
\]

Because the \(r\) triad is multiplied by

\[
\lambda_r\mu_r\nu_r=1.
\]

After adding the common permutation, it can be written as

\[
\bar A=AP\Lambda,\qquad
\bar B=BPM,\qquad
\bar C=CPN,
\tag{4}
\]

And the three scaling products are required to be 1 for the corresponding components after permutation. There are also documents written as \(A\Lambda P\); the only difference between the two notations is the rearrangement of the diagonal elements.

## Essentially unique

If

\[
[A,B,C]=[\bar A,\bar B,\bar C]
\]

Equation (4) must be deduced, and this decomposition is called **essentially unique**, that is, essentially unique.

The "essence" preserves symmetries that cannot be excluded by the model structure itself. Requiring that three factor matrices be identical element-by-element will incorrectly classify equivalent decompositions as different.

## Expanded form

Let \(\odot\) represent the Khatri--Rao product, that is, the Kronecker product of two matrices based on corresponding columns. The three expansions can be written as

\[
X_{(1)}=A(C\odot B)^\mathsf T,
\]

\[
X_{(2)}=B(C\odot A)^\mathsf T,
\]

\[
X_{(3)}=C(B\odot A)^\mathsf T.
\]

These formulas connect three-way decompositions to matrix algebra, but looking at either expansion alone still leaves a general reversible transformation ambiguity. Kruskal conditions jointly use three directions to compress ambiguity into displacement and scaling.

## How to eliminate scaling in probabilistic models

If each column of \(A,B,C\) is a conditional probability vector, then

\[
\boldsymbol 1^\mathsf T\boldsymbol a_r
=
\boldsymbol 1^\mathsf T\boldsymbol b_r
=
\boldsymbol 1^\mathsf T\boldsymbol c_r
=1.
\]

Any scaling other than 1 will break normalization. Therefore, after renormalizing the columns from the equivalent decomposition, the scaling is fixed; the co-permutation still exists.

This is the bridge that transforms the "uniqueness of displacement and scaling" of tensors into the "uniqueness of label displacement" of latent class models.
