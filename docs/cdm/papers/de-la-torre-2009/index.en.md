# de la Torre (2009) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Jimmy de la Torre. *DINA Model and Parameter Estimation: A Didactic*. |
|Journal| *Journal of Educational and Behavioral Statistics*, 34(1), 115--130, 2009 |
| DOI | [10.3102/1076998607309474](https://doi.org/10.3102/1076998607309474) |
|Publisher page| [SAGE Journals](https://journals.sagepub.com/doi/10.3102/1076998607309474) |
|Original PDF|[Carnegie Mellon University course archive](https://www.stat.cmu.edu/~brian/PIER-methods/For%202013-03-04/Readings/de%20la%20Torre-dina-est-115-30-jebs.pdf)|
|Paper type|Teaching model paper; including formula derivation, simulation study and real data analysis|
|original implementation|The author uses Ox to write the EM program; the paper description code can be obtained from the author, and no public repository is provided.|

This paper completes the most critical closed loop in getting started with DINA:

\[
\text{Properties and Q matrices}
\longrightarrow
\text{ideal response}
\longrightarrow
\text{guess/slip observation model}
\longrightarrow
\text{marginal likelihood}
\longrightarrow
\text{EM estimation and standard error}.
\]

The paper also introduces the high-order attribute distribution and MCMC estimation of HO-DINA, and uses simulated data and fractional subtraction data to compare the estimated results.

## One sentence main line

For each student \(i\) and item \(j\), first

\[
\eta_{ij}
=
\prod_{k=1}^{K}
\alpha_{ik}^{q_{jk}}
\]

Determine whether students have mastered all the attributes required by the question, and then use

\[
P(X_{ij}=1\mid\boldsymbol\alpha_i)
=
g_j^{1-\eta_{ij}}
(1-s_j)^{\eta_{ij}}
\]

Allow students who have not reached the ideal state to guess correctly and students who have achieved the ideal state to make mistakes. EM calculates the posterior weights on all \(2^K\) attribute profiles, and then updates \(g_j,s_j\) with the expected number of correct answers.

## Recommended reading order

1. [Problem, object and model hypothesis](01-problem-and-model.md): Why does CDM provide attribute portraits, and what inputs do DINA require.
2. [Q matrix and ideal response](02-q-matrix-and-ideal-response.md): Explain \(\alpha,q,\eta\) and AND gate letter by letter.
3. [response probability and likelihood](03-response-function-and-likelihood.md): guess, slip, local independence, conditional likelihood and marginal likelihood.
4. [Differences among three estimated routes](04-estimation-overview.md): JML, marginal ML/EM, HO-DINA/MCMC.
5. [EM complete derivation of](05-em-algorithm.md): E step, expectation count, A10--A11 closed-form update and complexity.
6. [standard error and classification](06-standard-errors-and-classification.md): Appendix A12--A15, observation information matrix and posterior attribute profile.
7. [HO-DINA and MCMC](07-ho-dina-and-mcmc.md): Higher-order capabilities, attribute dependencies, parameter dimensionality reduction, and paper evidence boundaries.
8. [Simulation experiment](08-simulation.md): complete experimental design, Q matrix, running settings and Table 2 results.
9. [Real data of fraction subtraction](09-fraction-subtraction.md): 2,144 students, 15 questions, Table 3--4 and result explanation.
10. [Code Implementation Intensive Reading](10-code-implementation.md): The original Ox implementation status is mapped piece by piece with the EM recurrence script of this site.
11. [Two complete EM iterations](11-worked-example.md): four students, all class likelihoods, posteriors, expected counts, g/s updates, and likelihood checks.
12. [Limitations and Future Work](12-limitations-and-future.md): Fixed Q, exponential complexity, fixed prior and classification research problem.
13. [Symbol table](13-symbols.md): Unified query of full-text symbols, dimensions and code objects.
14. [Summary and follow-up reading](14-summary.md): Paper contribution, strength of conclusions, and route to G-DINA.
15. [Reference](references.md): Original text and directly relevant sources.

## What algorithm details does the paper really provide?

|part|The level of detail in this article|
| --- | --- |
| DINA EM |Appendix complete derivation parameter update and standard error|
|Saturated attribute profile distribution|gives the marginal form of class \(2^K\)|
| HO-DINA |Gives the distribution of higher-order attributes and the number of parameters|
| MCMC |State the purpose and cite de la Torre & Douglas (2004), this article does not rewrite the sampler|
|Ox program|Instructions are available from the author; the paper does not have a public download address.|

This site will not use subsequent software to replace the original algorithm. `tools/de_la_torre_2009_dina_em.py` is written as a runnable teaching implementation in the appendix, and the differences from the original Ox code are clearly listed.
