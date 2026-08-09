# CDM core model

This page organizes the main line models of cognitive diagnosis models (Cognitive Diagnosis Models, CDM). Read the model structure first, then go into the Q matrix, identifiability, and estimation.

## Reading target

- Differentiate modeling assumptions for DINA, DINO, G-DINA, LCDM, GDM and Fusion Model.
- Clarify how the Q-matrix connects items and attributes.
- Trace the route from strong hypothesis models to general frameworks: conjunctive/disjunctive models to saturated/general models.
- Establish unified symbols for subsequent reading of GDINA software and extended models.

## Basics and Early Framework

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Junker & Sijtsma (2001). Cognitive assessment models with few assumptions, and connections with nonparametric item response theory. | `cdm/papers/junker-sijtsma-2001-few-assumptions.md` |Connection between CDM and nonparametric IRT. Focus on reading hypothetical models and diagnostic explanations.|
|Intensive reading| de la Torre (2009). DINA model and parameter estimation: A didactic. |[Full topic](papers/de-la-torre-2009/index.md)|DINA's introductory core literature. Covered slip, guessing, likelihood, EM, standard error, simulated and real data.|
|Intensive reading| Templin & Henson (2006). Measurement of psychological disorders using cognitive diagnosis models. | `cdm/papers/templin-henson-2006-dino.md` |Representative literature of the DINO model (Deterministic Input, Noisy Or gate), suitable for comparison with DINA.|

## Generalized model and unified framework

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| de la Torre (2011). The generalized DINA model framework. |[Full topic](papers/de-la-torre-2011/index.md)|Covered saturated item response function, three types of links, constrained sub-models, MMLE, Wald, experiments and code implementation.|
|main reading| Henson, Templin & Willse (2009). Defining a Family of Cognitive Diagnosis Models Using Log-Linear Models with Latent Variables. | `cdm/papers/henson-templin-willse-2009-lcdm.md` |LCDM uses log-linear language to unify a group of CDMs and compares with G-DINA and GDM.|
|main reading| von Davier (2005/2008). A general diagnostic model applied to language testing data. | `cdm/papers/von-davier-2008-general-diagnostic-model.md` |General diagnostic model (GDM) route. Focus on discrete latent variables and item parameterization methods.|
|main reading| Roussos, DiBello, Stout, Hartz, Henson & Templin (2007). The Fusion Model Skills Diagnosis System. | `cdm/papers/roussos-dibello-stout-hartz-henson-templin-2007-fusion.md` |Fusion Model's systematic diagnosis framework is suitable for understanding the design of skill diagnosis systems.|
|main reading| Rupp, Templin & Henson (2010). Diagnostic Measurement: Theory, Methods, and Applications. | `cdm/papers/rupp-templin-henson-2010-diagnostic-measurement.md` |Serving as a book-like background for model families and applied writing.|

## Software and extension entrance

|reading level|Paper|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|Intensive reading| Ma & de la Torre (2020). GDINA: An R package for cognitive diagnosis modeling. | `cdm/papers/ma-de-la-torre-2020-gdina-package.md` |The website will be connected to R Shiny in the future, so this article is the entrance to the implementation. Focus on reading which models the `GDINA` package can fit.|
|main reading| Zhan, Wang, Jiao & Bian (2018). Probabilistic-input, noisy conjunctive models for cognitive diagnosis. | `cdm/papers/zhan-wang-jiao-bian-2018-pinc.md` |The PINC model probabilizes the input control state. Subsequent connections to continuous-Q and partial mastery lines.|

## Recommended order

1. Junker & Sijtsma (2001)
2. de la Torre (2009)
3. Templin & Henson (2006)
4. de la Torre (2011)
5. Henson, Templin & Willse (2009)
6. Ma & de la Torre (2020)
7. Zhan, Wang, Jiao & Bian (2018)
