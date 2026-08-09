# Architecture, Backbone and Learning Objectives

## 1. Common skeleton of Transformer

The core attention is:

\[
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(\frac{QK^\top}{\sqrt{d_k}}+M\right)V.
\]

\(M\) determines visibility: bidirectional encoders usually only cover padding; autoregressive decoder uses causal mask.

See [Transformer paper intensive reading](../transformer-2017/index.md) for complete details.

## 2. Three types of Backbone

|Architecture|visible context|Typical goals|Applicable|
|---|---|---|---|
| Encoder-only |Two-way|MLM, discrimination task|Representation, classification, extraction|
| Decoder-only |left to right| full LM |Universal generation and in-context learning|
| Encoder-decoder |encoder bidirectional, decoder causal| conditional generation |Translation, summary, conditional generation|

Model capabilities cannot be explained solely by the number of parameters; backbone and objective determine the training signal and inference interface.

## 3. Full Language Modeling

\[
\mathcal L_{\mathrm{CLM}}
=
-\sum_{t=1}^{n}
\log p_\theta(x_t\mid x_{<t}).
\]

Suitable for decoder-only models, training and generation forms are consistent.

## 4. Masked Language Modeling

Randomly select the location set \(M\):

\[
\mathcal L_{\mathrm{MLM}}
=
-\sum_{t\in M}
\log p_\theta(x_t\mid \widetilde x).
\]

Models can take advantage of context. BERT uses MLM pretraining and then fine-tuning for downstream tasks.

## 5. Prefix Language Modeling

Prefix allows bidirectional visibility inside, and the generation area maintains causality:

```text
[bidirectional prefix] → [causal continuation]
```

It provides another mask structure between conditional understanding and generation.

## 6. Mixture of Experts

The router selects a small number of experts for each token:

\[
h'
=
\sum_{e\in\operatorname{TopK}(g(h))}
g_e(h)E_e(h).
\]

MoE increases the total parameter capacity and controls active parameters, but increases weight residency, expert equalization, and communication difficulty.

## 7. Architecture selection principles

Application requirements should be mapped to model properties:

```text
Requires high quality embedding/token classification
→ encoder or specialized embedding model

Requires open generation / tool use
→ instruction-tuned decoder

Requires strict input to output conversion
→ encoder-decoder or controlled decoder
```

"Using the largest chat model uniformly" will increase costs and may also reduce controllability.

## 8. Intrinsic loss and application evaluation

perplexity：

\[
\operatorname{PPL}=\exp\left(
-\frac1n\sum_t\log p_\theta(x_t\mid x_{<t})
\right).
\]

Low perplexity does not guarantee that tool parameters are correct, references are faithful, or CAT measurements are valid. Model-intrinsic evaluation must be separated from application-level evaluation.

