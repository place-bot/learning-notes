# Experiment: accuracy and weighted F1

## 1. Two-category confusion table

|real\prediction| O | M |
| --- | ---: | ---: |
| O | \(TP_O\) | \(FN_O=FP_M\) |
| M | \(FP_O=FN_M\) | \(TP_M\) |

The total number of questions is

\[
N=TP_O+FN_O+FP_O+TP_M.
\]

## 2. Accuracy

\[
\operatorname{Accuracy}
=
\frac{TP_O+TP_M}{N}.
\]

It is easy to interpret, but may be dominated by the majority class when classes are imbalanced.

## 3. Each type of precision and recall

\[
\operatorname{Precision}_O
=
\frac{TP_O}{TP_O+FP_O},
\]

\[
\operatorname{Recall}_O
=
\frac{TP_O}{TP_O+FN_O}.
\]

The same applies to category M.

## 4. F1 per category

\[
F1_c
=
\frac{
2\operatorname{Precision}_c\operatorname{Recall}_c
}{
\operatorname{Precision}_c+\operatorname{Recall}_c
}.
\]

The equivalent form is

\[
F1_c
=
\frac{2TP_c}
{2TP_c+FP_c+FN_c}.
\]

## 5. weighted F1 of scikit-learn

The true support is

\[
t_O=TP_O+FN_O,
\qquad
t_M=TP_M+FN_M.
\]

The standard support-weighted F1 is

\[
F1_{\mathrm{weighted}}
=
\frac{t_O}{N}F1_O
+
\frac{t_M}{N}F1_M.
\]

## 6. Why macro-F1 should also be reported

\[
F1_{\mathrm{macro}}
=
\frac{F1_O+F1_M}{2}.
\]

It gives equal weight to both categories and more easily exposes the under-recognition of M-category.

## 7. Indicator combinations reported in the paper

The judgment rule of the paper is that accuracy and weighted F1 are both high at the same time. This combination is more complete than just giving accuracy , but still lacks:

- Class M recall;
- macro-F1；
- balanced accuracy；
- confusion matrix;
-confidence interval.

## 8. balanced accuracy

\[
\operatorname{BalancedAccuracy}
=
\frac12
\left(
\operatorname{Recall}_O
+
\operatorname{Recall}_M
\right).
\]

It fits the 82.7%/17.3% unbalanced structure of this study.

## 9. Q row-level follow-up indicators

If extended to multi-label Q, should be added:

\[
\operatorname{HammingLoss}
=
\frac{1}{JK}
\sum_{j,k}
\mathbb I
\left(
\widehat q_{jk}\ne q_{jk}
\right),
\]

and row exact match. Binary classification accuracy cannot replace these indicators.
