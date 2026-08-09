# FFN, residuals and LayerNorm

Attention is responsible for exchanging information between positions, and FFN is responsible for nonlinear feature transformation within each position.

## 1. Position-wise FFN

\[
\operatorname{FFN}(\mathbf x)
=
\max(0,\mathbf x\mathbf W_1+\mathbf b_1)
\mathbf W_2+\mathbf b_2.
\]

base model:

\[
\mathbf W_1\in\mathbb R^{512\times2048},
\qquad
\mathbf W_2\in\mathbb R^{2048\times512}.
\]

All locations on the same layer share \(\mathbf W_1,\mathbf W_2\), and the parameters of different layers are independent. It can also be viewed as a convolution of two kernel size 1.

## 2. residual connection

\[
\mathbf r=\mathbf x+\operatorname{Dropout}(
\operatorname{Sublayer}(\mathbf x)).
\]

Residuals provide identity paths to facilitate the propagation of information and gradients across layers. All sub-layer inputs and outputs must maintain \(d_{\text{model}}\) dimensions before they can be added together.

## 3. LayerNorm

For \(d_{\text{model}}\) features of a single token:

\[
\mu=\frac1d\sum_kx_k,\qquad
\sigma^2=\frac1d\sum_k(x_k-\mu)^2,
\]

\[
\operatorname{LN}(\mathbf x)
=
\boldsymbol\gamma\odot
\frac{\mathbf x-\mu}{\sqrt{\sigma^2+\epsilon}}
+\boldsymbol\beta.
\]

It does not depend on other samples in the batch and is suitable for variable-length sequences.

## 4. The original paper is Post-LN

\[
\operatorname{LN}(
\mathbf x+\operatorname{Sublayer}(\mathbf x)).
\]

Many modern large models use Pre-LN:

\[
\mathbf x+\operatorname{Sublayer}(
\operatorname{LN}(\mathbf x)).
\]

Pre-LN tends to be easier to train very deep networks, but is a common subsequent modification. Post-LN should be used when interpreting Figure 1 of the original paper and reproducing base/big.

## 5. Activation function

The original paper FFN uses ReLU. GELU, SwiGLU, GEGLU, etc. are subsequent Transformer variants and cannot be backfilled to 2017 configurations.
