# HO-DINA & MCMC

## Bottleneck of saturated attribute distribution

\(K\) binary attributes are generated

\[
2^K-1
\]

free mode probability:

| \(K\) |Mode number \(2^K\)|free scale parameters|
| ---: | ---: | ---: |
| 5 | 32 | 31 |
| 10 | 1,024 | 1,023 |
| 20 | 1,048,576 | 1,048,575 |

The E-step of EM also requires that all modal posteriors be stored or computed for each student.

## High-level abilities

Introduction of HO-DINA

\[
\theta_i\sim N(0,1),
\]

Interpret it as general ability in a certain field. Given \(\theta_i\), each attribute condition is independent:

\[
P(\boldsymbol\alpha_i\mid\theta_i)
=
\prod_{k=1}^{K}
P(\alpha_{ik}\mid\theta_i).
\]

The probability of attribute mastery is

\[
p_k(\theta_i)
=
P(\alpha_{ik}=1\mid\theta_i)
=
\frac{
\exp(\lambda_{0k}+\lambda_1\theta_i)
}{
1+\exp(\lambda_{0k}+\lambda_1\theta_i)
}.
\tag{18}
\]

The complete Bernoulli probability is written as

\[
P(\boldsymbol\alpha_i\mid\theta_i)
=
\prod_{k=1}^{K}
p_k(\theta_i)^{\alpha_{ik}}
\left[
1-p_k(\theta_i)
\right]^{1-\alpha_{ik}}.
\tag{19}
\]

The original Equation 6 uses the abbreviation of \(P(\alpha_k\mid\theta)\) to express this layer; Equation (19) completes the binary state.

## Parameter reduction

The paper adopts:

- One intercept per attribute \(\lambda_{0k}\);
- All attributes share a positive slope \(\lambda_1>0\).

The total number of attribute distribution parameters is

\[
K+1.
\]

The positive slope ensures that the higher the general ability, the greater the probability of mastering each attribute.

## Why are attributes relevant?

The attributes are independent when the condition is \(\theta\); after marginalizing \(\theta\), they share the same continuous source:

\[
P(\boldsymbol\alpha)
=
\int
P(\boldsymbol\alpha\mid\theta)
\phi(\theta)\,d\theta.
\]

Therefore, there is a positive dependence between attributes.

## Combination with DINA observation layer

HO-DINA only changes the attribute profile distribution. The item response layer is still:

\[
\eta_{ij}
=
\prod_k\alpha_{ik}^{q_{jk}},
\]

\[
P(X_{ij}=1\mid\boldsymbol\alpha_i)
=
g_j^{1-\eta_{ij}}
(1-s_j)^{\eta_{ij}}.
\]

So the "DINA" part of DINA is the same as HO-DINA, the difference is \(P(\boldsymbol\alpha)\).

## MCMC’s role in this article

Thesis description:

- HO-DINA parameters use MCMC;
- The item parameters point is estimated using posterior mean;
- standard error uses posterior standard deviation;
- Reliability evidence from de la Torre and Douglas (2004).

This article does not give:

- Complete conditional distribution;
- a priori hyperparameter;
- chain length, burn-in, thin;
- Convergence diagnostics;
- MCMC pseudocode.

Therefore, this 2009 paper alone cannot reconstruct the original MCMC implementation line by line. Intensive reading of the complete code requires simultaneous entry into the 2004 HO-DINA paper or subsequent public software.

## Modeling Tradeoffs

|Saturated DINA| HO-DINA |
| --- | --- |
|Arbitrary attribute profile distribution|A single higher-order ability induces dependence|
|\(2^K-1\) scale parameters|\(K+1\) high-order parameters|
|Flexible when small \(K\)|More compact when larger \(K\)|
|EM has closed item parameters update|The paper uses MCMC|
|Can represent complex or negative dependencies|Shared positive slopes mainly express forward dependence|

The two item parameters in Table 4 are close, which only shows that the HO constraint is more reasonable for the fractional subtraction data; it does not establish universal equivalence for all CDM data.

## A numerical conditional-profile calculation

At \(\theta=0,\lambda_{01}=-1,\lambda_{02}=0,\lambda_1=1\), the mastery probabilities are .268941 and .5. The conditional profile probabilities for00,01,10,11 are approximately .365529,.365529,.134471,.134471.

These are not population proportions: integrate over the normal ability distribution. A quadrature approximation would use

\[
\pi_l\approx\sum_m v_m\prod_kp_k(\theta_m)^{\alpha_{lk}}
(1-p_k(\theta_m))^{1-\alpha_{lk}},
\]

with normal-integration nodes and weights. This illustrates integration, not the paper's particular MCMC implementation.

The posterior factors as
\(p(X\mid A,g,s,Q)p(A\mid\theta,\lambda)p(\theta)p(\lambda,g,s)\).
A sampler additionally needs priors, constraints, update blocks, proposals, and tuning. The 2009 paper does not uniquely specify them; do not invent missing settings and label them its original algorithm.
