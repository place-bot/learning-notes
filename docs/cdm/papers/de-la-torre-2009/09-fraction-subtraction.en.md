# Fractional subtraction real data

## Data

Paper analysis:

|item|numerical value|
| --- | ---: |
|student|2,144 secondary school students|
|item|15 fraction subtraction questions|
|Properties|5|
|Data source|K. Tatsuoka (1990), see also C. Tatsuoka (2002)|

The authors thank Kikumi Tatsuoka for providing the data. The paper did not publish the data files as attachments.

## Q matrix of Table 3

|item| \(\boldsymbol q_j\) |item| \(\boldsymbol q_j\) |
| ---: | --- | ---: | --- |
| 1 | (1,0,0,0,0) | 9 | (1,0,1,0,0) |
| 2 | (1,1,1,1,0) | 10 | (1,0,1,1,1) |
| 3 | (1,0,0,0,0) | 11 | (1,0,1,0,0) |
| 4 | (1,1,1,1,1) | 12 | (1,0,1,1,0) |
| 5 | (0,0,1,0,0) | 13 | (1,1,1,1,0) |
| 6 | (1,1,1,1,0) | 14 | (1,1,1,1,1) |
| 7 | (1,1,1,1,0) | 15 | (1,1,1,1,0) |
| 8 | (1,1,0,0,0) |  |  |

There are no single attribute questions for attributes 2 and 5. The Q matrix also contains multiple questions requiring four or five attributes, so the ideal response vectors for some patterns may be very close.

## Two kinds of fitting

|model|Attribute distribution|estimate|Point estimates and uncertainty|
| --- | --- | --- | --- |
| DINA |saturated multinomial distribution| EM |Maximum value and information matrix SE|
| HO-DINA |High-level ability constraints| MCMC |posterior mean and posterior SD|

## Table 4 Complete itemresult

In parentheses is the standard error or posterior standard deviation.

|question| DINA \(\hat g\) | DINA \(\hat s\) | HO \(\hat g\) | HO \(\hat s\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0.00 (.050) | 0.28 (.013) | 0.00 (.004) | 0.28 (.012) |
| 2 | 0.21 (.013) | 0.12 (.011) | 0.21 (.012) | 0.12 (.010) |
| 3 | 0.13 (.023) | 0.04 (.005) | 0.13 (.027) | 0.04 (.005) |
| 4 | 0.12 (.011) | 0.13 (.014) | 0.13 (.009) | 0.13 (.015) |
| 5 | 0.30 (.025) | 0.25 (.012) | 0.23 (.035) | 0.25 (.011) |
| 6 | 0.03 (.006) | 0.23 (.014) | 0.03 (.006) | 0.23 (.014) |
| 7 | 0.07 (.008) | 0.08 (.009) | 0.07 (.008) | 0.08 (.009) |
| 8 | 0.15 (.020) | 0.05 (.007) | 0.15 (.022) | 0.05 (.007) |
| 9 | 0.08 (.016) | 0.06 (.007) | 0.09 (.018) | 0.06 (.007) |
| 10 | 0.17 (.013) | 0.07 (.010) | 0.17 (.012) | 0.07 (.010) |
| 11 | 0.10 (.017) | 0.11 (.009) | 0.11 (.017) | 0.11 (.009) |
| 12 | 0.03 (.006) | 0.13 (.012) | 0.04 (.007) | 0.13 (.011) |
| 13 | 0.13 (.012) | 0.16 (.012) | 0.14 (.010) | 0.16 (.012) |
| 14 | 0.02 (.005) | 0.20 (.016) | 0.02 (.005) | 0.20 (.016) |
| 15 | 0.01 (.003) | 0.18 (.013) | 0.01 (.004) | 0.18 (.013) |

## How close are the two models?

Most point estimates are the same or differ by just 0.01. The paper points out that the main exceptions are:

- \(\widehat g\) for Item 5: 0.30 vs. 0.23;
- \(\operatorname{SE}(\widehat g)\) for Item 1: 0.050 vs. 0.004;
- \(\operatorname{SE}(\widehat g)\) for Item 5: 0.025 vs. 0.035.

Based on this, the author believes that it is reasonable to use high-order capabilities to constrain the attribute joint distribution of these data.

## Explanation of Item 12

Item 12 requires attributes 1, 3, and 4:

\[
\boldsymbol q_{12}=(1,0,1,1,0).
\]

DINA gives

\[
\widehat g_{12}=0.03,
\qquad
\widehat s_{12}=0.13.
\]

Therefore:

The probability of answering correctly for those who master all the required attributes is

\[
1-\widehat s_{12}=0.87.
\]

The probability of correct answer for a person who lacks at least one required attribute is

\[
\widehat g_{12}=0.03.
\]

This is the specific example used by the paper to demonstrate the pedagogical interpretation of DINA parameters.

## Where can result be supported?

Table 4 supports:

- Two attribute distribution settings obtain similar item parameters on this data;
- DINA parameters can be converted into correct answer probability under ideal conditions;
- EM versus MCMC did not produce systematically large differences in this instance.

The paper does not report:

- Comparison of model fit goodness;
- Set aside sample predictions;
- Q matrix alternative;
- Student classification accuracy;
- The impact of diagnostic feedback on teaching results.

So the real data part is a demonstration of parameter estimation and cannot alone prove that the Q matrix is correct or that the diagnostic intervention is effective.
