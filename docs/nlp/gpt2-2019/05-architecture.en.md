# Differences between GPT-2 architecture and GPT-1

## 1. Decoder-only Transformer

Enter the token ID \(x_t\) and check the token embedding and location embedding first:

\[
\mathbf h_t^{(0)}
=
\mathbf W_E[x_t]
+
\mathbf W_P[t].
\]

After that, \(L\) causal Transformer blocks are passed. Each position is only allowed to read itself and the left position:

\[
M_{t,s}=
\begin{cases}
0,&s\le t,\\
-\infty,&s>t.
\end{cases}
\]

## 2. A Pre-LN block

GPT-2 moves LayerNorm to each sublayer input. The \(\ell\) layer can be written as:

\[
\widetilde{\mathbf H}^{(\ell)}
=
\mathbf H^{(\ell-1)}
+
\operatorname{MHA}
\left(
\operatorname{LN}(\mathbf H^{(\ell-1)})
\right),
\]

\[
\mathbf H^{(\ell)}
=
\widetilde{\mathbf H}^{(\ell)}
+
\operatorname{MLP}
\left(
\operatorname{LN}(\widetilde{\mathbf H}^{(\ell)})
\right).
\]

After stacking, add the final LayerNorm:

\[
\mathbf H^{\mathrm{final}}
=
\operatorname{LN}(\mathbf H^{(L)}).
\]

## 3. Multi-head causal self-attention

Enter \(\mathbf X\) for a certain layer:

\[
\mathbf Q=\mathbf X\mathbf W_Q,
\quad
\mathbf K=\mathbf X\mathbf W_K,
\quad
\mathbf V=\mathbf X\mathbf W_V.
\]

Single head attention is

\[
\operatorname{Attn}(\mathbf Q,\mathbf K,\mathbf V)
=
\operatorname{softmax}
\left(
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_h}}+\mathbf M
\right)\mathbf V.
\]

The causal mask \(\mathbf M\) allows all positions to be calculated in parallel during training while preventing the current position from seeing future tokens.

## 4. MLP and GELU

Each location independently passes through a two-layer feed-forward network:

\[
\operatorname{MLP}(\mathbf h)
=
\mathbf W_2\operatorname{GELU}(\mathbf W_1\mathbf h+\mathbf b_1)
+\mathbf b_2.
\]

The middle width is \(4d_{\mathrm{model}}\). The official TensorFlow code uses approximate GELU:

\[
\operatorname{GELU}(x)
\approx
\frac{x}{2}
\left[
1+\tanh\left(
\sqrt{\frac{2}{\pi}}(x+0.044715x^3)
\right)
\right].
\]

## 5. Output layer and weight sharing

The final hidden state is projected to vocabulary logits. The official implementation directly uses the transpose of the token embedding matrix:

\[
\mathbf z_t
=
\mathbf h_t^{\mathrm{final}}\mathbf W_E^\top,
\qquad
p(x_{t+1}\mid x_{\le t})
=
\operatorname{softmax}(\mathbf z_t).
\]

Sharing input embedding and output weights can reduce parameters and put input and output tokens in the same representation space.

## 6. Four model sizes

The original form of the report is as follows:

|Report parameter quantity|Number of layers| \(d_{\mathrm{model}}\) |
|---:|---:|---:|
| 117M | 12 | 768 |
| 345M | 24 | 1024 |
| 762M | 36 | 1280 |
| 1542M | 48 | 1600 |

All models use 1024 token context, vocabulary expanded to 50,257, and training batch size is 512. The official repository later corrected the parameter count, and public checkpoints are often referred to as 124M, 355M, 774M and 1558M/1.5B.

## 7. Main changes compared to GPT-1

The papers list:

- LayerNorm moves from the sub-layer output side to the input side, that is, pre-normalization;
- Add LayerNorm after the last self-attention block;
- The residual layer initialization is scaled according to depth, and the weights are multiplied by approximately \(1/\sqrt{N}\);
- Context length increased from 512 to 1024;
- batch size increased to 512;
- The byte-level BPE vocabulary is 50,257.

These changes collectively serve to achieve deeper, greater stability in training, and the experiment does not ablate the independent contribution of each change one by one.
