# Definition and statistical explanation of GDI

## Definition

The candidate q-vector produces several reduced attribute groups. G-DINA discrimination index is defined as

\[
\begin{aligned}
\varsigma_j^2(\boldsymbol q)
&=
\sum_{\boldsymbol\alpha_{\boldsymbol q}}
w(\boldsymbol\alpha_{\boldsymbol q})
\left[
p_j(\boldsymbol\alpha_{\boldsymbol q})
-\bar p_j
\right]^2\\
&=
\sum_{\boldsymbol\alpha_{\boldsymbol q}}
w(\boldsymbol\alpha_{\boldsymbol q})
p_j^2(\boldsymbol\alpha_{\boldsymbol q})
-\bar p_j^2,
\end{aligned}
\tag{5}
\]

Among them

\[
\bar p_j
=
\sum_{\boldsymbol\alpha_{\boldsymbol q}}
w(\boldsymbol\alpha_{\boldsymbol q})
p_j(\boldsymbol\alpha_{\boldsymbol q}).
\tag{6}
\]

## Conditional expectation variance

because

\[
p_j(\boldsymbol\alpha_{\boldsymbol q})
=
E(Y_j\mid\boldsymbol\alpha_{\boldsymbol q}),
\]

So

\[
\varsigma_j^2(\boldsymbol q)
=
\operatorname{Var}_w
\left\{
E(Y_j\mid\boldsymbol\alpha_{\boldsymbol q})
\right\}.
\tag{7}
\]

It measures how much of the “difference in success rates between groups” the candidate groupings can explain.

## Full variance formula

Full mode GDI can be broken down into

\[
\begin{aligned}
\operatorname{Var}
\{E(Y_j\mid\boldsymbol\alpha)\}
= {}&
E\!\left[
\operatorname{Var}
\{E(Y_j\mid\boldsymbol\alpha)
\mid\boldsymbol\alpha_{\boldsymbol q}\}
\right]\\
&+
\operatorname{Var}
\{E(Y_j\mid\boldsymbol\alpha_{\boldsymbol q})\}.
\end{aligned}
\tag{8}
\]

The second term is the candidate GDI, and the first term is non-negative. Therefore:

\[
\varsigma_j^2(\boldsymbol q)
\le
\varsigma_j^2(\boldsymbol 1).
\]

## Relationship with \(R^2\)

Liu (2017) pointed out,

\[
\frac{\varsigma_j^2(\boldsymbol q)}
{\operatorname{Var}(Y_j)}
\]

With an explanation like \(R^2\): How much of the total variation in dichotomous responses is explained by candidate attribute grouping.

The PVAF denominator actually used in the paper is the saturated attribute grouping GDI:

\[
\operatorname{PVAF}_j(\boldsymbol q)
=
\frac{\varsigma_j^2(\boldsymbol q)}
{\varsigma_j^2(\boldsymbol 1)}.
\]

It measures the proportion of candidates that retain the complete grouping explainable variance.

## Relation to 2008 \(\delta\)

DINA has only two success probabilities:

\[
p_0=g,
\qquad
p_1=1-s.
\]

The difference between the two groups is

\[
p_1-p_0=1-s-g=\delta.
\]

In the case of the second group:

\[
\varsigma^2
=
w_0w_1(p_1-p_0)^2
=
w_0w_1\delta^2.
\]

Therefore, GDI generalizes DINA's two-group distinction into the weighted variance of multiple groups of success probabilities.
