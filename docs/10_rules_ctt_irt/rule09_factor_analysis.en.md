# Detailed explanation of rule 9: factor analysis of binary items

Rule comparison

| CTT | IRT |
| --- | --- |
|Factor analysis of binary items produces artifacts rather than factors|Factor analysis of original item data produces complete information factor analysis|

## 1. The importance of binary item factor analysis

Binary item and factor analysis

**Why is factor analysis needed? **

Factor analysis is the core method to verify the construct validity of the test, helping us understand:

- Whether the test actually measures the intended construct
-How many potential dimensions are there
- How each item reflects these dimensions

**Universality of binary items**:

- **Aptitude Test**: True/False, Right/Incorrect Answer
- **Diagnosis scale**: yes/no, with/without symptoms
- **Behavior Observation**: Appear/Not Appear
- **Attitude Test**: Agree/Disagree (dichotomized processing)

### 1.1 Special properties of binary items

**Speciality 1: Limited mutation range**

Binary items can only take on 0 or 1, and the range of variation is strictly limited.

**Speciality 2: Non-normal distribution**

Binary items follow Bernoulli distribution:

\[
P(X = x) = p^x(1-p)^{1-x}, \quad x \in \{0,1\}
\]

**Speciality 3: Dependence of variance and mean**

\[
\text{Var}(X) = p(1-p)
\]

The variance is completely determined by the mean, which results in unique statistical properties.

**Speciality 4: Limitation of correlation coefficient**

The correlation coefficient between two binary items is severely limited by the marginal distribution.

## 2. Fundamental issues related to Phi in CTT

### 2.1 Derivation of Phicorrelation coefficient

Phicorrelation coefficient

**joint distribution table**:

Assume two binary variables \(X\) and \(Y\), with values 0 or 1

|  | \(Y=1\) | \(Y=0\) |total|
| --- | --- | --- | --- |
| \(X=1\) | \(p_{11}\) | \(p_{10}\) | \(p_1\) |
| \(X=0\) | \(p_{01}\) | \(p_{00}\) | \(1-p_1\) |
|total| \(p_2\) | \(1-p_2\) | 1 |

**Derivation steps**:

**Step 1: Calculate covariance**

\[
\text{Cov}(X,Y) = E[XY] - E[X]E[Y]
\]

Due to:

\[
E[XY] = 1 \cdot 1 \cdot p_{11} + 1 \cdot 0 \cdot p_{10} + 0 \cdot 1 \cdot p_{01} + 0 \cdot 0 \cdot p_{00} = p_{11}
\]

\[
E[X] = p_1, \quad E[Y] = p_2
\]

Therefore:

\[
\text{Cov}(X,Y) = p_{11} - p_1 p_2
\]

**Step 2: Calculate standard deviation**

\[
\text{Var}(X) = p_1(1-p_1), \quad \sigma_X = \sqrt{p_1(1-p_1)}
\]

\[
\text{Var}(Y) = p_2(1-p_2), \quad \sigma_Y = \sqrt{p_2(1-p_2)}
\]

**Step 3: Phi related formulas**

\[
\phi = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{p_{11} - p_1 p_2}{\sqrt{p_1(1-p_1)p_2(1-p_2)}}
\]

### 2.2 Derivation of Phi related upper bound

**Question**: Find the maximum possible value of \(\phi\)

**Constraints**:

\[
\begin{align}
p_{11} + p_{10} &= p_1 \
p_{11} + p_{01} &= p_2 \
p_{11}, p_{10}, p_{01}, p_{00} &\geq 0 \
p_{11} + p_{10} + p_{01} + p_{00} &= 1
\end{align}
\]

**Maximize \(p_{11}\)**:

By constraints:

\[
p_{11} \leq \min(p_1, p_2)
\]

When \(p_{11} = \min(p_1, p_2)\), \(\phi\) reaches the maximum value.

**Case 1**: \(p_1 \leq p_2\)

\[
p_{11,\max} = p_1
\]

\[
\phi_{\max} = \frac{p_1 - p_1p_2}{\sqrt{p_1(1-p_1)p_2(1-p_2)}} = \frac{p_1(1-p_2)}{\sqrt{p_1(1-p_1)p_2(1-p_2)}}
\]

\[
= \sqrt{\frac{p_1(1-p_2)}{(1-p_1)p_2}}
\]

**General formula**:

\[
\phi_{\max} = \sqrt{\frac{\min(p_1, p_2) \cdot \min(1-p_1, 1-p_2)}{\max(p_1, p_2) \cdot \max(1-p_1, 1-p_2)}}
\]

### 2.3 The generation mechanism of difficulty factors

Assuming there are 4 items, the real factor structure is:

- item1 and 2: Measurement factor A, difficulty is 0.2 and 0.8 respectively
- items3 and 4: Measurement factor B, difficulty is 0.2 and 0.8 respectively

**Ideal correlation matrix** (if there are no difficulty effects):

\[
R_{\text{ideal}} = \begin{pmatrix}
1 & 0.8 & 0 & 0 \
0.8 & 1 & 0 & 0 \
0 & 0 & 1 & 0.8 \
0 & 0 & 0.8 & 1
\end{pmatrix}
\]

**Actual Phi correlation matrix**:

Correlations are compressed due to difficulty constraints. According to the previous formula, when \(p_1 = 0.2, p_2 = 0.8\):

\[
\phi_{\max} = \sqrt{\frac{0.2 \times 0.2}{0.8 \times 0.8}} = 0.25
\]

Therefore, even if the true correlation is 0.8, the observed correlation can only be \(0.8 \times 0.25 = 0.2\) at most.

## 3. Improvement attempts related to four points

### 3.1 Theoretical basis of four-point correlation

Tetrachoric Correlation

**Core Assumption**: Behind each binary item there is an underlying continuous normal variable

**Model**:
Assume latent variables \(Z_1 \sim N(0,1)\) and \(Z_2 \sim N(0,1)\), and the thresholds are \(\tau_1\) and \(\tau_2\):

\[
X = \begin{cases}
1 & \text{if} Z_1 > \tau_1 \
0 & \text{if} Z_1 \leq \tau_1
\end{cases}
\]

\[
Y = \begin{cases}
1 & \text{if} Z_2 > \tau_2 \
0 & \text{if} Z_2 \leq \tau_2
\end{cases}
\]

**Target**: Estimate \(\rho = \text{Cor}(Z_1, Z_2)\)

### 3.2 Calculation of four-point correlation

**Step 1: Infer thresholds from marginal probabilities**

\[
p_1 = P(X=1) = P(Z_1 > \tau_1) = 1 - \Phi(\tau_1)
\]

Therefore:

\[
\tau_1 = \Phi^{-1}(1-p_1) = -\Phi^{-1}(p_1)
\]

Same reason:

\[
\tau_2 = -\Phi^{-1}(p_2)
\]

**Step 2: Leveraging joint probabilities**

\[
p_{11} = P(X=1, Y=1) = P(Z_1 > \tau_1, Z_2 > \tau_2)
\]

This is the integral of a two-variable normal distribution:

\[
p_{11} = \int_{\tau_1}^{\infty} \int_{\tau_2}^{\infty} \frac{1}{2\pi\sqrt{1-\rho^2}} \exp\left(-\frac{z_1^2 - 2\rho z_1 z_2 + z_2^2}{2(1-\rho^2)}\right) dz_2 dz_1
\]

**Step 3: Numerical solution**

Define function:

\[
L(\rho, \tau_1, \tau_2) = \int_{\tau_1}^{\infty} \int_{\tau_2}^{\infty} \phi_2(z_1, z_2; \rho) dz_2 dz_1
\]

Need to solve the equation:

\[
L(\rho, \tau_1, \tau_2) = p_{11}
\]

### 3.3 Analysis of issues related to four points

**Issue 1: Calculation Instability**

When \(p\) is close to 0 or 1, the threshold tends to infinity:

\[
\lim_{p \to 0} \Phi^{-1}(p) = -\infty, \quad \lim_{p \to 1} \Phi^{-1}(p) = +\infty
\]

This leads to extremely unstable numerical integration.

**Problem 2: Non-positive definite matrix problem**

Considering the case of three items, even if the four-point correlation of each pair of items is reasonable, the entire matrix may not be positive definite.

**Example**:

\[
R = \begin{pmatrix}
1 & 0.9 & 0.9 \
0.9 & 1 & -0.8 \
0.9 & -0.8 & 1
\end{pmatrix}
\]

Calculate eigenvalue:

\[
\det(R - \lambda I) = 0
\]

Get: \(\lambda_1 = 2.62\), \(\lambda_2 = 0.38\), \(\lambda_3 = -0.00\)

A negative eigenvalue makes factor analysis impossible.

## 4. Full information factor analysis in IRT

### 4.1 Multidimensional IRT model

Full Information Factor Analysis (FIFA)

**Core idea**: Model the original reaction data directly without calculating the correlation matrix

**Two-dimensional 2-parameter logistic model (M2PL)**:

\[
P_i(\mathbf{\theta}) = \frac{\exp(\mathbf{a}_i' \mathbf{\theta} + d_i)}{1 + \exp(\mathbf{a}_i' \mathbf{\theta} + d_i)}
\]

Among them:
- \(\mathbf{\theta} = (\theta_1, \theta_2, \ldots, \theta_m)'\): individual score vector on \(m\) factors
- \(\mathbf{a}_i = (a_{i1}, a_{i2}, \ldots, a_{im})'\): The loading vector of item \(i\) on each factor
- \(d_i\): The intercept parameter of item \(i\)

### 4.2 Linearized representation

Log odds form:

\[
\text{logit}(P_i(\mathbf{\theta})) = \ln\left(\frac{P_i(\mathbf{\theta})}{1-P_i(\mathbf{\theta})}\right) = \mathbf{a}_i' \mathbf{\theta} + d_i
\]

Expand to:

\[
\text{logit}(P_i(\mathbf{\theta})) = \sum_{k=1}^m a_{ik} \theta_k + d_i
\]

This is a linear function of \(\mathbf{\theta}\), similar to linear factor analysis.

### 4.3 Parameter estimation: marginal maximum likelihood

**Individual Likelihood**:

For the response vector \(\mathbf{u}_j = (u_{1j}, u_{2j}, \ldots, u_{Ij})'\) for individual \(j\):

\[
L_j(\mathbf{\theta}) = \prod_{i=1}^I P_i(\mathbf{\theta})^{u_{ij}} [1-P_i(\mathbf{\theta})]^{1-u_{ij}}
\]

**marginal likelihood**:

\[
L_j = \int L_j(\mathbf{\theta}) g(\mathbf{\theta}) d\mathbf{\theta}
\]

where \(g(\mathbf{\theta})\) is usually assumed to be a multivariate normal distribution:

\[
g(\mathbf{\theta}) = \frac{1}{(2\pi)^{m/2}|\mathbf{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}\mathbf{\theta}'\mathbf{\Sigma}^{-1}\mathbf{\theta}\right)
\]

**Log-likelihood**:

\[
\ln L = \sum_{j=1}^J \ln L_j = \sum_{j=1}^J \ln \left[\int L_j(\mathbf{\theta}) g(\mathbf{\theta}) d\mathbf{\theta}\right]
\]

### 4.4 Detailed derivation of EM algorithm

**E step (expected step)**:

Compute the expectation of the complete data log-likelihood:

\[
Q(\mathbf{\Psi}|\mathbf{\Psi}^{(t)}) = \sum_{j=1}^J \int \ln[L_j(\mathbf{\theta})g(\mathbf{\theta})] h_j(\mathbf{\theta}|\mathbf{\Psi}^{(t)}) d\mathbf{\theta}
\]

Among them, posterior distribution:

\[
h_j(\mathbf{\theta}|\mathbf{\Psi}^{(t)}) = \frac{L_j(\mathbf{\theta}|\mathbf{\Psi}^{(t)}) g(\mathbf{\theta})}{\int L_j(\mathbf{\theta}|\mathbf{\Psi}^{(t)}) g(\mathbf{\theta}) d\mathbf{\theta}}
\]

Calculate the posterior moment:

\[
\mathbf{\mu}_j = E[\mathbf{\theta}_j|\mathbf{u}_j] = \int \mathbf{\theta} h_j(\mathbf{\theta}) d\mathbf{\theta}
\]

\[
\mathbf{\Sigma}_j = E[\mathbf{\theta}_j\mathbf{\theta}_j'|\mathbf{u}_j] = \int \mathbf{\theta}\mathbf{\theta}' h_j(\mathbf{\theta}) d\mathbf{\theta}
\]

**M step (maximization step)**:

For item \(i\), maximize:

\[
Q_i = \sum_{j=1}^J E_{\mathbf{\theta}_j|\mathbf{u}_j}\left[u_{ij} \ln P_i(\mathbf{\theta}_j) + (1-u_{ij}) \ln(1-P_i(\mathbf{\theta}_j))\right]
\]

Using Newton-Raphson:

Gradient:

\[
\frac{\partial Q_i}{\partial a_{ik}} = \sum_{j=1}^J E\left[\theta_{kj}(u_{ij} - P_i(\mathbf{\theta}_j))\right]
\]

Hessian matrix:

\[
\frac{\partial^2 Q_i}{\partial a_{ik} \partial a_{il}} = -\sum_{j=1}^J E\left[\theta_{kj}\theta_{lj}P_i(\mathbf{\theta}_j)(1-P_i(\mathbf{\theta}_j))\right]
\]

### 4.5 Information function and measurement accuracy

**item information function**：

\[
I_i(\mathbf{\theta}) = \frac{[\nabla P_i(\mathbf{\theta})][\nabla P_i(\mathbf{\theta})]'}{P_i(\mathbf{\theta})[1-P_i(\mathbf{\theta})]}
\]

Among them:

\[
\nabla P_i(\mathbf{\theta}) = \frac{\partial P_i(\mathbf{\theta})}{\partial \mathbf{\theta}} = P_i(\mathbf{\theta})[1-P_i(\mathbf{\theta})]\mathbf{a}_i
\]

Therefore:

\[
I_i(\mathbf{\theta}) = P_i(\mathbf{\theta})[1-P_i(\mathbf{\theta})]\mathbf{a}_i\mathbf{a}_i'
\]

**Total Information Matrix**:

\[
\mathbf{I}(\mathbf{\theta}) = \sum_{i=1}^I I_i(\mathbf{\theta}) = \sum_{i=1}^I P_i(\mathbf{\theta})[1-P_i(\mathbf{\theta})]\mathbf{a}_i\mathbf{a}_i'
\]

**standard error matrix**:

\[
\text{SE}(\hat{\mathbf{\theta}}) = \mathbf{I}(\mathbf{\theta})^{-1/2}
\]

## 5. Model selection and application

### 5.1 Determination of the number of factors

**Information Guidelines**:

\[
\text{AIC} = -2\ln L + 2p
\]

\[
\text{BIC} = -2\ln L + p\ln N
\]

Where \(p\) is the number of parameters:

\[
p = I \times (m + 1) + \frac{m(m-1)}{2}
\]

- \(I \times m\): Load parameters
- \(I\): Intercept parameter
- \(\frac{m(m-1)}{2}\): Factor related parameters

### 5.2 Practical application examples

**Interpretation of Loading Matrix**:

\[
\text{Total Distinction} = ||\mathbf{a}_i|| = \sqrt{\sum_{k=1}^m a_{ik}^2}
\]

**Factor contribution ratio**:

\[
\text{Contribute}_{ik} = \frac{a_{ik}^2}{\sum_{l=1}^m a_{il}^2}
\]

**Commonality**:

\[
h_i^2 = \frac{\sum_{k=1}^m a_{ik}^2}{1 + \sum_{k=1}^m a_{ik}^2}
\]

Practical suggestions

**Data preparation**

- Check data quality (missing values, unusual responses)
- Encode binary responses as 0/1
- Check the basic statistics of the item

**model fit**

- Start with a one-factor model
- Gradually increase the number of factors
- Compare fit indices of different models

**result explanation**

- Analyze load patterns
- Calculation factors related
- Evaluate item quality
