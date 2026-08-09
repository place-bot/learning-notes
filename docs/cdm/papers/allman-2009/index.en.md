# Allman, Matias and Rhodes (2009) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Elizabeth S. Allman, Catherine Matias, and John A. Rhodes. *Identifiability of Parameters in Latent Structure Models with Many Observed Variables*. |
|Journal| *The Annals of Statistics*, 37(6A), 3099--3132, 2009 |
| DOI | [10.1214/09-AOS689](https://doi.org/10.1214/09-AOS689) |
|preprint| [arXiv:0809.5032](https://arxiv.org/abs/0809.5032) |
|Original PDF| [arXiv PDF](https://arxiv.org/pdf/0809.5032) |
|Paper type|identifiability theory; no data sets, simulation experiments or empirical comparisons are included in the full text|
|official code|Not provided|

This paper establishes a set of proof methods that can be transferred repeatedly: find the conditionally independent structure after the latent variable is given, merge the observation variables into three blocks, write the joint distribution as a three-way tensor, and then use Kruskal's uniqueness theorem to restore the latent class parameters.

## One sentence main line

\[
\underbrace{P(X_1,\ldots,X_p)}_{\text{Observable joint distribution}}
\longrightarrow
\underbrace{\text{Three conditional independent observation blocks}}_{\text{grouping}}
\longrightarrow
\underbrace{\text{Three-way tensor decomposition}}_{\text{Kruskal}}
\longrightarrow
\underbrace{\pi,\ M_1,\ldots,M_p}_{\text{Differential latent class label permutation}}.
\]

For CDM, the latent class can be temporarily understood as attribute profile \(\boldsymbol\alpha\), and the observed variable is the item response. What the paper provides is the upstream theory to restore "latent class proportion and class conditional response probability"; the Q matrix, attribute meaning and DINA/G-DINA constraints still require CDM to specifically identify the result.

## Recommended reading order

1. [Problem and theoretical background](01-question-and-background.md): Identification, label permutation, universally identifiable and algebraic exception sets.
2. [Latent class model and tensor scale representation](02-model-and-tensor.md): Explain \(Z,r,\pi,p,\kappa_j,M_j\) and three-way tensor one by one.
3. [Kruskal’s theorem and three-variable result](03-kruskal-and-three-variables.md): Theorem 1, Corollary 2 and Corollary 3.
4. [Blocking Theorem and Bernoulli Mixture](04-grouping-and-bernoulli.md): Theorem 4, Corollary 5 and \(p\ge 2\lceil\log_2r\rceil+1\).
5. [Full text result and evidence boundary](05-results-and-evidence.md): HMM, random graph, non-parametric mixture, and why there is no Experiment in this article.
6. [Proof details and hand calculation example](06-proofs-and-worked-example.md): row tensor product, Vandermonde construction and \(r=4,p=5\) example.
7. [Interface with CDM identifiability](07-cdm-connection.md): From general latent classes to Q matrices, DINA parameters and attribute structures.
8. [Computable Reproducibility](08-computational-check.md): The paper has no official code; this site provides condition checking and label replacement verification scripts.
9. [Symbol table](09-symbols.md): unified query of full-text symbols, dimensions and corresponding meanings.
10. [Summary and subsequent reading](10-summary.md): Conclusions, limitations and the next batch of intensive reading papers.
11. [Reference](references.md): original text and directly related theoretical sources.

## Grasp the three levels when reading

|level|object|Where can the paper be identified?|
| --- | --- | --- |
|observation layer| \(P(X_1,\ldots,X_p)\) |Assume that the overall joint distribution is known|
|latent class layer| \(\pi_i,\ P(X_j=\cdot\mid Z=i)\) |Can revert to common label replacement when the condition is met|
|CDM structure layer|\(Q,\boldsymbol\alpha,g,s\) or G-DINA parameters|This article does not directly identify these structures|

!!! warning "Types of evidence for theoretical papers"
    The conclusions of this paper come from theorems, lemmas and algebraic proofs. There is no data table or prediction accuracy that can be written as experimental results. The subsequent "results" page will itemize the assumptions, conclusions, and applicable boundaries, leaving empirical questions to CDM-specific papers.

