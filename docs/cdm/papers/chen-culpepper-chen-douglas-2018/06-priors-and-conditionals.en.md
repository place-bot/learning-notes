# Priori and complete conditional distribution of each layer

## Attribute ratio \(\boldsymbol\pi\)

A priori is

\[
\boldsymbol\pi\sim
\operatorname{Dirichlet}(\delta_{01},\ldots,\delta_{0C}).
\]

If the current attribute class count is

\[
n_c=\sum_{i=1}^{N}
I(\boldsymbol\alpha_i=\boldsymbol a_c),
\]

The conjugate update is

\[
\boldsymbol\pi\mid\boldsymbol\alpha
\sim
\operatorname{Dirichlet}
(\delta_{01}+n_1,\ldots,\delta_{0C}+n_C).
\]

The author's code uses \(\delta_{0c}=1\).

## Student attributes \(\boldsymbol\alpha_i\)

Calculate for each candidate class \(c\)

\[
w_{ic}
=
\pi_c
\prod_{j=1}^{J}
p(Y_{ij}=y_{ij}\mid
\boldsymbol a_c,s_j,g_j,\boldsymbol q_j).
\]

After normalization

\[
P(\boldsymbol\alpha_i=\boldsymbol a_c\mid-)
=
\frac{w_{ic}}{\sum_{d=1}^{C}w_{id}}.
\]

The original C++ `parm_update_nomiss()` loops through all \(2^K\) classes for each student, computes `pYit()`, and does another categorical sampling.

## Guess rate \(g_j\)

Given the current ideal response, suppose not all of them are in the group:

\[
G_j
=
\sum_i I(\eta_{ij}=0,Y_{ij}=1),
\]

\[
F_j
=
\sum_i I(\eta_{ij}=0,Y_{ij}=0).
\]

When monotonic truncation is ignored,

\[
g_j\mid-\sim
\operatorname{Beta}
(\alpha_g+G_j,\beta_g+F_j).
\]

Due to the requirement \(g_j<1-s_j\), the actual complete conditional distribution is truncated at

\[
[0,1-s_j).
\]

The code first calculates Beta CDF

\[
u_{\max}
=
F_{\text{Beta}}(1-s_j;
\alpha_g+G_j,\beta_g+F_j),
\]

Then draw \(u\sim U(0,u_{\max})\), and finally use the Beta quantile function to get \(g_j\).

## Error rate \(s_j\)

In the omnipotent group, let

\[
S_j
=
\sum_i I(\eta_{ij}=1,Y_{ij}=0),
\]

\[
C_j
=
\sum_i I(\eta_{ij}=1,Y_{ij}=1).
\]

When truncation is ignored,

\[
s_j\mid-\sim
\operatorname{Beta}
(\alpha_s+S_j,\beta_s+C_j).
\]

Under the updated \(g_j\), truncate the distribution to

\[
[0,1-g_j).
\]

## Complete conditions for Q

\[
p(Q\mid
\boldsymbol Y,\boldsymbol\alpha,\boldsymbol s,\boldsymbol g)
\propto
p(\boldsymbol Y\mid
\boldsymbol\alpha,\boldsymbol s,\boldsymbol g,Q)
I(Q\in\mathcal Q).
\]

The prior on Q is constant in the legal space, so the posterior ratio between legal candidates is completely determined by the conditional likelihood.

## The location of hyperparameter in the paper and code

text handle

\[
\boldsymbol\delta_0,\quad
\alpha_s,\beta_s,\alpha_g,\beta_g
\]

Reserved as a general hyperparameter. Additional C++ fixes:

\[
\delta_{0c}=1,\qquad
\alpha_s=\beta_s=\alpha_g=\beta_g=1.
\]

This makes both the latent class proportions and the untruncated item parameters prior uniform priors. This set of implementation choices should be documented when reproducing the original text.

## Conditional relationships brought about by the update sequence

The code first truncates \(g_j\) according to the old \(s_j\), and then truncates \(s_j\) according to the new \(g_j\). Both constitute a Gibbs update of the joint truncated beta density. Satisfied every step of the way

\[
0\le g_j<1-s_j\le1.
\]

[Next page: Three identifiable conditions for Q](07-identifiability-conditions.md)
