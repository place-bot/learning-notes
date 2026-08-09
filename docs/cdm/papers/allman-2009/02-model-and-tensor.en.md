#Latent class model and representation

## Limited latent class model

This paper first considers \(p\) finite state observation variables

\[
X_1,\ldots,X_p.
\]

The state number of the \(j\) variable is \(\kappa_j\), and the value set can be recorded as

\[
\mathcal X_j=\{1,\ldots,\kappa_j\}.
\]

latent variable

\[
Z\in\{1,\ldots,r\}
\]

There are \(r\) categories, and \(r\) is known. The category ratio is

\[
\pi_i=P(Z=i),\qquad
\pi_i>0,\qquad
\sum_{i=1}^{r}\pi_i=1.
\]

Given \(Z=i\), each observed variable is independent of each other:

\[
P(X_1=x_1,\ldots,X_p=x_p\mid Z=i)
=
\prod_{j=1}^{p}P(X_j=x_j\mid Z=i).
\]

## Conditional probability vectors and matrices

For the latent class \(i\) and the observed variable \(j\), define

\[
\boldsymbol p_{ij}
=
\bigl(
p_{ij}(1),\ldots,p_{ij}(\kappa_j)
\bigr),
\]

Among them

\[
p_{ij}(\ell)=P(X_j=\ell\mid Z=i).
\]

It is a probability vector:

\[
p_{ij}(\ell)\ge 0,
\qquad
\sum_{\ell=1}^{\kappa_j}p_{ij}(\ell)=1.
\]

Stack the conditional distributions of the same observed variable under all latent classes in rows to get

\[
M_j
=
\begin{bmatrix}
\boldsymbol p_{1j}\\
\boldsymbol p_{2j}\\
\vdots\\
\boldsymbol p_{rj}
\end{bmatrix}
\in\mathbb R^{r\times\kappa_j}.
\]

Row \(i\) corresponds to a latent class, and column \(\ell\) corresponds to a state of \(X_j\). The sum of each row is 1, so \(M_j\) is a row-stochastic matrix.

## Intra-class joint distribution

Given \(Z=i\), the joint probability table for the entire reaction vector is the vector outer product

\[
P_i
=
\boldsymbol p_{i1}\otimes\boldsymbol p_{i2}
\otimes\cdots\otimes\boldsymbol p_{ip}.
\]

Its \((x_1,\ldots,x_p)\) element is

\[
P_i(x_1,\ldots,x_p)
=
\prod_{j=1}^{p}p_{ij}(x_j).
\]

The overall observation distribution is a finite mixture of these multiplicative distributions:

\[
P
=
\sum_{i=1}^{r}\pi_iP_i
=
\sum_{i=1}^{r}
\pi_i
\bigotimes_{j=1}^{p}\boldsymbol p_{ij}.
\tag{1}
\]

The paper describes this model as

\[
\mathcal M(r;\kappa_1,\ldots,\kappa_p).
\]

## Parameter dimension and observation distribution dimension

Category scale has \(r-1\) free parameters. Each row of each \(M_j\) has
\(\kappa_j-1\) free parameters, with a total of \(r\) rows. Therefore, the dimension of parameter space is

\[
L
=
(r-1)+r\sum_{j=1}^{p}(\kappa_j-1).
\]

The observation joint probability table has

\[
K_{\mathrm{obs}}
=
\prod_{j=1}^{p}\kappa_j
\]

cells, and \(K_{\mathrm{obs}}-1\) degrees of freedom after deducting constraints that sum to 1.

Dimension comparison

\[
L\le K_{\mathrm{obs}}-1
\]

It is a necessary intuition for recognition, but it is not a sufficient condition. The parametric mapping may still be many-to-one when the dimensions are matched, or it may be continuously unrecognizable because the actual dimensions of the model image are reduced.

## Tensor when three observation variables

When \(p=3\), the joint distribution is

\[
P(X_1=u,X_2=v,X_3=w)
=
\sum_{i=1}^{r}
\pi_i
M_1(i,u)M_2(i,v)M_3(i,w).
\]

definition

\[
\widetilde M_1=\operatorname{diag}(\boldsymbol\pi)M_1.
\]

For papers

\[
[\widetilde M_1,M_2,M_3]
\]

Represents a three-way tensor

\[
[\widetilde M_1,M_2,M_3]
=
\sum_{i=1}^{r}
\widetilde{\boldsymbol m}_{1i}
\otimes
\boldsymbol m_{2i}
\otimes
\boldsymbol m_{3i},
\]

where \(\boldsymbol m_{ji}\) is row \(i\) of \(M_j\). of this tensor
The elements of \((u,v,w)\) happen to be the observed joint probabilities:

\[
[\widetilde M_1,M_2,M_3]_{u,v,w}
=
P(X_1=u,X_2=v,X_3=w).
\]

So the problem of identifying the overall distribution becomes the uniqueness problem of three-way tensor decomposition.

## Two inevitable differences

### Replace three groups of lines at the same time

If the same permutation matrix \(P\) is used to rewrite the three factors:

\[
(\widetilde M_1,M_2,M_3)
\mapsto
(P\widetilde M_1,PM_2,PM_3),
\]

The summation terms of each latent class only change the order, and the tensor remains unchanged. This is label replacement.

### Scaling between three factors

For the \(i\)th rank-one component, if

\[
\widetilde{\boldsymbol m}_{1i}
\mapsto a_i\widetilde{\boldsymbol m}_{1i},
\quad
\boldsymbol m_{2i}
\mapsto b_i\boldsymbol m_{2i},
\quad
\boldsymbol m_{3i}
\mapsto c_i\boldsymbol m_{3i},
\]

and satisfy

\[
a_ib_ic_i=1,
\]

The outer product remains unchanged. General tensor decomposition can only revert to this scaling.

The probabilistic model additionally knows that each row of \(M_1,M_2,M_3\) sums to 1. After renormalizing the recovered rows, the scaling is removed and the remaining scale goes into \(\pi_i\). This step converts pure algebraic uniqueness into probabilistic parameter uniqueness.

## Ordinary rank and Kruskal rank

The ordinary row rank of the matrix \(M\) is the dimension of the space spanned by all rows. Kruskal row rank is defined as

\[
\operatorname{rank}_K(M)
=
\max\left\{
k:
\text{Any \(k\) row of \(M\) is linearly independent}
\right\}.
\]

There is always

\[
\operatorname{rank}_K(M)\le \operatorname{rank}(M).
\]

For example

\[
M=
\begin{bmatrix}
1&0\\
1&0\\
0&1
\end{bmatrix}
\]

has ordinary rank 2, but the first two rows are linearly related, so

\[
\operatorname{rank}_K(M)=1.
\]

Kruskal rank is stronger than ordinary rank because tensor uniqueness requires that no degeneration occurs for any number of potential class rows.

If a \(r\times\kappa\) matrix has full row rank \(r\), then all \(r\) rows are linearly independent, so

\[
\operatorname{rank}_K(M)=r.
\]

## Why two-way tables are usually not enough

Two observed variables can only give matrix decomposition

\[
P_{12}=M_1^\top\operatorname{diag}(\pi)M_2.
\]

Matrix factorization can insert reversible transformations and their inverses, which are usually not unique. The third direction of the three-way tensor provides additional coupling constraints, and Kruskal's theorem uses the co-occurrence of these three groups of factors to ensure uniqueness.

## Matrix translation for CDM

\(\kappa_j=2\) in binary CDM, can be written

\[
M_j(i,\cdot)
=
\bigl(1-\theta_{j,i},\ \theta_{j,i}\bigr),
\]

Among them

\[
\theta_{j,i}=P(Y_j=1\mid Z=i).
\]

The single question \(M_j\) has only two columns, so

\[
\operatorname{rank}_K(M_j)\le 2.
\]

When the number of latent classes \(r\) is large, the single-question matrix cannot provide a sufficiently high Kruskal rank. Later in the paper, multiple questions were combined into one large observation block, so that the number of block states increased from 2 to \(2^{|S|}\). This is the key to the multivariable theorem.

