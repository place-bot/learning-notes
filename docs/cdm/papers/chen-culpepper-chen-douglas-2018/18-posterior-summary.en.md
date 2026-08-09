# Posterior mode and column permutation of the entire Q

## Attribute label exchange

Permute the matrix \(R\) to any \(K\times K\) column, and simultaneously transform

\[
Q^\star=QR,
\qquad
\boldsymbol\alpha_i^\star=R^{\mathsf T}\boldsymbol\alpha_i,
\]

The ideal response and observation distribution of DINA will be maintained. Attribute column names cannot be determined by the model itself.

## Binary column encoding

Order

\[
\boldsymbol v
=
(2^{J-1},2^{J-2},\ldots,2,1)^{\mathsf T}.
\]

Column \(k\) of Q is encoded as an integer

\[
z_k=\boldsymbol v^{\mathsf T}Q_k.
\]

So the entire Q corresponds to a \(K\)-dimensional integer vector:

\[
\boldsymbol z(Q)=(z_1,\ldots,z_K).
\]

## Normalize column order

Sort \(\boldsymbol z(Q)\) in descending order:

\[
\widetilde{\boldsymbol z}(Q)
=
\operatorname{sort}_{\downarrow}
\{\boldsymbol z(Q)\}.
\]

Equivalent Qs with column permutations will get the same canonical encoding. Count the occurrence times of each code for MCMC retained samples, and the one with the highest frequency corresponds to

\[
\widehat Q_{\text{mode}}.
\]

## Why use the mode of the entire matrix?

The "\(\widehat Q=Q\)" simulated in the paper requires that every element is correct. The posterior mode of the entire Q directly faces this 0--1 overall loss:

\[
L(\widehat Q,Q)
=
I(\widehat Q\not\sim Q),
\]

Where \(\sim\) represents column replacement equivalent.

## Element-wise posterior average

Another kind of summary is

\[
\overline q_{jk}
=
\frac1M\sum_{m=1}^{M}q_{jk}^{(m)},
\]

It represents the posterior frequency of an edge being included under the current label alignment scheme. Element-wise threshold

\[
\widehat q_{jk}
=
I(\overline q_{jk}>0.5)
\]

Facing Hamming loss, it does not automatically maintain the structural constraints of the entire Q.

##Original text’s own warning

The paper points out that when \(K\) increases, the number of different Qs increases exponentially. Even if the chain visits a high-probability region, the occurrence frequency of a single matrix may be so low that reliable identification of the mode requires a long chain. The author lists element-wise mode as a future research direction.

## This site further discovered

The current `edina` package uses an element-wise averaging post-threshold of 0.5. This site has constructed three legitimate posterior samples of \(K=2,J=6\). The first column after their element-wise majority vote has only two 1s, violating the restriction of at least three questions per attribute.

So the identity check should be called again after using element-wise summarization. Optional fixes include:

- Select the posterior mode from the entire sampled Q;
- Project element-wise mean to \(\mathcal Q\);
- Minimize the weighted Hamming loss among the candidates that satisfy the constraints.

This counterexample is aimed at the current software aggregation strategy and does not change the experimental conclusion of the original paper on the entire Q mode.

[Next page: Experiment——Analog Design](19-simulation-design.md)
