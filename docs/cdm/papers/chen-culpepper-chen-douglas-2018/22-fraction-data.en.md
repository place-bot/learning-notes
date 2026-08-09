# Experiment: Fractional subtraction data and analysis design

## Data

Tatsuoka fraction subtraction data contains:

\[
N=536\ \text{middle school student},
\qquad
J=20\ \text{question}.
\]

Each answer is scored 0/1. This data is available from `fraction.subtraction.data` in the R package `CDM` and is a classic data used repeatedly in Q matrix studies.

## Eight attributes defined by experts

The original Table 2 lists:

1. Convert integers to fractions;
2. Separate the whole number part from the fraction;
3. Divide before subtracting;
4. Find the common denominator;
5. Borrow from the integer part;
6. After borrowing, subtract the second molecule from the transformation value of the first molecule;
7. Subtraction of molecules;
8. Reduce the calculation result to its simplest form.

## Structural issues of expert Q

Expert Q has \(K=8\). Almost all questions require attribute 7, and many questions require multiple attributes at the same time. For a quiz with only 20 questions:

- Two sets of \(I_8\) already require 16 pure questions;
- At least three questions for each attribute require additional coverage;
- The expert Q of Table 2 does not satisfy the identifiable structure used in this paper.

Therefore, the author did not put \(K=8\) Q directly into the restricted algorithm, but explored it separately

\[
K=3
\quad\text{and}\quad
K=4.
\]

## Analysis target

Compare:

- Restricted MH;
- Restricted Gibbs;
- Chung (2014) Unconstrained Gibbs.

Report for each \(K\):

\[
\widehat Q,\qquad
\widehat s_j,\qquad
\widehat g_j.
\]

Constrained Gibbs and MH get the same posterior mode Q, so Tables 3--4 only show MH and unconstrained Gibbs side by side, and note under the table that Q of CGibbs is the same as MH.

## Supplementary R script

Original author's script:

```r
data(fraction.subtraction.data)
Y = as.matrix(fraction.subtraction.data)
K = 3
burnin = 20000
chain_length = burnin + 10000
B = 2*K
```

Then call:

```r
dina_Gibbs_Q(Y, K, burnin, chain_length)
DINA_MH_Q(Y, K, B, burnin, chain_length)
DINA_Gibbs_Q_unconst(Y, K, burnin, chain_length)
```

This public script sets 20,000 burn-ins and 10,000 holdout samples. To reproduce \(K=4\), you need to change `K` to 4 and run again.

## How to interpret attributes

Column labels for exploratory Q are unnamed by the model. The author observes which questions only load a certain column, and then combines the item operation content to give explanations to the three attributes:

1. Find the common denominator;
2. Borrow from the integer part;
3. Perform subtraction on the integer and fractional parts separately.

These names are a post hoc explanation of the content of the estimated columns and are not input to the algorithm.

## Empirical evidence boundaries

The paper does not report:

- Comparison of the marginal likelihood or information criterion of \(K=3\) and \(K=4\);
- Posterior prediction test;
- Student classification accuracy;
- Independent review by experts of exploratory attribute interpretations;
- Stability of different chain initial values.

Therefore, the result shows two low-dimensional exploration structures, and it cannot be concluded that \(K=3\) or \(K=4\) is the only correct attribute number.

[Next page: Experiment——K=3 question-by-question result](23-fraction-k3.md)
