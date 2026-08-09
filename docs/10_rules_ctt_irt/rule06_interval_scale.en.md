# Detailed explanation of rule 6: establishing scale attribute

Rule comparison

| CTT | IRT |
| --- | --- |
|The interval scale property is implemented by obtaining a normal score distribution|The interval scale property is implemented by applying a justified measurement model|

## 1. Four levels of measurement scale

Stevens (1946) measurement scale classification

**Nominal Scale**

- Only classification, no order relationship
- Example: gender, ethnicity, blood type
- Allowed operations: \(=\), \(\neq\)

**Ordinal Scale**

- Can be sorted, but with unequal spacing
- Example: Satisfaction, pain level
- Allowed operations: \(=\), \(\neq\), \(>\), \(<\)

**Interval Scale**

- equal spacing, but no absolute zero
- Example: Temperature (Celsius), standardized test scores
- Allowed operations: \(+\), \(-\) (the difference is meaningful)

**Ratio Scale**

- There is an absolute zero point and multiples can be compared
- Example: height, weight, response time
- Allowed operations: \(\times\), \(\div\) (the ratio is meaningful)

## 2. Why is interval scale important?

### 2.1 Core properties of interval scale

Isometric properties

For interval scale, it must satisfy:

\[
d(a,b) = d(c,d) \Leftrightarrow |a-b| = |c-d|
\]

where \(d(\cdot,\cdot)\) represents the distance function

**Linear transformation invariance**:

If \(X\) is an interval scale, then \(Y = aX + b\) (\(a > 0\)) is also an interval scale

Proof:

\[
|Y_1 - Y_2| = |(aX_1 + b) - (aX_2 + b)| = a|X_1 - X_2|
\]

The relative distance remains the same:

\[
\frac{|Y_1 - Y_2|}{|Y_3 - Y_4|} = \frac{a|X_1 - X_2|}{a|X_3 - X_4|} = \frac{|X_1 - X_2|}{|X_3 - X_4|}
\]

### 2.2 The necessity of supporting parameter statistics

Only interval scale (and above) can be used reasonably:

- Average: \(\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i\)
- variance: \(\sigma^2 = \frac{1}{n}\sum_{i=1}^n (X_i - \bar{X})^2\)
- correlation coefficient: \(r = \frac{\sum(X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum(X_i - \bar{X})^2\sum(Y_i - \bar{Y})^2}}\)

## 3. CTT’s attempt to implement interval scale

### 3.1 Method 1: item selection strategy

Gulliksen's (1950) strategy

Select the item with pass rate \(p \approx 0.5\)

**Theoretical derivation**:

Let the true fraction \(T \sim N(\mu_T, \sigma_T^2)\)

For the binary scoring item \(i\), define the item characteristic function:

\[
u_i = \begin{cases}
1 & \text{if } T > \tau_i \
0 & \text{if } T \leq \tau_i
\end{cases}
\]

Among them, \(\tau_i\) is the threshold of item \(i\).

Pass rate:

\[
p_i = P(u_i = 1) = P(T > \tau_i) = 1 - \Phi\left(\frac{\tau_i - \mu_T}{\sigma_T}\right)
\]

When \(p_i = 0.5\):

\[
\Phi\left(\frac{\tau_i - \mu_T}{\sigma_T}\right) = 0.5
\]

Therefore \(\tau_i = \mu_T\)

**Application of the Central Limit Theorem**:

total score \(S = \sum_{i=1}^n u_i\)

When all items are \(p_i \approx 0.5\), according to the Lindeberg-Feller central limit theorem:

\[
\frac{S - n \cdot 0.5}{\sqrt{n \cdot 0.5 \cdot 0.5}} \xrightarrow{d} N(0,1)
\]

### 3.2 Method 2: Percentile Match Standardization

nonlinear transformation

**Percentile matching process**:

1. Calculate the cumulative distribution function: \(F_X(x) = P(X \leq x)\)
2. Standardized transformation: \(Z = \Phi^{-1}(F_X(X))\)

**Proof of nonlinear transformation**:

Let the transformation function \(g(x) = \Phi^{-1}(F_X(x))\)

Calculate the derivative:

\[
g'(x) = \frac{d}{dx}\Phi^{-1}(F_X(x)) = \frac{f_X(x)}{\phi(\Phi^{-1}(F_X(x)))}
\]

Where \(f_X(x)\) is the density function of \(X\), and \(\phi\) is the standard normal density.

\(g\) is linear only if \(\frac{f_X(x)}{\phi(\Phi^{-1}(F_X(x)))}\) is a constant.

This requires \(X\) itself to be a normal distribution!

### 3.3 Quantitative analysis of fractional compression

Score Compression

Reduced resolution of test scores within a certain interval

**Information function perspective**:

In CTT, the test information function is approximately:

\[
I(T) \approx \sum_{i=1}^n p_i(T)(1-p_i(T))
\]

For easy quizzes (\(p_i(T)\) is generally higher):

- When \(T\) is high, \(p_i(T) \approx 1\), therefore \(I(T) \approx 0\)
- The amount of information in high segments is extremely low, resulting in score compression

For difficult quizzes (\(p_i(T)\) is generally lower):

- When \(T\) is low, \(p_i(T) \approx 0\), therefore \(I(T) \approx 0\)
- Low segment information content is extremely low, resulting in score compression

## 4. Jones (1971) interval scale theory

### 4.1 Theoretical Framework

Jones's two assumptions

1. The true fraction \(T\) has the interval scale attribute
2. The true score has a normal distribution among the target population: \(T \sim N(\mu_T, \sigma_T^2)\)

**Theorem**: Under the above assumption, if and only if the observation score has a normal distribution, the observation score has the interval scale attribute.

**Proof**:

Let the observation score \(X = T + E\), where \(E\) be the error.

If \(X\) has an interval scale attribute, then there is a transformation \(h\) such that:

\[
h(X) = aT + b
\]

Since \(T \sim N(\mu_T, \sigma_T^2)\), therefore \(h(X) \sim N(a\mu_T + b, a^2\sigma_T^2)\)

To make \(h(X)\) have a normal distribution, \(h\) must be a linear transformation.

Therefore: \(X = \frac{1}{a}h(X) - \frac{b}{a} = T\) (ignoring errors)

This requires \(X\) itself to be in normal distribution. \(\square\)

### 4.2 Limitations of the theory

Three main questions

1. **Population dependency**: The scale attribute is bound to a specific population
2. **Unverifiability**: True fractions are unobservable
3. **Circular Argument**: Use normal distribution to prove interval properties, and use interval properties to support normalization

## 5. IRT solution

### 5.1 Measurement theoretical basis of Rasch model

Basic measurement principles

**Invariant Comparison Principle (Invariant Comparison)**:

- Individual comparison does not depend on item
- item comparison does not depend on the individual

**expression**:

For two individuals \(\theta_1\) and \(\theta_2\), on any item \(i\):

\[
\frac{P_i(\theta_1)/[1-P_i(\theta_1)]}{P_i(\theta_2)/[1-P_i(\theta_2)]} = \frac{e^{\theta_1 - b_i}}{e^{\theta_2 - b_i}} = e^{\theta_1 - \theta_2}
\]

This ratio only depends on \(\theta_1 - \theta_2\) and has nothing to do with item parameters \(b_i\).

For two items \(i\) and \(j\), on any individual \(\theta\):

\[
\frac{P_i(\theta)/[1-P_i(\theta)]}{P_j(\theta)/[1-P_j(\theta)]} = \frac{e^{\theta - b_i}}{e^{\theta - b_j}} = e^{b_j - b_i}
\]

This ratio depends only on \(b_j - b_i\) and has nothing to do with the individual parameter \(\theta\).

### 5.2 Linear structure of log odds

Logit transformation

\[
\text{logit}(P) = \ln\left(\frac{P}{1-P}\right)
\]

In the Rasch model:

\[
\text{logit}(P_i(\theta)) = \theta - b_i
\]

**Proof of linearity**:

Assume two competency levels \(\theta_1\) and \(\theta_2\), and two items \(i\) and \(j\)

Difference:

\[
\text{logit}(P_i(\theta_1)) - \text{logit}(P_j(\theta_2)) = (\theta_1 - b_i) - (\theta_2 - b_j) = (\theta_1 - \theta_2) - (b_i - b_j)
\]

This is the linear combination of the \(\theta\) difference and \(b\) difference, which meets the interval scale requirements.

### 5.3 sufficient statistic and interval properties

The role of sufficient statistic

In the Rasch model, the original total score \(r = \sum u_i\) is the sufficient statistic of the ability \(\theta\)

**Monotonic Transformation**:

\[
\hat{\theta} = \ln\left(\frac{r}{n-r}\right) + C
\]

where \(C\) is the normalization constant.

This transformation preserves order and imparts interval properties.

## 6. Practical significance

Application suggestions

**CTT Scenario**:

- small sample study
- Rapidly developed quizzes
- Tests with normal norms already available

**IRT Situation**:

- Large-scale standardized testing
- Need to compare across groups
- Computer Adaptive Testing

**Verification method**:

- Check the linearity of the equating function
- Verify measurement invariance of different groups
- Analyze item-individual interactions
