# 6. Exploratory multidimensional model

## 6.1 Relationship with factor analysis

Factor analysis of binary items is increasingly similar to the multidimensional IRT model:

- Takane & de Leeuw (1988) showed that they are identical under certain assumptions
- McDonald's (1967) nonlinear factor analysis is the basis for unification
- Both involve weighted combinations of latent traits

**Key differences:**

- Factor analysis: modeling correlations
- Multidimensional IRT: directly modeling item responses (full information method)

**Comparison of advantages:**

Factor analysis:

- Simple concept
- Popularization of software
- Result is easy to interpret

Multidimensional IRT:

- Use all information
- Processing binary data is more reasonable
- Can predict individual responses

## 6.2 Multidimensional Logic Model

### 6.2.1 Multidimensional Rasch model

McKinley and Reckase (1982) model:

\[
P(X_{is} = 1|\theta_s,\delta_i) = \frac{\exp(\sum_m \theta_{sm} + \delta_i)}{1 + \exp(\sum_m \theta_{sm} + \delta_i)} \tag{4.14}
\]

**Key Features:**

- Unidimensional trait levels are replaced by equally weighted trait complexes
- All dimensions are equally weighted

**Problem:** Model not recognized

- Unable to distinguish individual differences in various dimensions
- Different trait levels cannot be estimated separately

**Analogy:**

It's like saying "this student's total ability is 5", but I don't know whether it is "Math 3 + Chinese 2" or "Math 1 + Chinese 4".

### 6.2.2 Multidimensional extension of two-parameter logistic model

Give the discrimination parameter in each dimension for each item:

\[
P(X_{is} = 1|\theta_s,\delta_i,\alpha_i) = \frac{\exp(\sum_m \alpha_{im} \theta_{sm} + \delta_i)}{1 + \exp(\sum_m \alpha_{im} \theta_{sm} + \delta_i)} \tag{4.15}
\]

**Key understanding:**

- Individual potential is reflected by the sum of weighted traits
- The higher the weight (\(\alpha_{im}\)), the more important the trait is
- Different items can rely on different combinations of dimensions

**Explanation of examples:**

Application questions might be:

- 70% relies on computing power (\(\alpha_{i1} = 0.7\))
- 30% depends on reading ability (\(\alpha_{i2} = 0.3\))

### 6.2.3 Model identification

To make the model identifiable, constraints are required:

- Fixed trait means and standard deviations
- or impose other parameter constraints

**Common methods:**

1. Fix the mean of each dimension to 0 and the variance to 1
2. Fixed some "mark" items only having load in one dimension

### 6.2.4 Three-dimensional visualization

![Figure 4.8: Three-dimensional diagram of multi-dimensional logical model](../assets/images/ch4_fig4.8.png)

Figure 4.8 shows the itemresponse probability under the influence of two latent traits.

**Points to observe:**

- Trait level 1 has greater influence (the surface rises faster along that axis)
- This reflects that the item has higher distinction in trait 1
- The two dimensions jointly determine the probability of success

**How to understand three-dimensional diagrams? **

Imagine a hillside:

- X-axis: East-West direction (Capability 1)
- Y-axis: North-South direction (Capability 2)
- Z axis: height (probability of correct answer)
- Slope reflects the importance of each direction

### 6.2.5 Multidimensional extension of three-parameter logistic model

Add guessing parameter:

\[
P(X_{is} = 1|\theta_s,\delta_i,\alpha_i,\gamma_i) = \gamma_i + (1-\gamma_i)\frac{\exp(\sum_m \alpha_{im} \theta_{sm} + \delta_i)}{1 + \exp(\sum_m \alpha_{im} \theta_{sm} + \delta_i)} \tag{4.16}
\]

The probability surface is similar to Figure 4.8, but does not drop to zero.

**Key points to understand:**

Even if the ability in both dimensions is very low, there is still a probability of guessing correctly of \(\gamma_i\).

## 6.3 Normal Ogive multidimensional model

### 6.3.1 Bock et al.’s model

The full information factor analysis model of Bock, Gibbons, and Muraki (1988).

Individual potential:

\[
z_{si} = \sum_m \alpha_{im} \theta_{sm} + \delta_i \tag{4.17}
\]

Probability:

\[
P(X_{is} = 1|\theta_s,\delta_i,\alpha_i) = \int_{-\infty}^{z_{si}} \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{t^2}{2}\right)dt \tag{4.18}
\]

### 6.3.2 Parameter conversion

Factor loadings and standard difficulty can be calculated as:

\[
\lambda_{im} = \frac{\alpha_{im}}{g_i} \quad \text{and} \quad \beta_i = \frac{\delta_i}{g_i} \tag{4.19}
\]

Among them:

\[
g_i = \sqrt{1 + \sum_m \alpha_{im}^2}
\]

**Meaning of these conversions:**

Convert IRT parameters into forms familiar from factor analysis for easier interpretation and comparison.

### 6.3.3 Version with guessing

\[
P(X_{is} = 1|\theta_s,\beta_i,\alpha_i,\gamma_i) = \gamma_i + (1-\gamma_i) \int_{-\infty}^{z_{si}} \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{t^2}{2}\right)dt \tag{4.20}
\]
