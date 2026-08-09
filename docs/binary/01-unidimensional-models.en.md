# 1. Single-dimensional IRT model for binary data

## 1.1 When to use single-dimensional IRT model?

In the unidimensional IRT model, a single latent trait is considered sufficient to characterize individual differences.

**Popular understanding:** Just like measuring height with a ruler, we assume that a numerical value can represent a certain ability.

The single-dimensional IRT model is suitable for the following situations:

1. When a single common factor dominates item response time
2. When all items involve the same combination of each factor (even if there are multiple potential factors)

**Example description:**

- Applicable: Pure calculation ability test (all items only test calculation)
- Applicable: Even if the test contains calculation and reasoning, each question is a fixed combination of 70% calculation + 30% reasoning

Cases where the single-dimensional IRT model is not applicable

The single-dimensional IRT model is not applicable when the following conditions occur:

1. Two or more latent traits have different effects on the item
2. Individuals have systematic differences in strategies, knowledge structures, or explanations applied to items.

In these cases, multidimensional IRT models should be used.

**Example:**

- In the Chinese language test, some items mainly test reading comprehension, and some mainly test writing ability.
- When students solve problems, some use algebraic methods and some use geometric methods.

## 1.2 Symbol system

In the one-dimensional models presented in this chapter, the following notations will be used:

- \(X_{is}\): The response of individual \(s\) to item \(i\) (0 or 1)
- \(\theta_s\): The trait level (ability value) of individual \(s\)
- \(\beta_i\): The difficulty of item \(i\)
- \(\alpha_i\): Discrimination of item \(i\)
- \(\gamma_i\): The lower asymptote of item \(i\) (guessing parameter)

**Intuitive understanding of these parameters:**

- \(\theta_s\): Like a student's "ability score", usually between -3 and +3
- \(\beta_i\): The "difficulty score" of the item, using the same scale as the ability
- \(\alpha_i\): item "sensitivity", whether it can distinguish students with different abilities
- \(\gamma_i\): The lower limit of the probability of pure guessing

## 1.3 Example Dataset: Abstract Reasoning Test (ART)

To illustrate three logical unidimensional IRT models, we use a large data set. Data come from the Abstract Reasoning Test (ART; Embretson, 1998) and include:

- 30 items
- Sample of 787 young adults
- Estimation of IRT parameters by marginal maximum likelihood method using the BILOG program

**Table 4.1: Classic item statistics of 30 items in the abstract reasoning test**

|item|Number of people passing|correct percentage|biserial correlation|
| --- | --- | --- | --- |
| 1 | 746 | .948 | .582 |
| 2 | 439 | .558 | .483 |
| 3 | 662 | .841 | .407 |
| 4 | 519 | .659 | .465 |
| 5 | 634 | .806 | .539 |
| ... | ... | ... | ... |
| 22 | 188 | .239 | .174 |
| 25 | 164 | .208 | .200 |
| 30 | 334 | .424 | .249 |

Observed data characteristics:

- Item difficulty varies greatly: correct percentage ranges from 20.8% to 94.8%
- Biserial correlations are all positive, with only a few below .30

**Data Interpretation:**

- Almost everyone answered item1 correctly (94.8%), the explanation is very simple
-Only 20.8% of people answered item25 correctly, which means it is very difficult.
- Items with high bi-column correlation (such as .582 for item1) can well distinguish between high and low ability people.

## 1.4 Point-Biserial Correlation

**Definition**:

Biserial correlation is a special kind of Pearson correlation, which is used to measure the degree of correlation between a binary variable (such as whether the item is answered correctly) and a continuous variable (such as total score).

**Popular explanation:**

Imagine a class exam where the question asked in a double column is: "Do students who answer this question correctly generally have a higher total score?"

**Meaning**:

- The higher the value (usually > .30), it means that the item can better distinguish between high-scoring and low-scoring examinees.
- A value close to 0 means that the item has no distinguishing effect on people with high and low abilities, and may be an invalid item**.
- Negative values usually indicate that the item design is incorrect (for example, the score is wrong or the answer is too disruptive).

**Calculation formula (simplified form)**:

\[
r_{pb} = \frac{\bar{X}_1 - \bar{X}_0}{s_X} \sqrt{ \frac{p \cdot q}{n} }
\]

Among them:

- \(\bar{X}_1\): The average total score of those who answered the question correctly
- \(\bar{X}_0\): The average total score of those who answered the question incorrectly
- \(s_X\): total score standard deviation
- \(p\): Proportion of correct answers
- \(q = 1 - p\)

**Practical explanation**:

- Item 1 (r = .582) has a high degree of discrimination, indicating that high-ability examinees are more likely to get it right;
- Item 22 (r = .174) has low discrimination, even though it is difficult, it cannot effectively distinguish examinee;
- If the item has a medium accuracy rate + a high biserial correlation, it is a very ideal item.

**Why is this important? **

Good test items should be easy for people with high ability to answer correctly, but not easy for people with low ability to answer correctly. If everyone answers a question correctly or incorrectly, or if the correct answer or incorrect answer has nothing to do with ability (it depends on luck), the question has no measurement value.

Note: Biserial correlation is one of the most commonly used indicators to measure item quality in **Classical Test Theory**.
