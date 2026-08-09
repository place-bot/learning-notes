# 4. Practical impact of scale level: not just a theoretical issue

## 4.1 Wrong Statistical Inference: Real Cases

The issue of scale level is not only a theoretical discussion, it can lead to practical wrong conclusions.

### 4.1.1 What is Factorial Design?

**Factorial design** is a multivariable experimental design method in which researchers manipulate two or more "independent variables" (factors) and observe their main effect and interaction effect on the "dependent variable". Common structures such as:

- \(2 \times 2\): two factors, two levels each
- \(3 \times 2\): one factor with three levels and the other with two levels

**interaction effect**: refers to the fact that the influence of one factor on the result depends on the level of another factor. For example, whether the effect of a treatment on achievement varies with student ability.

### 4.1.2 Spurious t-test result

Research by Maxwell and Delaney (1985) demonstrated an alarming phenomenon:

shocking discovery

**Experimental design:** Two groups of participants, with the same true ability mean
**CTT analysis result:** The mean values of the observed scores of the two groups are significantly different!
**Cause:** Test difficulty is too high + different ability distributions lead to non-linear compression of scores

### 4.1.3 False interaction effect

More serious consequences occur in factor analysis:

The creation of false interactions

**True situation:** There is no interaction effect (only main effect)
**CTT analysis result:** Significant interaction detected
**Consequences:** Researchers may incorrectly derive a theoretical interaction structure

## 4.2 simulation study: specific display of scale differences

Through a simulation experiment, we can clearly see the misjudgment caused by scale.

### 4.2.1 Experimental design description

3×2 Factorial Design Simulation

- **Ability Factor A:** Three groups (low, medium, high)
  Control group mean: -1.0, 0.0, 1.0
  Treatment group mean: -0.5, 0.5, 1.5
- **Treatment Factor B:** Control vs Treatment
  Effects are both +0.5 (no interaction)

### 4.2.2 Conversion from IRT abilities to CTT scores

Assume that the test item difficulty \(\beta = 1.5\) (moderately difficult), then the IRT ability \(\theta\) is converted into a proportional accuracy rate (through the logistic function):

\[
P = \frac{1}{1 + e^{-(\theta - \beta)}}
\]

This transformation is non-linear and can "compress" the score especially at extremely high or low abilities.

### 4.2.3 Illustration comparison: how the result is distorted

- ![Figure 5.1: IRT trait level vs scale correct non-linear relationship](../assets/images/ch6_fig6.8.png)
- ![Figure 5.2: Comparison of group means under two scales](../assets/images/ch6_fig6.9.png)

**Explanation of Figure 5.2:**

- **Above (IRTscale):** Parallel lines, indicating no interaction, constant processing effect
- **Figure below (CTTscale):** Obvious interaction, misleading researchers into thinking that different ability groups respond differently

The mechanism of false interactions

**Root cause:** The test is too difficult, causing the high-ability group to be in the sensitive area of the logistic curve
**result:** The same effect is "stretched" or "compressed" by the curve into different sizes
**Misleading:** Researchers believe that treatment effects vary from person to person, and then construct a wrong theory

## 4.3 Impact of other statistical methods

### 4.3.1 Instability of correlation coefficient

Distortion of correlation coefficient

The related results of the same set of data at different scales may be different:

- IRT capabilities vs external variables: \(r = 0.45\)
- raw score vs external variable: \(r = 0.62\)
- Standard score vs external variable: \(r = 0.38\)

### 4.3.2 Regression analysis bias

- **Longitudinal Study:** Learning Growth Trend Shapes Can Be Distorted
- **Multiple Regression:** Variables may be in the wrong order of importance
- **Structural Equation Modeling:** Fitting results depend on the measurement level of the score

## 4.4 Score comparison between IRT and CTT

### 4.4.1 High correlation ≠ equal quality

High correlation does not mean good quality

IRT ability is highly correlated with raw score number (often > 0.95)
But this is only sorted close to
It does not mean that the true ability can be accurately measured.

### 4.4.2 Unique advantages of IRT

Four major advantages of the IRT method

- **Test Equivalency:** Different test papers can be compared
- **item bias detection:** Whether the item is unfair to a certain group
- **Adaptive Quiz:** Difficulty dynamically adjusts based on ability
- **standard error modeling:** Different ability levels have different measurement accuracy

## 4.5 Practical advice: when scale level must be considered

### 4.5.1 High-risk research scenarios

Situations where IRT must be used

- Comparison between groups (gender/race/education group)
- Longitudinal intervention studies (developmental/therapeutic)
- Multi-factor design (main effect + interaction analysis)

### 4.5.2 Precautionary Suggestions in Analysis and Interpretation

Practice defense strategies

- Choose a reasonable test difficulty and avoid extreme ranges
- Conversion or comparative analysis using IRT methods
- Check if the interaction comes from scale non-linearity
- Report standard error instead of just average
