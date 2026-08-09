# Three identifiable conditions for Q

## Condition 1: Two sets of unit arrays

There is an item row permutation matrix \(P\) of \(J\times J\), so that

\[
PQ=
\begin{bmatrix}
I_K\\
I_K\\
\widetilde Q
\end{bmatrix},
\]

Among them \(\widetilde Q\) has \(J-2K\) rows.

This means that each attribute \(k\) has at least two "pure questions":

\[
\boldsymbol q_j=\boldsymbol e_k.
\]

There is no restriction on the order of items; \(P\) just moves these unit rows to the top of the matrix for expression.

## Condition 2: At least three questions for each attribute

\[
Q_k^{\mathsf T}\boldsymbol1_J\ge3,
\qquad k=1,\ldots,K.
\]

The first two sets of unit arrays already had at least two 1's in each column, so they also required

\[
\widetilde Q_k^{\mathsf T}\boldsymbol1_{J-2K}>0.
\]

That is, each attribute must appear at least once in the remaining items.

## Condition 3: There is no all-zero item

\[
\boldsymbol q_j^{\mathsf T}\boldsymbol1_K>0,
\qquad j=1,\ldots,J.
\]

Each question requires at least one attribute. All zero guilds will

\[
\eta_{ij}=1
\]

It is true for all students, so that this question cannot provide any attribute structure information.

## Collection writing method

The paper writes the legal space as

\[
\mathcal Q
=
\left\{
Q:
Q_k^{\mathsf T}\boldsymbol1_J\ge3\ \forall k,\
\boldsymbol q_j^{\mathsf T}\boldsymbol1_K>0\ \forall j,\
(PQ)^{\mathsf T}
=
[I_K,I_K,\widetilde Q^{\mathsf T}]
\right\}.
\]

## The relationship between the three conditions

|Conditions|Control object|Protective actions in the algorithm|
| --- | --- | --- |
|Two sets \(I_K\)|Pure question anchors for each attribute|It is not allowed to delete the unit row with only two copies left.|
|At least 3 1's per column|Property override|When the column sum is 3, it is not allowed to convert 1 into 0|
|At least 1 1 per line|item validity|The only 1 in the unit row is not allowed to be translated into 0|

The three "hold still" positions listed in the original article by Restricted Gibbs are local manifestations of these three types of boundaries.

## A legal example

When \(K=2,J=6\):

\[
Q=
\begin{bmatrix}
1&0\\
0&1\\
1&0\\
0&1\\
1&1\\
1&1
\end{bmatrix}.
\]

Each of the two unit rows appears twice, the sum of the two columns is 4, and each row is non-zero, so \(Q\in\mathcal Q\).

## An illegal example with only one space missing

\[
Q'=
\begin{bmatrix}
1&0\\
0&1\\
1&0\\
0&1\\
0&1\\
0&1
\end{bmatrix}.
\]

The sum of the first column is 2, violating Article 2. The model is excluded even though every row is still non-zero and both unit rows appear at least twice.

## Sufficient historical location

This article quotes Chen et al. (2015)'s DINA identifiable result, and defines the sampling space accordingly. Later literature further investigated weaker, necessary and sufficient, or generally identifiable conditions. When reading the 2018 paper, the algorithm should be understood in terms of the set of sufficient conditions adopted by the authors at the time.

[Next page: Why limit the posterior to the identifiable space](08-identified-space.md)
