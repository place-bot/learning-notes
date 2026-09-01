# Local Dependence Modeling

This section is a complete guided reading of Noventa, Spoto, Heller, and Kelava's (2026)
*On the Modeling of Local Dependence*. The paper does not propose one more LD index. Instead, it
builds a common language for local-dependence models from item response theory (IRT), knowledge
space theory (KST), and cognitive diagnostic assessment (CDA).

## Paper information

| Field | Information |
| --- | --- |
| Paper | Stefano Noventa, Andrea Spoto, Jurgen Heller, & Augustin Kelava. *On the Modeling of Local Dependence*. |
| Journal | *Psychometrika*, 91, 1020--1047, 2026 |
| DOI | [10.1017/psy.2026.10099](https://doi.org/10.1017/psy.2026.10099) |
| License | CC BY 4.0 |
| Scope | Categorical responses in IRT, KST, and CDA; continuous-response factor analysis is outside the direct scope |

## The framework in one equation

\[
P(\boldsymbol X=\boldsymbol x\mid\Theta)
=
\sum_{K\in\mathcal K}
\underbrace{P(\boldsymbol X=\boldsymbol x\mid K,\Theta)}_{g\text{-process}}
\underbrace{\pi(K\mid\Theta)}_{p\text{-process / SRF}}.
\]

| Layer | Question |
| --- | --- |
| Structure \(\mathcal K\) | Which latent states are possible in principle? |
| \(p\)-process / SRF | Given ability or attributes, how likely is each latent state? |
| \(g\)-process | Given a latent state, how do guessing and slipping generate an observed response? |

The main distinction is:

\[
\boxed{\mathcal K=2^Q:\ \text{probabilistic LD}}
\qquad
\boxed{\mathcal K\subsetneq2^Q:\ \text{deterministic LD}}.
\]

Probabilistic LD retains every response pattern and changes their probabilities. Deterministic LD
removes patterns from the latent support and uses a \(g\)-process when structurally prohibited patterns
nevertheless appear in observed data.

## Reading route

1. [Research question, terminology, and contribution](01-question-terms-contribution.md)
2. [Local independence and contingency tables](02-local-independence-tables.md)
3. [Structures, states, and processes](03-structures-and-processes.md)
4. [Unified framework and two taxonomies](04-unified-taxonomy.md)
5. [Probabilistic LD I: ULD, testlets, and RD](05-probabilistic-uld-rd.md)
6. [Probabilistic LD II: OD, CD, Bahadur, and copulas](06-probabilistic-joint-models.md)
7. [Deterministic LD: boundary mixtures, SLD, and KST-IRT](07-deterministic-models.md)
8. [Numerical comparisons](08-numerical-comparisons.md)
9. [Parameter interpretation and identifiability](09-interpretation-identifiability.md)
10. [Polytomous items, testlets, and knowledge structures](10-polytomous-testlets.md)
11. [New model directions and conclusions](11-new-models-conclusions.md)
12. [Appendices](12-appendices.md)
13. [Symbols and abbreviations](symbols.md)
14. [References](references.md)

The paper delivers a taxonomy and a model-design language. It does not deliver a complete structure-
learning algorithm; identifiability, estimation, model comparison, and applied validation remain open.

