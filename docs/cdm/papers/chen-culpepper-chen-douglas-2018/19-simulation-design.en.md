#Experiment: Analog Design

## Factor design

Simulate crossing the following conditions:

|factors|level|
| --- | --- |
|sample size \(N\)| 500、1000、2000、4000 |
|Number of attributes \(K\)| 3、4 |
|Property related \(\rho\)| 0、0.05、0.15、0.25 |
|Repeat for each condition| 100 |

total

\[
4\times2\times4\times100
=
3200
\]

data sets, each of which fits three MCMC methods.

## attribute profile generation

When \(\rho=0\), it is generated uniformly from \(2^K\) patterns.

When \(\rho>0\), first generate

\[
\boldsymbol\theta_i
\sim
N(\boldsymbol0,\Sigma),
\]

Among them

\[
\Sigma
=(1-\rho)I_K+\rho\boldsymbol1\boldsymbol1^{\mathsf T},
\]

Binarization again:

\[
\alpha_{ik}
=
I(\theta_{ik}\ge0).
\]

The marginal mastery rate for each attribute is 0.5, and dependence is introduced by potential normal correlation.

## \(K=3\)’s true Q

There are total \(J=18\) questions:

- \((100),(010),(001)\) repeated 3 times each;
- \((110),(101),(011)\) repeated 2 times each;
- \((111)\) repeated 3 times.

## \(K=4\)’s true Q

There is also the question \(J=18\):

- Each of the four unit vectors is repeated 2 times;
- Each of the six two-attribute combinations appears once;
- Each of the four three-attribute combinations appears once.

Both Qs satisfy the discernible constraints of the paper.

## Comparison method

|Abbreviation|method|Q Update|
| --- | --- | --- |
| MH |This article is restricted to Metropolis| DS2，\(B=2K\) |
| CGibbs |This article is restricted Gibbs|Update each element sequentially|
| Gibbs | Chung（2014） |Unconstrained Gibbs|

## MCMC settings

Each fit:

\[
\text{chain length}=30{,}000,
\qquad
\text{burn-in}=15{,}000.
\]

\(s,g,\pi\) draws the initial value from the priori, and Q draws the initial value randomly from \(\mathcal Q\).

## Evaluation indicators

### Restore the entire Q

Satisfied in 100 repetitions

\[
\widehat Q=Q
\]

number of times; attribute column substitution is allowed before comparison.

### Element-wise accuracy

\[
\frac{1}{JK}
\sum_{j=1}^{J}\sum_{k=1}^{K}
I(\widehat q_{jk}=q_{jk}),
\]

A further 100 repetitions were averaged and converted to percentages.

### item parameters MSE

Calculate the mean squared error for \(\widehat s_j\) and \(\widehat g_j\) respectively. The original text is shown in Figures 1--2 by item q-vector.

## Reproducibility gap

The text does not report the specific generated values or distribution of the true \(s_j,g_j\) in the simulation; the public R file only reproduces the empirical analysis, and the public C++ provides `sim_Y_dina()`, without attaching the complete simulation driver script and random seeds that generate Table 1 and Figures 1--2.

Therefore, design factors, Q, chain settings, and table results can be accurately reviewed, and all simulation data cannot be reconstructed bit by bit from the accompanying material alone.

[Next page: Experiment——All results of Table 1](20-table1-results.md)
