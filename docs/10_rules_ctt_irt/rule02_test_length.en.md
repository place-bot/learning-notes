# Rule 2: test length and reliability

Rule comparison

| CTT | IRT |
| --- | --- |
|Longer quizzes are more reliable than shorter ones|Shorter quizzes may be more reliable than longer ones|

## 1. CTT: Spearman-Brown formula

### 1.1 Question setting

core issues

If the test length is increased to \(n\) times, what will the new reliability be?

### 1.2 Derivation process

**Set variables**:

- Original test: length \(k\), reliability \(r_{tt}\)
- New tests: length \(nk\), reliability \(r_{nn}\) (to be requested)

**Step 1: Variance change analysis**

Original quiz:

\[\sigma_X^2 = \sigma_T^2 + \sigma_E^2\]

When the length increases by \(n\) times:

- True fraction variance: \(\sigma_{T_n}^2 = n^2\sigma_T^2\) (perfect correlation, linear superposition)
- error variance: \(\sigma_{E_n}^2 = n\sigma_E^2\) (independent error, variance superposition)

**Step 2: New Quiz Variance**

\[\sigma_{X_n}^2 = n^2\sigma_T^2 + n\sigma_E^2 = n(n\sigma_T^2 + \sigma_E^2)\]

**Step 3: New reliability calculation**

\[r_{nn} = \frac{\sigma_{T_n}^2}{\sigma_{X_n}^2} = \frac{n^2\sigma_T^2}{n(n\sigma_T^2 + \sigma_E^2)} = \frac{n\sigma_T^2}{n\sigma_T^2 + \sigma_E^2}\]

**Step 4: Substitute the original reliability**

From \(r_{tt} = \frac{\sigma_T^2}{\sigma_T^2 + \sigma_E^2}\):

- \(\sigma_T^2 = r_{tt}(\sigma_T^2 + \sigma_E^2)\)
- \(\sigma_E^2 = (1-r_{tt})(\sigma_T^2 + \sigma_E^2)\)

Assume \(V = \sigma_T^2 + \sigma_E^2\) and substitute:

\[r_{nn} = \frac{n \cdot r_{tt} \cdot V}{n \cdot r_{tt} \cdot V + (1-r_{tt}) \cdot V} = \frac{nr_{tt}}{nr_{tt} + (1-r_{tt})}\]

Spearman-Brown formula

\[r_{nn} = \frac{nr_{tt}}{1 + (n-1)r_{tt}}\]

**Special circumstances**:

- \(n=2\)：\(r_{22} = \frac{2r_{tt}}{1 + r_{tt}}\)
- \(n=0.5\)：\(r_{0.5} = \frac{0.5r_{tt}}{1 - 0.5r_{tt}}\)

### 1.3 Monotonicity Proof

\[\frac{dr_{nn}}{dn} = \frac{r_{tt}(1-r_{tt})}{[1 + (n-1)r_{tt}]^2} > 0\]

Because \(0 < r_{tt} < 1\), the derivative is always positive and **reliability increases monotonically with the length**.

### 1.4 Numerical Example

Original test reliability \(r_{tt} = 0.6\):

| \(n\) |Calculation process| \(r_{nn}\) |
| --- | --- | --- |
| 2 | \(\frac{2 \times 0.6}{1 + 0.6} = \frac{1.2}{1.6}\) | 0.75 |
| 3 | \(\frac{3 \times 0.6}{1 + 2 \times 0.6} = \frac{1.8}{2.2}\) | 0.82 |
| 0.5 | \(\frac{0.5 \times 0.6}{1 - 0.5 \times 0.6} = \frac{0.3}{0.7}\) | 0.43 |

## 2. IRT: Quality over quantity

### 2.1 Information function perspective

Core Concept: Test Information Function

\[I(\theta) = \sum_{i=1}^n I_i(\theta)\]

Test information = sum of all item information

### 2.2 Fixed test vs adaptive test

**Fixed Quiz Questions**:

For a participant with capability \(\theta\), information for item \(i\):

\[I_i(\theta) = P_i(\theta)[1-P_i(\theta)]\]

When \(P_i(\theta) \approx 1\) (too easy) or \(P_i(\theta) \approx 0\) (too hard), \(I_i(\theta) \approx 0\)

**Advantages of Adaptive Quiz**:

Select the item \(P_i(\theta) \approx 0.5\), each item provides maximum information \(I_i(\theta) = 0.25\)

### 2.3 Numerical comparison

**Scenario**: Participant with ability \(\theta = 1\)

**Test A (30 fixed questions)**:

- 10 simple questions: \(P \approx 0.9\), \(I \approx 0.09 \times 10 = 0.9\)
- 10 medium questions: \(P \approx 0.7\), \(I \approx 0.21 \times 10 = 2.1\)
- 10 difficult questions: \(P \approx 0.3\), \(I \approx 0.21 \times 10 = 2.1\)
- General information: \(I_A = 5.1\)

**Quiz B (20 adaptive questions)**:

- 20 best questions: \(P \approx 0.5\), \(I \approx 0.25 \times 20 = 5.0\)
- General information: \(I_B = 5.0\)

Key findings

The measurement accuracy of 20 adaptive items ≈ 30 fixed items!

\[SE_A = \frac{1}{\sqrt{5.1}} = 0.443\]

\[SE_B = \frac{1}{\sqrt{5.0}} = 0.447\]

### 2.4 Graphic analysis: U-shaped curve of standard error

```text
standard error
  ^
  | Fixed 20 questions
  |    /
  |   /
  | / \ Fixed 30 questions
  | /              \   /---------
  |/                \ /
  |                  X
  | Adaptive 20 questions
  |            ----------------
  | Adaptive 30 questions
  +-------------------------------------> θ
 -3                  0                  3
```

**Explanation of U-shaped curve**:

For a fixed test, the total information function is:

\[I(\theta) = \sum_{i=1}^n I_i(\theta)\]

When all item difficulties are concentrated near \(b = 0\):

\[I(\theta) \approx n \cdot \frac{e^{-\theta^2}}{(1 + e^{-\theta})^2}\]

This peaks at \(\theta = 0\) and drops rapidly towards both ends, resulting in:

\[SE(\theta) = \frac{1}{\sqrt{I(\theta)}}\]

It rises rapidly at both ends to form a U shape.

## 3. Practical significance

Select suggestions

**Use CTT + increase length**:

- Sufficient resources
- Fixed paper and pencil quizzes
- Group testing

**Using IRT + Adaptive Quiz**:

- Computerized tests
- individualized assessment
- Limited time but high accuracy requirements
