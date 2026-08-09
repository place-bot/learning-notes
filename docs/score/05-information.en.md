# 5. item and test information

## 5.1 The concept of information

### 5.1.1 Definition of Fisher information

Definition of information

**Fisher Information** is an indicator in statistics that measures the uncertainty about parameters in an observation sample.

\[
I(\theta) = E\left[\left(\frac{\partial \log L}{\partial \theta}\right)^2\right] = -E\left[\frac{\partial^2 \log L}{\partial \theta^2}\right]
\]

- The first form of explanation: the larger the expected square derivative, it means that small parameter changes lead to larger log-likelihood changes, so the "information amount" contained in the sample is greater.
- The second form of explanation: the expectation of the second derivative of the log likelihood function (the negative sign is because it is usually negative) also represents the "curvature" of the log likelihood - the steeper, the more accurate the estimate.

**Intuitive understanding**:

- The large amount of information means that we can estimate parameters more accurately;
- The amount of information is small, and it is estimated that there will be greater uncertainty;
-The relationship between it and standard error is:

\[
SE(\theta) = \frac{1}{\sqrt{I(\theta)}}
\]

That is, the greater the information, the smaller the standard error.

---

## 5.2 item information function

### 5.2.1 Information formula of dichotomous item

Definition and derivation of item information

**1. Basic definition:**

Assume that the response of the \(i\) item \(u_i\) is a binary random variable (0 or 1) that satisfies the Bernoulli distribution:

\[
u_i \sim \text{Bernoulli}(P_i(\theta))
\]

Then its **log likelihood function** is:

\[
\log L_i(\theta) = u_i \log P_i(\theta) + (1 - u_i) \log [1 - P_i(\theta)]
\]

Take its derivative with respect to \(\theta\):

\[
\frac{\partial \log L_i(\theta)}{\partial \theta} = \frac{u_i P'_i(\theta)}{P_i(\theta)} - \frac{(1 - u_i) P'_i(\theta)}{1 - P_i(\theta)} = \frac{P'_i(\theta)}{P_i(\theta)[1 - P_i(\theta)]} \cdot (u_i - P_i(\theta))
\]

The definition of **Fisher information** is the expectation of the square of the derivative:

\[
I_i(\theta) = E \left[ \left( \frac{\partial \log L_i(\theta)}{\partial \theta} \right)^2 \right]
\]

Bringing in the above derivatives we get:

\[
I_i(\theta) = \left( \frac{P'_i(\theta)}{P_i(\theta)[1 - P_i(\theta)]} \right)^2 \cdot E\left[(u_i - P_i(\theta))^2\right]
\]

Note that the expected term is variance:

\[
E[(u_i - P_i(\theta))^2] = \text{Var}(u_i) = P_i(\theta)[1 - P_i(\theta)]
\]

So in the end we get:

\[
I_i(\theta) = \frac{[P'_i(\theta)]^2}{P_i(\theta)[1 - P_i(\theta)]}
\]

1PL/Rasch model

**Reaction Function**:

\[
P_i(\theta) = \frac{1}{1 + \exp[-(\theta - \beta_i)]}
\]

Assume \(\eta_i = \theta - \beta_i\), then:

\[
P_i(\theta) = \frac{e^{\eta_i}}{1 + e^{\eta_i}}, \quad \Rightarrow \quad P'_i(\theta) = \frac{d}{d\theta} P_i(\theta) = P_i(\theta)[1 - P_i(\theta)]
\]

Bringing in the general formula:

\[
I_i(\theta) = \frac{[P_i(\theta)(1 - P_i(\theta))]^2}{P_i(\theta)[1 - P_i(\theta)]} = P_i(\theta)[1 - P_i(\theta)]
\]

2PL model

**Reaction Function**:

\[
P_i(\theta) = \frac{1}{1 + \exp[-\alpha_i(\theta - \beta_i)]}
\]

Let \(\eta_i = \alpha_i(\theta - \beta_i)\), calculate the derivative:

\[
P'_i(\theta) = \alpha_i \cdot P_i(\theta)[1 - P_i(\theta)]
\]

So substitute the information function:

\[
I_i(\theta) = \frac{[\alpha_i \cdot P_i(\theta)[1 - P_i(\theta)]]^2}{P_i(\theta)[1 - P_i(\theta)]} = \alpha_i^2 \cdot P_i(\theta)[1 - P_i(\theta)]
\]

3PL model

**Reaction Function**:

\[
P_i(\theta) = c_i + (1 - c_i) \cdot \frac{1}{1 + \exp[-\alpha_i(\theta - \beta_i)]}
\]

Assume:

\[
Q_i(\theta) = \frac{1}{1 + \exp[-\alpha_i(\theta - \beta_i)]}
\]

Then:

\[
P_i(\theta) = c_i + (1 - c_i) Q_i(\theta)
\]

Derivative:

\[
P'_i(\theta) = (1 - c_i) \cdot Q'_i(\theta) = (1 - c_i) \cdot \alpha_i \cdot Q_i(\theta)[1 - Q_i(\theta)]
\]

Remember:

\[
Q_i(\theta) = \frac{P_i(\theta) - c_i}{1 - c_i}
\]

Arrangement and substitution:

\[
P'_i(\theta) = \alpha_i \cdot \frac{P_i(\theta) - c_i}{1 - c_i} \left(1 - \frac{P_i(\theta) - c_i}{1 - c_i}\right) = \alpha_i \cdot \frac{(P_i - c_i)(1 - P_i)}{(1 - c_i)^2}
\]

So the information function is:

\[
I_i(\theta) = \frac{[P'_i(\theta)]^2}{P_i(\theta)[1 - P_i(\theta)]} = \alpha_i^2 \cdot \frac{(P_i - c_i)^2 (1 - P_i)}{(1 - c_i)^4 P_i}
\]

The final commonly used finishing version is:

\[
I_i(\theta) = \alpha_i^2 \cdot \frac{[P_i(\theta) - c_i]^2}{(1 - c_i)^2} \cdot \frac{1 - P_i(\theta)}{P_i(\theta)}
\]

### 5.2.2 Characteristics of information function

key rules

**1. Location rules**:

- For 1PL and 2PL models, the information function reaches its maximum value at \(\theta = \beta\).
- For the 3PL model, due to the influence of the guessing parameter, the maximum value is biased to a position slightly higher than \(\beta\).

**2. Highly regular**:

- The larger the discrimination \(\alpha\), the steeper the response curve and the greater the information.
- The larger the guessing parameter \(c\) is, the higher the bottom probability will be and the amount of information will be reduced.

**3. Shape rules**:

- The highly differentiated item information curve is peak-shaped (highly concentrated);
- The low-resolution item information curve is relatively flat, with a wider range of effects but low accuracy.

Derivation of properties of information function

**1. Position law: the position of the maximum value of the information function**

Let’s take the 2PL model as an example. Its information function is:

\[
I_i(\theta) = \alpha_i^2 P_i(\theta)[1 - P_i(\theta)]
\]

Because \(P_i(\theta)\) is an S-shaped function, symmetric about \(\theta = \beta_i\), its value is between \([0, 1]\).

When \(P_i(\theta) = 0.5\), \(1 - P_i(\theta) = 0.5\), the information function at this time is:

\[
I_i(\theta) = \alpha_i^2 \cdot 0.5 \cdot 0.5 = \frac{\alpha_i^2}{4}
\]

Therefore, information is maximized at:

\[
\boxed{\theta = \beta_i}
\]

For the 1PL model (i.e., \(\alpha_i = 1\)), the conclusion is also true.

For the 3PL model, the information function becomes:

\[
I_i(\theta) = \alpha_i^2 \cdot \frac{[P_i(\theta) - c_i]^2}{(1 - c_i)^2} \cdot \frac{1 - P_i(\theta)}{P_i(\theta)}
\]

Since the lower bound of \(P_i(\theta)\) is \(c_i\), the information peak no longer appears at \(\theta = \beta_i\), but is slightly shifted to the right, that is:

\[
\boxed{\theta^\star > \beta_i}
\]

**2. Height regularity: the size of the information peak**

Continuing to take the 2PL model as an example, substitute \(\theta = \beta_i\) to get:

\[
I_i(\beta_i) = \alpha_i^2 \cdot 0.5 \cdot 0.5 = \frac{\alpha_i^2}{4}
\]

It can be seen that the information peak is proportional to the square of the discrimination.

Further explanation follows:

- If the discrimination \(\alpha_i\) is larger, the slope is steeper and the peak value is higher;
- If the guessing parameter \(c_i\) is larger, it will increase the probability of correct answers for people with low abilities, make \(P_i(\theta)\) flatter, and reduce \([P_i(\theta) - c_i]^2\), thus reducing the amount of information.

**3. Shape rules: steepness and flatness of the information curve**

By the formula:

\[
I_i(\theta) = \alpha_i^2 P_i(\theta)[1 - P_i(\theta)]
\]

It can be inferred that the shape of the information function is controlled by the discrimination \(\alpha_i\).

- If \(\alpha_i\) is larger:

  - \(P_i(\theta)\) rises faster;
  - The information function is concentrated near \(\theta = \beta_i\);
  - The curve has a narrow peak.
- If \(\alpha_i\) is smaller:

  - \(P_i(\theta)\) rises more slowly;
  - The information function has a wide distribution range;
  - The curve is flatter (broad curve).

**Summary:**

- Discrimination \(\alpha_i\) determines the "concentration degree" of the information function;
- A higher \(\alpha_i\) means a more accurate measurement but a narrower range;
- A lower \(\alpha_i\) means a wider measurement range but less accuracy.

## 5.3 Test information function

### 5.3.1 Additivity of information

Calculation of test information

**Basic Principle**: If items are independent, the information function is additive.

\[
TI(\theta) = \sum_{i=1}^I I_i(\theta)
\]

**Meaning description**:

- The overall information amount of the test is the sum of the information functions of all items;
- Each question contributes to the accuracy of the ability level;
- This is the basis for test design and adaptive testing.

### 5.3.2 Information and standard error

Practical formula

**Relationship between standard error and total information**:

\[
SE(\theta) = \frac{1}{\sqrt{TI(\theta)}}
\]

**Example description**:

- \(TI(\theta) = 4\)：\(SE = 0.50\)
- \(TI(\theta) = 25\)：\(SE = 0.20\)
- \(TI(\theta) = 100\)：\(SE = 0.10\)

> This means that to improve accuracy (reduce SE), we can design more effective items to increase the amount of information.

---

## 5.4 polytomous item information

### 5.4.1 Promotion of multi-category models

Expand to multiple categories

For items with multiple options (such as GRM, NRM models), the information function is generalized as follows:

\[
I_i(\theta) = \sum_{k=0}^{m_i} \frac{[P'_{ik}(\theta)]^2}{P_{ik}(\theta)}
\]

- \(P_{ik}(\theta)\) represents the probability of selecting category \(k\) when the capability is \(\theta\);
- \(P'_{ik}(\theta)\) is the derivative of this probability with respect to \(\theta\);
- Both spline and logistic models can be substituted into this general formula.

**Understand**: This formula measures "the richer information provided by sharp changes in the probability curve."

- If the selection probability of an option changes drastically with ability, then we can distinguish subjects with high and low abilities accordingly, so the question provides more information at this point.

The multi-category information function is usually largest near the turning point (category boundary) between each category.

> This is especially important for constructing multi-level rating items (such as Likertscale).
