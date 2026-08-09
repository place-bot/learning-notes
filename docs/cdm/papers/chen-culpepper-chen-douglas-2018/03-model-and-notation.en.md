# DINA model, data and all symbols

## Data structure

There are \(N\) students, \(J\) binary scoring questions, and \(K\) binary attributes.

\[
\boldsymbol Y=(Y_{ij})_{N\times J},
\qquad
Y_{ij}\in\{0,1\}.
\]

\(Y_{ij}=1\) means student \(i\) answered the correct item \(j\).

## Student attributes

The potential attribute profile of student \(i\) is

\[
\boldsymbol\alpha_i
=
(\alpha_{i1},\ldots,\alpha_{iK})^{\mathsf T},
\qquad
\alpha_{ik}\in\{0,1\}.
\]

share

\[
C=2^K
\]

kind of attribute profile. The paper uses \(\boldsymbol a_c\) to represent the \(c\) mode, and let

\[
\pi_c=P(\boldsymbol\alpha_i=\boldsymbol a_c).
\]

So

\[
\boldsymbol\pi=(\pi_1,\ldots,\pi_C)^{\mathsf T},
\qquad
\sum_{c=1}^{C}\pi_c=1.
\]

## Q matrix

\[
Q=(q_{jk})_{J\times K}
=
(\boldsymbol q_1,\ldots,\boldsymbol q_J)^{\mathsf T}
=
(Q_1,\ldots,Q_K).
\]

Here you need to distinguish between the two uppercase/lowercase writing methods:

- \(\boldsymbol q_j^{\mathsf T}\): The \(j\) row of Q indicates which attributes are required by question \(j\);
- \(Q_k\): The \(k\) column of Q indicates which questions require the \(k\) attribute;
- \(q_{jk}=1\): item \(j\) requires attribute \(k\);
- \(q_{jk}=0\): item \(j\) does not require attribute \(k\).

## item parameters

Each question has two parameters:

\[
g_j=P(Y_{ij}=1\mid \eta_{ij}=0),
\]

\[
s_j=P(Y_{ij}=0\mid \eta_{ij}=1).
\]

\(g_j\) is the correct guess probability when at least one required attribute is missing; \(s_j\) is the error probability when all required attributes are present.

The monotonicity limit is

\[
0\le g_j<1-s_j\le1.
\]

It ensures that the correct answer probability of those who have all the skills is higher than that of those who have not all the skills.

## ideal response indicator

\[
\eta_{ij}
=
I(\alpha_{ik}\ge q_{jk},\ \forall k)
=
I(\boldsymbol\alpha_i^{\mathsf T}\boldsymbol q_j
=\boldsymbol q_j^{\mathsf T}\boldsymbol q_j).
\]

- \(\eta_{ij}=1\): The student has all the attributes required by the item;
- \(\eta_{ij}=0\): At least one is missing.

The second equation utilizes binary vectors:

\[
\boldsymbol q_j^{\mathsf T}\boldsymbol q_j
\]

is equal to the number of attributes required by the item, and

\[
\boldsymbol\alpha_i^{\mathsf T}\boldsymbol q_j
\]

Equal to the number of required attributes the student already possesses. When both are equal, all requirements are met.

## Random variables and observed values

The original text deliberately distinguishes:

- Capital \(\boldsymbol Y\): random answer matrix;
- Lowercase \(\boldsymbol y\): Actual observed response matrix.

During the derivation, the author sometimes directly writes \(\boldsymbol Y\) into the likelihood. Just judge according to the context when understanding.

## A general table of symbols

|symbol|Dimensions|meaning|
| --- | --- | --- |
| \(N\) |scalar|Number of students|
| \(J\) |scalar|number of items|
| \(K\) |scalar|Number of attributes|
| \(C=2^K\) |scalar|Number of potential classes|
| \(Y_{ij}\) |scalar|binary answer|
| \(\boldsymbol\alpha_i\) | \(K\times1\) |student attribute profile|
| \(\boldsymbol a_c\) | \(K\times1\) |Possible pattern \(c\)|
| \(Q\) | \(J\times K\) |item—property mapping|
| \(\boldsymbol q_j\) | \(K\times1\) |Line \(j\) of Q|
| \(Q_k\) | \(J\times1\) |Column \(k\) of Q|
| \(\eta_{ij}\) |scalar|DINA ideal response|
| \(s_j,g_j\) |scalar|Error rate and guessing rate|
| \(\pi_c\) |scalar|Overall proportion of class \(c\)|
| \(\mathcal Q\) |collection|Q-space satisfying identifiable constraints|
| \(P\) | \(J\times J\) |item row permutation matrix|
| \(B\) |scalar|DS2 updated column block size|

[Next page: ideal response, item response function and likelihood](04-dina-likelihood.md)
