# 1. Instance data

## 1.1 Data source

- 350 undergraduate students
- Test: Neuroticism-Extraversion-Openness Five-Factor Personality questionnaire (NEO-FFI)
- Specific part: 12 items of neuroticism scale
- Reference: Costa & McCrae, 1992

## 1.2 Data display

**Table 5.1: NEO-FFI Neuroticism scaleitem response frequency and mean score (N = 350)**

|Item|item content| 0 | 1 | 2 | 3 | 4 | M |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |Not a Worrier (R)\*| 29 | 55 | 50 | 137 | 79 | 2.52 |
| 2 |Feel inferior to others| 35 | 120 | 100 | 72 | 23 | 1.70 |
| 3 |Feeling like breaking down under pressure| 25 | 72 | 43 | 141 | 69 | 2.45 |
| 4 |Rarely feel lonely, blue (R)| 20 | 90 | 68 | 125 | 47 | 2.25 |
| 5 |feeling nervous and anxious| 17 | 111 | 97 | 101 | 24 | 2.01 |
| 6 |sometimes feel worthless| 72 | 89 | 52 | 94 | 43 | 1.85 |
| 7 |Rarely feel fear or anxiety (R)| 11 | 95 | 79 | 130 | 35 | 2.24 |
| 8 |Angry at the way he was treated| 22 | 98 | 92 | 109 | 29 | 2.07 |
| 9 |feeling frustrated and wanting to give up| 27 | 128 | 66 | 95 | 34 | 1.96 |
| 10 |Rarely feeling sad, depressed (R)| 22 | 105 | 79 | 107 | 37 | 2.09 |
| 11 |Often feel helpless and need help| 56 | 129 | 68 | 73 | 24 | 1.66 |
| 12 |experience shame| 30 | 88 | 55 | 118 | 59 | 2.25 |

> Note: 0 = Strongly disagree; 1 = Disagree; 2 = Neutral; 3 = Agree; 4 = Strongly agree.
> \* All items with (R) have been reverse encoded.

Shows each item:

- Brief content description
- Frequency of observed responses within each category
- average item score (0 to 4scale)

Example:

- item1: "Not a Worrier (R)", category distribution: 29, 55, 50, 137, 79 people, average score 2.52
- item2: "Feeling inferior to others", category distribution: 35, 120, 100, 72, 23 people, average score 1.70

**Table 5.2: Raw total score averages by response category and item (N = 350)**

### 1.2.1 Average raw score number of item 1–6

|reaction category|item 1|item 2|item 3|item 4|item 5|item 6|
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 23.2 | 15.8 | 14.8 | 17.7 | 14.0 | 17.0 |
| 1 | 19.5 | 25.7 | 19.1 | 18.4 | 20.4 | 21.6 |
| 2 | 21.2 | 26.0 | 21.9 | 22.8 | 25.7 | 25.9 |
| 3 | 25.2 | 31.0 | 27.4 | 28.8 | 29.3 | 29.8 |
| 4 | 32.0 | 34.7 | 32.3 | 33.1 | 34.6 | 34.6 |
| **\(R_{p\\beta}\)** | .43 | .61 | .64 | .64 | .59 | .70 |

### 1.2.2 Average raw score number of item 7–12

|reaction category|item 7|item 8|item 9|item 10|item 11|item 12|
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 16.4 | 18.0 | 14.3 | 18.5 | 16.2 | 16.9 |
| 1 | 19.8 | 21.4 | 20.3 | 19.7 | 22.5 | 20.5 |
| 2 | 22.9 | 25.1 | 26.0 | 24.3 | 27.1 | 23.9 |
| 3 | 28.9 | 28.7 | 30.1 | 29.5 | 31.1 | 27.7 |
| 4 | 32.7 | 29.4 | 36.0 | 33.1 | 35.7 | 32.1 |
| **\(R_{p\\beta}\)** | .56 | .42 | .72 | .58 | .67 | .56 |

> Note: item responses are scored on a scale from 0 to 4.

## 1.3 The meaning and use of Rpbeta indicator

### 1.3.1 Basic definition

**\(R_{p\beta}\)** means:

> **Pearson correlation coefficient** between item score (score on a certain question) and total test score**
> That is: whether the item is consistent with the total score and whether it "follows the measurement target."

Also known as:

- **item-total score correlation (Item-total correlation)**
- Or more rigorously: **corrected item-total score related**

### 1.3.2 Calculation method

Assume:

- \( X_p \): participant \( p \)’s original score for a certain item (such as 0–4)
- \( T_p \): participant \( p \) removes the total score of this question from the scale

Then the correlation coefficient is calculated as:

\[
R_{p\beta} = \mathrm{Cor}(X_p, T_p)
\]

### 1.3.3 Purpose of use

1. **Judge item discrimination (Discrimination)**
2. \( R_{p\beta} > 0.30 \): has the ability to distinguish
3. \( R_{p\beta} > 0.50 \): Strong discrimination ability
4. **Perform item analysis**
5. Determine which items are “helpful” to the measurement goal and which items may be “inverse”
6. **Item quality check before reliability analysis**

### 1.3.4 Comparison with IRT discrimination

|Features| \(R_{p\beta}\) |IRT discrimination parameter \(\alpha\)|
| --- | --- | --- |
|theory of belonging|Classical Measurement Theory (CTT)|Item Response Theory (IRT)|
|Meaning|Linear correlation between item and total score|The slope of latent ability on the probability of answering a question|
|Typical value range|-1 to 1|Usually a positive value (such as 0.5~3.0)|
|Does it depend on the model?|No|Yes (like 2PL model)|

### 1.3.5 Notes

- Remember when using \(R_{p\beta}\) **reverse questions need to be reverse coded first**
- Usually used in the preliminary analysis stage of Likert scale, personality questionnaire, and psychometrics

## 1.4 Important Observations

- average item scores are not widely dispersed
- But the frequency of category responses varies greatly between items
- NEO-FFIitem has substantial differences in its relationship with total test scores and ability to distinguish subjects

## 1.5 Basic assumptions

In the following analysis, it is assumed that the NEO-FFIitem reaction forms a single-dimensional scale and is locally independent. For practical application, these assumptions need to be supported by empirical evidence.
