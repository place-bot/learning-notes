# 5. Concept Supplement 11: In-depth analysis of the principle of specific objectivity

An important feature of the Rasch model is that it satisfies the "specific objectivity" principle. This concept is worth understanding in depth.

## 5.1 Basic concept of specific objectivity

Definition of specific objectivity

**Basic idea:** Comparisons between objects must be generalizable beyond the specific conditions under which they are observed

**Specific meaning:** Measurement results should not depend on the specific conditions of measurement, including specific items or specific participant groups.

## 5.2 Detailed derivation of two invariant comparisons

### 5.2.1 Invariance of personnel comparisons

**Question:** Is the ability comparison of two people affected by item selection?

**Proof in Rasch model:**

For any two people \(p\) and \(q\), on any item \(i\):

\(\ln\left(\frac{P_{pi}/(1-P_{pi})}{P_{qi}/(1-P_{qi})}\right) = \ln\left(\frac{P_{pi}}{1-P_{pi}}\right) - \ln\left(\frac{P_{qi}}{1-P_{qi}}\right)\)

\(= (\theta_p - \beta_i) - (\theta_q - \beta_i) = \theta_p - \theta_q\)

This result has nothing to do with item difficulty\(\beta_i\)!

### 5.2.2 Invariance of item comparison

**Question:** Is the difficulty comparison of two items affected by participant selection?

**Proof in Rasch model:**

For any two items\(i\) and \(j\), on any participant\(p\):

\(\ln\left(\frac{P_{pi}/(1-P_{pi})}{P_{pj}/(1-P_{pj})}\right) = (\theta_p - \beta_i) - (\theta_p - \beta_j) = \beta_j - \beta_i\)

This result has nothing to do with participant ability \(\theta_p\)!

## 5.3 The actual meaning of specific objectivity

Value in practical applications

**Adaptability test:** Different participants can accept different items, but the ability comparison is still valid

**item bank:** Item parameters can be calibrated with different participant groups

**Longitudinal study:** Different items can be used at different time points to track changes in abilities.
