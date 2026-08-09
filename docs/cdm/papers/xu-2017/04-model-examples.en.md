# How does the six-category diagnostic model enter the framework?

The paper uses six model examples to illustrate the coverage of equations (2.2)--(2.3).

## DINA

The ideal response indicator is

\[
\xi^{\mathrm{DINA}}_{j,\boldsymbol\alpha}
=
\mathbb I(\boldsymbol\alpha\succeq\boldsymbol q_j).
\]

Add noise with the error parameter \(s_j\) and guessing parameter \(g_j\):

\[
\theta_{j,\boldsymbol\alpha}
=
(1-s_j)^{
\xi^{\mathrm{DINA}}_{j,\boldsymbol\alpha}}
g_j^{
1-\xi^{\mathrm{DINA}}_{j,\boldsymbol\alpha}}.
\]

Therefore

\[
\theta_{j,\boldsymbol\alpha}
=
\begin{cases}
1-s_j,&\boldsymbol\alpha\succeq\boldsymbol q_j,\\
g_j,&\boldsymbol\alpha\nsucceq\boldsymbol q_j.
\end{cases}
\]

Equations (2.2)--(2.3) correspond to \(1-s_j>g_j\) in DINA.

## DINO

DINO uses disjunctive gates. As long as at least one of the required attributes is mastered, the ideal response is 1:

\[
\xi^{\mathrm{DINO}}_{j,\boldsymbol\alpha}
=
\mathbb I
\left(
\exists k:\ q_{jk}=1,\ \alpha_k=1
\right).
\]

The success probability still consists of two groups: \(1-s_j\) and \(g_j\). For single-attribute questions, the ideal grouping of DINA and DINO is consistent, so equation (2.3) is also guaranteed by \(1-s_j>g_j\).

## G-DINA

identity-link G-DINA expands the main effect of the required attributes and all interaction effects:

\[
\theta_{j,\boldsymbol\alpha}
=
\beta_{j0}
+
\sum_k\beta_{jk}q_{jk}\alpha_k
+
\sum_{k<k'}
\beta_{jkk'}
(q_{jk}\alpha_k)(q_{jk'}\alpha_{k'})
+
\cdots.
\]

Attributes not required by \(\boldsymbol q_j\) will not enter the response function of this question. As long as the two attribute profiles have the same reduction pattern on the attributes required for the question, they have the same probability of success.

## Linear logistic model / logit-CDM

\[
\operatorname{logit}
\theta_{j,\boldsymbol\alpha}
=
\beta_{j0}
+
\sum_{k=1}^K
\beta_{jk}q_{jk}\alpha_k.
\]

The equivalent probability form is

\[
\theta_{j,\boldsymbol\alpha}
=
\frac{
\exp\left(
\beta_{j0}+\sum_k\beta_{jk}q_{jk}\alpha_k
\right)}
{1+
\exp\left(
\beta_{j0}+\sum_k\beta_{jk}q_{jk}\alpha_k
\right)}.
\]

It is also called compensatory RUM.

## reduced RUM / log-CDM

\[
\theta_{j,\boldsymbol\alpha}
=
\pi_j
\prod_{k=1}^K
r_{jk}^{\,q_{jk}(1-\alpha_k)},
\qquad 0<r_{jk}<1.
\]

\(\pi_j\) is the probability of success when all required attributes are present; each missing attribute is multiplied by a penalty less than 1. Taking the logarithm gives us the additive form:

\[
\log\theta_{j,\boldsymbol\alpha}
=
\beta_{j0}
+
\sum_k\beta_{jk}q_{jk}\alpha_k.
\]

## Wider model family listed in the paper

The text also mentions NIDA, NIDO, fusion model, rule-space method, attribute hierarchy method and general diagnostic model. The main theorem does not depend on a specific link function, as long as \(\Theta\) satisfies the restriction formula of the paper.

## Unified perspective

|model|Ability sufficient group|Incompetent group|In-question parameterization|
| --- | --- | --- | --- |
| DINA |a high probability|a common low probability|two parameters|
| DINO |At least one required attribute is high|a common low probability|two parameters|
| G-DINA |All required attributes reach the common maximum|There can be multiple probabilities|main effect and interaction|
| logit-CDM |All required attributes reach the common maximum|Changes with mastery of combinations|logit addition|
| reduced RUM |All required attributes are \(\pi_j\)|Multiply penalty by missing attribute|log addition|

The paper identifies \(\Theta\) and \(\boldsymbol p\) in the unified representation. Within a specific model, if the parameterization from model parameters to \(\Theta\) is itself one-to-one, the corresponding \(s,g,\beta,\pi,r\) and other parameters can be further identified.
