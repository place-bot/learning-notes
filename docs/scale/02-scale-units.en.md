# 2. Numerical interpretation of trait levels: the secret of the scale unit

## 2.1 Why do the same abilities have different values?

When we use different IRT software or different parameter settings, we often find that the trait level of the same person has different values. For example:

puzzling phenomenon

- Software A displays: \(\theta = 1.2\)
- Software B displays: \(\theta = 0.8\)
- Software C display: \(\theta = 2.4\)

Which of these three results is "correct"?

## 2.2 Anchoring system: find a "zero point" for scale

The answer is: they are both probably correct! The difference comes from the difference in the **anchoring system**.

### 2.2.1 Why is anchoring needed?

Let us understand the necessity of anchoring through a derivation example.

Detailed derivation of the model identification problem

In the Rasch model, we want to predict the log odds:

\[
\ln\left(\frac{P_{is}}{1 - P_{is}}\right) = \theta_i - \beta_i
\]

Suppose we want to predict the log odds of 1.5, let's see how many solutions there are:

**Solution 1:** \(\theta = 3,\ \beta = 1.5\)

\[
3 - 1.5 = 1.5 \quad \checkmark
\]

**Solution 2:** \(\theta = 2,\ \beta = 0.5\)

\[
2 - 0.5 = 1.5 \quad \checkmark
\]

**Solution 3:** \(\theta = 1,\ \beta = -0.5\)

\[
1 - (-0.5) = 1.5 \quad \checkmark
\]

**Solution 4:** \(\theta = 0,\ \beta = -1.5\)

\[
0 - (-1.5) = 1.5 \quad \checkmark
\]

All these combinations produce the same predicted result, so the model has an identification problem.

This is the **model identification problem**: the absolute values of the parameters cannot be determined from the data alone, only the relative relationships.

### 2.2.2 Concept Supplement 4: Deep understanding of model identification problems

Why does the recognition problem occur?

**Root Cause:**

In the IRT model, what we really care about is the relative relationship between ability and difficulty (\(\theta - \beta\)), not their absolute values.

**Analogy understanding:**

It's like saying the altitude difference between two cities is 100 meters, but that doesn't tell us the absolute altitude of each city. We need to choose a reference point (such as sea level) to determine the absolute altitude.

**Solution:**

Anchoring is to choose such a reference point so that all parameters have definite values.

### 2.2.3 Anchor to item: Centered on item

**Basic idea:** Set the average item difficulty to 0

item anchor settings

- average item difficulty: \(\mu_\beta = 0\)
- item discrimination: \(\alpha = 1.0\) (Rasch model)
- result: trait level is explained relative to the average difficulty of the item

**Explanation logic:**

Explanation of item anchoring

- \(\theta > 0\): The ability is higher than the average difficulty of the item, and it is easy to answer correctly.
- \(\theta = 0\): The ability is equal to the average difficulty of the item, and the probability of correct answer is 50%.
- \(\theta < 0\): The ability is lower than the average difficulty of the item, and it is not easy to answer correctly.

This anchoring method is particularly suitable for educational measurement because it emphasizes what items students can master rather than their ranking in the group.

### 2.2.4 Anchoring to people: crowd-centered

**Basic idea:** Set the average ability of the population to 0 and the standard deviation to 1

Crowd anchoring settings

- Average ability: \(\mu_\theta = 0\)
- Capability standard deviation: \(\sigma_\theta = 1\)
- result: Trait level is similar to z-score

**Explanation logic:**

Crowd anchoring explained

- \(\theta = 1.0\): 1 standard deviation above the mean, more than 84% of people
- \(\theta = 0\): average, more than 50% of people
- \(\theta = -1.0\): 1 standard deviation below the mean, only more than 16% of people

### 2.2.5 Equivalence of anchoring methods

Here is an important realization:

The nature of anchoring choices

Different anchoring methods simply choose different "coordinate systems", just like temperature can be expressed in degrees Celsius or Fahrenheit.

Important relationships (such as differences in ability between two people) do not change based on anchoring methods.

### 2.2.6 Choice of measurement unit: Logit vs Normal

In addition to anchoring, there is also a choice of measurement units:

**Logit measure:**

\[\ln(P(X_{is})/(1 - P(X_{is}))) = \alpha(\theta_i - \beta_i)\]

**Normal measure:**

\[\ln(P(X_{is})/(1 - P(X_{is}))) = 1.7\alpha(\theta_i - \beta_i)\]

1.7 Source of Multiplier

This constant 1.7 comes from the ratio of the standard deviations of the logistic distribution and the normal distribution. It makes the parameter values ​​under the two measurement systems have similar numerical ranges.

## 2.3 Scale types: different “languages” of numbers

In Item Response Theory (IRT), an individual's ability level \(\theta\) is not the only way to express it. In addition to fixing anchor locations, IRT also allows capabilities to be transformed into different scale representations.

### Definition: What is "scale"?

In IRT, **scale (scale)** refers to the representation method used to express the numerical value of a participant's ability (latent trait). Different scales convey different information focuses, such as differences, ratios, probabilities, etc.

### 2.3.1 Logitscale: The language of difference

**Definition:** Logitscale is the most basic and commonly used IRTscale type, directly derived from the linear prediction part of the logistic model.

\[
\theta \in \mathbb{R}, \quad P(X=1|\theta, \beta) = \frac{1}{1 + e^{-(\theta - \beta)}}
\]

Characteristics of logitscale

- **Value range:** Usually between \(-3\) to \(+3\)
- **Core Features:** Equal spacing (equal differences have the same meaning)
- **Theoretical basis:** Logarithmic odds (log-odds)
- **Applicable scenarios:** Theoretical modeling, model fit, parameter estimation

**Derivation of the meaning of equal spacing:**

Derivation of equidistant properties of logitscale

Suppose the ability difference between two people is \(d = \theta_1 - \theta_2\), then:

\[
\ln\left(\frac{P_1}{1 - P_1}\right) - \ln\left(\frac{P_2}{1 - P_2}\right) = (\theta_1 - \beta) - (\theta_2 - \beta) = d
\]

The log odds difference depends only on ability difference and has nothing to do with item difficulty. Therefore, on a logitscale, the same numerical difference always represents the same behavioral difference.

### 2.3.2 Odds Scale: The language of multiples

**Definition:** Odds scale is the exponential transformation of logit, used to express the multiple relationship between success and failure:

\[
\xi_s = e^{\theta_s}
\]

Characteristics of odds scale

- **Value range:** \((0, \infty)\), always positive
- **Core Features:** Ratios make sense (i.e. "how many times more success than failure")
- **Theoretical basis:** The ratio of success probability to failure probability, defined as \( \text{odds} = \frac{p}{1 - p} \)
- **Applicable scenarios:** Practical explanation and understanding by non-professional readers, such as in education, medical, and psychometrics reports

**Example form:**

|personnel|Logitscale \(\theta_i\)|Odds scale \(\xi_i = e^{\theta_i}\)|Odds explained|
| --- | --- | --- | --- |
|person 1| -2.20 | 0.11 |1 to 9 (failure is better than success)|
|person 2| -1.10 | 0.33 |1 to 3|
|person 3| 0.00 | 1.00 |1 to 1 (50/50)|
|person 4| 1.10 | 3.00 |3 to 1 (success than failure)|
|person 5| 2.20 | 9.02 |9 to 1 (success than failure)|

Intuitive explanation of odds scale

**Odds for Person 4 = 3.0, meaning: **

- The probability of success is 3 times the probability of failure
- If you try 100 times, about 75 will succeed and 25 will fail
- Probability of success = \( \frac{3}{3 + 1} = 0.75 \)

### 2.3.3 Concept Supplement 5: Odds vs Probability

The difference between odds vs probability

- **Probability:** Number of successes / total number of times, the range is \([0, 1]\)
- **Odds:** Number of successes/number of failures, the range is \([0, \infty)\)

**The conversion relationship is as follows:**

- From probability to odds:

\[
\text{odds} = \frac{p}{1 - p}
\]

- From odds to probability:

\[
p = \frac{\text{odds}}{1 + \text{odds}}
\]

Odds are more discriminative, especially in low probability areas.

### 2.3.4 Proportion True Score: The language of success rate

**Definition:** The proportional true score refers to a person's **average accuracy** on a certain set of items, that is, the expected score:

\[
P_{is} = \frac{1}{I} \sum_{i=1}^{I} P(X_{is} = 1 | \theta_s, \beta_i)
\]

Characteristics of Proportional Proper Fractions

- **Value range:** \([0, 1]\), represents the expected accuracy rate
- **Core Features:** Intuitive and easy to understand, suitable for direct display as "accuracy rate"
- **Theoretical basis:** The average of the sum of the probabilities of answering each question correctly, that is

\[
\text{EPC} = \frac{1}{I} \sum_{i=1}^I P(X_i = 1)
\]

- **Applicable scenarios:** Test reports, ability explanations, understanding by non-professional audiences

**Example form:**

|people| Logit \(\theta_i\) |Quiz 1 (Easy)|Quiz 2 (Hard)|item bank overall|
| --- | --- | --- | --- | --- |
|person 1| -2.20 | 0.13 | 0.06 | 0.18 |
|person 2| -1.10 | 0.28 | 0.14 | 0.28 |
|person 3| 0.00 | 0.50 | 0.30 | 0.50 |
|person 4| 1.10 | 0.71 | 0.52 | 0.72 |
|person 5| 2.20 | 0.87 | 0.73 | 0.85 |

Important Limitations of Proportional Proper Fractions

Note the difference between Person 1 and Person 2:

- On easy quizzes: 0.28 - 0.13 = 0.15
- On the hard test: 0.14 - 0.06 = 0.08

**Note:** The same ability difference will show different score differences on different difficulty groups of questions. Therefore, proportional true scores are not an equally spaced scale and are not suitable as a strict measurement index of ability.

### Summary

|scale|Example|Features|Applicable|
| --- | --- | --- | --- |
|Logitscale| \(\theta = 1.2\) |Equally spaced, theoretical modeling|Model estimation|
|Odds scale| \(e^{1.2} = 3.32\) |Explanation of multiples|Practice communication|
|proportional true fraction| \(P = 0.75\) |Easy to read and intuitive|Score report|

## 2.4 Specific examples of trait level explanations

Now let's put all the concepts together and see how a specific trait level can be explained.

### 2.4.1 Comparison with item: direct mapping of capabilities

Example of person-item comparison

**Situation:** Use energy to wake up scale, item anchoring, Logitscale

**Person 4 Trait Level:** \(\theta = 0.90\)

**Steps explained:**

1. Find the item with a difficulty of 0.90: "Energy"
2. Predicted probability of agreement: P = 0.50
3. For easier items: higher probability
4. For more difficult items: lower probability

![Figure 3.1: Comparing people and items: the odds of two people](../assets/images/ch6_fig6.3.png)

Figure 3.1 shows the comparison of the success odds of two people on different items. We can see that person 4 generally has higher odds of identifying with any item on the scale, due to higher trait levels.

### 2.4.2 Concept Supplement 6: Nonlinear Characteristics of Odds Difference

Key observations

Note that their odds vary greatly on easy items and less on hard items.

This shows that although logitscale has equidistant properties, when we convert to odds scale, this equidistant property is no longer maintained.

### 2.4.3 Comparison with standards: Judgment of absolute level

We can set a standard, such as "indifference" (neither agree nor disagree).

![Figure 3.2: Comparison with standard: no difference](../assets/images/ch6_fig6.4.png)

Figure 3.2 shows that the characteristic curve of person 3 is close to the indifference criterion. The indifference criterion is a particularly interesting concept because it represents a neutral point.

### 2.4.4 Comparison with the norm: Determination of relative position

IRT can also provide traditional norm comparisons, but is richer.

![Figure 3.3: Person-item frequency distribution](../assets/images/ch6_fig6.5.png)

Figure 3.3 shows the relationship between human ability distribution and item difficulty distribution. The upper level shows the frequency distribution of people in logit units, and the lower level shows the item difficulty distribution.

The importance of person-item distribution matching

This two-level distribution plot provides important information about the quality of the test. Ideally, the item difficulty distribution should match the person ability distribution to provide accurate measurements for people of all ability levels.

## 2.5 Practical considerations for scale selection

Faced with so many choices, how should we decide which scale to use?

Guidelines for scale selection

**Logitscale - when required:**

- Theoretical analysis and model comparison
- Accurate statistical inference
- Ability comparison across tests

**Odds scale - when required:**

- Explain results to non-experts
- Emphasis on the multiple relationship of success probability
- Conduct risk assessment

**Proportional True Fractions - When Needed:**

- The most intuitive explanation
- Analogy to traditional fractions
- But beware of its limitations
