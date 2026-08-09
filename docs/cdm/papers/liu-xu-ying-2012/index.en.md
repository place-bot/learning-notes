# Liu, Xu and Ying (2012) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Jingchen Liu, Gongjun Xu & Zhiliang Ying. *Data-Driven Learning of Q-Matrix*. |
|Journal| *Applied Psychological Measurement*, 36(7), 548--564 |
| DOI | [10.1177/0146621612456591](https://doi.org/10.1177/0146621612456591) |
| OnlineFirst | 16 August 2012 |
| Version of Record | 13 September 2012 |
|Open full text| [PubMed Central, PMC3733574](https://pmc.ncbi.nlm.nih.gov/articles/PMC3733574/) |
|Original code|Neither the main text nor the open version provides code repositories, software versions or random seeds.|
|This site reappears| [`tools/liu_xu_ying_2012_q_learning.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/liu_xu_ying_2012_q_learning.py) |

## One sentence conclusion

The paper converts each candidate Q matrix into a \(T\)-matrix, and uses it to predict the joint answer rate of single questions, question pairs, and even higher-order question groups; the more suitable the candidate Q,

\[
T_{\widehat{\boldsymbol c},\widehat{\boldsymbol g}}(Q)
\widehat{\boldsymbol p}
\]

The closer it is to the joint answer rate vector \(\boldsymbol\beta\) directly calculated in the sample. The algorithm starts from the expert's initial matrix \(Q_0\), changes only the entire row of q-vector for one question in each round, and selects the modification method that reduces the distance the most.

## What does this paper advance?

|Verified by existing experience|Data-driven learning in this article|
| --- | --- |
|Look at a certain distinguishing indicator topic by topic|Match the joint reaction moments of many question groups simultaneously|
|Usually make local corrections around a given q-vector|Treat the complete Q as a discrete optimization object|
|Indicators directly depend on some item grouping|Use \(T\)-matrix to write it uniformly as \(T(Q)\boldsymbol p\)|
|Main output: Topic-by-topic advice|Output the overall Q obtained by local search|

This article still needs a \(Q_0\) that is "close enough to the true value". Therefore, data-driven learning here is more suitable to be explained as overall calibration and structure search driven by reaction data.

## Recommended reading order

1. [Research questions, contributions and evidence boundaries](01-question-and-contribution.md)
2. [DINA model and all basic symbols](02-dina-setup.md)
3. [From complete reaction distribution to observable moments](03-observable-moments.md)
4. [B-vector and T-matrix](04-t-matrix.md)
5. [Complete hand calculation of three questions and two attributes](05-t-matrix-example.md)
6. [Objective function and three estimators](06-objective-functions.md)
7. [Unknown \(c,g,p\) and DINA EM](07-nuisance-estimation.md)
8. [Algorithm 1 Line-by-line hill climbing search](08-algorithm-one.md)
9. [T-matrix truncation and calculation amount](09-truncation-computation.md)
10. [Calibration of some known Q and new questions](10-partial-information.md)
11. [identifiability, label exchange and counterexample](11-identifiability.md)
12. [Simulation experiment co-designed with three Q](12-simulation-design.md)
13. [Table 1: sample size, number of attributes and recovery rate](13-main-simulation-results.md)
14. [Figures 1--2 with 4.5% early stop](14-early-stopping.md)
15. [Table 3: Related and Unbalanced Properties](15-correlated-attributes.md)
16. [Table 4: Single new question calibration](16-partial-information-results.md)
17. [Model verification, sample size and evidence boundary](17-model-validation.md)
18. [Open code status and implementation intensive reading](18-code-implementation.md)
19. [This site can calculate and reproduce](19-computational-reproduction.md)
20. [Limitations, conclusions and future work](20-limitations-conclusion-future.md)
21. [Symbol table](21-symbol-table.md)
22. [Summary and follow-up reading](22-summary.md)
23. [Reference and source check](references.md)

## You should be able to answer after reading

- What does each row and column of \(T\)-matrix represent?
- \(\boldsymbol\beta\) Why can it be calculated directly from the answer matrix?
- How do \(S(Q)\), \(\widehat S(Q)\) and DINA divide their work?
- Algorithm 1 Why does each round require approximately \(J2^K\) candidate evaluations?
- 4.5% Why does early stopping increase the true Q recovery rate in small samples?
- How should 94 in Table 1 and 98 in the text be handled?
- What additional conditions does the theoretical guarantee given by the paper rely on?
- Can this method discover the meaning of attributes from scratch?
