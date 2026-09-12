# standard error and classification

## Objectives of the appendix

The parameter point is estimated as

\[
\widehat{\boldsymbol\beta}
=
(\widehat g_1,\widehat s_1,\ldots,\widehat g_J,\widehat s_J)^\mathsf T.
\]

The appendix uses a marginal-score outer-product approximation to information, then approximates covariance. This is not a finite-sample identity with the exact negative Hessian:

\[
\widehat{\operatorname{Cov}}
(\widehat{\boldsymbol\beta})
\approx
\mathcal I(\widehat{\boldsymbol\beta})^{-1}.
\tag{13}
\]

The standard error is the square root of the diagonal element of the inverse matrix.

## Press the attribute posterior to the ideal state of the item

definition

\[
p_j(z\mid\boldsymbol X_i)
=
\sum_{l:\eta_{lj}=z}
P(\boldsymbol\alpha_l\mid\boldsymbol X_i).
\tag{14}
\]

It represents the posterior probability that the student is in the ideal state \(z\) on question \(j\), given the student's complete response vector.

## Expected score of a single student on the parameter

Order

\[
P_j(0)=g_j,
\qquad
P_j(1)=1-s_j.
\]

For \(\beta_{j0}=g_j\):

\[
u_{i,j0}
=
p_j(0\mid\boldsymbol X_i)
\frac{
X_{ij}-g_j
}{
g_j(1-g_j)
}.
\tag{15}
\]

For \(\beta_{j1}=s_j\), because

\[
\frac{\partial(1-s_j)}{\partial s_j}=-1,
\]

Got:

\[
u_{i,j1}
=
p_j(1\mid\boldsymbol X_i)
\frac{
(1-s_j)-X_{ij}
}{
(1-s_j)s_j
}.
\tag{16}
\]

## Equation A15

Arrange all \(2J\) parameter scores into vector \(\boldsymbol u_i\). A15 of the paper can be written as:

\[
\mathcal I(\widehat{\boldsymbol\beta})
\approx
\sum_{i=1}^{I}
\boldsymbol u_i\boldsymbol u_i^\mathsf T
\bigg|_{\boldsymbol\beta=\widehat{\boldsymbol\beta}}.
\tag{17}
\]

This will produce a

\[
2J\times2J
\]

The information matrix contains cross-parameter information terms; its inverse, not the information matrix itself, approximates covariance.

## Why can’t we just use two binomial distribution formulas?

If each person’s \(\eta_{ij}\) is known, it can be approximately written

\[
\operatorname{SE}(\widehat g_j)
\approx
\sqrt{
\frac{g_j(1-g_j)}{I_j^{(0)}}
}.
\]

In DINA, \(\eta_{ij}\) is a posteriori uncertain, and the same attribute profile affects multiple questions at the same time. A15 preserves this part of the dependence through full posteriors and cross products.

## How to verify standard error in simulation

In 100 repetitions, the paper compares:

- The standard error of the model obtained from each fitting is then averaged;
- Empirical standard deviation of 100 parameter estimates.

The two are very close. The paper reports that the model standard error is on average about 2% more conservative than the empirical standard deviation.

## Boundary estimation

The DINA result of real data Item 1 is

\[
\widehat g_1=0.00,
\qquad
\operatorname{SE}(\widehat g_1)=0.050.
\]

When the parameter is close to 0 or 1:

- The normal approximation may be asymmetric;
- The information matrix may be pathological;
- Different priors or constraints will significantly affect the result;
- The Wald interval may exceed \([0,1]\).

In Table 4, HO-DINA gives a standard error of 0.004 for the same \(g_1\), showing that the latent variable distribution and Bayesian estimation will change the uncertainty near the boundary.

## attribute profile classification

EM has been generated

\[
w_{il}
=
P(\boldsymbol\alpha_l\mid\boldsymbol X_i).
\]

It can be defined accordingly:

### MAP mode classification

\[
\widehat l_i^{\text{MAP}}
=
\arg\max_l w_{il}.
\]

### Single attribute EAP

\[
\widehat P(\alpha_{ik}=1\mid\boldsymbol X_i)
=
\sum_{l:\alpha_{lk}=1}
w_{il}.
\]

This article mainly studies the calibration of item parameters. The discussion section clearly lists pattern identifiability, classification methods, test length, and Q matrix specifications as follow-up issues that require systematic study.

## Deriving the marginal score

For fixed \(\pi\), \(m_i=\sum_l\pi_lL_i(l)\), and

\[
\partial_{\beta_r}\log m_i
=\sum_l\frac{\pi_lL_i(l)}{m_i}\partial_{\beta_r}\log L_i(l).
\]

The weights are exactly the posterior. Group0 contributes to g, group1 to s, with the negative derivative of \(\log(1-s)\) accounted for.

At the initial parameters, student1 of the worked example has the interleaved score

\[
u_i\approx(.669915,-.962241,-.669915,1.985384,2.509135,-.438490).
\]

For example \(u_{g_1}=(1-.866017052)(1-.2)/[.2(.8)]\).
Compute each student's outer product and then sum, not the outer product of the summed scores. Standard errors require evaluation at fitted parameters, not these illustrative initial ones.

## Three information concepts

The exact observed information is the negative Hessian. OPG is \(\sum_i u_i u_i^\mathsf T\). Their expectations agree under appropriate regularity and correct specification, but the two finite-sample matrices generally differ. Appendix A12–A15 uses an expectation argument followed by an empirical approximation.

For the purely illustrative matrix

\[
I=\begin{pmatrix}4&1\\1&9\end{pmatrix},\qquad
I^{-1}=\frac1{35}\begin{pmatrix}9&-1\\-1&4\end{pmatrix},
\]

SEs are \(\sqrt{9/35}\) and \(\sqrt{4/35}\), not the reciprocal square roots of I's diagonal. Invert the whole matrix first.

The four-person example has six item parameters and OPG rank at most4, so it cannot provide six valid OPG SEs. A numerical ridge is not a substitute for identified information.

If mixing proportions are estimated, uncertainty should also account for their \(L-1\) free parameters. The existing item-only script does not do this automatically.

## MAP and marginal decisions differ

For posterior \((.35,.25,.10,.30)\) in order00,01,10,11, MAP is00, while marginal mastery probabilities .40,.55 produce01 at a .5 threshold. Whole-profile and attribute-wise decisions target different losses. Tie handling must also be specified.
