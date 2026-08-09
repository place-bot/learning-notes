# Majority class baseline and class imbalance

## 1. Category baseline

Category O has 666 questions and Category M has 139 questions:

\[
\pi_O=\frac{666}{805}=0.827329,
\]

\[
\pi_M=\frac{139}{805}=0.172671.
\]

The accuracy of constant prediction O is

\[
\operatorname{Accuracy}_{\text{all-O}}
=
\pi_O
=
82.733\%.
\]

## 2. Compare with the best model

The best NB accuracy is 85.2%, so the absolute gain is

\[
85.2-82.733
=
2.467\text{ pp}.
\]

The relative error rate drops to

\[
\frac{
(1-0.82733)-(1-0.852)
}{
1-0.82733
}
\approx14.3\%.
\]

These two quantities describe different scales and both can be reported.

## 3. LR and SVM

The best LR accuracy is 75.3% and the best SVM is 74.9%. Both are below all-O accuracy.

This does not mean that the models are worthless: they may sacrifice majority class accuracy to identify M. It cannot be determined when the confusion matrix is ​​missing.

## 4. Standard weighted F1 baseline

When all-O:

\[
\operatorname{Precision}_O
=
\frac{666}{805}=0.82733,
\]

\[
\operatorname{Recall}_O=1,
\]

\[
F1_O
=
\frac{2(0.82733)(1)}
{0.82733+1}
=0.90551.
\]

Class M F1 is 0. Weighted by true support:

\[
F1_{\mathrm{weighted,all-O}}
=
\frac{666}{805}\times0.90551
=74.915\%.
\]

## 5. Paper results relative to F1 baseline

|Optimal configuration of the model| weighted F1 |Relative to all-O|
| --- | ---: | ---: |
| LR | 73.1% | -1.8 pp |
| SVM | 72.0% | -2.9 pp |
| NB | 85.6% | +10.7 pp |

Under the standard weighted F1 definition, the advantage of NB is more obvious than accuracy.

## 6. Baseline still needed

- stratified random classifier；
- class-prior classifier；
- Only use the length of the question stem;
- Only use a few rules such as whether it contains "integer/sum/picture";
- Multinomial NB；
- Complement NB；
- character \(n\)-gram；
- Upper bound on agreement among experts.

The paper does not report these baselines.

## 7. More suitable main indicator

For new title annotation, missing a few attributes may be important. It is recommended to set the following indicators as the main report:

\[
\operatorname{Recall}_M,
\quad
F1_{\mathrm{macro}},
\quad
\operatorname{BalancedAccuracy}.
\]

If the model output sets reliability, it should also report:

- calibration curve；
- Brier score；
- selective accuracy；
- Error rates under different manual review rates.
