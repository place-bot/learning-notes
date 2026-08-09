# Experiment: Data partitioning, \(k\) adjustment algorithm selection

## 1. Division ratio

805 questions are randomly divided into:

\[
80\%\text{ train},
\qquad
10\%\text{ validation},
\qquad
10\%\text{ test}.
\]

Each part maintains the O/M ratio.

By integer sample size, the most natural scale is close to:

|subset|scale|
| --- | ---: |
|training| 644 |
|Verify| 80 |
|test| 81 |

The paper does not report the actual integer size and random seed.

## 2. Three characteristic ranges

\[
\mathcal G
=
\{
(1,1),(1,2),(1,3)
\}.
\]

Corresponding to three result tables respectively.

## 3. Three algorithms

\[
\mathcal A
=
\{
\mathrm{LR},\mathrm{SVM},\mathrm{NB}
\}.
\]

## 4. Search for \(k\)

\[
\mathcal K
=
\{5,10,15,\ldots,300\}.
\]

\[
|\mathcal K|
=
\frac{300-5}{5}+1
=60.
\]

Each "feature range × algorithm" combination is fitted on the training set, and the best performing \(k\) is selected on the validation set.

The feature selection branch contains at least

\[
3\times3\times60=540
\]

Secondary candidate fit.

## 5. Full feature comparison

Each feature range and algorithm also trains a no feature selection version:

\[
3\times3=9
\]

A comparison.

## 6. Final test

Fixed the \(\widehat k\) selected by the validation set for each combination, and then reported it in the test set:

- accuracy；
- weighted F1。

## 7. The main independent variable of the experiment

|factors|level|
| --- | --- |
|\(n\)-gram range| 3 |
|classifier| 3 |
|Feature selection|Yes / No|
| top-\(k\) |60 candidates, only for selective branches|

## 8. Uncontrolled factors

The paper has no system adjustment:

- tokenization method;
- TF--IDF definition;
- LR regular strength;
- \(C\) and kernel of SVM;
- NB variant;
- Category weight;
- Random division;
- Question template grouping.

## 9. Risk of single division

10% test set is small. A more robust design can use:

- repeated stratified \(K\)-fold；
- nested cross-validation；
- Group split according to question type template;
- Split by year, school or item bank source;
- bootstrap confidence interval.

The paper has no repeated divisions and no significance tests.
