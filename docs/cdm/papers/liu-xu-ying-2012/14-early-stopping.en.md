# Figures 1--2 with 4.5% early stop

## Target path under small sample

Thesis checks the failure case of \(N=500,K=5\). Draw on the left side of each picture

\[
\text{current}Q^{(m)}\text{Number of false entries with true Q},
\]

Draw on the right

\[
\widehat S(Q^{(m)}).
\]

## Figure 1

The algorithm initially fixes the error quickly, but eventually stops at a matrix that is still 1 entry away from the true Q. Subsequent \(S\) drops very little.

## Figure 2

The path once reaches true Q:

\[
\text{Number of error entries}=0,
\]

Then continue updating to another matrix, eventually retaining 1 error entry. With limited samples, the \(S\) of that error matrix is ​​slightly lower.

## Common phenomenon

- The target dropped significantly in the first two or three rounds;
-The target curve then becomes flat;
- \(S\) for multiple Qs are almost the same;
- "Keep going down" is probably just chasing sample noise.

## Early stop rules

If the relative improvement in round \(m\) is less than 4.5%, stop:

\[
\frac{
S(Q^{(m-1)})-S(Q^{(m)})
}{
S(Q^{(m-1)})
}
<0.045.
\]

This amounts to setting a minimum evidentiary threshold for each structural modification.

## Table 2

On the same batch of \(N=500\) samples:

| Q |Original Algorithm 1|4.5% early stop|
| --- | ---: | ---: |
| \(Q_2,K=4\) | 82 | 94 |
| \(Q_3,K=5\) | 38 | 70 |

Numbers are full recoveries out of 100.

## Why can it be improved?

The initial Q has only 3 rows of errors, and the true Q is usually on the short path. Large target drops most likely correspond to repairing major structural errors; small drops are more likely to result from limited sample perturbations. Early stopping preserves the first few strong updates and prevents subsequent weak updates from taking the path away from the true Q.

## Evidence Limitations

4.5% are inspired by these failure paths and report improvements on the same batch of simulated samples. The paper does not:

- Independent verification threshold;
- Compare other thresholds;
- Give asymptotic selection rules;
- Report the average entry error from true Q;
- Describes the sensitivity of the threshold to the initial number of errors.

Therefore 4.5% should be considered as the rule of thumb in this experiment.
