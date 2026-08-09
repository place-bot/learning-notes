# Table 4: Single new question calibration

## Settings

\[
Q=
\begin{pmatrix}
I_K\\I_K\\V_J
\end{pmatrix},
\qquad
J=2K+1.
\]

The first \(2K\) rows are known, only \(V_J\) is estimated. Per condition:

\[
s_j=g_j=.2,\qquad
p_{\boldsymbol\alpha}=2^{-K},
\]

Generate 100 copies of data.

## \(K=3\)

| \(V_J\) | \(N=250\) | \(N=500\) | \(N=1000\) | \(N=2000\) |
| --- | ---: | ---: | ---: | ---: |
| 100 | 91 | 98 | 100 | 100 |
| 110 | 82 | 97 | 99 | 100 |
| 111 | 70 | 83 | 100 | 100 |

## \(K=4\)

| \(V_J\) | \(N=500\) | \(N=1000\) | \(N=2000\) | \(N=4000\) |
| --- | ---: | ---: | ---: | ---: |
| 1000 | 91 | 98 | 100 | 100 |
| 1100 | 84 | 94 | 100 | 100 |
| 1110 | 71 | 87 | 99 | 100 |
| 1111 | 39 | 62 | 94 | 100 |

## \(K=5\)

| \(V_J\) | \(N=1000\) | \(N=2000\) | \(N=4000\) | \(N=8000\) |
| --- | ---: | ---: | ---: | ---: |
| 10000 | 95 | 100 | 100 | 100 |
| 11000 | 88 | 99 | 100 | 100 |
| 11100 | 77 | 98 | 100 | 100 |
| 11110 | 47 | 76 | 92 | 100 |
| 11111 | 29 | 37 | 56 | 88 |

Footnote added: \(V_J=11111\) is restored 100 times at \(N=12000\).

## Rule 1: The more attributes required, the harder it is

DINA is a conjunctive model. Under uniform attribute distribution, the proportion required to cover a given \(r\) attribute is

\[
2^{-r}.
\]

The ideal mastery group for all 1 new questions is very small:

\[
K=5,\ r=5
\quad\Rightarrow\quad
\Pr(\xi=1)=1/32.
\]

Estimating \(c_J\) and discerning "requires four" from "requires five" require a large sample size.

## Rule 2: The anchor question significantly reduces the problem

The main experiment needs to correct the complete Q at the same time; here the first \(2K\) rows are fixed, and only the \(2^K\) new question q-vectors are compared. Therefore, new questions with low dimensions and low number of attributes have a high recovery rate under a small N.

## Rule 3: The total sample size needs to increase with the rare master group

For \(K=5,V_J=11111\), even \(N=8000\) still fails 12 times out of 100 times. When designing the calibration sample, in addition to the average number of people in the \(2^K\) category, you should also check the ideal number of people in the new question mastering group

\[
N\Pr(\xi_J=1).
\]
