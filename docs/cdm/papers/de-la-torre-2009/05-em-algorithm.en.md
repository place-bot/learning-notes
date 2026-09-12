# EM complete derivation

## missing data

Record the indicator variable that student \(i\) belongs to attribute profile \(l\) as

\[
Z_{il}
=
\mathbf 1(
\boldsymbol\alpha_i=\boldsymbol\alpha_l
).
\]

If \(Z_{il}\) is known, guess and slip are grouped Bernoulli proportions. For EM

\[
w_{il}
=
E(Z_{il}\mid\boldsymbol X_i)
=
P(\boldsymbol\alpha_l\mid\boldsymbol X_i)
\]

Substitute for the unknown indicator variable.

## E step

According to Bayes formula:

\[
w_{il}
=
\frac{
\pi_l
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
}{
\sum_{h=1}^{L}
\pi_h
L(\boldsymbol X_i\mid\boldsymbol\alpha_h)
}.
\tag{7}
\]

For each student:

\[
\sum_{l=1}^{L}w_{il}=1.
\]

## Aggregate the expected number of people according to the ideal state

For item \(j\) and status \(z\in\{0,1\}\), define:

\[
I_j^{(z)}
=
\sum_{i=1}^{I}
\sum_{l:\eta_{lj}=z}
w_{il},
\tag{8}
\]

That is, the ideal number of people expected is \(z\).

The expected number of correct answers is

\[
R_j^{(z)}
=
\sum_{i=1}^{I}
\sum_{l:\eta_{lj}=z}
w_{il}X_{ij}.
\tag{9}
\]

and

\[
I_j^{(0)}+I_j^{(1)}=I.
\]

## Step M: Update guessing

For the \(\eta=0\) group, the probability of correct answer is \(g_j\). Appendix Equation A10 gives:

\[
\widehat g_j
=
\frac{R_j^{(0)}}{I_j^{(0)}}.
\tag{10}
\]

It is "the expected proportion of correct answers among those who do not master all required attributes."

## Step M: Update slipping

For the \(\eta=1\) group, the probability of an incorrect answer is \(s_j\). Equation A11 gives:

\[
\widehat s_j
=
\frac{
I_j^{(1)}-R_j^{(1)}
}{
I_j^{(1)}
}.
\tag{11}
\]

It is "the expected proportion of incorrect answers among those who master all required attributes."

## Complete algorithm

1. Given an initial \(g_j^{(0)},s_j^{(0)}\) and a fixed pattern prior \(\pi_l\).
2. Calculate all \(w_{il}\) using current parameters.
3. Calculate \(I_j^{(0)},R_j^{(0)},I_j^{(1)},R_j^{(1)}\).
4. Use equations (10)--(11) to update all item parameters.
5. Calculate the maximum absolute difference between the parameters of the two rounds before and after.
6. If the threshold is not reached, return to step 2.

Thesis simulation uses:

\[
\max_m
|\beta_m^{(t+1)}-\beta_m^{(t)}|
<0.0001
\]

as a convergence criterion.

## Why does step M have a closed form solution?

After step E, each question is split into two weighted Bernoulli samples:

- \(\eta=0\) group estimated success rate \(g_j\);
- \(\eta=1\) Group estimated failure rate \(s_j\).

Bernoulli maximum likelihood is simply the weighted number of successes divided by the weighted total number, so no numerical optimizer is needed.

## Fixed priors and empirical Bayes extensions

The underlying algorithm of the paper uses the same set of \(\pi_l\) in each round. Suggested updates to the discussion section:

\[
\widehat\pi_l
=
\frac{1}{I}
\sum_{i=1}^{I}
w_{il}.
\tag{12}
\]

This extends the algorithm to simultaneously estimate saturated attribute profile proportions.

The script of this site reproduces the fixed uniform prior by default; plus

```bash
--update-prior
```

(12) is executed and marked as an extension of the paper discussion.

## Computational complexity

The E step in each round must be correct

\[
I\times 2^K\times J
\]

Calculating the probability of a student-category-item combination, the main complexity is

\[
O(IJ2^K).
\]

This explains the paper's concerns about the larger \(K\). The M-step aggregation expectation count also relies on the same posterior matrix, but is generally less expensive than the E-step likelihood calculation.

## Derive the auxiliary objective rather than jump to the ratios

Let \(\beta=(g_1,s_1,\ldots,g_J,s_J)\). The complete-data log likelihood is

\[
\ell_c=\sum_{il}Z_{il}\left[\log\pi_l+
\sum_j\{X_{ij}\log P_j(l)+(1-X_{ij})\log(1-P_j(l))\}\right].
\]

Take its conditional expectation under the old parameters. Linearity replaces \(Z_{il}\) with \(w_{il}^{(t)}\), giving the auxiliary objective \(\mathcal Q\), distinct from the item Q-matrix.

Collecting terms for item j yields

\[
\begin{aligned}
\mathcal Q_j={}&R_j^{(0)}\log g_j+
(I_j^{(0)}-R_j^{(0)})\log(1-g_j)\\
&+R_j^{(1)}\log(1-s_j)+
(I_j^{(1)}-R_j^{(1)})\log s_j.
\end{aligned}
\]

Counts use the old posterior and are constants throughout this M-step. Therefore

\[
\frac{\partial\mathcal Q_j}{\partial g_j}
=\frac{R_j^{(0)}}{g_j}
-\frac{I_j^{(0)}-R_j^{(0)}}{1-g_j}=0.
\]

Multiply by \(g_j(1-g_j)\) and cancel cross terms:

\[
R_j^{(0)}-g_jI_j^{(0)}=0.
\]

Likewise,

\[
-\frac{R_j^{(1)}}{1-s_j}
+\frac{I_j^{(1)}-R_j^{(1)}}{s_j}=0
\]

reduces to \(I_j^{(1)}-R_j^{(1)}-s_jI_j^{(1)}=0\).
These give the reported ratios. The second derivatives are nonpositive; an empty group is undefined, while all-correct/all-wrong groups may attain boundary maxima.

Do not differentiate the old posterior within the M-step. Replacing soft weights by MAP assignments is also a different algorithm.

## Derive the optional mixing proportions

With \(n_l=\sum_iw_{il}^{(t)}\), maximize
\(\sum_ln_l\log\pi_l+\lambda(\sum_l\pi_l-1)\).
Stationarity gives \(\pi_l=-n_l/\lambda\); normalization and \(\sum_ln_l=I\) give \(\lambda=-I\). Thus \(\pi_l=n_l/I\). This is optional, not part of the fixed-prior branch.

## Why exact EM is monotone

For each student, Jensen gives

\[
\log\sum_lw^t_{il}\frac{\pi_lL_i(l;\beta)}{w^t_{il}}
\ge\sum_lw^t_{il}\log\frac{\pi_lL_i(l;\beta)}{w^t_{il}}.
\]

Equality holds at the old parameters with the exact posterior. Increasing this lower bound in the M-step cannot decrease the observed likelihood. This requires compatible objectives and constraints; it does not guarantee global optimality.

All items use the same old W within one iteration. Recompute W and the likelihood after the final parameter update, including when reporting nonconvergence at an iteration cap.
