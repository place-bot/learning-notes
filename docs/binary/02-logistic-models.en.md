# 2. Traditional logic model

## 2.1 Basics of logical distribution

The logistic IRT model is based on a logistic distribution, which gives the response probability in a simple expression.

**Why use logistic distribution? **
We need a function that can convert any range of values (-∞ to +∞) into probabilities (0 to 1). Logical functions just meet this need!

Core formula: If \(w_{is}\) represents the combination of individual and item parameters in the model, the probability is expressed as follows:

\[
P(X_{is} = 1|w_{is}) = \frac{\exp(w_{is})}{1 + \exp(w_{is})} \tag{4.1}
\]

Among them:

- \(\exp(w_{is})\) (also written \(e^{w_{is}}\)) is the base of the natural logarithm (2.718...) raised to the power \(w_{is}\)
- The probability of success is calculated by taking the inverse of \(w_{is}\)

**Understand this formula:**

When \(w_{is} = 0\):

\[
P = \frac{e^0}{1 + e^0} = \frac{1}{2} = 0.5
\]

When \(w_{is} = 2\):

\[
P = \frac{e^2}{1 + e^2} = \frac{7.39}{8.39} \approx 0.88
\]

When \(w_{is} = -2\):

\[
P = \frac{e^{-2}}{1 + e^{-2}} = \frac{0.135}{1.135} \approx 0.12
\]

**Key Insights:**

- The larger \(w_{is}\) is, the closer the probability is to 1
- The smaller \(w_{is}\) is, the closer the probability is to 0
- When \(w_{is} = 0\), the probability is exactly 0.5
- This creates a smooth S-shaped curve!

## 2.2 one-parameter logistic model (1PL) or Rasch model

### 2.2.1 Formal expression of model

The Rasch model predicts the probability of individual s succeeding on itemi:

\[
P(X_{is} = 1|\theta_s,\beta_i) = \frac{\exp(\theta_s - \beta_i)}{1 + \exp(\theta_s - \beta_i)} \tag{4.2}
\]

Key things to understand:

- The logit of Formula 4.2, \(\theta_s - \beta_i\), is the simple difference between trait level and item difficulty
- This difference replaces \(w_{is}\) in Equation 4.1
- The Rasch model is also called a one-parameter logistic (1PL) model because it contains only one item parameter (difficulty)

**Intuitive understanding of Rasch model:**

Imagine a high jump competition:

- \(\theta_s\) = Athletes' high jumping ability (for example, able to jump 1.8 meters)
- \(\beta_i\) = the height of the crossbar (for example, set at 1.5 meters)
- \(\theta_s - \beta_i\) = The degree to which ability exceeds difficulty (1.8 - 1.5 = 0.3 meters)
- The more you exceed, the greater your probability of success!

**Specific calculation example:**

Student ability \(\theta_s = 1.0\), item difficulty \(\beta_i = 0.5\):

\[
P = \frac{\exp(1.0 - 0.5)}{1 + \exp(1.0 - 0.5)} = \frac{\exp(0.5)}{1 + \exp(0.5)} = \frac{1.65}{2.65} \approx 0.62
\]

This student has a 62% probability of answering this question correctly!

### 2.2.2 Another expression form of the model

The 1PL model can also be represented by the constant item discrimination value \(\alpha\):

\[
P(X_{is} = 1|\theta_s,\beta_i) = \frac{\exp(\alpha(\theta_s - \beta_i))}{1 + \exp(\alpha(\theta_s - \beta_i))} \tag{4.3}
\]

The difference between the two forms:

- Formula 4.3: The constant value of item discrimination is freely estimated
- Formula 4.2: The value of constant item discrimination is assumed to be 1.0

**What does the discrimination α do? **

Imagine two thermometers:

- α = 1: Standard thermometer, the temperature changes by 1 degree, the display changes by 1 degree
- α = 2: Sensitive thermometer, temperature changes by 1 degree, display changes by 2 degrees
- α = 0.5: Dull thermometer, the temperature changes by 1 degree, the display only changes by 0.5 degrees

In IRT, α determines the degree to which ability differences are reflected in probability.

Important note

The choice of measurement scale for the constant (1.0 or free estimate) has consequences for other parameters in the model (discussed in Chapter 6).

But with all parameters appropriately measured scaled, Equations 4.2 and 4.3 give exactly the same predictions.

### 2.2.3 item characteristic curve (ICC)

![Figure 4.1: item characteristic curve](../assets/images/ch4_fig4.1.png) of one-parameter logistic model

Figure 4.1 shows the item characteristic curves (ICCs) of three items in the Rasch model.

## 2.3 Key features of Rasch model ICC:

1. **S-shaped curve**:
   The probability gradually increases with the trait level of each item.

   **Why is it S-shaped? **

   - When the ability is very low, even if it is lowered, the probability of correct answer is close to 0
   - When the ability is very high, even if it is improved, the probability of correct answer is close to 1
   - The middle part changes the fastest, forming an S shape
2. **Parallel Curves**:

   - items only differ in difficulty
   - The slopes of the curves are equal
   - Curves converge but do not intersect

   **Analogy understanding:**

   It's like three slides of the same shape, but with different starting heights
3. **Inflection point characteristics**:

   - The inflection point of ICC (the point where the rate of change switches from increasing acceleration to increasing deceleration) occurs when the probability of passing the item is .50
   - The reference line starts from a trait level equal to item difficulty and crosses the ICC at probability .50

   **Actual meaning:**

   When the student's ability is exactly equal to the item difficulty, the probability of correct answer is exactly 50%
4. **Explanatory**:

   - Trait level can be interpreted as the threshold level of item difficulty
   - Indicates that individuals have an equal chance of passing or failing
   - For example: for an item with a difficulty of 1.00, the probability of an individual with a trait level of 1.00 passing the item is .50

### 2.3.1 Parameter estimation example

**Table 4.2: Rasch model item parameter estimates for abstract reasoning test**

|item| β | σ_β |
| --- | --- | --- |
| 1 | -2.826 | .172 |
| 2 | -.176 | .081 |
| 3 | -1.479 | .104 |
| ... | ... | ... |
| 22 | 1.809 | .086 |
| 25 | 2.008 | .090 |
| 30 | .841 | .076 |

-2 log Likelihood = 25924.52

**Interpret this form:**

- β is an estimate of item difficulty
- σ_β is the standard error (uncertainty of the estimate)
- Negative values indicate easy items, positive values indicate difficult items
- item1 (β = -2.826) is very easy
- item25 (β = 2.008) is very difficult

Observe the result:

- item difficulty ranges from -2.826 to 2.008
- The standard error of item difficulty varies between items.
- Generally speaking, the standard error of extreme item difficulty is larger

**Why is the standard error of extreme items larger? **

Imagine estimating the height of a mountain:

- If many people can climb it, we know exactly how difficult it is
- If almost no one can climb it, we have limited knowledge of its true difficulty
- The less information, the more uncertain the estimate!

Use of standard error

The standard error can be used to set the confidence interval around the item difficulty estimate.

For example, the 95% confidence interval of item1 is approximately: -2.826 ± 1.96 × 0.172 = [-3.163, -2.489]

**Practical significance:** We are 95% sure that the true difficulty of this question is between -3.163 and -2.489

## 2.4 two-parameter logistic model (2PL)

### 2.4.1 Why is the 2PL model needed?

In reality, not all items are equally effective in differentiating student abilities:

- Some items are very sensitive (high discrimination) → can distinguish students with different abilities well
- Some items have poor differentiation effect (low discrimination) → insensitive to changes in abilities

**Specific example:**

Consider two questions:

1. "Calculate 2+2 = ?" (low discrimination: almost everyone can)
2. "Solve the equation x² + 3x - 4 = 0" (High discrimination: able to distinguish students who can solve equations from those who cannot)

Even if the difficulty is adjusted, the first question still cannot distinguish students' abilities very well!

### 2.4.2 Expression

The 2PL model adds itemdiscrimination parameter \(\alpha_i\):

\[
P(X_{is} = 1|\theta_s,\beta_i,\alpha_i) = \frac{\exp[\alpha_i(\theta_s - \beta_i)]}{1 + \exp[\alpha_i(\theta_s - \beta_i)]} \tag{4.4}
\]

**Key differences from the Rasch model:**

Compare Equation 4.4 with Equation 4.3:

- itemdiscrimination parameter has subscript \(\alpha_i\)
- This represents the **difference** of item discrimination
- Therefore, the 2PL model is suitable for measurement of unequal relationships between items and latent traits.

### 2.4.3 The role of discrimination parameter

The meaning of discrimination parameter \(\alpha_i\):

- \(\alpha > 1\): Steep ICC, sensitive to capability changes
- \(\alpha = 1\): Standard slope (equivalent to Rasch)
- \(\alpha < 1\): Flat ICC, insensitive to ability changes
- \(\alpha < 0\): Negative discrimination (usually indicates there is a problem with the item)

**Image metaphor:**

Imagine hillsides with different slopes:

- \(\alpha = 2\): Steep hill, a little horizontal movement, big change in altitude
- \(\alpha = 1\): Standard hillside, 45 degree angle
- \(\alpha = 0.5\): gentle slope, you need to walk a long way to climb higher
- \(\alpha < 0\): Downhill! (The higher the ability, the greater the probability of incorrect answers, indicating that there is a problem with the item)

### 2.4.4 item characteristic curve comparison

![Figure 4.2: item characteristic curve](../assets/images/ch4_fig4.2.png) of two-parameter logistic model

Figure 4.2 shows the item characteristic curves of three items under the 2PL model.

**Comparison of ICC curves of different parameter combinations under the 2PL model**

- The **difficulty parameter b between items is different**, they are -1.0, 0.0, 1.0 respectively;
- item1 and 2 have the same discrimination parameter α = 0.5**, but different difficulties;
- item2 and 3 have the same difficulty parameter b = 0**, but have different degrees of differentiation;
- The ICC of item2 intersects with items1 and 3, indicating that their probability rankings at different θ levels have been reversed;
- In the 2PL model, **regardless of the value of α, at the θ value corresponding to itemdifficulty parameterb, the probability of correct answer is always 0.50**

**Meaning of Crossover:**

Intersecting curves means:

- A certain question may be easier for low-ability students
- For high ability students, another question may be easier
- This cannot happen in the Rasch model (parallel lines do not intersect)!

### 2.4.5 Parameter estimation comparison

**Table 4.3: Comparison of parameter estimates between Rasch model and 2PL model**

|item| Rasch β | 2PL α | 2PL β |
| --- | --- | --- | --- |
| 1 | -2.826 | 1.578 | -2.118 |
| 22 | 1.809 | 0.476 | 2.815 |
| ... | ... | ... | ... |

-2 log Likelihood (2PL) = 25659.39

**Important findings:**

**Significant difference in discrimination**: range from 0.476 to 2.154

- This suggests that the constant item discrimination assumption may not fit the data

**Changes in Difficulty Estimate**:

- The item difficulty of the 2PL model is different from that of the Rasch model
- As item discrimination decreases, item difficulty becomes more extreme
- For example: item22 (minimum discrimination 0.476) is more extreme in difficulty in 2PL (2.815) than in Rasch (1.809)

### 2.4.6 Explanation: Why does low discrimination lead to extreme difficulty?

When the discrimination is very low, the ICC curve is very flat. To achieve P = 0.5 at θ = β, more extreme β values ​​are needed to compensate for the low slope.

**Explanation:**

At the inflection point (θ=β), the slope of ICC is:

\[
\frac{\partial P}{\partial \theta}\bigg|_{\theta=\beta} = \frac{\alpha}{4}
\]

The smaller the slope (smaller α), the flatter the curve, and more extreme positions are required to differentiate between individuals of different abilities.

**Intuitive understanding:**

Imagine two seesaws:

1. Standard seesaw (α=1): the fulcrum is in the middle and the balance point is clear
2. Extra-long seesaw (α=0.5): To also achieve balance, the fulcrum needs to be moved to a more extreme position

This is why the difficulty parameter of low-discrimination items will be "pushed" to more extreme values!

## 2.5 three-parameter logistic model (3PL)

### 2.5.1 The necessity of introducing guessing parameter

Consider a real-life problem: In a multiple-choice question of 1 out of 4, even if you don't know it at all, there is a 25% probability of getting the answer right by random guessing. How to account for this guesswork in the model?

**Real scene:**

In standardized tests (such as SAT, GRE):

- Students will guess when faced with items they do not know.
- Completely random guessing has a 1/4 success rate
- But smart guessing (which excludes obviously wrong options) has a higher success rate
- Ignoring this factor will underestimate the actual scores of low-ability students

### 2.5.2 Expression

The 3PL model accommodates the guesswork by adding the lower asymptote parameter \(\gamma_i\):

\[
P(X_{is} = 1|\theta_s,\beta_i,\alpha_i,\gamma_i) = \gamma_i + (1-\gamma_i)\frac{\exp[\alpha_i(\theta_s - \beta_i)]}{1 + \exp[\alpha_i(\theta_s - \beta_i)]} \tag{4.5}
\]

**Intuitive understanding of the model:**

This can be understood as a combination of two processes:

1. Guess directly with probability \(\gamma_i\)
2. Really know the answer with probability \((1-\gamma_i)\), and then decide whether the answer is correct according to the ability level

Actually:

\[
P(\text{Correct answer}) = P(\text{Guess right}) + P(\text{Don't guess}) \times P(\text{Know the answer|Don’t guess})
\]

**Examples:**

Assuming \(\gamma = 0.2\) (20% correct guess probability), the student’s true ability corresponds to 60% correct answer probability:

\[
P(\text{Final answer correct}) = 0.2 + 0.8 \times 0.6 = 0.2 + 0.48 = 0.68
\]

Even if you were only 60% sure originally, after taking into account the guesses, you have a 68% chance of getting the answer right!

### 2.5.3 Characteristics of guessing parameter

**Important facts about \(\gamma_i\):**

1. \(\gamma_i\) = lower asymptote of item
2. Indicates the probability of correct answers when ability is extremely low
3. Usually not equal to random guess probability (1/number of options)

**Why \(\gamma_i\) ≠ 1/number of options? **

- Systematic guessing strategy: examinee can eliminate obviously wrong options
- Partial knowledge: even if not completely certain, there is a certain tendency
- Differences in option attractiveness: some distractors are designed to be more confusing

**Example:**

Consider the item: "What is the capital of the United States?"

A. New York B. Washington C. Los Angeles D. Chicago

Even if they are not sure, many people will guess between A and B. The actual probability of guessing correctly may be 40% instead of 25%!

### 2.5.4 item characteristic curve

![Figure 4.3: item characteristic curve](../assets/images/ch4_fig4.3.png) of three-parameter logistic model

Figure 4.3 shows three items with the same difficulty and discrimination but different lower asymptotes.

**Key Features:**

- Even at the lowest trait level, item success probability is greater than zero
- For the item \(\gamma_i = 0.25\), even if the ability is extremely low, the probability of success is at least 0.25

### 2.5.5 Changes in parameter meanings

Important changes

In the 3PL model, the meaning of \(\beta_i\) has fundamentally changed!

- It is no longer the ability value corresponding to \(P = 0.5\)
- It is the ability value corresponding to the **inflection point** (the point where the curve change rate is the largest)
- The probability at this time is: \(P = \gamma_i + \dfrac{1 - \gamma_i}{2}\)

**The derivation process is as follows:**

In the 3PL model, the item characteristic curve is:

\[
P(\theta) = \gamma_i + (1 - \gamma_i) \cdot \frac{1}{1 + e^{-a_i(\theta - \beta_i)}}
\]

Let the internal logistic function part be written as:

\[
L(\theta) = \frac{1}{1 + e^{-a_i(\theta - \beta_i)}}
\]

We know that the inflection point of \(L(\theta)\) is at \(\theta = \beta_i\), and its value is:

\[
L(\beta_i) = \frac{1}{1 + e^0} = \frac{1}{2}
\]

So:

\[
P(\beta_i) = \gamma_i + (1 - \gamma_i) \cdot \frac{1}{2} = \gamma_i + \frac{1 - \gamma_i}{2}
\]

That is:

\[
P(\beta_i) = \frac{1 + \gamma_i}{2}
\]

This shows that: in the 3PL model, \(\beta_i\) no longer represents \(P = 0.5\), but represents the ability level at the **inflection point** of the curve, and the corresponding correct answer probability is higher than 0.5, depending on the size of \(\gamma_i\) (guessing parameter).

**Calculation example:**

If \(\gamma_i = 0.2\), then at \(\theta = \beta_i\):

\[
P = 0.2 + \frac{0.8}{2} = 0.2 + 0.4 = 0.6
\]

This means that item difficulty does not correspond to a 50% pass rate, but a 60% pass rate!

**Why is this important? **

When interpreting the results of the 3PL model, we cannot simply say "a difficulty of 1.0 means that students with an ability of 1.0 have a 50% probability of answering correctly", but the influence of the guessing parameter must be considered!

### 2.5.6 Parameter estimation example

**Table 4.4: Estimates of 3PLitem parameters for the abstract reasoning test**

|item| α | β | γ |
| --- | --- | --- | --- |
| 1 | 1.286 | -2.807 | .192 |
| 2 | 1.203 | .136 | .162 |
| ... | ... | ... | ... |
| 22 | 1.150 | 2.609 | .170 |
| 25 | .728 | 3.461 | .128 |

-2 log Likelihood = 25650.60

**Observe result:**

- The lower asymptote estimate is just above zero and ranges from .095 to .226
- Most are below 0.25 (random guess probability of one of four choices)
- Due to lower asymptote changes, item difficulty and discrimination estimates are different from the 2PL model

**Actual explanation:**

These results indicate:

- Even for the most difficult items, there is about a 10-20% chance of guessing it right.
- The guessing parameter is generally lower than the theoretical value of 0.25, indicating that the interference option design is effective
- Different items have different guessing difficulties, reflecting the characteristics of the item

estimation problem

3PL models that estimate unique lower asymptotes for each item can lead to estimation problems (see Chapter 8).

To avoid such problems, it is common to estimate a common lower asymptote for all items or groups of similar items.

**Reason:** The guessing parameter is difficult to estimate accurately and requires a large amount of data from low-capacity participants.

## 2.6 Model selection: Which model is most suitable?

### 2.6.1 Selection criteria

Several criteria can be applied to determine the best model:

**1. The weight of item in the rating**

- Requires equal weighting → Rasch model
- Allow different weights → 2PL or 3PL model

**Practical considerations:**

-Standardized tests: usually 1 point per question, suitable for Rasch
- Diagnostic evaluation: important items should have greater weight, suitable for 2PL

**2. scale attribute requirements**

- Need the strongest proof of scale property → Rasch model
- Pay more attention to fit → 2PL or 3PL model

**Explanation:**
The Rasch model satisfies "specific objectivity":

- Comparing the abilities of any two people has nothing to do with which items they use.
- The difficulty comparison of any two questions has nothing to do with who answered them

**3. Fit to the data**

- Compare models using statistical tests
- Likelihood ratio test, AIC, BIC, etc.

**4. Purpose of parameter estimation**

- Understand item characteristics → Consider the interpretability of parameters
- Accuracy ability estimate → choose the best fitting model

### 2.6.2 Likelihood Ratio Test

Likelihood ratio tests were used to compare nested models.

**What is a nested model? **

- Rasch is a special case of 2PL (all α=1)
- 2PL is a special case of 3PL (all γ=0)
- Simple models are "nested" within complex models

**Testing principle:**

In maximum likelihood estimation, -2 times the log-likelihood of the data represents the degree to which the data deviates from the model.

**Why is it -2 times the logarithm? **

The statistics constructed in this way approximately obey the chi-square distribution, which is convenient for hypothesis testing!

**Test statistic:**

\[
\chi^2 = -2 \log L_{\text{simple}} - (-2 \log L_{\text{complicated}})
\]

Degrees of freedom = number of parameters added to a complex model

**Example: 2PL vs Rasch**

```text
Rasch model:
- Number of parameters: 30 difficulty parameters
- -2logL = 25924.52

2PL model:
-Number of parameters: 30 difficulty + 30 discrimination = 60
- -2logL = 25659.39

Test statistic:
χ² = 25924.52 - 25659.39 = 265.13
df = 60 - 30 = 30

Conclusion: p < 0.001, 2PL is significantly better than Rasch
```

**Explanation:**
The huge chi-square value (265.13) shows that allowing variation in discrimination significantly improves model fit!

**Example: 3PL vs 2PL**

```text
χ² = 25659.39 - 25650.60 = 8.79
df = 30
Conclusion: p > 0.05, 3PL is not significantly better than 2PL
```

**Explanation:**
The small improvement (8.79) is not enough to justify adding 30 guessing parameters.

### 2.6.3 Comparison of parameter estimates

![Figure 4.4: Regression relationship between two-parameter and three-parameter logistic model item difficulty on Rasch model](../assets/images/ch4_fig4.4.png)

Figure 4.4 shows the differences in item difficulty estimates between different models.

**Interpretation:**

- Each point represents the β comparison of an item under the Rasch and 2PL/3PL models
- The closer to the diagonal y=x, the model estimate is consistent
- Visible in the picture: 2PL model (block) has more bias compared to Rasch
- This bias is most obvious among "low-discrimination" items
- The guessing parameter \(\gamma_i\) is introduced in the 3PL model, which is closer to Rasch’s β estimate.
- In 2PL/3PL, the explanation of item difficulty needs to be understood together with the discrimination parameter.

### 2.6.4 Why are the item difficulties different in 2PL and Rasch models?

In the Rasch model (i.e. 1PL), the distinction of each item is fixed at \(\alpha = 1\),
The difficulty parameter \(\beta_i\) of item accurately represents:

> The probability of an individual answering this item at the ability \(\theta = \beta_i\) is 0.5.

Therefore, \(\beta_i\) only determines the position of the ICC curve on the horizontal axis.

But in the 2PL model, the probability of correct answer is determined by the following formula:

\[
P(\theta) = \frac{1}{1 + \exp(-\alpha_i(\theta - \beta_i))}
\]

Here \(\alpha_i\) is the distinction of the item, which is allowed to vary depending on the topic.
This brings two important impacts:

1. \(\beta_i\) still represents the **inflection point position** of the ICC curve, but **is no longer always P=0.5** (unless \(\alpha_i = 1\))
2. When \(\alpha_i\) is very small (the curve becomes gentle), in order to fit the "fuzzy answering pattern", the model will drag the ICC wider and "further" to both sides.
3. So here it comes: **The difficulty of low-discrimination items is estimated to be more off-center (more extreme)**

**Image analogy intuition:**

- item A: \(\alpha = 1.5\), ICC is steep → the inflection point is concentrated near the average ability of the crowd
- item B: \(\alpha = 0.3\), ICC is very flat → the inflection point needs to be "zoomed out" to align the observation data
- So even if the original data of the two items look similar, **the question with low discrimination β will be estimated further** (for example, from 0 to ±1.5)

**Actual meaning:**

This reminds us that in the 2PL model:

- difficulty parameter cannot be interpreted in isolation
- Distinction must also be considered
- "Extremely difficult" questions with low discrimination may actually have poor discrimination effects

Summary:

- In Rasch, capability level \(\beta_i\) = P=0.5
- In 2PL, \(\beta_i\) = ability value at the steep change of the curve, affected by \(\alpha_i\)
- **Only when the discrimination is low, the phenomenon of "β being pulled away" will occur**
- Therefore, the understanding of β in 2PL must be combined with α to be accurate, and **cannot be interpreted alone**

> **Tip:** The low-discrimination points in Figure 4.4 are exactly those items whose β is "estimated further" in 2PL

### 2.6.5 Comparison of ability estimates

![Figure 4.5: Regression relationship between two-parameter logistic ability and Rasch model ability](../assets/images/ch4_fig4.5.png)

Figure 4.5 shows the regression relationship between 2PL trait level and Rasch model trait level.

**Discovery:**

- High correlation (R² = .98)
- But the 2PL estimates are somewhat dispersed around the Rasch model estimates
- The importance of this dispersion depends on the purpose of the measurement

**Actual Impact:**

A high correlation (.98) means:
- The ability ranking of the two models is basically the same
- But the specific values are different
- If you only care about sorting (such as selection), the difference is not big
- Caution is required if precise scores are required (e.g. for diagnosis)

### 2.6.6 Select suggestions

Practical advice

The relative value of the various criteria determines which model is best suited for a specific application:

- If the main concern is to fit existing data → 2PL model
- If item parameters are required to be very accurate → 2PL model
- If items are equally important or require a highly rationalized measurement scale → Rasch model
- If there is a significant guessing effect → 3PL model

No single criterion can be recommended as adequate. It may be possible to fit the Raschmodel to the data by removing a few extremely discriminative items.

**Example:**

1. Is it a multiple choice question?
2. Yes → Consider 3PL
3. No → 2PL or Rasch
4. Is equating (comparison across years) required?
5. Yes → Rasch inclined
6. No → 2PL may be better
7. Is the sample size large?
8. Less than 500 → Rasch is more stable
9. Greater than 1000 → You can try complex models
