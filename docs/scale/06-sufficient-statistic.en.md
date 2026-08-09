# 6. Concept Supplement 12: Complete derivation of sufficient statistic

Sufficient statistic is another important feature of the Rasch model. Let us derive this concept completely.

## 6.1 Definition of sufficient statistic

Strict definition of sufficient statistic

The statistic \(T(\mathbf{X})\) is the sufficient statistic of the parameter \(\theta\) if and only if:

\(P(\mathbf{X} = \mathbf{x} | T(\mathbf{X}) = t, \theta) = P(\mathbf{X} = \mathbf{x} | T(\mathbf{X}) = t)\)

That is, after the value of the statistic \(T\) is given, the distribution of the data no longer depends on the parameter \(\theta\).

## 6.2 Sufficient statistic derivation in Rasch model

**Probability mass function of Rasch model:**

\(P(\mathbf{X} = \mathbf{x} | \theta) = \prod_{i=1}^{I} \frac{\exp[x_i(\theta - \beta_i)]}{1 + \exp(\theta - \beta_i)}\)

**Rearranged:**

\(P(\mathbf{X} = \mathbf{x} | \theta) = \frac{\exp[\theta \sum_{i=1}^{I} x_i] \prod_{i=1}^{I} \exp(-x_i \beta_i)}{\prod_{i=1}^{I} [1 + \exp(\theta - \beta_i)]}\)

\(= \frac{\exp[\theta \sum_{i=1}^{I} x_i]}{\prod_{i=1}^{I} [1 + \exp(\theta - \beta_i)]} \prod_{i=1}^{I} \exp(-x_i \beta_i)\)

Notice that this expression only depends on the data via \(\sum_{i=1}^{I} x_i\) (total score).

## 6.3 Calculation of conditional probability

Given the total score\(r = \sum_{i=1}^{I} x_i\), the conditional probability of a specific reaction pattern is:

\(P(\mathbf{X} = \mathbf{x} | \sum_{i=1}^{I} x_i = r) = \frac{P(\mathbf{X} = \mathbf{x})}{P(\sum_{i=1}^{I} x_i = r)}\)

Since the \(\exp(\theta r)\) terms in the numerator and denominator will cancel, the result does not depend on \(\theta\)!

## 6.4 The actual meaning of sufficient statistic

Practical applications of sufficient statistic

**Scenario 1:** Student A answered items 1, 3, and 5 correctly, total score=3

**Scenario 2:** Student B answered items 2, 4, and 6 correctly, total score=3

**Conclusion of the Rasch model:** The ability estimates of the two students are exactly the same!

**Meaning:** As long as the total score is the same, it does not matter which items are answered correctly.

This feature makes the Rasch model very practical, because we can replace complex reaction patterns with simple total scores.
