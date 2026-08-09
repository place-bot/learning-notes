# 6. partial credit model (PCM)

## 6.1 Development background

**Developed by:** Masters (1982)

**Initial purpose:**

- Analyze test items that require multiple steps
- It is important to give partial credit for each step completed in solving the problem

**Scope of application:**

- Naturally applicable to achievement test items (such as middle school math problems), partially correct answers are possible
- Also great for analyzing attitude or personality scale responses (multi-point scale scoring)

## 6.2 Key differences between PCM and previous models

Model type

- Unlike GRM and M-GRM, PCM is a divide-by-total model
- Also known as "direct" IRT model
- The probability of a response in a particular category is written directly as the ratio of the exponents divided by the sum of the exponents
- No two-step process required like GRM

**Model properties:**

- PCM can be regarded as an extension of the 1PL model in Chapter 4
- Has all the features of the standard Rasch model, such as separability of person and item parameters

## 6.3 Formal expression of PCM

**Assumption:** The score of item \(i\) is \(x\) = 0, ..., \(m_i\), and the item has \(K_i = m_i + 1\) response categories

**Formula 5.6:** In the partial credit model (Partial Credit Model, PCM), the probability of a participant scoring \(x \in \{0, 1, \dots, m_i\}\) on item \(i\) is given by:

\[
P_{ix}(\theta) = \frac{\exp\left(\sum_{j=1}^{x} (\theta - \delta_{ij}) \right)}{\sum_{r=0}^{m_i} \exp\left( \sum_{j=1}^{r} (\theta - \delta_{ij}) \right)} \tag{5.6}
\]

Among them:

- \(\theta\): participant’s latent ability level;
- \(\delta_{ij}\): The \(j\)th **step parameter** of item \(i\), indicating the ability required to jump from score \(j - 1\) to \(j\);
- \(m_i\): The maximum score level of item \(i\).

Since only \(m_i\) free parameters can be estimated for each item in PCM, to ensure that the model is identifiable, the following convention is usually adopted:

\[
\delta_{i0} := 0
\]

In this way, the minimum score \(x = 0\) is:

\[
\sum_{j=1}^{0} (\theta - \delta_{ij}) := 0
\]

That is, the probability numerator is:

\[
\exp(0) = 1
\]

This is a general normalization setting, not a result derived from the model, but to use the response with a score of 0 as the baseline category to simplify the normalization process of the entire distribution. The response probabilities for all other levels are defined relative to this baseline.

## 6.4 Step-by-step explanation of the formula

### 6.4.1 Molecular part

\[\exp\left[\sum_{j=0}^{x}(\theta - \delta_{ij})\right]\]

This means that to reach category x, all steps from step 0 to step x need to be cumulatively completed.

Detailed development

- Category 0: \(\exp[0] = 1\) (does nothing)
- Category 1: \(\exp[(\theta - \delta_{i1})]\) (complete step 1)
- Category 2: \(\exp[(\theta - \delta_{i1}) + (\theta - \delta_{i2})]\) (complete steps 1 and 2)
- Category 3: \(\exp[(\theta - \delta_{i1}) + (\theta - \delta_{i2}) + (\theta - \delta_{i3})]\) (complete steps 1, 2, 3)

### 6.4.2 Denominator part

\[\sum_{r=0}^{m_i}\exp\left[\sum_{j=0}^{r}(\theta - \delta_{ij})\right]\]

This is the sum of the numerators of all possible classes, ensuring that the probabilities sum to 1.

## 6.5 Parameter explanation

Parameter meaning

- **\(\theta\) (theta):** The subject's trait level (e.g. neuroticism)
- **\(\delta_{ij}\):** Category intersection parameter
  - \(\delta_{i1}\): Difficulty of steps from category 0 to category 1
  - \(\delta_{i2}\): Difficulty of steps from Category 1 to Category 2
  - \(\delta_{i3}\): Difficulty of steps from Category 2 to Category 3

Key understanding

1. **Cumulative Properties:** To reach category x, all previous steps must be "passed"
2. **Step Difficulty:** The larger the \(\delta_{ij}\), the more difficult the step is to complete and requires a higher trait level
3. **Meaning of intersection point:** \(\delta_{ij}\) is the point where the response curves of two adjacent categories intersect on the trait scale.
4. **Differences from GRM:**
   - GRM's \(\beta_{ij}\) is the point with threshold probability 0.5
   - PCM's \(\delta_{ij}\) is the intersection of the class response curves

## 6.6 Understanding the concept of steps

Examples of four types of attitude items

An attitude item with four categories of ratings, the options and steps are structured as follows:

```text
Score: 0 1 2 3
        ─────────┬──────────┬──────────┬─────────
Options: Completely Disagree Somewhat Agree Moderately Agree Agree
                  │          │          │
               Step 1 Step 2 Step 3
```

Subjects must complete three steps in order:

1. Decide between Totally Disagree and Somewhat (Step 1)
2. Decide between a little and moderate (Step 2)
3. Decide between Moderation and Consent (Step 3)

## 6.7 PCM parameter estimation on NEO-FFI data

### 6.7.1 Table 5.5: Estimated item parameters and item fitting statistics of PCM estimation

\[
H_0: \text{The model fits well, that is, there is no significant deviation}
\]

|item| δ₁ (SE) | δ₂ (SE) | δ₃ (SE) | δ₄ (SE) | χ² | df | p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | -1.400 (.23) | -0.279 (.19) | -1.017 (.16) | 0.923 (.14) | 38.78 | 10 | 0.000 |
| 2 | -1.763 (.19) | 0.080 (.14) | 0.622 (.15) | 1.830 (.24) | 11.36 | 11 | 0.413 |
| 3 | -1.800 (.23) | 0.167 (.19) | -1.168 (.17) | 1.117 (.15) | 9.36 | 10 | 0.498 |
| 4 | -2.205 (.25) | -0.003 (.16) | -0.507 (.15) | 1.471 (.17) | 8.82 | 11 | 0.639 |
| 5 | -2.519 (.26) | -0.063 (.14) | 0.170 (.14) | 2.055 (.23) | 9.90 | 10 | 0.450 |
| 6 | -0.686 (.16) | 0.431 (.17) | -0.354 (.17) | 1.376 (.19) | 5.74 | 10 | 0.837 |
| 7 | -2.890 (.32) | -0.105 (.15) | -0.383 (.14) | 1.835 (.19) | 13.86 | 10 | 0.179 |
| 8 | -2.143 (.24) | -0.154 (.15) | 0.011 (.14) | 1.907 (.21) | 29.31 | 10 | 0.001 |
| 9 | -2.132 (.21) | 0.505 (.15) | -0.139 (.16) | 1.636 (.20) | 7.53 | 11 | 0.755 |
| 10 | -2.206 (.24) | 0.065 (.15) | -0.134 (.15) | 1.623 (.19) | 13.35 | 10 | 0.204 |
| 11 | -1.281 (.16) | 0.600 (.15) | 0.264 (.17) | 1.823 (.24) | 22.29 | 11 | 0.022 |
| 12 | -1.738 (.21) | 0.203 (.17) | -0.666 (.16) | 1.166 (.16) | 20.02 | 10 | 0.029 |

**Total model fit:**
χ² = 190.38, df = 124, p < 0.001
-2 log likelihood = 11,553.011

> Note: δₖ represents step parameters from category *k-1* to *k*; standard error (SE) is enclosed in parentheses.

**Program used:** PARSCALE (Muraki, 1993)

**Parameter structure:**

Each item has 4 category intersection parameters: \(\delta_1\), \(\delta_2\), \(\delta_3\), \(\delta_4\)

### 6.7.2 Important finding 1: Parameter "reversal" phenomenon

**Comparison with GRM**

**In GRM:** The threshold parameters between categories must be in order

**In PCM:** \(\delta_{ij}\) parameters are not necessarily ordered like GRM

**"Inversion" definition**

When the intersection parameters are not ordered, this phenomenon is called "inversion" (Dodd & Koch, 1987)

**Specific examples**

Look at item 3 ("Feeling like I'm going to collapse under pressure"):

- \(\delta_1 = -1.800\)
- \(\delta_2 = 0.167\)
- \(\delta_3 = -1.168\)
- \(\delta_4 = 1.117\)

The normal sequence should be: \(\delta_1 < \delta_2 < \delta_3 < \delta_4\)

But the actual value is: \(\delta_1 < \delta_3 < \delta_2 < \delta_4\) (reversed)

### 6.7.3 Figure 5.4: Category response curve of item3 (with inversion)

![Figure 5.4: Category response curve of PCMitem3 (with inversion)](../assets/images/ch5_fig5.4.png)

Figure 5.4 shows the category response curve of item3, showing the inversion phenomenon.

**Relative order of intersections:**
Step 1, Step 3, Step 2, Step 4

**actual meaning:**

- From score 0 → 1 (step 1): relatively easy transition
- From score 2→3 (step 3): relatively easy transition
- From score 1→2 (step 2): relatively difficult transition

**result：**

PCM well explains the phenomenon that item 3 category 2 is rarely selected and category 3 is selected relatively frequently (see the frequency distribution in Table 5.1)

### 6.7.4 Figure 5.5: Category response curve of item5 (no inversion)

![Figure 5.5: Class response curve of PCMitem5 (without inversion)](../assets/images/ch5_fig5.5.png)

Figure 5.5 shows the category response curve of item5, showing the normal ordering situation.

**Comparison example:** item5 ("Feeling nervous and anxious")

**Features:**

- Have ordered intersection parameters
- Most subjects responded in categories 1, 2 or 3 (see Table 5.1)
- Each response option has its "most likely trait level area"

### 6.7.5 General rules of reversal

**Important conclusions of Andrich (1988)**

**Ordered intersection:**

- If the category intersection parameters within the item are ordered
- then there is the most likely region for each response option at the latent trait level

**Reverse intersection:**

- if there is an "inversion" of the intersection parameters
- This guarantees that at least one category will never be the most likely choice (conditional on trait level)

### 6.7.6 Graphical Interpretation: Deep Understanding of Reversal Phenomenon

![Figure 5.4: Category response curve of PCMitem3 (with inversion)](../assets/images/ch5_fig5.4.png)

Let’s look at Figure 5.4 again and observe the key features of Figure 5.4

**1. "Disappearance" of Category 2:**

- Look at the curve labeled "2" in the figure, its peak value is very low (about 0.2)
- Category 2 is almost never the most likely choice across the spectrum of trait levels
- This explains why only 43 people chose category 2 of item3 in Table 5.1 (relatively few)

**2. Strange selection mode:**

- Trait levels between -3 and -2: Main selection category 0
- Trait level between -2 and -1: Main choice category 1
- Trait level - between 1 and 1: jump directly to category 3 (skipping category 2!)
- Trait level 1 or above: Main selection category 4

**3. Specific manifestation of reversal:**

Due to \(\delta_3 = -1.168 < \delta_2 = 0.167\), resulting in:

- It is easier to go from category 2 to category 3 than from category 1 to category 2
- People tend to "skip" Category 2

**Observe the normal characteristics of Figure 5.5**

![Figure 5.5: Class response curve of PCMitem5 (without inversion)](../assets/images/ch5_fig5.5.png)

**1. Each category has a "turf": **

- Category 0: highest probability at \(\theta < -2.5\)
- Category 1: Highest probability at \(\theta \approx -1.5\)
- Category 2: The highest probability at \(\theta \approx 0\)
- Category 3: Highest probability at \(\theta \approx 1.5\)
- Category 4: Highest probability at \(\theta > 2.5\)

**2. Smooth transition:**

- As trait levels increase, people transition smoothly from low to high categories
- No categories are "skipped"

**3. Intuitive:**

- People with low neuroticism choose "disagree"
- The level of neuroticism gradually increases, and the choices gradually increase
- This is consistent with our psychological intuition

### 6.7.7 Practical significance

**Implications for test preparation**

**Explanation of reversal phenomenon:**

- There may be a problem with the expression of Category 2
- Subjects may feel there is no clear distinction between Category 2 and Category 3
- Or the description of Category 2 is not attractive enough

**Improvement suggestions:**

- Redesigned category labels
- Or merge similar categories
- Make sure each category has its own unique psychological meaning

**Advantages of the PCM model:**

PCM can detect this problem, while traditional statistical methods may ignore this subtle but important test quality issue.

## 6.8 PCM item fitting statistics

Let’s look at Table 5.5 again, focusing on the item fitting statistics of PCM.

\[
H_0: \text{The model fits well, that is, there is no significant deviation}
\]

|item| δ₁ (SE) | δ₂ (SE) | δ₃ (SE) | δ₄ (SE) | χ² | df | p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | -1.400 (.23) | -0.279 (.19) | -1.017 (.16) | 0.923 (.14) | 38.78 | 10 | 0.000 |
| 2 | -1.763 (.19) | 0.080 (.14) | 0.622 (.15) | 1.830 (.24) | 11.36 | 11 | 0.413 |
| 3 | -1.800 (.23) | 0.167 (.19) | -1.168 (.17) | 1.117 (.15) | 9.36 | 10 | 0.498 |
| 4 | -2.205 (.25) | -0.003 (.16) | -0.507 (.15) | 1.471 (.17) | 8.82 | 11 | 0.639 |
| 5 | -2.519 (.26) | -0.063 (.14) | 0.170 (.14) | 2.055 (.23) | 9.90 | 10 | 0.450 |
| 6 | -0.686 (.16) | 0.431 (.17) | -0.354 (.17) | 1.376 (.19) | 5.74 | 10 | 0.837 |
| 7 | -2.890 (.32) | -0.105 (.15) | -0.383 (.14) | 1.835 (.19) | 13.86 | 10 | 0.179 |
| 8 | -2.143 (.24) | -0.154 (.15) | 0.011 (.14) | 1.907 (.21) | 29.31 | 10 | 0.001 |
| 9 | -2.132 (.21) | 0.505 (.15) | -0.139 (.16) | 1.636 (.20) | 7.53 | 11 | 0.755 |
| 10 | -2.206 (.24) | 0.065 (.15) | -0.134 (.15) | 1.623 (.19) | 13.35 | 10 | 0.204 |
| 11 | -1.281 (.16) | 0.600 (.15) | 0.264 (.17) | 1.823 (.24) | 22.29 | 11 | 0.022 |
| 12 | -1.738 (.21) | 0.203 (.17) | -0.666 (.16) | 1.166 (.16) | 20.02 | 10 | 0.029 |

**Total model fit statistics:**

- χ² = 190.38，df = 124，p < 0.001
- -2 log likelihood = 11,553.011

> Note: δₖ represents the step threshold parameter from category *k–1* to *k*. Standard error (Standard Error) is in parentheses.

### 6.8.1 Table 5.5: Fitting statistics result

**The right column displays:** The likelihood ratio chi-square fitting statistic output by PARSCALE (see Chapter 9 for details)

**result summary:**

- 4 out of 12 items are not well represented by the estimated PCMitem parameters
- p < 0.05 for these items, indicating poor fit

### 6.8.2 Overall fit evaluation

**Additivity between items:**

- Chi-square statistics are additive between items
- Total chi-square value: 190.39 (124 degrees of freedom)
- p value < 0.001, indicating poor overall model fit

**Log-likelihood value:**

- -2 times log-likelihood = 11,553.011
- Although this statistic cannot be used alone to evaluate model fit
- but useful when comparing PCM with the generalized partial credit model in the next section

### 6.8.3 Expected result

**Why is the fit poor? **

Remember what we discovered earlier in our GRM analysis?

- The slope parameters of different items vary greatly (Table 5.3)
- item9: \(\alpha = 2.09\)
- item8: \(\alpha = 0.65\)

**PCM Limitations:**

- PCM assumes that all items have the same slope (all equal to 1.0)
- But actual data shows that item slopes vary greatly
- Therefore PCM cannot fit this data well
