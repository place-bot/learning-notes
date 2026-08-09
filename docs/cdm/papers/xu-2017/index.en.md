# Xu (2017) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Gongjun Xu. *Identifiability of Restricted Latent Class Models with Binary Responses*. |
|Journal| *The Annals of Statistics*, 45(2), 675--707, 2017 |
| DOI | [10.1214/16-AOS1464](https://doi.org/10.1214/16-AOS1464) |
|Journal page| [Project Euclid](https://projecteuclid.org/journals/annals-of-statistics/volume-45/issue-2/Identifiability-of-restricted-latent-class-models-with-binary-responses/10.1214/16-AOS1464.full) |
|open version| [arXiv:1603.04140](https://arxiv.org/abs/1603.04140) |
|Original code|The paper does not report a public code base; this site provides computable verification scripts|

## One sentence conclusion

For the bipartite response Q-restricted latent class model defined in the paper, if the Q matrix contains two \(I_K\) blocks after item reordering, and the remaining items can distinguish each single attribute class \(\boldsymbol e_k\) from the zero attribute class \(\boldsymbol 0\), then the item parameters matrix \(\Theta\) and attribute distribution \(\boldsymbol p\) all have **strict identifiability**.

## Main line of the paper

\[
\text{Observed response distribution}
\Longleftrightarrow
T(Q,\Theta)\boldsymbol p
\overset{\mathrm{C1,C2}}{\Longrightarrow}
(\Theta,\boldsymbol p)\text{only}.
\]

Among them:

- \(T(Q,\Theta)\) collects the marginal probability of "all correct answers for a subset of items";
- C1 provides two sets of single-attribute anchor questions;
- C2 lets the remaining items distinguish \(\boldsymbol 0\) from each \(\boldsymbol e_k\);
- a reversible row transformation \(D(\boldsymbol\theta^*)\) that cancels selected \(T\)-matrix elements to zero;
- Prove that zero attribute columns are first identified, then single attribute columns are identified, and finally all \(2^K\) potential classes are classified according to the number of attributes.

## Recommended reading order

1. [Problem, Contribution and Evidence Boundaries](01-question-and-scope.md)
2. [RLCM model and local independence](02-model-setup.md)
3. [Q matrix restriction and monotonicity](03-q-restrictions.md)
4. [How does the six-category diagnostic model enter the framework](04-model-examples.md)
5. [Definition of strict identifiability](05-identifiability.md)
6. [Margin \(T\)-Matrix](06-t-matrix.md)
7. [Complete Q matrix and ideal response](07-completeness.md)
8. [C1, C2 and three sets of \(I_K\)](08-conditions-c1-c2.md)
9. [Main Theorem and Test Design Implications](09-main-theorem.md)
10. [Proposition 3: Reversible translation transformation](10-transform.md)
11. [Proof step 1--2](11-proof-steps-one-two.md)
12. [Proof step 3--5](12-proof-steps-three-five.md)
13. [Two technical lemmas](13-lemmas.md)
14. [C1 Counterexample](14-counterexample.md) that alone is not sufficient
15. [From identifiability to consistency](15-consistency.md)
16. [Original Evidence and Experiment Boundary](16-experiment-and-evidence.md)
17. [Code implementation and computable verification](17-computational-check.md)
18. [Limitations, subsequent corrections and future work](18-limitations-and-future.md)
19. [Symbol table](19-symbols.md)
20. [Summary and follow-up reading](20-summary.md)
21. [Reference](references.md)

## Four things to distinguish repeatedly when reading

|level|objects in the paper|Questions that can be answered|
| --- | --- | --- |
|observation layer| \(P(\boldsymbol R=\boldsymbol r)\) |What can be known with unlimited samples?|
|latent layer| \(\boldsymbol\alpha\in\{0,1\}^K\) |Which attribute profile does the student belong to?|
|parameter layer| \(\Theta,\boldsymbol p\) |Can the item response pattern and group composition be uniquely restored?|
|design layer| \(Q\)、C1、C2 |Which test structures ensure that parameters are unique|

This paper studies parameter identification of population models. It does not study the real-time topic selection of CAT on a person-by-person basis, nor does it provide item selection criteria. Its value for CAT lies at the level of reaction model and item bank design: if the underlying diagnostic model lacks identifiability, no matter how sophisticated the adaptive policy is, it may be based on a student model that cannot be uniquely estimated.
