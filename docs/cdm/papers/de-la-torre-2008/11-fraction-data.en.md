# Fraction subtraction data and design

## Data source

The paper uses a subset of fractional subtraction data collected by Tatsuoka and analyzed multiple times:

|item|numerical value|
| --- | ---: |
|student|2,144 secondary school students|
|item|15 fraction subtraction questions|
|Properties|5|
|reaction|Two points|
|Initial Q source|Mislevy (1996) Q for the same data|

## Five attributes

1. Perform basic fraction subtraction operations;
2. Simplify or reduce;
3. Separate the integer part and the fraction part;
4. Borrow 1 from the integer part to the fractional part;
5. Convert integers to fractions.

## Initial Q and item parameters

|question number|Q OK| \(\widehat g\) | \(\widehat s\) |
| ---: | :---: | ---: | ---: |
| 1 | 10000 | .00 | .28 |
| 2 | 11110 | .21 | .12 |
| 3 | 10000 | .14 | .04 |
| 4 | 11111 | .12 | .13 |
| 5 | 10100 | .33 | .25 |
| 6 | 11110 | .03 | .23 |
| 7 | 11110 | .07 | .08 |
| 8 | 11000 | .16 | .05 |
| 9 | 10100 | .08 | .06 |
| 10 | 10111 | .17 | .07 |
| 11 | 10100 | .10 | .10 |
| 12 | 10110 | .03 | .13 |
| 13 | 11110 | .13 | .16 |
| 14 | 11111 | .02 | .20 |
| 15 | 11110 | .01 | .18 |

Attribute 1 appears in every question; attributes 2--5 only appear in some operation structures.

## Authentication settings

\[
\varepsilon=.000,.001,\ldots,.050.
\]

Add 100 EM cycles to each set of candidate Q to obtain the final item parameters. The program is still implemented in Ox by the author.

## What does this application check?

Fraction subtraction Q has a clear tradition of cognitive analysis. The key points here are:

- Will the data driver change a mature Q without reason;
- Which \(\varepsilon\) can completely retain the original Q;
-Would looking at statistical indicators alone make ridiculous attribute requirements in terms of content?

## Differences from the common 536-person version

Fraction subtraction data common in the CDM literature has different subsets and different Qs. This article clearly reports:

\[
N=2144,\quad J=15,\quad K=5.
\]

Subsequent software examples or other papers may use the 536-person, 12-question, 4-attribute version. Reproduction and citation need to be checked according to the paper version, and different subsets cannot be mixed into the same experiment.

