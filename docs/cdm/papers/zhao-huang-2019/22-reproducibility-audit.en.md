# Reproducibility audit: the paper does not report implementation choices

## 1. Public materials

Available:

- ACM 5 page official PDF;
- Figure 1, Figure 2 and Tables 1--3 in the paper;
-Algorithm formula and overall process.

Not obtained:

- 1,069 question texts;
- 805 experimental question texts;
- Q tag;
- training/validation/testing index;
- source code;
- Supplementary materials;
- Question-by-question predictions.

Neither the paper nor the ACM page gives code/data availability.

## 2. Data processing gap

- `jieba` version;
- User dictionary;
- stop words;
- Punctuation and number processing;
- How to convert graphic questions into text;
- Formula, unit and special character processing;
- Processing of near-duplicate questions.

## 3. Feature engineering gap

- Is the characteristic variable of IG binary occurrence, word frequency or TF--IDF;
- Whether IG is only calculated in the training set;
- The fitting range of vocabulary and IDF;
- TF--IDF formula;
- normalization;
- bigram/trigram vocabulary size;
- \(k\) final selection for each configuration.

## 4. Model gap

- `SVC` or `LinearSVC`;
- SVM kernel；
- LR solver；
-`var_smoothing` for Gaussian NB;
- Category weight;
- sklearn version;
- Convergence status.

## 5. Experimental Gap

- Random seed;
- Exact number of questions for the three subsets;
- Count of each category in each subset;
- Use accuracy or F1 when selecting \(k\);
- Whether to select \(k\) for each model separately;
- Whether the same test set is used for all tables;
- Whether to repeat random division.

## 6. result gap

- confusion matrix;
- precision/recall/F1 per category;
- macro-F1；
-confidence interval;
- Verification curve of \(k\);
- Complete list of features;
- Question-by-question error analysis.

## 7. Potential information leakage points

If the execution order is:

```text
All 805 questions on building vocabulary and calculations IG
            ↓
Divide train/validation/test
```

The test label will participate in feature selection.

The strict order should be:

```text
Divide first
   ↓
Only training set fits vocabulary, IDF, IG and model
   ↓
Validation set select k
   ↓
test set final evaluation
```

The original text cannot confirm which order the author used.

## 8. Official code search

As of 2026-07-26:

- Searching the GitHub repository of the paper title and DOI did not find a matching item;
- There is no code link between the author page and the ACM page;
- The ResearchGate page displays no full-text attachments and no code.

Therefore, this site provides method reconstruction and numerical auditing, and is clearly marked as an independent implementation.

## 9. Reproduction level

|Hierarchy|Current status|
| --- | --- |
|Formulas and Processes Restated|OK|
|Table number verification|OK|
|Data scale and baseline calculation|OK|
|Approximate reconstruction of original algorithm|OK|
|Value-by-value reproduction Tables 1--3|Unable to complete without data and source code|
|External item bank verification|new data needed|
