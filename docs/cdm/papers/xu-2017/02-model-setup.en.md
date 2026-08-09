# RLCM model and local independence

## Observe reactions

The response vector of a participant to question \(J\) is

\[
\boldsymbol R=(R_1,\ldots,R_J)^\top,
\qquad R_j\in\{0,1\}.
\]

\(R_j=1\) indicates a positive response to question \(j\), which usually indicates a correct answer in educational measurement.

## Potential attribute profile

participant has \(K\) binary attributes:

\[
\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_K)^\top
\in\{0,1\}^K.
\]

\(\alpha_k=1\) means mastering the \(k\) attribute. There are \(2^K\) potential classes. The proportion of attribute profile in the group is

\[
p_{\boldsymbol\alpha}
=P(\boldsymbol\alpha_i=\boldsymbol\alpha),
\qquad
p_{\boldsymbol\alpha}>0,
\qquad
\sum_{\boldsymbol\alpha}p_{\boldsymbol\alpha}=1.
\]

The paper arranges all the proportions into

\[
\boldsymbol p
=
\left(
p_{\boldsymbol\alpha}:
\boldsymbol\alpha\in\{0,1\}^K
\right)^\top.
\]

The strict proportionality assumption is important: the isolation equation in the proof requires that each latent class has positive mass. When allowing structure zero, additional identification analysis must be done.

## Conditional response probability

Given the attribute profile, the positive response probability of question \(j\) is

\[
\theta_{j,\boldsymbol\alpha}
=P(R_j=1\mid\boldsymbol\alpha).
\]

So

\[
P(R_j=r\mid\boldsymbol\alpha)
=
\theta_{j,\boldsymbol\alpha}^{\,r}
(1-\theta_{j,\boldsymbol\alpha})^{1-r},
\qquad r\in\{0,1\}.
\]

Rank the probabilities of all items and potential classes

\[
\Theta
=
\left(\theta_{j,\boldsymbol\alpha}\right)_
{J\times 2^K}.
\]

Rows correspond to items, and columns correspond to attribute profiles.

## Partially independent

The joint response probability of the paper uses the Bernoulli product:

\[
P(\boldsymbol R=\boldsymbol r
\mid\boldsymbol\alpha,Q,\Theta)
=
\pi_{\boldsymbol r,\boldsymbol\alpha}(Q,\Theta)
=
\prod_{j=1}^J
(1-\theta_{j,\boldsymbol\alpha})^{1-r_j}
\theta_{j,\boldsymbol\alpha}^{r_j}.
\]

This means that given \(\boldsymbol\alpha\), the reaction conditions of each question are independent. Marginalize the latent class to get the observed distribution:

\[
P(\boldsymbol R=\boldsymbol r
\mid Q,\Theta,\boldsymbol p)
=
\sum_{\boldsymbol\alpha\in\{0,1\}^K}
\pi_{\boldsymbol r,\boldsymbol\alpha}(Q,\Theta)
p_{\boldsymbol\alpha}.
\]

## Two sources of parameters

|parameters|size|explain|
| --- | ---: | --- |
| \(\Theta\) | \(J\times 2^K\) |Positive response probability of each latent class on each question|
| \(\boldsymbol p\) | \(2^K\times1\) |latent class population proportion|

The difference between RLCM and the unconstrained latent class model comes from the structure of \(\Theta\): the Q matrix specifies which \(\theta_{j,\boldsymbol\alpha}\) must be equal, and which should maintain order.

## A two-attribute example

If \(K=2\), the column order is

\[
\boldsymbol 0=(0,0),\quad
\boldsymbol e_1=(1,0),\quad
\boldsymbol e_2=(0,1),\quad
\boldsymbol 1=(1,1),
\]

rule

\[
\Theta=
\begin{pmatrix}
\theta_{1,00}&\theta_{1,10}&\theta_{1,01}&\theta_{1,11}\\
\vdots&\vdots&\vdots&\vdots\\
\theta_{J,00}&\theta_{J,10}&\theta_{J,01}&\theta_{J,11}
\end{pmatrix},
\qquad
\boldsymbol p=
\begin{pmatrix}
p_{00}\\p_{10}\\p_{01}\\p_{11}
\end{pmatrix}.
\]

The subsequent identification justifies the unique recovery of these two groups of objects from all response pattern probabilities.
