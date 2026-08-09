# Question-by-question Wald test

## Test target

First fit the saturated G-DINA, and then test the equality constraints of the reduced model \(r\) on item \(j\):

\[
H_0:
R_{jr}
f(\boldsymbol P_j)
=
\boldsymbol 0.
\]

\(f(\boldsymbol P_j)\) can be the probability itself, or an effect parameter on the identity, logit, or log scale.

## Wald Statistics

\[
\begin{aligned}
W
=\;&
\left[
R_{jr}f(\widehat{\boldsymbol P}_j)
\right]^\top\\
&\times
\left\{
R_{jr}
\widehat{\operatorname{Var}}
\left[
f(\widehat{\boldsymbol P}_j)
\right]
R_{jr}^\top
\right\}^{-1}\\
&\times
\left[
R_{jr}f(\widehat{\boldsymbol P}_j)
\right].
\end{aligned}
\]

If the reduced model has \(p\) free parameters, the asymptotic distribution is

\[
W
\overset{a}{\sim}
\chi^2_{2^{K_j^*}-p}.
\]

## Constraints on two-attribute questions

### DINA

\[
P_{00}=P_{10}=P_{01}.
\]

can be written as

\[
R_{\mathrm{DINA}}
\boldsymbol P
=
\begin{pmatrix}
1&-1&0&0\\
0&1&-1&0
\end{pmatrix}
\begin{pmatrix}
P_{00}\\P_{10}\\P_{01}\\P_{11}
\end{pmatrix}
=
\boldsymbol0.
\]

The degrees of freedom are

\[
4-2=2.
\]

### A-CDM

\[
\delta_{12}=0,
\]

Equivalent to

\[
P_{11}-P_{10}-P_{01}+P_{00}=0.
\]

The degrees of freedom are

\[
4-3=1.
\]

## Important computational advantages

The paper's Wald test does not require re-estimation of the reduced model. Just:

1. \(\widehat{\boldsymbol P}_j\) of saturated model;
2. Corresponding covariance matrix;
3. Restriction matrix \(R_{jr}\) of the reduced model.

This allows efficient comparison of multiple candidate models for each question.

## The meaning of statistical decision-making

- Not rejected \(H_0\): The data does not show that this reduction constraint causes significant loss;
- Rejection \(H_0\): At least one of the constrained directions in the saturated model is clearly inconsistent with the reduced model.

It is not rejected that it cannot be shown that cognitive processes are necessarily equivalent to this parsimonious model. Small sample size, sparse patterns, or unstable covariance estimates may reduce test power.

## Multiple comparisons

If multiple questions and multiple models are tested repeatedly, the original significance level will accumulate Type I error. The paper recommends research in the discussion:

- Bonferroni et al. correction for multiple comparisons;
- AIC and other indicators that take into account both complexity and fitting;
- Joint decision-making at the item layer and test layer.

The subsequent `GDINA` software `modelcomp()` has added Holm, Bonferroni, BH, BY and other adjustment methods, and also provides Wald, LR and LM routes. These are subsequent software extensions and cannot be extrapolated to what was already proven in the 2011 paper.
