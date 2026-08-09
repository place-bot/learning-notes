# RMSNorm, SwiGLU, RoPE and GQA

## 1. A Llama 2 block

For input \(\mathbf X\), use Pre-Norm residuals:

\[
\mathbf H
=
\mathbf X
+
\operatorname{Attention}
\left(\operatorname{RMSNorm}(\mathbf X)\right),
\]

\[
\mathbf Y
=
\mathbf H
+
\operatorname{SwiGLU}
\left(\operatorname{RMSNorm}(\mathbf H)\right).
\]

## 2. RMSNorm

For vector \(\mathbf x\in\mathbb R^d\):

\[
\operatorname{RMS}(\mathbf x)
=
\sqrt{\frac{1}{d}\sum_{i=1}^{d}x_i^2+\epsilon},
\]

\[
\operatorname{RMSNorm}(\mathbf x)
=
\mathbf g\odot
\frac{\mathbf x}{\operatorname{RMS}(\mathbf x)}.
\]

It does not subtract the mean, only scales by the root mean square, and then multiplies the learnable weight \(\mathbf g\). The official code first converts to float for calculation, and then converts back to the original dtype.

## 3. SwiGLU

The official implementation is:

\[
\operatorname{FFN}(\mathbf x)
=
\mathbf W_2
\left[
\operatorname{SiLU}(\mathbf W_1\mathbf x)
\odot
(\mathbf W_3\mathbf x)
\right].
\]

Among them

\[
\operatorname{SiLU}(z)=z\sigma(z).
\]

One branch acts as a gate, and the other branch passes the content, which is multiplied element by element and then projected back to the model dimension.

## 4. RoPE

Rotary Position Embedding performs a position-dependent rotation on the 2D coordinate pairs of query and key. Treat two real dimensions as complex numbers:

\[
q_{t,j}^{\mathbb C}
\longmapsto
q_{t,j}^{\mathbb C}e^{it\omega_j},
\]

\[
k_{s,j}^{\mathbb C}
\longmapsto
k_{s,j}^{\mathbb C}e^{is\omega_j}.
\]

The inner product after rotation relies on the relative displacement \(t-s\), which injects position information into attention without learning the absolute position embedding separately.

## 5. MHA, MQA and GQA

### Multi-Head Attention

Each query head has its own K/V head:

\[
H_Q=H_K=H_V.
\]

### Multi-Query Attention

All query heads share a K/V head:

\[
H_K=H_V=1.
\]

### Grouped-Query Attention

Multiple query heads form a group and share a K/V head:

\[
1<H_{KV}<H_Q.
\]

If

\[
n_{\mathrm{rep}}=
rac{H_Q}{H_{KV}},
\]

K/V can be logically repeated during inference to match each query head, but the cache only needs to save \(H_{KV}\) copies.

## 6. Why does GQA reduce KV cache?

The number of cache elements per layer is roughly:

\[
2BT H_{KV}d_h,
\]

Where 2 represents K and V. MHA uses \(H_{KV}=H_Q\), and GQA uses fewer K/V heads, so there is less pressure on video memory and bandwidth during long context and large batch decoding.

The paper uses GQA in 34B and 70B. Appendix ablation shows that GQA improves large batch inference throughput while approaching MHA quality.

## 7. Causal attention and cache

The model still uses a causal mask:

\[
\operatorname{softmax}
\left(
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_h}}
+\mathbf M_{\mathrm{causal}}
\right)
\mathbf V.
\]

Training can be calculated in parallel for all positions; generation is still token-by-token. KV cache avoids repeated calculation of historical K/V, and GQA further reduces cache size.

## 8. Effect of 4K context

Compared to Llama 1's 2K, Llama 2 trains to 4K. The appendix long-context ablation shows that the 4K model is stronger on long-context tasks, with no significant impairment overall for normal tasks. Doubling the context length will significantly increase dense attention calculations. GQA mainly alleviates the generation of cache and will not completely eliminate the \(T^2\) cost of training attention.
