# Simulation experiment

## Research questions

MCMC of HO-DINA has been studied by de la Torre and Douglas (2004). This simulation focuses on testing:

> Can the DINA EM given in the appendix accurately restore the guessing, slip and standard errors of the item?

## Experimental design

|settings|value|
| --- | ---: |
|Number of students \(I\)| 2,000 |
|Number of items \(J\)| 30 |
|Number of attributes \(K\)| 5 |
|Number of attribute profiles| \(2^5=32\) |
|All \(g_j\)| 0.20 |
|All \(s_j\)| 0.20 |
|attribute profile distribution|32 patterns with equal probability|
|Repeat times| 100 |
|convergence threshold|Maximum parameter change \(<0.0001\)|
|program|EM written by Ox|
|At that time the hardware|3.0 GHz CPU, 1 GB RAM|

## Q matrix of Table 1

Items are divided into three groups according to the number of required attributes:

### Items 1--10: Single attribute questions

\[
\begin{array}{c|ccccc}
j&q_1&q_2&q_3&q_4&q_5\\\hline
1,6&1&0&0&0&0\\
2,7&0&1&0&0&0\\
3,8&0&0&1&0&0\\
4,9&0&0&0&1&0\\
5,10&0&0&0&0&1
\end{array}
\]

Each attribute was measured twice individually.

### Items 11--20: Double attribute questions

\[
\begin{array}{c|c@{\qquad}c|c}
j&\boldsymbol q_j&j&\boldsymbol q_j\\\hline
11&(1,1,0,0,0)&16&(0,1,0,1,0)\\
12&(1,0,1,0,0)&17&(0,1,0,0,1)\\
13&(1,0,0,1,0)&18&(0,0,1,1,0)\\
14&(1,0,0,0,1)&19&(0,0,1,0,1)\\
15&(0,1,1,0,0)&20&(0,0,0,1,1)
\end{array}
\]

### Items 21--30: Three attribute questions

\[
\begin{array}{c|c@{\qquad}c|c}
j&\boldsymbol q_j&j&\boldsymbol q_j\\\hline
21&(1,1,1,0,0)&26&(1,0,0,1,1)\\
22&(1,1,0,1,0)&27&(0,1,1,1,0)\\
23&(1,1,0,0,1)&28&(0,1,1,0,1)\\
24&(1,0,1,1,0)&29&(0,1,0,1,1)\\
25&(1,0,1,0,1)&30&(0,0,1,1,1)
\end{array}
\]

## Running time

On the hardware reported in the paper, this averages less than 18 seconds per dataset.

This number only describes Ox implementations, hardware, and a single design from the 2000s; it is not a cross-language algorithm benchmark.

## Table 2: Parameter recovery

Average of 100 repetitions:

- 59 parameters rounded to a generated value of 0.20;
- The only exception is

  \[
  \overline{\widehat s}_{25}=0.21.
  \]

The overall bias is very small.

## standard error varies with the number of required attributes

Table 2 shows the clear structure:

|item type|Average model SE: \(g\)|Average model SE: \(s\)|Reason|
| --- | ---: | ---: | --- |
|1 attribute|About 0.015--0.016|About 0.015--0.016|In equal probability mode, \(\eta=0,1\) is about half each|
|2 attributes|About 0.011|About 0.022|The total mastery ratio is about \(1/4\)|
|3 properties|About 0.010|About 0.030|The total mastery ratio is about \(1/8\)|

The more attributes required by the item, the smaller the \(\eta=1\) group:

\[
P(\eta=1)=2^{-m}
\]

where \(m\) is the desired number of attributes. Therefore, the effective sample size of \(s_j\) decreases and the standard error increases; the \(\eta=0\) group becomes larger, and the standard error of \(g_j\) decreases slightly.

## Model standard error and empirical standard deviation

Thesis report:

- The average model standard error obtained by A15 is close to the empirical standard deviation of 100 estimates;
- The model standard error is about 2% conservative on average.

This supports both:

1. The EM point estimate recovers well under this design;
2. The appendix observation information can approximately reflect the sampling variation under this design.

## Scope of evidence

The simulation contains only one main condition:

- \(I=2000,J=30,K=5\)；
- Uniform attribute profile;
- All questions \(g=s=.20\);
- The Q matrix is given and correct.

It does not systematically change sample size, test length, parameter quality, attribute correlation, Q errors or rare modes. The paper also leaves more systematic classification research to follow-up work.
