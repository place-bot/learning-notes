# New model directions and conclusions

Section 3.2.3 identifies unoccupied cells in the taxonomy rather than presenting three fully estimated
new models.

## Three extensions

### Multidimensional SRFs on any support

ULD acts on \(\pi(K\mid\Theta)\), whereas deterministic versus probabilistic LD is determined by
the support. One can therefore combine

\[
\mathcal K\subsetneq2^Q
\quad\text{and}\quad
\pi(K\mid\theta,u_t).
\]

The extra trait redistributes probability among allowable states without restoring forbidden ones.

### Probabilistic interactions inside a deterministic structure

RD-, OD-, or CD-like constraints can be applied to the SRF on restricted support:

\[
\pi(K\mid\theta)\propto
\exp\{f_{base}(K,\theta)+\gamma h(K)\},
\qquad K\in\mathcal K,
\]

while \(\pi(K\mid\theta)=0\) outside \(\mathcal K\). Structural and probabilistic mechanisms are
complementary.

### Ability-dependent error processes

Replace fixed error rates by

\[
\eta_i(\theta)=\frac1{1+\exp(\widetilde\eta_i-\theta)},
\qquad
\beta_i(\theta)=\frac1{1+\exp(\theta-\widetilde\beta_i)}.
\]

Higher-ability people can succeed more often without full modeled mastery and slip less often. This
breaks \(X\perp\theta\mid K\) and raises additional interpretation and identifiability questions.

## Final synthesis

The taxonomy uses two primitives--structure and process--and two operations--factorization and
reparameterization. Probabilistic LD keeps \(2^Q\) and models dependence within the SRF.
Deterministic LD uses \(\mathcal K\subsetneq2^Q\) and a \(g\)-process to recover observed
violations. The mechanisms can coexist.

| Model | Mechanism in the taxonomy |
| --- | --- |
| RD | Chain-rule factorization plus links for marginal and conditional probabilities |
| OD/CD | Direct joint softmax reparameterization |
| Locally dependent latent-trait model | Higher-order log-linear SRF interactions |
| Bahadur/copula | Joint dependence designed to preserve margins |
| SLD/boundary mixture | Mixture containing restricted-support components |
| KST-IRT | Explicit structure, SRF, and \(g\)-process |

## Four practical advantages

1. Choose restricted support only when structural zeroes are substantively defensible.
2. Understand why a direct-copy or boundary mechanism can generate stronger association than moderate
   continuous ULD parameters.
3. Avoid forcing slopes or interactions toward infinity merely to approximate structural zeroes, while
   acknowledging the added \(g\)-process parameters.
4. Treat PCM as the chain case of a more general item-level structural approach to testlets.

The paper leaves identifiability, estimation, simulation comparisons, new model construction, and
applied KST-IRT validation for future work. Its deliverable is a design language, not a turnkey fitting
algorithm.

