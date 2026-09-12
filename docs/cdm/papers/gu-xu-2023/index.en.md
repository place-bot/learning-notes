# Gu and Xu (2023): joint MLE for large-scale SLAMs

Gu, Y., & Xu, G. (2023). *A Joint MLE Approach to Large-Scale Structured Latent Attribute Analysis*. Journal of the American Statistical Association, 118(541), 746–760. [DOI](https://doi.org/10.1080/01621459.2021.1955689).

**Language:** the detailed chapters are currently in Chinese; the English site uses its configured Chinese fallback for those pages. This page is an English guide, not a claim that the full tutorial has been translated.

The tutorial covers the binary A/Q model, joint versus marginal likelihood, assumptions and three main theorems, profile-likelihood proofs, Gibbs conditionals, ADG-EM, two-stage regression, simulations, TIMSS, and the supplement.

## Reading order

1. [Question](01-question.md), [model](02-model.md), [likelihood](03-likelihood.md).
2. [Identification](04-identification.md), [assumptions](05-assumptions.md), [Theorem 1](06-theorem1.md).
3. [Profile likelihood](07-profile-proof.md), [concentration](08-concentration.md), [structural recovery](09-structure-proof.md).
4. [Multi-parameter proof](10-multiparameter-proof.md), [Theorems 2–3](11-misspecification.md).
5. [Gibbs derivation](12-gibbs.md), [ADG-EM](13-adg-em.md), [two-stage regression](14-two-stage.md).
6. [Simulations](15-simulations.md), [TIMSS](16-timss.md), [supplementary experiments](17-supplement.md).
7. [Executable checks](18-computational-checks.md), [source audit](19-source-audit.md), [summary](20-summary.md), [sources](references.md).

The reading copy is [arXiv v3 with its supplement](https://arxiv.org/pdf/2009.04096v3). Formula-level concerns are version-specific and explicitly separated from confirmed derivations. In particular, global-MLE consistency is not a guarantee that every ADG-EM run reaches the global optimum.
