# 3. Grade response model (GRM)

## 3.1 Basic information

- Developer: Samejima, 1969; 1996
- Applicable: item responses can be characterized as ordered category responses (such as Likert scale)
- Nature: It is a generalization of the 2PL model in Chapter 4 and belongs to the "difference model" category
- Type: "Indirect" IRT model (requires a two-step process to calculate response probability)

## 3.2 Model advantages

- Items in the test do not have to have the same number of response categories
- item parameters estimation is not complicated by different response formats
- (This is different from the later evaluation scale model)

## 3.3 Parameter description

For each scaleitem(i), we need to estimate:

- **An item slope parameter** (\(\alpha_i\))
- \(j\) = 1... \(m_i\) category "threshold" parameters (\(\beta_{ij}\))
- Among them: \(m_i + 1 = K_i\) = the number of response categories in item

## 3.4 Examples

Consider an item with K = 5 response options and subject scores x = 0...4:

- There are 5 reaction options
- So there are \(m_i = 4\) thresholds (j = 1...4) between reaction options

**Specific example:**

Question: Do I like going to loud frat parties?

```text
Hate them Not really Love them a bit Yes Definitely Love them
    0        1        2       3      4
    |        |        |       |      |
  Threshold 1 Threshold 2 Threshold 3 Threshold 4
```

## 3.5 Two calculation stages of GRM

### 3.5.1 Phase 1: Calculation of Operating Characteristic Curve (ICC)

GRM uses a two-step method to calculate category response probability. First calculate the **operating characteristic curve**.

\[
P^*_x(\theta) = \frac{\exp[\alpha_i(\theta - \beta_{ij})]}{1 + \exp[\alpha_i(\theta - \beta_{ij})]} \tag{5.1}
\]

Among them \(x = j = 1, ..., m_i\)

The meaning of operating characteristic curve

\(P^*_x(\theta)\) represents the probability that the examinee's original item response (x) falls at or above the given category threshold (j), conditional on the trait level (\(\theta\)).

This is essentially the 2PL function from Chapter 4, which computes a curve for each threshold.

**Parameter explanation:**

For 5 categories of items:

- 4 \(\beta_{ij}\) parameters need to be estimated (thresholds)
- Need to estimate 1 public slope \(\alpha_i\) parameter

The meaning of \(\beta_{ij}\) parameters

\(\beta_{ij}\) represents the necessary trait level such that the probability at this threshold j is 0.50.

GRM treats item as a series of \(m_i = K-1\) binary choices:

- 0 vs. 1,2,3,4
- 0,1 vs. 2,3,4
- 0,1,2 vs. 3,4
- 0,1,2,3 vs. 4

### 3.5.2 Phase 2: Calculate the actual category response probability

The actual class probability is calculated from the difference between adjacent operating characteristic curves:

\[
P_x(\theta) = P^*_x(\theta) - P^*_{x+1}(\theta) \tag{5.2}
\]

**Boundary conditions:**

- \(P^*_0(\theta) = 1.0\) (probability of responding in the lowest category or above)
- \(P^*_5(\theta) = 0.0\) (probability of response higher than highest category)

Specific calculation of 5 category items

For items in 5 categories (0-4):

\[P_0(\theta) = 1.0 - P^*_1(\theta)\]

\[P_1(\theta) = P^*_1(\theta) - P^*_2(\theta)\]

\[P_2(\theta) = P^*_2(\theta) - P^*_3(\theta)\]

\[P_3(\theta) = P^*_3(\theta) - P^*_4(\theta)\]

\[P_4(\theta) = P^*_4(\theta) - 0\]

Note: For any fixed \(\theta\) value, the sum of all response probabilities is equal to 1.0

## 3.6 Graphical example of GRM

### 3.6.1 Example of operating characteristic curve

Consider a five-category item with the following parameter settings:

- \(\alpha_i = 1.5\)
- \(\beta_{i1} = -1.5\), \(\beta_{i2} = -0.5\), \(\beta_{i3} = 0.5\), \(\beta_{i4} = 1.5\)

![Figure 5.1: GRM operating characteristic curve](../assets/images/ch5_fig5.1.png)

Figure 5.1 shows four operating characteristic curves \(P^*_x(\theta)\), each curve representing the probability of responding at or above that threshold.

### 3.6.2 Category response curve

![Figure 5.2: Category response curve of GRM](../assets/images/ch5_fig5.2.png)

Figure 5.2 shows the corresponding category response curves, representing the probability of responding in each category (x = 0...4).

## 3.7 The role of item parameters in GRM

Effect of slope parameter \(\alpha_i\)

- **Higher values**: The steeper the operating characteristic curve and the higher the peak of the class response curve
- **Meaning**: Response categories are well differentiated between trait levels
- **Analogy**: Like adjusting the focus of a camera lens

Impact of threshold parameter \(\beta_{ij}\)

- Determine the position of the operating characteristic curve
- Determine the peak position of the category response curve for each intermediate response option
- **Important rule**: The peak of the class response curve occurs at the midpoint of two adjacent threshold parameters

## 3.8 GRM parameter estimation of NEO-FFI neurotic item

### 3.8.1 Table 5.3: Estimated item parameters

The parameter results estimated using the MULTILOG (Thissen, 1991) program are as follows:

|item| \(a_i\) (SE) | \(\beta_{i1}\) (SE) | \(\beta_{i2}\) (SE) | \(\beta_{i3}\) (SE) | \(\beta_{i4}\) (SE) |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.70 (0.13) | -3.80 (0.84) | -1.93 (0.43) | -0.87 (0.28) | 1.88 (0.39) |
| 2 | 1.42 (0.15) | -2.07 (0.25) | -0.22 (0.12) | 0.93 (0.15) | 2.42 (0.26) |
| 3 | 1.93 (0.18) | -2.37 (0.28) | -0.92 (0.14) | -0.39 (0.13) | 1.34 (0.17) |
| 4 | 1.31 (0.15) | -2.72 (0.36) | -0.81 (0.15) | 0.04 (0.13) | 1.85 (0.24) |
| 5 | 1.14 (0.14) | -3.14 (0.42) | -0.60 (0.16) | 0.64 (0.15) | 2.72 (0.39) |
| 6 | 1.84 (0.19) | -1.15 (0.14) | -0.15 (0.10) | 0.37 (0.10) | 1.60 (0.18) |
| 7 | 1.06 (0.13) | -3.75 (0.57) | -0.99 (0.20) | 0.11 (0.16) | 2.47 (0.37) |
| 8 | 0.65 (0.12) | -4.43 (0.90) | -1.08 (0.31) | 0.75 (0.28) | 3.96 (0.79) |
| 9 | 2.09 (0.20) | -1.93 (0.18) | -0.20 (0.09) | 0.42 (0.09) | 1.70 (0.17) |
| 10 | 1.18 (0.14) | -2.81 (0.39) | -0.64 (0.16) | 0.37 (0.15) | 2.24 (0.32) |
| 11 | 1.69 (0.18) | -1.46 (0.17) | 0.08 (0.10) | 0.81 (0.12) | 2.13 (0.23) |
| 12 | 1.15 (0.14) | -2.52 (0.35) | -0.76 (0.16) | -0.04 (0.14) | 1.71 (0.24) |

Note:

- Response categories: 0 = Strongly Disagree; 1 = Disagree; 2 = Neutral; 3 = Agree; 4 = Strongly Agree.
- \(a_i\): The **discrimination parameter** (discrimination) of item \(i\) reflects the sensitivity of the item to latent ability.
- \(\beta_{ij}\): The **\(j\)th threshold parameter** (threshold) of item \(i\) indicates the ability level required by the respondent when transitioning from category \(j-1\) to category \(j\).
- The parameters in this table are based on GRM (Grade Response Model) estimation and are suitable for ordered multi-category items.

### 3.8.2 Important Observations

**1. Threshold parameter distribution: **

The inter-category threshold parameters are fairly evenly distributed across the idiosyncratic range.

ordering constraints

Within each item, the threshold parameters between categories must be ordered:

\[\beta_{i1} < \beta_{i2} < \beta_{i3} < \beta_{i4}\]

This is an inherent requirement of the GRM model.

**2. Estimation problem:**

The first and last category threshold parameters of some items are poorly estimated (such as items 1 and 8).

Extreme category estimation problem

**Reason**: Few subjects choose the extreme options of these items, and these items are not strongly related to the latent trait.

**Solution**: It may be necessary to combine extreme categories or collect more data.

**3. Difference in slope parameters:**

- **Maximum Slope**: item9 ("Feeling frustrated and want to give up") and item6 ("Sometimes feeling worthless")
- **Minimum Slope**: item8 ("angry about the way I was treated") and item1 ("not a worrier")

### 3.8.3 Relationship between slope parameter and discrimination

Important reminder

In multinomial IRT models, slope parameter values should not be interpreted directly as item discrimination.

**Why does slope parameter ≠ discrimination? **

In a multinomial model, discrimination depends on a combination of two factors:

1. **Slope parameter \(\alpha_i\)**: Affects the "steepness" of the response curves of all categories
2. **Distribution range of threshold parameters**: Distribution range of \(\beta_1, \beta_2, \beta_3, \beta_4\)

Specific examples

Consider two items:

**itemA**: \(\alpha = 2.0\), threshold: -0.1, 0.0, 0.1, 0.2 (threshold intensive)

**itemB**: \(\alpha = 1.0\), threshold: -2.0, -1.0, 1.0, 2.0 (threshold dispersion)

result:

- Although itemA has a large slope, it only provides good discrimination near \(\theta \approx 0\)
- Although itemB has a small slope, it has good discrimination within the wider \(\theta\) range.

To directly evaluate the discrimination provided by an item, it is necessary to calculate **item information curves (IICs)** (see Chapter 7 for details).

## 3.9 GRM model fit evaluation

### 3.9.1 Fitting test function of MULTILOG

The program provides for each item:

- **Proportion of responses observed** in each category
- **Model predicted value** (calculated from item parameters and estimated latent trait distribution)

### 3.9.2 Fitting result of this example

The estimated model parameters performed well in predicting the observed response proportions:

- **No residuals greater than 0.01**
- Most residuals are zero

Important reminder

1. **out-of-sample prediction**: Residual values are expected to increase when the model is applied to new subject samples that were not included in the calibration.
2. **Complexity of fit evaluation**: In IRT, a single fit index is rarely satisfactory in the complex problem of judging model fit. In practice a variety of methods should be used (see Chapter 9 for details).
