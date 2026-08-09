#NAEP Data & Design

## Original data and analysis subset

The original 2003 NAEP Eighth Grade Mathematics Q-Matrix developed by L. DiBello and colleagues contains:

- 195 multiple choice questions and constructed response questions;
- 17 properties.

This article uses a subset of Texas students:

|item|numerical value|
| --- | ---: |
|student| 3,823 |
|item| 90 |
|Properties| 9 |
|inclusion criteria|Answer at least 12 questions|
|Minimum number of people answering each question| 419 |
|Average number of answers per question|About 794|

Raw multipart reactions are analyzed as dichotomous reactions.

## Nine attributes

|No.|Properties|Number of occurrences in original Q|
| ---: | --- | ---: |
| 1 |calculator| 15 |
| 2 |Measurements, units and conversions| 17 |
| 3 |Data display| 15 |
| 4 |Geometry| 27 |
| 5 |score| 13 |
| 6 |Arithmetic operations in context| 22 |
| 7 |Interpolation, Extrapolation and Estimation| 14 |
| 8 |spatial perception| 16 |
| 9 |higher order thinking| 42 |

Attribute 9 covers nearly half of the questions, far more than other attributes; column Q is not balanced.

## Missingness and weight

The NAEP matrix is very sparse, with each student answering only a subset of the questions. The author modifies the aforementioned algorithm so that:

- The posterior expected number of people and the number of correct answers are included in observation weights;
- Missing answers will not be included in the count of corresponding questions;
- The effective sample size can be different for different questions.

The original article did not list the modified complete Ox code in the main text.

## Authentication settings

\[
\varepsilon=.000,.001,\ldots,.100.
\]

Add 10 EM cycles to each set of candidate Q, and update the item parameters and posterior distribution.

## Initial parameters

Original Table 9:

|Statistics| \(\widehat g\) | \(1-\widehat s\) | \(\widehat\delta\) |
| --- | ---: | ---: | ---: |
|smallest| .0338 | .2613 | -.0004 |
|average| .5022 | .8099 | .3077 |
|maximum| .9786 | 1.0000 | .6407 |

From the average \(1-\widehat s=.8099\) we get:

\[
\overline{\widehat s}=.1901.
\]

So the original test-level indicator is

\[
\overline{\widehat g}+\overline{\widehat s}
=.5022+.1901
=.6923.
\]

## Why is the initial fit so poor?

- Students who have not mastered the required attributes still have an average of 50% probability of answering correctly;
- Guessing of a certain question reaches .9786;
- The correct answer rate for a certain question after mastering all required attributes is only .2613;
- In at least one question \(\delta=-.0004\), the directions of the two groups are almost reversed;
- Average \(\delta=.3077\), weak separation of the two groups.

The authors explicitly acknowledge that the model–data misfit is evident and the purpose of continuing the analysis is primarily to demonstrate what Q diagnostic information the method can provide.

