# Unified framework and two taxonomies

## Table 1: assessment models by process composition

| \(g\)-process | No \(p\)-process | \(p\)-process present |
| --- | --- | --- |
| None | Complete or incomplete contingency tables | Traditional latent-class/CDA/IRT models |
| Competence-independent | Basic probabilistic KST | KST-CDA and KST-IRT with fixed guessing/slipping |
| Competence-dependent | Mixture models without a \(p\)-process | The most general, rarely used family |

The common equations are

\[
P(X)=\sum_CP(X\mid C)\nu(C) \quad\text{(CDA)},
\]

\[
P(X)=\int P(X\mid\theta)f(\theta)d\theta \quad\text{(IRT)},
\]

and

\[
P(X\mid\theta)=\sum_{K\in\mathcal K}P(X\mid K)\pi(K\mid\theta)
\tag{19}
\]

for KST-IRT. The state response function \(\pi(K\mid\theta)\) generalizes a one-item IRF to an
entire collection of items.

## BLIM, Theta-BLIM, and GLI

BLIM factorizes the \(g\)-process:

\[
P(\boldsymbol X\mid K)
=\prod_iP(X_i=1\mid K)^{X_i}P(X_i=0\mid K)^{1-X_i},
\tag{20}
\]

with lucky-guess \(\eta_i\) and careless-error \(\beta_i\). Theta-BLIM adds
\(\pi(K\mid\theta)\) but leaves its form unspecified.

Generalized local independence factorizes the SRF as

\[
\pi(K\mid\theta)
=\prod_{q_i\in K}\pi(K_i=1\mid\theta)
\prod_{q_i\in K^O}\pi(K_i=0\mid\theta),
\tag{21}
\]

where \(K^O\) contains only items that can legally be added to \(K\) in one step. For
\(\mathcal K=2^Q\), \(K^O=Q\setminus K\) and GLI reduces to ordinary LI. Equation (21) is
directly limited to learning spaces that support one-item additions.

## Theta-SLM and LKS

The latent-trait version of (21) is the Theta-Simple Learning Model, a template for sequential models.
A log-link/softmax reparameterization gives the Logistic Knowledge Structure:

\[
\pi(K\mid\theta)
=\frac{\exp[\sum_{q_i\in K}(\theta-b_i)]}
{\sum_{L\in\mathcal K}\exp[\sum_{q_i\in L}(\theta-b_i)]}.
\tag{24}
\]

It becomes independent Rasch items on a power set and the partial credit model on a chain.

## Table 2: LD taxonomy

| Support/process | No \(p\) | Nonfactorized \(p\) | GLI-factorized \(p\) |
| --- | --- | --- | --- |
| Probabilistic LD, \(\mathcal K=2^Q\), no \(g\) | Complete table | ULD, RD, OD, CD, log-linear, LND, Bahadur, copula | Strong-LI baseline and multidimensional IRFs |
| Deterministic LD, \(\mathcal K\subsetneq2^Q\), no \(g\) | Incomplete table | SRF constraints on restricted support | Theta-SLM |
| Deterministic LD, fixed \(g\) | Basic probabilistic KST | General KST-IRT and LKS | Sequential KST-IRT |
| Deterministic LD, ability-dependent \(g\) | SLD/boundary mixtures | Ability-dependent-error KST-IRT | Ability-dependent sequential KST-IRT |

Empty cells are research opportunities, not mathematical impossibilities.

