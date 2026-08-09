# 3. Measuring scale characteristics: the rules behind the numbers

## 3.1 Why should we care about the "quality" of numbers?

When we get test scores, we often perform various operations: calculating average scores, standard deviations, correlation coefficients, etc. But do we have the right to do these maths on these numbers?

The problem of rationality in number operations

**Assume there are three student scores:**

- Xiao Ming: 60 points
- Xiaohong: 80 points
- Xiao Li: 100 points

**We can say:**

- Xiao Hong is 20 points higher than Xiao Ming? ✓
- Xiao Li is 1.67 times stronger than Xiao Ming? ❓
-The average score is 80 points? ❓
- Xiao Hong’s score is right between Xiao Ming and Xiao Li? ❓

The answer depends on what measurement scale properties these fractions have.

## 3.2 The Nature of Measurement: Representation Theory

Before we go any further, we need to understand the underlying concept of measurement.

The core idea of representation theory

**Purpose of measurement:** Use numbers to represent the relationships between objects in the real world

**Basic requirements:** The relationship between numbers must reflect the true relationship between objects

**Example:** If object A is heavier than object B, then the weight value of A must be greater than B

## 3.3 Four scale levels: from simple to complex

Stevens (1946) proposed four levels of measurement, each with different characteristics.

### 3.3.1 Nominal scale: the world of labels

**Basic features:** Numbers are just labels and have no relationship with size.

Example of nominal scale

**Personality disorder type coding:**

- Paranoid = 1
- Schizoid = 2
- Borderline = 3

**Key understanding:**

- 3 is not "more" than 1
- Can be recoded at will: 1→99, 2→33, 3→17
- Just keep the categories separate

**Table 4.1: Nominal Measures of Personality Disorders**

|Type|Score 1|Score 2|Score 3|
| --- | --- | --- | --- |
|Paranoid| 1 | 11 | 1 |
|Schizoid| 2 | 3 | 1 |
|schizoid type| 3 | 4 | 1 |
|Performative| 4 | 9 | 2 |
|Narcissistic| 5 | 10 | 2 |
|Antisocial| 6 | 2 | 3 |
|borderline| 7 | 5 | 3 |
|Avoidant| 8 | 6 | 3 |
|Dependent| 9 | 7 | 4 |
|obsessive| 10 | 8 | 4 |
|passive-aggressive| 11 | 1 | 4 |

> Note: The transformation from score 1 to score 2 maintains the uniqueness of the category; the transformation from score 3 results in information loss

**Allowed statistics:** Frequency, mode, chi-square test

**Not allowed operations:** Addition, average, size comparison

### 3.3.2 Ordinal scale: the world of ranking

**Basic Features:** Numbers indicate order, but spacing has no meaning

Ordinal scale transformation example

**Different Transformations of Energy Arousal Score:**

|people|raw score number|linear transformation|nonlinear transformation|
| --- | --- | --- | --- |
| 1 | 2 | 51 | 4 |
| 2 | 4 | 52 | 16 |
| 3 | 6 | 53 | 36 |
| 4 | 8 | 54 | 64 |
| 5 | 10 | 55 | 100 |

**Key Insights:**

-Linear transformation keeps relative distance unchanged
- Nonlinear transformation changes relative distances
- Both transformations maintain ordering relationships
- For ordinal data, both transformations are legal!

**Allowed statistics:** Median, percentile, rank-related

**Operations not allowed:** Mean, standard deviation of addition operation

### 3.3.3 Interval scale: the world of distance

**Basic Characteristics:** Equal numerical differences represent equal actual differences

Core features of interval scale

**Additivity:** Satisfies additional properties so that the difference has a fixed meaning

**Allowed transformations:** Only linear transformations (\(aX + b\))

**Meaning:** Spacing makes sense but ratio does not

Let us verify the properties of linear transformations through detailed derivation:

Verified derivation of linear transformation

**Raw data:**
\(X_1 = 6.22\) (mean), \(\sigma_X = 3.07\) (standard deviation)

**Linear Transformation:**
\(Y = 0.5X + 50\)

**Transformed mean and standard deviation:**
\(Y_1 = 53.11\) (mean), \(\sigma_Y = 1.53\) (standard deviation)

**Verify whether the inverse transformation is established:**

\[
\text{Original mean} = (Y_1 - 50) \times 2 = (53.11 - 50) \times 2 = 6.22 \quad \checkmark
\]

**Nonlinear Transformation:**
\(Z = X^2\)

**After transformation:**
\(Z_1 = 47.11\) (mean)

**Try inverse transformation:**

\[
\sqrt{Z_1} = \sqrt{47.11} \approx 6.86 \neq 6.22 \quad \times
\]

→ Under nonlinear transformation, the **mean value is not reversible**.

This example illustrates that linear transformations maintain statistical relationships, while linear transformations destroy this relationship.

**Allowed statistics:** Mean, standard deviation, correlation coefficient, t-test

**Not allowed operations:** Ratio comparisons (e.g. "A is twice as big as B")

### 3.3.4 Ratio scale: The world of proportion

**Basic Features:** There is a true zero point and the ratio is meaningful

Characteristics of ratio scale

**True Zero:** A value of zero indicates the complete absence of an attribute

**Allowed transformations:** Only multiplication by constant (\(aX\))

**Meaning:** It can be said that "A is twice as big as B"

**Allowed statistics:** All statistics, including coefficient of variation

**Reality in psychometrics:** True ratio scales are rare because psychological properties rarely have an absolute zero point

## 3.4 How to prove scale level? joint measurement theory

Now we face a key question: How do we know what scale our test scores have?

### 3.4.1 Advantages of physical measurement

In the physical world, we can directly operate:

Direct verification of length measurements

**Sequence:** Directly observe which stick is longer

**Additivity:** Connect two 1-meter rods to get a 2-meter rod

**Verification:** 1 + 1 = 2, the physical operation is consistent with the operation

### 3.4.2 Challenges of psychometrics

Psychological properties cannot be manipulated directly and we need other methods.

**Joint Measurement Theory** provides a solution: when three variables satisfy a specific relationship, the scale property can be proven.

Core conditions for joint measurement

**Basic requirements:**

1. All variables can be sorted
2. The result variable is the additive function of the other two variables.
3. Meet the double elimination conditions

### 3.4.3 Parallelism between Rasch model and physics

Rasch cleverly designed his model to resemble the additive relationship in physics:

**Mechanical relations in physics:**

\[\text{Acceleration} = \frac{\text{Force}}{\text{Mass}}\]

Taking the logarithm gives us the additive relationship:

\[\log(\text{Acceleration}) = \log(\text{Force}) - \log(\text{Mass})\]

**Additive relationship for Rasch model:**

\[\log(\text{Success Odds}) = \text{Ability Level} - \text{item difficulty}\]

That is:

\[\ln\left(\frac{P_{is}}{1-P_{is}}\right) = \theta_s - \beta_i\]

### 3.4.4 Double elimination condition: test of actual data

Double elimination conditions provide a practical way to test additive relationships.

The meaning of double elimination condition

In the table of ability × item, the probability of success should change monotonically when moving along any diagonal.

**Table 4.2: Rasch model theoretical prediction (double elimination holds)**

|item difficulty|ability level|  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | -1.00 | 0.00 | 1.00 | 1.25 | 1.50 |
| -1.00 | 0.50↗ | 0.73↗ | 0.88↗ | 0.91↗ | 0.92 |
| 0.00 | 0.27↗ | 0.50↗ | 0.73↗ | 0.78↗ | 0.82 |
| 0.25 | 0.22↗ | 0.44↗ | 0.68↗ | 0.73↗ | 0.78 |
| 1.00 | 0.12↗ | 0.27↗ | 0.50↗ | 0.56↗ | 0.62 |

> Note: Diagonal arrows (↗) show double elimination mode; probability increases monotonically along the diagonal direction

**Table 4.3: Actual data (basically meets double elimination)**

|item group|raw score array|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13-16 |
| 1-2 | 0.92↗ | 0.98↗ | 0.98↗ | 0.99↗ | 0.98↗ | 0.99↗ | 0.99↗ | 1.00↗ | 1.00↗ | 1.00↗ | 1.00 |
| 3-4 | 0.48↗ | 0.84↗ | 0.84↗ | 0.86↗ | 0.86↗ | 0.90↗ | 0.95↗ | 0.96↗ | 0.98↗ | 0.99↗ | 1.00 |
| 5-6 | 0.06↗ | 0.18↗ | 0.40↗ | 0.70↗ | 0.70↗ | 0.79↗ | 0.84↗ | 0.88↗ | 0.94↗ | 0.95↗ | 0.98 |

> Note: The table shows the success probabilities of people with different raw score levels on different item sets; the diagonal arrows show the double elimination mode, which is basically satisfied except for a few exceptions.

Although not perfect, it generally conforms to the double elimination mode and supports the interval scale feature.

![Figure 4.1: Graphical representation of double elimination](../assets/images/ch6_fig6.7.png)

Figure 4.1 is an item characteristic curve diagram covered with diagonal arrows. Double elimination is equivalent to saying that ICC does not cross.

**Table 4.4: 2PL model predictions (violation of double elimination)**

|item difficulty|Discrimination|ability level|  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | -1.00 | 0.00 | 1.00 | 1.25 | 1.50 |
| -1.00 | 1.00 | 0.50↗ | 0.73↗ | 0.88↗ | 0.91↗ | 0.92 |
| 0.00 | 1.50 | 0.38↗ | 0.50↗ | 0.62↗ | 0.65↗ | 0.68 |
| 0.25 | 0.50 | 0.13↗ | 0.41↗ | 0.76↗ | 0.82↗ | 0.87 |

> Note: The probability of some positions does not increase monotonically along the diagonal, violating the double elimination condition

Note that the probabilities sometimes fall diagonally, violating the double elimination condition.

### 3.4.5 Concept Supplement 7: In-depth analysis of double elimination conditions

Intuitive understanding of double elimination conditions

**What is double elimination? **

Imagine a table of ability × item. If we move along the diagonal (simultaneously increasing ability and decreasing item difficulty), the probability of success should always increase.

**Why is it important? **

This condition ensures a consistent additive relationship between ability, item difficulty, and probability of success.

**What does a violation mean? **

If it is violated, it means that performance cannot be predicted by simply subtracting ability from item difficulty.

## 3.5 The special status of Rasch models: rigorous proof of invariance

Rasch models have unique measurement properties that we can understand through rigorous proofs.

### 3.5.1 Comparison of Invariant People: Stability of Ability Differences

**Core question:** Does the difference in ability between two people have the same meaning on all items?

Let us consider two people: \(\theta_1 = -2.20\), \(\theta_2 = -1.10\)

For any itemi, their performance difference is:

\[\ln\left(\frac{P_{1i}}{1-P_{1i}}\right) - \ln\left(\frac{P_{2i}}{1-P_{2i}}\right)\]

**Detailed derivation:**

According to the Rasch model:

\[\ln\left(\frac{P_{1i}}{1-P_{1i}}\right) = \theta_1 - \beta_i\]

\[\ln\left(\frac{P_{2i}}{1-P_{2i}}\right) = \theta_2 - \beta_i\]

Subtract the two equations:

\[\ln\left(\frac{P_{1i}}{1-P_{1i}}\right) - \ln\left(\frac{P_{2i}}{1-P_{2i}}\right) = (\theta_1 - \beta_i) - (\theta_2 - \beta_i)\]

\[= \theta_1 - \theta_2 = -2.20 - (-1.10) = -1.10\]

Amazing result

item difficulty\(\beta_i\) has been eliminated! This means that the performance difference between the two does not depend on item difficulty at all.

![Figure 4.2: Graphical proof of invariant comparison](../assets/images/ch6_fig6.6.png)

Figure 4.2 shows that the differences between people remain constant on different items.

### 3.5.2 Concept Supplement 8: The deeper meaning of immutability

The actual value of immutability

**Meaning in educational applications:**

If Student A is 1 logit unit higher in ability than Student B, then the meaning of this difference is the same whether we test them on easy items or difficult items.

**Meaning in Quiz Development:**

We can use different items to measure the same ability difference without worrying that item selection will affect the comparison results.

### 3.5.3 Comparison of unchanged items: stability of item differences

Similarly, we can show that item difficulty differences do not depend on participant ability:

For any participant, the difficulty difference between two items is:

\[\ln\left(\frac{P_{s1}}{1-P_{s1}}\right) - \ln\left(\frac{P_{s2}}{1-P_{s2}}\right)\]

**Detailed derivation:**

\[\ln\left(\frac{P_{s1}}{1-P_{s1}}\right) = \theta_s - \beta_1\]

\[\ln\left(\frac{P_{s2}}{1-P_{s2}}\right) = \theta_s - \beta_2\]

Subtract the two equations:

\[\ln\left(\frac{P_{s1}}{1-P_{s1}}\right) - \ln\left(\frac{P_{s2}}{1-P_{s2}}\right) = (\theta_s - \beta_1) - (\theta_s - \beta_2)\]

\[= -(\beta_1 - \beta_2)\]

Participant capability \(\theta_s\) has been eliminated!

### 3.5.4 Complexity of 2PL model

In contrast, this simplicity is broken in the 2PL model:

\[\ln\left(\frac{P_{1i}}{1-P_{1i}}\right) - \ln\left(\frac{P_{2i}}{1-P_{2i}}\right)\]

\[= \alpha_i(\theta_1 - \beta_i) - \alpha_i(\theta_2 - \beta_i)\]

\[= \alpha_i(\theta_1 - \theta_2)\]

Now the difference depends on the item's distinction \(\alpha_i\)!

### 3.5.5 Invariance of different scale units

In the IRT model, capabilities (\(\theta\)) can be expressed in different numerical units. Two common scales—logit scale and odds scale—have different invariance implications:

**Logit scale: achieve invariance of differences** (interval scale)

- **scale features:** For any two subjects, the difference in ability \(\theta_1 - \theta_2\) is meaningful.
- **Meaning:** Regardless of the item difficulty, the difference in \(\theta\) constantly affects the logarithmic probability difference of the correct rate.
- **Conclusion:** The logit scale is an **interval scale**, that is, the "additive unit" is meaningful, but the zero point is set arbitrarily.

**Odds scale: Implementing invariance of ratios** (ratio scale)

- **Transformation relationship:** \(\xi_s = e^{\theta_s}\), convert logit to odds scale
- **scale features:** The ability ratio of any two subjects \(\xi_1 / \xi_2\) has a fixed meaning
- **Meaning:** The relative likelihood of success remains consistent as a **multiple**
- **Conclusion:** The odds scale is a **ratio scale**, that is, the "multiplication unit" is meaningful, and the zero point is naturally defined (\(\xi = 0\) when there is no possibility of success)

**Ability ratio has nothing to do with item**

Consider that on any item \(i\), the success probabilities of two participants \(1\) and \(2\) are \(P_{i1}, P_{i2}\) respectively, and their odds ratio is:

\[
\frac{P_{i1}/(1-P_{i1})}{P_{i2}/(1-P_{i2})}
= \frac{\xi_1 / e^{\beta_i}}{\xi_2 / e^{\beta_i}}
= \frac{\xi_1}{\xi_2}
\]

- \(\xi_s = e^{\theta_s}\): Odds of the \(s\) participant
- \(e^{\beta_i}\): The difficulty of item \(i\) is expressed in the odds space

**Inference:**

- Although the difficulty of each question is different (\(\beta_i\)),
- but they cancel each other out in the numerator and denominator,
- So the odds ratio only depends on the ability ratio \(\xi_1 / \xi_2\)

This is the embodiment of **unit invariance**: different items do not change the meaning of the ability difference or ratio between participants.

### 3.5.6 Concept Supplement 9: In-depth understanding of sufficient statistic

The Rasch model also has an important feature: the original total score is a sufficient statistic of ability.

sufficient statistic meaning

**What is sufficient statistic? **

If a statistic contains all information about the parameters in the sample, it is called a sufficient statistic.

**Sufficient statistic in Rasch model:**

In the Rasch model, if two people have the same original total score, then their ability estimates are also the same, regardless of which specific items they answered correctly.

**Derivation of sufficient statistic:**

The likelihood function of the Rasch model can be written as:

\[L(\theta | \mathbf{x}) = \frac{\exp(\theta \sum x_i)}{\prod_i (1 + \exp(\theta - \beta_i))}\]

Among them, \(\sum x_i\) is the original total score. Note that the likelihood function only depends on the total score and not on the specific reaction mode.

This means:

\[P(\mathbf{x} | \sum x_i, \theta) = P(\mathbf{x} | \sum x_i)\]

That is, given a total score, the specific response pattern has nothing to do with ability.

## 3.6 CTT’s scale level dilemma

In stark contrast to IRT, CTT faces fundamental difficulties in establishing scale characteristics.

### 3.6.1 The impact of test difficulty

The fundamental problem of CTT

In CTT, the meaning of score differences is directly affected by test difficulty:

**Easy Quiz:** High ability students differ little (all get high scores)

**Difficult Test:** Little difference among low ability students (all got low scores)

**Moderate Test:** The greatest differences are found among students of moderate ability

### 3.6.2 Strict conditions for interval scale

Proving interval scale in CTT requires two conditions:

1. **Real ability is normal distribution** (hypothetical question)
2. **Observe that the scores show a normal distribution** (operational question)

However, multiple norm groups will cause conflicts:

The paradox of multi-constant modules

Assume that four people have raw scores: 2, 3, 6, 7

**Young people norm (normal):** Linear transformation, maintaining relative distance

**Mania Norm (skewness):** Normalized transformation, changing relative distances

- Distance between 1st and 2nd person: 5 standard units
- Distance between the 3rd and 4th person: 13 standard units

**Contradiction:** The same raw score difference has different meanings in different norms.
