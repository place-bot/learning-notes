# Original Ox and `GDINA::Qval()` code intensive reading

## Original code status

Thesis description:

- Two-stage estimation and search by Ox;
- Implementation cited Doornik (2007);
-Interested readers may contact the first author.

The article does not give the warehouse, download address, version number or random seed. So the original Ox implementation cannot be audited line by line.

## Current public implementation

Check this page:

- [`Wenchao-Ma/GDINA`](https://github.com/Wenchao-Ma/GDINA)；
- CRAN `GDINA` 2.9.12；
- `R/GDI.R`；
- `src/varsigma.cpp`；
- `Qval()` document.

This package is maintained by Wenchao Ma and Jimmy de la Torre. The current interface is:

```r
fit <- GDINA(dat = Y, Q = Q0, model = "GDINA")
out <- Qval(
  fit,
  method = "PVAF",
  iter = "none",
  eps = 0.95
)
```

## Entrance check for `Qval()`

The R layer checks first:

- The input object belongs to `GDINA`;
- `eps` is located at \([0,1]\) or equal to `-1`;
- Single group model;
- binary attributes;
- There is no default structure for attributes;
- `iter` belongs to `none/test/test.att/item`.

These restrictions clarify the scope of the current function.

## Get the posterior from the fitting object

Core objects:

```r
w <- extract(GDINA.obj, "posterior.prob")
logpost <- extract(GDINA.obj, "logposterior.i")
```

Among them:

- `w` corresponds to \(\widehat w_l\);
- `exp(logpost)` corresponds to \(\tau_{il}\) for each student.

The code calculates the posterior expected number of correct answers:

```r
rc <- apply(YY, 2, function(x) {
  colSums(x * exp(logpost))
})
```

And the posterior expected number of respondents:

```r
rn <- apply(1 * (!is.na(Y)), 2, function(x) {
  colSums(x * exp(logpost))
})
```

Complete model success rate:

```r
est.p <- (rc + 1e-10) / (rn + 2e-10)
```

This corresponds to

\[
\widehat p_{jl}
=
\frac{\sum_i\tau_{il}Y_{ij}+10^{-10}}
{\sum_i\tau_{il}+2\times10^{-10}}.
\]

The minimal smoothing term prevents division by zero for empty categories.

## Candidate grouping

```r
patt <- attributepattern(K)[-1, ]
loc <- eta(patt)
```

`patt` contains \(2^K-1\) non-zero candidates, and `eta()` returns the grouping number for each candidate pair \(2^K\) complete patterns.

## `varsigma()` for C++

`src/varsigma.cpp` Execute for each question and each candidate:

```cpp
arma::vec wp = mP.col(j) % vw;
reducedw(l) = arma::accu(vw.elem(q1));
reducedp(l) = arma::accu(wp.elem(q1)) / reducedw(l);
double pbar = arma::accu(reducedp % reducedw);
double Sbar = arma::accu(reducedp % reducedp % reducedw);
varsig(j,q) = Sbar - pbar * pbar;
```

Row-by-row mapping:

| C++ |formula|
| --- | --- |
| `wp` | \(w_lp_{jl}\) |
| `reducedw` |Collapse group weight|
| `reducedp` |Folding group weighted success rate|
| `pbar` | \(\bar p_j\) |
| `Sbar` | \(\sum_r w_rp_r^2\) |
| `Sbar-pbar*pbar` | \(\varsigma_j^2\) |

## PVAF and proposal vectors

R layer:

```r
vsg <- varsigma(t(loc), est.p, w)
PVAF <- vsg / vsg[, L - 1]
```

The last column is full attribute candidates. Then group by the desired number of attributes:

1. Get the highest PVAF within each attribute number;
2. Determine whether the highest value is greater than `eps`;
3. Get the first attribute number that passes the threshold;
4. Return the corresponding q-vector.

The current code uses strict comparison:

```r
max(x) > eps
```

Use of text in the paper

\[
\operatorname{PVAF}\ge\varepsilon.
\]

There is a difference between the two only when the PVAF is exactly equal to the threshold.

## Subsequent expansion

Currently `GDINA::Qval()` has added functions not found in the original text:

|Options|meaning|
| --- | --- |
| `eps=-1` |Generate thresholds using prediction formulas from subsequent studies|
| `iter="test"` |Refit after updating all suggested questions in each round|
| `iter="test.att"` |Only one attribute number is changed for each question in each round|
| `iter="item"` |Give priority to revising one question in each round|
| `method="wald"` |Verify using stepwise Wald|
| mesa plot |Check attribute number and PVAF path|

Iterative implementations respond to the problem of "initial Q contaminating the posterior" but may still loop or stop at the wrong equilibrium point. Code explicitly documented:

- Convergence;
- Loop detected;
- Generate empty attribute columns;
- The maximum number of iterations is reached.

## Standalone `Qval` package

CRAN's [`Qval`](https://cran.r-project.org/package=Qval) further integrates:

- GDI；
- Wald；
- Hull；
- MLR-B；
- Multiple search and iteration methods.

It is a follow-on general framework and cannot be reversed as the original 2016 Ox program.

## Application suggestions

The current `GDINA` documentation recommends that when the default PVAF generates too many modifications:

- Check mesa plots;
- Try stepwise Wald;
- Try iterative implementation;
- Use prediction threshold;
- Incorporate content review.

This is closer to a robust analysis process than the single `.95` threshold.
