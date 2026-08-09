# Estimation, regularization and calculation

This page presents estimation methods (estimation), regularization (regularization), joint maximum likelihood estimation (joint MLE), high-dimensional attribute structures (high-dimensional attribute structures) and computational implementations.

## Reading target

- Understand that CDM estimation is not just EM, but also includes regularized likelihood, joint MLE, Bayesian estimation, variational inference and structural learning.
- Distinguish between two estimation philosophies that treat the attribute \(A\) as a random latent variable and a fixed unknown parameter.
- Establish methodological background for subsequent R Shiny examples and `GDINA` package practice.
- Prepare Comparison for algorithm design of continuous-Q or exploratory-Q.

## Regularization and Q matrix estimation

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Chen, Liu, Xu & Ying (2015). Statistical analysis of Q-matrix based diagnostic classification models. | `cdm/papers/chen-liu-xu-ying-2015-q-matrix-dcm.md` |An important reference for regularized maximum likelihood and Q-matrix structure learning.|
|Intensive reading| Chen, Li, Liu & Ying (2017). Regularized latent class analysis with application in cognitive diagnosis. | `cdm/papers/chen-li-liu-ying-2017-regularized-lca.md` |Regularized latent class analysis and CDM applications.|
|main reading| Chen, Culpepper & Liang (2020). A sparse latent class model for cognitive diagnosis. | `cdm/papers/chen-culpepper-liang-2020-sparse-latent-class.md` |Sparse latent class model (SLCM) and exploratory CDM.|

## High-dimensional attributes and joint MLE

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Gu & Xu (2019). Learning attribute patterns in high-dimensional structured latent attribute models. | `cdm/papers/gu-xu-2019-high-dimensional-attribute-patterns.md` |Consistent selection of significant attribute patterns in high-dimensional SLAM.|
|Intensive reading| Gu & Xu (2023). A joint MLE approach to large-scale structured latent attribute analysis. | `cdm/papers/gu-xu-2023-joint-mle-slam.md` |Treat latent attributes as the core documentation of fixed unknown parameters.|
|Intensive reading| Ma & Xu. Learning latent and hierarchical structures in cognitive diagnosis models. | `cdm/papers/ma-xu-latent-hierarchical-structures.md` |At the same time, learn latent structure and hierarchy, and you will need to complete the complete publication information later.|

## Software, Bayesian and Scalable Computing

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Ma & de la Torre (2020). GDINA: An R package for cognitive diagnosis modeling. | `cdm/papers/ma-de-la-torre-2020-gdina-package.md` |Main entry point to R implementations and Shiny examples.|
|main reading| Chen, Culpepper, Chen & Douglas (2018). Bayesian estimation of the DINA Q-matrix. | `cdm/papers/chen-culpepper-chen-douglas-2018-bayesian-q.md` |Comparison of Bayesian Q-matrix estimation.|
|main reading| Liu, Andersson & Skrondal (2020). A constrained Metropolis-Hastings Robbins-Monro algorithm for Q matrix estimation in DINA models. | `cdm/papers/liu-andersson-skrondal-2020-mhrm-q.md` |Constrained sampling with Robbins-Monro updating.|
|main reading| Li, Ma & Xu (2022). Learning large Q-matrix by restricted Boltzmann machines. | `cdm/papers/li-ma-xu-2022-rbm-q-matrix.md` |Deep learning-style large-scale Q matrix estimation.|
|main reading| Oka & Okada (2023). Scalable Bayesian approach for the DINA Q-matrix estimation combining stochastic optimization and variational inference. | `cdm/papers/oka-okada-2023-scalable-bayesian-q.md` |Scalable routes to stochastic optimization and variational inference.|
|main reading| Balamuta & Culpepper (2022). Exploratory restricted latent class models with monotonicity requirements under Pólya-Gamma data augmentation. | `cdm/papers/balamuta-culpepper-2022-exploratory-rlcm-monotonicity.md` |The intersection of Bayesian computation, monotonicity, and exploratory latent structure.|

## Recommended order

1. Chen, Liu, Xu & Ying (2015)
2. Chen, Li, Liu & Ying (2017)
3. Gu & Xu (2019)
4. Gu & Xu (2023)
5. Ma & Xu’s structure learning paper
6. Ma & de la Torre (2020)
7. Bayesian, RBM, variational and Pólya-Gamma extensions
