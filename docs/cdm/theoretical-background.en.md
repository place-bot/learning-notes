# Theoretical background: latent structure and mixed models

This page is placed at the front of the CDM partition. The reason is that many CDM problems essentially start not with the DINA formula, but with latent structure models, finite mixture models, and identifiability.

## Reading target

- Understand the identification logic from observed response distribution \(P(Y)\) to latent class response profiles.
- Understand when finite mixture models are identifiable, which conditions are merely sufficient, and which conditions are close to necessary.
- Learn to distinguish between model parameter identifiability, latent structure identifiability and label switching.
- Prepare for later reading restricted latent class models (RLCM) and Q-matrix (Q-matrix) identification.

## Latent structure and generic identifiability

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Allman, Matias & Rhodes (2009). Identifiability of parameters in latent structure models with many observed variables. |[Full topic](papers/allman-2009/index.md)|Upstream of CDM identification theory. Focus on the expressions of three-block decomposition, Kruskal's condition, and generic identifiability.|
|background| Allman & Rhodes (2006/2009). Tree topology and covarion identifiability papers. | `cdm/papers/allman-rhodes-phylogenetic-identifiability.md` |It is not used as the main proof of CDM, but it can help understand how to write identifiability in the mixture/covarion model.|
|background| Koopmans & Reiersøl (1950). The identification of structural characteristics. | `cdm/papers/koopmans-reiersol-1950-identification.md` |Classical statistical background on general recognition problems as a source of terminology and ideas.|
|background| Koopmans (1950). Statistical Inference in Dynamic Economic Models. | `cdm/papers/koopmans-1950-dynamic-economic-models.md` |Read only identification-related background and do not enter the CDM mainline.|
|background| Rothenberg (1971). Identification in parametric models. | `cdm/papers/rothenberg-1971-parametric-identification.md` |A general language used to complement parametric identifiability.|

## Finite mixture model and latent class model

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Teicher (1967). Identifiability of mixtures of product measures. | `cdm/papers/teicher-1967-product-mixtures.md` |Basic identification result of finite product distribution mixtures (mixtures of product measures).|
|Intensive reading| Yakowitz & Spragins (1968). On the identifiability of finite mixtures. | `cdm/papers/yakowitz-spragins-1968-finite-mixtures.md` |The classic result of finite mixture model identifiability, suitable for comparison with Teicher.|
|main reading| Goodman (1974). Exploratory latent structure analysis using both identifiable and unidentifiable models. | `cdm/papers/goodman-1974-latent-structure.md` |An early text on latent structure analysis, suitable for understanding the exploratory perspective.|
|main reading| Lindsay (1995). Mixture Models: Theory, Geometry and Applications. | `cdm/papers/lindsay-1995-mixture-models.md` |Mixture geometry and theoretical background.|
|main reading| McLachlan & Peel (2000). Finite Mixture Models. | `cdm/papers/mclachlan-peel-2000-finite-mixture-models.md` |EM, model selection, finite mixture model writing caliber.|
|main reading| Carreira-Perpiñán & Renals (2000). Practical identifiability of finite mixtures of multivariate Bernoulli distributions. | `cdm/papers/carreira-perpinan-renals-2000-bernoulli-mixtures.md` |It is very close to the binary reaction data of CDM, focusing on the practical identifiability of Bernoulli mixture.|
|background| Gyllenberg, Koski, Reilink & Verlaan (1994). Nonuniqueness in probabilistic numerical identification of bacteria. | `cdm/papers/gyllenberg-koski-reilink-verlaan-1994-nonuniqueness.md` |As a counterexample background to nonuniqueness.|

## Non-parametric mixing and repeated measurements

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|main reading| Hettmansperger & Thomas (2000). Almost nonparametric inference for repeated measures in mixture models. | `cdm/papers/hettmansperger-thomas-2000-repeated-measures-mixtures.md` |A mixture of repeated measures identifies and estimates background.|
|main reading| Hall & Zhou (2003). Nonparametric estimation of component distributions in a multivariate mixture. | `cdm/papers/hall-zhou-2003-nonparametric-mixtures.md` |Nonparametric estimation of multivariate mixtures.|
|main reading| Elmore, Hettmansperger & Thomas (2004). Estimating component cumulative distribution functions in finite mixture models. | `cdm/papers/elmore-hettmansperger-thomas-2004-component-cdf.md` |Estimation method of component distribution, connected to non-parametric mixture lines.|
|main reading| Hall, Neeman, Pakyari & Elmore (2005). Nonparametric inference in multivariate mixtures. | `cdm/papers/hall-neeman-pakyari-elmore-2005-multivariate-mixtures.md` |An inference framework for multivariate nonparametric mixtures.|
|main reading| Cruz-Medina, Hettmansperger & Thomas (2004). Semiparametric mixture models and repeated measures: The multinomial cut point model. | `cdm/papers/cruz-medina-hettmansperger-thomas-2004-cut-point.md` |Specific models of repeated measures and semiparametric mixtures.|
|background| Benaglia, Chauveau & Hunter (2009). An EM-like algorithm for semi and nonparametric estimation in multivariate mixtures. | `cdm/papers/benaglia-chauveau-hunter-2009-em-like-mixtures.md` |Just read the algorithm idea, and then compare it with EM, MML, and variational methods of CDM.|

## Temporary reading method

This group does not require that all details be understood at the beginning. The order of precedence is:

1. Allman, Matias & Rhodes (2009)
2. Kruskal (1977), see Mathematical Tools page
3. Teicher (1967) and Yakowitz & Spragins (1968)
4. Goodman (1974)、Lindsay (1995)、McLachlan & Peel (2000)
5. Non-parametric mixture and repeated-measures literature
