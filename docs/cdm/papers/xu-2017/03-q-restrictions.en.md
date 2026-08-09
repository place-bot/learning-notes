# Q matrix restrictions and monotonicity

## Q matrix

\[
Q=(q_{jk})_{J\times K},
\qquad q_{jk}\in\{0,1\}.
\]

Line \(j\)

\[
\boldsymbol q_j=(q_{j1},\ldots,q_{jK})
\]

Give the required attributes for this question. If \(q_{jk}=1\), question \(j\) is connected to attribute \(k\).

Use component-wise partial ordering for bipartite vectors:

\[
\boldsymbol\alpha\succeq\boldsymbol q_j
\iff
\alpha_k\ge q_{jk}\quad\forall k.
\]

At this time, \(\boldsymbol\alpha\) has all the attributes required by this question. If at least one required attribute is missing, write it as

\[
\boldsymbol\alpha\nsucceq\boldsymbol q_j.
\]

## Restrictions (2.2)

Thesis requirements

\[
\max_{\boldsymbol\alpha:\,
\boldsymbol\alpha\succeq\boldsymbol q_j}
\theta_{j,\boldsymbol\alpha}
=
\min_{\boldsymbol\alpha:\,
\boldsymbol\alpha\succeq\boldsymbol q_j}
\theta_{j,\boldsymbol\alpha}
\ge
\theta_{j,\boldsymbol\alpha'}
\ge
\theta_{j,\boldsymbol 0}.
\tag{2.2}
\]

Explained item by item:

1. Potential classes with all required attributes have the same probability of success;
2. This common probability is not lower than the probability of any inability class;
3. The zero attribute class has the lowest probability of success.

The first part is the equating restriction, and the last two parts are the order restriction. If a question only requires attribute 1, \((1,0)\) and \((1,1)\) have the same probability of success on that question.

## Restrictions (2.3)

When a question only tests the \(k\) attribute, that is

\[
\boldsymbol q_j=\boldsymbol e_k,
\]

Additional requirements for thesis

\[
\theta_{j,\boldsymbol 1}
>
\max_{\boldsymbol\alpha:\,
\boldsymbol\alpha\nsucceq\boldsymbol e_k}
\theta_{j,\boldsymbol\alpha}.
\tag{2.3}
\]

Since Equation (2.2) makes all people who master the attribute \(k\) share the highest probability, Equation (2.3) gives strict separation:

\[
\theta_{j,\alpha_k=1}
>
\theta_{j,\alpha_k=0}.
\]

The nonzero products in the proof depend on this strict inequality.

## Original arithmetic example

The two attributes are "addition" and "multiplication", and the three questions are

\[
Q=
\begin{array}{c|cc}
&\text{addition}&\text{Multiplication}\\\hline
2+1&1&0\\
3\times2&0&1\\
(2+1)\times2&1&1
\end{array}.
\]

For the first question:

\[
\theta_{1,(1,0)}
=
\theta_{1,(1,1)}
>
\theta_{1,(0,0)},\theta_{1,(0,1)}.
\]

The second attribute does not change the highest probability of success for "master adders" on the first question.

## These restrictions affect parameter dimensions

The unconstrained model has \(2^K\) class probabilities for each question. Q restricts the merging of several units. Take \(K=2\), \(\boldsymbol q_j=(1,0)\) as an example:

\[
\theta_{j,10}=\theta_{j,11},
\qquad
\theta_{j,10}>\theta_{j,00},
\qquad
\theta_{j,10}>\theta_{j,01}.
\]

Constrained spaces have lower dimensions than unconstrained spaces. This is why the generic identifiability result cannot be directly transplanted.

## A detail

Equation (2.2) only ensures that all required attribute groups reach the common highest probability, and allows different incapacity classes to have different probabilities. DINA further reduces all incapacity classes into a guess probability; G-DINA, LLM and reduced RUM can retain finer differences. Xu's theorem covers this wider family of models.
