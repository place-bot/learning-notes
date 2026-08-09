# Chen, Culpepper, Chen and Douglas (2018) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Yinghan Chen, Steven Andrew Culpepper, Yuguo Chen & Jeffrey Douglas. *Bayesian Estimation of the DINA Q Matrix*. |
|Journal| *Psychometrika*, 83(1), 89--108 |
| DOI | [10.1007/s11336-017-9579-4](https://doi.org/10.1007/s11336-017-9579-4) |
|Online publication and issue|Published online 2017; Issue Volume 83, Issue 1, March 2018|
|data|Tatsuoka fraction subtraction data, \(N=536\), \(J=20\)|
|Original supplementary code|[Yuguo Chen’s software page](https://publish.illinois.edu/yuguo/software/) provides C++, R and README|
|Subsequent R packages|[`tmsalab/edina`](https://github.com/tmsalab/edina), current code implements restricted Gibbs version and adds model diagnostics compared to \(K\)|
|Verification on this site| [`tools/chen_et_al_2018_bayesian_q_check.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/chen_et_al_2018_bayesian_q_check.py) |

## One sentence conclusion

The paper directly puts the unknown Q matrix into DINA's Bayesian hierarchical model, and limits the state space of MCMC to Q that meets three identifiable conditions; restricted Gibbs is significantly better than the other two samplers in the simulation of \(K=4\), and real data analysis also ensures that the final estimated Q is located in the identifiable space.

The entire calculation chain can be written as:

\[
Q^{(t-1)}
\longrightarrow
(\boldsymbol s^{(t)},\boldsymbol g^{(t)},\boldsymbol\alpha^{(t)},\boldsymbol\pi^{(t)})
\longrightarrow
Q^{(t)}\in\mathcal Q
\longrightarrow
\widehat Q.
\]

\(\mathcal Q\) is a discrete set of identifiable Q's. The algorithm first updates item parameters, student attribute profiles and latent class proportions in each round, and then updates Q in \(\mathcal Q\).

## The three most important points of this paper

### 1. Exploratory estimation of the entire Q

The input only requires a binary answer matrix and the number of attributes \(K\). The method does not require the expert to first give a Q that is close to the true value, nor does it need to make partial revisions around the expert's Q line by line.

### 2. identifiability goes into the sampler itself

Each retained Q sample satisfies:

1. After replacement, two sets of \(I_K\) are included;
2. Each attribute is required by at least three questions;
3. Each question requires at least one attribute.

Therefore, posterior sampling does not access unidentifiable states excluded by the paper.

### 3. Theory, experiment and code form a closed loop

The paper provides irreducibility and symmetry proofs of dependency proposals; simulates and compares restricted MH, restricted Gibbs and unconstrained Gibbs; the supplementary material provides Rcpp implementations of the three methods; the subsequent `edina` package encapsulates restricted Gibbs into an installable R interface.

## Recommended reading order

1. [Research questions, contributions and evidence boundaries](01-question-and-contribution.md)
2. [Relationship with existing Q learning methods](02-relation-to-prior-work.md)
3. [DINA model, data and all symbols](03-model-and-notation.md)
4. [ideal response, item response function and likelihood](04-dina-likelihood.md)
5. [Complete Bayesian Hierarchical Model](05-bayesian-hierarchy.md)
6. [Prior and complete conditional distribution of each layer](06-priors-and-conditionals.md)
7. [Three identifiable conditions of Q](07-identifiability-conditions.md)
8. [Why limit the posterior to the identifiable space](08-identified-space.md)
9. [Conditional posterior and uniform prior of Q](09-q-posterior.md)
10. [Overview of three types of candidate generators](10-proposal-overview.md)
11. [Independent proposal with DS1](11-independence-and-ds1.md)
12. [DS2 block dependency proposal to gradually dismantle](12-ds2.md)
13. [Theorem 1: Irreducibility](13-irreducibility.md)
14. [Theorem 2: Symmetry and Acceptance Rate](14-symmetry-and-acceptance.md)
15. [Metropolis-within-Gibbs complete algorithm](15-metropolis-within-gibbs.md)
16. [Restricted Gibbs complete algorithm](16-constrained-gibbs.md)
17. [Conditional probability derivation of single \(q_{jk}\)](17-q-full-conditional.md)
18. [Posterior mode of the entire Q and column permutation](18-posterior-summary.md)
19. [Experiment: Analog Design](19-simulation-design.md)
20. [Experiment: All results of Table 1](20-table1-results.md)
21. [Experiment: item parameters MSE and convergence](21-item-parameter-results.md)
22. [Experiment: Fractional Subtraction Data and Analysis Design](22-fraction-data.md)
23. [Experiment: Question-by-question result](23-fraction-k3.md) of \(K=3\)
24. [Experiment: Question-by-question result](24-fraction-k4.md) of \(K=4\)
25. [Original Supplementary Material Code Intensive Reading](25-original-code.md)
26. [Current `edina` package code intensive reading](26-edina-package.md)
27. [This site’s computable verification and code review found](27-computational-check.md)
28. [Limitations, conclusions and future work](28-limitations-conclusion-future.md)
29. [References, code and data sources](references.md)

## You should be able to answer after reading

- Q Why do we need two sets of unit formations?
- How do "at least three questions for each attribute" correspond to "two sets of unit arrays"?
- What does \(p(Q)\propto I(Q\in\mathcal Q)\) actually stipulate?
- Which 0's and 1's does DS2 pin in a column block?
- Which problem of MCMC do irreducibility and symmetry each solve?
- How can MH and restricted Gibbs share the same target posterior?
- Why does the mode of the entire Q need to eliminate column label swapping first?
- \(K=4\) How big of an advantage is time-limited Gibbs?
- Why is it only fitting \(K=3,4\) in the real data and not directly using the expert's 8 attributes Q?
- What are the substantial differences between the original supplementary code, the 2018 paper, and the current `edina` package?
