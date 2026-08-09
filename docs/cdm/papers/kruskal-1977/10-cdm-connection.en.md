#Interface with CDM

## Divide the item into three pieces

Let the potential attribute profile be

\[
\boldsymbol\alpha\in\mathcal A,
\qquad
|\mathcal A|=R.
\]

Divide the item into three non-overlapping blocks:

\[
\mathcal J_1,\qquad
\mathcal J_2,\qquad
\mathcal J_3.
\]

For block \(t\), rank the probabilities of the reaction modes of all blocks under attribute profile \(\boldsymbol\alpha_r\).

\[
\boldsymbol m_{t,r}
=
\left[
P(\boldsymbol X_{\mathcal J_t}=\boldsymbol x
\mid
\boldsymbol\alpha_r)
\right]_{\boldsymbol x}.
\]

Reform matrix

\[
M_t=
\begin{bmatrix}
\boldsymbol m_{t,1}&\cdots&\boldsymbol m_{t,R}
\end{bmatrix}.
\]

## Conditionally independent triple product

If the attribute profile is given and the three item blocks are conditionally independent, the overall joint distribution is

\[
\mathcal P
=
\sum_{r=1}^{R}
\pi_r
\boldsymbol m_{1,r}
\otimes
\boldsymbol m_{2,r}
\otimes
\boldsymbol m_{3,r}.
\tag{11}
\]

Absorb the blending weights into the first matrix:

\[
\widetilde M_1
=
M_1\operatorname{diag}(\boldsymbol\pi),
\]

So

\[
\mathcal P
=[\widetilde M_1,M_2,M_3].
\]

This is where Kruskal's theorem can enter into the CDM.

## Kruskal Conditions

If

\[
k_{M_1}+k_{M_2}+k_{M_3}\ge2R+2,
\tag{12}
\]

and all \(\pi_r>0\), then multiplying by the diagonal weights does not reduce the linear independence between the corresponding columns:

\[
k_{\widetilde M_1}=k_{M_1}.
\]

The overall response distribution therefore determines three block conditional probability matrices, allowing common column permutations and scaling.

## How to fix scaling in probability normalization

For any column of \(M_2,M_3\),

\[
\boldsymbol 1^\mathsf T\boldsymbol m_{t,r}=1.
\]

Renormalizing the recovered columns fixes the scaling in both directions. The first direction normalized column gives \(M_1\) and the absorbed column sum gives

\[
\pi_r.
\]

Therefore, the final remaining ambiguity is that all matrices use the same column permutation.

## What does co-permutation mean in CDM

Kruskal's theorem recovers \(R\) unnamed latent components. It can explain:

\[
\{\text{Ingredient 1},\ldots,\text{Ingredients \(R\)}\}
\]

Can be restored to a set, but it does not automatically tell us which column corresponds

\[
(0,0,\ldots,0),\quad
(1,0,\ldots,0),\quad\ldots
\]

Such a specific attribute profile.

To anchor ingredient labels to cognitive meaning, use:

- a known or identifiable Q matrix;
- DINA, DINO, G-DINA and other item response constraints;
- Monotonicity or ideal response structure;
- attribute hierarchy or other structural assumptions.

## What step did Allman (2009) take?

Allman, Matias, and Rhodes combined multiple observed variables into three supervariables and proved that the block matrix has a sufficiently high Kruskal rank at general parameter points.

Therefore, the division of labor between the two papers is:

|Paper|completed bridge|
| --- | --- |
| Kruskal (1977) |The three factors satisfy the \(k\)-rank sum condition \(\Rightarrow\) triple integral decomposition is essentially unique|
| Allman et al. (2009) |How to divide multiple observation variables into three blocks, and why the block matrix generally satisfies the rank condition|
|CDM identification paper|How do Q matrices and concrete response models fix unnamed latent classes into attribute profiles?|

## Correct handling after condition failure

If equation (12) fails, you can continue in the following order:

1. Change the division of three items;
2. Merge more items to increase the number of reaction modes in each block;
3. Use the model structure to directly prove that some block matrices have full rank;
4. Find tensor uniqueness conditions that are finer than Theorem 4a;
5. Use CDM’s specialized identity theorem;
6. Construct equivalent parameters to determine whether it is really unrecognizable.

"Inequality failed" is a diagnostic result; the final identification conclusion still requires positive proof or counterexample.

## A reminder about limited sample studies

Kruskal conditions act on the overall probability matrix. Even if the model is identifiable in limited samples, it may occur:

- The response probabilities of the two latent classes are very close;
- Some subformulas are close to 0;
- Empirical tensor noise amplification;
- It is estimated to have a large standard error;
- Numerical algorithms are sensitive to initial values.

Algebraic uniqueness and stable estimation belong to two levels. Subsequent CDM simulation studies need to report both identification conditions and limited sample performance.
