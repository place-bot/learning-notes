# Research question, terminology, and contribution

## Why local dependence matters

Local independence (LI) requires item responses to have no systematic association after conditioning
on the constructs measured by the test. Violations invalidate the usual product likelihood and can bias
item and person parameters. A familiar symptom is slope inflation: repeated evidence from dependent
items is treated as independent information.

## Fragmented terminology

| Term | Meaning in this paper |
| --- | --- |
| SLD | Surface LD caused by similar content, location, shared stimuli, or response copying |
| ULD | Underlying LD caused by an omitted latent construct |
| RD | Response dependence: a later response is conditional on an earlier response |
| Trait dependence | Essentially the same idea as ULD |
| OD | Asymmetric order dependence |
| CD | Symmetric combination dependence for a set of items |

Similar observed tables can come from different mechanisms. RD uses chain-rule factorization; OD
reparameterizes the joint distribution. CD uses a joint interaction; SLD can be represented as a mixture
with a structurally restricted component.

## Dimensionality is not local independence

Items can be locally independent conditional on several traits, and they can be locally dependent in a
unidimensional model. Hence

\[
\text{dimensionality}\neq\text{local independence}.
\]

Unmodeled dimensions are one cause of LD, but direct item effects are another.

## Why fit statistics are not enough

General fit tests can react to LD, misspecified dimensionality, nonmonotonicity, or a misspecified latent
density. Multidimensional IRT and locally dependent unidimensional IRT may also be empirically
indistinguishable. The paper therefore classifies generating mechanisms rather than proposing another
omnibus statistic.

## Two primitives and two operations

The unified view uses:

- **structure**: the collection of allowable states;
- **process**: a conditional-probability relation between structures;
- **factorization**: writing a probability as a product;
- **reparameterization**: assigning a functional form through a link function.

Probabilistic LD uses \(\mathcal K=2^Q\); deterministic LD uses
\(\mathcal K\subsetneq2^Q\). “Deterministic” refers to a support restriction imposed before the
stochastic processes, not to a non-probabilistic final model.

## Four claimed advantages

1. Match model assumptions to whether substantive structural zeros are plausible.
2. Explain why moderate-to-high SLD may require extreme ULD loadings to mimic.
3. Represent structural zeros without inflating slopes, difficulties, or interactions.
4. Unify polytomous items and dependent binary items, then generalize testlets beyond sum-score chains.

