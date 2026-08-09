# Complete Bayesian hierarchical model

## Five layers of unknown quantities

Paper joint estimate:

\[
\Theta
=
\left(
Q,\boldsymbol s,\boldsymbol g,
\boldsymbol\alpha,\boldsymbol\pi
\right).
\]

The hierarchical structure is as follows:

```text
π ──> α_i ──┐
             ├──> η_ij(Q, α_i) ──> Y_ij
Q ──────────┘                    ↑
                         (s_j, g_j)
```

## Answer layer

\[
Y_{ij}\mid
\boldsymbol\alpha_i,s_j,g_j,\boldsymbol q_j
\sim
\operatorname{Bernoulli}
\left(
(1-s_j)^{\eta_{ij}}g_j^{1-\eta_{ij}}
\right).
\]

## attribute profile layer

\[
P(\boldsymbol\alpha_i=\boldsymbol a_c\mid\boldsymbol\pi)
=\pi_c.
\]

Students are conditionally independent, and the answers of the same student are conditionally independent after given attributes and item parameters.

##Latent class scale layer

\[
\boldsymbol\pi
\sim
\operatorname{Dirichlet}(\boldsymbol\delta_0).
\]

Supplementary code usage

\[
\boldsymbol\delta_0=\boldsymbol1_{2^K},
\]

That is, the Dirichlet prior on simplex uniformity.

## item parameters layer

For each question,

\[
p(s_j,g_j)
\propto
s_j^{\alpha_s-1}(1-s_j)^{\beta_s-1}
g_j^{\alpha_g-1}(1-g_j)^{\beta_g-1}
I(0\le g_j<1-s_j\le1).
\]

Supplementary code sets all four Beta hyperparameters to 1 and maintains them through truncated sampling

\[
g_j<1-s_j.
\]

## Q layer

\[
p(Q)\propto I(Q\in\mathcal Q).
\]

This is equivalent to using a uniform prior on the finite identifiable set \(\mathcal Q\). The prior probability of Q outside the set is 0.

## Joint Posterior

Ignore the normalization constant:

\[
\begin{aligned}
p(&Q,\boldsymbol s,\boldsymbol g,
\boldsymbol\alpha,\boldsymbol\pi\mid\boldsymbol Y)
\propto
\prod_{i=1}^{N}\prod_{j=1}^{J}
p(Y_{ij}\mid
\boldsymbol\alpha_i,s_j,g_j,\boldsymbol q_j)\\
&\times
\prod_{i=1}^{N}\pi_{c(i)}
\times
p(\boldsymbol\pi)
\times
\prod_{j=1}^{J}p(s_j,g_j)
\times
I(Q\in\mathcal Q),
\end{aligned}
\]

Among them, \(c(i)\) is the attribute class to which student \(i\) currently belongs.

## One round of MCMC dependencies

The MH version of the paper is in the following order:

\[
\boldsymbol g^{(t)}
\leftarrow
p(\boldsymbol g\mid
\boldsymbol Y,\boldsymbol s^{(t-1)},
\boldsymbol\alpha^{(t-1)},Q^{(t-1)}),
\]

\[
\boldsymbol s^{(t)}
\leftarrow
p(\boldsymbol s\mid
\boldsymbol Y,\boldsymbol g^{(t)},
\boldsymbol\alpha^{(t-1)},Q^{(t-1)}),
\]

\[
\boldsymbol\alpha^{(t)}
\leftarrow
p(\boldsymbol\alpha\mid
\boldsymbol Y,\boldsymbol s^{(t)},\boldsymbol g^{(t)},
\boldsymbol\pi^{(t-1)},Q^{(t-1)}),
\]

\[
\boldsymbol\pi^{(t)}
\leftarrow
p(\boldsymbol\pi\mid\boldsymbol\alpha^{(t)}),
\]

\[
Q^{(t)}
\leftarrow
\text{MH}\{p(Q\mid
\boldsymbol Y,\boldsymbol s^{(t)},\boldsymbol g^{(t)},
\boldsymbol\alpha^{(t)})\}.
\]

Restricted Gibbs only replaces the last step.

## Q Update why condition to current attribute sample

Once \(\boldsymbol\alpha\) has been sampled, the conditional posterior for Q no longer needs to be summed over \(2^K\) classes. For a candidate that changes only a small number of q elements, the likelihood ratio only involves the items whose ideal response has changed, and the code can calculate it locally.

[Next page: Priori and complete conditional distribution of each layer](06-priors-and-conditionals.md)
