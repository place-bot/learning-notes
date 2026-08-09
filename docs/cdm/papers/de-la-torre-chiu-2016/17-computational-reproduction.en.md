# This site can calculate recurrence

## Script

[`tools/de_la_torre_chiu_2016_gdi_validation.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/de_la_torre_chiu_2016_gdi_validation.py) Implementation:

- Table 1 for all 16 weights and success probabilities;
- The folding weight and success probability of any candidate q-vector;
- GDI and PVAF;
- \(2^K-1\) Exhaustive;
- Threshold, parsimony and tie rules;
- \(30\times5\) Q of the paper;
- High-order attribute generation;
- Study 1 five generative models;
- 7/8 random Q entry errors;
- provisional G-DINA EM；
- Recovery rate of entry and vector layers.

## Accurate verification

```bash
python3 tools/de_la_torre_chiu_2016_gdi_validation.py \
  --demo-only
```

Output:

```text
correct q=1110 GDI=0.029558
overspecified q=1111 GDI=0.029558
under+over q=0111 GDI=0.012524
collapsed group 000-: w=0.090, p=0.225
selected at epsilon=0.950: q=1110
```

It checks three theoretical threads:

\[
\varsigma^2(1110)
=
\varsigma^2(1111),
\]

\[
\varsigma^2(0111)
<
\varsigma^2(1110),
\]

\[
\text{When juxtaposing, choose the one with fewer attributes.}1110.
\]

## Code to formula

|Python functions|mathematical objects|
| --- | --- |
| `collapsed_success_profile()` |Folding of formula (3)--(4) \(w,p\)|
| `gdi()` | \(\sum w(p-\bar p)^2\) |
| `exhaustive_search()` |GDI, PVAF, minimal decision making|
| `estimate_full_class_probabilities()` |\(\widehat p_{jl}\) posterior expectation count|
| `higher_order_attributes()` |Paper high-order attribute model|
| `simulate_study1_responses()` |Five reduction models|
| `randomly_misspecify_q()` |7/8 random entries flipped|
| `validate_one_dataset()` |provisional fit to suggested Q|
| `q_recovery_summary()` |Four grid rates for Tables 4--5|

## Quick random check

```bash
python3 tools/de_la_torre_chiu_2016_gdi_validation.py \
  --model DINA \
  --examinees 1200 \
  --replications 3
```

The default output also reports:

- Whether EM converges;
- average number of iterations;
- Error entry correction rate;
- Correct entry retention rate;
- Error vector correction rate;
- Correct vector retention rate.

## Paper size

```bash
python3 tools/de_la_torre_chiu_2016_gdi_validation.py \
  --model DINA \
  --paper-scale
```

This uses:

\[
N=2000,\qquad R=100,
\]

The first 50 copies are flipped over 7 squares, and the last 50 copies are flipped over 8 squares.

The five Study 1 models need to be run separately:

```text
DINA
DINA-ACDM
ACDM
DINO-ACDM
DINO
```

## The boundary between accurate reproduction and teaching reproduction

Table 1 is a deterministic exact reproduction. The Monte Carlo part is a transparent teaching reproduction, and the values ​​will not be equal to Table 4 cell by cell. The reasons include:

- The original article did not disclose the random seed;
-Original Ox initialization and convergence settings are incomplete;
- Not all implementation details of empirical Bayes EM are given;
- Randomly flip the position every time it changes;
- The original article summarizes 100 pieces of data for each condition.

The script currently implements Study 1. The monotonic unconstrained probability sampling of Study 2 requires additional determination of random generation details not detailed in the original paper, so the original table should be based on Table 5 of the paper.

## Data boundaries

The fractional subtraction response matrix is not published in the repository with the paper. This site reproduces it:

- Q；
- item text;
- GDI/PVAF table;
- Suggested result;
- Recording of numerical inconsistencies.

No claim was made to recalculate the raw response data for 536 people.
