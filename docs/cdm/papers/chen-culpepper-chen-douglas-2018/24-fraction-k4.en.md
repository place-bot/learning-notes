# Experiment: Question-by-question result of \(K=4\)

## Table 4 complete result

CGibbs' \(\widehat Q\) is also consistent with MH.

|item| MH \(\widehat q_j\) | \(\widehat s\) | \(\widehat g\) | Gibbs \(\widehat q_j\) | \(\widehat s\) | \(\widehat g\) |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| \(5/3-3/4\) | 1000 | .11 | .04 | 1000 | .12 | .04 |
| \(3/4-3/8\) | 1000 | .04 | .05 | 1000 | .04 | .04 |
| \(5/6-1/9\) | 1000 | .12 | .01 | 1000 | .12 | .01 |
| \(3\frac12-2\frac32\) | 0100 | .12 | .15 | 0100 | .12 | .16 |
| \(4\frac35-3\frac4{10}\) | 1010 | .16 | .34 | 1010 | .21 | .31 |
| \(6/7-4/7\) | 0010 | .04 | .30 | 0010 | .04 | .28 |
| \(3-2\frac15\) | 0001 | .24 | .02 | 0001 | .20 | .01 |
| \(2/3-2/3\) | 0010 | .06 | .54 | 0100 | .06 | .56 |
| \(3\frac78-2\) | 0010 | .17 | .40 | 0010 | .25 | .33 |
| \(4\frac4{12}-2\frac7{12}\) | 0100 | .23 | .03 | 0110 | .23 | .03 |
| \(4\frac13-2\frac43\) | 0110 | .08 | .07 | 0110 | .08 | .07 |
| \(1\frac18-1/8\) | 0010 | .09 | .21 | 0010 | .09 | .17 |
| \(3\frac38-2\frac56\) | 1111 | .33 | .02 | 1110 | .34 | .02 |
| \(3\frac45-3\frac25\) | 0010 | .07 | .10 | 0010 | .07 | .06 |
| \(2-1/3\) | 0001 | .11 | .04 | 0011 | .11 | .04 |
| \(4\frac57-1\frac47\) | 0010 | .11 | .13 | 0010 | .12 | .12 |
| \(7\frac35-2\frac45\) | 0110 | .14 | .06 | 0110 | .14 | .05 |
| \(4\frac1{10}-2\frac8{10}\) | 0111 | .20 | .13 | 0110 | .16 | .13 |
| \(4-1\frac43\) | 0111 | .32 | .03 | 0111 | .26 | .03 |
| \(4\frac13-1\frac53\) | 0110 | .19 | .02 | 0110 | .19 | .02 |

## q-vector difference

The two methods differ on five questions:

|item| MH/CGibbs |Unconstrained Gibbs|
| --- | --- | --- |
| \(2/3-2/3\) | 0010 | 0100 |
| \(4\frac4{12}-2\frac7{12}\) | 0100 | 0110 |
| \(3\frac38-2\frac56\) | 1111 | 1110 |
| \(2-1/3\) | 0001 | 0011 |
| \(4\frac1{10}-2\frac8{10}\) | 0111 | 0110 |

The restricted method classifies both \(3-2\frac15\) and \(2-1/3\) into the fourth single attribute; the unconstrained method allows the latter question to load an additional third attribute.

## item parameters difference

The author emphasizes:

\[
\widehat s(3-2\tfrac15):
\quad .24\ \text{vs.}\ .20,
\]

\[
\widehat s(3\tfrac78-2):
\quad .17\ \text{vs.}\ .25.
\]

In addition, the slipping of \(4-1\frac43\) is .32 vs. .26, and the difference is also visible.

## Common structure of \(K=3\) and \(K=4\)

The first three questions always load the first attribute; multiple simple questions with the same denominator load the third attribute; complex borrowed questions load multiple attributes. Both restricted MH and CGibbs give the same posterior mode in both dimensions, indicating that the two restricted transfer kernels found the same dominant mode in this run.

## Nothing can be inferred from this table

Tables 3--4 do not provide model selection criteria, so it is impossible to determine whether \(K=3\) or \(K=4\) is better based solely on the size of item parameters. The current `edina` package later added BIC, DIC and posterior predictive diagnostics and is a software extension.

[Next page: Original supplementary material code reading](25-original-code.md)
