# Summary and further reading

## A main line

\[
\text{Initial Q-fit DINA}
\rightarrow
\widehat P(\boldsymbol\alpha\mid\boldsymbol X)
\rightarrow
(N_{jl},R_{jl})
\rightarrow
\widehat\delta_j(\boldsymbol q)
\rightarrow
\text{sequential search}
\rightarrow
\widehat Q(\varepsilon)
\rightarrow
\text{Additional EM and expert review}.
\]

## Five core formulas

### ideal response

\[
\eta_l(\boldsymbol q)
=
\prod_{k=1}^{K}\alpha_{lk}^{q_k}.
\]

### Candidate guessing

\[
\widehat g
=
\frac{R^{(0)}}{N^{(0)}}.
\]

### Candidate slipping

\[
\widehat s
=
\frac{N^{(1)}-R^{(1)}}{N^{(1)}}.
\]

### Candidate Discrimination

\[
\widehat\delta
=
1-\widehat s-\widehat g.
\]

### Add attribute guidelines

\[
\widehat\delta^{(s)}
-
\widehat\delta^{(s-1)}
>
\varepsilon.
\]

## Conclusion of the original three experiments

|experiment|Main result|cannot be launched|
| --- | --- | --- |
|Simulation|Recover all erroneous rows and keep all correct rows under current 12 conditions|In general, the error rate is always 0|
|Fraction subtraction|\(\varepsilon=.009\)--.012 Keep the original Q intact|The original Q is a real cognitive structure in all groups|
| NAEP |Optimal \(\bar g+\bar s\) dropped from .6923 to .6847|Q modification has solved the obvious model mismatch|

## The most important substantive conclusion

In the counterexample of fraction subtraction, after adding irrelevant attribute 5 to question 1:

\[
\bar g+\bar s:.2461\rightarrow.2379.
\]

Statistical indicators improve, but content interpretation worsens. Q matrix verification requires putting two types of evidence into the same decision:

\[
\text{response-data evidence}
+
\text{substantive evidence}.
\]

## Original algorithm and current CDM package

|aspects|Original text| `CDM::din.validate.qmatrix()` |
| --- | --- | --- |
|candidate search|Add attributes step by step|Enumerate all non-zero vectors|
|number of candidates|Up to \(K(K+1)/2\)| \(2^K-1\) |
|threshold|Adjacent step increment|IDI improvement of the candidate relative to the original row|
|posterior count| EM expected counts |same thought|
|final comparison|More \(\varepsilon\), additional EM, content review|Return to the suggestion Q, which needs to be completed by the user later.|

## Relationship to subsequent papers

Suggested reading for the next article:

[de la Torre & Chiu (2016): General Empirical Q Matrix Validation](../de-la-torre-chiu-2016/index.md)

Key comparisons:

- Why the 2008 method relies on DINA;
- How to adapt the general discrimination index to a wider CDM;
- How to deal with the local path problem of sequential search;
- How to explain cutoff;
- How posterior error and multi-attribute items affect recovery.

Read further:

1. Chiu (2013): Residual-based statistical Q-refinement;
2. Liu, Xu and Ying (2012, 2013): Data-driven Q learning and theory;
3. Chen et al. (2018)：Bayesian DINA Q estimation；
4. Gu and Xu (2021): Necessary and sufficient conditions for Q itself to be identifiable.

## Boundary to CAT

This article does not include real-time topic selection, stopping rules, or test sequence generation on a student-by-student basis. It handles the "what cognitive attributes the item requires" layer in the item bank. For cognitive CAT, the validated Q goes into:

- Student attribute posterior;
- Probability of success for candidate questions;
- Attribute coverage constraints;
- Diagnostic information and topic selection utility.

Therefore it is the model foundation document of adaptive policy.
