# Empirical moment \(\boldsymbol\alpha\) and overall mapping

## Each T row has an observation corresponding quantity

If a row of \(T(Q)\) corresponds to

\[
I_{i_1}\wedge\cdots\wedge I_{i_\ell},
\]

Then record the number of people in the sample who answered all these questions correctly:

\[
N_{I_{i_1}\wedge\cdots\wedge I_{i_\ell}}
=
\sum_{r=1}^N
\prod_{h=1}^{\ell}
\mathbf 1(R_r^{i_h}=1).
\]

The original text expresses the same event using a collection of indicator functions. Writing the product more directly shows "all 1's".

The corresponding empirical joint correct answer rate is

\[
\alpha_{i_1,\ldots,i_\ell}
=
\frac{
N_{I_{i_1}\wedge\cdots\wedge I_{i_\ell}}
}{N}.
\]

Stack the proportions of all selected question groups in row order of \(T(Q)\) to get

\[
\boldsymbol\alpha.
\]

## \(\boldsymbol\alpha\) fully observable

\(\boldsymbol\alpha\) only requires a binary response matrix. It does not need to know:

- Which attribute profile does the student belong to;
- attribute profile ratio;
- True Q;
- Attribute classification of individual students.

Therefore it is suitable as a common observation target faced by candidate Q.

## Identities without noise

The proportion of non-zero attribute profiles in the sample is written

\[
\widehat{\boldsymbol p}
=
(\widehat p_{\boldsymbol A}:
\boldsymbol A\in\{0,1\}^k\setminus\{\boldsymbol0\}).
\]

Under \(R^i=\xi^i\),

\[
T(Q)\widehat{\boldsymbol p}
=
\boldsymbol\alpha.
\tag{2.5}
\]

This equation can be proven line by line. Take any question group \(S=\{i_1,\ldots,i_\ell\}\), and the corresponding component on the left is

\[
\sum_{\boldsymbol A\ne\boldsymbol0}
B_Q(I_{i_1}\wedge\cdots\wedge I_{i_\ell})_{\boldsymbol A}
\widehat p_{\boldsymbol A}.
\]

The B-vector takes 1 for the pattern that can complete the entire set of questions and 0 for the remaining patterns, so the sum is exactly equal to the proportion of people in the sample who can complete the set of questions. "Able to complete" without noise is the same as "actually all correct answers", so it is equal to the corresponding \(\alpha\).

## Overall version

According to the law of large numbers,

\[
\widehat{\boldsymbol p}
\overset{\text{a.s.}}{\longrightarrow}
\boldsymbol p^*,
\]

Thus

\[
\boldsymbol\alpha
=T(Q)\widehat{\boldsymbol p}
\overset{\text{a.s.}}{\longrightarrow}
T(Q)\boldsymbol p^*.
\]

here

\[
\boldsymbol\mu_Q
=T(Q)\boldsymbol p^*
\]

is the overall moment vector determined by Q and the overall attribute distribution.

## Why use all combined correct answer rates?

For \(m\) binary questions, the complete response distribution has \(2^m-1\) free probabilities. Joint positive response probability for all non-empty question sets

\[
\Pr(R^{i_1}=\cdots=R^{i_\ell}=1)
\]

There are also \(2^m-1\), and the complete reaction distribution can be restored through the inclusion-exclusion relationship. Therefore saturated \(\boldsymbol\alpha\) does not actively discard information about the reaction distribution.

## A sample of four people

Suppose the responses to the two questions are

\[
\begin{array}{c|cc}
\text{student}&R^1&R^2\\\hline
1&1&1\\
2&1&0\\
3&0&1\\
4&0&0
\end{array}
\]

rule

\[
\alpha_1=\frac24,\qquad
\alpha_2=\frac24,\qquad
\alpha_{1,2}=\frac14.
\]

If you only look at the margins, you will see that both accuracy rates are \(1/2\). The joint moment then tells us that the proportion of correct answers to both questions at the same time is \(1/4\), thus adding constraints on the underlying structure.

## From identities to estimates

True Q allows a certain probability vector to accurately interpret the noiseless sample moments. For the error candidate \(Q'\), the same explanation generally cannot be established. The next page defines this degree of inexplicability as distance.

[Next page: Objective function, Q estimator and calculation](05-objective-and-estimator.md)
