# Bahdanau Attention: Joint Learning Alignment and Translation

This topic focuses on the paper **Neural Machine Translation by Jointly Learning to Align and Translate** by Dzmitry Bahdanau, Kyunghyun Cho and Yoshua Bengio.

The paper starts from the fixed vector bottleneck of early neural machine translation and proposes a mechanism later often called **Bahdanau attention** or **additive attention**. Before generating each target word, it recalculates a set of source weights based on the current decoding state, and then uses the weighted sum to form the context of the current step.

## Read the paper with a picture

```text
Source sentence x1, x2, ..., xTx
        │
        ├── Forward GRU ──► h→1, h→2, ..., h→Tx
        │
        └── Reverse GRU ──► h←1, h←2, ..., h←Tx
                           │
                           ▼
              Bidirectional annotation hj = [h→j ; h←j]
                           │
             Recalculate for each target position i
                           ▼
    Previous decoding state si-1 ─► additive alignment score eij
                           │ Do softmax on all source positions
                           ▼
                    Attention weight αij
                           │
                           ▼
                  ci = Σj αij hj
                           │
                           ▼
        Previous target word yi-1 + si-1 + ci
                           │
                           ▼
                 Decoding state and next word yi
```

## Citation details

|item|information|
|---|---|
|Author| Dzmitry Bahdanau、Kyunghyun Cho、Yoshua Bengio |
|Officially announced| ICLR 2015 Conference Paper，Oral Presentation |
| arXiv | [1409.0473](https://arxiv.org/abs/1409.0473) |
|first submission|September 1, 2014|
|Check version of this topic|v7, May 19, 2016|
|The author publicly implements| [lisa-groundhog/GroundHog](https://github.com/lisa-groundhog/GroundHog/tree/master/experiments/nmt) |

The paper first appeared as an arXiv preprint in 2014 and was subsequently published as an ICLR 2015 conference paper. The official ICLR schedule lists this as an oral presentation on May 9, 2015.

## The core problem to be solved in the paper

Early RNN Encoder–Decoder compresses the entire source sentence into a fixed-dimensional vector:

\[
\mathbf x
\longrightarrow
\mathbf c
\longrightarrow
\mathbf y.
\]

When the source sentence becomes longer, \(\mathbf c\) must simultaneously preserve entities, modification relationships, long-distance dependencies, word order, and all details. The paper regards this fixed vector as the main bottleneck affecting the translation of long sentences.

RNNsearch retains an entire list of source annotations:

\[
\mathbf h_1,\mathbf h_2,\ldots,\mathbf h_{T_x},
\]

And generate independent context for each step of the target:

\[
\mathbf c_i
=
\sum_{j=1}^{T_x}
\alpha_{ij}\mathbf h_j.
\]

Therefore, the same sentence source text can provide different information summaries when generating different target words.

## Four-layer structure of paper contribution

### 1. Presentation layer

Bidirectional RNN generates annotations \(\mathbf h_j\) containing both left and right context for each source word.

### 2. Retrieval layer

Alignment network \(a(\mathbf s_{i-1},\mathbf h_j)\) computes the matching score of the previous decoded state to each source position.

### 3. Probability layer

The score is subjected to softmax at the source position to obtain the normalized weight \(\alpha_{ij}\), and then the desired annotation \(\mathbf c_i\) is formed.

### 4. Learning layer

Weights are continuous and differentiable. The gradient of the translation negative log-likelihood can pass through the context, softmax, alignment network and bidirectional encoder, so that translation and alignment are jointly learned.

## Original text scope

The main text of the paper and the appendix clearly state:

- Probabilistic decomposition of fixed vector RNN Encoder–Decoder;
- Stepwise context for RNNsearch;
- additive alignment model；
- Bidirectional RNN encoder;
- Complete formula of gated hidden unit;
- deep output and maxout output layers;
- WMT 2014 British and French data, preprocessing and model size;
- Adadelta, gradient norm constraints, batch sorting and parameter initialization;
- BLEU result, length grouping curve, alignment heat map and long sentence translation examples;
- Comparison of RNNencdec, RNNsearch and Moses;
- GroundHog/Theano implementation link.

Topics will supplement this content with shape checking, gradient derivation, hand calculation examples, and modern PyTorch implementations, keeping the supplementary derivation separate from the original presentation.

## Recommended reading route

### First time: establishing a complete information flow

1. [Paper identity, problems and innovation](01-paper-identity-motivation.md)
2. [Probabilistic basis of neural machine translation and fixed vector bottleneck](02-nmt-probability-and-fixed-vector.md)
3. [Bidirectional encoder and source annotation](03-bidirectional-encoder.md)
4. [Step-by-step decoding and conditional generation](04-decoder-and-generation.md)
5. [Additive Attention complete derivation of](05-additive-attention.md)

### The second time: thorough training and reasoning

1. [End-to-end goal with backpropagation](06-end-to-end-training.md)
2. [GRU, Initialization and Deep Output](07-gru-and-deep-output.md)
3. [Beam Search and Inference](08-beam-search-and-inference.md)
4. [Step-by-step hand calculation: from attention to gradient](09-worked-example.md)

### The third time: judging experimental evidence

1. [Experimental design, data and training configuration](10-experiment-design.md)
2. [BLEU result and length analysis](11-results-and-length-analysis.md)
3. [Soft alignment and long sentence case](12-alignment-and-long-sentences.md)

### Fourth Time: Connecting Code to Modern Models

1. [GroundHog original code intensive reading](13-groundhog-code-reading.md)
2. [Modern PyTorch implementation](14-modern-pytorch-implementation.md)
3. [Attention explanation, complexity and bounds](15-attention-interpretation-and-complexity.md)
4. [Limitations, Transformer interface and follow-up work](16-limitations-transformer-future.md)
5. [Symbol table, conclusion and reading map](17-symbols-conclusion.md)

## You should be able to explain after reading

- Fixed the specific information path where the vector bottleneck occurs;
- Why annotations at each source location require bidirectional context;
- What do \(\mathbf s_{i-1}\), \(\mathbf h_j\), \(e_{ij}\), \(\alpha_{ij}\) and \(\mathbf c_i\) mean respectively;
-Matrix shape of each step of additive attention;
- Why soft alignment can be trained with standard backpropagation;
- How does the gated hidden unit in the paper differ from modern GRU notation;
- How deep output and maxout generate vocabulary probability;
- How the training phase is different from the beam-search inference phase;
- Which results do the experimental advantages of RNNsearch-50 come from?
- Why "No UNK" BLEU should be explained separately from the full test set BLEU;
- What conclusions can the alignment heat map support, and what cannot be proven alone?
- How GroundHog code implements precomputation, mask, dynamic context and beam search;
- The connection and difference between Bahdanau attention and Transformer cross-attention and self-attention.
