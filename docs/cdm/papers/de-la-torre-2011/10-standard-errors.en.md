# MLE, immutability and standard error

## Information matrix of saturation probability

The paper’s probability vector for item \(j\)

\[
\boldsymbol P_j
\]

Construct the observation information matrix. For the two reduction modes \(\boldsymbol a,\boldsymbol b\), the information element can be written as the sum of the products of the posterior scores:

\[
\mathcal I_{ab}
=
\sum_{i=1}^{I}
u_{ia}u_{ib},
\]

Among them

\[
u_{ia}
=
\tau_{ij}(\boldsymbol a)
\frac{
X_{ij}-P_j(\boldsymbol a)
}{
P_j(\boldsymbol a)
[1-P_j(\boldsymbol a)]
}.
\]

After substituting \(\widehat{\boldsymbol P}_j\),

\[
\widehat{\operatorname{Var}}
(\widehat{\boldsymbol P}_j)
\approx
\mathcal I(\widehat{\boldsymbol P}_j)^{-1}.
\]

The standard error of a single probability is the square root of the corresponding diagonal element of the covariance matrix.

## Why is the saturation parameter also MLE?

For saturated models, the effect parameter is a one-to-one transformation of the probability vector:

\[
\widehat{\boldsymbol\phi}_j
=
f(\widehat{\boldsymbol P}_j).
\]

Due to the immutability of MLE,

\[
\widehat{\boldsymbol P}_j
\text{Yes MLE}
\Longrightarrow
f(\widehat{\boldsymbol P}_j)
\text{is the MLE of the corresponding parameters}.
\]

This applies to:

\[
\widehat{\boldsymbol\delta}_j,
\qquad
\widehat{\boldsymbol\lambda}_j,
\qquad
\widehat{\boldsymbol\nu}_j.
\]

## Multivariate delta method

If

\[
\boldsymbol\phi_j=f(\boldsymbol P_j),
\]

rule

\[
\operatorname{Var}
\left[
f(\widehat{\boldsymbol P}_j)
\right]
\approx
G_j
\operatorname{Var}(\widehat{\boldsymbol P}_j)
G_j^\top,
\]

Among them

\[
G_j
=
\left.
\frac{\partial f(\boldsymbol P_j)}
{\partial\boldsymbol P_j^\top}
\right|_{\widehat{\boldsymbol P}_j}.
\]

Under identity link,

\[
G_j=(M_j^{(S)})^{-1}.
\]

logit and log link are also multiplied by the corresponding element-wise derivatives:

\[
\frac{d\,\operatorname{logit}(P)}{dP}
=
\frac{1}{P(1-P)},
\qquad
\frac{d\log P}{dP}
=
\frac{1}{P}.
\]

## The influence of boundary probability

When \(\widehat P\) is close to 0 or 1:

- logit and log derivatives will quickly become large;
- The covariance matrix may be ill-conditioned;
- Wald approximation may be unstable;
- The effective sample size of some reduction groups may be small.

Therefore, the numerical computability and asymptotic reliability of standard error need to be judged separately.

## The paper has not completed verification

The paper points out that systematic research is still needed:

- Accuracy of parameters and SE under different sample sizes;
- Performance when attribute distribution is uneven;
- \(K_j^*\) The quality of the Wald approximation when growing;
- Statistical properties of two-step estimates of the non-special reduction class.

These contents belong to the research agenda proposed in the paper, and the simulation part only directly verifies some properties of the A-CDM Wald test.
