# 8. Concept Supplement 4: Expected item response (true score curve)

## 8.1 Formula 5.7: Expected score calculation

\[
E(X) = \sum_{x=0}^{m_i} xP_x(\theta) \tag{5.7}
\]

**Meaning:**

- Shows how subjects' expected item responses vary with trait level
- Sometimes called item "true fraction"

## 8.2 Special properties of PCM

**Result for the same slope:**

- Since PCM is a Rasch model, all items have the same slope (1.0)
- These true fraction curves are very similar between items
- The item true score curve is additive between items

## 8.3 Figure 5.6: True score curve of neuroticism scale

![Figure 5.6: True score curve of PCM neuroticism scale](../assets/images/ch5_fig5.6.png)

Figure 5.6 shows a summary of the 12 neuroticism true score curves.

**Display content:**

- A summary of 12 neuroticism true score curves
- How expected raw total score changes with trait level

**Important Observations:**

- Subjects with trait variables close to zero are expected to score approximately 24 raw score points
- Curve showing non-linear relationship between observed scores and trait levels
- Should be contrasted with the CTT perspective which assumes a linear relationship

## 8.4 Measurement Tool Quality Assessment

Examining such true score curves is one way to study the quality of a measurement instrument for assessing the measurement effectiveness of latent trait variables.

## 8.5 Why can the true fraction curves in PCM be directly superimposed?

### 8.5.1 Core reason: same slope

**Basic assumptions of PCM:**

- The slope parameter of all items is equal to 1.0
- This is characteristic of the Rasch model family

**result：**

When the slopes of all items are the same, the true score curves of each item have similar shapes, but their positions on the trait scale are different.

### 8.5.2 Use a simple example to illustrate

Suppose there are 3 items, all with slope = 1.0:

- The true score curve of itemA: the score expectation at \(\theta=-1\) is 2
- The true score curve of itemB: the score expectation at \(\theta=-1\) is 1.5
- The true score curve of itemC: the score expectation at \(\theta=-1\) is 1.8

Total expected score = 2 + 1.5 + 1.8 = 5.3

### 8.5.3 What happens if the slopes are different?

Assume that items have different slopes:

- itemA: slope=2.0 (very steep)
- itemB: slope = 0.5 (very gentle)

**Question:**

- The shapes of curves with different slopes vary greatly
- Contribution patterns are different at different θ levels
- Simple addition does not accurately reflect the overall measurement accuracy

### 8.5.4 Practical significance

**Advantages of the PCM/Rasch model:**

- Since the slopes are the same, the information of each item can be simply "superimposed"
-The total score is the direct accumulation of the contributions of each item
- This is why "the original total score is sufficient statistic"

**Models with different slopes (such as GRM):**

- Each item has different contribution weights at different θ levels.
- Cannot be simply superimposed
- Requires more complex weight combinations
