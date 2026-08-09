# LLM, G-NIDA and R-RUM

## logit CDM and LLM

The saturated logit CDM is

\[
\operatorname{logit}
\left[P(\boldsymbol\alpha^*_{lj})\right]
=
\lambda_{j0}
+\sum_k\lambda_{jk}\alpha_{lk}
+\sum_{k<k'}\lambda_{jkk'}\alpha_{lk}\alpha_{lk'}
+\cdots.
\]

Remove all interaction terms to get LLM:

\[
\operatorname{logit}
\left[P(\boldsymbol\alpha^*_{lj})\right]
=
\lambda_{j0}
+\sum_{k=1}^{K_j^*}
\lambda_{jk}\alpha_{lk}.
\]

Therefore

\[
P(\boldsymbol\alpha^*_{lj})
=
\frac{
\exp\left(\lambda_{j0}+\sum_k\lambda_{jk}\alpha_{lk}\right)
}{
1+\exp\left(\lambda_{j0}+\sum_k\lambda_{jk}\alpha_{lk}\right)
}.
\]

The property has a multiplicative effect on odds and an additive effect on log-odds.

## NIDA’s attribute layer noise

Traditional NIDA puts guessing and slipping at the attribute level. The success of item requires that each required attribute be successfully executed:

\[
P(\boldsymbol\alpha^*_{lj})
=
\prod_{k=1}^{K_j^*}
g_k^{1-\alpha_{lk}}
(1-s_k)^{\alpha_{lk}}.
\]

The multiplication sign here represents the multiplication of the execution probabilities of each attribute. The traditional form requires the same attribute to be shared on different items \(g_k,s_k\), which is very restrictive.

## G-NIDA

G-NIDA allows parameters to change with items:

\[
P(\boldsymbol\alpha^*_{lj})
=
\prod_{k=1}^{K_j^*}
g_{jk}^{1-\alpha_{lk}}
(1-s_{jk})^{\alpha_{lk}}.
\]

Take the logarithm:

\[
\log P(\boldsymbol\alpha^*_{lj})
=
\sum_k\log g_{jk}
+\sum_k
\alpha_{lk}
\log\frac{1-s_{jk}}{g_{jk}}.
\]

definition

\[
\nu_{j0}=\sum_k\log g_{jk},
\qquad
\nu_{jk}
=
\log\frac{1-s_{jk}}{g_{jk}},
\]

This results in log CDM without interaction.

## R-RUM

R-RUM writing

\[
P(\boldsymbol\alpha_l)
=
\pi_j^*
\prod_{k=1}^{K}
(r_{jk}^*)^{q_{jk}(1-\alpha_{lk})}.
\]

Organize it into a reduced attribute profile and establish parameter mapping with G-NIDA. Therefore, the paper regards R-RUM as another parameterization of G-NIDA and a reduced form of log CDM.

## Substantial differences between the three "additive models"

|model|addition occurs at|Attribute contribution|
| --- | --- | --- |
| A-CDM | \(P\) |Probability increases by a fixed amount|
| LLM | \(\operatorname{logit}(P)\) |log-odds increases by a fixed amount|
| G-NIDA/R-RUM | \(\log P\) |Probability of success multiplied by a fixed multiple|

They all have \(K_j^*+1\) parameters, but usually give different probabilities of success.

## Boundary issues

LLM automatically gives legal probabilities via logistic transformation.

A-CDM to check

\[
0\leq
\delta_{j0}+\sum_k\delta_{jk}\alpha_{lk}
\leq1.
\]

G-NIDA/R-RUM checks that the indexed result does not exceed 1. Modern software will add probabilistic upper and lower bounds and monotonic constraints during optimization.
