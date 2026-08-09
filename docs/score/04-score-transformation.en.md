# 4. Fraction transformation and interpretation

## 4.1 The necessity of scale transformation

### 4.1.1 Limitations of standardized scale

Why is transformation needed?

**IRT default scale**:

- In most IRT software, the ability value \(\theta\) is assumed to obey the standard normal distribution: \(\theta \sim \mathcal{N}(0, 1)\)
- means mean capability is 0 and standard deviation is 1
- The actual output ability estimate is usually within the interval \([-3, 3]\)

**Disadvantages of this scale**:

- Not intuitive to educators, students, or policymakers
- For example, a value like \(\theta = 1.3\) is difficult to understand what it actually means
- There are no clear signs such as "full score" and "passing line", making it difficult to make educational decisions

**Actual demand**:

- **Hundred-point system**: more suitable for teaching purposes, such as \([0, 100]\) score
- **SAT and other standardized test scores**: such as \([200, 800]\)
- **Grading system**: such as 1–9 scale, A–F grading system

---

## 4.2 Linear transformation formula

### 4.2.1 Basic transformation formula

linear transformation

**Linear transformation of ability parameter**:

\[
\theta^* = a\theta + b
\]

Among them:

- \(a > 0\): Control standard deviation (scale size)
- \(b\): Control the mean (overall offset)

**In order to keep the IRT model unchanged, the item parameters must also be transformed accordingly**:

- Discrimination transformation: \(\alpha^* = \dfrac{\alpha}{a}\)
- Difficulty change: \(\beta^* = a\beta + b\)
- guessing parameter remains unchanged: \(c^* = c\)

**Equivalence formula**:

\[
P(\theta^*, \alpha^*, \beta^*, c^*) = P(\theta, \alpha, \beta, c)
\]

This means that under the old and new scales, the probability of **examinee answering the question correctly remains unchanged**, and comparability is guaranteed.

---

**Derivation process: starting from the equivalence formula**

Assume the original model probability is:

\[
P(\theta) = c + (1 - c) \cdot \frac{1}{1 + \exp(-\alpha(\theta - \beta))}
\]

New model settings:

\[
\theta^* = a\theta + b
\]

Hope to satisfy:

\[
P(\theta^*; \alpha^*, \beta^*, c^*) = P(\theta; \alpha, \beta, c)
\]

Expand the new model expression:

\[
P(\theta^*) = c^* + (1 - c^*) \cdot \frac{1}{1 + \exp(-\alpha^*(\theta^* - \beta^*))}
\]

Let \(c^* = c\) be substituted into \(\theta^* = a\theta + b\):

\[
\frac{1}{1 + \exp(-\alpha^*(a\theta + b - \beta^*))} = \frac{1}{1 + \exp(-\alpha(\theta - \beta))}
\]

To make the exponents on both sides equal:

\[
-\alpha^*(a\theta + b - \beta^*) = -\alpha(\theta - \beta)
\]

Remove the negative sign and expand:

\[
\alpha^* a \theta + \alpha^* b - \alpha^* \beta^* = \alpha \theta - \alpha \beta
\]

Side-by-side comparison:

- Coefficient item: \(\alpha^* a = \alpha \Rightarrow \alpha^* = \dfrac{\alpha}{a}\)
- Constant item: \(\alpha^* b - \alpha^* \beta^* = -\alpha \beta\)

Recommended:

\[
\beta^\* = a\beta + b
\]

---

**Intuitive understanding**:

- After zooming in, reducing or panning \(\theta\), if you want to keep \(\theta - \beta\) unchanged, you must reversely scale \(\alpha\) and translate \(\beta\) simultaneously.
- This is **scale invariance** of IRT: the model only cares about the "ability - difficulty" difference

---

**Actual meaning**:

- Facilitate linking between different tests (score linking)
- \(\theta\) can be mapped to a more familiar fraction system (e.g. 0–100)
- Ensure that the transformed test results have the same explanatory power without relying on the norm group**

---

### 4.2.2 Common transformation examples

Transformations for practical applications

**T score scale**:

-The mean is 50 and the standard deviation is 10
- Transformation formula: \(\theta^* = 10\theta + 50\)
- item parameters:

\[
\alpha^* = \alpha/10,\quad \beta^* = 10\beta + 50
\]

**SAT score scale**:

-The mean is 500 and the standard deviation is 100
- Transformation formula: \(\theta^* = 100\theta + 500\)
- item parameters:

\[
\alpha^* = \alpha/100,\quad \beta^* = 100\beta + 500
\]

---

## 4.3 Unique interpretation of IRT scores

### 4.3.1 Explanation relative to item

The revolutionary nature of IRT explanation

**Traditional CTT model**:

- It can only tell "how many people you have passed"
- Completely dependent on the reference sample population (norm-referenced)
- Difficult to compare directly across time or tests

**How the IRT model is interpreted**:

- Does not rely on norms, but explains ability relative to item difficulty
- Example: \(\theta = 1.2\) means you have a 50% probability of answering a question with a difficulty level of 1.2
- So IRT is "item-referenced" and the explanation is more stable and intuitive

---

### 4.3.2 Special cases of Rasch model

Explanation of item centralization

**Rasch model settings**:

- Unify and standardize item difficulty to meet:

\[
\sum_{i=1}^{I} \beta_i = 0
\]

- That is, the average difficulty level of the entire test is 0

**Intuitive explanation**:

- \(\theta = 0\): The probability of answering the average difficulty item correctly is 0.5
- \(\theta = 1\): The probability of correctly answering an item that is 1 difficulty higher than the average is 0.5
- \(\theta = -1\): Can only answer items whose difficulty is 1 lower than the average (probability 0.5)

---

## 4.4 Test linking and comparability

### 4.4.1 Common item design

How to test link

**Anchor question method (common item equating)**:

- When designing two sets of tests, keep some "anchor questions" (same items)

For example:

- Test A contains items 1–30
- Test B contains items 21–50
- The public part is item 21–30

**Steps**:

1. Use anchor questions to fit the linear transformation relationship between A and B ability scales
2. Convert B’s ability estimate to A’s scale (or vice versa)
3. Achieve ability estimate alignment and comparable scores between different tests

---

## 4.5 Innovations in IRT Score Reporting

### 4.5.1 confidence interval report

probability statement

**Traditional Reporting Method**:

- \(\hat{\theta} = 1.2\), standard error \(SE = 0.3\)

**Improvement**:

- "Has 68% reliability, capability at \([0.9, 1.5]\)"
- "Has 95% reliability, capability at \([0.6, 1.8]\)"

**Advantages**:

- Let non-expert users more intuitively understand the uncertainty of estimates
- Suitable for teaching feedback, psychometrics and policy reports

---

### 4.5.2 Likelihood Ratio Report

relative likelihood

**Example statement**:

> "Based on your answering patterns, you are 10 times more likely to have an ability above 1.0 than below 0.0"

**Mathematical expression**:

\[
LR = \frac{L(\theta > 1.0 \mid \mathbf{u})}{L(\theta < 0.0 \mid \mathbf{u})}
\]

**Meaning**:

- Emphasize that one side is significantly more likely than the other
- Helps to make judgments on educational decisions such as "whether to pass or whether to master"
