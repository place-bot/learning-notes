# Probabilistic LD I: ULD, testlets, and RD

Probabilistic LD uses the complete support \(\mathcal K=2^Q\). All patterns remain possible and the
dependence is encoded in the SRF.

## ULD and trait dependence

An omitted common construct is represented by a multidimensional trait

\[
\Theta=(\theta,u_1,u_2,\ldots),
\qquad
P(\boldsymbol X\mid\Theta)=\pi(K\mid\Theta).
\]

Given the complete \(\Theta\), items may again satisfy LI. The dependence appears when the analyst
conditions only on \(\theta\).

For item \(i\) in testlet \(t\), a random-effect model is

\[
P(X_i=1\mid\theta,u_t)
=\frac{e^{\theta-b_i-u_t}}{1+e^{\theta-b_i-u_t}}.
\tag{25}
\]

Items in the same testlet share \(u_t\). Assuming testlet effects arise from a common distribution is a
hierarchical partial-pooling assumption, not a logical fact, and must be justified by design and data.
Such models lie in the bifactor family: a general factor affects all items and group-specific factors
explain residual within-testlet association.

Finite ULD loadings generally leave all patterns with positive probability, so ULD changes probability
rather than structural possibility.

## Response dependence

RD factorizes by the chain rule:

\[
P(X_i,X_{i'}\mid\theta)
=P(X_i\mid\theta)P(X_{i'}\mid X_i,\theta).
\]

The conditional response model is

\[
P(X_{i'}=x_{i'}\mid X_i=x_i,\theta)
=\frac{e^{x_{i'}[\theta-b_{i'}-(1-2x_i)d]}}
{1+e^{\theta-b_{i'}-(1-2x_i)d}}.
\tag{26}
\]

For \(d>0\), the effective difficulty of item \(i'\) is \(b_{i'}+d\) after failure on item \(i\) and
\(b_{i'}-d\) after success. RD therefore represents a directional mechanism such as answer reuse,
practice, hints, or stage ordering. Reversing item order may change its meaning.

| ULD | RD |
| --- | --- |
| Shared omitted latent variable | Direct conditional response path |
| LI may return after conditioning on all traits | Dependence remains after conditioning on ability |
| Often symmetric across a testlet | Directional |
| Multidimensional SRF | Chain-rule factorization |

