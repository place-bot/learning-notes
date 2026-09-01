# Probabilistic LD II: OD, CD, Bahadur, and copulas

## Divide-by-total models

OD and CD directly score joint response patterns:

\[
P(\boldsymbol X=\boldsymbol x\mid\theta,\Gamma)
=\frac{e^{f(\boldsymbol x,\theta,\Gamma)}}
{\sum_{\boldsymbol y}e^{f(\boldsymbol y,\theta,\Gamma)}}.
\tag{27}
\]

OD uses an asymmetric kernel and can represent Table A. CD uses a symmetric interaction
\(x_ix_{i'}b_{ii'}\) and can represent Table B. RD and OD may fit similar tables, but RD is a
conditional sequence whereas OD is a joint softmax. Likewise, CD is a joint interaction whereas SLD
is a mixture with a restricted component.

## General log-linear latent-trait models

Ip's model includes main and higher-order effects:

\[
\log P(\boldsymbol X=\boldsymbol x\mid\theta)
=\sum_ix_i\omega_i(\theta)
+\sum_{i<j}x_ix_j\omega_{ij}(\theta)+\cdots-k\omega(\theta).
\tag{29}
\]

Setting interactions of order two and above to zero recovers LI. An important interpretive question is
marginal reproducibility:

\[
\sum_{\boldsymbol x_{-i}}P(\boldsymbol x\mid\theta)
=P(X_i=x_i\mid\theta).
\]

OD and CD are generally nonreproducible; adding their interaction changes the marginal IRFs.

## LND and Bahadur representation

Local nonnegative dependence replaces LI equalities by inequalities that increase \(00,11\) and
decrease discordant cells. It constrains the SRF without specifying one unique model.

For

\[
Z_i(\theta)=\frac{X_i-p_i(\theta)}
{\sqrt{p_i(\theta)[1-p_i(\theta)]}},
\]

Bahadur's bivariate representation is

\[
P(X_i,X_{i'}\mid\theta)
=P(X_i\mid\theta)P(X_{i'}\mid\theta)
[1+\rho_{ii'}(\theta)Z_iZ_{i'}].
\tag{31}
\]

The centered standardized terms preserve the supplied marginal IRFs. Higher-order versions add
\(\rho_I(\theta)\prod_{i\in I}Z_i\).

## Copulas

Let \(X_i^*=\theta-b_i+\varepsilon_i\) and \(X_i=1\) iff \(X_i^*>0\). A copula joins fixed
marginal residual distributions:

\[
P(00\mid\theta)
=C(F_i(b_i-\theta),F_{i'}(b_{i'}-\theta)).
\tag{32}
\]

The remaining cells follow by subtraction, preserving both margins. At the Fréchet-Hoeffding upper
bound \(C(u,v)=\min(u,v)\), some cells become exactly zero. The model then reaches a deterministic-
LD boundary: unequal difficulties yield Table A and equal difficulties yield Table B.

