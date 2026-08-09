#Theorem 2.4: Noiseless Consistency

## Theorem statement

Assume that C1--C5 is established, and the response of the \(r\) student to the \(i\) question satisfies

\[
R_r^i
=\xi_r^i
=
\prod_{j=1}^k(A_r^j)^{Q_{ij}}.
\]

Let \(\widehat Q\) be the solution that minimizes \(S(Q')\) for all \(m\times k\) binary candidate matrices in equation (2.7), then

\[
\lim_{N\to\infty}
\Pr(\widehat Q\sim Q)=1.
\tag{2.14}
\]

redefine

\[
\widetilde{\boldsymbol p}
=
\arg\inf_{\boldsymbol p}
\left\|
T(\widehat Q)\boldsymbol p-\boldsymbol\alpha
\right\|_2^2.
\tag{2.15}
\]

After appropriately rearranging the columns of \(\widehat Q\), for any \(\varepsilon>0\),

\[
\lim_{N\to\infty}
\Pr\!\left(
\|\widetilde{\boldsymbol p}-\boldsymbol p^*\|_2
\le\varepsilon
\right)=1.
\]

## What is the first part talking about?

As the number of students increases:

- The estimated probability that Q falls into the true Q equivalence class approaches 1;
- The names of attribute columns are still freely interchangeable;
- Any structurally non-equivalent Q will eventually be eliminated by moment distance.

This is a consistent conclusion. It does not promise certain recovery under a certain limited \(N\), nor does it give the sample size required to achieve a certain recovery rate.

## What is the second part talking about?

Once the column structure of Q is restored correctly, the full column rank of \(T(Q)\) enables a unique solution to the attribute distribution. So

\[
\widetilde{\boldsymbol p}
\overset{p}{\longrightarrow}
\boldsymbol p^*.
\]

Here the attribute columns must be aligned first. If it is estimated that Q exchanges two columns, the corresponding attribute profile probabilities in \(\widetilde{\boldsymbol p}\) will also be exchanged.

## Four steps of proof

### Step 1: Experience attribute ratio convergence

C3 gives independently and identically distributed samples, so

\[
\widehat{\boldsymbol p}
\overset{\text{a.s.}}{\longrightarrow}
\boldsymbol p^*.
\]

### Step 2: The sample loss of true Q is always 0

\[
\boldsymbol\alpha
=T(Q)\widehat{\boldsymbol p},
\]

So

\[
S(Q)=0.
\]

### Step 3: Error Q maintains a positive distance from the overall moment

Propositions 6.3--6.4 and Corollary 6.5 give:

\[
Q'\not\sim Q
\quad\Longrightarrow\quad
T(Q)\boldsymbol p^*
\notin\mathcal C(T(Q')).
\]

The column space is a finite-dimensional closed set, so there exists \(\delta_{Q'}>0\) such that the false candidate is at least \(\delta_{Q'}\) away from the true total moment.

### Step 4: Candidate Q is limited

When \(m,k\) is fixed, there are only a finite number of binary Qs. Select the minimum interval for all error candidates:

\[
\delta
=
\min_{Q'\not\sim Q}\delta_{Q'}
>0.
\]

Once the empirical moments are close enough to the overall moment, the loss for all false candidates is greater than some positive number, while the loss for true Q is 0. Therefore global minimizers can only come from true equivalence classes.

## Why attribute distribution consistency requires full column rank

When \(\widehat Q=Q\),

\[
T(Q)\widetilde{\boldsymbol p}
=
\boldsymbol\alpha
=
T(Q)\widehat{\boldsymbol p}.
\]

Proposition 6.1 Prove that \(T(Q)\) has full column rank, so

\[
\widetilde{\boldsymbol p}
=
\widehat{\boldsymbol p}.
\]

Combined with \(\widehat{\boldsymbol p}\to\boldsymbol p^*\), the conclusion is obtained.

## This theorem does not cover the error

The noiseless model assumes that ability dictates complete determination of the answer. In the real test, if you can do it but answer it wrong, if you can't but guess it right, it will be destroyed.

\[
T(Q)\widehat{\boldsymbol p}
=\boldsymbol\alpha
\]

The sample-by-sample exact identity of . Section 3 replaces the 0/1 B-vector with the conditional probability of correct answer, turning the equation into a probability matching at the overall level.

[Next page: Known errors and guessing parameter of DINA](10-known-cg-dina.md)
