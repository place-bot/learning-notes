# Three link functions

## Unified form

Order

\[
\boldsymbol P_j
=
\left\{
P(\boldsymbol\alpha^*_{lj})
\right\}_{l=1}^{2^{K_j^*}}.
\]

The paper expands the attributes main effect and interaction effect on three scales:

\[
h\!\left[
P(\boldsymbol\alpha^*_{lj})
\right]
=
\phi_{j0}
+\sum_k\phi_{jk}\alpha_{lk}
+\sum_{k<k'}\phi_{jkk'}\alpha_{lk}\alpha_{lk'}
+\cdots.
\]

Different \(h\) correspond to different model families.

## identity link

\[
h(P)=P.
\]

It directly decomposes the probability of success:

\[
P(\boldsymbol\alpha^*_{lj})
=
\delta_{j0}
+\sum_k\delta_{jk}\alpha_{lk}
+\sum_{k<k'}\delta_{jkk'}\alpha_{lk}\alpha_{lk'}
+\cdots.
\]

The most direct explanation:

- \(\delta_{j0}\): Success probability of zero attribute group;
- \(\delta_{jk}\): Probability changes brought about by adding attribute \(k\) alone;
- Interactive terms: additional changes brought by joint mastery.

This model is named G-DINA in the paper.

## logit link

\[
h(P)=\operatorname{logit}(P)
=
\log\frac{P}{1-P}.
\]

So

\[
\operatorname{logit}
\left[
P(\boldsymbol\alpha^*_{lj})
\right]
=
\lambda_{j0}
+\sum_k\lambda_{jk}\alpha_{lk}
+\cdots.
\]

Property effects operate on log-odds. The paper calls it log-odds CDM and points out that it is equivalent to log-linear CDM and can also be regarded as a special form of GDM.

## log link

\[
h(P)=\log P.
\]

So

\[
\log
P(\boldsymbol\alpha^*_{lj})
=
\nu_{j0}
+\sum_k\nu_{jk}\alpha_{lk}
+\cdots.
\]

After indexation, the attribute effect has a multiplicative effect on the probability of success.

## Why is the fitting the same when saturated?

If the intercept, all main effects and all orders of interaction effects are retained, the number of parameters is

\[
2^{K_j^*}.
\]

As long as the probability is within the allowed interval, all three links can represent the same group of \(\boldsymbol P_j\). Therefore:

\[
\text{same}\widehat{\boldsymbol P}_j
\Longrightarrow
\text{Same model fit}.
\]

The differences arise in parameter interpretation and coordinate scaling.

## Why is the result different after reduction?

The meaning of "removing the interaction term" on the three scales is:

| link |No interaction means|
| --- | --- |
| identity |Addition to probability of success|
| logit |Addition on log-odds|
| log |Multiplication on probability of success|

They may have the same number of parameters, but different sets of predicted probabilities. The paper specifically emphasizes that A-CDM, LLM and G-NIDA/R-RUM are not interchangeable.

## Probability Boundary

logit link comes with

\[
0<P<1
\]

of normalization.

Reduction models of identity and log link require explicit guarantees that the predicted probabilities are valid. The linear sum of identity-link may exceed \([0,1]\); log link is guaranteed to be positive, but may still be greater than 1. Boundary or monotonic constraints must be added during actual estimation.
