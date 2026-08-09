# Model verification, sample size and evidence boundary

## Use S to verify that Q exists

If the existing Q is correct, the DINA assumption holds, and the parameter estimates are consistent, then

\[
\left\|
\boldsymbol\beta
-
T_{\widehat{\boldsymbol c},\widehat{\boldsymbol g}}(Q)
\widehat{\boldsymbol p}
\right\|_2
\xrightarrow{p}0.
\]

Therefore, \(\widehat S(Q)\) is very large and can prompt:

- Q structure error;
- DINA reaction function is inappropriate;
- Local independent failure;
- Parameter estimation failed;
- Limited sample error is large.

S alone cannot determine which source.

## Convergence speed

If

\[
\widehat{\boldsymbol c}-\boldsymbol c
=O_p(N^{-1/2}),
\qquad
\widehat{\boldsymbol g}-\boldsymbol g
=O_p(N^{-1/2}),
\]

The necessary expression for correct Q is

\[
\widehat S(Q)=O_p(N^{-1/2}).
\]

The paper points out that the asymptotic distribution of S depends on the specific form of \((\widehat c,\widehat g)\), and does not give a critical value or p-value that can be used directly.

## sample size empirical formula

The paper was proposed by the result of \(K=5\):

\[
N\ge30\times2^K.
\]

It is 960 for \(K=5\), which is close to \(N=1000\), while the recovery rate in Table 1 rises from 38% for \(N=500\) to 98%.

This is an empirical magnitude inspired by simulations and is suitable for designs where the class is approximately uniform. Experiments with related properties have shown that rare modes further increase the required N.

## No real data experiments

The Simulation part of the full text only generates DINA data, and the Discussion does not include actual measured data analysis. Therefore the paper does not show:

- How content experts interpret data recommendations;
- How to evaluate true Q when it lacks a true value;
- Behavior of S under model misconfiguration;
- Actual improvements in student classification after modifying Q;
- The running time of the real item bank.

## Three-layer output suggestions

Practical applications can simultaneously report:

1. Current Q’s \(\widehat S\);
2. Several near-optimal Qs and their \(\Delta S\);
3. The content expert’s reasons for acceptance or rejection of each q-vector change.

This preserves the structural uncertainty when the target is flat, and is also in line with the paper's recommendation to conduct a substantive review of multiple near-optimal matrices.
