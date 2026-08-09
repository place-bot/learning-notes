# Table 3: Related and uneven attributes

## Generate model

First generate

\[
\boldsymbol\theta=(\theta_1,\ldots,\theta_K)
\sim N(\boldsymbol0,\Sigma),
\]

The diagonal of \(\Sigma\) is 1, and the common correlation of any two dimensions is

\[
\rho\in\{.05,.15,.25\}.
\]

redefine

\[
\alpha_k=
\mathbf 1\left[
\theta_k\ge
\Phi^{-1}\left(\frac{k}{K+1}\right)
\right].
\]

The threshold changes with the attribute number, so the marginal mastery rate of each attribute is different. Continue to use \(Q_1,K=3\), \(s_j=g_j=.2\), 100 copies of data per condition, and adopt similar early stopping.

## Original table recovery times

| \(\rho\) | \(N=1000\) | \(N=2000\) | \(N=4000\) |
| ---: | ---: | ---: | ---: |
| .05 | 78 | 98 | 100 |
| .15 | 71 | 94 | 99 |
| .25 | 41 | 76 | 95 |

## Related effects

For fixed N, the higher the correlation, the lower the complete recovery rate. For example \(N=1000\):

\[
78\%\to71\%\to41\%.
\]

Correlation allows samples to be concentrated into a small number of attribute combinations, with certain patterns having very few people. Although the total N remains unchanged, the "effective sample size" that distinguishes a specific q-vector decreases.

## sample size compensation

Fixed \(\rho=.25\):

\[
41\%\to76\%\to95\%.
\]

Expanding N can partially compensate for attribute class imbalance.

## Difference between table title and table header

The title of Table 3 is written as \(N=500,1000,2000,4000\), but the actual header and data are only listed as \(1000,2000,4000\). The text also does not provide the three frequencies of \(N=500\). This topic does not make up missing columns.

## Empirical reminder of sample size

Discuss some suggestions

\[
N\ge30\times2^K,
\]

This means that on average there are about 30 people per attribute profile. When attributes are unevenly distributed, averages can mask rare patterns; a more reasonable check is

\[
Np_{\min}
\]

and the actual number of master/non-master groups most relevant to each q-vector.
