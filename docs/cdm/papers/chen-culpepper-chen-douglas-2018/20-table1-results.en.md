# Experiment: All results of Table 1

## \(K=3\)

Each cell is written as "Number of recovery times for the entire Q/Element-by-element accuracy %".

| \(N\) | \(\rho\) | MH | CGibbs | Gibbs |
| ---: | ---: | ---: | ---: | ---: |
| 500 | 0 | 91 / 95.89 | 95 / 98.22 | 94 / 97.12 |
| 1000 | 0 | 94 / 97.59 | 99 / 99.61 | 95 / 97.93 |
| 2000 | 0 | 96 / 98.52 | 92 / 97.33 | 90 / 95.11 |
| 4000 | 0 | 98 / 99.56 | 88 / 96.33 | 91 / 95.42 |
| 500 | .05 | 87 / 93.25 | 99 / 99.63 | 82 / 92.96 |
| 1000 | .05 | 92 / 94.67 | 99 / 99.64 | 90 / 94.41 |
| 2000 | .05 | 93 / 97.89 | 95 / 98.52 | 90 / 95.18 |
| 4000 | .05 | 94 / 98.78 | 88 / 96.33 | 88 / 95.20 |
| 500 | .15 | 93 / 97.42 | 99 / 99.63 | 91 / 95.44 |
| 1000 | .15 | 95 / 98.51 | 99 / 99.67 | 92 / 95.89 |
| 2000 | .15 | 96 / 99.29 | 95 / 98.10 | 94 / 97.65 |
| 4000 | .15 | 95 / 99.35 | 91 / 97.39 | 89 / 94.04 |
| 500 | .25 | 92 / 98.70 | 99 / 99.98 | 90 / 94.55 |
| 1000 | .25 | 96 / 99.42 | 98 / 99.65 | 94 / 96.20 |
| 2000 | .25 | 96 / 99.92 | 94 / 98.10 | 93 / 95.83 |
| 4000 | .25 | 97 / 99.88 | 89 / 95.57 | 91 / 95.76 |

This site is based on 16 equal weighted averages:

|method|Whole Q recovery rate %|Element-by-element accuracy %|
| --- | ---: | ---: |
| MH | 94.06 | 98.04 |
| CGibbs | 94.94 | 98.36 |
| Gibbs | 90.88 | 95.54 |

## \(K=4\)

| \(N\) | \(\rho\) | MH | CGibbs | Gibbs |
| ---: | ---: | ---: | ---: | ---: |
| 500 | 0 | 60 / 91.42 | 97 / 99.92 | 59 / 89.81 |
| 1000 | 0 | 67 / 93.11 | 91 / 97.29 | 67 / 92.24 |
| 2000 | 0 | 76 / 94.52 | 79 / 94.54 | 73 / 93.96 |
| 4000 | 0 | 87 / 95.50 | 51 / 87.02 | 82 / 95.25 |
| 500 | .05 | 37 / 82.00 | 98 / 99.13 | 40 / 83.39 |
| 1000 | .05 | 52 / 88.57 | 94 / 98.36 | 58 / 89.87 |
| 2000 | .05 | 48 / 88.02 | 90 / 97.44 | 53 / 89.28 |
| 4000 | .05 | 53 / 89.50 | 53 / 89.62 | 51 / 88.94 |
| 500 | .15 | 34 / 81.61 | 96 / 99.43 | 40 / 83.09 |
| 1000 | .15 | 44 / 84.87 | 88 / 96.83 | 60 / 92.00 |
| 2000 | .15 | 55 / 89.13 | 90 / 97.17 | 53 / 88.97 |
| 4000 | .15 | 56 / 89.92 | 74 / 91.64 | 52 / 89.19 |
| 500 | .25 | 35 / 81.78 | 97 / 99.58 | 37 / 82.94 |
| 1000 | .25 | 43 / 84.67 | 96 / 98.57 | 58 / 90.24 |
| 2000 | .25 | 55 / 89.87 | 85 / 95.64 | 54 / 89.80 |
| 4000 | .25 | 55 / 90.09 | 79 / 94.07 | 51 / 89.30 |

This site is based on 16 equal weighted averages:

|method|Whole Q recovery rate %|Element-by-element accuracy %|
| --- | ---: | ---: |
| MH | 53.56 | 88.41 |
| CGibbs | 84.88 | 96.02 |
| Gibbs | 55.50 | 89.27 |

## The most stable result

Across the 12 conditions for \(K=4,\rho>0\), CGibbs had the highest or tied highest number of full-card Q recoveries in every condition. The advantages of small samples are particularly obvious:

\[
N=500,\rho=.25:
\quad
35\ \text{vs.}\ 97\ \text{vs.}\ 37.
\]

## An abnormal trend

CGibbs recovery rate decreases as \(N\) increases under certain conditions. For example \(K=4,\rho=0\):

\[
97,\ 91,\ 79,\ 51.
\]

Statistical consistency does not automatically guarantee that the algorithm error at a fixed 30,000 iterations decreases with \(N\). The posterior becomes sharper with the sample size, and the element-wise chain may be more difficult to cross the pattern; this is a reasonable computational explanation, and the original article did not directly verify it with additional chain length experiments.

## Limited comparison with Chen et al. (2015) \(L_1\)

The original text only gives some figures that can be directly compared. When \(N=500,\rho=0\):

| \(K\) |\(L_1\) recovery| MH | CGibbs | Gibbs |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 38 | 91 | 95 | 94 |
| 4 | 20 | 60 | 97 | 59 |

The author also pointed out that at \(N=2000,4000\), the 2015 \(L_1\) method outperformed the three Bayesian methods in this article. The paper does not list all \(L_1\) numbers side by side in Table 1, so the complete four-method table cannot be reconstructed from this paper.

[Next page: Experiment——item parameters MSE and convergence](21-item-parameter-results.md)
