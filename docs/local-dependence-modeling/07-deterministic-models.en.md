# Deterministic LD: boundary mixtures, SLD, and KST-IRT

Deterministic LD starts from \(\mathcal K\subsetneq2^Q\). The final model is stochastic; the word
“deterministic” refers only to the latent support restriction.

## Mixtures of structures

Boundary-mixture models combine a power-set component and a restricted component:

\[
P_t(X\mid\theta)
=(1-\delta_t)P_{2^Q}(X\mid\theta)
+\delta_tP_{\mathcal K}(X\mid\theta).
\tag{33}
\]

The restricted component occupies the boundary of the probability space and may assign structural
zeroes to discordant patterns.

## Surface local dependence

SLD can be expressed as response copying:

- with probability \(1-\pi_{LD}\), item \(i'\) follows its own IRF;
- with probability \(\pi_{LD}\), \(X_{i'}=X_i\).

Thus

\[
P^*(X_{i'}=1\mid\theta)
=(1-\pi_{LD})P(X_{i'}=1\mid\theta)
+\pi_{LD}P^*(X_i=1\mid\theta).
\tag{36}
\]

If both independent success probabilities are .5,

\[
P_{00}=P_{11}=\frac{1+\pi_{LD}}4,
\qquad
P_{01}=P_{10}=\frac{1-\pi_{LD}}4.
\]

A moderate mixture weight can therefore sharply reduce discordant cells, whereas a continuous ULD
factor may need extreme loadings to approximate the same table.

## Two-process KST-IRT

\[
P(\boldsymbol X=\boldsymbol x\mid\theta)
=\sum_{K\in\mathcal K}P(\boldsymbol X=\boldsymbol x\mid K)\pi(K\mid\theta).
\]

The SRF assigns probability to allowable mastery states. A \(g\)-matrix maps those states to the full
observed response space. For \(\mathcal K_A=\{00,10,11\}\), observing \(01\) from latent state
\(10\) requires a slip on item 1 and a guess on item 2, with probability containing
\(\beta_1\eta_2\). Structural exclusion at the mastery level is therefore compatible with noisy data.

Probabilistic IRT models could define a \((2^Q,2^Q)\) \(g\)-process. They usually omit it because
latent and observed responses are identified, making the mapping an identity. The 4PL admits a
nontrivial \(g\)-process interpretation.

