# Item Response Theory: Model-based measurement

## 0. Why are better measurement methods needed?

Thinking questions

Suppose you are a teacher with two students:

- Xiao Ming scored 80 points on a simple test paper
- Xiaohong scored 70 points on a difficult test paper

**Question: Who has more ability? **

This seemingly simple question reveals the fundamental flaw of traditional testing theory (CTT). Today, we will learn how Item Response Theory (IRT) solves this problem.

## 1. Understand the nature of measurement

### 1.1 Latent variable problem

core concepts

**Latent Variables**: Psychological traits that are not directly observable but affect observable behavior

**Manifest Variables**: Behavioral performance that can be directly observed and recorded

Let’s use an analogy with medical diagnosis:

|Analog object|Visible information|inferred target|
| --- | --- | --- |
|medical diagnosis|Fever 38.5°C, cough, fatigue|maybe the flu|
|psychometrics|Correct answer to question 1, incorrect answer to question 5, total score 75 points|What is the competency level?|

Key differences

Doctors have thermometers that can accurately measure fever levels, but how do psychologists "measure" invisible abilities?
That's why we need **measurement models**!

### 1.2 Comparison of two measurement models

![Figure 3.1: Two models of the relationship between latent variables and behavior](assets/images/ch3_fig3.1.png)

**Classical Testing Theory (CTT)**:

- Follow total score
- Model: Observed Score = True Score + Error
- Simple but limited

**Item Response Theory (IRT)**:

- Pay attention to the reaction of each item
- Model: P(correct answer) = f(ability, item parameters)
- Complex but more precise

## 2. Three fatal flaws of CTT

The fundamental problem of CTT

1. **Test dependency**: If you change the set of questions, the meaning of the scores will change.
2. **Information waste**: only use total score and ignore the answer mode
3. **Unable to separate parameters**: I don’t know whether the high score is due to strong ability or simple items

### 2.1 Case analysis: Why is CTT not enough?

Consider the following situation:

|student|Answer mode|total score|CTT conclusion|
| --- | --- | --- | --- |
| A |Answer questions 1-4 (easy questions)|4 points|Same ability|
| B |Answer questions 2-5 (including difficult questions)|4 points|Same ability|

Are they really the same?

If question 5 is much more difficult than question 1, does student B’s correct answer to question 5 mean that he is more capable?
CTT cannot answer this question!

## 3. Revolutionary breakthrough of IRT

### 3.1 Rasch model: the simplest IRT model

The core idea of Rasch model

The probability of correct answer depends on:

- **Ability (θ)**: individual’s latent trait level
- **Difficulty (β)**: difficulty parameter of item

When ability = difficulty, probability of correct answer = 50%

#### 3.1.1 Formal expression

**Logarithmic probability form** (intuitive understanding):

\[
\ln\left[\frac{P_{\text{correct}}}{P_{\text{incorrect}}}\right] = \theta - \beta
\]

**Probability form** (actual calculation):

\[
P(\text{correct}) = \frac{e^{(\theta - \beta)}}{1 + e^{(\theta - \beta)}}
\]

memory skills

- θ > β: ability exceeds difficulty → probability of correct answer > 50%
- θ = β: Difficulty of ability matching → Probability of correct answer = 50%
- θ < β: difficulty exceeds ability → probability of correct answer < 50%

### 3.2 item characteristic curve (ICC)

![Figure 3.3: The item characteristic curve](assets/images/ch3_fig3.3.png) of the three items in the Rasch model

Key Features of ICC

1. **S-shaped curve**: steep in the middle and gentle at both ends
2. **Position parameter**: The curve moves left and right to indicate different levels of difficulty.
3. **Parallel Curves**: All ICCs in the Rasch model are parallel (same slope)

### 3.3 Real data example

Let’s look at the data from Rasch’s original study:

![Figure 3.2: Ability test item × score category probability](assets/images/ch3_fig3.2.png)

Data characteristics

1. The probability increases monotonically with the total score.
2. Present an S-shaped growth pattern
3. The item curves do not intersect (maintain difficulty order)

## 4. Revolutionary method of ability estimate

### 4.1 From summation to search

fundamental change

**CTT method:** Depends on total score
total score = \(\sum\) item score
ability estimate = standardized total score

**IRT method:** Probability-based maximum likelihood estimation

For every possible \(\theta\):

- Calculate \(L(\text{observed response pattern} \mid \theta)\)
- Select \(\theta\) that maximizes \(L\) as the ability estimate

### 4.2 Specific calculation examples

Suppose there are 5 questions, the difficulty is (-2, -1, 0, 1, 2), and a student’s answer pattern is (1,1,1,1,0):

Likelihood calculation process

**Step 1**: Choose a candidate θ value (e.g. θ = 0)

**Step 2**: Calculate the probability of correct answer for each question:

|item|Difficulty β|Actual answer|\(P(\text{correct}\mid \theta=0)\)|
| --- | --- | --- | --- |
| 1 | -2 |Correct answer| 0.88 |
| 2 | -1 |Correct answer| 0.73 |
| 3 | 0 |Correct answer| 0.50 |
| 4 | 1 |Correct answer| 0.27 |
| 5 | 2 |Wrong answer| 0.12 |

**Step 3**: Calculate likelihood
L = 0.88 × 0.73 × 0.50 × 0.27 × (1 - 0.12) = 0.076

**Step 4**: Try other values of θ and find the θ that maximizes L

### 4.3 Visualization of search process

![Figure 3.8: Trait-level violence estimate for items with uniform discrimination](assets/images/ch3_fig3.8.png)

Key findings

- The likelihood curve shapes of different answering modes are different
-The peak position is the best ability estimate
- Inconsistent answering patterns (such as answering difficult questions correctly first and then answering easy questions incorrectly) are less likely

## 5. 2PL model - adding differentiation

### 5.1 Why is discrimination parameter needed?

think

Are all items equally valid?

- Some items can well differentiate students with different abilities
- Some items have poor differentiation effect

### 5.2 2PL model formula

\[
P(\text{correct}) = \frac{e^{α(\theta - β)}}{1 + e^{α(\theta - β)}}
\]

Among them:

- α discrimination = parameter (slope)
- The larger α is, the steeper the curve is and the better the discrimination effect is.

![Figure 3.7: Item characteristic curve](assets/images/ch3_fig3.7.png) with different degrees of discrimination

important difference

In the **2PL model**, the total score is no longer sufficient statistic!

Two students with the same total score, if:

- **Student A**: Mainly answered items with low discrimination correctly.
- **Student B**: Mainly answered items with high distinction correctly.

Then: → **Student B will get a higher ability estimate**

**Explanation of reasons**:

In 2PL, the **discrimination parameter (α)** of each question affects the "information content" of the answer.
Highly differentiated questions contribute more to the ability estimate, so
→ Students with the same total score but different problem-solving modes will have different **ability estimates**.

In other words:
The total score cannot capture "which questions were answered correctly", so it is not a sufficient statistic.

## 6. Practical applications of IRT

### 6.1 Test equating problem

IRT solutions

By including item parameters, IRT automatically adjusts for the impact of different test difficulties

![Figure 3.10: Trait level violence estimate for more difficult items](assets/images/ch3_fig3.10.png)

Get 4 questions correct on the hard test → higher ability estimate

Get 4 questions correct on the easy test → lower ability estimate

ability estimate reliability

- **Horizontal axis θ**: Which θ gives the highest probability of the response pattern predicted by the model → is the student’s ability estimate
- **Vertical axis L(θ)**: The height of the maximum likelihood value indicates the "reasonableness" or "internal consistency" of the reaction pattern

**Example comparison**:

- **Pattern 1 (1,1,1,1,0)**: Answer 4 questions correctly on the easy questions, θ ≈ 1, high likelihood value → stable estimation
- **Pattern 4 (1,1,1,0,1)**: Answer 4 questions correctly on more difficult questions, θ ≈ 2.5, the likelihood value is also higher → stronger ability
- **Pattern 2 (1,1,0,1,0)**: alternating right and wrong, inconsistent answers, overall likelihood value is low → ability estimate is unstable and untrustworthy

### 6.2 Adaptability Test (CAT)

IRT makes CAT possible

1. Select the item with the most appropriate difficulty based on the current ability estimate
2. Update ability estimate in real time
3. Stop testing when the accuracy requirements are met.

result: shorter tests, more accurate measurements!

## 7. Summary: IRT vs CTT

IRT’s revolutionary contribution

|Features| CTT | IRT |
| --- | --- | --- |
|**measurement invariance**|❌ Rely on specific tests|✅ Stable across tests|
|**Information Utilization**|❌ Only use total score|✅ Utilize quiz mode|
|**Parameter separation**|❌ Mix it up|✅ Ability and item are independent|
|**Measurement accuracy**|❌ Assuming constant|✅Varies with ability|
|**Adaptability Test**|❌ Not supported|✅Natural support|

core concept

CTT asked: "How many points did you score?"

IRT asks: "Based on your answering pattern and item characteristics, what ability level is most likely to produce this result?"

**This is the essential leap from "scoring" to "measurement"! **

## 8. Think and practice

Thoughts after class

1. Why is IRT said to be a "model-based" measurement?
2. Under what circumstances will two students with the same total score get different ability estimates?
3. If you want to design an adaptive testing system, how can IRT help you?

In-depth study suggestions

- Try manually calculating a simple likelihood function
- Think about what the item characteristic curves tested in different subjects might look like.
- Understand how modern large-scale examinations (such as GRE, TOEFL) apply IRT

The content of this chapter is based on Chapter 3 of Embretson & Reise (2000)
