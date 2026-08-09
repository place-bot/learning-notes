# Table 1: sample size, number of attributes and recovery rate

## Original table

The numbers in the table below are the number of times the true Q is completely restored out of 100 times.

| Q | \(N=500\) | \(N=1000\) | \(N=2000\) | \(N=4000\) |
| --- | ---: | ---: | ---: | ---: |
| \(Q_1,K=3\) | 94 | 100 | 100 | 100 |
| \(Q_2,K=4\) | 82 | 100 | 100 | 100 |
| \(Q_3,K=5\) | 38 | 98 | 100 | 100 |

The number of failures is 100 minus the value in the table.

## sample size effect

When K is fixed, the recovery rate increases rapidly when N increases. The most difficult \(K=5\):

\[
38\%\to98\%\to100\%\to100\%.
\]

The joint moments are more stable and EM estimates of rare attribute classes are more reliable.

## Dimension effect

Fixed \(N=500\):

\[
94\%\to82\%\to38\%.
\]

Growth K simultaneously expands:

- Number of attribute categories \(2^K\);
-The number of candidate q-vectors for each question is \(2^K\);
- The effective complexity of the nuisance parameter;
- The number of approximately equivalent candidates in the search.

## Original text 94/98 Contradiction

Table 1 explicitly writes for \(Q_1,N=500\):

\[
\widehat Q=Q:94,\qquad \widehat Q\ne Q:6.
\]

The text below the table says "recovers the true Q-matrix 98 times". Both the official PDF and the PMC text retain this contradiction. This topic uses the table number 94, because the sum of 94 and failure 6 is exactly 100; at the same time, the difference in the text is retained to avoid silently changing the number for the author.

## Can we say "large samples will definitely recover"

These are 100 Monte Carlo frequencies per condition. Observing 100/100 indicates good performance under this design, but it still does not follow that finite sample recovery is inevitable for all parameters, all Q, and all starting points.

## Relationship to Algorithm 1

The result mixes three factors at the same time:

1. The overall degree of identifiability of Q;
2. Whether the limited sample objective ranks true Q near the lowest;
3. Whether the line-by-line search starting from \(Q_0\) reaches true Q.

Table 1 does not separate the three. Figures 1--2 then show that true Q sometimes fails to even reach the minimum of the finite sample target.
