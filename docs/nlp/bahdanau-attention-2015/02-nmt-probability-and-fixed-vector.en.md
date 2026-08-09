# Probabilistic basis and fixed vector bottleneck of neural machine translation

## 1. Translation is conditional sequence modeling

Given source sentence

\[
\mathbf x=(x_1,\ldots,x_{T_x}),
\]

The translation system needs to find the target sentence

\[
\mathbf y=(y_1,\ldots,y_{T_y})
\]

Maximize the conditional probability:

\[
\widehat{\mathbf y}
=
\operatorname*{arg\,max}_{\mathbf y}
p_\theta(\mathbf y\mid\mathbf x).
\]

Model parameters \(\theta\) are learned from parallel sentence pairs.

## 2. Autoregressive decomposition

The joint conditional probability is decomposed in target word order:

\[
p_\theta(\mathbf y\mid\mathbf x)
=
\prod_{i=1}^{T_y}
p_\theta(y_i\mid y_1,\ldots,y_{i-1},\mathbf x).
\tag{1}
\]

Take the logarithm:

\[
\log p_\theta(\mathbf y\mid\mathbf x)
=
\sum_{i=1}^{T_y}
\log p_\theta(y_i\mid y_{<i},\mathbf x).
\tag{2}
\]

This turns the sentence-level target into a series of word-level predictions, but each word-level condition still relies on the full source sentence and the target prefix.

## 3. Training objectives

Let the parallel corpus be

\[
\mathcal D
=
\{(\mathbf x^{(n)},\mathbf y^{(n)})\}_{n=1}^{N}.
\]

Maximum likelihood training is equivalent to minimizing the negative log-likelihood:

\[
\mathcal L(\theta)
=
-\sum_{n=1}^{N}
\sum_{i=1}^{T_y^{(n)}}
\log
p_\theta
\left(
y_i^{(n)}
\mid
y_{<i}^{(n)},
\mathbf x^{(n)}
\right).
\tag{3}
\]

The actual calculation also requires a mask to exclude the padding positions filled in the batch.

## 4. Target prefix during training

At each training position, the model reads the true previous target word \(y_{i-1}\) and predicts the true current word \(y_i\). This practice came to be commonly known as teacher forcing.

```text
Real target sentence: <bos> le chat dort <eos>
Enter prefix: <bos> le chat dort
Supervision target: le chat dort <eos>
```

The training loss can aggregate multiple target locations, but the RNN hidden states are still recursive in time.

The real target prefix is not available during inference, and the model must read the words it has already generated. The training and inference prefixes come from different sources, which will bring exposure bias.

## 5. Basic RNN Encoder–Decoder

### 5.1 encoder

The encoder reads source words in order:

\[
\mathbf h_t
=
f_{\mathrm{enc}}
(\mathbf h_{t-1},\mathbf E_x x_t).
\tag{4}
\]

Among them, \(\mathbf E_x x_t\) represents the source word embedding.

Finally, a fixed vector is used to summarize the source sentence:

\[
\mathbf c
=
q(\mathbf h_1,\ldots,\mathbf h_{T_x}).
\tag{5}
\]

Common choices are:

\[
\mathbf c=\mathbf h_{T_x}.
\tag{6}
\]

### 5.2 decoder

Decoding state recursion:

\[
\mathbf s_i
=
f_{\mathrm{dec}}
(\mathbf s_{i-1},\mathbf E_y y_{i-1},\mathbf c).
\tag{7}
\]

The target word probability is:

\[
p_\theta(y_i\mid y_{<i},\mathbf x)
=
g(y_{i-1},\mathbf s_i,\mathbf c).
\tag{8}
\]

All target locations share the same \(\mathbf c\).

## 6. Fixed vector interface

The information flow of the basic model is:

```text
x1 → x2 → ... → xTx
                  │
                  ▼
             single vector c
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
      y1         y2        ... yTy
```

\(\mathbf c\) is also:

- The only direct channel from encoder to decoder;
- Source sentence summary shared for each target position;
- The basis for decoder to restore all source details.

## 7. Why does the bottleneck increase with sentence length?

### 7.1 Increase in the number of messages

The longer the source sentence, the more entities, relationships, and local structures that need to be preserved.

### 7.2 Increased recursion distance

The influence of early source words on the final state needs to go through more recursive updates, and the gradient also needs to return along a longer path.

### 7.3 Decoding requirements change over time

The source information that needs to be paid attention to when generating target words \(y_i\) and \(y_{i+k}\) is different. Fixed \(\mathbf c\) Unable to explicitly change read position.

### 7.4 Training length distribution restrictions

Sentences that exceed the training length require the model to squeeze more information into the same dimension and hold it for longer.

## 8. Dimension fixation and information fixation

"Fixed length" describes that the vector dimension does not change with the length of the source sentence:

\[
\mathbf c\in\mathbb R^d
\quad
\text{to any}T_x.
\]

A real vector can mathematically encode a lot of information, so the bottleneck is not a simple information-theoretic impossibility conclusion. The paper focuses on learnability:

- limited accuracy;
- limited parameters;
- Limited training data;
- Gradient propagation of RNN;
- Generalizable continuous representation;
- Whether the downstream decoder can retrieve details stably.

## 9. Probabilistic rewriting of RNNsearch

RNNsearch introduces \(\mathbf c_i\) for each target location:

\[
p_\theta
(y_i\mid y_{<i},\mathbf x)
=
g(y_{i-1},\mathbf s_i,\mathbf c_i),
\tag{9}
\]

\[
\mathbf s_i
=
f_{\mathrm{dec}}
(\mathbf s_{i-1},y_{i-1},\mathbf c_i).
\tag{10}
\]

The conditional probability still maintains the autoregressive decomposition of equation (1). What has changed is the source information interface:

\[
\mathbf c
\quad\longrightarrow\quad
\mathbf c_1,\ldots,\mathbf c_{T_y}.
\]

## 10. From compression to addressable reading

RNNsearch encoder output:

\[
H
=
(\mathbf h_1,\ldots,\mathbf h_{T_x}).
\]

Decoder step \(i\) reads through attention:

\[
\operatorname{Read}(\mathbf s_{i-1},H)
=
\mathbf c_i.
\]

This can be understood as a differentiable content addressing process:

1. Use \(\mathbf s_{i-1}\) to indicate the current translation progress;
2. Calculate compatibility with each \(\mathbf h_j\);
3. Normalize the source position;
4. Aggregate the required information.

## 11. Dynamic context is still a fixed dimension

The dimensions of each \(\mathbf c_i\) remain fixed:

\[
\mathbf c_i\in\mathbb R^{d_h}.
\]

The key difference is that \(\mathbf c_i\) can change with \(i\). The model does not need a vector to hold all the information permanently, it only needs to form a suitable summary at the current step.

## 12. Structural comparison of the two models

|Dimensions| RNNencdec | RNNsearch |
|---|---|---|
|Source output|single vector|annotation sequence|
|source sentence direction|One-way RNN|Bidirectional RNN|
|target context|All steps are the same|Recalculate every step|
|Alignment|No explicit mechanism|Can be aligned with Microsoft|
|training supervision|target word|target word|
|long sentence information path|All after final encoding state|Read directly from any source location|
|Additional cost per step|low|Traverse all source locations to score|

## 13. The relationship between likelihood and BLEU

Training directly optimizes the token-level log-likelihood of equation (3). The experiment uses BLEU evaluation to generate translations.

The two have different goals:

- Likelihood rewards the conditional probability of each word in the true target sequence;
- BLEU compares the n-gram overlap between the generated sentence and the reference sentence and includes a length penalty;
- Beam search approximates to find high probability sequences;
- Higher likelihood usually helps translation, but does not guarantee a monotonic improvement in BLEU.

The paper reports NLL during training and BLEU for the final comparison.

## 14. The main conclusion of this chapter

RNNsearch does not change the autoregressive probabilistic definition of neural machine translation. It redesigns the mechanism of "how to access the source sentence" in conditional probability:

\[
\boxed{
\text{single fixed summary}
\;\longrightarrow\;
\text{Stepwise soft reading controlled by decoding status}
}
\]

The next chapter details how readable source annotations are generated by a bidirectional encoder.
