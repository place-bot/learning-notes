# Zhao and Huang (2019) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Shuai Zhao & Xiaoting Huang. *Automated Q-matrix Identification Using Text Classification Techniques* |
|meeting| *Proceedings of the 11th International Conference on Education Technology and Computers*, 273--277 |
| DOI | [10.1145/3369255.3369308](https://doi.org/10.1145/3369255.3369308) |
|meeting time|2019-10-28 to 2019-10-31, Amsterdam|
|ACM Records|[Paper page and 5 pages PDF](https://dl.acm.org/doi/10.1145/3369255.3369308); ACM page marked as Free access, the official launch date of the page record is 2020-01-21|
|data|1,069 third-grade math problems; only 805 of them with two high-frequency attributes were used in the experiment|
|official code|The paper does not provide a warehouse, data download address or supplementary materials; as of 2026-07-26, no public implementation by the author has been retrieved|
|Site code|[Numerical audit](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/zhao_huang_2019_audit.py) · [Leak-safe independent reconstruction](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/zhao_huang_2019_reimplementation.py)|

## One sentence conclusion

In this paper, the question text is represented by Chinese tokenization, \(n\)-gram, information gain word selection and TF--IDF, and then uses LR, linear SVM and Gaussian NB to predict the cognitive attributes of the item; the best result is NB's 85.2% accuracy and 85.6% weighted F1 under unigram+bigram+trigram.

This number needs to be read together with the experimental bounds:

- The original nine-attribute \(Q\) matrix is cut into a classification problem with two mutually exclusive attributes;
- 666 of the 805 questions are integer operations, and the accuracy for most categories is 82.7%;
- The best accuracy is improved by about 2.5 percentage points compared to the majority class baseline;
- The 10% test set is likely to have only 81 questions, and one question corresponds to approximately 1.24 percentage points;
- The weighted F1 formula printed in the paper uses predicted class size weighting, which is different from scikit-learn's true class support weighting definition.

## Where should this paper be placed in Q matrix research?

```text
Question stem text + a few expert tags
              │
              ▼
       Text supervised classifier
              │
              ▼
   Attribute tag for new question/first draft of line Q
              │
       ┌──────┴──────┐
       ▼             ▼
  Expert review of CDM data calibration
       └──────┬──────┘
              ▼
         Available Q matrices
```

This paper deals with **semantic annotation when new questions are entered into the database**. It does not use student response data, nor does it estimate DINA, G-DINA or other CDMs, nor does it conduct CAT question selection.

## Recommended reading order

1. [Research questions, contributions and evidence boundaries](01-question-contribution.md)
2. [Interface of CDM, Q matrix and text classification](02-cdm-q-context.md)
3. [Original data: 1,069 questions and nine attributes](03-data-1069.md)
4. [Experimental cut: 805 questions and two mutually exclusive categories](04-binary-reduction.md)
5. [Mathematical expression of supervised learning task](05-problem-formulation.md)
6. [Three-stage framework overview](06-three-stage-framework.md)
7. [Chinese tokenization and \(n\)-gram feature](07-tokenization-ngrams.md)
8. [Information gain feature selection](08-information-gain.md)
9. [TF--IDF item vector](09-tfidf.md)
10. [C-SVM’s objective function and implementation ambiguity](10-svm.md)
11. [Gaussian Naive Bayes](11-naive-bayes.md)
12. [L2 Logistic Regression](12-logistic-regression.md)
13. [Experiment: Data partition, \(k\) tuning and participation algorithm selection](13-experiment-design.md)
14. [Experiment: accuracy and weighted F1](14-performance-measures.md)
15. [Experiment: unigram result](15-results-unigram.md) of Table 1
16. [Experiment: unigram+bigram result](16-results-bigram.md) of Table 2
17. [Experiment: trigram result](17-results-trigram.md) of Table 3
18. [Keyword result and educational semantic explanation](18-feature-interpretation.md)
19. [Majority class baseline and class imbalance](19-imbalance-baselines.md)
20. [Small test set, resolution and uncertainty](20-finite-sample-uncertainty.md)
21. [Equation (9) weighted F1 audit](21-f1-equation-audit.md)
22. [Reproducibility audit: The paper does not report the implementation choice](22-reproducibility-audit.md)
23. [Independent code reconstruction: strict separation of training, verification and testing](23-independent-reimplementation.md)
24. [This site’s numerical verification and its output](24-computational-audit.md)
25. [The gap between text classification and complete Q matrix generation](25-classification-vs-q-generation.md)
26. [Interface with CDM, CAT and RecCAT](26-cdm-cat-interface.md)
27. [Limitations, conclusions and future work](27-limitations-conclusion-future.md)
28. [Symbol table](28-symbol-table.md)
29. [Reference and verification source](references.md)

## You should be able to answer after reading

- Why did the original \(Q\) of 1,069×9 end up as 805×2?
- Under what conditions is the task of the paper equivalent to binary classification?
- What are the responsibilities of \(n\)-gram, information gain and TF--IDF respectively?
- Why does feature selection have a much greater impact on NB than LR and SVM?
- How should the 85.2% accuracy and 82.7% majority class baseline compare?
- What is the difference between Equation (9) and scikit-learn weighted F1?
- To what extent can this paper support "automatically generate a complete multi-label \(Q\) matrix"?
- If the semantic model is integrated into CAT, which modules still need to be driven by students' question-by-question responses?
