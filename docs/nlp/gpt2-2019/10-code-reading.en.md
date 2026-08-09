# Official code intensive reading

## 1. Warehouse scope

The official warehouse [openai/gpt-2](https://github.com/openai/gpt-2) provides:

- TensorFlow 1.x model forward;
- byte-level BPE encoder/decoder；
- Conditional and unconditional generation;
- top-k, top-p and temperature sampling;
- Expose checkpoint download script.

The warehouse does not provide paper-level WebText training pipeline and complete benchmark evaluation code. Therefore, it is suitable for verifying model structure and generation, but not enough to reproduce paper training and all tables with one click.

## 2. `default_hparams()`

The default configuration is:

```python
n_vocab = 0
n_ctx = 1024
n_embd = 768
n_head = 12
n_layer = 12
```

The real runtime overwrites these values from `hparams.json` in the checkpoint directory.

## 3. `attention_mask()`

The code constructs the lower triangle condition:

```python
i = tf.range(nd)[:, None]
j = tf.range(ns)
m = i >= j - ns + nd
```

When there is no past cache, \(nd=ns=T\), so

\[
m_{t,s}=\mathbb I(s\le t).
\]

The masked logits are subtracted by about \(10^{10}\), and the future position probability after softmax is approximately 0.

## 4. Tensor shape of `attn()`

Input:

\[
\mathbf X\in\mathbb R^{B\times T\times d}.
\]

A linear projection produces a spliced QKV:

\[
\mathbf C\in\mathbb R^{B\times T\times 3d}.
\]

After splitting into long positions:

\[
\mathbf Q,\mathbf K,\mathbf V
\in
\mathbb R^{B\times H\times T\times d_h}.
\]

Attention weight shape:

\[
\mathbf A
\in
\mathbb R^{B\times H\times T_{\mathrm{dst}}\times T_{\mathrm{src}}}.
\]

## 5. `block()` Verification Pre-LN

The core logic is:

```python
a, present = attn(norm(x, 'ln_1'), ...)
x = x + a
m = mlp(norm(x, 'ln_2'), ...)
x = x + m
```

LayerNorm clearly occurs before attention and MLP, and the residual is added directly back to the original state. This corresponds to the pre-normalization description of the paper.

## 6. Embedding and output sharing

`model()` created:

```python
wpe = position_embedding
wte = token_embedding
h = gather(wte, X) + gather(wpe, positions)
```

Finally logits are used:

```python
logits = tf.matmul(h_flat, wte, transpose_b=True)
```

Therefore, the output layer reuses \(\mathbf W_E^\top\) and does not have a separate vocabulary projection matrix.

## 7. KV cache

Each layer stacks the current key and value into `present`:

\[
\text{present}
\in
\mathbb R^{B\times2\times H\times T\times d_h}.
\]

The next generation step concatenates past K/V with current K/V along the sequence dimension. This way the already calculated prefixes do not need to pass through all attention projections from scratch each time.

Note: cache reduces repeated calculations, but autoregressive token dependency still exists. The \(t+1\) token cannot be determined until the \(t\) token is generated.

## 8. Sampling code

Do temperature first in each step:

\[
\mathbf z' = \frac{\mathbf z}{\tau}.
\]

`top_k_logits` Set values below the \(k\) largest logit to approximately \(-10^{10}\). `top_p_logits` Sort by probability and retain the smallest set of candidates whose cumulative quality reaches the threshold. Finally, use `tf.multinomial` to extract a token.

## 9. An implementation detail: top-p was added later

The paper abstract experiment explicitly uses top-k; the current warehouse also contains nucleus sampling. When reading the code, you should distinguish between "the experimental configuration reported in the paper at the time" and "the inference function subsequently added to the warehouse."

## 10. Parameter count correction

The repository README states that parameter counts in earlier blogs and papers were incorrect. Public model cards list 124M, 355M, 774M and 1.5B. When writing a replication experiment, you should also record:

- The checkpoint directory name used;
- `hparams.json`；
- Actual parameter statistical methods;
- Scale labels used in the original table of the paper.
