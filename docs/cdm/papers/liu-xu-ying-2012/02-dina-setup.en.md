# DINA model and all basic symbols

## Data

\[
\boldsymbol R_i=(R_i^1,\ldots,R_i^J)^\top,
\qquad
R_i^j\in\{0,1\}.
\]

- \(i=1,\ldots,N\): student;
- \(j=1,\ldots,J\): item;
- \(R_i^j=1\): Student \(i\) answered correctly item \(j\).

All observations form the \(N\times J\) response matrix.

## Potential attribute profile

\[
\boldsymbol\alpha_i=(\alpha_{i1},\ldots,\alpha_{iK})^\top
\in\{0,1\}^K.
\]

\(\alpha_{ik}=1\) indicates that the student has mastered the attribute \(k\). There are \(2^K\) possible patterns. Thesis hypothesis

\[
\Pr(\boldsymbol\alpha_i=\boldsymbol\alpha)=p_{\boldsymbol\alpha},
\qquad
\sum_{\boldsymbol\alpha}p_{\boldsymbol\alpha}=1.
\]

\(\boldsymbol p\) is a class proportion vector of length \(2^K\).

## Q matrix

\[
Q=(Q_{jk})_{J\times K},\qquad Q_{jk}\in\{0,1\}.
\]

Line \(j\)

\[
\boldsymbol q_j=(Q_{j1},\ldots,Q_{jK})
\]

Describe what attributes are required for item \(j\).

## DINA ideal response

\[
\xi^j(\boldsymbol\alpha,Q)
=
\mathbf 1
\left(
\alpha_k\ge Q_{jk},\ \forall k
\right).
\tag{1}
\]

If the student covers all attributes required by the item, \(\xi^j=1\); if one is missing, \(\xi^j=0\). Additional mastery of the unrequired attributes will not change the ideal state of the question.

can also be written as

\[
\xi^j(\boldsymbol\alpha,Q)
=
\prod_{k=1}^K \alpha_k^{Q_{jk}}.
\]

## slipping, guessing and \(c\)

- \(s_j\): The probability of a person with all required attributes answering incorrectly;
- \(g_j\): The probability of correct answer for those who do not cover all required attributes;
- \(c_j=1-s_j\): The probability of a person with all required attributes answering correctly.

Order

\[
\pi_{j\boldsymbol\alpha}
=
\Pr(R^j=1\mid \boldsymbol\alpha,Q,\boldsymbol c,\boldsymbol g),
\]

rule

\[
\pi_{j\boldsymbol\alpha}
=
c_j^{\xi^j}
g_j^{1-\xi^j}
=
g_j+(c_j-g_j)\xi^j.
\tag{2}
\]

\(c_j>g_j\) is usually required for the item to have positive diagnostic significance; the natural constraint in the original text is only \([0,1]\), and this order constraint is not additionally written in Equation (15).

## Partially independent

Given \(\boldsymbol\alpha_i\), the reaction conditions for each question are independent:

\[
\Pr(\boldsymbol R_i=\boldsymbol r\mid\boldsymbol\alpha_i)
=
\prod_{j=1}^J
\pi_{j\boldsymbol\alpha_i}^{r_j}
(1-\pi_{j\boldsymbol\alpha_i})^{1-r_j}.
\]

Local independence makes the joint correct answer probability of multiple questions become the product of the single question probabilities, which is the key to the establishment of the \(T\)-matrix construction.
