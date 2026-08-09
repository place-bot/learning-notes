# Inference optimization: Cache, quantization, distillation and accelerated decoding

## 1. Prefill and Decode

```text
Prefill: Process input in parallel and establish KV cache
Decode: Generate a token in each round and read cache repeatedly
```

The first token delay is mainly affected by queuing, tokenization and prefill; subsequent speed is determined by single-step decoding, memory bandwidth and batching.

## 2. KV Cache

Cache the keys and values of this layer:

\[
M_{KV}
\approx
2Lnh_{kv}d_hb,
\]

Among them, \(L\) is the number of layers, \(n\) is the cache token, \(h_{kv}\) is the KV heads, \(d_h\) is the head dimension, and \(b\) is the number of bytes.

Long contexts and concurrency will enlarge the KV cache, even if the weights are 4-bit quantized.

## 3. Quantification

\[
q=\operatorname{round}\left(\frac{w-z}{s}\right),
\qquad
\widehat w=sq+z.
\]

Low bit weight reduces storage and memory bandwidth. Symmetric quantization always sets the zero point to 0; asymmetric quantization allows non-zero \(z\), which is more flexible but has more complex metadata and kernel.

Quantization quality depends on bitwidth, grouping, calibration, outlier processing and hardware kernel. Smaller files don't guarantee faster speeds.

## 4. Knowledge Distillation

Student model fit teacher distribution:

\[
\mathcal L
=
\lambda\mathcal L_{\mathrm{hard}}
+(1-\lambda)T^2
\operatorname{KL}
\left(
p_T^{\mathrm{teacher}}
\parallel
p_T^{\mathrm{student}}
\right).
\]

It is also possible to distill generated data, inference trajectories, tool behaviors or embeddings.

## 5. Speculative Decoding

The small draft model proposes multiple tokens at once, and the large target model verifies in parallel:

```text
draft proposes k tokens
→ target verifies in one pass
→ accept valid prefix
→ resample first rejection
```

The algorithm can maintain target distribution while reducing the number of expensive target forwards. Velocity depends on draft cost and acceptance rate.

## 6. Parallel Decoding

Try to predict multiple positions simultaneously or use multiple candidate branches to reduce the number of serial steps. Actual benefits depend on model support, validation mechanisms, and request length.

## 7. Early Exit

Output early when the intermediate layers are sufficiently determined, suitable for classification or specialized architectures. Generalized autoregressive generation is difficult to use directly because the error for each token enters subsequent context.

## 8. Serving evaluation

Report at least:

- time to first token；
- inter-token latency；
- Single user tokens/s;
- Total concurrent throughput;
- Peak GPU/CPU memory;
- Energy consumption or cost per request;
-Quantified task quality;
- Long context performance.

## 9. Connection to local inference

The roles and differences of llama.cpp, Transformers, vLLM and TGI have been compiled in [LLM software stack topic](../llm-software-stack/index.md). It should be measured on the target hardware, target batch and target context.

