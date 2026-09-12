# response probability and likelihood

## slipping and guessing

For item \(j\):

\[
s_j
=
P(X_{ij}=0\mid\eta_{ij}=1),
\]

\[
g_j
=
P(X_{ij}=1\mid\eta_{ij}=0).
\]

So

\[
P(X_{ij}=1\mid\eta_{ij}=1)=1-s_j,
\]

\[
P(X_{ij}=0\mid\eta_{ij}=0)=1-g_j.
\]

## Equation 2

\[
P_j(\boldsymbol\alpha_i)
=
P(X_{ij}=1\mid\boldsymbol\alpha_i)
=
g_j^{1-\eta_{ij}}
(1-s_j)^{\eta_{ij}}.
\tag{3}
\]

It depends on the situation:

\[
P_j(\boldsymbol\alpha_i)
=
\begin{cases}
g_j,&\eta_{ij}=0,\\
1-s_j,&\eta_{ij}=1.
\end{cases}
\]

When there is no noise \(g_j=s_j=0\), the observed response is equal to the ideal response. Actual models allow for two types of deviations.

usually hope

\[
1-s_j>g_j,
\]

In this way, those who master all the required attributes are more likely to answer correctly. The updated equations in the appendix of this paper do not additionally derive this inequality constraint; whether the software implementation enforces monotonicity needs to be checked separately.

## The item likelihood of a given attribute profile

Reaction vector for student \(i\)

\[
\boldsymbol X_i=(X_{i1},\ldots,X_{iJ}),
\]

After given \(\boldsymbol\alpha_i\), it is assumed that the items are locally independent:

\[
L(\boldsymbol X_i\mid\boldsymbol\alpha_i)
=
\prod_{j=1}^{J}
P_j(\boldsymbol\alpha_i)^{X_{ij}}
\left[
1-P_j(\boldsymbol\alpha_i)
\right]^{1-X_{ij}}.
\tag{4}
\]

Local independence decomposes a student's joint response probability into \(J\) Bernoulli terms.

## When attribute profile is known

If all \(\boldsymbol\alpha_i\) are known, the students for each question can be divided into:

- \(\eta_{ij}=0\) group;
- \(\eta_{ij}=1\) group.

At this time

\[
\widehat g_j
=
\frac{\eta_{ij}=0\text{The number of correct answers in the group}}
{\eta_{ij}=0\text{Group size}},
\]

\[
\widehat s_j
=
\frac{\eta_{ij}=1\text{Number of wrong answers in the group}}
{\eta_{ij}=1\text{Group size}}.
\]

EM just replaces the unknown group with the posterior expected number of people.

## marginal likelihood

attribute profile is unknown. enumeration

\[
\boldsymbol\alpha_1,\ldots,\boldsymbol\alpha_L,
\qquad L=2^K,
\]

co-located

\[
\pi_l=P(\boldsymbol\alpha_l).
\]

The marginal likelihood of a single student is

\[
L(\boldsymbol X_i)
=
\sum_{l=1}^{L}
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
\pi_l.
\tag{5}
\]

Full sample likelihood:

\[
L(X)
=
\prod_{i=1}^{I}
\sum_{l=1}^{L}
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
\pi_l.
\tag{6}
\]

This is a finite mixture model with class \(2^K\) and class conditional probabilities constrained by DINA.

## Logarithmic form

Numerical implementation uses

\[
\ell(X)
=
\sum_{i=1}^{I}
\log
\left[
\sum_{l=1}^{L}
\pi_l
\exp\{
\ell_{il}^{\text{conditional}}
\}
\right].
\]

To prevent many small probability multiplications from underflowing, the code uses log-sum-exp:

\[
\log\sum_l e^{a_l}
=
m+\log\sum_l e^{a_l-m},
\qquad
m=\max_l a_l.
\]

This is a numerical implementation detail. The original article uses a product formula to express the statistical model.

## Conditional likelihood, weighted likelihood, marginal probability

For response101 and candidate10 in the worked example:

\[
L_i(10)=.2025,\quad \pi_{10}L_i(10)=.050625,\quad
m_i=\sum_l\pi_lL_i(l)=.102625.
\]

The posterior is .050625/.102625=.493300853. The unweighted likelihood sum .4105 is not the marginal; the prior factor .25 cancels for posterior normalization but not for computing \(\log m_i\).

Multiply across items conditional on one shared profile, then sum across mutually exclusive profiles. Multiplying itemwise marginal probabilities instead would effectively allow a new profile for every item.

With \(a_l=\log\pi_l+\log L_i(l)\) and \(b=\max_la_l\),

\[
\sum_le^{a_l}=e^b\sum_le^{a_l-b}.
\]

Thus posterior normalization can use \(e^{a_l-b}\). Values -1000,-1001 become 1 and \(e^{-1}\) after shifting, preserving posterior probabilities while preventing underflow.

A genuinely zero prior corresponds to log weight \(-\infty\). The teaching program floors prior probabilities, so forbidden profiles require an explicit implementation change rather than this numerical floor.
