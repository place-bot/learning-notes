# 4. Other one-dimensional models

Although a complete description of all models is beyond the scope of this chapter, several important extended models should be mentioned.

## 4.1 Linear logistic latent trait model (LLTM)

### 4.1.1 Model motivation

LLTM (Fischer, 1973) aims to incorporate item content into the prediction of item success.

**Core idea:** If we know what factors cause item difficulty, can we directly model these factors?

**Actual example:**

The difficulty of an item may be determined by the following factors:
- Count steps
- Whether carry is required
- Whether fractions are involved
- Is there a text description?

LLTM attempts to quantify the contribution of each factor!

### 4.1.2 Expression

LLTM decomposes item difficulty into interpretable components:

\[
\beta_i = \sum_k \tau_k q_{ik} + q_0
\]

Complete model:

\[
P(X_{is} = 1|\theta_s,\tau) = \frac{\exp(\theta_s - (\sum_k \tau_k q_{ik} + q_0))}{1 + \exp(\theta_s - (\sum_k \tau_k q_{ik} + q_0))} \tag{4.13}
\]

Among them:

- \(q_{ik}\) = value of stimulus k in item i
- \(\tau_k\) = the weight of stimulus factor k in item difficulty
- \(q_0\) = normalization constant

### 4.1.3 Application examples

**Difficulty breakdown of paragraph understanding items:**

Assume that item is affected by five factors:

1. Vocabulary level
2. Syntactic complexity
3. Density of proposition type 1
4. Density of proposition type 2
5. Density of proposition type 3

If the involvement of each factor can be quantified numerically, LLTM can estimate the weight of each factor.

**Example Design Matrix:**

|item|Vocabulary|syntax|Proposition 1|Proposition 2|Proposition 3|
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1 | 3 | 0 | 1 |
| 2 | 3 | 2 | 1 | 2 | 0 |
| 3 | 1 | 3 | 2 | 1 | 2 |

It is estimated that the result may display:

- \(\tau_1 = 0.3\) (lexical weight)
- \(\tau_2 = 0.4\) (syntactic weight)
- Wait...

**Actual meaning:**

If the weight for syntactic complexity is 0.4, it means:

- Each unit increase in syntactic complexity
- item difficulty increased by 0.4 logit units
- Can predict the difficulty of new items!

### 4.1.4 Special Application: Change Measurement

A special case of LLTM is the measurement of changes between conditions. If the item is presented after a condition that changes the average trait level, add a constant to reflect the effect of the condition.

**Example:**

Testing the effects of drugs on cognition:

- item difficulty before taking medicine = β
- item difficulty after taking medicine = β + τ
- τ represents drug effect

## 4.2 Models that combine speed and accuracy

### 4.2.1 Real needs

In many tests, performance levels depend on both accuracy and speed:

- Timed cognitive test
- response time tasks
- Efficiency assessment

**Actual scene:**

On standardized tests:

- Some students are accurate but slow
- Some students are quick but careless
- The ideal state is fast and accurate

### 4.2.2 Modeling method

Several ways to incorporate response time into successful predictions:

1. **Directly incorporated into the model**: The correct response probability partly depends on the response time
2. **Joint Modeling**: Modeling accuracy and speed simultaneously
3. **Conditional Model**: Modeling accuracy under given speed conditions

Roskam (1997) and Verhelst et al. (1997) proposed various models. For some variants, only the average or total response time is required.

**Application example:**

Online quizzing systems can:

- Record the time taken for each question
- Discover rushed responses (too fast may be random guessing)
- Adjust ability estimate

## 4.3 Multiple attempts for a single item

### 4.3.1 Applicable situations

When the same task is repeated multiple times:

- Psychomotor tasks (e.g. shooting)
- Behavioral observations (e.g. social responses)
- Skill practice

**Specific example:**

- Basketball free throws: 10 opportunities, how many were scored?
- Typing test: How many mistakes did you make in 5 minutes?
- Child behavior: How many times a day do you have tantrums?

### 4.3.2 Model type

Masters (1992) and Spray (1997) proposed appropriate models:

1. **Binomial distribution model**: Assume that each attempt is independent and has constant probability
2. **Poisson model**: suitable for rare events
3. **Inverse Binomial Distribution Model**: Allowing for overdispersion

**Application Example:** Safrit et al. (1989) describe an application to motor behavior.

**Selection Principle:**

- Fixed degree → binomial distribution
- Number of times in a fixed time → Poisson distribution
- There is intra-individual variation → inverse binomial distribution

## 4.4 ICC special form model

### 4.4.1 Non-monotone ICC

In some cases, item response probability is not monotonically increasing.

**Attitude Data Example:**

Statement: "I think the death penalty is necessary, but I wish it wasn't"

- Extreme opponents: Disagree (think unnecessary)
- Moderate attitude: Agree (ambivalence)
- Extreme supporters: Disagree (think it is necessary and should)

**Graphic Features:**

Not an S-shaped curve, but an inverted U-shaped curve! People in the middle are most likely to agree.

### 4.4.2 Applicable models

1. **Hyperbolic Cosine IRT Model** (Andrich, 1997)
2. **Parallelogram IRT model** (Hoijtink, 1991)

These models allow the ICC to reach a maximum value at a certain point and then decrease.

**Example of form:**

The hyperbolic cosine model uses:

\[
P(\theta) = \frac{\cosh(\alpha(\theta - \beta))}{\gamma + \cosh(\alpha(\theta - \beta))}
\]

## 4.5 Non-parametric IRT model

### 4.5.1 Why are non-parametric methods needed?

Assuming that ICC has a single functional form may be too restrictive. Some data may require more complex functions.

**Analogy:**

The parametric model is like using a ruler to draw lines, while the non-parametric model is like using a curved board, which can draw any shape.

### 4.5.2 Ramsey’s method

Ramsey’s (1991) non-parametric IRT method:

- Apply kernel smoothing technology to each item
- does not assume a specific functional form
- Flexible fitting of various ICC shapes

**Advantages:**

- Can spot unexpected patterns
- Not restricted by functional form
- Suitable for exploratory analysis

**Disadvantages:**

- Requires large sample size
- hard to explain
- Difficult to promote

### 4.5.3 Possible ICC forms

![Figure 4.7: Comparison between non-parametric item characteristic curve and three-parameter normal ogive model](../assets/images/ch4_fig4.7.png)

Figure 4.7 shows three ICCs fitted using non-parametric methods:

1. **Non-zero asymptote**: similar to 3PL
2. **Local flatness**: The probability changes very little within certain capability ranges
3. **Non-monotone**: The probability decreases in some areas

**Trade-off:** Greater flexibility comes at the cost of model complexity. Each item may require different functions.

**Usage suggestions:**

- Use parametric model first
- If fit is not good, try non-parametric
- Use non-parametric results to guide the improvement of parametric models
