# 9. generalized partial credit model (G-PCM)

## 9.1 Development background

**Developer:** Muraki (1992; 1993)

**Core Improvements:**

- is a generalization of PCM
- Allow items within scale to differ in slope parameters
- Solved the limitation that the slopes of all PCM items must be equal

**Estimation procedure:** PARSCALE (Muraki, 1993)

## 9.2 Expression of G-PCM

**Formula 5.8:** Add slope parameter based on PCM

\[
P_x(\theta) = \frac{\exp\left[\sum_{j=0}^{x}\alpha_i(\theta - \delta_{ij})\right]}{\sum_{r=0}^{m_i}\exp\left[\sum_{j=0}^{r}\alpha_i(\theta - \delta_{ij})\right]} \tag{5.8}
\]

Among them: \(\sum_{j=0}^{0}\alpha_i(\theta - \delta_{ij}) = 0\)

## 9.3 Parameter explanation

Category intersection parameter \(\delta_{ij}\)

- Interpretation is the same as PCM
- as the intersection point of two adjacent category response curves
- is the point at which a category response becomes relatively more likely than the previous response

Special explanation of slope parameter \(\alpha_i\)

- **NOTE:** Different from the way it is explained in the dichotomous IRT model!
- In multinomial models, item discrimination depends on the combination of the slope parameter and the distribution range of the class intersection point

## 9.4 The role of slope parameter in G-PCM

**Description by Muraki (1992, p. 162):**
The slope parameter "represents the extent to which the category response changes between items when theta level changes"

**Specific impact:**

- At \(\alpha_i < 1.0\): CRCs become flat relative to PCM
- \(\alpha_i > 1.0\): CRCs become more spiky relative to PCM

## 9.5 Analysis setup instructions

Important note

In the PARSCALE analysis, the 12 NEO-FFI neurotic items each form their own "chunk" (see Chapter 13 for details)

**result：**

- A separate set of category intersection parameters is estimated for each item
- This is different from the previous PCM settings

## 9.6 Parameter estimation of G-PCM on NEO-FFI data

### 9.6.1 Table 5.6: G-PCM estimated item parameters

|item|α (slope)| δ1 | δ2 | δ3 | δ4 | χ² | DF |p-value|
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.261 (.03) | -2.937 (.87) | 0.121 (.74) | -3.857 (.63) | 2.328 (.54) | 36.29 | 13 | 0.001 |
| 2 | 0.877 (.07) | -2.130 (.22) | 0.070 (.16) | 0.755 (.18) | 2.197 (.28) | 8.71 | 13 | 0.795 |
| 3 | 0.797 (.06) | -2.295 (.30) | 0.197 (.24) | -1.462 (.22) | 1.399 (.19) | 9.29 | 14 | 0.813 |
| 4 | 0.735 (.06) | -2.923 (.34) | 0.028 (.22) | -0.703 (.20) | 1.919 (.23) | 3.02 | 13 | 0.998 |
| 5 | 0.683 (.05) | -3.513 (.38) | -0.041 (.20) | 0.182 (.21) | 2.808 (.33) | 9.29 | 12 | 0.678 |
| 6 | 1.073 (.09) | -0.873 (.15) | 0.358 (.16) | -0.226 (.16) | 1.547 (.18) | 8.71 | 11 | 0.650 |
| 7 | 0.583 (.05) | -4.493 (.55) | -0.004 (.26) | -0.732 (.24) | 2.792 (.33) | 16.93 | 11 | 0.109 |
| 8 | 0.345 (.03) | -4.815 (.68) | 0.012 (.42) | -0.362 (.41) | 4.256 (.60) | 11.58 | 14 | 0.640 |
| 9 | 1.499 (.11) | -1.997 (.15) | 0.210 (.10) | 0.103 (.11) | 1.627 (.14) | 4.93 | 11 | 0.934 |
| 10 | 0.631 (.05) | -3.215 (.37) | 0.195 (.24) | -0.292 (.23) | 2.299 (.30) | 15.07 | 13 | 0.302 |
| 11 | 1.059 (.09) | -1.440 (.16) | 0.551 (.15) | 0.397 (.16) | 2.039 (.23) | 22.12 | 11 | 0.023 |
| 12 | 0.565 (.05) | -2.628 (.37) | 0.534 (.30) | -1.241 (.29) | 1.720 (.28) | 9.65 | 13 | 0.723 |

**Total model fit:**

- Total chi-square statistic: 155.64
- Total degrees of freedom: 149
- Overall fitted p-value: 0.338
- -2 log likelihood = 11,384.921

> Note: The brackets in the table are standard errors (Standard Error).

**Parameter structure:**

Each item displays:

- α: slope parameter
- δ₁, δ₂, δ₃, δ₄: four category intersection parameters
- Chi-square fit statistic, degrees of freedom and p-value

### 9.6.2 Important finding 1: Huge variation in slope parameters

**Specific value:**

- item1: α = 0.261 (minimum)
- item8: α = 0.345
- item9: α = 1.499 (maximum)
- item6: α = 1.073

**Variation range:**

From 0.261 to 1.499, the difference is nearly 6 times! This confirms our previous expectations.

### 9.6.3 Important Finding 2: Consistency with GRMresult

**Consistent Interpretation of Slope Ranking**

**Review the previous GRMresult (Table 5.3):**

Slope parameter in GRM:

- item9: α = 2.09 (highest)
- item6: α = 1.84
- item2: α = 1.42
- item1: α = 0.70
- item8: α = 0.65 (lowest)

Slope ordering in GRM (highest to lowest):

item9 > item6 > item2 > ... > item1 > item8

**Now look at the result of G-PCM (Table 5.6):**

Slope parameter in G-PCM:

- item9: α = 1.499 (highest)
- item6: α = 1.073
- item2: α = 0.877
- item1: α = 0.261
- item8: α = 0.345 (lowest)

Slope ordering in G-PCM (from high to low):

item9 > item6 > item2 > ... > item8 > item1

Key findings: The ordering is almost identical!

**Consistency reflected:**

- The item (item9) with the highest slope in GRM is also the highest in G-PCM
- The item (item8) with the lowest slope in GRM is also the lowest in G-PCM
- The relative ordering of the items in the middle is also basically the same.

**Why are the values different but the ordering the same? **

**1. Different modeling frameworks:**

- GRM is an "indirect" model (two-step process)
- G-PCM is a "direct" model (one-step process)
- The expression methods are different, so the parameter values are different.

**2. But it measures the same concept: **

- Both models are measuring "item discrimination"
- Items with high discrimination show high slopes in both models
- Items with low discrimination show low slopes in both models

**Actual meaning:**

- Model verification: Consistent ranking proves that both models are reasonably identifying item characteristics
- Practical value: no matter which model is used, we will reach the same conclusion

### 9.6.4 Graphical example: Effect of different slopes

Choose three typical items for explanation:

![Figure 5.7: Category response curve of G-PCMitem6 (baseline reference)](../assets/images/ch5_fig5.7.png)

Figure 5.7 shows the category response curve for item 6, with a slope estimate of ≈ 1.0, which can be used as a baseline for comparison with other curves.

![Figure 5.8: Class response curve (low slope) of G-PCMitem5](../assets/images/ch5_fig5.8.png)

Figure 5.8 shows the category response curve for item5, which has a relatively low slope value. The curve nicely captures the fact that most responses to this item are concentrated in categories 1 and 3, demonstrating how a low slope produces a flatter curve.

![Figure 5.9: Class response curve (high slope) of G-PCMitem9](../assets/images/ch5_fig5.9.png)

Figure 5.9 shows the category response curve for item9, with a large slope value. Relative to item 5, these curves are more peaky, demonstrating how a high slope can produce a steeper, more differentiated curve.

### 9.6.5 Summary of visual effects of slope parameters

**Low slope (such as item5):**

- Flat curve
- Provides information over a wide theta range
- Relatively low discrimination

**High slope (such as item9):**

- Curve spikes
- Provides strong information over a narrow theta range
- Relatively high degree of discrimination

**Medium slope (such as item6):**

- A balance between the two

## 9.7 Evaluation of fitting statistics of G-PCM

### 9.7.1 Table 5.6: Fitting statistics result

|item|α (slope)| δ1 | δ2 | δ3 | δ4 | χ² | DF |p-value|
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.261 (.03) | -2.937 (.87) | 0.121 (.74) | -3.857 (.63) | 2.328 (.54) | 36.29 | 13 | 0.001 |
| 2 | 0.877 (.07) | -2.130 (.22) | 0.070 (.16) | 0.755 (.18) | 2.197 (.28) | 8.71 | 13 | 0.795 |
| 3 | 0.797 (.06) | -2.295 (.30) | 0.197 (.24) | -1.462 (.22) | 1.399 (.19) | 9.29 | 14 | 0.813 |
| 4 | 0.735 (.06) | -2.923 (.34) | 0.028 (.22) | -0.703 (.20) | 1.919 (.23) | 3.02 | 13 | 0.998 |
| 5 | 0.683 (.05) | -3.513 (.38) | -0.041 (.20) | 0.182 (.21) | 2.808 (.33) | 9.29 | 12 | 0.678 |
| 6 | 1.073 (.09) | -0.873 (.15) | 0.358 (.16) | -0.226 (.16) | 1.547 (.18) | 8.71 | 11 | 0.650 |
| 7 | 0.583 (.05) | -4.493 (.55) | -0.004 (.26) | -0.732 (.24) | 2.792 (.33) | 16.93 | 11 | 0.109 |
| 8 | 0.345 (.03) | -4.815 (.68) | 0.012 (.42) | -0.362 (.41) | 4.256 (.60) | 11.58 | 14 | 0.640 |
| 9 | 1.499 (.11) | -1.997 (.15) | 0.210 (.10) | 0.103 (.11) | 1.627 (.14) | 4.93 | 11 | 0.934 |
| 10 | 0.631 (.05) | -3.215 (.37) | 0.195 (.24) | -0.292 (.23) | 2.299 (.30) | 15.07 | 13 | 0.302 |
| 11 | 1.059 (.09) | -1.440 (.16) | 0.551 (.15) | 0.397 (.16) | 2.039 (.23) | 22.12 | 11 | 0.023 |
| 12 | 0.565 (.05) | -2.628 (.37) | 0.534 (.30) | -1.241 (.29) | 1.720 (.28) | 9.65 | 13 | 0.723 |

**Total model fit:**

- Total chi-square statistic: 155.64
- Total degrees of freedom: 149
- Overall fitted p-value: 0.338
- -2 log likelihood = 11,384.921

> Note: The brackets in the table are standard errors (Standard Error).

**The right column shows:** Chi-square fit statistic output by PARSCALE

**result summary:**

- Only 2 of the 12 items are not well represented by the estimated G-PCMitem parameters
- This is a significant improvement compared to the 4 unfit items of PCM

### 9.7.2 Overall fit evaluation

**Overall fit statistics:**

- Total chi-square value: 155.64 (149 degrees of freedom)
- p = 0.33, indicating that the overall fit is adequate
- This is a non-significant result, indicating that the model fit is good

**Log-likelihood value:**

- -2 times log-likelihood = 11,384.921

### 9.7.3 Model comparison: PCM vs G-PCM

**Statistical comparison:**

- PCM's -2 log likelihood = 11,553.011
- G-PCM's -2 log likelihood = 11,384.921
- Chi-square change = 11,553.011 - 11,384.921 = 168.09
- Degrees of freedom change = 12 (add 1 slope parameter for each item)

**Significance test:**

- Chi-square change = 168.08 (12 degrees of freedom)
- p < 0.001
- This means that G-PCM is a significant improvement over PCM

### 9.7.4 result explanation

**The advantages of G-PCM are verified:**

1. **Better item level fitting**: from 4 unfit items to 2
2. **Better overall fit**: overall p-value improved from <0.001 to 0.33
3. **Statistically significant improvement**: Likelihood ratio test is highly significant

**Why does G-PCM perform better? **

- Allow items to have different slope parameters
- Better reflects the difference in item discrimination in actual data
- There is no unrealistic constraint of PCM "all item slopes are equal"

### 9.7.5 Practical Implications

Model selection recommendations

- When the data shows a large difference in item discrimination, G-PCM should be selected instead of PCM
- The extra parameter (slope) is worthwhile because the fit is significantly improved

Test Development Implications

- Different items of NEO-FFI do have different degrees of discrimination.
- This difference is real and should not be ignored
