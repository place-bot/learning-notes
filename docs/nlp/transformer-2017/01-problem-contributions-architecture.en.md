# Panorama of issues, innovations and architecture

## 1. Bottlenecks faced by the paper

RNN binds position to computation time:

\[
\mathbf h_t=f(\mathbf h_{t-1},\mathbf x_t).
\]

Within the same training sample, \(n\) states need to be calculated sequentially. When the sequence becomes longer, the batch is limited by the video memory, and this serial critical path becomes the training throughput bottleneck.

CNNs can calculate positions in parallel, but establishing connections at arbitrary distant locations requires multiple layers of convolutions: the longest path for ordinary convolutions grows linearly with distance, and for dilated convolutions it grows approximately logarithmically.

## 2. Core proposal of the paper

Transformer completely removes sequence-aligned recurrence and convolution, using:

- self-attention exchanges information at different locations;
- position-wise FFN transforms features within each position;
- residual connection and LayerNorm stabilize deep training;
- positional encoding injection sequence;
- encoder–decoder attention connects the source sequence and the target sequence.

## 3. Encoder

The original paper stacks \(N=6\) layers, each layer contains:

1. multi-head self-attention；
2. position-wise FFN。

used outside each sub-layer

\[
\operatorname{LayerNorm}(
\mathbf x+\operatorname{Sublayer}(\mathbf x)).
\]

This is **Post-LN**: add residuals first, then LayerNorm.

## 4. Decoder

Each decoder layer has three sub-layers:

1. masked multi-head self-attention；
2. Multi-head cross-attention for encoder output;
3. position-wise FFN。

The target token embedding is shifted one position to the right, and with the causal mask, the position \(i\) can only rely on \(y_{<i}\).

## 5. Original paper base configuration

|parameters|numerical value|
|---|---:|
|Number of layers \(N\)| 6 encoder + 6 decoder |
| \(d_{\text{model}}\) | 512 |
| \(d_{\text{ff}}\) | 2048 |
|Number of heads \(h\)| 8 |
| \(d_k=d_v\) | 64 |
| dropout | 0.1 |
| label smoothing | 0.1 |
|Parameter quantity|About 65M|

The big model uses \(d_{\text{model}}=1024\), \(d_{\text{ff}}=4096\), 16 heads, and about 213M parameters.

## 6. The exact scope of “Attention Is All You Need”

The title emphasizes that the exchange of information between sequence positions no longer relies on RNNs or convolutions. The full model still includes embedding, positional encoding, FFN, residual, LayerNorm, softmax and autoregressive search. Attention is the main body of relationship modeling in the architecture, and is not the only operation of the entire network.

## 7. Connection to Bahdanau

Bahdanau attention queries bidirectional RNN annotations with a decoded state. Transformer matrixes all query, key, and value:

- encoder self-attention: query all source positions for each source position;
- decoder self-attention: query known target prefixes for each target position;
- cross-attention: Query all source representations for each target position.

The idea of dynamic reading is retained, and the recursive query generation method is removed.
