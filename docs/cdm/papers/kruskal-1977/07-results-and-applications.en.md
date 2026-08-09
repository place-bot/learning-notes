#Theoretical results and applications

## Result layout of the paper

The 44 pages of the 1977 paper can be organized into three result lines:

|result line|core object|Main output|
| --- | --- | --- |
|three-way array rank|triad, slab-space, pattern transformation|Multiple tensor rank lower bounds, including generalizations to Frobenius matrix results|
|decompose uniqueness|Triple product, column subset rank, permutation lemma|Theorem 4a and finer 4b, 4c|
|Application|Bilinear calculation and three-way statistical model|Interpret rank and uniqueness as computational lower bounds or parametric determinism|

Theorem 4a is often truncated from the CDM literature; a full reading requires knowing that it lies within a larger rank-decomposition-application structure.

## Rank lower bound

Given an explicit \(R\) term decomposition, it can only be obtained immediately

\[
\operatorname{rank}(\mathcal X)\le R.
\]

To prove that it is the shortest, a lower bound in the opposite direction is required. Paper passed:

- The dimensionality of slab-space;
- Apply linear transformations in different directions;
- Compare the retained ranks before and after transformation;
- Deduct overlapping space for duplicate counts,

Create several lower bounds.

Representative exceptions in the abstract are

\[
\operatorname{rank}(\mathcal X)
\ge
\dim_1(U*_{1}\mathcal X)
+
\operatorname{rank}(W*_{3}\mathcal X)
-
\dim_1(U*_{1}W*_{3}\mathcal X).
\]

It illustrates that tensor rank can be jointly constrained by multiple designed "views".

## Unique result

Most commonly used Theorem 4a passed

\[
k_A+k_B+k_C\ge2R+2
\]

It is guaranteed that the \(R\) item decomposition is essentially unique.

The original article also compares multiple sets of conditions on the rank of column subsets. 4b, 4c use richer information than a single \(k\)-rank, so uniqueness can still be established in some situations that 4a cannot cover.

This brings to an important conclusion:

> The simple sum condition is an easily verifiable certificate of uniqueness; it does not exhaust all unique decompositions.

## Arithmetic complexity

Many bilinear calculations can be written as

\[
y_k
=
\sum_{i,j}x_{ijk}u_i v_j.
\]

If the coefficient array \(\mathcal X=(x_{ijk})\) can be decomposed into \(R\) triads,

\[
x_{ijk}
=
\sum_{r=1}^{R}
a_{ir}b_{jr}c_{kr},
\]

Then the calculation can be organized as:

1. Calculate \(R\) linear forms about \(\boldsymbol u\);
2. Calculate \(R\) linear forms about \(\boldsymbol v\);
3. Corresponding multiplication;
4. Use \(C\) to perform linear combination to obtain the output.

Therefore, tensor rank is directly connected to the number of scalar multiplications required. The tensor rank lower bound can be transformed into a multiplicative complexity lower bound for bilinear algorithms.

The paper provides a theoretical interface and does not give benchmark programs or runtime experiments in today's sense.

## Three-way statistical model

Three-way data often has the structure of "object × condition × participant" or "item block 1 × item block 2 × item block 3". If the overall array satisfies

\[
\mathcal P
=
\sum_{r=1}^{R}
\pi_r
\boldsymbol a_r\otimes
\boldsymbol b_r\otimes
\boldsymbol c_r,
\tag{10}
\]

Then each \(r\) can represent a potential component:

- \(\pi_r\): component weight;
- \(\boldsymbol a_r,\boldsymbol b_r,\boldsymbol c_r\): Conditional mode for three observation directions under this component.

Kruskal conditions make these components recoverable by the overall three-way array, allowing for co-label permutations.

The original article also relates three-way multidimensional scaling to INDSCAL class models. The common structure is that multiple two-dimensional relationship matrices share a set of potential directions, and each participant or condition uses different weights for these directions. Three-way decomposition uniqueness illustrates when shared directions and weights have a deterministic interpretation.

## How to "verify" the conclusion of this paper

|Common empirical research elements|The situation of this article|
| --- | --- |
|Data set|None|
|training/testing split|None|
|Simulation conditions|None|
|Comparison of parameter estimation algorithms|None|
|Accuracy, bias, RMSE|None|
|Theorems and proofs|Yes|
|Construction, rank inequalities, sufficient conditions|Yes|
|Application explanation|Yes|

The strength of the paper's results comes from mathematical proofs. It gives deterministic conclusions at the level of the exact population array and does not evaluate the stability of estimates under limited samples.

## What are the missing steps from theory to practical estimation?

Only empirical frequencies or noisy three-way arrays are observed in actual data. Still need to deal with:

- How to choose the component \(R\);
- How to numerically find CP decomposition;
- How to impose non-negative and probabilistic normalization constraints;
- Local optima, degenerate sequences and condition numbers;
- How does the parameter variance increase when the \(k\)-rank condition is close to failure;
- How to align unnamed components to CDM attribute profile.

These tasks belong to the subsequent tensor algorithms, latent class estimation, and CDM structure identification.
