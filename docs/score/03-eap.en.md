# 3. Expected posterior probability (EAP) score

## 3.1 Basic idea of EAP method

### 3.1.1 From mode to mean

The difference between the three estimates

**ML**: Find the maximum value (mode) of likelihood function

**MAP**: Find the maximum value (mode) of the posterior distribution

**EAP**: Calculate the expectation (mean) of the posterior distribution

\[\hat{\theta}_{EAP} = E[\theta|\mathbf{u}] = \int_{-\infty}^{\infty} \theta \cdot P(\theta|\mathbf{u}) d\theta\]

### 3.1.2 Numerical integration method

Prerequisite: Bayes’ theorem (continuous parameter space)

According to Bayes’ theorem:

\[
P(\theta \mid \mathbf{u}) = \frac{L(\mathbf{u} \mid \theta) \cdot P(\theta)}{\int_{-\infty}^{\infty} L(\mathbf{u} \mid \theta') \cdot P(\theta') \, d\theta'}
\]

- The numerator is the joint density, representing the joint probability given the ability \(\theta\) and the observation \(\mathbf{u}\);
- The denominator is a normalization constant, ensuring that the integral of the posterior distribution \(P(\theta \mid \mathbf{u})\) is 1;
- When calculating MAP or EAP, the proportional form is often used:

\[
P(\theta \mid \mathbf{u}) \propto L(\mathbf{u} \mid \theta) \cdot P(\theta)
\]

Principles and formulas of numerical integration

**EAP (Expected A Posteriori) estimation** is a type of Bayesian estimation. The goal is to solve the expectation of posterior distribution:

\[
\hat{\theta}_{EAP} = \mathbb{E}[\theta \mid \mathbf{u}] = \int_{-\infty}^{\infty} \theta \cdot P(\theta \mid \mathbf{u}) \, d\theta
\]

1. Starting from Bayes’ formula

According to Bayes’ theorem:

\[
P(\theta \mid \mathbf{u}) = \frac{L(\mathbf{u} \mid \theta) \cdot P(\theta)}{\int L(\mathbf{u} \mid \theta') \cdot P(\theta') \, d\theta'}
\]

2. Substitute into the EAP estimation formula:

\[
\hat{\theta}_{EAP} = \frac{ \int \theta \cdot L(\mathbf{u} \mid \theta) \cdot P(\theta) \, d\theta }{ \int L(\mathbf{u} \mid \theta) \cdot P(\theta) \, d\theta }
\]

3. Why is numerical integration needed?

Usually \(L(\mathbf{u} \mid \theta)\) is the product of the following form:

\[
L(\mathbf{u} \mid \theta) = \prod_{i=1}^I P_i(\theta)^{u_i} (1 - P_i(\theta))^{1 - u_i}
\]

Among them:

\[
P_i(\theta) = \frac{1}{1 + \exp(-\alpha_i(\theta - \beta_i))}
\]

Because \(L(\mathbf{u} \mid \theta)\) is the product of multiple nonlinear sigmoid functions, its product with the prior \(P(\theta)\) cannot be calculated analytically in most cases:

\[
\int_{-\infty}^{\infty} L(\mathbf{u} \mid \theta) \cdot P(\theta) \, d\theta \quad \text{no closed form}
\]

Therefore, we can only approximate the normalization constant and expectation of the posterior distribution by numerical integration (such as Gauss-Hermite or simple summation approximation).

4. Numerical approximation (discrete integral):

Discretize the interval \([-3, 3]\) into \(R\) points and calculate the approximate value:

\[
\hat{\theta}_{EAP} \approx \frac{\sum_{r=1}^{R} \theta_r \cdot L(\mathbf{u}|\theta_r) \cdot P(\theta_r)}{\sum_{r=1}^{R} L(\mathbf{u}|\theta_r) \cdot P(\theta_r)}
\]

5. Explanation of each item:

- \(\theta_r\): The \(r\)th ability point (such as from \(-3\) to \(3\), step size \(0.1\))
- \(L(\mathbf{u}|\theta_r)\): Likelihood value at this point
- \(P(\theta_r)\): The density of the prior distribution at this point

6. Intuitive explanation:

> "On each \(\theta_r\), use its posterior probability as the weight, and find its weighted average."

7. Practical suggestions:

- Commonly used \(R=61\) (\([-3,3]\))
- Gauss-Hermite quadrature can be used for higher accuracy
- EAP is more stable but slower to calculate than MAP

## 3.2 Implementation of EAP algorithm

Specific steps of EAP numerical integration

We already know before that EAP is estimated to be the expectation of the posterior distribution:

\[
\hat{\theta}_{EAP} = \frac{ \int \theta \cdot L(\mathbf{u} \mid \theta) \cdot P(\theta) \, d\theta }{ \int L(\mathbf{u} \mid \theta) \cdot P(\theta) \, d\theta }
\]

Review its approximation:

\[
\hat{\theta}_{EAP} \approx \frac{\sum_{r=1}^{R} \theta_r \cdot L(\mathbf{u}|\theta_r) \cdot P(\theta_r)}{\sum_{r=1}^{R} L(\mathbf{u}|\theta_r) \cdot P(\theta_r)}
\]

Below we use the **discrete sum approximation** integral, which is divided into five steps:

**Step one: Set the integration point**

- On the interval \(\theta \in [-3, 3]\), select \(R=61\) equidistant points
- For example: \(\theta_r \in \{-3.0, -2.9, ..., 2.9, 3.0\}\)
- The step size is \(0.1\), with a total of \(R=61\) points

**Step 2: Calculate the prior density \(P(\theta_r)\)**

- If using standard normal prior: \(P(\theta_r) = \phi(\theta_r) = \frac{1}{\sqrt{2\pi}} e^{-\theta_r^2/2}\)
- Optional normalized version: \(W_r = \frac{\phi(\theta_r)}{\sum_{s=1}^R \phi(\theta_s)}\) (makes the weights sum to 1)

**Step 3: Calculate likelihood function \(L(\mathbf{u} \mid \theta_r)\)**

- Calculated at each \(\theta_r\):

\[
L(\mathbf{u} \mid \theta_r) = \prod_{i=1}^I P_i(\theta_r)^{u_i} \cdot (1 - P_i(\theta_r))^{1 - u_i}
\]

- Where \(P_i(\theta_r) = \frac{1}{1 + \exp(-\alpha_i(\theta_r - \beta_i))}\) is the 2PL model success probability of the \(i\) item

**Step 4: Calculate non-normalized posterior weights**

\[
W_r^* = L(\mathbf{u} \mid \theta_r) \cdot P(\theta_r)
\]

> Posterior density ∝ Likelihood × prior, so this is the proportional term

**Step 5: Normalize and find weighted average**

- Normalization:

\[
\tilde{W}_r = \frac{W_r^*}{\sum_{s=1}^R W_s^*}
\]

-Finally get the EAP estimate:

\[
\hat{\theta}_{EAP} = \sum_{r=1}^R \theta_r \cdot \tilde{W}_r
\]

**Conclusion understanding:**

> Essentially a "weighted average of all \(\theta_r\)", where the weight is the **posterior probability density** of each point, so it reflects the central trend of the posterior.

## 3.3 Calculation of standard error

Definition and calculation of EAPstandard error

To measure the uncertainty of the EAP estimate, we wish to calculate the standard deviation of the posterior distribution as the estimate error:

1. Basic definition

The definition of posterior standard deviation is the standard deviation of the posterior distribution with respect to its expectation:

\[
SE_{EAP} = \sqrt{ \text{Var}[\theta \mid \mathbf{u}] }
= \sqrt{ \mathbb{E}[(\theta - \hat{\theta}_{EAP})^2 \mid \mathbf{u}] }
\]

This represents the degree of fluctuation of \(\theta\) around its mean (i.e. \(\hat{\theta}_{EAP}\)) under the posterior distribution.

2. Substitute into posterior distribution

Expand the expectation into integral form:

\[
SE_{EAP}
= \sqrt{ \int_{-\infty}^{\infty} (\theta - \hat{\theta}_{EAP})^2 \cdot P(\theta \mid \mathbf{u}) \, d\theta }
\]

Note: This is different from the standard error based on the sampling distribution in the frequentist school. Here, the **posterior distribution** is integrated.

3. Discrete sum approximation

Since the integral cannot be calculated analytically, we approximate it using numerical integration:

\[
SE_{EAP}
\approx \sqrt{ \sum_{r=1}^R (\theta_r - \hat{\theta}_{EAP})^2 \cdot \tilde{W}_r }
\]

Among them:

- \(\theta_r\) is a discretized ability point (such as \([-3, 3]\) interval equidistant division)
- \(\tilde{W}_r\) is the normalized posterior probability:

\[
\tilde{W}_r = \frac{L(\mathbf{u} \mid \theta_r) \cdot P(\theta_r)}{\sum_{s=1}^R L(\mathbf{u} \mid \theta_s) \cdot P(\theta_s)}
\]

That is, at each \(\theta_r\) point, "the posterior probability of occurrence of this ability level"

4. Summary of meaning

- This standard deviation quantifies the **uncertainty** of \(\theta\) under the posterior distribution;
- If \(\tilde{W}_r\) is very concentrated (meaning we are very sure about the location of \(\theta\)), then \(SE_{EAP}\) will be very small;
- If \(\tilde{W}_r\) is widely distributed (indicating that we are very uncertain), then \(SE_{EAP}\) will be large;
- It does not rely on sample size information, nor does it use Fisher information. It is a standard error form unique to Bayesian inference.

> Unlike the standard error of MAP or MLE, the standard error of EAP considers the entire posterior distribution, not just the curvature near a point.

## 3.4 EAP scoring example

Table 7.4 shows the EAP scoring results:

|examinee|reaction mode| MAP |  | EAP |  |
| --- | --- | --- | --- | --- | --- |
|  |  | \(\hat{\theta}\) | \(SE\) | \(\hat{\theta}\) | \(SE\) |
| 1 | \(1111100000\) | \(0.00\) | \(0.47\) | \(0.00\) | \(0.48\) |
| 15 | \(0000000000\) | \(-1.48\) | \(0.53\) | \(-1.52\) | \(0.54\) |
| 23 | \(1111111110\) | \(1.48\) | \(0.53\) | \(1.52\) | \(0.54\) |

EAP vs MAP comparison

**Similarities**:

- Both use prior information
- Estimates are usually very close
-Able to handle extreme reactions

**Difference**:

- EAP is the mean and MAP is the mode
- EAP calculation does not require iteration
- EAP is easier to generalize to complex models

## 3.5 Comprehensive comparison of three methods

Scoring Method Selection Guide

**Use ML when**:

- Longer test (>30 questions)
- No worries about extreme reactions
- Requires unbiased estimates

**Use MAP when**:

- Shorter quizzes
- Need to handle all reactive patterns
- Willing to accept slight bias

**Use EAP when**:

- Requires quick calculations
- Use complex IRT models
- Pay attention to the minimum mean squared error
