# 1. The meaning of trait level: the fundamental difference between CTT vs IRT

## 1.1 The nature of measurement: the art of comparison

To understand any measurement, we first need to understand a basic truth: **Measurement is comparison**.

Measurement analogies in everyday life

When we say "Xiao Ming is 1.75 meters tall", we are actually saying:

- **Comparison:** Xiao Ming’s height vs standard meter stick
- **Comparison result:** Xiao Ming’s height is 1.75 times the length of a standard meter stick
- **Comparative Property:** This is a ratio relationship (1.75:1)

## 1.2 Comparative Challenges in Psychometrics

But psychometrics faces a difficulty: we measure psychological traits that are invisible and intangible.

Confusion about psychometrics

- There is no "standard meter" for traits such as intelligence, anxiety, and extroversion.
- We cannot directly measure a person's "intelligence length"
- So, what should we use as a comparison standard?

## 1.3 CTT’s solution: human standard

Classical Test Theory (CTT) opts for a seemingly natural solution: **use others as a standard of comparison**.

### 1.3.1 CTT comparison logic

The core idea of CTT

**Comparison standard:** Score distribution of others (norm group)

**Comparative property:** Ordinal relationship (ranking)

**Explanation method:** "How many people are you higher than and how many people are you lower than?"

### 1.3.2 Specific examples of CTT explanation

Let us understand how CTT is explained through an example of energy awakening scale:

**Table 2.1: Item difficulty of energy awakening scale**

|variable|\(p\)-value| Logit \(\beta_i\) |Odds \(e_i\)|
| --- | --- | --- | --- |
|**Energy Awakening**|  |  |  |
|active| 0.36 | 1.84 | 6.30 |
|energetic| 0.48 | 0.90 | 2.45 |
|High energy| 0.69 | -0.74 | 0.48 |
|Lively| 0.52 | 0.61 | 1.84 |
|full of energy| 0.63 | -0.22 | 0.80 |
|Drowsy (-)| 0.73 | -1.02 | 0.36 |
|Tired (-)| 0.76 | -1.34 | 0.26 |
|sleepy (-)| 0.71 | -0.94 | 0.39 |
|wake up| 0.53 | 0.50 | 1.65 |
|alert| 0.55 | 0.40 | 1.49 |

> Note: \((-)\) represents the reverse-scored item; \(p\)-value represents the proportion of subjects who agree with the item

![Figure 2.1: Energy arousal scores converted to standard scores](../assets/images/ch6_fig6.1.png) in three norm groups

Figure 2.1 shows that the same raw score number has completely different meanings in three different groups.

### 1.3.3 Concept Supplement 1: The Power and Traps of the Normal Group

The norm group is the core concept of CTT, but it is also its biggest weakness. Let’s understand this concept in depth:

In-depth analysis of norm group

**What is the norm group? **

The norm group is a group of people used to make comparisons. Just like your opponents in a race, your performance depends entirely on who you compete with.

**How does the choice of norm group affect the result? **

The same raw score number has completely different meanings in different norm groups. This is not a technical problem, but a fundamental feature of CTT.

### 1.3.4 Surprising differences between different norm groups

Let’s understand this difference in concrete numbers:

Same score, different meaning

Assume that Xiao Li scored 6 points on the energy awakening scale:

**Among younger adults:** T-score = 45 (below average)

**In the elderly population:** T-score = 55 (above average)

**In the manic population:** T-score = 35 (very low)

The same 6 points has completely different meanings in different groups!

This example reveals a fundamental problem with CTT: the meaning of the scores depends entirely on the comparison group we choose. It's like saying whether a person's height is "tall" or "short" depends entirely on whether he is on the basketball team or the gymnastics team.

### 1.3.5 The profound impact of linear transformation vs nonlinear transformation

Key differences between conversion types

**Linear transformation (normal distribution norm group):**

When the scores of the norm group are in a normal distribution, the conversion from the raw score number to the standard score is linear. This means that equal differences in raw scores correspond to equal differences in standard scores.

**Nonlinear transformation (skewed distribution norm group):**

When the scores of the norm group are distributed in a skewed manner, standardization is required. This changes the relative distance between fractions, turning an equal difference into an unequal difference.

### 1.3.6 Fundamental characteristics of CTT explanation

Through this example, we can summarize the core features of CTT explanation:

Fundamental Limitations of CTT

**Relativity:** The meaning of the score depends entirely on the reference group

**Instability:** If you change the group, the meaning of the score changes.

**Ordinality:** We can only know the high and low, but we cannot know "how much higher"

## 1.4 IRT’s revolutionary solution: using item as the standard

Item Response Theory proposes a revolutionary idea: **use item as a comparison standard**.

### 1.4.1 Comparison logic of IRT

Core Innovations of IRT

**Comparison standard:** Difficulty of item

**Comparative properties:** Difference relationship (ability-difficulty)

**Explanation method:** "What kind of items can you get right?"

### 1.4.2 The revolutionary concept of common scale of people and items

This is the most important innovation of IRT: putting people and items on the same continuous scale.

![Figure 2.2: Person-item comparison](../assets/images/ch6_fig6.2.png)

Figure 2.2 shows the revolutionary person-item co-scale concept. In this figure, we see that 10 items and 4 people are positioned on the same continuum.

### 1.4.3 Concept Supplement 2: In-depth understanding of the common scale of people and items

The breakthrough significance of common scale

**Limitations of traditional thinking:**

In traditional thinking, people are people and items are items, and the two belong to different worlds. People have different levels of ability, and items have different levels of difficulty, but the two cannot be directly compared.

**Breakthrough in IRT:**

IRT puts human ability and item difficulty on the same scale, making direct comparison possible. Just like expressing both the thermometer and the object to be measured in degrees Celsius.

### 1.4.4 The direct meaning of trait level

On this common scale, trait levels have direct meaning:

The core meaning of IRT trait levels

**When \(\theta = \beta\):** Success probability = 0.5

**When \(\theta > \beta\):** Success probability > 0.5

**When \(\theta < \beta\):** Success probability < 0.5

Expressed by the formula (Rasch model):

\[P(X_{ij} = 1|\theta_j, \beta_i) = \frac{\exp(\theta_j - \beta_i)}{1 + \exp(\theta_j - \beta_i)}\]

### 1.4.5 Specific explanation examples

Let us understand through the example in Figure 2.2:

Trait Level Explanation of Person 4

**Person 4 Trait Level:** \(\theta = 0.90\)

**Corresponding item:** "Energetic" (\(\beta = 0.90\))

**Specific meaning:** The probability of person 4 agreeing with "energetic" is 50%

**Easier item:** The probability of person 4 agreeing with "not sleepy" (\(\beta = -0.94\)) is 87%

This mode of interpretation provides a wealth of substantive implications. Not only do we know that person 4 scores higher on energy arousal than person 2, we also know that person 4's trait level corresponds to the specific item content of "energetic."

### 1.4.6 Psychophysical Analogy

To better understand this explanation, we can borrow concepts from psychophysics:

Listening test analogy

**Traditional Hearing Test:**

- Play sounds with different volumes
- Find the volume at which the participant has a 50% chance of hearing it
- This is the hearing threshold

**IRT Trait Measurement:**

- Present items of different difficulty
- Find the item that the participant has a 50% probability of answering correctly
- This is the ability threshold

Just like we can describe a person's hearing sensitivity by the minimum sound intensity that a person can detect, we can also describe a person's level of a certain psychological trait by the items that a person has a 50% probability of identifying with.

### 1.4.7 Concept Supplement 3: In-depth understanding of threshold concept

The concept of threshold is key to understanding IRT, let’s dig into it:

Multiple meanings of threshold concept

**Thresholds in Physics:**

In physics, a threshold is a critical point. For example, the boiling point of water is 100 degrees Celsius, which is a clear threshold.

**Thresholds in Psychology:**

In psychology, threshold usually refers to the 50% probability point. This reflects the probabilistic, rather than absolute, nature of psychological phenomena.

**Threshold in IRT:**

In IRT, when a person's ability is equal to item difficulty, the probability of success is 50%. This point is the threshold of the person on the item.

## 1.5 Summary of essential differences between the two methods

Fundamental differences between CTT vs IRT

**CTT (Classical Test Theory):**

- Standard of comparison: Others
- Numerical basics: ordinal numbers (ranking)
- Explanation logic: relative position
- Stability: dependent on the group

**IRT (Item Response Theory):**

- Comparison standard: item
- Numerical basics: difference/ratio
- Explanation logic: absolute ability
- Stability: independent of the group
