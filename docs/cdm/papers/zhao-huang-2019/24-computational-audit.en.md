# Numerical verification and output of this site

## 1. Files and targets

[`tools/zhao_huang_2019_audit.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/zhao_huang_2019_audit.py) only relies on the Python standard library for verification:

- Nine categories of questions;
- O/M ratio;
- all-O baseline;
- Feature selection gain of Tables 1--3;
- \(k\) search size;
- 85.2% of possible test denominators;
- Wilson interval;
- Equation (9) with standard weighted F1.

## 2. Run

```bash
python3 tools/zhao_huang_2019_audit.py
```

JSON：

```bash
python3 tools/zhao_huang_2019_audit.py --json
```

## 3. Verify output

```text
Nine-category total: 1069; O+M subset: 805
O share: 82.733%; all-O accuracy: 82.733%
All-O standard support-weighted F1: 74.915%
All-O F1 under printed Equation (9): 90.551%
Best reported accuracy gain over all-O: 2.467 percentage points
```

## 4. Feature selection gain

The program subtracts cell by cell to get:

|representation|model|accuracy gain|F1 gain|
| --- | --- | ---: | ---: |
| unigram | LR | +1.6 | +4.0 |
| unigram | SVM | +3.2 | +4.7 |
| unigram | NB | +62.7 | +62.3 |
| unigram+bigram | LR | +1.9 | +2.8 |
| unigram+bigram | SVM | +3.8 | +3.9 |
| unigram+bigram | NB | +15.5 | +17.9 |
| unigram+bigram+trigram | LR | +2.8 | +3.7 |
| unigram+bigram+trigram | SVM | +3.6 | +3.7 |
| unigram+bigram+trigram | NB | +16.3 | +18.4 |

## 5. \(k\) grid

\[
\{5,10,\ldots,300\}
\]

Contains 60 candidates.

## 6. Test the denominator

The program searches for an integer denominator around 10% of 805. The only nearest neighbor combination that rounds the accuracy to 85.2% is:

\[
n_{\mathrm{test}}=81,
\qquad
\text{correct}=69.
\]

## 7. Uncertainty

```text
one item = 1.235 percentage points
Wilson 95% interval = [75.9%, 91.3%]
```

## 8. Confusion table compatible with 85.6% F1

The program finds two candidates that are close to the overall proportion:

```text
O->O 60, O->M 7, M->O 5, M->M 9
O->O 61, O->M 7, M->O 5, M->M 8
```

Their standard weighted F1 is both rounded to 85.6%, and Equation (9) is about 84.8%.

## 9. Automatic assertion

The script data structure makes the following identities directly checkable:

\[
\sum_{c=1}^{9}n_c=1069,
\]

\[
n_O+n_M=805,
\]

\[
|\mathcal K|=60.
\]

## 10. Evidence boundaries

The program checks for consistency between published figures in papers, does not fit a classifier, and does not claim to reproduce the authors' predictions.
