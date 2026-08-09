# 4. Modified Grade Response Model (M-GRM)

## 4.1 Development background

**Developer:** Muraki (1990)

**Purpose:**

- Facilitates the use of GRM in analyzing questionnaire with scale type response format
- For example: all items have the same number of attitude questionnaire response categories

Naming instructions

- This book is called: "Modified" Grade Response Model (M-GRM)
- Muraki et al. sometimes call this model "evaluation scale model"
- This term is not used in this book to avoid confusion with Andrich’s assessment scale model later.
- Actually, M-GRM is a restricted version of Samejima (1969) GRM

## 4.2 The relationship between M-GRM and GRM

**Same points:**

- Allow item slope parameters to vary between items
- is indirect (calculating response probability requires a two-step process)

**Key differences:**

In M-GRM, the inter-category threshold parameter of GRM (\(\beta_{ij}\)) is decomposed into two parts:

\[
\beta_{ij} = b_i - c_j
\]

Among them:

- \(b_i\): Position parameters of each item
- \(c_j\): A set of category threshold parameters for the entire scale

## 4.3 Expression of M-GRM

**Operating characteristic curve:**

\[
P^*_x(\theta) = \frac{\exp[\alpha_i(\theta - (b_i - c_j))]}{1 + \exp[\alpha_i(\theta - (b_i - c_j))]} \tag{5.3}
\]

Or equivalently:

\[
P^*_x(\theta) = \frac{\exp[\alpha_i(\theta - b_i + c_j)]}{1 + \exp[\alpha_i(\theta - b_i + c_j)]} \tag{5.4}
\]

**Actual category response probability:**

\[
P_x(\theta) = P^*_x - P^*_{x+1} \tag{5.5}
\]

The boundary conditions are the same as GRM: \(P^*_{(x=0)}(\theta) = 1.0\), \(P^*_{(x=m+1)}(\theta) = 0.0\)

## 4.4 Parameter explanation

Slope parameter \(\alpha_i\)

- Similar to parameters in GRM
- Indicates how quickly item scores are expected to change with trait level

Position parameter \(b_i\)

- Used to move category threshold parameters up and down the trait continuum
- Represents the "difficulty" or scale value of the item
- **Positive**: Few subjects choose the highest response category on this item
- **Large Negative Value**: Few subjects scored low on this item

## 4.5 The core difference between M-GRM and GRM

### 4.5.1 Differences in parameter estimates

**GRM Medium:**

- Each category threshold parameter (\(\beta_{ij}\)) of each item is estimated separately
- More flexible, but requires more parameters

**M-GRM:**

- A set of category threshold parameters (\(c_j\)) estimates the entire scale
- Simultaneously estimate a position parameter (\(b_i\)) for each item
- More parameter-saving, but more limited

### 4.5.2 The meaning of "restricted" model

M-GRM assumptions

The distance between category boundaries is equal between scale items, that is, the distance pattern between categories of all items is the same.

**GRM Flexibility:**

- Category boundaries can change freely between items
- Each item can have its own unique category distribution model

**result:** M-GRM requires fewer parameters to be estimated than GRM

## 4.6 Advantages and limitations of the M-GRM model

Among the multi-category item response models, **M-GRM (modified grade response model)** is a model that is particularly suitable for handling "Likert scale items". In this section we will explain in depth: what M-GRM is, why it was designed, what scenarios it is suitable for, and what its limitations are.

### 4.6.1 The core motivation of M-GRM: making the model more suitable for “Likert scale”

In psychology and educational measurement, many questionnaires use a **Likert scale** (ordinal options such as "strongly disagree" to "strongly agree"). But these reaction options:

- Each question looks the same (all score 0–4);
- But the "difficulty" of the items may be different;
- The psychological distance between options (such as "agree" and "strongly agree") can be seen as the structure of the scale itself.

**M-GRM Goals:**
In the model, the "item position" and "category structure" are separated for modeling.

### 4.6.2 M-GRM parameter structure disassembly

M-GRM has two key parameter groups:

**item position parameter** \( b_i \)

- Indicates the trait level required for the \( i \) item to "change from disagreement to agreement" (such as neuroticism)
- Like "Is this question difficult to pass?" or "What kind of people will agree with the item?"
- Can be used to sort items (from easy to agree to not easy to agree)

**Category Threshold Parameter** \( c_j \)

- Represents the increment in ability required to jump from one option to the next (e.g. "disagree" → "neutral")
- It is a structural parameter on the entire scale and does not depend on the specific item.
- All items share a set of \( c_1, c_2, c_3, c_4 \)

**Model formula of M-GRM:**
If we disassemble GRM's \(\beta_{ij}\) into:

\[
\beta_{ij} = b_i - c_j
\]

Then the threshold of each category is determined by the "item position" minus the "category position".
This is the main feature of M-GRM: **separating "item preference" and "rating point structure"**.

### 4.6.3 Advantages of M-GRM (Why use it)

1. **Strong explanation power**: You can clearly know that the position of the item is determined by the content, and the structure of the rating level is uniformly defined.
   Particularly suitable for theoretical research: For example, you want to know "about how much neuroticism it takes for a subject to change from 'neutral' to 'agree'."
2. **Save the number of parameters**: All items share a set of \( c_j \), which is more "economical" than GRM's independent estimation of a set of thresholds for each question.
3. **Closely linked to classical measurement theory**: Ideologically similar to Thurstone’s “continuous category model” (that is, assuming that rating points represent equidistant intervals on a continuous psychological measurement scale).

### 4.6.4 Limitations and implementation difficulties of M-GRM

1. **Arbitrariness of category parameters**: \( c_j \) does not have a natural unit scale, and usually requires an artificial constraint (such as \( c_1 = 0 \)) to be recognized.
   This makes the "absolute values" of model parameters have no practical meaning and can only be used for "relative interpretation".
2. **Difficulty in dealing with different scoring formats**: If some questions in the questionnaire are "0-4" and some are "1-7", M-GRM cannot handle them uniformly.
   Items with different scoring formats must be artificially grouped (called "block modeling").
3. **Different blocks cannot be directly compared**: The item parameters of block 1 cannot be directly compared with block 2.
   If you want to put the entire scale on a unified "measurement scale", you need to do **scale linking**.

### 4.6.5 M-GRM and GRM selection suggestions

Suggestions for applicable scenarios

It is recommended to use M-GRM when:

- All items use the same scoring format (e.g. all 0–4)
- You want to separately model "the difficulty of the item itself" and "the psychological distance of the scoring structure"
- You are interested in the structure between rating scales (e.g. how far is between "neutral" and "agree")

GRM is recommended when:

- The items in your questionnaire use different numbers of options (for example, some questions are 0–3, and some are 0–5)
- Or you want each question to have its own independent scoring structure
- or you are not sure whether the scoring structure can be unified

## 4.7 Application of M-GRM on NEO-FFI data

### 4.7.1 Analysis settings

**Program used:** PARSCALE (Muraki, 1993)

**Processing method:**

- All 12 items are treated as a single block
- (Note: When each item is analyzed as its own block, the parameter estimates are almost identical to MULTILOG's GRM)

Reasons for parameter differences

Any differences in parameter estimates in Table 5.3 (GRM) and Table 5.4 (M-GRM) are entirely due to the results of estimating the "common" set of class thresholds in M-GRM.

### 4.7.2 Table 5.4: M-GRM estimation result: estimated item parameters and fitting statistics of the modified rank response model

|item|Slope \( a_i \) (SE)|Location \( b_i \) (SE)| \(\chi^2\) | df | \(p\) |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.93 (0.05) | -0.96 (0.10) | 20.66 | 12 | 0.055 |
| 2 | 1.45 (0.07) | 0.28 (0.06) | 14.67 | 13 | 0.328 |
| 3 | 1.13 (0.06) | -0.73 (0.08) | 21.15 | 12 | 0.048 |
| 4 | 1.33 (0.07) | -0.39 (0.07) | 6.90 | 11 | 0.808 |
| 5 | 1.16 (0.08) | -0.02 (0.06) | 8.37 | 12 | 0.756 |
| 6 | 0.98 (0.05) | 0.25 (0.09) | 36.90 | 13 | 0.000 |
| 7 | 1.51 (0.08) | -0.35 (0.06) | 11.10 | 10 | 0.349 |
| 8 | 1.19 (0.06) | -0.09 (0.08) | 18.47 | 13 | 0.140 |
| 9 | 1.50 (0.08) | 0.06 (0.06) | 21.37 | 13 | 0.060 |
| 10 | 1.33 (0.07) | -0.15 (0.07) | 7.97 | 13 | 0.847 |
| 11 | 1.30 (0.07) | 0.51 (0.07) | 36.64 | 12 | 0.000 |
| 12 | 1.03 (0.05) | -0.42 (0.09) | 8.28 | 13 | 0.825 |

> **M-GRM category threshold (shared parameter):**
> \( c_1 = -2.254 \pm 0.04,\quad c_2 = -0.451 \pm 0.02,\quad c_3 = 0.431 \pm 0.02,\quad c_4 = 2.266 \pm 0.04 \)

**Note:**

The five-level response model threshold parameter \(\beta_{ij}\) for each question can be given by:

\[
\beta_{ij} = b_i - c_j
\]

Obtained, where \( b_i \) is the item position and \( c_j \) is the shared category threshold.

However, the model assumptions of M-GRM are slightly different from those of traditional GRM, so the calculated \(\beta_{ij}\) is not completely consistent.

### 4.7.3 Important Observations

**1. Slope parameter characteristics:**

- Slope parameters in M-GRM tend to have less variability than slope estimates under GRM
- Even items with poor functionality (such as item1) have a slope parameter of 0.93

**2. Correspondence between position parameters and item difficulty:**

- The position parameter indicates the "difficulty" of the item
- The sorting corresponds exactly to the item average value shown in Table 5.1
- item2: small average (1.70) → high position (0.30) → few subjects have high scores
- item1: large average (2.52) → low position (-0.96) → few subjects scored low

**3. Category threshold characteristics:**

- sums to zero (program-imposed scale recognition constraint)
- orderly
- remains unchanged across all 12 items

### 4.7.4 Fit statistics

**Chi-Square Fit Statistics:**

- The right column displays the chi-square fit statistic output by PARSCALE
- Result: 3 out of 12 items are not well represented by the estimated M-GRItem parameters (p < .05)

Important notes

Position (\(b_i\)) minus category threshold (\(c_j\)) roughly yields the \(\beta_{ij}\) parameter in GRM. They are not identical because the two models make different assumptions.
