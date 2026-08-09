#identifiabilitytheory

Identifiability (identifiability) is a main line in CDM that must be read carefully. It is organized here from general latent structures, through CDM/RLCM, to DINA, Q matrices, and extended data types.

## Reading target

- The difference between identifiable, generically identifiable and estimable.
- Understand how Kruskal's theorem feeds into latent class models and RLCM proofs.
- Understand how the Q matrix structure, attribute distribution and item parameters jointly determine identityability.
- Prepare terminology for continuous-Q, general-response or exploratory CDM writing.

## Universal base

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Kruskal (1977). Three-way arrays: Rank and uniqueness of trilinear decompositions. | `cdm/papers/kruskal-1977-three-way-arrays.md` |To prove the tool, you don’t need to read the details outside the application, but you need to master the use of the uniqueness theorem.|
|Intensive reading| Allman, Matias & Rhodes (2009). Identifiability of parameters in latent structure models with many observed variables. |[Full topic](papers/allman-2009/index.md)|A key theoretical source for identifying latent class response profiles from observational distributions.|

## RLCM and CDM parameter identification

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Xu (2017). Identifiability of restricted latent class models with binary responses. |[Full topic](papers/xu-2017/index.md)|CDM as the core identification theory of RLCM.|
|Intensive reading| Xu & Shang (2018). Identifying latent structures in restricted latent class models. | `cdm/papers/xu-shang-2018-latent-structures-rlcm.md` |A bridge from given restriction to learning latent structure.|
|Intensive reading| Fang, Liu & Ying (2019). On the identifiability of diagnostic classification models. | `cdm/papers/fang-liu-ying-2019-dcm-identifiability.md` |More general DCM identifiability caliber.|
|Intensive reading| Culpepper (2023). A note on weaker conditions for identifying restricted latent class models for binary responses. | `cdm/papers/culpepper-2023-weaker-rlcm-identification.md` |Weaken the conditions and focus on the use of dyad-completeness and Kruskal.|
|Intensive reading| Balamuta & Culpepper (2022). Exploratory restricted latent class models with monotonicity requirements under Pólya-Gamma data augmentation. | `cdm/papers/balamuta-culpepper-2022-exploratory-rlcm-monotonicity.md` |Also exploratory RLCM, Bayesian computation and identifiability.|

## DINA and Q matrix identification

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Gu & Xu. Sufficient and necessary conditions for the identifiability and estimability of the DINA model. | `cdm/papers/gu-xu-dina-identifiability-estimability.md` |The core writing method of necessary and sufficient conditions of DINA model. The complete year and publication information need to be completed later.|
|Intensive reading| Gu & Xu (2021). Sufficient and necessary conditions for the identifiability of the Q-matrix. |[Full topic](papers/gu-xu-2021/index.md)|Core literature on joint identification of unknown Q, item parameters and latent class proportions.|
|Intensive reading| Chen, Liu, Xu & Ying (2015). Statistical analysis of Q-matrix based diagnostic classification models. | `cdm/papers/chen-liu-xu-ying-2015-q-matrix-dcm.md` |Cross-core literature on Q matrices, estimation and identifiability.|
|Intensive reading| Gu (2022/2023). Generic identifiability of the DINA model and blessing of latent dependence. | `cdm/papers/gu-2023-generic-identifiability-dina.md` |A great reference for anchor-free/generic languages. The year is checked against the publication version in the literature page.|

## Extended response type

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Lin & Xu (2024). Sufficient and necessary conditions for the identifiability of DINA models with polytomous responses. | `cdm/papers/lin-xu-2024-polytomous-dina-identifiability.md` |DINA identification under polytomous responses.|
|main reading| Liu & Culpepper (2024). Restricted latent class models for nominal response data: Identifiability and estimation. | `cdm/papers/liu-culpepper-2024-nominal-rlcm.md` |RLCM identification and estimation under nominal response data can be used as a background for general-response.|

## Recommended order

1. Kruskal (1977)
2. Allman, Matias & Rhodes (2009)
3. Xu (2017)
4. Gu & Xu’s DINA identification paper
5. Chen, Liu, Xu & Ying (2015)
6. Gu & Xu (2021)
7. Gu (2022/2023)
8. Fang, Liu & Ying (2019), Xu & Shang (2018), Culpepper (2023) and extended response type papers
