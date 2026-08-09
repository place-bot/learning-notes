# Intensive reading of the original supplementary material code

## File composition

The original author published with the article:

|File|function|
| --- | --- |
| `Q_Dina_all.cpp` |Three MCMC, data generation, encoding and helper functions|
| `fraction_subtraction.R` |Read data, compile C++, fit three methods, and extract results|
| `README.txt` |Function entry, parameters and return object description|

C++ is compiled with `RcppArmadillo`, and the R side uses:

```r
Rcpp::sourceCpp("Q_Dina_all.cpp")
```

## Paper object to code function

|Thesis object|code|
| --- | --- |
|Binary vector integer encoding| `bijectionvector()` |
|Integer reduction attribute/q-vector| `inv_bijectionvector()` |
|ideal response matrix| `ETAmat()` |
|Legal initial Q| `random_Q()` |
|Three identifiable limitations| `identify_check()` |
|Student attributes, \(\pi,s,g\) update| `parm_update_nomiss()` / `update_alpha()` / `update_sg()` |
|Restricted element-wise Q update| `updateQ_DINA_new()` |
| DS2 + MH | `updateQ_MH()` |
|Restricted Gibbs main chain| `dina_Gibbs_Q()` |
|Restricted MH main chain| `DINA_MH_Q()` |
|Unconstrained Gibbs main chain| `DINA_Gibbs_Q_unconst()` |
|DINA simulation| `sim_Y_dina()` |

## `identify_check()` How to check three conditions

Code calculation:

```cpp
c_sum = sum(Q, 0);
r_sum = sum(Q, 1);
```

Check separately

\[
\min_k c_k>2,
\qquad
\min_j r_j>0.
\]

Then count the occurrence number `n_ek` of each unit row \(\boldsymbol e_k\) through matrix operations, requiring

\[
\min_k n_{e_k}>1.
\]

It is legal to return if all three Boolean values are true.

##Ideal response implementation

`ETAmat(K,J,Q)` enumerates \(2^K\) attribute profiles. For item \(j\) and category \(c\):

```cpp
compare = qj * alpha_c - qj * qj.t();
ETA(j, cc) = (compare >= 0);
```

This corresponds to

\[
\eta_{cj}
=
I(\boldsymbol q_j^{\mathsf T}\boldsymbol a_c
\ge
\boldsymbol q_j^{\mathsf T}\boldsymbol q_j).
\]

For binary vectors, the left side cannot exceed the right side, so `>= 0` is equivalent to equal.

## Fast condition updates for restricted Gibbs

`ETAmat_nok_one_m_ac(K)` precomputes each attribute under \(k\), the remaining q-vector configuration and attribute classes

\[
\eta_{-k}(1-\alpha_k).
\]

`abcounts()` Then count the affected students as \(Y_{ij}=0,1\). This eliminates the need to regenerate the full ETA for all Qs each time \(q_{jk}\) is updated.

Conditional sampling uses:

```cpp
qjk = 1.0 * (
    log(1-u) - log(u)
    > a0*log(s/(1-g)) + a1*log((1-s)/g)
);
```

The derivation is consistent with the previous page.

## Local likelihood ratio of MH

`updateQ_MH()`：

1. Extract \(B\) row positions from a certain column;
2. Press DS2 to fix the necessary 0/1;
3. Enumerate the legal configuration numbers of free bits;
4. Calculate the new-to-old likelihood ratio only for the selected item row;
5. Accept with `min(1, ratio)`.

The original implementation successively multiplied the probability ratio. Big data reproduction should be changed to log likelihood difference to reduce floating point underflow.

## Implementation of Q mode

Each Q sample is first calculated

\[
Q^{\mathsf T}\boldsymbol v,
\]

Then sort the codes in descending order. The last line of `Qcount` or `Qveccount` stores the number of occurrences. R script takes:

```r
modeindex = which.max(out$Qcount[K+1, ])
modeQ = inv_bijectionmat(J, out$Qcount[1:K, modeindex])
```

This implements the entire matrix mode and column label alignment described in Section 2.7 of the paper.

## Return value

All three main functions return:

- `QS`: Q sample after burn-in;
- `PIs`: latent class proportional sample;
- `SS`, `GS`: item parameters samples;
- `Qcount` or `Qveccount`: Standard Q code and frequency.

The MH version also returns the student category sample `CLASSES`.

## Scope of original code

It completely implements the three algorithms of paper comparison. The public R file is only for fractional subtraction applications, and the 3200 data set driver scripts, real item parameters, and random seeds that simulate Table 1 are not released with the text.

## Three recurring issues found during line-by-line review

These issues are from the current static version of the public supplement and are implementation and reproduction level.

### 1. R script contains an undefined object

The script is executed before any estimators are called:

```r
vj = bijectionvector(J)
Qvj = t(Q) %*% vj
```

At this time, the script does not create `Q`, and `Qvj` is not used in the following text. In a new R session, the second line will report `object 'Q' not found`. These two lines can be deleted when reoccurring; `vv` has been created separately for subsequent mode recovery.

### 2. The initial value of MH may violate monotonicity in the first round

`DINA_MH_Q()` is generated independently:

```cpp
ss = randu(J);
gs = randu(J);
```

Therefore, it may appear during the first round of attribute updates

\[
g_j\ge1-s_j.
\]

Subsequent `update_sg()` restores the truncation limit, and a long burn-in weakens the initial impact. A clearer initialization is how the original code is written in restricted Gibbs:

```cpp
ss = randu(J);
gs = (ones(J) - ss) % randu(J);
```

### 3. The DS2 free bits must all be 1.

`updateQ_MH()` only in

```cpp
Bmax > Bmin
```

When assigning a 0/1 configuration to the free position. If `Bmax == Bmin > 0`, the only legal configuration is that all free bits are 1, but the original array will retain the initial sentinel value of 2. Robust implementations should allow this equality boundary to also go into `validvector()`, or explicitly set all free bits to 1.

These review findings do not rewrite the reported numbers in Table 1 of the paper; if the supplementary code is recompiled for new experiments, it is recommended to correct and record the patch first.

[Next page: Current edina package code intensive reading](26-edina-package.md)
