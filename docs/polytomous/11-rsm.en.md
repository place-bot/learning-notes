# 11. Rating scale model (RSM)

## 11.1 Definition

Rating Scale Model (RSM) is a polytomous item response model proposed by Andrich (1978a, 1978b) and is a specialized form of partial credit model (Partial Credit Model, PCM). The main features of RSM are: **All items share the same response category structure (ie, the threshold intervals are equal), but each item is allowed to have different position parameters (difficulty shift)**. This model is suitable for test situations where the scoring standards are fixed and a unified scale is used, such as attitude tests, psychological scales, etc.

### 11.1.1 Parameter decomposition

In RSM, the step difficulty of PCM is decomposed into two components:

\[\delta_{ij} = \lambda_i + \delta_j\]

Among them:

- \(\lambda_i\): item’s position on the potential scale
- \(\delta_j\): Category intersection parameter

### 11.1.2 The form of RSM (represented by Dodd (1990)) is:

\[
P_{ix}(\theta) = \frac{\exp\left[\sum_{j=0}^{x}(\theta - \lambda_i - \delta_j)\right]}{\sum_{k=0}^{m} \exp\left[\sum_{j=0}^{k}(\theta - \lambda_i - \delta_j)\right]}
\]

Among them:

- \(P_{ix}(\theta)\): The probability that the subject obtains the \(x\) category score on the \(i\) item
- \(\theta\): Subject’s latent ability
- \(\lambda_i\): Position parameter of the \(i\) item (overall difficulty)
- \(\delta_j\): The \(j\)th category intersection (shared by all items)

### 11.1.3 Alternative Equivalent Forms

\[P_x(\theta) = \frac{\exp[\psi_x + x(\theta - \lambda_i)]}{\sum_{r=0}^{m_i}\exp[\psi_r + r(\theta - \lambda_i)]} \tag{5.10}\]

Among them:

- \(\psi_x = -\sum_{j=0}^{x}\delta_j\)
- \(\psi_0 = \psi_m = 0\)

## 11.2 Important naming instructions

Terminology confusion warning

The term "scale model" can cause confusion for several reasons:

- Multiple versions of RSM exist, with different model structures and assumptions
- Naming and expression methods in different documents are inconsistent
- This section describes the **Andrich (1978) version** of RSM, which is the most commonly used form in actual software implementations

## 11.3 What is assessment scale?

**Definition:**
A rating scale is a scale in which all items use the exact same response options and the same category labels.

Typical rating scale

Please indicate your level of agreement with the following statements:

- 1 = completely disagree
- 2 = Disagree
- 3 = Neutral
- 4 = Agree
- 5 = completely agree

item1: I like to attend parties 1 2 3 4 5

item2: I often feel anxious 1 2 3 4 5

item3: I am organized 1 2 3 4 5

## 11.4 Relationship between RSM and PCM

- RSM can be viewed as a simplified form of PCM (Masters & Wright, 1984)
- Both use score-based model structures
- The key difference is: PCM has an independent category threshold for each item, while RSM shares a unified threshold structure for all items and only adjusts the overall position.

## 11.5 Key Features of RSM

For items with a uniform response format (e.g. all 0–4 points), RSM assumes:

- Each item uses a position parameter \(\lambda_i\) to represent the overall difficulty
- All items share a set of category intersection parameters \(\delta_1, \delta_2, \dots, \delta_m\)
- The category threshold spacing is the same among all items, and the model structure is more compact

This structure is especially suitable for scales that use standardized scoring tables, such as:

- Mental health measurement scale
- Learning motivation or attitude scale
- Likert scale item group

## 11.6 Core differences between RSM and PCM (example)

Suppose we have three items rated 0–4, measuring the same latent trait (such as “neuroticism”).

### In 11.6.1 PCM model:

Each item has its own threshold:

- item1: "I am often anxious"
  \(\delta_{11} = -1.0,\ \delta_{12} = 0.2,\ \delta_{13} = 1.1,\ \delta_{14} = 2.0\)
- item2: "I get nervous easily"
  \(\delta_{21} = -0.5,\ \delta_{22} = 0.8,\ \delta_{23} = 1.5,\ \delta_{24} = 2.3\)
- item3: "I'm worried"
  \(\delta_{31} = -1.2,\ \delta_{32} = -0.1,\ \delta_{33} = 0.9,\ \delta_{34} = 1.8\)

At this time, the category intervals of each item are different, and the model is more flexible but has more parameters.

### In 11.6.2 RSM model:

All items share the same category structure, but allow overall positional differences:

- Public category threshold:
  \(\delta_1 = -1.0,\ \delta_2 = 0.1,\ \delta_3 = 1.0,\ \delta_4 = 2.0\)
- item position parameters:
  \(\lambda_1 = 0.2,\ \lambda_2 = 0.5,\ \lambda_3 = -0.1\)

Then the actual threshold for each item is:
\(\lambda_i + \delta_j\), that is, item characteristics are obtained through overall translation.

Core comparison summary

PCM: The category spacing (step difficulties) of each item is **variable**
RSM: The category spacing of all items is **the same**, only the overall position offset (item difficulty) is allowed

## 11.7 Applicable conditions and restrictions of RSM

**Basic requirements:**

- RSM assumes that the entire item set uses a fixed set of rating points
- If the items within the scale have different formats, RSM is not an appropriate choice

Situations not suitable for using RSM

Examples of mixed formats:

- item1: "How often do you feel anxious?" (1=never to 5=always)
- item2: "What is your age group?" (1=18-25 years old to 4=46 years old and above)
- item3: "Do you agree with this statement?" (1=completely disagree to 4=completely agree)

This is not a rating scale, because the category meaning of each item is different!

## 11.8 Identification constraints that sum to 0

Why is this constraint needed?

Without constraints, parameter estimates would have infinitely many solutions.

Example: If the true class intersection is:

\(\delta_1 = -1\), \(\delta_2 = 0\), \(\delta_3 = 1\), \(\delta_4 = 2\)

We can add the constant C to all parameters and subtract C from all \(\lambda_i\), and the result will be exactly the same!

The "sum to 0" constraint fixes the "zero point" of the parameter, ensuring the uniqueness of the parameter estimate.

## 11.9 Application of RSM on NEO-FFI data

### 11.9.1 Analysis program

**Program used:** RUMM (Sheridan, Andrich, & Luo, 1996)

### 11.9.2 Table 5.7: RSM estimation result

|item|Location (SE)|item fitting| CHI | DF | p |
| --- | --- | --- | --- | --- | --- |
| 1 | -0.44 (0.05) | 7.492 | 9.199 | 1 | 0.031 |
| 2 | 0.30 (0.05) | -1.943 | 2.492 | 1 | 0.648 |
| 3 | -0.39 (0.05) | 1.008 | 4.470 | 1 | 0.329 |
| 4 | -0.16 (0.05) | -0.934 | 0.960 | 1 | 0.913 |
| 5 | 0.08 (0.05) | -2.356 | 5.728 | 1 | 0.200 |
| 6 | 0.27 (0.05) | 1.631 | 28.309 | 1 | 0.000 |
| 7 | -0.14 (0.05) | -0.695 | 6.234 | 1 | 0.160 |
| 8 | 0.21 (0.05) | 3.838 | 20.313 | 1 | 0.000 |
| 9 | 0.15 (0.05) | -3.502 | 7.524 | 1 | 0.087 |
| 10 | 0.00 (0.05) | 0.010 | 1.318 | 1 | 0.855 |
| 11 | 0.47 (0.05) | -1.107 | 11.022 | 1 | 0.000 |
| 12 | -0.17 (0.05) | 3.800 | 1.392 | 1 | 0.841 |

**Note:** RSM public category crossover points are: -1.600, 0.224, -0.184, 1.560.

**Explanation of position parameters (\(\lambda_i\))**

**The first column shows:** RSM position parameters of each item

**Important findings:**
The position parameter represents the "difficulty" of the item, and the ranking corresponds exactly to the item average shown in Table 5.1

**Specific correspondence:**

- item2: small average (1.70) → high position (\(\lambda_2 = 0.30\))
-Meaning: Few subjects score high on this item
- item1: Large average (2.52) → Low position (\(\lambda_1 = -0.44\))
-Meaning: Few subjects scored low on this item

**Common Category Intersection Parameters**

**Bottom of Table 5.7 shows:** Four estimated category intersection (\(\delta_j\)) parameters

- \(\delta_1 = -1.600\)
- \(\delta_2 = 0.224\)
- \(\delta_3 = -0.184\)
- \(\delta_4 = 1.560\)

**Features:**

- These values remain constant across all 12 items
- sums to 0 (program-imposed scale recognition constraint)

### 11.9.3 Effect of positional parameters

![Figure 5.10: Category response curve](../assets/images/ch5_fig5.10.png) of RSItem1

Figure 5.10 shows the category response curve for item1.

![Figure 5.11: Category response curve](../assets/images/ch5_fig5.11.png) of RSMitem2

Figure 5.11 shows the category response curve for item2.

**Key Observations:**

- These CRCs have the same general shape
- But the curve of item2 moves to the right relative to item1

**The role of \(\lambda_i\) parameters:**

- Represents the average difficulty of a specific item relative to the category intersection
- item2's \(\lambda_2 = 0.30\) > item1's \(\lambda_1 = -0.44\)
- So item 2 is more "difficult" (requires higher neuroticism level to get high score)

### 11.9.4 Fit evaluation of RSM

**Fit statistics for the RUMM program:**

-item fitting value
- 1 degree of freedom chi-square value
- Relevant probabilities

**result：**

- About half (5) of the 12 items do not fit the model (p < 0.05)
- This shows that RSM produces a rather poor fit at the item level

Expected poor fit

**Why is the fit not good? **

- G-PCM and GRM analysis show that items have differences in slopes
- NEO-FFIitem may not constitute the rating scale assumed by RSM
- RSM assumes that all items have the same discrimination (slope), but actual data shows that item discrimination varies greatly
