# Fractional subtraction real data

## Data

- \(N=536\) junior high school students;
- \(J=11\) fraction subtraction questions;
- \(K=4\) cognitive attributes;
- Data derived from a subset of data used by Tatsuoka (1990) and de la Torre (2011).

## Four attributes

|Properties|meaning|
| --- | --- |
| \(\alpha_1\) |Perform basic fraction subtraction|
| \(\alpha_2\) |simplify or reduce|
| \(\alpha_3\) |Separate integer part from fraction|
| \(\alpha_4\) |Borrow 1 from the integer part to the fractional part|

## Original 11 questions Q

|question number|item|Original q-vector|Saturated maximum GDI|
| ---: | --- | :---: | ---: |
| 1 | \(3\frac17-2\frac37\) | 1111 | .1463 |
| 2 | \(\frac67-\frac47\) | 1000 | .0916 |
| 3 | \(3\frac78-2\) | 1010 | .0351 |
| 4 | \(4\frac4{12}-2\frac7{12}\) | 1111 | .1383 |
| 5 | \(4\frac13-2\frac43\) | 1111 | .1922 |
| 6 | \(\frac{11}{8}-\frac18\) | 1100 | .1146 |
| 7 | \(3\frac45-3\frac25\) | 1010 | .1392 |
| 8 | \(4\frac57-1\frac47\) | 1010 | .1213 |
| 9 | \(7\frac35-\frac45\) | 1011 | .1715 |
| 10 | \(4\frac1{10}-2\frac8{10}\) | 1111 | .1496 |
| 11 | \(4\frac13-1\frac53\) | 1111 | .1681 |

The last column is

\[
\widehat{\varsigma}_{\max}^2
=
\widehat{\varsigma}^2(1111).
\]

## Analysis steps

1. Fit G-DINA with original Q;
2. Estimate the posterior weights of 16 complete attribute profiles;
3. Estimate the success rate of each question under 16 modes;
4. Search for 15 non-zero q-vectors for each question;
5. Use \(\varepsilon=.95\) to select the suggestion row.

## Why this data has explanatory value

The surface structures of multiple questions are similar, but they are:

- Whether you need to borrow a seat;
- Whether the subtrahend is a mixed number;
- Whether to generate improper fractions;
- Whether simplification is ultimately needed

Different aspects. Statistical suggestions can be compared with clear problem-solving steps on a problem-by-question basis, making it easy to observe the agreement and conflict between the empirical Q and the expert Q.
