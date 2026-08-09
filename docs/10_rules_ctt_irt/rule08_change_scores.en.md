# Detailed explanation of Rule 8: The meaning of change scores

Rule comparison

| CTT | IRT |
| --- | --- |
|Change scores cannot be meaningfully compared when initial score levels are different|Change scores allow meaningful comparisons even when initial score levels are different|

## 1. Definition and importance of change score

Change Score

Measure changes in individual abilities before and after intervention

**Basic formula**:

\[X_{j,\text{change}} = X_{j2} - X_{j1}\]

Among them:

- \(X_{j1}\): Pretest score (before intervention) for individual \(j\)
- \(X_{j2}\): Posttest score (post-intervention) for individual \(j\)
- \(X_{j,\text{change}}\): Change score of individual \(j\)

**Typical application scenarios**:

- **Educational Research**: Learning effects before and after teaching intervention
- **Clinical Psychology**: Symptom changes before and after treatment
- **Rehabilitation Medicine**: Functional improvement before and after training
- **Organizational Psychology**: Performance improvement before and after training

**Why is change score so difficult to measure? **

Root cause: Change scores involve two measurements, errors accumulate, and differences in baseline levels affect the interpretability of change.

## 2. Three fundamental issues with change scores in CTT

### 2.1 Paradoxical Reliability

Bereiter (1963) Paradox

The lower the pre-test and post-test correlation, the higher the reliability of the change score!

**Full derivation**:

Settings:

- \(X_1 = T_1 + E_1\) (pre-test)
- \(X_2 = T_2 + E_2\) (post-test)
- \(D = X_2 - X_1\) (change score)
- \(T_D = T_2 - T_1\) (real change)

Reliability of change scores:

\[
r_{DD} = \frac{\sigma_{T_D}^2}{\sigma_D^2}
\]

**Step 1: Calculate the change score variance**

\[
\sigma_D^2 = \text{Var}(X_2 - X_1) = \sigma_1^2 + \sigma_2^2 - 2\sigma_{12}
\]

**Step 2: Calculate the true change variance**

\[
\sigma_{T_D}^2 = \text{Var}(T_2 - T_1) = \sigma_{T_1}^2 + \sigma_{T_2}^2 - 2\sigma_{T_1 T_2}
\]

**Step 3: Express the covariance of the observed scores**

\[
\sigma_{12} = \text{Cov}(T_1 + E_1, T_2 + E_2) = \text{Cov}(T_1, T_2) = \sigma_{T_1 T_2}
\]

(Assume that the error is not related to the true score, and the errors at different points in time are not related)

**Step 4: Final Reliability Formula**

\[
r_{DD} = \frac{\sigma_{T_1}^2 + \sigma_{T_2}^2 - 2\sigma_{T_1 T_2}}{\sigma_1^2 + \sigma_2^2 - 2\sigma_{12}}
\]

**Key Insight**: When \(\sigma_{T_1 T_2}\) is close to \(\sigma_{T_1}\sigma_{T_2}\) (i.e. the true scores are highly correlated):

- The numerator \(\sigma_{T_1}^2 + \sigma_{T_2}^2 - 2\sigma_{T_1 T_2}\) tends to 0
- The denominator \(\sigma_1^2 + \sigma_2^2 - 2\sigma_{12}\) decreases but does not tend to 0
- The entire ratio \(r_{DD}\) tends to 0

### 2.2 False negative correlation

**correlation coefficient calculation**:

\[
r(D, X_1) = r(X_2 - X_1, X_1) = \frac{\text{Cov}(X_2 - X_1, X_1)}{\sigma_D \sigma_1}
\]

**Expand covariance**:

\[
\text{Cov}(X_2 - X_1, X_1) = \text{Cov}(X_2, X_1) - \text{Cov}(X_1, X_1) = \sigma_{12} - \sigma_1^2
\]

**Final formula**:

\[
r(D, X_1) = \frac{\sigma_{12} - \sigma_1^2}{\sigma_D \sigma_1}
\]

**Conditions for negative correlation**:

When \(\sigma_{12} < \sigma_1^2\), that is, \(r_{12} < \frac{\sigma_1}{\sigma_2}\), the correlation is negative.

Special case: if \(\sigma_1 = \sigma_2\), then when \(r_{12} < 1\), the correlation must be negative!

**Proof of regression effect**:

Let \(X_2 = \alpha + \beta X_1 + \epsilon\), where \(\epsilon\) is the random error.

Then:

\[
D = X_2 - X_1 = \alpha + (\beta - 1)X_1 + \epsilon
\]

When \(\beta < 1\) (regression effect), \(D\) and \(X_1\) must be negatively correlated.

### 2.3 Different meanings of different initial levels

Consider a cognitive ability test on a 100-point scale:

- **Student A**: Improved from 30 points to 35 points (+5 points)
- **Student B**: Improved from 80 points to 85 points (+5 points)

**Analysis 1: Relative improvement**

- Student A: Relative improvement of \((35-30)/30 = 16.7\%\)
- Student B: Relative improvement of \((85-80)/80 = 6.25\%\)

**Analysis 2: Improvement of distance maximum**

- Student A: Improved by 5 points out of the remaining 70 points, improvement rate \(5/70 = 7.1\%\)
- Student B: Improved by 5 points out of the remaining 20 points, improvement rate \(5/20 = 25\%\)

**Analysis 3: Capability distribution location**

If the score distribution is normal distribution, \(\mu = 50, \sigma = 15\):

- Student A: Improved from \((30-50)/15 = -1.33\) standard deviation to \(-1.0\) standard deviation
- Student B: Improved from \((80-50)/15 = +2.0\) standard deviation to \(+2.33\) standard deviation

At the tail of the normal distribution, the same difference in scores represents a larger difference in ability.

## 3. Why does change score need interval scale?

### 3.1 Strict definition of interval scale

Interval Scale

**Definition**: There is a function \(f: \Theta \to \mathbb{R}\) such that for any \(\theta_1, \theta_2, \theta_3, \theta_4 \in \Theta\):

\[
\theta_1 - \theta_2 = \theta_3 - \theta_4 \Leftrightarrow f(\theta_1) - f(\theta_2) = f(\theta_3) - f(\theta_4)
\]

**Intuitive meaning**: Equal trait differences correspond to equal scale differences, no matter where they are on the scale

**Allowed transformations**: \(Y = aX + b \quad (a > 0)\)

**Change Score Requirements**: Only on the interval scale, we can say:

\[\Delta_1 = \Delta_2 \Leftrightarrow \text{Equal changes in traits}\]

### 3.2 Reasons why CTT is difficult to meet the interval scale requirements

**Reason 1: The non-linear nature of total score**

CTTtotal score is a simple addition of item scores:

\[
X = \sum_{i=1}^n X_i
\]

But the relationship between trait level and item response is usually nonlinear (such as an S-shaped curve).

**Cause 2: Fractional compression effect**

Assume that the relationship between trait \(\theta\) and observation score \(X\) is:

\[
X = g(\theta)
\]

Where \(g\) is a nonlinear function.

The change score is:

\[
\Delta X = g(\theta_2) - g(\theta_1)
\]

\(\Delta X\) is proportional to \(\Delta \theta\) only when \(g\) is a linear function.

**Example: Logistic Function**

\[
X = \frac{100}{1 + e^{-(\theta - \mu)}}
\]

Derivative analysis:

\[
\frac{dX}{d\theta} = \frac{100e^{-(\theta - \mu)}}{(1 + e^{-(\theta - \mu)})^2}
\]

The derivative is maximum at \(\theta = \mu\), meaning that the same \(\Delta \theta\) produces the maximum \(\Delta X\) in the middle part.

## 4. Revolutionary improvements in change scoring in IRT

### 4.1 Fundamental advantages of IRT

**Advantage 1: True interval scale**

In the Rasch model, the log odds are a linear function of \(\theta\):

\[
\ln\left(\frac{P(\theta)}{1-P(\theta)}\right) = \theta - b
\]

This guarantees:

\[
\Delta \theta_1 = \Delta \theta_2 \Leftrightarrow \text{The log odds change equally for all items}
\]

**Advantage 2: individualized measurement accuracy**

IRT provides different standard errors for each ability level:

\[
\text{SE}(\hat{\theta}) = \frac{1}{\sqrt{I(\theta)}}
\]

where \(I(\theta)\) is the information function of this ability level.

**Advantage 3: Sample-independent parameters**

IRT parameters are not dependent on a specific sample, and the meaning of change scores remains consistent across groups.

### 4.2 Multidimensional Rasch Model of Learning and Change (MRMLC)

MRMLC model

**Core idea**: Decompose individual abilities into two independent components

**Stable ability**: Basic ability that is not affected by short-term intervention

**Modability**: Ability components that can be changed through learning or training

**Basic Model**:

\[\theta_{\text{post}} = \theta_{\text{pre}} + \alpha \cdot \text{Modifiability}\]

where \(\alpha\) is the intervention intensity parameter

**Pre-test model**:

\[
P_{i,\text{pre}}(\theta_{\text{pre}}) = \frac{\exp(\theta_{\text{pre}} - b_i)}{1 + \exp(\theta_{\text{pre}} - b_i)}
\]

**Post-test model**:

\[
P_{i,\text{post}}(\theta_{\text{post}}) = \frac{\exp(\theta_{\text{post}} - b_i)}{1 + \exp(\theta_{\text{post}} - b_i)}
\]

**Ability relationship**:

\[
\theta_{\text{post}} = \theta_{\text{pre}} + \Delta_{\text{learned}}
\]

**Modability Modeling**:

\[
\Delta_{\text{learned}} = \lambda \cdot M
\]

Among them, \(M\) is the individual modifiable parameter, and \(\lambda\) is the intervention effect parameter.

### 4.3 Example analysis of cognitive aging research

Embretson (1998b) studied performance differences between young and older adults on spatial ability training.

**Traditional Analysis**:

\[
\text{raw gain} = X_{\text{post}} - X_{\text{pre}}
\]

**MRMLC Analysis**:

Simultaneously estimate the stability ability and modifiability to obtain a pure learning ability index.

**Why is the relationship non-linear? **

**Reason 1: Baseline Difference Adjustment**

MRMLC adjusts the impact of initial competency levels:

\[
\text{raw gain} = f(\text{modifiability}, \theta_{\text{pre}})
\]

**Reason 2: Non-linearity of the learning curve**

The actual learning process often follows the law of logarithm or power function:

\[
\Delta_{\text{learned}} = \lambda \cdot M^{\gamma}
\]

Among them, \(\gamma < 1\) reflects the diminishing marginal effect.

## 5. Practical Guide to Change Score Analysis

Change score analysis process based on IRT

**Preliminary design**

- Make sure the pre- and post-tests use the same or equating tests
- Design a sufficient number of items to obtain a stable estimate
- Consider practice effects and memory effects

**Model Selection**

- Simple case: estimate \(\theta\) value using basic IRT model
- Complex situations: consider MRMLC or other change models
- Validate model assumptions and fit

**Parameter estimation**

- Jointly estimate pre- and post-test parameters (ensure parameter equating)
- Check the stability of parameter estimates
- Calculate the standard error of the change score

**result explanation**

- Report changes in ability scale (rather than raw score numbers)
- Provide varying confidence intervals
- Explain what the changes actually mean

**Common pitfalls and how to avoid them**:

**Trap 1: Ignoring measurement error**

- Problem: Treat the change score as the true value without error
- Solution: Report changed standard error and confidence interval

**Trap 2: Regression Effect**

- Problem: Misattributing regression effects to real changes
- Solution: Use control group or baseline correction method

**Trap 3: scale dependency**

- Question: Compare change scores on different scales
- Solution: Make sure to use IRTscale with interval scale properties
