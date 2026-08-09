# Rule 1: Measure standard error

Rule comparison

| CTT | IRT |
| --- | --- |
|The standard error of measurement error applies to all scores within a specific population|The standard error of measurement error varies with score, but can be generalized to multiple groups|

## 1. CTT standard error derivation

### 1.1 Basic model

Basic assumptions of CTT

\[X = T + E\]

- \(X\) = observation score
- \(T\) = True score
- \(E\) = Measurement error

**Three core assumptions**:
1. \(E(E) = 0\)
2. \(\rho(T,E) = 0\)
3. \(\rho(E_1,E_2) = 0\)

### 1.2 Derivation of standard error formula

**Step 1: Variance Decomposition**

\[\sigma_X^2 = \text{Var}(X) = \text{Var}(T + E) = \sigma_T^2 + \sigma_E^2 + 2\text{Cov}(T,E)\]

Due to \(\text{Cov}(T,E) = 0\):

\[\sigma_X^2 = \sigma_T^2 + \sigma_E^2\]

**Step 2: Reliability Definition**

\[r_{tt} = \frac{\sigma_T^2}{\sigma_X^2} = \frac{\sigma_T^2}{\sigma_T^2 + \sigma_E^2}\]

**Step 3: Solve for error variance**

\[\sigma_E^2 = \sigma_X^2 - \sigma_T^2 = \sigma_X^2\left(1 - \frac{\sigma_T^2}{\sigma_X^2}\right) = \sigma_X^2(1 - r_{tt})\]

CTT standard error formula

\[SE_{\text{msmt}} = \sigma_E = \sigma_X\sqrt{1 - r_{tt}}\]

**Features**: Same for all participants, regardless of ability level

### 1.3 Numerical Example

Given: \(\sigma = 15\), \(r_{tt} = 0.84\)

\[SE_{\text{msmt}} = 15\sqrt{1 - 0.84} = 15\sqrt{0.16} = 15 \times 0.4 = 6\]

**Meaning**: No matter the test score is 80 points or 40 points, the measurement error is 6 points.

## 2. Derivation of IRT standard error

### 2.1 Information function

Core concept: information function

\[SE(\theta) = \frac{1}{\sqrt{I(\theta)}}\]

The standard error is inversely proportional to the information function

### 2.2 Derivation of information function (Rasch model)

**Step 1: Log likelihood function**

Response to a single item \(u_i \in \{0,1\}\):

\[\ln L_i = u_i \ln P_i(\theta) + (1-u_i) \ln(1-P_i(\theta))\]

Among them:

\[P_i(\theta) = \frac{e^{\theta - b_i}}{1 + e^{\theta - b_i}}\]

**Step 2: First Derivative**

\[\frac{\partial \ln L_i}{\partial \theta} = u_i - P_i(\theta)\]

**Step 3: Second Derivative**

\[\frac{\partial^2 \ln L_i}{\partial \theta^2} = -P_i(\theta)[1-P_i(\theta)]\]

**Step 4: Fisher Information**

item information function

\[I_i(\theta) = -E\left[\frac{\partial^2 \ln L_i}{\partial \theta^2}\right] = P_i(\theta)[1-P_i(\theta)]\]

**Maximum information point**: When \(P_i(\theta) = 0.5\), \(I_i(\theta) = 0.25\)

### 2.3 Analysis of the properties of information function

| \(P_i(\theta)\) | \(I_i(\theta)\) |Measurement accuracy|
| --- | --- | --- |
| 0.5 | 0.25 |highest|
| 0.9 | 0.09 |lower|
| 0.1 | 0.09 |lower|
| 0.99 | 0.0099 |very low|

**Core Insight**: When item difficulty matches ability (\(\theta = b_i\)), the measurement is most accurate.

## 3. IRT composite reliability

### 3.1 Square of average standard error

\[\sigma_\theta^2 = \frac{1}{N}\sum_{j=1}^N [SE(\theta_j)]^2 = \frac{1}{N}\sum_{j=1}^N \frac{1}{I(\theta_j)}\]

### 3.2 Trait variation

\[\sigma^2 = \frac{1}{N}\sum_{j=1}^N (\theta_j - \bar{\theta})^2\]

### 3.3 Composite reliability formula

IRT compound reliability

\[r'_{tt} = 1 - \frac{\sigma_\theta^2}{\sigma^2}\]

**Explanation**:

- \(\sigma^2\) = total variation (difference in ability between participants)
- \(\sigma_\theta^2\) = Variation due to measurement error
- \(r'_{tt}\) = Proportion of true ability variation that can be explained

### 3.4 Numerical calculation example

Assume 5 participants: \(\theta = [-2, -1, 0, 1, 2]\), information function: \(I(\theta) = [1.0, 1.2, 1.5, 1.2, 1.0]\)

**Calculate \(\sigma_\theta^2\)**:

| \(\theta_j\) | \(I(\theta_j)\) | \(SE(\theta_j)\) | \([SE(\theta_j)]^2\) |
| --- | --- | --- | --- |
| -2 | 1.0 | 1.000 | 1.000 |
| -1 | 1.2 | 0.913 | 0.834 |
| 0 | 1.5 | 0.816 | 0.666 |
| 1 | 1.2 | 0.913 | 0.834 |
| 2 | 1.0 | 1.000 | 1.000 |

\[\sigma_\theta^2 = \frac{1}{5}(1.000 + 0.834 + 0.666 + 0.834 + 1.000) = 0.867\]

**Calculate \(\sigma^2\)**:

\[\bar{\theta} = 0, \quad \sigma^2 = \frac{1}{5}(4 + 1 + 0 + 1 + 4) = 2\]

**Composite reliability**:

\[r'_{tt} = 1 - \frac{0.867}{2} = 0.567\]

## 4. CTT vs IRT comparison summary

Key differences

**CTT limitations**:

- Single standard error, ignoring differences in abilities
- Reliance on specific samples
- Inability to differentiate between measurement accuracy at different ability levels

**IRT Advantages**:

- individualizedstandard error
- Sample independent
- Accurately locate the best measurement interval
