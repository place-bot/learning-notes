# Computable recurrence

## Site script

[`tools/de_la_torre_2008_q_validation.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/de_la_torre_2008_q_validation.py) Implementation:

- \(30\times5\) Q in the original Table 3;
- Conditions 0--11 of Table 4;
- DINA data generation and empirical-prior EM;
- Posterior expected number of people and number of correct answers;
- \(\widehat g,\widehat s,\widehat\delta\) of any candidate q-vector;
- \(2^K-1\) Exhaustive search;
-Original text forward sequential search;
- \(\varepsilon\) stopping rule;
- Accurate calculations of hypothetical problems.

It reuses our contribution to the transparent DINA EM written by de la Torre (2009) and does not rely on NumPy or proprietary software.

## Run

In the repository root directory:

```bash
python3 tools/de_la_torre_2008_q_validation.py
```

Default:

- Condition 11；
- \(N=1200\) for quick inspection;
- \(\varepsilon=.00,.01,.05,.10,.20\)；
- Random Seeds 2008.

Use the original sample size:

```bash
python3 tools/de_la_torre_2008_q_validation.py \
  --condition 11 \
  --paper-scale \
  --compare-q
```

Check other conditions:

```bash
python3 tools/de_la_torre_2008_q_validation.py \
  --condition 5 \
  --examinees 5000
```

## Deterministic output of hypothetical question

The script first outputs:

```text
step 1: 10000:.30, 01000:.30, 00100:.00, 00010:.00, 00001:.00
step 2: 11000:.60, 10100:.20, 10010:.20, 10001:.20
step 3: 11100:.51, 11010:.51, 11001:.51
selected 11000 with g=.20, s=.20, delta=.60
```

These values accurately reproduce the main search lines of the original Tables 1--2:

\[
.30\rightarrow.60\rightarrow.51,
\]

So it stops at the double attribute vector \(11000\).

## Code to formula mapping

|code|formula object|
| --- | --- |
| `posterior_expected_counts()` | \(N_{jl},R_{jl}\) |
| `candidate_from_counts()` | \(\widehat g_{jl'},\widehat s_{jl'},\widehat\delta_{jl'}\) |
| `all_nonzero_q_vectors()` | \(\{0,1\}^K\setminus\{\boldsymbol0\}\) |
| `exhaustive_search()` |All \(2^K-1\) candidates|
| `sequential_search()` |Original text gradually adds attributes|
| `misspecified_q_matrix()` | Table 4 |
| `mean_guess_plus_slip()` | \(\bar g+\bar s\) |
| `proposed_q_matrix()` |Combine the suggested lines of 30 questions into a candidate Q|
| `continue_em()` |Add 5 EM cycles under candidate Q|

## Stop code for sequential search

```python
if accepted is not None \
        and best.delta - accepted.delta <= cutoff:
    break
```

The conditions for accepting new attributes are equivalent to:

\[
\widehat\delta^{(s)}
-
\widehat\delta^{(s-1)}
>
\varepsilon.
\]

##Why the random output is not equal to the original table cell by cell

The original text has not been published:

- Random number seed;
- Ox initialization details;
- Full implementation settings for empirical Bayesian prior;
- Complete intermediate states for each set of candidate Qs.

The script on this site is used to check the algorithm and direction. Stochastic simulations will produce numerical differences due to seeds, posterior estimates, and EM implementations; the fixed table values ​​of the original text should be based on Tables 5--6 of the paper.

## Reproducible boundaries

The script does not come with any copyright or licensing restrictions:

- 2144 human fraction subtraction response matrix;
- NAEP restricted-use or sample weight data;
-Original author Ox source code.

Therefore, the two real data pages reproduce the design, formula, and reported results, and cannot claim to have recalculated the original tables.

## Extensible checks

Can be added based on the script:

- Q row recovery rate for multiple replications;
- different \(N,J,K\);
- Attribute correlation and sparse mode;
- Low \(\delta\) item;
- leave-one-item-out posterior；
- bootstrap recommended frequency;
- Problem-by-question comparison with `CDM::din.validate.qmatrix()` exhaustive solution.
