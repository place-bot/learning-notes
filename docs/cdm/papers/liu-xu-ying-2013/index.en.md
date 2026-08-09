# Liu, Xu and Ying (2013) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Jingchen Liu, Gongjun Xu & Zhiliang Ying. *Theory of Self-Learning Q-Matrix*. |
|Journal| *Bernoulli*, 19(5A), 1790--1817 |
| DOI | [10.3150/12-BEJ430](https://doi.org/10.3150/12-BEJ430) |
|Receive and revise manuscripts|Received in March 2011, revised in November 2011|
|Open full text| [PubMed Central, PMC4011940](https://pmc.ncbi.nlm.nih.gov/articles/PMC4011940/)；[arXiv:1010.6120](https://arxiv.org/abs/1010.6120) |
|Original code|The paper does not provide code repositories, software packages, simulation programs or data files|
|Verification on this site| [`tools/liu_xu_ying_2013_theory_check.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/liu_xu_ying_2013_theory_check.py) |

## One sentence conclusion

The paper proves that: under the conditions of complete Q, saturated \(T\)-matrix, all attribute profiles have positive probabilities, and each attribute is required by at least two questions, the response data is enough to separate the **column permutation equivalence class** of the true Q from other candidate Qs; by minimizing the distance with the empirical joint correct answer rate, this equivalence class can be restored with a probability approaching 1 as the sample size increases.

The core map can be condensed into:

\[
Q
\longrightarrow
T_{c,g}(Q)
\longrightarrow
T_{c,g}(Q)\boldsymbol p+p_0\boldsymbol g
\longrightarrow
\boldsymbol\alpha .
\]

Among them, \(\boldsymbol\alpha\) is directly calculated from response data, and \(\boldsymbol p\) is the attribute profile distribution. The true Q can generate the overall limit of \(\boldsymbol\alpha\); the column space of any non-equivalent candidate Q is at a positive distance from this limit. This "column space separation" forms the core of the consistency proof.

## What does this paper solve?

|question|The treatment given in the paper|
| --- | --- |
|Q's attribute column names are interchangeable|Define the goal as restoring the column replacement equivalence class of \(Q\)|
|Q lies in a discrete binary matrix space|Exhaustively enumerate candidates Q and profile the attribute distribution for each candidate|
|Potential properties are unobservable|\(\boldsymbol\alpha\) is composed of the combined correct answer rate of single questions and question groups.|
|DINA has mistakes and guesses|Construct \(T_{c,g}(Q)\), and then use linear transformation to eliminate the known \(\boldsymbol g\)|
|Master accuracy rate \(c_i\) Unknown|Moment estimation is used for directly identifiable \(c_i\), and profile optimization is used for the remaining components.|
|Estimate whether it will converge to true Q|Divided into noiseless, known \(c,g\), and unknown \(c\), the consistency theorem is given at three levels|

## Recommended reading order

1. [The relationship between problem, innovation and 2012 paper](01-question-contribution-and-2012.md)
2. [Basic model, sample and all objects](02-model-setup.md)
3. [ideal response, B-vector and T-matrix](03-ideal-response-and-tmatrix.md)
4. [Empirical moment \(\boldsymbol\alpha\) and overall mapping](04-alpha-and-moment-map.md)
5. [Objective function, Q estimator and calculation](05-objective-and-estimator.md)
6. [Complete hand calculation of three questions and two attributes](06-worked-example.md)
7. [Column replacement equivalence, completeness and saturation](07-equivalence-completeness-saturation.md)
8. [C1--C5: What does each condition control?](08-conditions-c1-c5.md)
9. [Theorem 2.4: Noiseless Consistency](09-theorem-2-4.md)
10. [Known errors and guessing parameter of DINA](10-known-cg-dina.md)
11. [Noise T-matrix and objective function](11-noisy-tmatrix-objective.md)
12. [Theorem 3.1: Known consistency of \(c,g\)](12-theorem-3-1.md)
13. [Unknown \(c\): General estimation and moment estimation](13-unknown-c-estimation.md)
14. [Combined estimator with Theorem 4.2](14-combined-estimator-theorem-4-2.md)
15. [Total line of all proofs](15-proof-roadmap.md)
16. [Propositions 6.1--6.2: Full column rank](16-full-rank-propositions.md)
17. [Propositions 6.3--6.6: Column space separation](17-column-space-separation.md)
18. [Lemma 6.7 and the matrix that eliminates guesses \(D\)](18-guessing-removal-transform.md)
19. [Proof of the three main theorems](19-main-theorem-proofs.md)
20. [Appendix proves the key role of C5](20-appendix-and-c5.md)
21. [Counterexamples, necessity and identification boundaries](21-counterexamples-and-boundaries.md)
22. [Saturation moment, search complexity and practical truncation](22-computation-and-truncation.md)
23. [Experiment: A complete inventory of the original evidence](23-experiment-and-evidence.md)
24. [Code status and implementation intensive reading](24-code-implementation.md)
25. [This site can calculate and verify](25-computational-check.md)
26. [Limitations, conclusions and future work](26-limitations-conclusion-future.md)
27. [Symbol table](27-symbol-table.md)
28. [Summary and follow-up reading](28-summary.md)
29. [Reference and source check](references.md)

## You should be able to answer after reading

- What do the rows, columns and values of \(T(Q)\) represent?
- Why does the noiseless case exclude the all-zero attribute column, but when there is a guess, it needs to be filled in?
- Why is Q's "recognizable" only accurate to column substitutions?
- Which step of proof did C1--C5 enter?
- \(\boldsymbol\alpha\) How to approach the global moment through the law of large numbers?
- Which problem of uniqueness and troubleshooting is solved respectively by full column rank and column space separation?
- Matrix \(D\) How to convert \(T_{c,g}(Q)\) into \(T_{c-g}(Q)\)?
- Theorem 4.2 Why can Q be guaranteed to be consistent, but \(\boldsymbol p\) cannot be automatically guaranteed to be consistent?
- Why is there no experimental results page in the original article? To what extent can the numerical verification of this site be supported?
