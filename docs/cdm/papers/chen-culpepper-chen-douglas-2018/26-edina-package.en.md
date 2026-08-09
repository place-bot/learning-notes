# Current `edina` package code intensive reading

## Package positioning

[`tmsalab/edina`](https://github.com/tmsalab/edina) Encapsulate the method in this article into an R package. The current `DESCRIPTION` is 0.1.2, and the core entry is:

```r
fit = edina(data, k = 3, burnin = 10000, chain_length = 20000)
```

Also available:

```r
auto_edina(data, k = 2:4)
```

Used to fit multiple attribute numbers in sequence.

## Which original algorithm is retained in the current package?

`src/edina.cpp` only exports:

```cpp
edina_Gibbs_Q(...)
check_identifiability(...)
```

The current package master estimator corresponds to the **restricted Gibbs** of the paper. MH and Unconstrained Gibbs in the original supplementary material did not become the user interface.

## File structure

|path|function|
| --- | --- |
| `R/edina.R` |Parameter checking, calling C++, constructing and printing objects|
| `R/auto-edina.R` |Loop fitting of multiple \(K\)|
| `R/model-selection.R` | BIC、DIC、PPP |
| `R/q-matrix.R` |Q objects, formatting, identifiable markup|
| `R/vis-*.R` |Q heat map and model comparison chart|
| `src/edina.cpp` |Rcpp export thin package|
| `inst/include/edina_meat.h` |Main C++ algorithms|

## Improvements over the original supplementary code

### The semantics of retaining the number of samples are clearer

Current C++ usage

\[
\text{iter\_total}
=
\text{burnin}+\text{chain\_length}.
\]

`chain_length` represents the number of retained samples. The original code treats this as the total number of iterations and retains `chain_length-burnin` samples.

### Do not save the entire Q cube

Cumulative current implementation

\[
\overline Q
=
\frac1M\sum_{m=1}^{M}Q^{(m)},
\]

Reduce the memory of \(J\times K\times M\).

### Add model diagnosis

Each iteration of the simulation copy data is retained, and the odds ratio of the item pair is compared to form the posterior prediction probability; at the same time, the marginal log likelihood is accumulated for BIC and DIC.

### Add objects and visualizations

Returns a `edina` object, containing:

-Mean and standard deviation of item parameters;
- latent class proportion;
- `avg_q` and `est_q`;
- Amounts required for BIC, DIC and PPP;
- Running time and data names.

## An important summary change

Current code setup:

```cpp
Qest = conv_to<mat>::from(Q_summed > .5);
```

That is, element-wise majority voting. The original paper and the original supplementary code use the full Q posterior mode after removing column permutations.

An element-wise majority vote may leave \(\mathcal Q\). Currently `new_edina()` only formats `est_q` without forcing another check; and the complete Q sample is not saved. After the fitting is completed, the entire matrix mode of the original paper cannot be restored from the object.

Recommended software level:

1. Do `check_identifiability()` for `est_q`;
2. Keep the standard Q encoding frequency, or maintain top modes online;
3. If the majority vote is illegal, project it back to \(\mathcal Q\);
4. Provide both Q-mode and element-wise inclusion probabilities in the output.

## Input boundary

The R layer checks that `data` is a matrix, \(k\) and the chain length is an integer, but there is no explicit check for the current entry:

- Data only contains 0/1;
- missing values;
- \(J\) is sufficient to support the given \(K\);
- `burnin` and `chain_length` are positive;
- Recognizable space is not empty.

Use unsigned integers within `random_Q()` to calculate \(J-2K\). In practice, it should be ensured that at least

\[
J\ge2K+1.
\]

## An interface problem in current 0.1.2

`auto_edina()` Save the criterion matrix as:

```r
criterions
```

And `best_model.auto_edina()` currently reads:

```r
x$criterion[, ic]
```

Field is missing the end `s`. According to the current source code, this helper function will fail because the field does not exist. Just read `x$criterions` directly or correct the field name. This conclusion comes from the current warehouse code review and has nothing to do with the 2018 paper algorithm.

## The boundary between paper results and software extensions

BIC, DIC, PPP, `auto_edina()`, Q-heatmap, and element-wise threshold summaries were not present in the experiments of the 2018 paper. The software version should be referenced when using these features and their statistics and implementation behavior should be independently verified.

[Next page: This site’s computable verification and code review found](27-computational-check.md)
