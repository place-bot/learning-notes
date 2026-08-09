#Mistral: dense, MoE and multi-branch families

## 1. Why Mistral 7B is Attractive

Mistral 7B combines small parameter size with efficient attention. It uses grouped-query attention (GQA) to reduce key/value cache costs during inference, and in early versions used sliding-window attention (SWA) to limit the local window directly processed by each layer.

Standard causal self-attention forms an attention matrix of \(n\times n\) for a sequence of length \(n\), and the main calculation amount increases with \(n^2\). If each position only directly focuses on the nearest \(w\) positions, the number of sparse connections is approximately:

\[
O(nw),\qquad w\ll n.
\]

After multiple layers are stacked, information can still span longer distances layer by layer. The benefit here is to reduce the cost of long sequences, but the cost is that a single layer cannot directly compare any two long-distance tokens.

## 2. What costs does GQA reduce?

Ordinary multi-head attention stores key and value separately for each query head. GQA allows multiple sets of query heads to share fewer key/value heads. Assume that the number of query heads is \(h_q\) and the number of key/value heads is \(h_{kv}\). Then the head dimension cost ratio of KV cache is roughly reduced from \(h_q\) to \(h_{kv}\):

\[
\text{KV reduction}\approx \frac{h_{kv}}{h_q}.
\]

It mainly improves the memory bandwidth and cache occupation during autoregressive decoding, which is not equivalent to reducing the number of parameters of the entire model.

## 3. From dense to sparse MoE

Mixtral 8x7B replaces each layer of feed-forward network with a collection of experts. The router calculates the expert score for the token \(x_t\) and selects the top-\(k\) expert:

\[
g_t=\operatorname{softmax}(W_gx_t),
\]

\[
\operatorname{MoE}(x_t)
=
\sum_{e\in\operatorname{TopK}(g_t)}g_{t,e}E_e(x_t).
\]

Mixtral 8x7B has about 47B total parameters, but each token only activates about 13B parameters. Three different concepts of scale emerge:

|concept|decide what|
|---|---|
|Total parameters|Weight storage, cross-device communication and loading costs|
|activation parameters|Approximate cost of forward computation per token|
| KV cache |Memory cost of long context and concurrent decoding|

"Activation parameters are close to 13B" does not mean that it is as easy to deploy as a normal 13B dense model on any hardware, because all expert weights still need to reside or be read across devices.

## 4. Family evolution

Mistral subsequently formed multiple branches:

- **Small or medium dense model**: Emphasis on low latency and local deployment;
- **Mixtral**: Use sparse MoE to improve total capacity and unit token calculation efficiency;
- **Codestral/Devstral**: for code generation and software engineering agents;
- **Pixtral**: Add visual input;
- **Ministral**: For smaller deployment scale;
- **Mistral Large / Medium / Small**: For different service quality and cost levels.

These names represent a company's gradually expanding matrix of products and research, rather than an identical set of architectures or licenses.

## 5. tokenizer and chat template will also evolve

The official Mistral documentation distinguishes between multiple tokenizer versions. In the early days, Mistral 7B and Mixtral mainly used the SentencePiece series templates, and subsequent models also used tokenizers such as Tekken. The chat model relies on accurate control of tokens and message boundaries:

```text
<s>[INST] User message [/INST] Assistant answered </s>
```

If you feed a piece of text directly into the wrong template, the model may still be able to generate language, but it will lose the ability to call tools, distinguish between turns, or follow instructions. The model ID, tokenizer and chat template must be saved as one version.

## 6. License cannot be inferred by brand

The official model cards for Mistral 7B and Mixtral 8x7B list Apache 2.0 weights; other versions within the family may have different terms. When deploying, you should check each item:

```text
Exact model ID
→ Official model card
→ LICENSE corresponding to the weighted link
→ Whether commercial use, redistribution and model derivation are allowed
```

The value of Mistral's approach lies in demonstrating that efficient dense, GQA, local attention and sparse MoE can be combined into a technical route from local models to large-scale services. The brand itself does not provide license conclusions.

