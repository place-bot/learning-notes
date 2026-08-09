# Detailed explanation of Rule 5: Constructing a meaningful scale score

Rule comparison

| CTT | IRT |
| --- | --- |
|Test scores gain meaning by comparing their position to a norm group|Quiz scores gain meaning by comparing their distance to the item|

## 1. The essential issue of the meaning of scores

Score Meaning

**Core Question**: What does a test score actually mean?

**Example**: Student scored 80 points on the exam

- This 80 points itself has no absolute meaning
- Need to explain with reference to standards

**Two ways of explanation**:

1. **Relative explanation**: Where does a score of 80 rank in the class?
2. **Absolute explanation**: What knowledge and skills does a score of 80 indicate that you have mastered it?

## 2. Norm reference explanation (CTT method)

### 2.1 The concept of norm

Norm is the distribution of performance of a specific group on a test

**Norm group type**:

- National norm: represents the level of peers across the country
- Regional norm: represents the level of peers in a certain region
- School norm: represents the level of the same grade in a certain school
- Professional norm: represents the level of students in a certain major

### 2.2 Normal score conversion

**Percentile**:

\[
P_r = \frac{\text{Number of people below this score}}{\text{total number of people}} \times 100\%
\]

**Standard score (Z-score)**:

\[
z = \frac{X - \mu}{\sigma}
\]

**T score**:

\[
T = 50 + 10z = 50 + 10 \times \frac{X - \mu}{\sigma}
\]

### 2.3 Properties of standard scores

Let the number of raw scores be \(X\), the mean \(\mu_X\), and the standard deviation \(\sigma_X\)

Normalized transformation:

\[
Z = \frac{X - \mu_X}{\sigma_X}
\]

Verify the mean:

\[
E[Z] = E\left[\frac{X - \mu_X}{\sigma_X}\right] = \frac{E[X] - \mu_X}{\sigma_X} = \frac{\mu_X - \mu_X}{\sigma_X} = 0
\]

Verify variance:

\[
\text{Var}(Z) = \text{Var}\left(\frac{X - \mu_X}{\sigma_X}\right) = \frac{\text{Var}(X)}{\sigma_X^2} = \frac{\sigma_X^2}{\sigma_X^2} = 1
\]

Therefore \(Z \sim N(0,1)\)

### 2.4 Norm reference explanation of FIMscale

Functional Independence Measure (FIM)

Assess the ability to perform activities of daily living, often used in functional assessment of the elderly

**Position of four participants in the 80-89 year old norm group**:

**Anna**：\(z = -1.5\)

- 1.5 standard deviations below average
- Percentile: \(\Phi(-1.5) \approx 0.07 = 7\%\)
- Explanation: Functional level is significantly lower than that of peers

**Paul**：\(z = 0\)

- average level
- Percentile: \(\Phi(0) = 0.50 = 50\%\)
- Explanation: Functional level is equivalent to peers

**Vera**：\(z = +1.0\)

- 1 standard deviation above average
- Percentile: \(\Phi(1.0) \approx 0.84 = 84\%\)
- Explanation: Functional level is significantly higher than that of peers

**Mary**：\(z = +1.5\)

- 1.5 standard deviations above average
- Percentile: \(\Phi(1.5) \approx 0.93 = 93\%\)
- Explanation: Functional level is much higher than that of peers

### 2.5 Limitations of norm reference

Three major questions

1. **Lack of absolute meaning**: only know the relative position, not the absolute ability
2. **Norm dependence**: Different norm groups have different results.
3. **Unable to guide intervention**: Don’t know where the specific problem is

## 3. item reference explanation (IRT method)

### 3.1 The concept of common scale

The core idea of IRT: people and items are on the same scale

**scale features**:

- Normal range: \(-3\) to \(+3\)
- Numerical meaning: the gap between ability and difficulty
- Probabilistic interpretation: based on logistic function

### 3.2 Success probability calculation

Core formula:

\[
P(\text{success}) = \frac{e^{(\theta - b)}}{1 + e^{(\theta - b)}}
\]

When \(\theta = b\), \(P = 0.5\)

**Probability calculation table**:

| \(\theta - b\) | \(e^{(\theta - b)}\) | \(P\) |
| --- | --- | --- |
| -3 | 0.050 | 0.047 |
| -2 | 0.135 | 0.119 |
| -1 | 0.368 | 0.269 |
| 0 | 1.000 | 0.500 |
| +1 | 2.718 | 0.731 |
| +2 | 7.389 | 0.881 |
| +3 | 20.086 | 0.953 |

### 3.3 FIMitem difficulty level

Sorting item difficulty (from easy to difficult):

1. Grooming: \(b \approx -1.5\)
2. Wheelchair mobility: \(b \approx -1.0\)
3. Bed/chair transfer: \(b \approx 0\)
4. Walking: \(b \approx +0.5\)
5. Climbing stairs: \(b \approx +1.5\)

### 3.4 Reference explanation of individual ability items

**Anna**（\(\theta = -1.5\)）：

Freshen up:

\[
P = \frac{e^{(-1.5-(-1.5))}}{1+e^0} = 0.5
\]

Wheelchair mobility:

\[
P = \frac{e^{(-1.5-(-1.0))}}{1+e^{-0.5}} = \frac{e^{-0.5}}{1+e^{-0.5}} \approx 0.38
\]

Bed/Chair Transfer:

\[
P = \frac{e^{(-1.5-0)}}{1+e^{-1.5}} = \frac{e^{-1.5}}{1+e^{-1.5}} \approx 0.18
\]

**Explanation**: Anna is 50% sure to complete grooming, but the success rate for more complex activities is very low

**Paul**（\(\theta = 0\)）：

Freshen up:

\[
P = \frac{e^{(0-(-1.5))}}{1+e^{1.5}} = \frac{e^{1.5}}{1+e^{1.5}} \approx 0.82
\]

Wheelchair mobility:

\[
P = \frac{e^{(0-(-1.0))}}{1+e^{1.0}} = \frac{e^{1.0}}{1+e^{1.0}} \approx 0.73
\]

Bed/Chair Transfer:

\[
P = \frac{e^{(0-0)}}{1+e^0} = 0.5
\]

**Explanation**: Paul can complete basic activities very well, and is 50% sure of transferring from bed to chair.

### 3.5 Advantages of item reference

Four major advantages

1. **Absolutely clear meaning**: Know exactly what can be done, and the probability of success can be quantified
2. **Personalized Diagnosis**: Determine the boundaries of capabilities and identify the problem
3. **Guidance Intervention**: Set training goals and choose appropriate difficulty
4. **Cross-group comparison**: Does not rely on specific norms, the meaning remains consistent

## 4. Compatibility of the two methods

### 4.1 Linear transformation of IRT scores

The IRT ability score \(\theta\) can be linearly transformed into a standard score:

\[
T = 50 + 10\theta
\]

Transform the item difficulty accordingly:

\[
b' = 50 + 10b
\]

The reference meaning of the items is maintained, and norm comparisons can be made.

### 4.2 Application suggestions

Choice of different scenarios

- **Clinical Diagnosis**: Give priority to item reference explanations
- **Education Selection**: Can be explained with norm reference
- **Capacity Development**: Focus on item reference explanations
- **Policy Development**: Need to be supplemented by norm reference
