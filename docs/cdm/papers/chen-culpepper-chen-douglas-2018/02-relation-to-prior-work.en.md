# Relationship with existing Q learning methods

## Four front routes

The paper summarizes existing methods into four ideas.

### 1. Verify or revise around expert Q

de la Torre (2008), Chiu (2013), and de la Torre and Chiu (2016) start from a tentative Q, compare candidate q-vectors question by question, and then update inappropriate rows.

The advantage is that the amount of calculation is controllable and the result is easy to compare with the expert structure. The risk comes from the initial Q: if the tentative structure deviates far from the true value, the local search may stop in the wrong region.

### 2. Consistent estimation of T-matrix

Liu, Xu, and Ying (2013) presented a consistent estimation theory for DINA Q. Global search requires a relatively large candidate space. Taking \(J=40,K=5\) as an example, the bare binary matrix space has

\[
2^{JK}=2^{200}
\]

candidate.

The row-by-row version of Liu, Xu, and Ying (2012) reduces the number of candidates in an iteration to \(J2^K\), at the cost of relying on searches around the initial Q.

### 3. Regularization and model selection

Chen et al. (2015) first derived the identifiable conditions of DINA/DINO, then mapped the 0/1 structure of Q to the non-zero regression coefficient of LCDM, and used \(L_1\) regularization for variable selection.

This route is exploratory and can also borrow generalized linear model tools. The 2018 paper highlights two limitations:

- The regularized estimate does not explicitly force the final Q to be identifiable in the algorithm;
- When the number of attributes increases, high-order interaction terms increase rapidly.

### 4. Unconstrained Bayesian Sampling

Chung (2014) introduced hierarchical priors and topic-wise Gibbs updates for q-vectors. Its chain can access non-identifiable Q, and the posterior average may also span multiple equivalent likelihood patterns.

This article uses it as the main Bayesian baseline.

## Where is this article located?

|Dimensions|This article selects|
| --- | --- |
|Initial Expert Q|No need|
|Q search| MCMC |
|model|DINA; from duality to DINO|
|identifiable constraints|Explicitly force each step|
|Number of attributes \(K\)|predetermined by the researcher|
|Q point estimate|Posterior mode of the entire matrix after eliminating column permutation|
|uncertainty|Post-test samples are available|

## The precise meaning of “building on Chen et al. (2015)”

The paper abstract says the algorithm builds upon Chen et al. (2015). The main thing inherited here is the characterization of identifiable space:

\[
PQ=
\begin{bmatrix}
I_K\\
I_K\\
\widetilde Q
\end{bmatrix},
\qquad
\widetilde Q_{\cdot k}^{\mathsf T}\boldsymbol 1>0.
\]

The 2018 paper writes these structural restrictions:

- a priori support set of Q;
- Random generation of initial Q;
- MH candidate proposal;
- Element-by-element Gibbs legality check.

It does not follow the \(L_1\) objective function from 2015.

## Task differences with Q verification

Q verification usually asks:

> Is tentative line \(j\) appropriate? If not, which q-vector is better?

This article asks:

> Among all the identifiable whole Qs, which matrices have higher posterior probabilities?

The entire matrix constraint will couple the items. A certain \(q_{jk}\) looks reasonable on its own. If after flipping, there are only two questions left for a certain attribute, it still cannot become the next state of the restricted chain.

## Interface with subsequent work

This article leaves three direct lines of development:

1. Chen et al. (2021) further infers the number of attributes;
2. Oka and Okada (2023) use stochastic optimization and variational inference to improve scalability;
3. The current `edina` package adds BIC, DIC, posterior prediction checks and batch fitting of multiple \(K\).

These are subsequent extensions and should be read separately from the original 2018 algorithm.

[Next page: DINA model, data and all symbols](03-model-and-notation.md)
