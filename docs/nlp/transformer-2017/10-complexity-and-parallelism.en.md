# Complexity, path length and parallelization

The paper compares architectures using per-layer complexity, minimum serial operations, and maximum path length.

## 1. Original paper table 1

|layer|Each level of complexity|serial operation|maximum path|
|---|---:|---:|---:|
| Self-attention | \(O(n^2d)\) | \(O(1)\) | \(O(1)\) |
| Recurrent | \(O(nd^2)\) | \(O(n)\) | \(O(n)\) |
| Convolution | \(O(knd^2)\) | \(O(1)\) | \(O(\log_k n)\) |
| Restricted attention | \(O(rnd)\) | \(O(1)\) | \(O(n/r)\) |

## 2. When self-attention calculation is more economical

compare

\[
n^2d
\quad\text{with}\quad
nd^2.
\]

When \(n<d\), the term of self-attention is smaller. The length of common subword sequences in machine translation of the original paper is usually lower than the representation dimension of 512.

\(n^2\) will become the main bottleneck when the context is long, which gives rise to sparse, local, low-rank and linear attention.

## 3. Path length

self-attention: Any two positions in a layer are directly connected, and the longest path is constant. The information at both ends of the RNN needs to pass through \(O(n)\) recursions. This affects forward and backpropagation of long-distance signals.

## 4. Why training is parallel?

The entire layer can be written as several large matrix operations, with all query rows calculated together. causal mask only deletes illegal connections and does not require line-by-line waiting.

\(\mathbf h_t\) in RNN is the input for calculating \(\mathbf h_{t+1}\); \(\mathbf z_t\) in the same layer in Transformer only relies on the known matrix of the previous layer.

## 5. Why is reasoning still serial?

autoregressive probability

\[
p(\mathbf y\mid\mathbf x)
=
\prod_t p(y_t\mid y_{<t},\mathbf x)
\]

It is required to select \(y_t\) before entering the next step. Model internal position parallelism and external token generation sequence belong to two levels.

## 6. Actual hardware perspective

In addition to theoretical FLOPs, it is also affected by memory bandwidth, kernel fusion, sequence length, batch, communication and attention matrix storage. The advantage of Transformer comes from converting serial small calculations into hardware-efficient large matrices; extremely long sequences may be limited by secondary memory and calculations.
