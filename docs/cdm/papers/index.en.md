#CDM Overall progress of intensive reading of a single paper

The CDM paper database currently contains **86 papers**. Each article is made into multi-page notes according to the depth of the BOBCAT topic, and adopts a four-layer structure in the navigation:

```text
CDM
└── Intensive reading of a single paper
    └── Paper category
        └── Author and year
            ├── Reading Guide
            ├── Problems and Basics
            ├── Models and symbols
            ├── formula, theorem or algorithm
            ├── Proof or hand calculation example
            ├── Experiments and results
            ├── Code implementation
            ├── Summary
            └── References
```

The page name will be adjusted according to the paper type:

- Theoretical papers: focus on theorems, proofs, counterexamples, evidence boundaries and computable recurrence;
- Method papers: focusing on objective functions, estimation algorithms, experiments, ablation and official codes;
- Software papers: focus on interfaces, object structures, calculation processes, examples and implementation mapping;
- Books: Split by chapters related to CDM, and clarify the chapters actually covered by this topic.

## Current progress

|Category|Quantity|Completed|Current status|
| --- | ---: | ---: | --- |
|[Latent structure and mixture model](categories/latent-structure-mixtures.md)| 18 | 1 |Allman et al. (2009) First version completed|
|[Math Tools](categories/mathematical-tools.md)| 3 | 1 |Kruskal (1977) Completed first edition|
|[HMM, network and machine learning](categories/hmm-network-ml.md)| 15 | 0 |To be produced one by one|
|[CDM core model](categories/core-models.md)| 10 | 2 |de la Torre (2009, 2011) first edition completed|
|[Q Matrix Verification and Learning](categories/q-matrix.md)| 14 | 7 |de la Torre (2008), de la Torre & Chiu (2016), Liu et al. (2012, 2013), Chen et al. (2018), Gu & Xu (2021), Zhao & Huang (2019) The first edition has been completed|
|[identifiability theory](categories/identifiability.md)| 9 | 1 |Xu (2017) Completed first edition|
|[Estimation, regularization and calculation](categories/estimation-computation.md)| 5 | 0 |To be produced one by one|
|[Continuous and extended model](categories/continuous-extensions.md)| 8 | 0 |To be produced one by one|
|**Total**| **86** | **12** |Continuous updates|

## Production order

The production order takes into account both dependencies and the CDM mainline:

1. Allman, Matias and Rhodes (2009): Three-block tensor identification general entrance;
2. Kruskal (1977): The mathematical core of the uniqueness of three-way decomposition;
3. de la Torre (2009): DINA model and estimation;
4. de la Torre (2011): G-DINA framework;
5. Xu (2017): Bipartite RLCM identifiability (completed);
6. de la Torre (2008): Empirical Q-matrix validation of DINA (completed);
7. de la Torre and Chiu (2016): General empirical Q-matrix validation (completed);
8. Liu, Xu and Ying (2012): Data-driven Q-matrix learning (completed);
9. Liu, Xu and Ying (2013): Self-learning Q matrix theory (completed);
10. Chen, Culpepper, Chen and Douglas (2018): Bayesian DINA Q matrix estimation (completed);
11. Gu and Xu (2021): Necessary and sufficient conditions for Q matrix to be identifiable (completed);
12. Zhao and Huang (2019): Automatic recognition of Q matrix for text classification (completed);
13. Qin and Guo (2024): machine learning improves Q matrix verification (next article);
14. High-dimensional estimation, regularization and structure learning;
15. partial mastery, continuous-Q and general-response extensions;
16. HMM, random graph and machine learning background;
17. Remaining mixture models and sources of identification theory.

Detailed listings within the same category retain their original index order. For complete bibliographic information, see [General Index of Papers](../paper-index.md).

## Completion criteria

A paper is marked "completed" only if it meets the following conditions:

1. Check the original PDF, not the read-only summary;
2. Explain the core model symbol by symbol;
3. Connect key formulas into algorithms or proof chains;
4. Cover all major theorems or experimental tables;
5. Distinguish between the conclusion of the paper, the inference of this site and the speculation;
6. Complete the mapping of paper formulas to code objects when official code is available;
7. Clarify when there is no official code and provide appropriate computable checks;
8. Explain the interface with the CDM mainline and the conclusions that cannot be drawn;
9. Strict build and page rendering checks via MkDocs.
