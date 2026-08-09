# 2. Maximum a posteriori probability (MAP) score

## 2.1 Introduction of Bayesian method

### 2.1.1 Review of limitations of ML methods

Practical issues with ML scoring

**Question 1: Extreme Reaction Pattern**

- It’s impossible to predict whether it’s all right or all wrong.
- Frequently seen in actual tests

**Issue 2: Small sample nature**

- Estimates may be unstable in short tests
- Asymptotic properties may not hold true

### 2.1.2 Bayesian solution

The core idea of Bayesian method

**Basic Concept**: Combine prior information and data information

**Bayesian formula**:

\[P(\theta|\mathbf{u}) \propto P(\mathbf{u}|\theta) \times P(\theta)\]

Among them:

- \(P(\mathbf{u}|\theta)\)：likelihood function
- \(P(\theta)\)：prior distribution
- \(P(\theta|\mathbf{u})\)：posterior distribution

## 2.2 Selection of prior distribution

### 2.2.1 Standard normal prior

The most commonly used prior distribution

**standard normal distribution**:

\[P(\theta) = \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{\theta^2}{2}\right)\]

**Reason for selection**:

1. Convenient in calculation
2. Distribution consistent with many psychological traits
3. Consistent with IRT standardization

Figure 7.6 shows the standard normal prior distribution:

![normal distribution function](../assets/images/ch7_fig7.6.png)

### 2.2.2 The role of prior distribution

A priori influence mechanism

**Pull to center effect**:

- Extreme ability estimates are pulled toward the mean
- Effect size depends on data volume

**Shrinkage estimate**:

\[\hat{\theta}_{MAP} = w\hat{\theta}_{ML} + (1-w)\mu_{prior}\]

Among them, \(w\) depends on the amount of information in the data.

Deriving MAP Shrinkage Estimates from a Bayesian Perspective

Scene setting

We wish to estimate a person's ability value \(\theta\). We know two things:

**likelihood function (from data)**:

\[
\hat{\theta}_{ML} \sim \mathcal{N}(\theta, \sigma^2)
\]

Means: Under the real \(\theta\), the maximum likelihood estimation (based on answer data) will fluctuate.

**prior distribution (our prior knowledge of abilities)**:

\[
\theta \sim \mathcal{N}(\mu_{\text{prior}}, \tau^2)
\]

Step 1: Bayesian formula

According to Bayes' rule:

\[
P(\theta \mid \hat{\theta}_{ML}) \propto P(\hat{\theta}_{ML} \mid \theta) \cdot P(\theta)
\]

- **Likelihood Term**:

\[
P(\hat{\theta}_{ML} \mid \theta) \propto \exp\left(-\frac{1}{2\sigma^2}(\hat{\theta}_{ML} - \theta)^2\right)
\]

- **prior items**:

\[
P(\theta) \propto \exp\left(-\frac{1}{2\tau^2}(\theta - \mu_{\text{prior}})^2\right)
\]

Step 2: Construct logarithmic posterior function

\[
\log P(\theta \mid \hat{\theta}_{ML}) = -\frac{1}{2\sigma^2}(\hat{\theta}_{ML} - \theta)^2 - \frac{1}{2\tau^2}(\theta - \mu_{\text{prior}})^2 + \text{constant}
\]

Step 3: Find the derivative and set it to 0

\[
\frac{d}{d\theta} \log P(\theta \mid \hat{\theta}_{ML}) = \frac{1}{\sigma^2}(\hat{\theta}_{ML} - \theta) + \frac{1}{\tau^2}(\mu_{\text{prior}} - \theta)
\]

Let it be 0, and we get:

\[
\left(\frac{1}{\sigma^2} + \frac{1}{\tau^2}\right)\theta = \frac{\hat{\theta}_{ML}}{\sigma^2} + \frac{\mu_{\text{prior}}}{\tau^2}
\]

Step 4: Solve for MAP estimates

\[
\hat{\theta}_{MAP} = \frac{\frac{\hat{\theta}_{ML}}{\sigma^2} + \frac{\mu_{\text{prior}}}{\tau^2}}{\frac{1}{\sigma^2} + \frac{1}{\tau^2}}
\]

Organized into weighted average form:

\[
\hat{\theta}_{MAP} = w \cdot \hat{\theta}_{ML} + (1 - w) \cdot \mu_{\text{prior}}
\]

Among them:

\[
w = \frac{1/\sigma^2}{1/\sigma^2 + 1/\tau^2} = \frac{\tau^2}{\sigma^2 + \tau^2}
\]

Explanation: Why is this called "shrinkage estimation"?

- When the data is very reliable (\(\sigma^2\) is small), \(w \to 1\) mainly relies on \(\hat{\theta}_{ML}\)
- When the prior is strong (\(\tau^2\) is small), \(w \to 0\) mainly relies on \(\mu_{\text{prior}}\)
- Therefore, MAP will "pull back" the extreme \(\hat{\theta}_{ML}\) to \(\mu_{\text{prior}}\)

Summary formula

\[
\boxed{
\hat{\theta}_{MAP} = \frac{\tau^2}{\sigma^2 + \tau^2} \cdot \hat{\theta}_{ML} + \frac{\sigma^2}{\sigma^2 + \tau^2} \cdot \mu_{\text{prior}}
}
\]

This is the essential structure of the MAP estimate:
**Weighted average** between the MLE and the prior, where the weight is determined by the "information content" of the two.

## 2.3 Derivation of MAP estimate

### 2.3.1 Construction of posterior distribution

The form of posterior distribution

**Bayes Principle Review**:

\[
P(\theta \mid \mathbf{u}) \propto P(\mathbf{u} \mid \theta) \times P(\theta)
\]

After taking the logarithm, you can get the logarithmic posterior distribution:

\[
\log P(\theta \mid \mathbf{u}) = \log L(\mathbf{u} \mid \theta) + \log P(\theta) + \text{constant}
\]

**Expand the specific form** (taking the 2PL model as an example, assuming the prior is standard normal):

\[
\log P(\theta \mid \mathbf{u}) =
\sum_{i=1}^I \left[
u_i \log P_i(\theta) +
(1 - u_i) \log(1 - P_i(\theta))
\right]
- \frac{\theta^2}{2}
+ \text{constant}
\]

Among them:

- \(P_i(\theta) = \dfrac{1}{1 + \exp(-\alpha_i(\theta - \beta_i))}\) is the probability of answering the question \(i\) correctly
- \(-\dfrac{\theta^2}{2}\) from the logarithmic form of the standard normal prior \(\mathcal{N}(0,1)\)

**Explanation of derivation process:**

1. The likelihood function part comes from the joint probability of the 2PL model:

\[
P(\mathbf{u} \mid \theta) = \prod_{i=1}^I P_i(\theta)^{u_i} \cdot (1 - P_i(\theta))^{1 - u_i}
\]

   Taking the logarithm gives:

\[
\log P(\mathbf{u} \mid \theta) = \sum_{i=1}^I \left[ u_i \log P_i(\theta) + (1 - u_i) \log(1 - P_i(\theta)) \right]
\]

2. The prior is standard normal distribution \(\mathcal{N}(0, 1)\):

\[
P(\theta) = \dfrac{1}{\sqrt{2\pi}} \exp\left(-\dfrac{\theta^2}{2}\right)
\]

   After taking the logarithm, it is:

\[
\log P(\theta) = -\dfrac{\theta^2}{2} + \text{constant}
\]

Add the two to get the final logarithmic posterior expression.

**Explanation:**

- The position of the main peak of the posterior depends on the "balance" between the support of the data (likelihood function) and the penalty term of the prior distribution.
- The posterior distribution rises at high data support, but is also pulled toward the center by the prior (\(\theta = 0\)), which reflects the "compromise" idea of Bayesian estimation.

### 2.3.2 Modified Newton-Raphson algorithm

Iterative formula for MAP estimation

In order to obtain maximum a posteriori estimation \(\hat{\theta}_{MAP}\), we maximize the logarithmic posterior function:

- **Full MAP objective function (log posterior)**:

\[
L_{\text{MAP}}(\theta) =
\sum_{i=1}^I \left[ u_i \log L_i(\theta) + (1 - u_i) \log (1 - L_i(\theta)) \right]
- \frac{1}{2} \theta^2
+ \text{constant}
\]

Among them, \(L_i(\theta) = \frac{1}{1 + \exp(-\alpha_i(\theta - \beta_i))}\) is the predicted probability of answering question \(i\) correctly when the ability is \(\theta\).

- The first item is the log-likelihood item (Log-Likelihood), which measures the response probability corresponding to the current \(\theta\);
- The second term \(-\frac{1}{2}\theta^2\) comes from the normal prior \(\theta \sim \mathcal{N}(0,1)\) and acts as a contraction.

**The corrected first derivative is**:

\[
L'_{\text{MAP}}(\theta) =
\sum_{i=1}^I \alpha_i \left(u_i - L_i(\theta)\right)
- \theta
\]

**The corrected second derivative is**:

\[
L''_{\text{MAP}}(\theta) =
- \sum_{i=1}^I \alpha_i^2 L_i(\theta)(1 - L_i(\theta))
- 1
\]

**Iterative update formula (modified Newton-Raphson)**:

\[
\theta_{\text{new}} = \theta_{\text{old}} - \frac{L'_{\text{MAP}}(\theta_{\text{old}})}{L''_{\text{MAP}}(\theta_{\text{old}})}
\]

**Key points to understand**:

- When the data provides more information (the information function is large), the likelihood term dominates, and the MAP estimate is close to the MLE;
- When the data is sparse or the answers are extreme (such as all right/all wrong), the influence of the prior term on the objective function is enhanced, and \(\hat{\theta}_{MAP}\) shrinks towards 0;
- This shrinkage is a natural regularization effect of Bayesian estimation, which helps improve the stability of small samples.

Derivation of properties of MAP estimation: shrinkage and dominant mechanisms

**Objective function review**:

\[
L_{\text{MAP}}(\theta) =
\underbrace{\sum_{i=1}^I \left[ u_i \log L_i(\theta) + (1 - u_i) \log (1 - L_i(\theta)) \right]}_{\text{Likelihood term}}
\ - \ \underbrace{\frac{1}{2} \theta^2}_{\text{a priori penalty}}
+ \text{constant}
\]

**1. When the amount of sample information is large: MLE \(\approx\) MAP**

- For each question, the amount of information is defined as:

\[
I_i(\theta) = \alpha_i^2 L_i(\theta)(1 - L_i(\theta))
\]

- Total Fisher information:

\[
I(\theta) = \sum_{i=1}^I I_i(\theta)
\]

- When \(I(\theta)\) is very large (there are many questions, large discrimination, and answers are concentrated in the middle area), the likelihood function is very sharp:
- Its main peak has far greater influence than the prior term
- The posterior peak almost coincides with the log-likelihood peak
- At this time:

\[
\hat{\theta}_{MAP} \approx \hat{\theta}_{MLE}
\]

**2. Derivation of shrinkage estimate (approximate linear form)**

- Assume that MLE \(\hat{\theta}_{MLE}\) obeys approximately normality:

\[
\hat{\theta}_{MLE} \sim \mathcal{N}(\theta, \sigma^2)
\]

- Prior \(\theta \sim \mathcal{N}(0, 1)\)
- The posterior is approximated by Bayes' rule as:

\[
\theta \mid \hat{\theta}_{MLE} \sim \mathcal{N}\left( \frac{1}{1+\sigma^2} \hat{\theta}_{MLE}, \frac{\sigma^2}{1+\sigma^2} \right)
\]

- Get MAP estimate:

\[
\hat{\theta}_{MAP} = \frac{1}{1 + \sigma^2} \hat{\theta}_{MLE}
\]

- What does it mean?
- When \(\sigma^2\) is smaller (more data, MLE is stable), \(\hat{\theta}_{MAP} \to \hat{\theta}_{MLE}\)
- When \(\sigma^2\) is large (data is sparse), \(\hat{\theta}_{MAP} \to 0\)

**3. All right/all wrong extreme case**

- **Suppose \(u_i = 1\) is paired with all \(i\) (all pairs)**, at this time:

\[
L_{\text{MAP}}(\theta) = \sum_{i=1}^I \log L_i(\theta) - \frac{1}{2} \theta^2
\]

- Since \(L_i(\theta) = \frac{1}{1 + e^{-\alpha_i(\theta - \beta_i)}} \to 1\) follows \(\theta \to \infty\), the log-likelihood goes to 0:

\[
\sum \log L_i(\theta) \to 0 \quad \text{And} \quad -\frac{1}{2}\theta^2 \to -\infty
\]

- Therefore, the overall objective function has a **maximum value** and will not increase infinitely (compared to the divergence of MLE)
- In the same way, **all errors \(\theta \to -\infty\) is blocked**
- MAP estimates always exist and converge to finite values

**Conclusion summary:**

- The effect of the prior on MAP is equivalent to adding a regularization term \(-\frac{1}{2}\theta^2\) to the maximization problem
- When the likelihood provides less information (e.g. all true/all false), the prior provides a "soft constraint"
- MAP = “likelihood × shrinkage”, a natural mediator of extreme estimates

## 2.4 Example analysis of MAP scoring

### 2.4.1 Comparison with ML estimation

Table 7.3 shows the MAP score result:

|examinee|reaction mode|ML estimation|  |MAP estimate|  |
| --- | --- | --- | --- | --- | --- |
|  |  | \(\hat{\theta}\) | \(SE\) | \(\hat{\theta}\) | \(SE\) |
| 1 | \(1111100000\) | \(0.00\) | \(0.54\) | \(0.00\) | \(0.47\) |
| 15 | \(0000000000\) | \(-\infty\) | - | \(-1.48\) | \(0.53\) |
| 23 | \(1111111110\) | \(2.20\) | \(0.78\) | \(1.48\) | \(0.53\) |

Key differences between MAP vs ML

**1. Treatment of extreme reactions**:

- ML: Unable to estimate all true/all wrong
- MAP: gives a limited estimate

**2. Shrinkage effect**:

- All estimates shrink towards 0
- Extreme values shrink more

**3. standard error**：

- MAPstandard error is usually smaller
-Reflects the contribution of prior information

### 2.4.2 Visualization of prior effects

Figures 7.7 and 7.8 show the influence of the prior under different degrees of discrimination:

![When item discrimination is all 1.0, examinee’s log likelihood and posterior distribution](../assets/images/ch7_fig7.7.png)

![When the item discrimination is all 2.5, examinee’s log likelihood and posterior distribution](../assets/images/ch7_fig7.8.png)

Laws of a priori influence

**Low discrimination (little information)**:

- Large prior influence
- The posterior is close to the prior

**High Discrimination (More Information)**:

- Data-led
- posterior approximation likelihood

## 2.5 Advantages and disadvantages of MAP method

MAP method summary

**Advantages**:

1. Handle all reaction patterns
2. Small samples have better properties
3. Reduce extreme estimates

**Disadvantages**:

1. Biased estimation (biased towards prior mean)
2. Rely on a priori selection
3. Extreme ability that may conceal the truth

Why is MAP a biased estimate?

**Problem Background**:

MLE is a consistent, asymptotically unbiased estimator, whereas MAP introduces a prior that results in a systematic bias in parameter estimates.

We assume:

- **prior distribution**：\(\theta \sim \mathcal{N}(0, 1)\)
- **Likelihood Approximation**: \(\hat{\theta}_{\text{MLE}} \sim \mathcal{N}(\theta, \sigma^2)\), where \(\sigma^2\) is the variance of \(\hat{\theta}_{\text{MLE}}\) (determined by the information function)
- **Key Assumption**: \(\hat{\theta}_{\text{MLE}}\) is an unbiased estimator of \(\theta\), that is:

\[
\mathbb{E}[\hat{\theta}_{\text{MLE}}] = \theta
\]

This assumption is the basis for deriving MAP bias. If the MLE itself has a large bias (such as in a small sample or extreme response mode), then our following derivation is only an **approximate conclusion**.

**1. Simplifying assumptions (linear approximation analysis)**

- Assume that \(\hat{\theta}_{MLE}\) obeys an approximate normal distribution under certain conditions:

\[
\hat{\theta}_{MLE} \sim \mathcal{N}(\theta, \sigma^2)
\]

- Let the prior be the standard normal distribution:

\[
\theta \sim \mathcal{N}(0, 1)
\]

- The posterior distribution is the product of two normal distributions and is still normal:

\[
\theta \mid \hat{\theta}_{MLE} \sim \mathcal{N} \left( \mu_{\text{post}}, \sigma^2_{\text{post}} \right)
\]

Among them:

-The average is:

\[
\mu_{\text{post}} = \frac{1}{1 + \sigma^2} \hat{\theta}_{MLE}
\]

- variance is:

\[
\sigma^2_{\text{post}} = \frac{\sigma^2}{1 + \sigma^2}
\]

**2. Get MAP estimate**

\[
\hat{\theta}_{MAP} = \mu_{\text{post}} = \frac{1}{1 + \sigma^2} \hat{\theta}_{MLE}
\]

This is a weighted "shrink" of \(\hat{\theta}_{MLE}\).

**3. Source of bias**

Let's calculate the expectation of \(\hat{\theta}_{MAP}\) with respect to the real parameters \(\theta\):

\[
\mathbb{E}_{\hat{\theta}_{MLE} \sim \mathcal{N}(\theta, \sigma^2)}[\hat{\theta}_{MAP}]
= \mathbb{E} \left[ \frac{1}{1 + \sigma^2} \hat{\theta}_{MLE} \right]
= \frac{1}{1 + \sigma^2} \cdot \mathbb{E}[\hat{\theta}_{MLE}]
= \frac{1}{1 + \sigma^2} \cdot \theta
\]

So its bias is:

\[
\text{Bias}(\hat{\theta}_{MAP}) = \mathbb{E}[\hat{\theta}_{MAP}] - \theta
= \left( \frac{1}{1 + \sigma^2} - 1 \right) \theta
= -\frac{\sigma^2}{1 + \sigma^2} \cdot \theta
\]

**4. Summary of bias features**

- MAP shrinks towards **prior mean** (0 in this case)
- The more extreme \(\theta\), the larger the bias
- The bias direction is always "pull back" to the prior center

**Conclusion**

The bias of MAP comes from the "traction" of the prior to the posterior. Its estimate is:

\[
\hat{\theta}_{MAP} = w \cdot \hat{\theta}_{MLE} + (1 - w) \cdot \mu_{\text{prior}}
\]

Since \(w < 1\), \(\hat{\theta}_{MAP}\) are offset to \(\mu_{\text{prior}}\), they are not unbiased estimates.
