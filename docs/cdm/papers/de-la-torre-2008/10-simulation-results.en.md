# Simulation result and explanation

## Baseline under correct Q

Condition 0 uses the correct Q:

- item parameters average absolute bias .01;
- Maximum absolute bias .04;
- Average discrimination is about .61;
- \(\bar g+\bar s=.3924\), close to the generated value of .40.

This shows that the current \(N=5000\), uniform mode and \(g=s=.20\) conditions provide an easier recovery environment for EM.

## Error Q How to pollute parameters

The original text Table 5 reports the modified question parameters after initial error Q fitting:

|Conditions|question number| \(\widehat g\) | \(\widehat s\) | \(\widehat\delta\) |Full test \(\bar g+\bar s\)|
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | .1807 | .1984 | .6208 | .4139 |
| 2 | 1 | .4850 | .4878 | .0273 | .4008 |
| 3 | 11 | .3908 | .1918 | .4174 | .4058 |
| 4 | 11 | .3093 | .4789 | .2118 | .4019 |
| 5 | 11 | .1976 | .4686 | .3338 | .3968 |
| 6 | 21 | .2966 | .1867 | .5167 | .4028 |
| 7 | 21 | .1948 | .4688 | .3364 | .4083 |
| 8 | 21 | .1936 | .6362 | .1702 | .4044 |
| 9 | 21 | .2445 | .4704 | .2850 | .4104 |
| 10 | 21 | .2560 | .6554 | .0885 | .4105 |

The three incorrect questions in Condition 11 are:

|question number| \(\widehat g\) | \(\widehat s\) | \(\widehat\delta\) |
| ---: | ---: | ---: | ---: |
| 1 | .2654 | .6347 | .1000 |
| 11 | .1807 | .1984 | .6208 |
| 21 | .4850 | .4878 | .0273 |

Full test for Condition 11 \(\bar g+\bar s=.4260\).

## Parameter direction cannot be applied mechanically

The derivation of hypothetical questions shows that missing marks usually raise slip, and multiple marks usually raise guess. Simulations in Table 5 also show that errors overall cause shrinkage of bias and \(\delta\), but individual rows are affected by posterior feedback under the overall error Q. For example, the error question in Condition 1 is still very high \(\widehat\delta\).

This reminds us:

\[
\widehat\delta
\text{Depends on both candidate grouping and current posterior}.
\]

The initial posterior comes from the entire set of errors Q, and a certain parameter direction cannot be regarded as a deterministic label for cell-wise errors.

## Threshold .20 is too strict

When \(\varepsilon=.20\):

- Even if all Q in Condition 0 are correct, 10 lines have been changed;
- Most error conditions changed around 9--12 lines;
- The new Q generated raises the full quiz \(\bar g+\bar s\) to about .536--.546;
- Many multi-attribute questions are truncated into shorter q-vectors.

The large threshold requires that each new attribute brings at least a .20 increment of discrimination, and the real required attributes may not pass.

## Conditions 0--4

For \(\varepsilon=.00,.01,.05,.10\):

- Condition 0 retains all correct q-vectors;
- Conditions 1--4 only change the target error line;
- Recommended rows restored to correct q-vector;
- Updated \(\bar g+\bar s\) back to about .3927--.3930.

Individual errors in these conditions are easier to resolve directly with a set of recommendations.

## Conditions 5--10

A search of these conditions yielded two candidates, one of which was the correct q-vector. After updating the parameters and posterior under candidate Q, the author found:

- Correct q-vector always has lower full test \(\bar g+\bar s\);
- Choose the correct specification in the end;
- Correct other q-vectors are preserved.

This part shows the two-stage effect of "sequential search to propose candidates, and then update and compare by full test".

## Condition 11

When three lines are wrong at the same time:

- When \(\varepsilon<.20\), the suggestions for question 1 and question 11 are the same and correct;
- Question 21 suggestions will change with the threshold;
- \(\bar g+\bar s\) of \(\varepsilon=.10\) is the smallest after updating;
- This solution corresponds to the real Q.

Therefore, when the initial Q contamination is wider, the maximum \(\delta\) per question is not enough to determine the entire set of solutions, and the refitting comparison between thresholds is more important.

## Summary of the original text

Under this set of simulation conditions:

- Method to retrieve all modified q-vector;
- Keep all correct q-vectors;
- The authors accordingly report that both Type I and Type II errors are 0.

This "0" only corresponds to the 12 conditions and one simulation setup in the current design and cannot be used as a general error rate guarantee.

