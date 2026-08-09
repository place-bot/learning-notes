#MMLE and EM

## marginal likelihood

Assume \(I\) students, \(J\) questions, and \(L=2^K\) complete attribute profiles. The reaction vector of student \(i\) is

\[
\boldsymbol X_i=(X_{i1},\ldots,X_{iJ}).
\]

Given attribute profile \(\boldsymbol\alpha_l\), the local independent likelihood is

\[
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
=
\prod_{j=1}^{J}
P(\boldsymbol\alpha^*_{lj})^{X_{ij}}
\left[
1-P(\boldsymbol\alpha^*_{lj})
\right]^{1-X_{ij}}.
\]

The marginal likelihood integrates the attribute profile:

\[
L(\boldsymbol X)
=
\prod_{i=1}^{I}
\sum_{l=1}^{L}
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
p(\boldsymbol\alpha_l).
\]

The paper maximizes its logarithm to obtain marginal maximum likelihood estimates.

## Step E: Complete model posterior

\[
\tau_{il}
=
P(\boldsymbol\alpha_l\mid\boldsymbol X_i)
=
\frac{
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
p(\boldsymbol\alpha_l)
}{
\sum_{l'=1}^{L}
L(\boldsymbol X_i\mid\boldsymbol\alpha_{l'})
p(\boldsymbol\alpha_{l'})
}.
\]

A certain item only cares about the reduction mode \(\boldsymbol a\). So sum up the posteriors of all complete modes that map to \(\boldsymbol a\):

\[
\tau_{ij}(\boldsymbol a)
=
\sum_{l:
\boldsymbol\alpha^*_{lj}=\boldsymbol a}
\tau_{il}.
\]

## M step: closed-form update of probability

Thesis definition

\[
I_{\boldsymbol a j}
=
\sum_{i=1}^{I}
\tau_{ij}(\boldsymbol a)
\]

Reduce the expected number of people in group \(\boldsymbol a\) for item \(j\) and define

\[
R_{\boldsymbol a j}
=
\sum_{i=1}^{I}
\tau_{ij}(\boldsymbol a)X_{ij}
\]

The expected number of correct answers for the group.

So

\[
\widehat P_j(\boldsymbol a)
=
\frac{
R_{\boldsymbol a j}
}{
I_{\boldsymbol a j}
}.
\]

This is the paper formula (15).

## Why updates are easy

Within the reduction group, item responses obey the Bernoulli model of shared success probabilities. If the identity of the group members is known, MLE is the proportion of correct answers; EM replaces the unknown group member indicator variable with the posterior probability, thus obtaining the expected number of correct answers divided by the expected number of people.

## attribute profile distribution

Saturated attribute distributions can be used

\[
\widehat p(\boldsymbol\alpha_l)
=
\frac{1}{I}
\sum_{i=1}^{I}\tau_{il}
\]

Update. The paper also discusses the use when \(K\) is very large:

- higher-order latent trait；
- attribute hierarchy;
- Other structured distributions.

These structures can reduce the calculation and sample size pressure caused by \(2^K\) pattern probabilities.

## Key points of numerical implementation

Multiplying a large number of probabilities directly will underflow. Code usually uses

\[
\log L
=
\sum_j
\left[
X_{ij}\log P_{lj}
+(1-X_{ij})\log(1-P_{lj})
\right]
\]

And normalize the posterior with log-sum-exp.

Still need to deal with:

- Probability is close to 0 or 1;
- The expected number of people in the reduced group is too small;
- Multiple starting points;
- Monotonic constraints;
- Iteration upper bounds and convergence criteria.

## RELATIONSHIP TO 2009 DINA EM

Both papers use the same EM logic. The difference is concentrated in the M steps of each question:

|model|Reduction group for each question|
| --- | ---: |
| DINA | 2 |
| G-DINA | \(2^{K_j^*}\) |

G-DINA retains more groups, so it can discover attribute main effects and interactions, and also requires more data.
