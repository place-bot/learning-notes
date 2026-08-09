# item parameters estimation: calibration of IRT model

## 0. Introduction: The core issue of item parameters estimation

### 0.1 Chapter Positioning and Premise

In Chapter 7, we learned how to estimate the examinee's ability level, but that time assumed that the item parameters were known. In reality, when developing a new test, item parameters must first be estimated. This is the central question to be addressed in this chapter.

fundamental challenge

To estimate item difficulty, you need to know the student's ability; to estimate the student's ability, you need to know the item difficulty.

How to start when neither is known?

### 0.2 Data used in this chapter

All methods in this chapter will be demonstrated on the 10-item data of the Abstract Reasoning Test (ART):

- sample size: 818 young adults (787 valid samples, excluding 31 extreme scores)
- Number of items: 10, choose 1 from 8 (the probability of guessing is extremely small)
- model fit: reasonably fit the Rasch model

### 0.3 Prerequisite assumptions for estimation

Two key assumptions

1. **local independence**: After controlling the ability, the responses of each item are independent of each other.
2. **unidimensionality**: The test measures a single latent trait

For ART data, the correlation between items is overall significant (χ²₄₅ = 550.154, p < .000), but the residual correlation is not significant after controlling for single factor (χ²₃₅ = 41.980, p = .194), supporting the local independence hypothesis.

## 1. Heuristic estimation method

### 1.1 Rasch’s basic data matrix method

#### 1.1.1 Method principle

Rasch (1960) showed how to estimate item parameters by hand calculation from the basic data matrix. The key idea is:

- The rows represent items and the columns represent people with equal abilities (grouped by total score)
- total score is a sufficient statistic for estimating ability
- The number of people passing an item is a sufficient statistic for estimating difficulty.

#### 1.1.2 Construct basic data matrix

**Table 8.1 Basic data matrix of ART (n = 787)**

|item|Score 1|Score 2|Score 3|Score 4|score 5|Score 6|Score 7|Score 8|Score 9|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (N) | (18) | (40) | (96) | (101) | (132) | (133) | (111) | (88) | (68) |
| 7 | .39 | .40 | .69 | .81 | .89 | .86 | .94 | .98 | 1.00 |
| 10 | .22 | .57 | .63 | .75 | .85 | .91 | .91 | .97 | .96 |
| 13 | .11 | .18 | .28 | .46 | .62 | .79 | .86 | .90 | .99 |
| 8 | .00 | .13 | .38 | .52 | .61 | .74 | .87 | .93 | .97 |
| 27 | .00 | .15 | .34 | .39 | .52 | .69 | .82 | .85 | .93 |
| 19 | .11 | .18 | .14 | .30 | .34 | .54 | .60 | .80 | .91 |
| 16 | .01 | .15 | .19 | .21 | .32 | .56 | .64 | .67 | .87 |
| 33 | .01 | .01 | .16 | .25 | .39 | .32 | .54 | .61 | .87 |
| 22 | .00 | .01 | .15 | .23 | .27 | .34 | .49 | .73 | .85 |
| 28 | .00 | .10 | .01 | .01 | .19 | .24 | .32 | .57 | .68 |

Each cell in the matrix represents the passing rate of this ability group on this item. Note:

- Within the same row, the passing rate increases as ability increases
- Within the same column, the pass rate decreases with item difficulty

![Item solution probability of three ability groups](assets/images/ch8_fig8.1.png)

#### 1.1.3 Logarithmic ratio conversion

To obtain estimates consistent with the Rasch model, the pass rates need to be converted to log ratios:

\[
\log \text{odds}_{ig} = \log_e\left(\frac{P_{ig}}{1-P_{ig}}\right)
\]

For example, the logarithmic ratio of item7 in score group 5:

\[
\log \text{odds}_{75} = \log_e\left(\frac{0.89}{0.11}\right) = 2.09
\]

**Table 8.2 Log odds data matrix, marginal means and simple Raschiterm difficulty estimates for ART**

|item| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |mean|Rasch difficulty|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | -.45 | -.27 | .78 | 1.48 | 2.09 | 1.83 | 2.77 | 3.89 |Big| 1.86 | -1.91 |
| 10 | -1.27 | .28 | .50 | 1.10 | 1.79 | 2.31 | 2.31 | 3.56 | 3.18 | 1.52 | -1.57 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
|Ability θ| -2.68 | -1.61 | -.98 | -.73 | -.45 | -.19 | .08 | .53 | 1.18 |  |  |

(Note: "Large" in the table means maximum value, and continuity correction is used in actual calculations)

#### 1.1.4 Parameter estimation

1. Calculate the average log ratio of each row (item)
2. Calculate the overall item mean: -0.05
3. item difficulty = -(row mean - overall mean)

For example, item7:

- row mean = 1.86
- bias = 1.86 - (-0.05) = 1.91
- Difficulty = -1.91 (easy items have negative difficulty values)

![Item log odds ratio of three ability groups](assets/images/ch8_fig8.2.png)

#### 1.1.5 Realization of group invariance

Why is it not affected by the sample distribution?

The key is **unweighted averaging**: each ability group is equally weighted, regardless of how many people are in the group.

This ensures that the item parameter estimates remain the same regardless of whether more good students or more poor students are tested.

### 1.2 Logistic regression method with known ability

Assuming that the abilities of the 787 participants are known (actually estimated using MML), logistic regression can be used to estimate the item parameters.

![The four items are solved according to the item solution probability of known trait level](assets/images/ch8_fig8.3.png)

![Box plot of ability distribution of passed and failed items](assets/images/ch8_fig8.4.png)

#### 1.2.1 Model Settings

Logistic regression model:

\[
P(x_i = 1) = \frac{\exp(y)}{1 + \exp(y)}
\]

Among them \(y = b_0 + b_1\theta\)

For 2PL model, reparameterize: \(y = \alpha_i(\theta - \beta_i)\)

Therefore:

- Discrimination: \(\alpha_i = b_1\)
- Difficulty: \(\beta_i = -b_0/b_1\)

![Actual and predicted item probability](assets/images/ch8_fig8.5.png)

#### 1.2.2 Estimated result comparison

**Table 8.4 Heuristic item estimation**

|item library|P value|basic data matrix|Logistic regression|
| --- | --- | --- | --- |
| 7 | .84 | -1.91 | -1.65 |
| 10 | .82 | -1.57 | -1.50 |
| 13 | .65 | -.68 | -.50 |
| 8 | .66 | -.46 | -.45 |
| 27 | .60 | -.09 | -.17 |
| 19 | .47 | .25 | .46 |
| 16 | .45 | .54 | .55 |
| 33 | .40 | 1.01 | .90 |
| 22 | .38 | 1.06 | .91 |
| 28 | .26 | 1.87 | 1.57 |

![Regression of logisticitem estimates on MML 2PL estimates](assets/images/ch8_fig8.6.png)

![Regression of the basic data matrix estimation of the Rasch model on the logistic estimation](assets/images/ch8_fig8.7.png)

Estimates from the two methods are highly consistent (r² = .99).

## 2. Maximum likelihood estimation principle

### 2.1 Construction of likelihood function

#### 2.1.1 Likelihood of a single reaction

For a bipartite reaction (x ∈ {0,1}), the likelihood is:

\[
P(X_{is}) = P_i^{X_{is}} Q_i^{1-X_{is}}
\]

Among them \(Q_i = 1 - P_i\)

#### 2.1.2 Likelihood of complete data

Assuming local independence, the data likelihood is:

\[
L(\mathbf{X}) = \prod_s \prod_i P_{is}^{X_{is}} Q_{is}^{1-X_{is}}
\]

Log likelihood:

\[
\ln L(\mathbf{X}) = \sum_s \sum_i [X_{is} \ln P_{is} + (1-X_{is}) \ln Q_{is}]
\]

### 2.2 Search process

![Data likelihood under various values of item parameters](assets/images/ch8_fig8.8.png)

The likelihood function is in an inverted U shape and has a unique maximum value.

![Estimated equation values under various values of item parameters](assets/images/ch8_fig8.9.png)

The estimating equation (first derivative) is zero at the maximum value.

### 2.3 Newton-Raphson method

Iteration formula:

\[
\beta_{\text{improved}} = \beta_{\text{current}} - \frac{L'(\beta_{\text{current}})}{L''(\beta_{\text{current}})}
\]

Among them:

- \(L'\): First derivative (estimate equation)
- \(L''\): Second derivative (curvature information)

### 2.4 standard error calculation

For the Rasch model:

\[
SE(\beta) = \frac{1}{\sqrt{\sum_s P_{is}(1-P_{is})}}
\]

When \(P_{is} = 0.5\), the standard error is the smallest.

## 3. Three ways to deal with unknown abilities

### 3.1 Joint Maximum Likelihood (JML)

#### 3.1.1 Basic idea

Alternate estimates:

1. Fixed item parameters and estimated capabilities
2. Fixed capabilities, estimate item parameters
3. Repeat until convergence

#### 3.1.2 Estimation equation

For the Rasch model:

\[
\sum_s X_{is} = \sum_s P(X_{is} = 1|\theta_s, \beta_i)
\]

The left side is the observed correct number, and the right side is the expected correct number predicted by the model.

#### 3.1.3 Problems with JML

- Parameter estimates are biased
- Inconsistency (increasing samples does not improve accuracy)
- Cannot handle extreme scores

### 3.2 Marginal Maximum Likelihood (MML)

#### 3.2.1 Core idea

Treat abilities as random variables and eliminate them by integration:

\[
P(\mathbf{X}_r|\mathbf{\beta}) = \int P(\mathbf{X}_r|\theta, \mathbf{\beta}) g(\theta) d\theta
\]

where \(g(\theta)\) is the capability distribution (usually assumed to be standard normal).

#### 3.2.2 Numerical integration

Use the Gaussian quadrature approximation:

\[
P(\mathbf{X}_r|\mathbf{\beta}) \approx \sum_{q=1}^Q P(\mathbf{X}_r|\theta_q, \mathbf{\beta}) w_q
\]

![Five-point Gaussian product](assets/images/ch8_fig8.10.png)

#### 3.2.3 EM algorithm

Step E: Calculate expected frequency

- Expected number of people at ability point \(\theta_q\): \(N'_q\)
- The expected number of people who answered item \(i\) correctly in \(\theta_q\): \(R_{iq}\)

M-step: Maximize expected log-likelihood

\[
\sum_q R_{iq} = \sum_q N'_q P_i(\theta_q, \beta_i)
\]

### 3.3 Conditional Maximum Likelihood (CML)

#### 3.3.1 sufficient statistics

In the Rasch model, the total score \(r\) is the sufficient statistic of ability.

#### 3.3.2 Conditional probability

Given the total score, the probability of the reaction pattern:

\[
P(\mathbf{X}|r, \mathbf{\beta}) = \frac{\prod_i e^{-\beta_i X_i}}{\gamma_r}
\]

Note: ability parameter \(\theta\) has completely disappeared!

#### 3.3.3 Basic symmetry functions

\(\gamma_r\) is a basic symmetry function of order \(r\), representing all possible ways to get \(r\) points.

For example, a 4-question quiz:

- \(\gamma_0 = 1\)
- \(\gamma_1 = e^{-\beta_1} + e^{-\beta_2} + e^{-\beta_3} + e^{-\beta_4}\)
- \(\gamma_2 = e^{-\beta_1-\beta_2} + e^{-\beta_1-\beta_3} + ...\) (6 items)
- \(\gamma_3 = e^{-\beta_1-\beta_2-\beta_3} + ...\) (4 items)
- \(\gamma_4 = e^{-\beta_1-\beta_2-\beta_3-\beta_4}\)

### 3.4 Comparison of three methods

**Table 8.5 Maximum likelihood estimation of 10 items of ART data**

|item library|JML estimate|  |MML estimate|  |CML estimate|  |
| --- | --- | --- | --- | --- | --- | --- |
|  |difficulty| SE |difficulty| SE |difficulty| SE |
| 7 | -1.596 | .102 | -1.591 | .108 | -1.586 | .105 |
| 10 | -1.414 | .097 | -1.442 | .103 | -1.440 | .102 |
| 8 | -.460 | .084 | -.470 | .087 | -.473 | .085 |
| 13 | -.422 | .083 | -.419 | .087 | -.421 | .085 |
| 27 | -.151 | .082 | -.153 | .084 | -.155 | .082 |
| 19 | .452 | .081 | .437 | .083 | .438 | .081 |
| 16 | .531 | .081 | .531 | .083 | .532 | .081 |
| 33 | .752 | .082 | .776 | .084 | .778 | .083 |
| 22 | .863 | .082 | .868 | .085 | .870 | .083 |
| 28 | 1.445 | .088 | 1.462 | .091 | 1.457 | .090 |

The estimates from the three methods are very close.

## 4. Method selection and practical suggestions

### 4.1 Method selection decision

**Practical Decision Making Guide**

|situation|Recommended method|Reason|
| --- | --- | --- |
|Rasch model + large sample (N≥500)| CML |optimal properties|
|Rasch model + small sample (N<500)| MML |more stable|
|2PL/3PL model| MML |only option|
|Need to deal with extreme scores| MML |JML/CML cannot be processed|

### 4.2 sample size requirements

- Rasch model: minimum 200 people
- 2PL model: minimum 500 people
- 3PL model: minimum 1000 people

### 4.3 Software implementation

- **Rasch model**: Winsteps (JML/CML), ConQuest (MML)
- **2PL/3PL model**: BILOG-MG (MML), mirt package (MML)

## 5. Key points of technical appendix

### 5.1 Derivatives of JML

**Table 8.6 First and second derivatives of 1PL, 2PL and 3PL IRT models**

|model|parameters|first derivative|second derivative|
| --- | --- | --- | --- |
| 1PL(Rasch) |Difficulty| \(-\sum_s (X_{is} - P_{is})\) | \(-\sum_s P_{is}(1-P_{is})\) |
| 2PL |Discrimination| \(\sum_s (X_{is} - P_{is})(\theta_s - \beta_i)\) | \(-\sum_s P_{is}(1-P_{is})(\theta_s - \beta_i)^2\) |
| 2PL |Difficulty| \(-\alpha_i \sum_s (X_{is} - P_{is})\) | \(-\alpha_i^2 \sum_s P_{is}(1-P_{is})\) |

### 5.2 Expected frequency of MML

The expected number of people who answer item \(i\) correctly at ability point \(\theta_q\):

\[
R_{iq} = \sum_p n_p x_{ip} P(\theta_q|\mathbf{X}_p, \mathbf{\beta})
\]

where the posterior probability is:

\[
P(\theta_q|\mathbf{X}_p, \mathbf{\beta}) = \frac{w_q L(\mathbf{X}_p|\theta_q, \mathbf{\beta})}{\sum_{q'} w_{q'} L(\mathbf{X}_p|\theta_{q'}, \mathbf{\beta})}
\]

### 5.3 Conditional probability of CML

Given the total score \(r\), the probability of answering item \(i\) correctly:

\[
P(X_i = 1|r, \mathbf{\beta}) = e^{-\beta_i} \frac{\gamma_{r-1}^{(i)}}{\gamma_r}
\]

Among them, \(\gamma_{r-1}^{(i)}\) is the basic symmetry function after removing item \(i\).

## Summary

This chapter introduces methods for estimating IRTitem parameters:

1. **Heuristics** provide intuitive understanding and demonstrate group invariance
2. **Maximum Likelihood Principle** is the basis of modern estimation methods
3. **Three ML methods** each have their own advantages and disadvantages:
   - JML: simple but biased
   - MML: complex but the best quality
   - CML: elegant but only Rasch model

When choosing a method, you need to consider the model type, sample size, and actual needs. MML is the mainstream choice for modern IRT software.

The content of this chapter is based on Chapter 8 of Embretson & Reise (2000)
