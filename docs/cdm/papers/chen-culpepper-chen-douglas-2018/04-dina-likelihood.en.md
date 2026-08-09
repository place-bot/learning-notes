# ideal response, item response function and likelihood

## Probability of correct answer to a single question

DINA divides students into two groups:

\[
P(Y_{ij}=1\mid\eta_{ij}=1)=1-s_j,
\]

\[
P(Y_{ij}=1\mid\eta_{ij}=0)=g_j.
\]

After merging, we get the original formula (2):

\[
P(Y_{ij}=1\mid
\boldsymbol\alpha_i,s_j,g_j,\boldsymbol q_j)
=
(1-s_j)^{\eta_{ij}}g_j^{1-\eta_{ij}}.
\]

If \(\eta_{ij}=1\), the right side is \(1-s_j\); if \(\eta_{ij}=0\), the right side is \(g_j\).

## Bernoulli Probability Mass

Order

\[
p_{ij}
=(1-s_j)^{\eta_{ij}}g_j^{1-\eta_{ij}},
\]

rule

\[
P(Y_{ij}=y_{ij}\mid\cdots)
=
p_{ij}^{y_{ij}}(1-p_{ij})^{1-y_{ij}}.
\]

Expand \(1-p_{ij}\):

\[
1-p_{ij}
=
s_j^{\eta_{ij}}(1-g_j)^{1-\eta_{ij}}.
\]

Therefore, the contribution of a single question is

\[
\left[
(1-s_j)^{\eta_{ij}}g_j^{1-\eta_{ij}}
\right]^{y_{ij}}
\left[
s_j^{\eta_{ij}}(1-g_j)^{1-\eta_{ij}}
\right]^{1-y_{ij}}.
\]

## Complete data likelihood when student attributes are known

Conditioned on \(\boldsymbol\alpha=(\boldsymbol\alpha_1,\ldots,\boldsymbol\alpha_N)^{\mathsf T}\), and using local independence:

\[
\begin{aligned}
p(\boldsymbol Y\mid
\boldsymbol\alpha,\boldsymbol s,\boldsymbol g,Q)
&=
\prod_{i=1}^{N}\prod_{j=1}^{J}
\left[
(1-s_j)^{\eta_{ij}}g_j^{1-\eta_{ij}}
\right]^{y_{ij}}\\
&\quad\times
\left[
s_j^{\eta_{ij}}(1-g_j)^{1-\eta_{ij}}
\right]^{1-y_{ij}}.
\end{aligned}
\]

This is the core quantity used in the MH acceptance rate and element-wise Gibbs conditional probability of Q.

## marginal likelihood

Student attributes are unobservable. For the \(i\) student, score the \(2^K\) attribute profiles:

\[
\begin{aligned}
p(\boldsymbol Y\mid\boldsymbol s,\boldsymbol g,\boldsymbol\pi,Q)
=
\prod_{i=1}^{N}
\sum_{\boldsymbol a_c\in\{0,1\}^K}
\pi_c
\prod_{j=1}^{J}
&\left[
(1-s_j)^{\eta_{cj}}g_j^{1-\eta_{cj}}
\right]^{y_{ij}}\\
\times&
\left[
s_j^{\eta_{cj}}(1-g_j)^{1-\eta_{cj}}
\right]^{1-y_{ij}},
\end{aligned}
\]

Among them

\[
\eta_{cj}
=
I(\boldsymbol a_c^{\mathsf T}\boldsymbol q_j
=
\boldsymbol q_j^{\mathsf T}\boldsymbol q_j).
\]

## Why sample \(\boldsymbol\alpha_i\)

When using marginal likelihood directly, each student contains a summation of \(2^K\) terms. Data augmentation samples each student's attribute profile as a latent variable. Conditional on the current parameters,

\[
P(\boldsymbol\alpha_i=\boldsymbol a_c\mid-)
\propto
\pi_c
\prod_{j=1}^{J}
P(Y_{ij}=y_{ij}\mid
\boldsymbol a_c,s_j,g_j,\boldsymbol q_j).
\]

After normalizing these \(2^K\) weights, a categorical sampling can be performed.

## A two-attribute example

Set a question

\[
\boldsymbol q_j=(1,1)^{\mathsf T},
\qquad
s_j=0.10,\quad g_j=0.20.
\]

The correct answer probabilities for the four attribute profiles are:

| \(\boldsymbol\alpha\) | \(\eta\) |Probability of correct answer|
| --- | ---: | ---: |
| \((0,0)\) | 0 | 0.20 |
| \((1,0)\) | 0 | 0.20 |
| \((0,1)\) | 0 | 0.20 |
| \((1,1)\) | 1 | 0.90 |

DINA only recognizes the two groups "all present" and "at least one missing". The impact of the absence of a specific attribute cannot be distinguished by this question alone; unit rows and multi-question coverage in Q help the global model differentiate between attributes.

[Next page: Complete Bayesian Hierarchical Model](05-bayesian-hierarchy.md)
