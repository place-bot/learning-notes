# Code implementation intensive reading

## Original implementation in 2011

Thesis report:

- MMLE programs are written in Ox;
- Fractional subtraction data runs in less than 16 seconds;
- MCMI-III data runs less than 20 seconds;
- Computer is 3 GHz Pentium 4;
- Convergence criterion is 0.001.

The text does not give the source code download address, version library or supplementary materials. Therefore line-by-line verification of the original 2011 Ox files is not possible.

## Follow-up official implementation

The current public implementation is

[Wenchao-Ma/GDINA](https://github.com/Wenchao-Ma/GDINA)。

This site is checking submissions on 2026-07-10

[`ac5eca223a1ee32b6c2f595cfeaef9b330451425`](https://github.com/Wenchao-Ma/GDINA/tree/ac5eca223a1ee32b6c2f595cfeaef9b330451425)，

Repository `DESCRIPTION` tag version is 2.12.3. This package was co-developed by Wenchao Ma and Jimmy de la Torre and belongs to the software system formed after the 2011 paper.

## Enter from the user interface

The core entrance is

[`R/GDINA.R`](https://github.com/Wenchao-Ma/GDINA/blob/ac5eca223a1ee32b6c2f595cfeaef9b330451425/R/GDINA.R)。

User provided:

```r
fit <- GDINA(
  dat = dat,
  Q = Q,
  model = "GDINA"
)
```

The same portal supports DINA, DINO, A-CDM, LLM, RRUM, multiple-strategy DINA and subsequent extensions.

## Attribute space and reduction group

[`R/ExportedFuncs.R`](https://github.com/Wenchao-Ma/GDINA/blob/ac5eca223a1ee32b6c2f595cfeaef9b330451425/R/ExportedFuncs.R)
Several functions in directly correspond to the paper symbols:

|function|Thesis object|
| --- | --- |
| `attributepattern()` |All \(\boldsymbol\alpha_l\)|
| `LC2LG()` |Mapping of complete latent classes to reduced groups of items|
| `designmatrix()` | \(M_j\) |
| `att.structure()` |structured attribute space|

`designmatrix()` Generates the design matrix of G-DINA, DINA, DINO, A-CDM, LLM or RRUM based on the model name. LLM and RRUM use the same column structure as A-CDM, and are distinguished by different link functions.

## Single group estimation main loop

[`R/SingleGroup_Estimation.R`](https://github.com/Wenchao-Ma/GDINA/blob/ac5eca223a1ee32b6c2f595cfeaef9b330451425/R/SingleGroup_Estimation.R)
Complete:

1. Data and Q matrix inspection;
2. Complete attribute profile generation;
3. Each item is reduced to latent group and established;
4. Attribute joint distribution initialization;
5. Initialization of design matrix and constraint matrix;
6. Step E `LikNR()`;
7. M step `Mstep()`;
8. Attribute distribution update;
9. Convergence check;
10. Organize probability, effect parameters, posteriori and fitting indicators.

In the code, `Ng` and `Rg` correspond to the expected number of people in the group and the expected number of correct answers respectively.

## M steps

[`R/Mstep.R`](https://github.com/Wenchao-Ma/GDINA/blob/ac5eca223a1ee32b6c2f595cfeaef9b330451425/R/Mstep.R)
Distinguish between two routes.

### Closed update

identity-link G-DINA, DINA, DINO can be used directly:

```r
phat <- Rj / Nj
```

DINA/DINO will first merge the corresponding reduction groups `Rj` and `Nj` according to the design matrix.

### Constrained optimization

A-CDM, LLM, RRUM and user-defined models require numerical optimization. Code provided:

- BFGS；
- augmented Lagrangian；
- `solnp`；
- SLSQP。

The optimization handles both lower and upper bounds on probabilities and monotonic constraints.

The underlying probability calculation and objective function are given by

[`src/Mstep.cpp`](https://github.com/Wenchao-Ma/GDINA/blob/ac5eca223a1ee32b6c2f595cfeaef9b330451425/src/Mstep.cpp)
Rcpp/Armadillo code acceleration in .

## item-level model comparison

[`R/modelcomp.R`](https://github.com/Wenchao-Ma/GDINA/blob/ac5eca223a1ee32b6c2f595cfeaef9b330451425/R/modelcomp.R)
Implementation:

- Wald test；
- likelihood-ratio test；
- Lagrange-multiplier test；
- DINA, DINO, A-CDM, LLM, RRUM comparison;
- Holm, Bonferroni, BH, BY, etc. \(p\) value adjustment;
- Select models by maximum \(p\) value or model simplicity.

The Wald branch directly reads the item success probability and covariance matrix, and then calculates

```r
t(R %*% p) %*%
  ginv(R %*% vcov %*% t(R)) %*%
  (R %*% p)
```

This is consistent with the paper formula (35).

## Simulation tools

[`R/simGDINA.R`](https://github.com/Wenchao-Ma/GDINA/blob/ac5eca223a1ee32b6c2f595cfeaef9b330451425/R/simGDINA.R)
Support:

- Multiple CDMs;
- identity、logit、log link；
- Uniform, categorical, higher-order and other attribute distribution;
- Custom design matrix;
- Monotonic constraints;
- Bipartite and subsequent sequence models.

## Boundary between paper and software

The modern `GDINA` package contains a number of features developed after 2011, such as:

- Multiple sets of estimates;
- sequential G-DINA；
- polytomous attributes；
- Q matrix verification;
- DIF；
- Multiple item/test fits;
- bootstrap SE。

When reading the code, you should separate the "original framework of the paper" and "subsequent software extensions". Version 2.12.3 can verify how the core algorithm is implemented, but it cannot be used as evidence that the 2011 paper was fully functional at the time.

## Teaching implementation on this site

[`tools/de_la_torre_2011_gdina_framework.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/de_la_torre_2011_gdina_framework.py)
Keep the minimum mainline:

```text
Q + full attribute patterns
  -> item-specific reduced groups
  -> saturated G-DINA EM
  -> design-matrix transformation
  -> observed information
  -> A-CDM Wald test
```

It is suitable for formula-by-formula checking and does not replace the `GDINA` R package in formal analysis.
