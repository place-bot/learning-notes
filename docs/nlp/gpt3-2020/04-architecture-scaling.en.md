# Model architecture, eight scales and sparse attention

## 1. Architecture inheritance

GPT-3 follows the main design of GPT-2:

- decoder-only Transformer；
- causal self-attention；
- pre-LayerNorm；
- residual initialization scaling；
- byte-level BPE reversible tokenizer;
- Input and output embedding weight sharing;
- Autoregressive next-token loss.

The main structural change is that different layers alternately use dense attention and locally banded sparse attention, and the design refers to Sparse Transformer.

## 2. Eight scales

|model|Parameter quantity|Number of layers| \(d_{\mathrm{model}}\) |Number of heads| \(d_{\mathrm{head}}\) | batch tokens |learning rate|
|---|---:|---:|---:|---:|---:|---:|---:|
| Small | 125M | 12 | 768 | 12 | 64 | 0.5M | \(6.0\times10^{-4}\) |
| Medium | 350M | 24 | 1024 | 16 | 64 | 0.5M | \(3.0\times10^{-4}\) |
| Large | 760M | 24 | 1536 | 16 | 96 | 0.5M | \(2.5\times10^{-4}\) |
| XL | 1.3B | 24 | 2048 | 24 | 128 | 1M | \(2.0\times10^{-4}\) |
| 2.7B | 2.7B | 32 | 2560 | 32 | 80 | 1M | \(1.6\times10^{-4}\) |
| 6.7B | 6.7B | 32 | 4096 | 32 | 128 | 2M | \(1.2\times10^{-4}\) |
| 13B | 13.0B | 40 | 5140 | 40 | 128 | 2M | \(1.0\times10^{-4}\) |
| GPT-3 | 175.0B | 96 | 12,288 | 96 | 128 | 3.2M | \(0.6\times10^{-4}\) |

All models are trained with 300 billion tokens and the context length is 2048. The width of the feedforward layer is

\[
d_{\mathrm{ff}}=4d_{\mathrm{model}}.
\]

## 3. Dense causal attention

Complete causal attention computation:

\[
\mathbf A
=
\operatorname{softmax}
\left(
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_h}}+\mathbf M_{\mathrm{causal}}
\right).
\]

The score matrix of length \(T\) has \(T^2\) positions, and the attention time and the main item of the video memory are approximately

\[
O(T^2d).
\]

## 4. Locally banded sparse attention

Local strip mode makes position \(t\) read-only nearby window \(W(t)\):

\[
\alpha_{t,s}=0,
\qquad s\notin W(t).
\]

If the window width is \(w\ll T\), the number of attention connections drops from \(T^2\) to about \(Tw\). GPT-3 alternates dense and sparse patterns in different layers:

- The sparse layer reduces part of the attention calculation;
- The dense layer still provides global information connections;
- Multi-layer stacking expands the effective receptive field.

The paper does not disclose enough training code to completely reproduce its sparse kernel and distributed implementation.

## 5. Why is the number of parameters so large?

The main matrix approximations of a Transformer block include:

- QKV and output projection: about \(4d^2\);
- Two-layer MLP: approximately \(8d^2\).

Main items for each floor

\[
12d^2.
\]

At 96 layers and \(d=12{,}288\), the block matrix alone has entered the parameter level of hundreds of billions, plus embedding, LayerNorm and bias.

## 6. Model parallelism

A single 175B model cannot fit on a single V100. The paper is divided in two directions:

1. Inter-layer segmentation: Different Transformer layers are allocated to different devices;
2. Intra-layer splitting: The width dimension of a single matrix multiply is also split across GPU shards.

The goal is to overlap communication with computation and reduce data transfer between nodes. The paper only gives high-level instructions and does not release the complete training system.

## 7. Expanding the number of parameters does not only change the "capacity"

Larger models in the table also use:

- More layers and wider hidden states;
- Larger batch;
- Smaller initial learning rate;
- Different parallelism scales and training dynamics.

Therefore, the scale experiment studies a complete set of collaborative expansion solutions. Parameter volume is the main horizontal axis, but not all differences can be attributed to a single number.
