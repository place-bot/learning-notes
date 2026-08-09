# Theorem 1: A/B/C necessary and sufficient

## 1. Matrix blocking

Condition A allows permutations to be written as

\[
Q=
\begin{pmatrix}
I_K\\
Q^\star
\end{pmatrix}.
\]

Theorem 1 Assertion: In DINA model and

\[
p_{\boldsymbol\alpha}>0
\]

In the parameter space of , the conjunction of the following three terms is

\[
(Q,\boldsymbol s,\boldsymbol g,\boldsymbol p)
\]

Necessary and sufficient conditions for strict joint identification.

## 2. Three conditions

### A: Completeness

\[
Q\ \text{Includes one set}\ I_K.
\]

### B: Column reciprocity

\[
Q^\star_{\cdot k}\ne Q^\star_{\cdot \ell},
\qquad k\ne\ell.
\]

### C: repeated measurements

\[
\sum_{j=1}^{J}q_{jk}\ge3,
\qquad k=1,\ldots,K.
\]

## 3. The reading of “necessary and sufficient”

Adequacy:

\[
A+B+C
\Longrightarrow
\text{All legal parameter points are jointly unique}.
\]

Necessity:

\[
\neg A\ \text{or}\ \neg B\ \text{or}\ \neg C
\Longrightarrow
\text{There exists at least a set of indistinguishable alternatives}.
\]

Necessity does not mean that every parameter point that violates the condition loses universal recognition. The four-question two-attribute example violates C, but is identifiable outside the zero test set.

## 4. Division of labor under three conditions

|Conditions|Eliminate ambiguity|
| --- | --- |
| A |Latent classes cannot be distinguished at the ideal response level|
| B |Two attribute columns carry the same structural code in the non-anchor part|
| C |There are only one or two questions for a single attribute, and item parameters and latent class proportions can be continuously compensated.|

Together they lock three types of objects:

\[
\Gamma(Q)
\longrightarrow Q,
\qquad
\Gamma(Q),\text{reaction distribution}
\longrightarrow
(\boldsymbol s,\boldsymbol g,\boldsymbol p).
\]

## 5. Comparison with the conditions of Chen et al. (2018)

Chen et al.'s Bayesian DINA Q estimate limits the sampling space to:

- Two sets of \(I_K\);
- At least three 1's per column;
- At least one 1 per line.

Theorem 1 of this article allows one set of \(I_K\) to replace the second set of unit arrays with \(Q^\star\) columns. Two sets of \(I_K\) will automatically help column differences and repeated measurements, making it easier to implement an adequate design.

## 6. Direct practical implications

If the test developer wants to jointly learn the entire Q under DINA:

1. Set a single attribute anchor question for each attribute;
2. Arrange different binary codes for each attribute in the remaining questions;
3. Make sure each attribute is required by at least three questions in total.

These three steps are aimed at overall identification. Under limited samples, item discrimination, latent class sparseness, sample size and optimization algorithms still need to be considered.
