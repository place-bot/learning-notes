# Attention Is All You Need: Transformer intensive reading

This topic focuses on **Attention Is All You Need** by Vaswani et al. (2017). The paper changes the subject of sequence modeling from RNN/CNN to self-attention and proposes Transformer encoder–decoder.

## Core changes

\[
\text{RNN position-by-position state chain}
\quad\Longrightarrow\quad
\text{All-position attention matrix}.
\]

Each layer receives \(\mathbf X\in\mathbb R^{n\times d_{\text{model}}}\) and generates

\[
\mathbf Q=\mathbf X\mathbf W^Q,\quad
\mathbf K=\mathbf X\mathbf W^K,\quad
\mathbf V=\mathbf X\mathbf W^V,
\]

\[
\operatorname{Attention}(\mathbf Q,\mathbf K,\mathbf V)
=
\operatorname{softmax}\!\left(
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}
\right)\mathbf V.
\]

## Citation details

|item|information|
|---|---|
|Author|Ashish Vaswani and 8 other authors|
|publish| NeurIPS 2017 |
|Formal paper| [NeurIPS Proceedings](https://papers.nips.cc/paper/7181-attention-is-all-you-need) |
| arXiv | [1706.03762](https://arxiv.org/abs/1706.03762) |
|original implementation| [Tensor2Tensor](https://github.com/tensorflow/tensor2tensor) |

## Reading route

1. [Problems, Innovation and Architecture Panorama](01-problem-contributions-architecture.md)
2. [The meaning of Q, K, V and the matrix shape](02-query-key-value-shapes.md)
3. [Scaled Dot-Product Attention](03-scaled-dot-product-attention.md)
4. [Padding mask and causal mask](04-masks.md)
5. [Multi-Head Attention](05-multi-head-attention.md)
6. [Encoder, Decoder and three kinds of attention](06-encoder-decoder.md)
7. [positional encoding](07-positional-encoding.md)
8. [FFN, Residual, LayerNorm and original Post-LN](08-ffn-residual-layernorm.md)
9. [Training objectives, optimizers and autoregressive inference](09-training-and-inference.md)
10. [Complexity, path length and parallelization](10-complexity-and-parallelism.md)
11. [Complete hand calculation](11-worked-example.md)
12. [Experimental design, results and ablation](12-experiments-results.md)
13. [Tensor2Tensor with modern PyTorch implementation](13-code-reading-implementation.md)
14. [Limitations, Modern Variations and Conclusions](14-limitations-modern-variants-conclusion.md)
15. [References and primary sources](references.md)

## You should be able to answer after reading

- Where do query, key and value come from?
- Why divide by \(\sqrt{d_k}\);
- Why does causal mask not prevent cross-location parallelism during training?
- How to divide the eight heads into 512-dimensional representation;
- The difference between encoder self-attention, decoder masked self-attention, and cross-attention;
- How does sine positional encoding express relative displacement;
- Why the original paper is Post-LN, and the difference between it and modern Pre-LN;
- The reason why Transformer training can be parallelized but autoregressive generation is still token-by-token;
- base/big parameters, training configuration and BLEU evidence;
- LoRA will change which linear projections in Transformer will be changed in the future.
