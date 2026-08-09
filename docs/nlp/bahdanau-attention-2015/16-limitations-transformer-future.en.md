# Limitations, Transformer interface and follow-up work

## 1. Main limitations of the original model

### Word level 30k vocabulary

Low-frequency words are uniformly mapped to \([UNK]\), and the complete test set BLEU is obviously affected by vocabulary coverage. The later subword/BPE transformed the open vocabulary problem into combinable subword prediction.

### Recursive calculation

The encoder and decoder are serialized along the time step, limiting the training throughput of long sequences. Attention improves information access without removing the RNN state chain.

### Two-dimensional alignment cost

Each target step compares all source positions, and the attention matrix size is \(T_xT_y\). Long source sentences and long target sentences will increase both time and storage.

### Missing explicit override

The original model does not have a cumulative record of which source content has been translated. Repeated attention may lead to repeated translations, and low coverage positions may lead to missed translations.

### Teacher forcing

Training sees the real prefix, and inference sees the model prefix, resulting in exposure bias.

### Scope of evidence

The main experiment focuses on WMT14 English and French single direction, and does not report multiple sub-intervals, component ablation and manual alignment indicators.

## 2. Follow-up improvement clues

- Luong attention: propose global/local attention and different scores;
- Coverage: Feed back accumulated attention to subsequent steps;
- pointer/copy: copy rare words directly from the input position;
- BPE/subword: significant mitigation \([UNK]\);
- multi-head: Let multiple subspaces establish relationships in parallel;
- self-attention: replace loop encoding with full-position interaction;
- non-autoregressive decoding: Further research on output-side parallelism.

## 3. Bahdanau and Transformer attention

|Dimensions| Bahdanau attention | Transformer attention |
|---|---|---|
| query |Previous decoding status|Each position after linear projection|
| key/value |Bidirectional RNN annotation|Sequence representation after linear projection|
| score | MLP/additive | scaled dot product |
|Number of heads|single alignment mechanism| multi-head |
|inter-position status|RNN recursive| self-attention + position |
|Training position parallelism|subject to recursion|Matrixable|

Transformer cross-attention continues the idea of "the target-side query reads the source-side representation"; it rewrites the generation methods and compatibility functions of query, key, and value.

## 4. From addition scoring to dot product scoring

Bahdanau：

\[
e_{ij}
=
\mathbf v_a^\top
\tanh(\mathbf W_a\mathbf s_{i-1}+\mathbf U_a\mathbf h_j).
\]

Transformer：

\[
e_{ij}
=
\frac{\mathbf q_i^\top\mathbf k_j}{\sqrt{d_k}}.
\]

The former uses a small neural network to learn compatibility, and the latter uses matrix multiplication to efficiently calculate all position pairs, and uses \(\sqrt{d_k}\) to control the inner product scale.

## 5. Research questions

From this paper we can continue to ask:

1. What is the relationship between attention weight, artificial alignment and causal contribution respectively?
2. How to add coverage, terminology and dictionary constraints?
3. How to reduce the \(T_xT_y\) cost on long sequences?
4. How to improve the quality and parallel speed of autoregressive generation at the same time?
5. How can dynamic retrieval ideas be transferred to recommendation, CAT and adaptive teaching?

## Summary of this page

Bahdanau attention solves the problem of dynamic access to fixed vectors. Transformer then retains the query-key-value retrieval idea, removes the cyclic state chain in training, and introduces multi-head and position representation. The two papers form a clear line of architectural evolution.
