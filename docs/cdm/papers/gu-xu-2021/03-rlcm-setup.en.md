# RLCM data-generating process and all objects

## 1. Observe reaction

Writing of participant’s binary response vector

\[
\boldsymbol R=(R_1,\ldots,R_J)^\top\in\{0,1\}^{J}.
\]

\(R_j=1\) indicates a positive response to question \(j\), which usually corresponds to a correct answer in educational tests.

## 2. Potential attribute profile

\[
\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_K)^\top
\in\{0,1\}^{K}.
\]

\(\alpha_k=1\) means mastering the \(k\) attribute. The overall proportion of all \(2^K\) patterns is

\[
\boldsymbol p=
\left(p_{\boldsymbol\alpha}:
\boldsymbol\alpha\in\{0,1\}^{K}\right)^\top,
\]

and assume

\[
p_{\boldsymbol\alpha}>0,\qquad
\sum_{\boldsymbol\alpha}p_{\boldsymbol\alpha}=1.
\]

Strict proportionality is an important parameter space assumption of the main theorem.

## 3. Q matrix

\[
Q=(q_{jk})_{J\times K}\in\{0,1\}^{J\times K}.
\]

- \(q_{jk}=1\): Question \(j\) requires attribute \(k\);
- Line \(j\) \(\boldsymbol q_j\): Complete attribute requirements for question \(j\);
- Column \(k\): Which questions measure the attribute \(k\).

Define partial ordering

\[
\boldsymbol\alpha\succeq\boldsymbol q_j
\quad\Longleftrightarrow\quad
\alpha_k\ge q_{jk}\ \text{to all}k.
\]

This represents all the attributes required by the participant to master question \(j\).

## 4. Partial independence

Given \(\boldsymbol\alpha\), the reaction conditions for each question are independent:

\[
\Pr(\boldsymbol R=\boldsymbol r\mid
\boldsymbol\alpha,Q,\Theta)
=
\prod_{j=1}^{J}
\theta_{j,\boldsymbol\alpha}^{r_j}
(1-\theta_{j,\boldsymbol\alpha})^{1-r_j},
\]

Among them

\[
\theta_{j,\boldsymbol\alpha}
=
\Pr(R_j=1\mid\boldsymbol\alpha).
\]

After mixing out the latent classes,

\[
\Pr(\boldsymbol R=\boldsymbol r\mid Q,\Theta,\boldsymbol p)
=
\sum_{\boldsymbol\alpha\in\{0,1\}^{K}}
p_{\boldsymbol\alpha}
\prod_{j=1}^{J}
\theta_{j,\boldsymbol\alpha}^{r_j}
(1-\theta_{j,\boldsymbol\alpha})^{1-r_j}.
\]

## 5. Restrictions imposed by Q on parameters

The general RLCM in this paper assumes monotonicity:

\[
\theta_{j,\boldsymbol\alpha}>
\theta_{j,\boldsymbol\alpha'}
\quad
\text{As long as}\quad
\boldsymbol\alpha\succeq\boldsymbol q_j,\ 
\boldsymbol\alpha'\nsucceq\boldsymbol q_j.
\]

Latent classes that master all required attributes have a higher positive response probability.

Common RLCM also satisfies that the irrelevant attributes do not change the item response probability:

\[
\boldsymbol\alpha\odot\boldsymbol q_j
=
\boldsymbol\alpha'\odot\boldsymbol q_j
\quad\Longrightarrow\quad
\theta_{j,\boldsymbol\alpha}
=
\theta_{j,\boldsymbol\alpha'}.
\]

\(\odot\) represents element-wise product.

## 6. Two-step graph generation

```text
Latent class proportion p
    │
    └── Extract attribute profile α
              │
              ├── Q specifies which attributes the item depends on
              └── Θ gives the positive response probability for each question
                         │
                         └── Conditionally independent generation of R1,...,RJ
```

Joint identification requires inferring the upper \(Q,\Theta,\boldsymbol p\) from the lower reaction distribution.
