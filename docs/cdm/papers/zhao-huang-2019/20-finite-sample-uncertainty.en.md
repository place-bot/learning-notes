# Small test set, resolution and uncertainty

## 1. The test set is likely to have 81 questions

The paper says 10% is for testing. right

\[
N=805,
\]

Yes

\[
0.1N=80.5.
\]

The test scale will usually be 80 or 81.

## 2. 85.2% implies 69/81

On question 80, the correct number must be an integer:

\[
\frac{68}{80}=85.0\%,
\qquad
\frac{69}{80}=86.25\%.
\]

Cannot be rounded to 85.2%.

On question 81:

\[
\frac{69}{81}=85.185\%
\approx85.2\%.
\]

So "81 test questions, 69 correct" is the scale most compatible with the reported values.

## 3. Single question resolution

\[
\frac{1}{81}\times100\%
=
1.2346\text{ pp}.
\]

The best 85.2% is 0.6 pp different from the previous configuration's 84.6%, which is less than the resolution of one question.

## 4. Binomial proportion interval

Use Wilson's 95% interval for 69/81:

\[
\widehat p=0.85185,
\]

\[
CI_{95\%}
\approx
[0.759,0.913].
\]

The wide range reflects the limited number of test questions.

## 5. Relationship to 82.7% baseline

If the test set maintains the overall proportion, there will be about 67 category O questions among the 81 questions. Constant predicts that the correct number of O is about 67:

\[
\frac{67}{81}=82.7\%.
\]

The best model gets 69 questions correct, which is only about 2 more questions.

## 6. Possible confusion matrix

At a real O/M count of 67/14, the following table is consistent with 85.2% accuracy and 85.6% standard weighted F1:

|real\prediction| O | M |
| --- | ---: | ---: |
| O | 60 | 7 |
| M | 5 | 9 |

At this time:

\[
\operatorname{Accuracy}
=
\frac{60+9}{81}
=85.185\%,
\]

\[
F1_{\mathrm{weighted}}
\approx85.567\%.
\]

If the true distribution is 68/13, there is also a compatibility table for 61/7/5/8. The paper does not publish the confusion matrix, so these tables are only used to illustrate the integer structure of the result.

## 7. Repeated sampling is required

More reliable reporting should be given to:

\[
\overline{\operatorname{Score}}
\pm
\operatorname{SD}
\]

Or bootstrap interval, and display the result of each random division.

## 8. Conclusion

85.2% can prove that the pipeline learned part of the signal. The small test set does not support interpreting model differences of 0.5--1.0 percentage points as stable rankings.
