# Detailed explanation of rule 7: mixed item format

Rule comparison

| CTT | IRT |
| --- | --- |
|Mixed item formats lead to unbalanced impact on test total score|Mixing item formats produces optimal quiz scores|

## 1. Definition and type of item format

item format (Item Format)

item response style and scoring criteria

**Common formats**:

**Two categories of items**:

- Examples: True/False, Yes/No questions
- Score: 0 points (wrong) or 1 point (correct)
- Advantages: Objective and easy to score
- Disadvantages: Limited amount of information

**Multiple selection items**:

- Example: Choose one of four ABCD
- Score: 0 points (wrong answer) or 1 point (correct answer)
- Advantages: Reduce the probability of guessing
- Disadvantages: still binary information

**Likertscaleitem**：

- Example: 1-5 points or 1-7 points evaluation
- Rating: continuous level score
- Advantages: Can capture degree differences
- Disadvantages: Strong subjectivity

**Open item**:

- Examples: essays, answer questions
- Rating: 0-10 or more complex scoring scale
- Advantages: rich information and high authenticity
- Disadvantages: subjective scoring and high cost

## 2. Why do we need mixed formats?

### 2.1 Diversity of measurement requirements

Suppose the measured characteristic is \(\theta\). If only one format is used, the information function is:

\[
I_{\text{single}}(\theta) = \sum_{i=1}^n I_i(\theta)
\]

If mixed format is used, the information function is:

\[
I_{\text{mix}}(\theta) = \sum_{i=1}^{n_1} I_{i,\text{Format 1}}(\theta) + \sum_{j=1}^{n_2} I_{j,\text{Format 2}}(\theta) + \cdots
\]

In theory, \(I_{\text{mixed}}(\theta)\) can provide more information over a wider range of \(\theta\).

### 2.2 Principle of information complementarity

For two-category items, the information function is:

\[
I_{\text{Two points}}(\theta) = P(\theta)[1-P(\theta)]
\]

Maximum point:

\[
\frac{dI}{d\theta} = \frac{dP}{d\theta}[1-2P(\theta)] = 0
\]

Get \(P(\theta) = 0.5\), the maximum value is \(I_{\max} = 0.25\)

For polytomous items (such as 5-point Likert), the information function is:

\[
I_{\text{Many points}}(\theta) = \sum_{k=0}^4 P_k(\theta)\left[\frac{\partial \ln P_k(\theta)}{\partial \theta}\right]^2
\]

Expand the logarithmic derivative:

\[
\frac{\partial \ln P_k(\theta)}{\partial \theta} = \frac{1}{P_k(\theta)} \frac{\partial P_k(\theta)}{\partial \theta}
\]

This function may have local maxima at multiple \(\theta\) values.

## 3. Fundamental issues with mixed formats in CTT

### 3.1 Complete derivation of implicit weights

CTT weight problem

The total score \(X_{\text{total}} = \sum_{i=1}^I X_i\) in CTT seems to have equal weight, but it is not.

**variance decomposition**:

\[
\text{Var}(X_{\text{total}}) = \text{Var}\left(\sum_{i=1}^I X_i\right)
\]

Expand to:

\[
\text{Var}(X_{\text{total}}) = \sum_{i=1}^I \text{Var}(X_i) + 2\sum_{i<j} \text{Cov}(X_i, X_j)
\]

Rewritten as a double sum:

\[
\text{Var}(X_{\text{total}}) = \sum_{i=1}^I \sum_{j=1}^I \text{Cov}(X_i, X_j)
\]

**Definition of item contribution**:

The contribution of item \(i\) to total scorevariance is the sum of its corresponding rows (or columns) in the covariance matrix:

\[
\text{Contribute}_i = \sum_{j=1}^I \text{Cov}(X_i, X_j) = \text{Cov}\left(X_i, \sum_{j=1}^I X_j\right) = \text{Cov}(X_i, X_{\text{total}})
\]

**Verify that the weight sum is 1**:

\[
\sum_{i=1}^I \text{Contribute}_i = \sum_{i=1}^I \text{Cov}(X_i, X_{\text{total}}) = \text{Cov}\left(\sum_{i=1}^I X_i, X_{\text{total}}\right) = \text{Var}(X_{\text{total}})
\]

**Actual weight formula**:

\[
w_{\text{actual},i} = \frac{\text{Cov}(X_i, X_{\text{total}})}{\text{Var}(X_{\text{total}})}
\]

Define using correlation coefficient:

\[
\text{Cov}(X_i, X_{\text{total}}) = r_{i,\text{total}} \cdot \sigma_i \cdot \sigma_{\text{total}}
\]

Substitute:

\[
w_{\text{actual},i} = \frac{r_{i,\text{total}} \cdot \sigma_i \cdot \sigma_{\text{total}}}{\sigma_{\text{total}}^2} = \frac{r_{i,\text{total}} \cdot \sigma_i}{\sigma_{\text{total}}}
\]

### 3.2 Energy Awakening Scale Example Analysis

Assume that the original score of item 10 is \(Y\), with a score range of 1-4, and the modified score is \(2Y\), with a score range of 2-8.

**Mean Change**:

\[
E[X_{\text{Modify}}] = E[X_{\text{original}} - Y + 2Y] = E[X_{\text{original}}] + E[Y]
\]

If \(E[Y] = 2.29\), then:

\[
E[X_{\text{Modify}}] = 22.33 + 2.29 = 24.62
\]

**Variance changes**:

\[
\text{Var}(X_{\text{Modify}}) = \text{Var}(X_{\text{original}} - Y + 2Y) = \text{Var}(X_{\text{original}} + Y)
\]

Since \(Y\) is contained in \(X_{\text{original}}\):

\[
\text{Var}(X_{\text{original}} + Y) = \text{Var}(X_{\text{original}}) + \text{Var}(Y) + 2\text{Cov}(X_{\text{original}} - Y, Y)
\]

Assume \(S = X_{\text{original}} - Y\) (the sum of the first nine items). Then:

\[
\text{Cov}(S, Y) = \text{Cov}(X_{\text{original}} - Y, Y) = \text{Cov}(X_{\text{original}}, Y) - \text{Var}(Y)
\]

### 3.3 Quantitative analysis of individual differences

For two individuals A and B with the same original total score:

\[
X_{\text{original},A} = X_{\text{original},B} = 30
\]

But the reaction pattern is different:

- A: The first 9 items are worth 27 points, and the 10th item is worth 3 points.
- B: 29 points for the first 9 items, 1 point for the 10th item

Modified differences:

\[
\Delta = X_{\text{Modify},A} - X_{\text{Modify},B} = (27 + 6) - (29 + 2) = 2
\]

Generalization: If the score difference for item \(i\) is \(\delta_i\) and the category number multiplier is \(m\), then:

\[
\Delta_{\text{total score}} = \delta_i \times (m-1)
\]

## 4. CTT’s traditional approach to handling mixed formats

### 4.1 Standardization processing

Questions about standardized methods

Convert each item to a standard score:

\[
Z_{ij} = \frac{X_{ij} - \mu_i}{\sigma_i}
\]

**Issue 1: Sample Dependencies**

In sample 1:

\[
Z_i^{(1)} = \frac{X_i - \mu_i^{(1)}}{\sigma_i^{(1)}}
\]

In sample 2:

\[
Z_i^{(2)} = \frac{X_i - \mu_i^{(2)}}{\sigma_i^{(2)}}
\]

Generally, \(Z_i^{(1)} \neq Z_i^{(2)}\)

**Question 2: Changes in related structures**

Original covariance:

\[
\text{Cov}(X_i, X_j) = E[(X_i - \mu_i)(X_j - \mu_j)]
\]

Covariance after normalization:

\[
\text{Cov}(Z_i, Z_j) = E\left[\frac{(X_i - \mu_i)}{\sigma_i} \cdot \frac{(X_j - \mu_j)}{\sigma_j}\right] = \frac{\text{Cov}(X_i, X_j)}{\sigma_i \sigma_j} = r_{ij}
\]

### 4.2 Divide by constant method

Let the original maximum score be \(M_i\), normalized to the common maximum score \(M\):

\[
X_i' = \frac{M}{M_i} \cdot X_i
\]

**Nonlinearity of the reaction function**:

Assume that the individual's true attitude is \(\theta\), and the reaction function is:

- 4-point scale: \(f_4(\theta)\)
- 8-point scale: \(f_8(\theta)\)

The linear assumption requires:

\[
f_8(\theta) = 2 \cdot f_4(\theta)
\]

But in practice this relationship usually does not hold.

## 5. Solutions for mixed formats in IRT

### 5.1 Generalized Partial Credit Model (GPCM)

GPCM model

\[
P_{ik}(\theta) = \frac{\exp\left[\sum_{j=0}^k a_i(\theta - b_{ij})\right]}{\sum_{h=0}^{m_i} \exp\left[\sum_{j=0}^h a_i(\theta - b_{ij})\right]}
\]

Among them:
- \(P_{ik}(\theta)\): The probability that an individual with ability \(\theta\) selects category \(k\) on item \(i\)
- \(a_i\): discrimination parameter of item \(i\)
- \(b_{ij}\): The \(j\)th threshold parameter of item \(i\)
- \(m_i\): The highest category number of item \(i\)

**Cumulative probability function**:

Define the accumulation function:

\[
\Psi_{ik}(\theta) = \sum_{j=0}^k a_i(\theta - b_{ij})
\]

Then:

\[
P_{ik}(\theta) = \frac{\exp[\Psi_{ik}(\theta)]}{\sum_{h=0}^{m_i} \exp[\Psi_{ih}(\theta)]}
\]

**Derivation of Marginal Probability**:

For the special case of two categories (\(m_i = 1\)):

\[
P_{i1}(\theta) = \frac{\exp[a_i(\theta - b_{i1})]}{\exp(0) + \exp[a_i(\theta - b_{i1})]} = \frac{1}{1 + \exp[-a_i(\theta - b_{i1})]}
\]

This is exactly the 2PL model.

### 5.2 Properties of threshold parameters

Threshold definition

The threshold \(b_{ij}\) is the ability point where adjacent categories have equal probabilities:

\[
P_{i,j-1}(b_{ij}) = P_{ij}(b_{ij})
\]

**Derivation of threshold equation**:

At \(\theta = b_{ij}\):

\[
\frac{\exp[\Psi_{i,j-1}(b_{ij})]}{\sum_h \exp[\Psi_{ih}(b_{ij})]} = \frac{\exp[\Psi_{ij}(b_{ij})]}{\sum_h \exp[\Psi_{ih}(b_{ij})]}
\]

Simplified to:

\[
\exp[\Psi_{i,j-1}(b_{ij})] = \exp[\Psi_{ij}(b_{ij})]
\]

\[
\Psi_{i,j-1}(b_{ij}) = \Psi_{ij}(b_{ij})
\]

This is not possible because of \(\Psi_{ij} > \Psi_{i,j-1}\).

**Correct Threshold Definition**:

The threshold is actually the intersection point of the cumulative probability function and needs to be solved numerically.

### 5.3 Complete derivation of information function

**Expected score**:

\[
E[X_i|\theta] = \sum_{k=0}^{m_i} k \cdot P_{ik}(\theta)
\]

**Score function (first derivative)**:

\[
\frac{\partial E[X_i|\theta]}{\partial \theta} = \sum_{k=0}^{m_i} k \cdot \frac{\partial P_{ik}(\theta)}{\partial \theta}
\]

Using the derivative formula of the polynomial logit model:

\[
\frac{\partial P_{ik}(\theta)}{\partial \theta} = a_i P_{ik}(\theta) \left[k - E[X_i|\theta]\right]
\]

Substitute:

\[
\frac{\partial E[X_i|\theta]}{\partial \theta} = a_i \sum_{k=0}^{m_i} k \cdot P_{ik}(\theta) \left[k - E[X_i|\theta]\right]
\]

\[
= a_i \left[\sum_{k=0}^{m_i} k^2 P_{ik}(\theta) - E[X_i|\theta]^2\right]
\]

\[
= a_i \cdot \text{Var}[X_i|\theta]
\]

**Information function (negative value of second derivative)**:

\[
I_i(\theta) = -\frac{\partial^2 \ln L}{\partial \theta^2} = \left[\frac{\partial E[X_i|\theta]}{\partial \theta}\right]^2 \cdot \frac{1}{\text{Var}[X_i|\theta]}
\]

Substitute:

\[
I_i(\theta) = a_i^2 \cdot \text{Var}[X_i|\theta]
\]

### 5.4 Optimal combination of mixed formats

**Total information function**:

\[
I_{\text{total}}(\theta) = \sum_{i=1}^I I_i(\theta) = \sum_{i=1}^I a_i^2 \cdot \text{Var}[X_i|\theta]
\]

**Optimization goals**:

Select the item collection \(S\) and the parameter \(\{a_i, b_{ij}\}\) such that:

\[
\min_{\theta \in [\theta_{\min}, \theta_{\max}]} I_{\text{total}}(\theta) \geq I_{\text{target}}
\]

This ensures sufficient measurement accuracy within the target capabilities.

## 6. Practical application guidance

Mixed Format Design Principles

**Measurement goal orientation**:

- Determine the capability range to be measured for each item
- Select the item format that best suits the range

**Complementary information functions**:

- Analyze information function shapes in different formats
- Ensure that the total information function covers the target capability range

**Threshold rationality verification**:

- Check monotonicity of threshold: \(b_{i1} < b_{i2} < \cdots < b_{i,m_i}\)
- Analysis threshold spacing: \(\Delta_{ij} = b_{i,j+1} - b_{ij}\)

**Discrimination Balance**:

- Monitoring discrimination distribution: \(\text{CV}(a) = \frac{\sigma_a}{\mu_a}\)
- Adjust item weight if necessary

**Specific steps**:

Predict the information contribution of each format:

\[
I_{\text{Format}}(\theta) = \sum_{i \in \text{Format}} I_i(\theta)
\]

Calculate measurement error:

\[
\text{SE}(\theta) = \frac{1}{\sqrt{I_{\text{total}}(\theta)}}
\]

Assess reliability:

\[
\rho(\theta) = \frac{I_{\text{total}}(\theta)}{I_{\text{total}}(\theta) + 1}
\]
