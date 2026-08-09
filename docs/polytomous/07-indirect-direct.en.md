# 7. Concept Supplement 3: Calculation logic of indirect model and direct model

In multi-category Item Response Theory (IRT), there are two main modeling methods: indirect models (such as GRM) and direct models (such as PCM). They use different calculation ideas when calculating the response probability of each category.

## 7.1 "Two-step process" of indirect model

### 7.1.1 Taking the graded response model (GRM) as an example

Step 1: Calculate the operating characteristic curve \( P_x^*(\theta) \)

Use the formula:

\[
P_x^*(\theta) = \frac{\exp[\alpha_i(\theta - \beta_{ij})]}{1 + \exp[\alpha_i(\theta - \beta_{ij})]}
\]

This formula represents the probability that a subject answers in "category x or above."

For example: for an item with 5 categories (0–4),

- \( P_1^*(\theta) \): Probability of reaction in category 1 or above (i.e. sum of categories 1, 2, 3, 4)
- \( P_2^*(\theta) \): Probability of response in category 2 or above
- \( P_3^*(\theta) \): Probability of response in category 3 or above
- \( P_4^*(\theta) \): Probability of response in category 4

Step 2: Calculate the exact class probability \( P_x(\theta) \) through the difference

Use the formula:

\[
P_x(\theta) = P_x^*(\theta) - P_{x+1}^*(\theta)
\]

The specific calculation is as follows:

- \( P_0(\theta) = 1.0 - P_1^*(\theta) \)
- \( P_1(\theta) = P_1^*(\theta) - P_2^*(\theta) \)
- \( P_2(\theta) = P_2^*(\theta) - P_3^*(\theta) \)
- \( P_3(\theta) = P_3^*(\theta) - P_4^*(\theta) \)
- \( P_4(\theta) = P_4^*(\theta) \)

## 7.2 "One-step process" of direct models

### 7.2.1 Take partial credit model (PCM) as an example

Directly calculate the response probability of each category, using the formula:

\[
P_x(\theta) = \frac{\exp\left[\sum_{j=0}^{x}(\theta - \delta_{ij})\right]}{\sum_{r=0}^{m_i}\exp\left[\sum_{j=0}^{r}(\theta - \delta_{ij})\right]}
\]

This formula directly gives the probability that a subject answers in the specific category \( x \) in one step, without intermediate steps.

Features:

- No need to first calculate the cumulative probability of "or above"
- No need for difference calculation, directly obtain the probability of each type

## 7.3 Differences in modeling ideas

Indirect models (such as GRM):

1. Convert multi-category problems into multiple binary classification problems of "whether it is above the threshold"
2. Calculate the logic function once for each threshold
3. Obtain the probability of each category through the combination of adjacent differences

Direct model (such as PCM):

1. Directly use rating category modeling
2. Construct a polynomial model for summation of exponential terms
3. Obtain the probabilities of all categories in one step

## 7.4 Analogy understanding

The idea of the indirect model can be analogized to:

First ask: "Are you taller than 160cm? 170cm? 180cm?"
Then extrapolate: “Your height is probably between 170–180cm.”

The idea of a direct model is more like:

Ask directly: “Where is your height? 150–160, 160–170, 170–180, or over 180?”

## 7.5 M-GRM is also an indirect model

The modified grade response model (M-GRM) still follows a two-step logic in the calculation process:

1. First calculate the operating characteristic curve (such as formula 5.3 / 5.4)
2. Then obtain the category probability through the difference (Formula 5.5)

Although the parameter expression of M-GRM is different (such as \( \beta_{ij} = b_i - c_j \)), the calculation idea is consistent with GRM.

## 7.6 Summary

|Model type|Calculation method|Features|
| --- | --- | --- |
| GRM / M-GRM |Indirect (two steps)|Multiple binary classification models + difference operation|
| PCM / RSM |direct (one step)|Polynomial modeling, direct normalization calculation|

Indirect models build probabilities through "detours" of logistic functions, while direct models do it all in one go.
