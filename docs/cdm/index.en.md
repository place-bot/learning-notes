# CDM paper study route

The cognitive diagnosis model (Cognitive Diagnosis Models, CDM) partition is organized by paper study. The current paper library contains 86 articles,
Divided into eight categories; each article will have a BOBCAT-level multi-page intensive reading topic. The navigation adopts "Paper Category → Single Paper →
"Guidance/Model/Formula/Proof or Algorithm/Experiment/Code/Summary" level, see the completion status
[The total progress of intensive reading of a single paper is](papers/index.md).

The writing language is mainly Chinese, and English brackets are retained for important terms that appear for the first time, such as Q-matrix, identifiability, latent class model, restricted latent class model (RLCM), partial mastery and tensor decomposition.

## Reading order

1. Read the theoretical background first: latent structure models, finite mixture models, nonparametric mixture models and generic identifiability language.
2. Read mathematical tools again: Kruskal’s three-way array uniqueness and graphical models.
3. Supplement the background of HMM, network and machine learning: These are not the main line of CDM, but they can help understand hidden states, block models and EM-like learning.
4. Enter the CDM main line: DINA, DINO, G-DINA, LCDM, GDM, Fusion Model and GDINA software framework.
5. Intensive reading of Q matrix, identifiability, estimation and regularization: This is the most critical theoretical and algorithmic support for subsequent writing of continuous-Q or exploratory CDM.
6. Finally read the continuous and extended models: partial mastery, continuous attributes, continuous responses and general-response models.

## Special page

|order|Topics|Current use|
| --- | --- | --- |
| 1 |[Latent structure and mixture model](theoretical-background.md)|Establish a theoretical foundation for identifiability and hybrid models|
| 2 |[Math Tools](mathematical-tools.md)|Summarizing proof tools and geometric languages|
| 3 |[HMM, network and machine learning background](hmm-network-ml.md)|Place auxiliary background without mixing into the CDM main line|
| 4 |[Core model](core-models.md)| DINA、DINO、G-DINA、LCDM、GDM、Fusion Model |
| 5 |[Q Matrix Verification and Learning](q-matrix.md)|Q-matrix verification, learning, partially known Q-matrices, and AI-assisted methods|
| 6 |[identifiability theory](identifiability.md)|Identification theorem, necessary and sufficient conditions and generic identifiability of CDM and RLCM|
| 7 |[Estimation, regularization and calculation](estimation-computation.md)|Regularization, joint MLE, high-dimensional attribute profile, structure learning|
| 8 |[Continuous and extended model](continuous-extensions.md)| partial mastery、continuous response、general-response CDM |
| 9 |[Paper index](paper-index.md)|Summary list of all papers included in the reading plan|
| 10 |[Total progress of intensive reading of a single paper](papers/index.md)|Completion status and production order of 86 papers in eight categories|

## Single paper template

Each paper adopts a multi-page structure, with page names adapted to theory, method, software or book type:

```text
Paper Category/
└── Author year/
    ├── Reading Guide
    ├── Problems and theoretical basis
    ├── Model settings and symbols
    ├── Key formulas, theorems or algorithms
    ├── Proof details or hand calculation examples
    ├── Experiments, results and evidence boundaries
    ├── Intensive reading of the official code may be computable and reproducible
    ├── Relationship with CDM main line
    ├── Summary
    └── References
```

When a theoretical paper does not have empirical experiments or official code, the corresponding page will clearly record this fact and use theorem evidence and computable checks.
Replace, do not fill in the result that does not exist in the original text.
