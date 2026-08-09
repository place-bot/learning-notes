# The necessity of repeatability in general RLCM

## 1. Theorem 3

In general RLCM, Condition C is a necessary condition for joint universal recognition:

\[
\sum_{j=1}^{J}q_{jk}\ge3
\quad
\text{for each}k.
\]

If an attribute is only required by one or two questions, it is legal for any

\[
(\Theta,\boldsymbol p)
\]

There are infinitely many groups

\[
(\bar Q,\bar\Theta,\bar{\boldsymbol p})
\nsim
(Q,\Theta,\boldsymbol p)
\]

gives the same reaction distribution.

## 2. Why is the conclusion strong?

It shows that the missing recognition covers the entire parameter space, rather than a zero test set. Increasing the sample size will not resolve structural ambiguities.

## 3. Structural ideas for the two-question situation

After row and column replacement, attributes that appear only twice are placed in column 1, and related questions are placed in the first two rows:

\[
Q=
\begin{pmatrix}
1&\boldsymbol v_1^\top\\
1&\boldsymbol v_2^\top\\
\boldsymbol0&Q^\star
\end{pmatrix}.
\]

When constructing the substitution matrix, expand the attribute requirements of the first two questions, for example, change part 0 to 1. Then:

1. Keep the parameters of questions 3 to \(J\) unchanged;
2. Select small perturbation on part \(\bar\theta_{j,\alpha}\) of the first two questions;
3. Use linear equations to solve the remaining parameters of the first two questions;
4. Synchronously solve \(\bar{\boldsymbol p}\);
5. When the perturbation is small enough, the probability range and monotonicity still hold.

The free perturbation can take on continuous values, so an infinite number of equivalent models are obtained.

## 4. Why is there an exception to DINA?

DINA has only two probabilities \(c_j,g_j\) for each question, and the parameter restrictions are very strong. Dependencies between attributes can sometimes supplement the information measured by two questions, so Theorem 2 has a general recognition situation.

Generally, RLCM allows the main effect and interaction effect of the required attributes to change freely. The extra degrees of freedom are enough to absorb structural changes, resulting in the two-question measurement being insufficient for general recognition.

## 5. Numerical construction of Study VII

The author sets respectively:

\[
(K,J)=(3,20)
\quad\text{and}\quad
(5,20),
\]

Each scenario constructs 70 sets of alternative parameters. The maximum difference in response probability between all alternative models and the true model is

\[
1.30\times10^{-18}
\quad\text{and}\quad
5.42\times10^{-19},
\]

All are orders of magnitude lower than the MATLAB double-precision machine error.

## 6. Implications of test design

If you plan to use general models such as G-DINA and LCDM and jointly learn Q, the bottom line is to arrange at least three related questions for each attribute. Single attribute questions can be missing, but the number of measurements cannot be reduced to two.
