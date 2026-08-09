# Gu and Xu (2021) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Yuqi Gu & Gongjun Xu. *Sufficient and Necessary Conditions for the Identifiability of the Q-matrix* |
|Journal| *Statistica Sinica*, 31, 449--472 |
| DOI | [10.5705/ss.202018.0410](https://doi.org/10.5705/ss.202018.0410) |
|Formal paper|[Journal page](https://www3.stat.sinica.edu.tw/statistica/j31n1/j31n118/j31n118.html) · [24 pages PDF](https://www3.stat.sinica.edu.tw/statistica/oldpdf/A31n118.pdf)|
|Main text and supplementary materials|[arXiv:1810.03819](https://arxiv.org/abs/1810.03819), 83 pages, including all proofs and Simulation Studies I--VII|
|official code|[`yuqigu/Identify_Q`](https://github.com/yuqigu/Identify_Q), MATLAB condition checker and simulation code|
|Verification on this site| [`tools/gu_xu_2021_identifiability_check.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/gu_xu_2021_identifiability_check.py) |

## One sentence conclusion

When \(Q\) is also unknown, \(Q\), error parameter, guessing parameter and latent class proportion in the DINA model can be strictly jointly identified if and only if \(Q\) simultaneously satisfies completeness A, column mutuality after removing a set of unit arrays B, and repeatability C with each attribute appearing at least three times.

The paper also explains two layers of finer boundaries:

- DINA's general recognition can be established when individual attributes are measured by only two questions, and the conclusion depends on whether the \(q\)-vector shape and latent class proportion of the two questions fall on the zero test set;
- Generally, the universal recognition of RLCM can be guaranteed by the D/E condition of "two universal holon matrices + remaining questions covering all attributes".

## What does this paper answer?

```text
Observed response distribution
      │
      ├── Can the item parameters and latent class proportions under known Q be restored?
      │
      └── When Q is also unknown, can Q, item parameters and latent class proportions be restored at the same time?
                         │
                         ├── Strict identification: all legal parameter points are unique
                         └── Universal recognition: almost unique everywhere except zero test set
```

This article addresses the second question. It shares the A/B/C condition name with Gu and Xu's paper on "DINA Parameter Identification of Known \(Q\)", and has differences in study population and conclusion strength.

## Recommended reading order

1. [Research questions, contributions and evidence boundaries](01-question-contribution.md)
2. [Relationship with existing identification result](02-prior-work.md)
3. [RLCM data-generating process and all objects](03-rlcm-setup.md)
4. [DINA, G-DINA and general RLCM](04-dina-gdina.md)
5. [Strict identification, general identification and column label exchange](05-identifiability-definitions.md)
6. [Example of general recognition of four questions and two attributes](06-q42-generic-example.md)
7. [T-matrix and identification equivalent formula](07-t-matrix.md)
8. [Zero rows, monotonicity and equivalence relations](08-preliminaries.md)
9. [Theorem 1: A/B/C Necessary and Sufficient](09-theorem1-overview.md)
10. [Condition A: Integrity](10-condition-a.md)
11. [Condition B: The columns of \(Q^\star\) are different from](11-condition-b.md)
12. [Condition C:](12-condition-c.md) at least three times for each attribute
13. [The minimum number of questions and \(K=8,J=12\) construct](13-minimum-items.md)
14. [Theorem 1’s proof route](14-theorem1-proof.md)
15. [Theorem 2: Three structures](15-theorem2.md) when measured only twice
16. [Complete pan-recognition characterization of \(K=2\)](16-k2-characterization.md)
17. [The necessity of repeatability in general RLCM](17-general-rlcm-theorem3.md)
18. [Universal completeness and bipartite graph matching](18-generic-completeness.md)
19. [Theorem 4: D/E pan-recognition condition](19-theorem4.md)
20. [Theorem 5 and \(K=2\) necessary and sufficient conditions](20-theorem5.md)
21. [Finite sample error bound](21-finite-sample.md)
22. [Experiment: Main text pan-recognition simulation](22-main-simulation.md)
23. [Experiment: Supplementary Material Co-Design](23-supplement-design.md)
24. [Experiment：DINA Studies I--II](24-studies1-2.md)
25. [Experiment：DINA Studies III--IV](25-studies3-4.md)
26. [Experiment：G-DINA Study V](26-study5.md)
27. [Experiment：G-DINA Studies VI--VII](27-studies6-7.md)
28. [Official condition check code intensive reading](28-code-condition-checkers.md)
29. [Official simulation code intensive reading](29-code-simulations.md)
30. [This site can calculate verification and code review](30-computational-check.md)
31. [Limitations, conclusions and future work](31-limitations-conclusion-future.md)
32. [Symbol table](32-symbol-table.md)
33. [References and Sources](references.md)

## You should be able to answer after reading

- Why are "parameter identification of known \(Q\)" and "joint identification of unknown \(Q\)" two questions?
- Which observational equivalence does A, B, and C exclude?
- Why does DINA's strict identification only require one set of \(I_K\), but still requires less than \(2K+1\) questions?
- In the four-question two-attribute example, why is \(p_{00}p_{11}=p_{01}p_{10}\) equivalent to two independent attributes?
- How to order local general recognition, global general recognition and strict recognition?
- Why can "pan-completeness" in general RLCM be written as a bipartite graph perfect match?
- Are each of the seven sets of simulations verifying adequacy, necessity, or the phenomenon of zero test sets?
- Where are the judgment logic, calculation bottlenecks and annotation bias of the official MATLAB code?
