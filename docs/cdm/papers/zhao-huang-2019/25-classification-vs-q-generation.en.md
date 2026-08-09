# The gap between text classification and complete Q matrix generation

## 1. Actual output of the paper

Experiment categories are:

\[
y_j\in\{O,M\}.
\]

Output Q behavior:

\[
(1,0)
\quad\text{or}\quad
(0,1).
\]

This is equivalent to binary classification.

## 2. Space for complete Q lines

If there are \(K\) attributes, the general non-zero Q line space is

\[
\mathcal Q
=
\{0,1\}^K\setminus\{\boldsymbol0\}.
\]

The scale is

\[
|\mathcal Q|=2^K-1.
\]

When \(K=9\):

\[
2^9-1=511.
\]

The one-hot limit keeps only 9 of them.

## 3. Three different tasks

### 3.1 Single label multi-classification

\[
\sum_k q_{jk}=1.
\]

The model is selected in the \(K\) class.

### 3.2 Multi-label classification

\[
\sum_k q_{jk}\ge1.
\]

Output binary labels for each column independently or jointly.

### 3.3 Structured Q generation

In addition to predicting each column, also add:

- attribute hierarchy;
- Allow/disallow combinations;
- Question type rules;
- Q identifiability condition;
- item bank coverage constraints;
- CDM fit feedback.

## 4. Why "classification accuracy" is not equal to "Q available"

Even if a cell is highly accurate, a few critical errors can still break it:

- Completeness of a certain attribute;
- The number of measurements for each attribute;
- Distinguishing attribute columns;
- Students master pattern recognition;
- Content coverage for CAT.

Hence the need for matrix-level assessment.

## 5. Recommended assessment levels

```text
Layer 1: Text labels
  precision / recall / macro-F1 / exact match
          │
Layer 2: Q Structure
  Completeness, repeatability, column differentiation, attribute coverage
          │
Layer 3: CDM fitting
  log-likelihood / AIC / BIC / item fit
          │
Layer 4: Diagnostic results
  Attribute classification consistency rate, reliability, calibration
          │
Tier 5: CAT
  Test length, diagnostic accuracy, content coverage, exposure
```

## 6. Reasonable output of text model

More useful than hard tags are:

\[
p_\psi(\boldsymbol q_j\mid d_j)
\]

or probability per column

\[
p_\psi(q_{jk}=1\mid d_j).
\]

Downstream modules can retain uncertainty, deciding:

- Automatic acceptance;
- Quick confirmation from experts;
- Full discussion;
- Prioritize collection of reaction data.

## 7. The historical value of this paper

It verifies that question stem vocabulary can indeed predict some cognitive attributes, and provides an early task paradigm for subsequent deep learning, pretraining language model and multi-modal Q generation.

## 8. How to accurately interpret the title

The automated Q-matrix identification in the article can be understood as:

> Use the labeled items to train a text classifier to generate one-hot Q-line candidates for new questions.

It does not estimate the number of unknown attributes, nor does it identify statistical Q from student responses.
