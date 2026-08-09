# Rule 3: Interchangeable quiz formats

Rule comparison

| CTT | IRT |
| --- | --- |
|Comparing scores across multiple tests is optimal when test formats are parallel|Comparing scores across multiple tests is optimal when the difficulty levels of different tests vary from person to person|

## 1. Clarification of core concepts

### 1.1 What is the test format?

Test Forms

**Definition**: Different versions of a test that measure the same ability

**Realistic Example**:

- The college entrance examination has different test papers every year, but they all test the same subject ability
- Each SAT test has different items, but the scores must be comparable
- Each person’s TOEFL computer-based test has different items, but the scores must be fair.
- There is an item bank for the driving license test, and each person draws different items.

**Core question**: How to ensure that the scores of different versions can be compared?

### 1.2 What is a parallel test?

Parallel Tests

**Intuitive understanding**: The two tests are "completely equivalent" and can be substituted for each other.

**Strict requirements**:

- Measure the same psychological traits
- Have the same statistical properties
- Equally reliable for everyone

## 2. Strict theory of parallel testing

### 2.1 Gulliksen’s three conditions

Suppose two tests \(X\) and \(Y\) respectively measure the same psychological attribute of the same participant, and their observation scores are:

\[X = T_X + E_X\]

\[Y = T_Y + E_Y\]

Among them, \(T_X, T_Y\) is the true score of the respective test, and \(E_X, E_Y\) is the measurement error.

Three necessary and sufficient conditions for parallel testing

**Condition 1: Equal proper fractions**

\[T_X = T_Y\]

That is, the true scores of each participant in the two tests are exactly the same.

**Condition 2: Equal error variance**

\[\operatorname{Var}(E_X) = \operatorname{Var}(E_Y)\]

The measurement error for both tests has the same degree of variation.

**Condition 3: Independent errors**

\[\operatorname{Cov}(E_X, E_Y) = 0\]

The error terms of the two tests are uncorrelated with each other.

### 2.2 Deriving the properties of parallel tests

**Property 1: Means are equal**

\[\begin{align}
\mu_X &= \mathbb{E}[X] = \mathbb{E}[T_X + E_X] \
&= \mathbb{E}[T_X] + \mathbb{E}[E_X] \
&= \mathbb{E}[T_Y] + 0 \
&= \mathbb{E}[Y] = \mu_Y
\end{align}\]

**Property 2: Variance is equal**

\[\begin{align}
\sigma_X^2 &= \operatorname{Var}(X) = \operatorname{Var}(T_X + E_X) \
&= \operatorname{Var}(T_X) + \operatorname{Var}(E_X) + 2\operatorname{Cov}(T_X, E_X) \
&= \sigma_T^2 + \sigma_E^2 + 0 \
&= \sigma_Y^2
\end{align}\]

Which used:

- \(\operatorname{Cov}(T_X, E_X) = 0\) (CTT basic assumption)
- \(T_X = T_Y\) (Condition 1)
- \(\operatorname{Var}(E_X) = \operatorname{Var}(E_Y)\) (Condition 2)

**Property 3: Relevance equals reliability**

\[\begin{align}
r_{XY} &= \frac{\operatorname{Cov}(X, Y)}{\sigma_X \sigma_Y} \
&= \frac{\operatorname{Cov}(T_X + E_X, T_Y + E_Y)}{\sigma_X^2} \
&= \frac{\operatorname{Cov}(T_X, T_Y) + \operatorname{Cov}(T_X, E_Y) + \operatorname{Cov}(E_X, T_Y) + \operatorname{Cov}(E_X, E_Y)}{\sigma_X^2} \
&= \frac{\sigma_T^2 + 0 + 0 + 0}{\sigma_X^2} \
&= \frac{\sigma_T^2}{\sigma_X^2} = r_{XX} = r_{YY}
\end{align}\]

Summary of statistical characteristics of parallel tests

\[\boxed{\mu_X = \mu_Y, \quad \sigma_X = \sigma_Y, \quad r_{XY} = r_{XX} = r_{YY}}\]

**Meaning**:

- Same average difficulty
- Same degree of fractional dispersion
- Inter-test correlation is equal to their respective reliability

### 2.3 Why are these conditions needed?

**Necessity of equal means**:

- If test A has an average score of 80 and test B has an average score of 60
-Then the same person's scores on the two tests are not comparable

**Necessity of equal variance**:

- If test A scores are scattered and test B scores are concentrated
- Then the difference in the same score has different meanings

**Necessity of equal reliability**:

- If test A is reliable, test B is unreliable
-Then the reliability of the scores is different

## 3. equating issues and methods

### 3.1 What is equating?

equating (equating)

**Definition**: A statistical process that makes scores from different test formats comparable.

**Basic idea**:

Find a transformation function \(f\) such that:

\[Y = f(X)\]

where \(X\) is the score on one test and \(Y\) is the "equivalent" score on another test

**IDEAL GOALS**:

If two people have the same ability, then after equating, their scores should be the same.

### 3.2 Linear equating

**Model**:

\[Y = aX + b\]

**Parameters determined**:

Matching by moments:

\[a = \frac{\sigma_Y}{\sigma_X}\]

\[b = \mu_Y - a\mu_X\]

**Numerical example**:

- Quiz A: \(\mu_A = 70, \sigma_A = 15\)
- Quiz B: \(\mu_B = 80, \sigma_B = 12\)

Calculation:

\[a = \frac{12}{15} = 0.8\]

\[b = 80 - 0.8 \times 70 = 24\]

Therefore: \(Y = 0.8X + 24\)

If someone gets 60 points on test A:

\[Y = 0.8 \times 60 + 24 = 72\]

### 3.3 Nonlinear equating

#### Equating percentiles

Equipercentile Equating (Equipercentile Equating)

**Principle**: Scores with the same percentile are considered equivalent

**Steps**:

1. Calculate the cumulative distribution function of the two tests \(F_X(x)\) and \(F_Y(y)\)
2. Find the equivalent fraction: \(F_X(x) = F_Y(y)\)
3. equating function: \(y = F_Y^{-1}(F_X(x))\)

#### Why is nonlinear equating needed?

When the shape of the score distributions of the two tests is different, linear equating is not accurate enough:

- Test A: normal distribution
- Quiz B: Skewed Distribution

Linear transformation cannot maintain the correspondence of all percentile points at the same time.

### 3.4 Fundamental issues with traditional equating

Limitations of CTTequating

**Border Effect**:

- **Floor Effect**: On a difficult test, a score of 0 may correspond to a wide range of abilities
- **Ceiling Effect**: In an easy test, a perfect score may correspond to a wide range of abilities

**Information Lost**:

- The discrimination in extreme score areas is very low
- equating becomes unreliable in these areas

**Sample dependencies**:

- equating parameters depend on specific samples
- If you change the sample, the equating relationship may change.

## 4. Revolutionary solution for IRT

### 4.1 The elegance of common scale

The core advantages of IRT

**Unified capability scale**:

- All items define difficulty on the same \(\theta\) scale
- All participants have estimated capabilities on the same \(\theta\) scale
- No need for equating conversion, directly comparable

**Clear meaning**:

\[P(\text{Success}) = \frac{e^{(\theta - b)}}{1 + e^{(\theta - b)}}\]

\(\theta - b\) directly determines the probability of success

### 4.2 Adaptive Testing Algorithm

#### Basic process

Computer Adaptive Testing (CAT)

**Step 1: Initialization**

Set initial ability estimate \(\hat{\theta}_0 = 0\)

**Step 2: Select a topic**

Select the item with the largest information at the current estimate:

\[i^* = \arg\max_i I_i(\hat{\theta})\]

**Step 3: Testing and Recording**

Get reaction \(u_i \in \{0, 1\}\)

**Step 4: Update Estimate**

Update capabilities using maximum likelihood estimation

#### Newton-Raphson update algorithm

**Log likelihood function**:

\[\ln L(\theta) = \sum_{i \in \text{Answered}} [u_i \ln P_i(\theta) + (1-u_i) \ln(1-P_i(\theta))]\]

**First derivative** (score function):

\[S(\theta) = \frac{d \ln L}{d\theta} = \sum_{i \in \text{Answered}} [u_i - P_i(\theta)]\]

**Second derivative** (negative value of the information function):

\[\frac{d^2 \ln L}{d\theta^2} = -\sum_{i \in \text{Answered}} P_i(\theta)[1-P_i(\theta)] = -I(\theta)\]

Newton-Raphson iteration formula

\[\hat{\theta}_{n+1} = \hat{\theta}_n - \frac{S(\hat{\theta}_n)}{-I(\hat{\theta}_n)} = \hat{\theta}_n + \frac{\sum_i [u_i - P_i(\hat{\theta}_n)]}{\sum_i P_i(\hat{\theta}_n)[1-P_i(\hat{\theta}_n)]}\]

**Intuitive understanding**:

- Numerator: observed vs. expected bias
- Denominator: current amount of information
- Adjustment range = bias/information

### 4.3 Analysis of adaptive advantages

#### Information efficiency comparison

**Fixed Quiz**:

\[I_{\text{fixed}}(\theta) = \sum_{i=1}^n I_i(\theta)\]

Many of them \(I_i(\theta)\) are close to 0 (item is too difficult or too easy)

**Adaptive Quiz**:

\[I_{\text{adaptive}}(\theta) = \sum_{i=1}^n \max_j I_j(\theta)\]

For each item, choose the current best one

**Theorem**:

\[I_{\text{adaptive}}(\theta) \geq I_{\text{fixed}}(\theta) \quad \forall \theta\]

The equality sign holds true if and only if the fixed tests happen to be the optimal items (almost impossible).

#### Empirical results

It can be seen from Figure 2.5 in Chapter 2:

- Fixed quiz (difficult): \(r^2 = 0.8666\)
- Fixed quiz (easy): \(r^2 = 0.8736\)
- Adaptive quiz: \(r^2 = 0.9695\)

key insights

Adaptive tests not only save items, but more importantly, provide a more accurate ability estimate!

## 5. Practical suggestions

Selection Guide

**Parallel quiz using CTT**:

- Paper-and-pencil testing environment
- Requires pre-printing
- Regulations require "fairness"

**Adaptive quizzes using IRT**:

- Computerized environment
- Personalized assessment needs
- Pursue measurement efficiency
