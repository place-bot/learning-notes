# Three estimated routes

## Joint Maximum Likelihood

Joint maximum likelihood simultaneous optimization:

\[
\boldsymbol\beta
=(g_1,s_1,\ldots,g_J,s_J)
\]

and a discrete attribute profile for each student

\[
\boldsymbol\alpha_1,\ldots,\boldsymbol\alpha_I.
\]

The goal is conditional likelihood

\[
L(X\mid\boldsymbol\alpha)
=
\prod_i
L(\boldsymbol X_i\mid\boldsymbol\alpha_i).
\]

The paper points out that student attribute profiles belong to incidental parameters that increase as sample size increases. Similar to traditional IRT's JML, joint estimation may lead to inconsistencies in the structural parameters \(\widehat{\boldsymbol\beta}\).

## Marginal Maximum Likelihood and EM

Marginal maximum likelihood integrates the attribute profile:

\[
L(X)
=
\prod_i
\sum_l
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
\pi_l.
\]

Because the attribute distribution is discrete, the integration becomes the sum of \(2^K\) patterns.

EM alternation:

- Step E: Calculate the posterior probability that each student belongs to each attribute profile;
- Step M: Update \(g_j,s_j\) with the posterior expectation count.

The Appendix provides a complete derivation of this route.

## Saturated attribute distribution

If each attribute profile is given an independent probability:

\[
\boldsymbol\pi=(\pi_1,\ldots,\pi_{2^K}),
\qquad
\sum_l\pi_l=1,
\]

The number of free parameters is

\[
2^K-1.
\]

It can represent arbitrary attribute dependencies, but both computation and storage increase exponentially with \(K\).

The EM of this article uses fixed \(\pi_l\). The Discussion section proposes that the mode scale can be updated using empirical Bayes at each iteration.

## HO-DINA AND MCMC

HO-DINA uses a continuous higher-order capability \(\theta_i\) to explain inter-attribute dependencies:

\[
P(\alpha_{ik}=1\mid\theta_i)
=
\operatorname{logit}^{-1}
(\lambda_{0k}+\lambda_1\theta_i),
\qquad
\theta_i\sim N(0,1).
\]

The attribute distribution decreases from \(2^K-1\) free mode probability to:

\[
K\text{intercept}+1\text{common slope}.
\]

The paper states that the model is estimated using MCMC and points sampler details to de la Torre and Douglas (2004).

## Comparison of three routes

|route|attribute profile processing|Advantages|main cost|
| --- | --- | --- | --- |
| JML |Each person directly estimates a model|concept straightforward|incidental parameter problem|
| MML + EM |Summing \(2^K\) patterns|Appendix has closed M-step|Exponential number of categories|
| HO-DINA + MCMC |Use \(\theta\) to generate related attributes|The number of parameters increases linearly with \(K\)|Adding higher-order structural assumptions; sampling details in another paper|

## There are two differences when comparing real data.

The paper emphasizes that the results of DINA-EM and HO-DINA-MCMC do not need to be identical item by item:

1. DINA uses saturated multinomial attribute distribution, and HO-DINA uses high-order capability constraints;
2. DINA reports the likelihood mode/maximum value, and HO-DINA reports the posterior mean.

So Table 4 compares both the latent variable structure and the point estimation criterion.
