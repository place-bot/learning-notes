# Experiment：G-DINA Studies VI--VII

## Study VI: Severe non-recognition

### 1. Three true Qs

The authors used \(Q^1,Q^2,Q^3\) to generate the data. They respectively represent:

- All-zero column or extreme single-column structure;
- The number of measurements of a certain attribute is insufficient;
- Pan-complete or duplicate condition failed.

sample size is still

\[
N=10^5.
\]

### 2. result

None of the three true Qs maximize candidate likelihood.

In the \(Q^2\) scenario, out of 121 fits only the estimated parameters of the true \(Q^2\) and the alternative \(Q^{56}\) pass strong monotonic filtering; among them, the likelihood of \(Q^{56}\) is higher.

This shows that the monotonicity constraint itself cannot repair structural non-recognition.

## Study VII: Construct 70 sets of alternative parameters

### 1. Two scales

\[
(K,J)=(3,20)
\quad\text{with}\quad
(5,20).
\]

True Q's first property is measured only by the first two questions, violating Condition C.

### 2. True parameters

The latent class ratio is set to

\[
p_{\boldsymbol\alpha}=2^{-K}.
\]

Each question:

\[
\theta_{j,\boldsymbol0}=0.2,
\qquad
\theta_{j,\boldsymbol1}=0.8,
\]

The main effect and interaction effect adopt equal incremental construction.

### 3. Alternative parameters

The author changed some parameters of the first two questions of Q and added small random perturbations in the true value neighborhood:

\[
\bar\Theta^{(\ell)}_{i,j}
=
\Theta_{i,j}+U(-0.1,0.1),
\]

Then use the equations in the proof to solve the remaining item parameters and

\[
\bar{\boldsymbol p}^{(\ell)}.
\]

70 sets of alternatives were screened out that satisfied the probability range and monotonicity.

### 4. \(K=3\) result

All 70 sets of parameters are different from the true parameters, and the maximum difference of the complete response distribution is

\[
\max_{1\le\ell\le70}
\max_{\boldsymbol r\in\{0,1\}^{20}}
\left|
\Pr_Q(\boldsymbol r)
-\Pr_{\bar Q,\ell}(\boldsymbol r)
\right|
=1.30\times10^{-18}.
\]

### 5. \(K=5\) result

The corresponding maximum difference is

\[
5.42\times10^{-19}.
\]

### 6. Analysis

Study VII rules out the explanation of accidental numerical collisions. The perturbation parameters can be changed continuously,70 just for visual sampling; the theoretical construction allows any number of sets of alternative parameters.

Therefore, when C is violated, the unrecognizable set has local continuous dimensions, and generally RLCM cannot achieve universal recognition.

## Differences in evidence between two studies

| Study |evidence|
| --- | --- |
| VI |True Q fails in finite sample likelihood search|
| VII |Different parameters achieve equal machine accuracy for the complete population distribution|

Study VII is more direct about the structural mechanism of Theorem 3, and Study VI shows how this mechanism affects actual likelihood selection.
