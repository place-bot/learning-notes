# Overview of the three-phase framework

## 1. The process of the paper Figure 2

```text
Question text
   │
   ▼
Chinese tokenization and 1/2/3-gram candidates
   │
   ▼
Information gain sorting, retaining top-k
   │
   ▼
TF--IDF item vector
   │
   ├──────────┬──────────┐
   ▼          ▼          ▼
 C-SVM       LR      Gaussian NB
   └──────────┴──────────┘
              │
              ▼
        O/M attribute tag
              │
              ▼
        Two columns of one-hot Q rows
```

## 2. The first stage: feature selection

The goal is to find the most distinguishing words or phrases for the category from the large vocabulary.

Candidate features come from:

- unigram；
- unigram+bigram；
- unigram+bigram+trigram。

Each feature is ranked according to its mutual information with the category, retaining top-\(k\).

## 3. The second stage: item characterization

Each question is converted into a real value vector:

\[
\boldsymbol x_j
=
(x_{j1},\ldots,x_{jk}),
\]

Among them, \(x_{jr}\) is the TF--IDF weight of the \(r\)th retained feature.

## 4. The third stage: classification

Three algorithm learning

\[
\boldsymbol x_j\mapsto y_j.
\]

The paper compares their accuracy and weighted F1 under the same feature scheme.

## 5. Dependencies between the three stages

Three stages should be fitted to the training data:

```text
training set: vocabulary, IDF, IG sorting and model parameters after fitting tokenization
validation set: select k
test set: only final evaluation
```

If vocabulary, IDF or information gain is first calculated on all 805 questions, and then the test set is divided, the test information will enter the model selection process. The paper does not clearly report the fitting order, so strict separation needs to be proactively adopted when reproducing.

## 6. Advantages of frameworks

- Simple components and low calculation cost;
- Keywords can be read by experts;
- Can be trained with a small amount of labeled data;
- There is no need to wait for students to answer new questions;
- Can be combined with manual review process.

## 7. Frame boundaries

- Only use the question stem text;
- Does not process pictures, tables and formula structures;
- Do not use options and parsing;
- Do not use student responses;
- Does not express attribute hierarchy;
- The experiment outputs a single category;
- Probabilistic calibration and uncertainty triage are not expanded.

These boundaries determine that it is more suitable for preliminary screening of the library, rather than directly becoming the only source of final Q.
