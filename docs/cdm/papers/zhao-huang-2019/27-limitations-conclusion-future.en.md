# Limitations, conclusions and future work

## 1. Conclusion of the author’s report

A three-stage text classification pipeline can automatically predict cognitive attributes using question stems. Information gain feature selection improves the performance of the three types of algorithms. Gaussian NB achieves: under the third-order \(n\)-gram combination:

\[
85.2\%\text{ accuracy},
\qquad
85.6\%\text{ weighted F1}.
\]

Based on this, the author believes that text classification has the potential to reduce the cost of labeling large item bank Q.

## 2. Limitations clearly stated by the author

### 2.1 Expert labels also have errors

Content experts may disagree on which attributes are required for the same question, often requiring multiple rounds of discussion. Machine learning can only approximate the standard provided by the training labels.

### 2.2 Limited data scale

Only two attributes are retained in the experiment. The authors plan to extend this to multiple cognitive attributes on larger data.

### 2.3 The method is more traditional

The author proposes to use deep neural networks in the future to allow the model to automatically extract text features and improve accuracy.

## 3. Limitations of this site’s supplements

### 3.1 Task Scope

The experiment is a short text binary classification with two mutually exclusive attributes, and there is still a distance between it and the general multi-hot Q lines.

### 3.2 Category Imbalance

The majority class accuracy of 82.7% shrinks the absolute gain of 85.2% to about 2.5 percentage points.

### 3.3 Small test set

The test set is likely to have only 81 questions, and one question is equivalent to approximately 1.24 percentage points.

### 3.4 Single random division

There are no repeated splits, cross-validation, error intervals, or significance tests.

### 3.5 Recurrence information

Data, code, final \(k\), random seeds, software versions and a lot of preprocessing details are missing.

### 3.6 Indicator formula

Equation (9) weights by predicted class size, which is inconsistent with sklearn weighted F1.

### 3.7 Downstream validity

The paper did not put the predicted Q into CDM or CAT, so it did not test the effects of student diagnosis, fitting and adaptive topic selection.

## 4. Stronger future experiments

### Data

- Multi-grade, multi-subject, multi-source item bank;
- Question stems, options, pictures, formulas and analysis;
- Independent annotation by multiple experts;
- Expose de-identified data and partitioned indexes.

### Model

- multi-label encoder；
- pretraining Chinese language model;
- Multimodal models;
- Joint coding of attribute description and question stem;
- Hierarchy and graph structure constraints;
- Joint learning of text prior and response likelihood.

### Review

- macro-F1, balanced accuracy, recall of each type;
- row exact match and Hamming loss;
- calibration；
- Expert time savings;
- CDM item fit and student classification;
- CAT test length, content coverage and exposure.

## 5. Towards the goal of human-machine collaboration

Automated systems can optimize:

\[
\text{Minimize Q error given human review budget}.
\]

For example, set reliability offloading:

|Model status|Operation|
| --- | --- |
|High reliability and consistent rules|Quick confirmation|
|mid-mountedreliability|Single expert review|
|Low reliability or property conflict|Multi-expert discussion|

This goal is closer to actual cost than simply maximizing classification accuracy.

## 6. Summary

The core value of this 5-page conference paper is to establish an early route: question stem semantics can participate in Q matrix construction. It provides preliminary feasibility evidence on real data, but also leaves key issues such as multi-label structure, reproducibility, statistical uncertainty and downstream measurement validity.

For CAT research, it is suitable to become an item content understanding module. Real-time adaptive is still guaranteed by the closed loop of "react to update student status - reselect the next question".
