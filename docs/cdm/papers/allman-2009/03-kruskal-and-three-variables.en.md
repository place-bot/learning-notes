# Kruskal’s theorem and three-variable result

## Theorem 1: Three-way decomposition uniqueness

Set

\[
M_1\in\mathbb R^{r\times\kappa_1},
\qquad
M_2\in\mathbb R^{r\times\kappa_2},
\qquad
M_3\in\mathbb R^{r\times\kappa_3},
\]

And order

\[
I_j=\operatorname{rank}_K(M_j),\qquad j=1,2,3.
\]

Kruskal's theorem gives the condition

\[
I_1+I_2+I_3\ge 2r+2.
\tag{K}
\]

If condition (K) holds, then the tensor

\[
[M_1,M_2,M_3]
\]

Uniquely determines three factor matrices, allowing:

1. Perform the same permutation on the rows of the three matrices;
2. Each rank-one component is rescaled in three directions, but the product of the three scaling factors must be 1.

This result is a deterministic algebraic conclusion: as long as the Kruskal rank of three specific matrices satisfies the conditions, uniqueness is established at this parameter point.

## How to read \(2r+2\) in the condition

The tensor is summed by \(r\) rank-one components:

\[
\mathcal T
=
\sum_{i=1}^{r}
\boldsymbol a_i\otimes\boldsymbol b_i\otimes\boldsymbol c_i.
\]

\(I_1,I_2,I_3\) measures how difficult it is for latent class rows in each direction to be linearly confused. The greater the sum of the three, the more each component can be jointly distinguished by the three directions. \(2r+2\) on the right is the threshold of Kruskal uniqueness, not a simple comparison of the number of parameters.

## Corollary 2: Point state identification in probabilistic models

Three-variable latent class model usage

\[
\widetilde M_1=\operatorname{diag}(\pi)M_1.
\]

Because all \(\pi_i>0\), multiplying row \(i\) by a nonzero number does not change the linear correlation, so

\[
\operatorname{rank}_K(\widetilde M_1)
=
\operatorname{rank}_K(M_1).
\]

If

\[
I_1+I_2+I_3\ge 2r+2,
\]

Then the observation joint distribution uniquely determines

\[
\pi,\ M_1,\ M_2,\ M_3
\]

to latent class label permutation.

### Why does zoom disappear?

Kruskal decomposition may return

\[
D_1P\widetilde M_1,\qquad
D_2PM_2,\qquad
D_3PM_3,
\]

Among them, \(P\) is the common permutation, and \(D_1D_2D_3=I\) is the diagonal scaling.

The sum of each row of \(M_2,M_3\) is 1. The scaling factor can be obtained by summing the recovered rows, and then normalizing the rows. After normalization, the sum of each row of \(\widetilde M_1\) is the corresponding \(\pi_i\), and then restored to \(M_1\).

The probabilistic constraints therefore fix the scaling ambiguity of tensor decomposition.

## An example that directly satisfies the conditions

Assume \(r=2\), and the three observed variables are all dichotomous. If every

\[
M_j=
\begin{bmatrix}
1-\theta_{j1}&\theta_{j1}\\
1-\theta_{j2}&\theta_{j2}
\end{bmatrix}
\]

The two rows of are different, then the determinant

\[
\det(M_j)=\theta_{j2}-\theta_{j1}
\]

non-zero, so

\[
I_1=I_2=I_3=2.
\]

Kruskal condition becomes

\[
2+2+2=6=2(2)+2.
\]

Therefore, category exchange can be identified on these specific matrices for the parameters of the two latent classes and the three dichotomous observation variables.

## What can be derived when the condition fails?

Assume \(r=3\), there are still only three dichotomous variables. Each matrix has at most two columns, so

\[
I_j\le 2.
\]

Therefore

\[
I_1+I_2+I_3\le 6<8=2r+2.
\]

Kruskal's theorem cannot give uniqueness here. Logically we can only get

\[
\text{Kruskal's sufficient condition does not hold}.
\]

cannot be written directly as

\[
\text{The model is necessarily unrecognizable}.
\]

When sufficient conditions fail, the model may require more specialized tools, or it may indeed be unrecognizable.

## Corollary 3: From specific rank conditions to general recognition

For a general \(r\times\kappa_j\) matrix, the maximum possible Kruskal rank is

\[
\min(r,\kappa_j).
\]

The paper proves that matrices below the maximum fall on a true algebraic subvariety. Therefore, the general parameter points satisfy

\[
I_j=\min(r,\kappa_j).
\]

If

\[
\min(r,\kappa_1)
+
\min(r,\kappa_2)
+
\min(r,\kappa_3)
\ge 2r+2,
\tag{G}
\]

The three-variable latent class model can generally recognize label replacement.

## Why "low Kruskal rank" is an algebraic exception

Fixed an integer \(q\le\min(r,\kappa)\). A certain set of \(q\) rows is linearly related if and only if all \(q\times q\) subformulas composed of this set of rows are 0.

For the Kruskal rank to be less than \(q\), there only needs to be a set of \(q\) row correlations. By appropriately combining the non-zero subexpressions corresponding to each group of rows, a finite number of polynomials can be used to describe the failure set. By constructing a matrix that achieves the target Kruskal rank, we can confirm that these polynomials do not disappear identically.

So:

\[
\{\operatorname{rank}_K(M)<q\}
\]

It lies in the true algebraic subcluster and has measure 0.

## Fixed category ratio can still be widely recognized

Corollary 3 also shows that even if a positive category proportion vector \(\pi\) is fixed in advance, the conclusion still holds.

A separate argument is needed here, because "fixing \(\pi\)" is equivalent to limiting the parameter space to a low-dimensional subset. Having a bad set measure of 0 in the full parameter space does not automatically guarantee that a particular low-dimensional slice does not completely fall into a bad set.

The paper observes that as long as \(\pi_i>0\), the Kruskal rank condition only involves the subformula of \(M_j\); therefore, the general conclusion can be re-established in the conditional probability parameter space of fixed \(\pi\).

## Three different levels of statements

|statement|input|Conclusion strength|
| --- | --- | --- |
| Kruskal Theorem 1 |Three given matrices and their Kruskal ranks|Tensor factors are unique at that point, allowing permutations and scaling|
| Corollary 2 |Given the probability parameter, \(\pi_i>0\), the point state rank condition is established|The probability parameter is unique at that point, allowing label permutations|
| Corollary 3 |Given only \(r,\kappa_1,\kappa_2,\kappa_3\) and the dimension inequality|With the exception of the algebraic exception set, parameters are identifiable|

When reading subsequent CDM literature, one must distinguish between "a certain parameter point satisfies the full rank condition" and "it is universally true in a structured parameter space". The Q matrix constraint of CDM will limit the parameters to a special subspace, and general conclusions in the general latent class space cannot be moved directly without inspection.

