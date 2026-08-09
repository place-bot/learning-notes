# Classic Measurement Theory (CTT) and Item Response Theory (IRT)

## 0. Foreword: Historical background

### 0.1 Development of Classical Measurement Theory (CTT)

Historical context

- **1907-1913**: Spearman laid the foundation for classical measurement theory
- **1950**: Gulliksen publishes classic textbooks, and the CTT system matures
- **1968**: Lord and Novick proposed Item Response Theory (IRT)
- **Now**: IRT is becoming more mainstream, but CTT is still widely used

### 0.2 Detailed explanation of core terms

#### 0.2.1 What is "equating" (Equating)?

Definition and application of equating

**equating**: The process of making different versions of a test comparable

**Actual example**:

- There are multiple sets of test papers for the college entrance examination, but the final scores must be comparable to each other.
- SAT has new items every year, but the score standards must remain the same.
- Each person’s items in the computer-based TOEFL test are different, but the scores must be fair.

**Traditional equating method**:

1. **Linear equating**: \(Y = aX + b\) (simple linear transformation)
2. **Nonlinear equating**: Use more complex curve relationships

**Why is nonlinear equating needed? **

Because the score distribution of different tests may be different:

- Test A: Most people get average scores, showing normal distribution
- Quiz B: Many people get high or low scores, the distribution is skewed
- Simple linear transformation cannot handle this difference

#### 0.2.2 What is the "Delta method"?

Detailed explanation of Delta method

**Delta method**: item difficulty indicator proposed by Gulliksen (1950)

**Core formula**:

\[\Delta = 13 + 4\Phi^{-1}(p)\]

Among them:

- \(p\) = item pass rate (proportion of people who answered correctly)
- \(\Phi^{-1}\) = inverse function of standard normal distribution
- 13 and 4 are to avoid negative numbers and decimals

**Intuitive understanding**:

- If 50% of people answer correctly, \(p=0.5\), \(\Delta = 13\) (medium difficulty)
- If 90% of people answer correctly, \(p=0.9\) and \(\Delta\) are smaller (simple item)
- If 10% of people answer correctly, \(p=0.1\), \(\Delta\) is larger (difficult item)

#### 0.2.3 What is "interval scale"?

**Four levels of measurement scale**:

1. **Nominal scale**: can only be classified (eg: male/female)
2. **Sequential scale**: Can be sorted but with unequal spacing (such as: satisfactory/average/unsatisfactory)
3. **Interval scale**: equal intervals but no absolute zero (such as temperature)
4. **Ratio scale**: There is an absolute zero point (such as: height, weight)

Characteristics of interval scale

- Differences between values are meaningful
- The difference between 60 points and 70 points = The difference between 70 points and 80 points
- But you can't say that 80 points is "twice as good" as 40 points

**Questions in psychometrics**:
The raw score number usually does not meet the requirements of interval scale and needs to be achieved through statistical transformation.

#### 0.2.4 What is "norm"?

Norm

**Definition**: Performance standards of a reference group

**Example**:

- A student scored 100 points on the IQ test
- The score itself is meaningless
- But if the norm shows: mean score = 100, standard deviation = 15
- Then this student is "average"

**Common norm scores**:

- **Percentile**: what percentage of people exceed
- **Standard score**: \((X-\mu)/\sigma\)
- **T Score**: \(50 + 10 \times \text{standard score}\)

#### 0.2.5 What is "difficulty parallelism"?

Difficulty Parallel Concepts and Issues

**Difficulty parallelism**: The overall difficulty of different test versions is the same

**Traditional Practice**:

- Each version contains the same proportion of easy, medium and difficult items
- Same average difficulty
- Score distribution is similar

**Question**:
This approach assumes that everyone has the same ability distribution, which is often not the case.

#### 0.2.6 What is "question stimulation"?

The influence of question stem stimulation

**Question stimulus**: non-core factors in the item that affect the answer

**Example**:
Math question: "Xiao Ming bought 3 apples..."

- Core: Test computing power
- Stimulus: person’s name (Xiao Ming), object (apple), situation (shopping)

**Comparison of views**:

- **Conventional View**: These stimuli do not affect the measurement
- **Modern Perspective**: Stimuli may affect performance in different groups
  - Urban children are familiar with the situation of "buying apples"
  - Rural children may be more familiar with the situation of "growing apples"

#### 0.2.7 What is "Score Interpretation"?

**Scores explained**: How to understand and use quiz scores

1. **Absolute interpretation**: The fraction itself has a fixed meaning
2. Example: The passing mark for the exam is 60 points
3. **Relative Interpretation**: The performance of scores relative to others
4. Example: Top 10%
5. **Intra-individual interpretation**: Comparison of the same person at different times
6. Example: This time it is 5 points better than last time

## 1. CTT basic theory and formula derivation

### 1.1 Basic assumptions and derivation of CTT

#### 1.1.1 Origin of core formula

Basic assumptions of CTT

**Basic formula**:

\[X = T + E\]

Among them:

- \(X\) = observed score (actually measured score)
- \(T\) = true fraction (theoretical "real" fraction)
- \(E\) = Measurement error (random fluctuation)

**Further assumptions**:

1. \(E(E) = 0\) (error expectation is 0)
2. \(\rho(T,E) = 0\) (the true fraction is not related to the error)
3. \(\rho(E_1,E_2) = 0\) (errors in different measurements are not relevant)

#### 1.1.2 Derivation of reliability formula

**Step 1: Decompose the variance of the observed scores**

\[\text{Var}(X) = \text{Var}(T + E) = \text{Var}(T) + \text{Var}(E) + 2\text{Cov}(T,E)\]

Due to \(\text{Cov}(T,E) = 0\):

\[\sigma_X^2 = \sigma_T^2 + \sigma_E^2\]

**Step 2: Define reliability**

Reliability is the proportion of true fractional variance to total variance:

\[r_{tt} = \frac{\sigma_T^2}{\sigma_X^2} = \frac{\sigma_T^2}{\sigma_T^2 + \sigma_E^2}\]

**Step 3: Derive the standard error formula**

Available from \(\sigma_X^2 = \sigma_T^2 + \sigma_E^2\):

\[\sigma_E^2 = \sigma_X^2 - \sigma_T^2 = \sigma_X^2(1 - \frac{\sigma_T^2}{\sigma_X^2}) = \sigma_X^2(1 - r_{tt})\]

Therefore:

\[SE_{\text{msmt}} = \sigma_E = \sigma_X\sqrt{1 - r_{tt}}\]

CTT standard error formula summary

**standard error formula**:

\[SE_{\text{msmt}} = \sigma \sqrt{1 - r_{tt}}\]

**Derivation logic**:

1. Observed fraction = true fraction + error
2. Total variance = true fraction variance + error variance
3. reliability = true fraction variance / total variance
4. standard error = standard deviation of error

### 1.2 Derivation of Spearman-Brown formula

#### 1.2.1 Question setting

Suppose we have a test with a reliability of \(r_{tt}\). Now we want to know: if the test length is increased to \(n\) times, what will the new reliability be?

#### 1.2.2 Detailed derivation process

**Step 1: Set variables**

- Original test: length is \(k\), reliability is \(r_{tt}\)
- New test: length \(nk\), reliability \(r_{nn}\) (to be requested)

**Step 2: Analyze variance changes**

Variance breakdown of the original test:

\[\sigma_X^2 = \sigma_T^2 + \sigma_E^2\]

When the test length increases by \(n\) times:

- The true fraction variance increases by \(n^2\) times: \(\sigma_{T_n}^2 = n^2\sigma_T^2\)
- The error variance increases by \(n\) times: \(\sigma_{E_n}^2 = n\sigma_E^2\) (assuming the errors are independent)

**Step 3: Calculate the new total variance**

\[\sigma_{X_n}^2 = \sigma_{T_n}^2 + \sigma_{E_n}^2 = n^2\sigma_T^2 + n\sigma_E^2\]

**Step 4: Calculate new reliability**

\[r_{nn} = \frac{\sigma_{T_n}^2}{\sigma_{X_n}^2} = \frac{n^2\sigma_T^2}{n^2\sigma_T^2 + n\sigma_E^2} = \frac{n^2\sigma_T^2}{n(n\sigma_T^2 + \sigma_E^2)}\]

Simplify:

\[r_{nn} = \frac{n\sigma_T^2}{n\sigma_T^2 + \sigma_E^2}\]

**Step 5: Use original reliability expression**

Available from \(r_{tt} = \frac{\sigma_T^2}{\sigma_T^2 + \sigma_E^2}\):

- \(\sigma_T^2 = r_{tt}(\sigma_T^2 + \sigma_E^2)\)
- \(\sigma_E^2 = (1-r_{tt})(\sigma_T^2 + \sigma_E^2)\)

Assume \(\sigma_T^2 + \sigma_E^2 = V\), then:

\[r_{nn} = \frac{n \cdot r_{tt} \cdot V}{n \cdot r_{tt} \cdot V + (1-r_{tt}) \cdot V} = \frac{nr_{tt}}{nr_{tt} + (1-r_{tt})}\]

Spearman-Brown formula

**Final formula**:

\[r_{nn} = \frac{nr_{tt}}{1 + (n-1)r_{tt}}\]

**Special circumstances**:

- \(n=2\) (double the length): \(r_{22} = \frac{2r_{tt}}{1 + r_{tt}}\)
- \(n=0.5\) (halved length): \(r_{0.5} = \frac{0.5r_{tt}}{1 - 0.5r_{tt}}\)

#### 1.2.3 Numerical examples

Assume the original test reliability \(r_{tt} = 0.6\):

**Double the length** (\(n=2\)):

\[r_{22} = \frac{2 \times 0.6}{1 + (2-1) \times 0.6} = \frac{1.2}{1.6} = 0.75\]

**Length increased by 3 times** (\(n=3\)):

\[r_{33} = \frac{3 \times 0.6}{1 + (3-1) \times 0.6} = \frac{1.8}{2.2} = 0.82\]

**Length halved** (\(n=0.5\)):

\[r_{0.5} = \frac{0.5 \times 0.6}{1 + (0.5-1) \times 0.6} = \frac{0.3}{0.7} = 0.43\]

## 2. Basic theory of IRT

### 2.1 The core idea of IRT

A revolutionary perspective on IRT

1. **Individual differences**: People with different ability levels have different measurement accuracy.
2. **item features**: Each question has its own difficulty and distinction.
3. **Model driven**: based on probabilistic models rather than simple statistics
4. **Invariance**: item parameters do not depend on specific samples

### 2.2 The simplest IRT model: Rasch model

#### 2.2.1 Model formula

\[P_i(\theta) = \frac{e^{(\theta - b_i)}}{1 + e^{(\theta - b_i)}}\]

Among them:

- \(P_i(\theta)\) = The probability that a person with ability \(\theta\) correctly answers question \(i\)
- \(\theta\) = Human ability parameter (trait level)
- \(b_i\) = difficulty parameter of question \(i\)
- \(e\) = natural constant

#### 2.2.2 Model features

**When \(\theta = b_i\)**:

\[P_i(\theta) = \frac{e^0}{1 + e^0} = \frac{1}{2} = 0.5\]

This means: when the person's ability is equal to the item difficulty, the probability of getting the answer right is 50%.

**When \(\theta >> b_i\)**:

\[P_i(\theta) \approx 1\]

(Ability is much higher than difficulty, the answer is almost certain to be correct)

**When \(\theta << b_i\)**:

\[P_i(\theta) \approx 0\]

(The ability is far lower than the difficulty level, and the answer is almost certainly wrong)

Updated June 2025
