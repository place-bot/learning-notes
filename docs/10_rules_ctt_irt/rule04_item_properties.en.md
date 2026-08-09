# Detailed explanation of rule 4: unbiased estimation of item attributes

Rule comparison

| CTT | IRT |
| --- | --- |
|Unbiased estimates of item attributes can only be made with representative samples.|Even if the sample is not representative, unbiased estimates of item attributes can be made|

## 1. item attribute definition

Item Properties

The statistical characteristics of a single item in the test mainly include:

- **Difficulty**: The pass rate or position parameter of the item
- **Discrimination**: The ability of an item to distinguish between different ability levels
- **guessing parameter**: Probability of randomly guessing correctly (only in some models)

## 2. Item attributes under CTT framework

### 2.1 Difficulty indicator

CTItem difficulty

\[
p_i = \frac{\sum_{j=1}^n u_{ij}}{n}
\]

Where \(u_{ij} \in \{0,1\}\) represents the reaction of participant \(j\) on item \(i\)

### 2.2 Discrimination index

point biserial correlation coefficient

\[
r_{pb} = \frac{(\bar{X}_1 - \bar{X}_0)\sqrt{p(1-p)}}{\sigma_X}
\]

Derivation: Let \(u \in \{0,1\}\) be a binary variable and \(X\) be a continuous variable (total score).

covariance:

\[
\operatorname{Cov}(u, X) = \mathbb{E}[uX] - \mathbb{E}[u]\mathbb{E}[X]
\]

Due to:

\[
\mathbb{E}[uX] = P(u=1) \cdot \mathbb{E}[X|u=1] = p\bar{X}_1
\]

\[
\mathbb{E}[X] = p\bar{X}_1 + (1-p)\bar{X}_0
\]

Substitute:

\[
\operatorname{Cov}(u, X) = p\bar{X}_1 - p[p\bar{X}_1 + (1-p)\bar{X}_0] = p(1-p)(\bar{X}_1 - \bar{X}_0)
\]

Standard deviation:

\[
\sigma_u = \sqrt{\operatorname{Var}(u)} = \sqrt{p(1-p)}
\]

Therefore:

\[
r_{pb} = \frac{\operatorname{Cov}(u, X)}{\sigma_u \sigma_X} = \frac{p(1-p)(\bar{X}_1 - \bar{X}_0)}{\sqrt{p(1-p)} \cdot \sigma_X} = \frac{(\bar{X}_1 - \bar{X}_0)\sqrt{p(1-p)}}{\sigma_X}
\]

### 2.3 The nature of sample dependency

Assume that the true response function of item \(i\) is \(P_i(\theta)\), and the sample capability distribution is \(g(\theta)\), then:

\[
p_i = \int_{-\infty}^{\infty} P_i(\theta) g(\theta) d\theta = \mathbb{E}_{\theta \sim g}[P_i(\theta)]
\]

Different samples have different \(g(\theta)\):

- High-capacity samples: \(g_H(\theta) = \mathcal{N}(\mu_H, \sigma^2)\), \(\mu_H > 0\)
- Low-capacity samples: \(g_L(\theta) = \mathcal{N}(\mu_L, \sigma^2)\), \(\mu_L < 0\)

Even for the same item, \(p_{i,H} \neq p_{i,L}\).

## 3. Item attributes under the IRT framework

### 3.1 Rasch model

Rasch model definition

\[
P(u_{ij} = 1 | \theta_j, b_i) = \frac{\exp(\theta_j - b_i)}{1 + \exp(\theta_j - b_i)}
\]

- \(\theta_j\): ability parameter of participant \(j\)
- \(b_i\): difficulty parameter of item \(i\)

### 3.2 sufficient statistics

Theorem

In the Rasch model, the total score \(r_j = \sum_{i=1}^I u_{ij}\) is the sufficient statistic of \(\theta_j\).

**Proof**:

The likelihood function of the reaction vector \(\mathbf{u}_j = (u_{1j}, ..., u_{Ij})\):

\[
L(\mathbf{u}_j | \theta_j, \mathbf{b}) = \prod_{i=1}^I \left(\frac{e^{\theta_j - b_i}}{1 + e^{\theta_j - b_i}}\right)^{u_{ij}} \left(\frac{1}{1 + e^{\theta_j - b_i}}\right)^{1-u_{ij}}
\]

\[
= \prod_{i=1}^I \frac{e^{u_{ij}(\theta_j - b_i)}}{1 + e^{\theta_j - b_i}}
\]

\[
= \frac{\exp\left(\sum_{i=1}^I u_{ij}(\theta_j - b_i)\right)}{\prod_{i=1}^I (1 + e^{\theta_j - b_i})}
\]

\[
= \frac{\exp\left(\theta_j r_j - \sum_{i=1}^I u_{ij} b_i\right)}{\prod_{i=1}^I (1 + e^{\theta_j - b_i})}
\]

It breaks down into:

\[
L(\mathbf{u}_j | \theta_j, \mathbf{b}) = \underbrace{\frac{\exp(\theta_j r_j)}{\prod_{i=1}^I (1 + e^{\theta_j - b_i})}}_{g(r_j, \theta_j)} \cdot \underbrace{\exp\left(-\sum_{i=1}^I u_{ij} b_i\right)}_{h(\mathbf{u}_j, \mathbf{b})}
\]

According to the Neyman-Fisher factorization theorem, \(r_j\) is a sufficient statistic of \(\theta_j\). \(\square\)

## 4. Conditional maximum likelihood estimation

### 4.1 Derivation of conditional probability

Given the total score \(r_j\), the probability of the reaction mode:

\[
P(\mathbf{u}_j | r_j, \mathbf{b}) = \frac{P(\mathbf{u}_j | \theta_j, \mathbf{b})}{P(r_j | \theta_j, \mathbf{b})}
\]

The denominator is the sum of the probabilities of all reaction patterns with a total score of \(r_j\):

\[
P(r_j | \theta_j, \mathbf{b}) = \sum_{\mathbf{u}': \sum u'_i = r_j} P(\mathbf{u}' | \theta_j, \mathbf{b})
\]

\[
= \sum_{\mathbf{u}': \sum u'_i = r_j} \frac{\exp\left(\theta_j r_j - \sum_{i=1}^I u'_i b_i\right)}{\prod_{i=1}^I (1 + e^{\theta_j - b_i})}
\]

\[
= \frac{\exp(\theta_j r_j)}{\prod_{i=1}^I (1 + e^{\theta_j - b_i})} \sum_{\mathbf{u}': \sum u'_i = r_j} \exp\left(-\sum_{i=1}^I u'_i b_i\right)
\]

Substitute the conditional probability:

\[
P(\mathbf{u}_j | r_j, \mathbf{b}) = \frac{\exp\left(-\sum_{i=1}^I u_{ij} b_i\right)}{\sum_{\mathbf{u}': \sum u'_i = r_j} \exp\left(-\sum_{i=1}^I u'_i b_i\right)}
\]

keyresult

The conditional probability does not depend on \(\theta_j\), but only on the item parameters \(\mathbf{b}\)

### 4.2 Conditional likelihood function

To all participants:

\[
L_{CML}(\mathbf{b}) = \prod_{j=1}^J P(\mathbf{u}_j | r_j, \mathbf{b})
\]

Log likelihood:

\[
\ell_{CML}(\mathbf{b}) = \sum_{j=1}^J \left[-\sum_{i=1}^I u_{ij} b_i - \ln\left(\sum_{\mathbf{u}': \sum u'_i = r_j} \exp\left(-\sum_{i=1}^I u'_i b_i\right)\right)\right]
\]

## 5. Comparison of estimation methods

### 5.1 Joint Maximum Likelihood (JMLE)

\[
(\hat{\mathbf{\theta}}, \hat{\mathbf{b}}) = \arg\max_{\mathbf{\theta}, \mathbf{b}} \sum_{j=1}^J \sum_{i=1}^I [u_{ij} \ln P_i(\theta_j) + (1-u_{ij}) \ln(1-P_i(\theta_j))]
\]

Problem: The number of parameters increases with the number of samples, leading to inconsistency.

### 5.2 Marginal Maximum Likelihood (MML)

Assume \(\theta \sim \mathcal{N}(0, 1)\):

\[
L_{MML}(\mathbf{b}) = \prod_{j=1}^J \int_{-\infty}^{\infty} \left[\prod_{i=1}^I P_i(\theta)^{u_{ij}} (1-P_i(\theta))^{1-u_{ij}}\right] \phi(\theta) d\theta
\]

where \(\phi(\theta)\) is the standard normal density function.

### 5.3 Conditional Maximum Likelihood (CML)

See section 4.2.

Comparison of method properties

|Features| JMLE | MML | CML |
| --- | --- | --- | --- |
|Consistency|No|Yes|Yes|
|Distribution assumptions required|No|Yes|No|
|computational complexity|low|high|in|
|Applicable model|AllIRT|AllIRT| Rasch |

## 6. The nature of sample invariance

### 6.1 Sample dependencies in CTT

Suppose the ability distribution of the two samples is \(g_1(\theta)\) and \(g_2(\theta)\):

\[
p_{i,1} = \int P_i(\theta) g_1(\theta) d\theta
\]

\[
p_{i,2} = \int P_i(\theta) g_2(\theta) d\theta
\]

Generally, \(p_{i,1} \neq p_{i,2}\).

### 6.2 Sample invariance in IRT

Under CML estimation:

\[
\hat{b}_i^{(1)} = \arg\max_{b_i} L_{CML}^{(1)}(b_i)
\]

\[
\hat{b}_i^{(2)} = \arg\max_{b_i} L_{CML}^{(2)}(b_i)
\]

Theoretically, \(\hat{b}_i^{(1)} = \hat{b}_i^{(2)}\) (ignoring sampling error).

## 7. Practical significance

Advantages of IRT

**item bank construction**: item parameters remain stable across different samples

\[
b_i^{\text{pilot}} \approx b_i^{\text{operational}}
\]

**Test equating**: Different test forms are directly compared on a common scale

\[
\theta_{\text{Form A}} = \theta_{\text{Form B}}
\]

**Adaptive Test**: Select the optimal item based on stable item parameters

\[
i_{next} = \arg\max_i I_i(\hat{\theta}_{current})
\]
