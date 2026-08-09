# Code base to achieve intensive reading

## Original code status

All three experiments in the paper illustrate that the algorithm is implemented by the author using Ox, citing Doornik (2003). The text and references are not provided:

- Download address;
- Appendix code;
- software packages;
- executable file;
- Random seed.

Therefore, the original Ox program cannot be reviewed line by line. The formulas, algorithm descriptions and tables given in the original text are the main basis for reproduction.

## Subsequent public implementation

CRAN [`CDM`](https://cran.r-project.org/package=CDM) provides:

```r
din.validate.qmatrix(object, IDI_diff = .02, print = TRUE)
```

This site has verified the following of CDM 8.3-14:

- [`R/din.validate.qmatrix.R`](https://github.com/alexanderrobitzsch/CDM/blob/master/R/din.validate.qmatrix.R)
- [`src/cdm_rcpp_din_validate.cpp`](https://github.com/alexanderrobitzsch/CDM/blob/master/src/cdm_rcpp_din_validate.cpp)
- `man/din.validate.qmatrix.Rd`

This function refers to de la Torre (2008), but the search and threshold logic have important differences from the original sequential \(\delta\)-method.

## R layer input

The function accepts an object that has been fitted by `CDM::din()` and reads:

|object field|meaning|
| --- | --- |
| `object$q.matrix` |Current Q|
| `object$rule` |DINA or DINO rules for each question|
| `object$guess[,1]` |Current guessing|
| `object$slip[,1]` |current slipping|
| `object$I.lj` |The expected number of people for the mode and item|
| `object$R.lj` |The expected number of correct answers for the mode and item|
| `object$attribute.patt.splitted` |\(2^K\) attribute profiles|

The code first calculates:

```r
IDI <- 1 - slip - guess
```

This is the same as \(\widehat\delta\) from the original text.

## Candidate generation

R code to generate all bipartite vectors using `expand.grid()` and remove all zero rows:

```r
q.matrix.poss <- q.matrix.poss[
    !(rowMeans(q.matrix.poss) %in% 0),
]
```

The number of candidates is:

\[
2^K-1.
\]

This implementation therefore performs an exhaustive search. It does not follow the original secondary sequential search of "starting with a single attribute and adding only one attribute each round".

## How to group C++ cores

For each candidate `qvec`, item `ii` and attribute profile `ll`, C++ calculates:

```cpp
ness_ii += qvec[kk];
latresp += qvec[kk] * attr_patt(ll,kk);
```

If

```cpp
latresp < ness_ii
```

Then the mode enters the \(\eta=0\) group of DINA; otherwise, it enters the \(\eta=1\) group.

This is related to

\[
\eta_l(\boldsymbol q)
=
\prod_k\alpha_{lk}^{q_k}
\]

Equivalent.

The expected count aggregates to:

```cpp
Ij0[ii] += Ilj(ii,ll);
Rj0[ii] += Rlj(ii,ll);
Ij1[ii] += Ilj(ii,ll);
Rj1[ii] += Rlj(ii,ll);
```

Candidate parameters:

```cpp
guess[ii] = Rj0[ii] / Ij0[ii];
slip[ii] = (Ij1[ii] - Rj1[ii]) / Ij1[ii];
```

Completely corresponds to the original EM-based solution.

## How to select rows in R layer

C++ Return \(g,s\) for all "item × candidate q-vectors". R layer calculation:

```r
coef.modified$IDI <-
    1 - coef.modified$slip - coef.modified$guess
```

Calculate again:

```r
delta.IDI <- IDI(candidate) - IDI(original)
```

Only keep:

```r
IDI(candidate) - IDI(original) > IDI_diff
```

For each question, take the first row in descending IDI order as the suggestion q-vector.

## The difference between the two threshold meanings

|Original text \(\varepsilon\)| `CDM::IDI_diff` |
| --- | --- |
|Compare adjacent search step \(\delta^{(s)}-\delta^{(s-1)}\)|Compare `IDI(candidate)-IDI(original)` of the candidate with the original Q|
|Decide whether to continue adding an attribute|Decide if a candidate is enough to outlast the original row|
|Path dependent forward search|Filter after exhaustive exhaustion of all candidates|
|The largest number of candidates is \(K(K+1)/2\)|Number of candidates \(2^K-1\)|

So `IDI_diff=.02` cannot be directly interpreted as the same algorithm as the original \(\varepsilon=.02\).

## Return object

|Field|content|
| --- | --- |
| `coef.modified` |All items and all candidate parameters, IDIs and improvements|
| `coef.modified.short` |Candidates exceeding `IDI_diff`|
| `q.matrix.prop` |Suggestions after taking the highest IDI for each question Q|
| `time_diff` |Function takes time|

## Three points to note at the code level

1. The function uses the posterior expectation count in the current `din` object, and the initial Q error still goes into candidate scoring.
2. The function returns suggestion Q, but does not automatically complete the multi-threshold additional EM and content review mentioned in the original article under suggestion Q.
3. The exhaustive complexity increases exponentially with \(K\). When the number of attributes is large, memory and running time need to be evaluated.

## Official example

`CDM` document simulation has 12 questions, 3 attributes, and 4000 people. The Q line of question 1 and question 10 is written incorrectly. Suggestions given by `din.validate.qmatrix()` Q recovery:

\[
\boldsymbol q_1=100,\qquad
\boldsymbol q_{10}=110.
\]

This example verifies that the process in the package can be run; it is a follow-up software example and cannot replace the original 30-question simulation and two real-world data analyses.

