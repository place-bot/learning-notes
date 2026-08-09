# Q matrix verification and learning

The Q-matrix defines the dependency relationship between items and attributes. It is the most problematic part of CDM and the most worth reading in a separate line. This page separates validation, data-driven learning, Bayesian estimation, machine learning-assisted and AI-assisted methods.

## Reading target

- Understand why the Q matrix given by experts may be wrong, and what parameters and classifications will be affected if it is wrong.
- Distinguish between Q-matrix validation and Q-matrix learning.
- Understand the different statistical implications of learning Q matrices from response data, text information, and AI tools.
- Prepare comparisons for continuous-Q or exploratory-Q studies.

## Empirical verification and classic methods

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| de la Torre (2008). An empirically based method of Q-matrix validation for the DINA model: Development and applications. |[Full topic](papers/de-la-torre-2008/index.md)|Classic entry for empirical Q-matrix verification under DINA.|
|Intensive reading| de la Torre & Chiu (2016). A general method of empirical Q-matrix validation. |[Full topic](papers/de-la-torre-chiu-2016/index.md)|Generalizing empirical validation to the G-DINA family using GDI/PVAF.|
|Intensive reading| Chen, Liu, Xu & Ying (2015). Statistical analysis of Q-matrix based diagnostic classification models. | `cdm/papers/chen-liu-xu-ying-2015-q-matrix-dcm.md` |Belongs to Q matrix, identifiability and regularized estimation at the same time. Must read carefully.|

## Data-driven and theoretical learning

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Liu, Xu & Ying (2012). Data-driven learning of Q-matrix. |[Full topic](papers/liu-xu-ying-2012/index.md)|Learn Q from response data using \(T\)-matrix and joint reaction moments.|
|Intensive reading| Liu, Xu & Ying (2013). Theory of self-learning Q-matrix. |[Full topic](papers/liu-xu-ying-2013/index.md)|C1--C5, column space separation and noise-free, known \(c,g\), unknown \(c\) three-level consistency theory are given.|
|main reading| Li, Ma & Xu (2022). Learning large Q-matrix by restricted Boltzmann machines. | `cdm/papers/li-ma-xu-2022-rbm-q-matrix.md` |Large-scale Q-matrix learning, connecting restricted Boltzmann machines (RBM).|
|main reading| Chen, Liu, Culpepper & Chen (2021). Inferring the number of attributes for the exploratory DINA model. | `cdm/papers/chen-liu-culpepper-chen-2021-number-attributes.md` |exploratory Inference of number of attributes in DINA.|

## Bayesian and partially known Q matrices

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Chen, Culpepper, Chen & Douglas (2018). Bayesian estimation of the DINA Q-matrix. |[Full topic](papers/chen-culpepper-chen-douglas-2018/index.md)|Restricted MH with Gibbs for exploratory Bayesian estimation in identifiable Q-space.|
|main reading| Liu, Andersson & Skrondal (2020). A constrained Metropolis-Hastings Robbins-Monro algorithm for Q matrix estimation in DINA models. | `cdm/papers/liu-andersson-skrondal-2020-mhrm-q.md` |MCMC/Robbins-Monro Q matrix estimation with identification constraints.|
|main reading| Oka & Okada (2023). Scalable Bayesian approach for the DINA Q-matrix estimation combining stochastic optimization and variational inference. | `cdm/papers/oka-okada-2023-scalable-bayesian-q.md` |Large-scale Bayesian Q estimation, focusing on stochastic optimization and variational inference.|
|main reading| Yamaguchi (2025). Bayesian diagnostic classification models for a partially known Q-matrix. | `cdm/papers/yamaguchi-2025-partially-known-q.md` |A partially known Q-matrix between confirmatory and exploratory.|

## Text, machine learning and AI assistance

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Zhao & Huang (2019). Automated Q-matrix identification using text classification techniques. |[Full topic](papers/zhao-huang-2019/index.md)|Chinese tokenization, \(n\)-gram, information gain and TF--IDF; complete experimental table, category imbalance and F1 formula audit, independent code reconstruction, and explanation of its interface with CDM/CAT.|
|main reading| Qin & Guo (2024). Using machine learning to improve Q-matrix validation. | `cdm/papers/qin-guo-2024-ml-q-validation.md` |Machine learning for Q matrix verification.|
|main reading| Fan, Bialo & Li (2026). The use of AI tools to develop and validate Q-matrices. | `cdm/papers/fan-bialo-li-2026-ai-q-matrices.md` |AI tools assist Q matrix development and verification. It is currently used as the latest direction, and the full version information needs to be completed later.|

## Q matrix paper directly connected to identifiability

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Gu & Xu (2021). Sufficient and necessary conditions for the identifiability of the Q-matrix. |[Full topic](papers/gu-xu-2021/index.md)|Q. Necessary and sufficient conditions for joint identification of item parameters and latent class proportions, covering strict and general identification.|

## Recommended order

1. de la Torre (2008)
2. de la Torre & Chiu (2016)
3. Liu, Xu & Ying (2012, 2013)
4. Chen, Liu, Xu & Ying (2015)
5. Chen, Culpepper, Chen & Douglas (2018)
6. Gu & Xu (2021)
7. Large-scale, Bayesian, ML and AI directions
