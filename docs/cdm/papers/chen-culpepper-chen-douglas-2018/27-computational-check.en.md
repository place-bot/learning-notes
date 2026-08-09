# This site can calculate verification and code review findings

## Script

This site provides:

[`tools/chen_et_al_2018_bayesian_q_check.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/chen_et_al_2018_bayesian_q_check.py)

Run:

```bash
python3 tools/chen_et_al_2018_bayesian_q_check.py
```

It is independently pedagogically verified and does not replace the author's Rcpp implementation.

## Verification 1: Three identification restrictions

`is_identified(q)` Check:

\[
\min_j\sum_kq_{jk}>0,
\]

\[
\min_k\sum_jq_{jk}\ge3,
\]

\[
\#\{j:\boldsymbol q_j=\boldsymbol e_k\}\ge2
\quad\forall k.
\]

The third formula is equivalent to containing two sets of \(I_K\) after row replacement.

## Verification 2: Small-scale irreducibility

take

\[
K=2,\qquad J=6.
\]

Only \((10),(01),(11)\) is allowed in each line, and 230 tagged Qs that meet the limit are obtained by enumeration.

Define "only one element flip" between two legal states as a graph edge. Breadth first search output:

```text
Identified states for K=2, J=6: 230
States reached by one-flip graph: 230
One-flip graph connected: True
```

This verifies the conclusion of Theorem 1 in a limited small case. It does not constitute general proof.

## Verification 3: Table 1 aggregation

The script is entered in line 32 of Table 1 of the paper, and the recalculation condition is equal weighted average:

```text
K=3 mean whole-Q recovery:
MH=94.06, CGibbs=94.94, Gibbs=90.88
K=3 mean entry accuracy:
MH=98.04, CGibbs=98.36, Gibbs=95.54

K=4 mean whole-Q recovery:
MH=53.56, CGibbs=84.88, Gibbs=55.50
K=4 mean entry accuracy:
MH=88.41, CGibbs=96.02, Gibbs=89.27
```

It also checks: CGibbs has the highest or tied highest number of full Q recoveries in all \(K=4,\rho>0\) conditions.

## Verification 4: Element-wise majority vote counterexample

Consider three legal Qs:

\[
Q^{(1)}=
\begin{bmatrix}
10\\10\\10\\01\\01\\01
\end{bmatrix},
\quad
Q^{(2)}=
\begin{bmatrix}
10\\10\\01\\10\\01\\01
\end{bmatrix},
\quad
Q^{(3)}=
\begin{bmatrix}
10\\10\\01\\01\\10\\01
\end{bmatrix}.
\]

All three matrices satisfy two sets of unit matrices, at least three questions in each column, and non-zero in each row.

Element-wise majority vote gets

\[
\widehat Q_{\text{entry}}=
\begin{bmatrix}
10\\10\\01\\01\\01\\01
\end{bmatrix}.
\]

Its column sum is

\[
(2,4),
\]

There are only two questions for the first attribute, so

\[
\widehat Q_{\text{entry}}\notin\mathcal Q.
\]

Script output:

```text
Every one of three posterior draws is identified: True
Entry-wise majority is identified: False
Column sums of entry-wise majority: [2, 4]
```

## Direct suggestions for software usage

After using the current `edina` package, execute at least:

```r
q_hat = extract_q_matrix(fit, binary = TRUE)
check_identifiability(q_hat)
```

If `FALSE` is returned, element-wise inclusion probabilities should be reported and the entire Q digest that satisfies the constraints should be used instead. Since `check_identifiability()` is an Rcpp function in the package, whether the user interface can call it directly depends on the namespace export; you can also use `q_matrix(q_hat)` to view the `identifiable` attribute of the object.

## Verification scope

The script doesn't have:

- Rerun 3200 original simulations;
- Rebuild missing real \(s,g\) design;
- A chain of 30,000 repetitions to reproduce fraction subtraction;
- Prove the irreducibility of general \(K,J\);
- Evaluate the statistical calibration of the `edina` package.

It is mainly used to check discrete constraints, tabular summaries and software summary boundaries.

[Next page: Limitations, conclusions and future work](28-limitations-conclusion-future.md)
