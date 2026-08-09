# de la Torre (2011) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Jimmy de la Torre. *The Generalized DINA Model Framework*. |
|Journal| *Psychometrika*, 76(2), 179--199, 2011 |
| DOI | [10.1007/s11336-011-9207-7](https://doi.org/10.1007/s11336-011-9207-7) |
|Publisher page| [Springer Nature](https://link.springer.com/article/10.1007/s11336-011-9207-7) |
|Original PDF| [Springer PDF](https://link.springer.com/content/pdf/10.1007/s11336-011-9207-7.pdf) |
|Errata| [10.1007/s11336-011-9214-8](https://doi.org/10.1007/s11336-011-9214-8) |
|Paper code|The author uses Ox to implement MMLE; the text does not give a public code address|
|Follow-up software|[Wenchao-Ma/GDINA](https://github.com/Wenchao-Ma/GDINA), developed by Wenchao Ma and Jimmy de la Torre|

## Three problems solved by this paper

The 2011 paper expanded G-DINA from a reaction function into a complete framework:

1. **Unified representation**: Use link function and design matrix to represent G-DINA, DINA, DINO, A-CDM, LLM, G-NIDA and R-RUM.
2. **Unified estimation**: First use MMLE to estimate the correct answer probability of each item and each reduced attribute profile, and then transform it to the parameters of different models.
3. **Question-by-question comparison**: Use the Wald test to determine whether a certain multi-attribute question can be reduced from a saturated model to a more concise CDM.

The main line of calculation of the framework can be written as

\[
\boldsymbol X,Q
\longrightarrow
\widehat{\boldsymbol P}_j
\longrightarrow
\widehat{\boldsymbol\phi}_j
\longrightarrow
R_{jr}\widehat{\boldsymbol\phi}_j
\longrightarrow
\text{item-level model decision}.
\]

Among them, \(\widehat{\boldsymbol P}_j\) is the success probability of item \(j\) under all reduced attribute profiles; \(\boldsymbol\phi_j\) can be an effect parameter on identity, logit or log scale.

## Recommended reading order

1. [Overview of the problem and framework](01-question-and-framework.md)
2. [Reduced attribute profile and partial ordering](02-reduced-patterns.md)
3. [Three link function](03-link-functions.md)
4. [identity-link G-DINA](04-identity-gdina.md)
5. [DINA, DINO and A-CDM](05-special-cases.md)
6. [LLM, G-NIDA and R-RUM](06-logit-log-families.md)
7. [MMLE vs. EM](07-mmle.md)
8. [design matrix](08-design-matrix.md)
9. [Reduced model and weight matrix](09-reduced-model-estimation.md)
10. [MLE, immutability and standard error](10-standard-errors.md)
11. [Question-by-Question Wald Test](11-wald-test.md)
12. [Simulation experiment](12-simulation.md)
13. [Fraction subtraction data](13-fraction-subtraction.md)
14. [Clinical Data and Errata](14-clinical-data-and-erratum.md)
15. [Code implementation intensive reading](15-code-implementation.md)
16. [Two attribute item value disassembly](16-numerical-walkthrough.md)
17. [Limitations and future work](17-limitations-and-future.md)
18. [Symbol table](18-symbols.md)
19. [Summary and follow-up reading](19-summary.md)
20. [Reference](references.md)

## Three layers to distinguish when reading

|layer|object|function|
| --- | --- | --- |
|probability layer| \(\boldsymbol P_j=\{P(\boldsymbol\alpha^*_{lj})\}\) |Directly describe the success rate of each reduced attribute group|
|parameter layer| \(\boldsymbol\delta_j,\boldsymbol\lambda_j,\boldsymbol\nu_j\) |Decompose main effect and interaction effect|
|constraint layer| \(M_j,R_{jr}\) |Define specific models and conduct Wald tests|

The most important concept of the paper is that the same set of success probabilities can be represented by different coordinates; model reduction imposes testable restrictions between these coordinates or probabilities.
