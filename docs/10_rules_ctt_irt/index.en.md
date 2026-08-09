# CTT vs IRT Top Ten Rules Overview

About this chapter

This chapter systematically compares the ten core differences between Classical Measurement Theory (CTT) and Item Response Theory (IRT). Each rule contains a complete derivation process and example analysis.

## Rule overview table

|rules|CTT perspective|IRT perspective|core formula|
| --- | --- | --- | --- |
|[Rule 1](rule01_measurement_error.md)|standard errorconstant|standard error varies from person to person| \(SE_{CTT} = \sigma\sqrt{1-r_{tt}}\) vs \(SE_{IRT}(\theta) = \frac{1}{\sqrt{I(\theta)}}\) |
|[Rule 2](rule02_test_length.md)|The longer the better|Quality over quantity| Spearman-Brown: \(r_{nn} = \frac{nr_{tt}}{1+(n-1)r_{tt}}\) |
|[Rule 3](rule03_test_forms.md)|Need parallel testing|Personalized Optimal|Parallel conditions vs adaptive algorithms|
|[Rule 4](rule04_item_properties.md)|sample dependency|Sample irrelevant| \(p = \int P(\theta)g(\theta)d\theta\) vs \(P(\theta) = \frac{e^{\theta-b}}{1+e^{\theta-b}}\) |
|[Rule 5](rule05_score_meaning.md)|norm reference|item reference|Percentile vs ability-item distance|
|[Rule 6](rule06_interval_scale.md)|by normalization|by model|Nonlinear transformation vs logit linearity|
|[Rule 7](rule07_mixed_formats.md)|weight imbalance|optimal combination|Implicit weights vs GPCM|
|[Rule 8](rule08_change_scores.md)|initial value dependence|Comparable| \(r_{DD} = f(r_{12})\) vs MRMLC |
|[Rule 9](rule09_factor_analysis.md)|Phi related questions|full information approach| \(\phi_{max} < 1\) vs M2PL |
|[Rule 10](rule10_item_features.md)|Features are not important|Features can be modeled|Black box vs LLTM|

## Theoretical Framework

### CTT Basics

CTT core model:

\[
X = T + E
\]

Key assumptions:

1. \(E(E) = 0\)
2. \(\operatorname{Cov}(T,E) = 0\)
3. Error is the same for everyone

### IRT Basics

IRT core model (Rasch):

\[
P(\theta) = \frac{e^{\theta-b}}{1+e^{\theta-b}}
\]

Key features:

1. Probabilistic modeling
2. individualized accuracy
3. Parameter separation

## Quick navigation

### If you care about measurement accuracy

- [Rule 1: Measure standard error](rule01_measurement_error.md)
- [Rule 2: test length and reliability](rule02_test_length.md)

### If you care about quiz development

- [Rule 3: Interchangeable Quiz Form](rule03_test_forms.md)
- [Rule 4: item attribute estimate](rule04_item_properties.md)
- [Rule 10: item stimulus characteristics](rule10_item_features.md)

### If you care about fraction interpretation

- [Rule 5: The meaning of scores](rule05_score_meaning.md)
- [Rule 6: Interval scale attribute](rule06_interval_scale.md)
- [Rule 8: Change score](rule08_change_scores.md)

### If you care about advanced analytics

- [Rule 7: Mixed item format](rule07_mixed_formats.md)
- [Rule 9: Binary item factor analysis](rule09_factor_analysis.md)

## Symbol Conventions

|symbol|meaning|
| --- | --- |
| \(X\) |Observation score|
| \(T\) |true fraction|
| \(E\) |measurement error|
| \(\theta\) |IRT ability parameter|
| \(b\) |IRT difficulty parameter|
| \(P(\theta)\) |response probability function|
| \(I(\theta)\) |information function|
| \(r_{tt}\) |reliability coefficient|
| \(SE\) |standard error|

## References

Core literature:

- Gulliksen, H. (1950). *Theory of mental tests*.
- Lord, F. M., & Novick, M. R. (1968). *Statistical theories of mental test scores*.
- Rasch, G. (1960). *Probabilistic models for some intelligence and attainment tests*.
- Embretson, S. E., & Reise, S. P. (2000). *Item response theory for psychologists*.

## Study suggestions

1. Sequential learning: Follow the order of rules 1-10 to understand the evolution from CTT to IRT.
2. Contrastive learning: Each rule compares CTT and IRT methods.
3. Focus on derivation: focus on understanding the derivation process of each formula.
4. Example verification: Deepen understanding through numerical examples.

For readers:

- Have basic statistical foundation
- Familiar with basic concepts of probability theory
- Researchers interested in psychometrics

The content of this chapter is based on Chapter 2 of Embretson & Reise (2000).
