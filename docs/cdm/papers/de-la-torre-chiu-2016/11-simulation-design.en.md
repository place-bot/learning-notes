# Co-design of simulation experiments

## Two study goals

| Study |Generate model|Inspection points|
| --- | --- | --- |
| 1 | DINA、DINA/A-CDM、A-CDM、DINO/A-CDM、DINO |Method performance of trans-reduction reaction process|
| 2 |Unconstrained G-DINA|Performance under more complex success probability profiles|

Co-fixed:

\[
N=2000,\qquad J=30,\qquad K=5.
\]

100 copies of data were generated for each condition.

## Attribute generation

Students’ advanced abilities:

\[
\theta_i\sim N(0,1).
\]

Given \(\theta_i\), five attributes are conditionally independent:

\[
P(\alpha_{ik}=1\mid\theta_i)
=
\frac{
\exp[\lambda_{1k}(\theta_i-\lambda_{0k})]
}{
1+\exp[\lambda_{1k}(\theta_i-\lambda_{0k})]
}.
\tag{15}
\]

The parameters are

\[
\boldsymbol\lambda_0=(-1,-.5,0,.5,1),
\qquad
\lambda_{1k}=1.5.
\]

This results in correlated attributes: the higher the common \(\theta_i\), the higher the probability that multiple attributes are mastered simultaneously.

## Correct Q

The 30 questions are divided into 10 single-attribute questions, 10 dual-attribute questions, and 10 three-attribute questions on average:

|question number| q-vector |question number| q-vector |question number| q-vector |
| ---: | :---: | ---: | :---: | ---: | :---: |
| 1 | 10000 | 11 | 11000 | 21 | 11100 |
| 2 | 01000 | 12 | 10100 | 22 | 11010 |
| 3 | 00100 | 13 | 10010 | 23 | 11001 |
| 4 | 00010 | 14 | 10001 | 24 | 10110 |
| 5 | 00001 | 15 | 01100 | 25 | 10101 |
| 6 | 10000 | 16 | 01010 | 26 | 10011 |
| 7 | 01000 | 17 | 01001 | 27 | 01110 |
| 8 | 00100 | 18 | 00110 | 28 | 01101 |
| 9 | 00010 | 19 | 00101 | 29 | 01011 |
| 10 | 00001 | 20 | 00011 | 30 | 00111 |

## How to create errors Q

Each replication randomly flips about 5% of Q entries:

- Flip the first 50 copies into 7 cells;
- Flip the last 50 copies into 8 squares.

Since Q has \(30\times5=150\) squares, 7 or 8 squares is about 5%. Different errors may fall on different items, which can cause up to about 27% of the 30 q-vectors to be misset.

## Evaluation level

### q-entry layer

Judgment one by one:

- The proportion of initial incorrect cells that are corrected;
- The proportion of initially correct cells that are retained.

### q-vector layer

Judgment question by question:

- Proportion of complete recovery of initially erroneous rows;
- The proportion of initially correct rows that are kept intact.

## Original terminology reminder

The paper calls "error items corrected" as true-negative rate/sensitivity, and "correct items retained" as true-positive rate/specificity. This naming can easily cause confusion with common two-category conventions. This topic directly uses semantically clear names:

- **misspecified corrected**；
- **correct retained**。

## Threshold

All simulations use:

\[
\varepsilon=.95.
\]

Therefore, the difference between studies comes from the generation model and item quality, and the thresholds remain consistent.
