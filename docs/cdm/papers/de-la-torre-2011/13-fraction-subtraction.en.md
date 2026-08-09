# Fractional subtraction data

## Data and attributes

The paper uses a subset of the Tatsuoka fractional subtraction data:

|item|numerical value|
| --- | ---: |
|Number of students| 536 |
|number of items| 12 |
|Number of attributes| 4 |
|G-DINA item success probability total| 106 |

The four attributes are:

1. Basic fraction subtraction;
2. approximation;
3. Separate the integer and fractional parts from mixed numbers;
4. Borrow 1 from the integer part to the fractional part.

## Q matrix

|question number|Q OK|question number|Q OK|
| ---: | :---: | ---: | :---: |
| 1 | 1000 | 7 | 1100 |
| 2 | 1111 | 8 | 1010 |
| 3 | 1000 | 9 | 1010 |
| 4 | 1010 | 10 | 1011 |
| 5 | 1111 | 11 | 1111 |
| 6 | 1111 | 12 | 1111 |

Questions 2, 5, 6, 11, and 12 each require four attributes, so each question estimates 16 success probabilities; Questions 1 and 3 each require one attribute, so each question only has two success probabilities.

## Estimate settings

The author uses Ox to write the MMLE program and sets:

- Convergence criterion: 0.001;
- Computer: 3 GHz Pentium 4;
- Run time: within 16 seconds.

Since the sample size is limited relative to the probability of 106 items, the author imposes a monotonic constraint after obtaining the initial estimate:

\[
\widehat P(\boldsymbol a)
\leq
\widehat P(\boldsymbol a')
\quad
\text{when }
\boldsymbol a\prec\boldsymbol a'.
\]

## Complete probability result of Table 3

The following pattern lists only the attributes required for each question, in the same order in which the attributes appear in the corresponding Q row.

|question number|Reduction patterns and success probabilities|
| ---: | --- |
| 1 | \(P(0)=0.00,\ P(1)=0.71\) |
| 2 | \(0000:.21,\ 1000:.21,\ 0100:.21,\ 0010:.21,\ 0001:.21,\ 1100:.21,\ 1010:.21,\ 1001:.21,\ 0110:.23,\ 0101:.23,\ 0011:.23,\ 1110:.23,\ 1101:.23,\ 1011:.74,\ 0111:.23,\ 1111:.89\) |
| 3 | \(P(0)=0.12,\ P(1)=0.95\) |
| 4 | \(00:.33,\ 10:.47,\ 01:.33,\ 11:.77\) |
| 5 | \(0000:.01,\ 1000:.03,\ 0100:.01,\ 0010:.01,\ 0001:.01,\ 1100:.03,\ 1010:.04,\ 1001:.05,\ 0110:.04,\ 0101:.04,\ 0011:.04,\ 1110:.05,\ 1101:.05,\ 1011:.05,\ 0111:.05,\ 1111:.81\) |
| 6 | \(0000:.04,\ 1000:.05,\ 0100:.04,\ 0010:.04,\ 0001:.04,\ 1100:.05,\ 1010:.05,\ 1001:.10,\ 0110:.05,\ 0101:.05,\ 0011:.05,\ 1110:.10,\ 1101:.10,\ 1011:.81,\ 0111:.10,\ 1111:.94\) |
| 7 | \(00:.11,\ 10:.59,\ 01:.11,\ 11:.97\) |
| 8 | \(00:.04,\ 10:.42,\ 01:.04,\ 11:.97\) |
| 9 | \(00:.07,\ 10:.43,\ 01:.07,\ 11:.92\) |
| 10 | \(000:.01,\ 100:.05,\ 010:.01,\ 001:.01,\ 110:.05,\ 101:.07,\ 011:.05,\ 111:.88\) |
| 11 | \(0000:.00,\ 1000:.00,\ 0100:.00,\ 0010:.00,\ 0001:.00,\ 1100:.27,\ 1010:.18,\ 1001:.00,\ 0110:.00,\ 0101:.00,\ 0011:.00,\ 1110:.27,\ 1101:.41,\ 1011:.81,\ 0111:.27,\ 1111:.85\) |
| 12 | \(0000:.00,\ 1000:.00,\ 0100:.00,\ 0010:.00,\ 0001:.00,\ 1100:.02,\ 1010:.00,\ 1001:.00,\ 0110:.00,\ 0101:.00,\ 0011:.00,\ 1110:.02,\ 1101:.16,\ 1011:.37,\ 0111:.02,\ 1111:.85\) |

## Single attribute question

The result of question 3 is

\[
P(0)=0.12,
\qquad
P(1)=0.95.
\]

For single attribute questions, they can be directly interpreted as

\[
g_3=0.12,
\qquad
1-s_3=0.95.
\]

## Which questions are close to DINA

The paper believes that among the multi-attribute questions, only questions 5 and 10 are closer to DINA:

- The probabilities before full mastery are generally low and similar;
- The probability of success increases significantly when fully mastered.

The remaining eight multi-attribute questions clearly violate the constraint that "all non-full mastery modes share the same success rate".

## Differential effects of attributes

Questions 4, 7, 8, and 9 are all dual attribute questions. Take question 8 as an example:

\[
P(00)=0.04,\quad
P(10)=0.42,\quad
P(01)=0.04,\quad
P(11)=0.97.
\]

The first required attribute alone provides a significant improvement, the second has little effect on its own; when mastered together, the success rate reaches 0.97. DINA will suppress the first three probabilities to the same value, so the asymmetry in attribute contributions cannot be seen.

## Structure of the four-attribute question

In questions 2, 6, and 11, the pattern \(1011\) for mastering attributes 1, 3, and 4 has reached a high success rate:

\[
0.74,\quad0.81,\quad0.81.
\]

After adding attribute 2, the probability of full mastery reaches

\[
0.89,\quad0.94,\quad0.85.
\]

This suggests that basic arithmetic, integer/fraction separation and borrowing form a key combination, with reduction providing additional boost.

The partial mastery probability of Question 12 changes greatly, so it does not meet DINA's equal-probability low group assumption; at the same time, the success rate of the full mastery mode is still obviously the highest:

\[
P(1111)=0.85.
\]

## Explain boundaries

The paper clearly reminds that the sample size is small and the probability of each mode should be interpreted with caution. Further considerations include:

- Is the Q matrix correct?
- Effective number of people in rare mode;
- The impact of monotonic constraints on estimates;
- Whether attribute hierarchy exists;
- Whether the item content actually supports the estimated interaction.
