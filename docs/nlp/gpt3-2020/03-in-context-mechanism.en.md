# Probabilistic form of In-context learning

## 1. The pretraining goal has not changed

GPT-3 still minimizes autoregressive cross-entropy:

\[
\mathcal L_{\mathrm{pretrain}}(\theta)
=
-\mathbb E_{x\sim\mathcal D}
\sum_{t=1}^{T}
\log p_\theta(x_t\mid x_{<t}).
\]

There is no special few-shot loss during training, nor is each web page explicitly divided into support set and query set.

## 2. Prompt turns the task into a conditional probability

Consider an example of a classification task:

```text
Review: wonderful movie
Sentiment: positive

Review: boring plot
Sentiment: negative

Review: delightful acting
Sentiment:
```

Model comparison:

\[
p_\theta(\text{positive}\mid c)
\quad\text{with}\quad
p_\theta(\text{negative}\mid c).
\]

The examples illustrate both label semantics and output formats and input-to-output mappings.

## 3. Sequence-level answer scoring

If the answer is \(y=(y_1,\ldots,y_m)\), its conditional logarithmic probability is

\[
\log p_\theta(y\mid c)
=
\sum_{r=1}^{m}
\log p_\theta(y_r\mid c,y_{<r}).
\]

The multiple choice task can calculate the score for each candidate \(a\in\mathcal A\) and then take the maximum value:

\[
\hat a
=
\arg\max_{a\in\mathcal A}
S(a;c).
\]

Depending on the task, papers use raw probability, length normalization, or inter-candidate normalization; these details can change accuracy.

## 4. Example of how to enter each layer

For query position \(t\), self-attention can read the entire left prompt:

\[
\mathbf h_t^{(\ell)}
=
F_\ell
\left(
\mathbf h_{\le t}^{(\ell-1)}
\right).
\]

The token of the earlier example affects the attention output of the current query through K/V. After combining layers, the current hidden state can be encoded:

-Current task category;
- Input and output field boundaries;
- Tag word meaning;
- Common conversion rules in the examples;
- The similarity of the current new input to the example.

The paper does not directly identify which algorithm is implemented in each layer. These are mechanically allowed computations, not internal explanations that have been proven layer by layer.

## 5. Why is the number of examples limited by context?

The total length of the context satisfies:

\[
\sum_{i=1}^{K}
\left(|x_i|+|y_i|+|\text{format}_i|\right)
+|x_*|
+|y_*|
\le 2048.
\]

The longer the example, the smaller the \(K\) that can be placed; if too many examples are given, the earliest content will be truncated or there will be insufficient space left for the answer.

## 6. Temporary nature of in-context learning

Suppose two prompts define tasks A and B respectively:

\[
p_\theta(y\mid c_A,x)
\ne
p_\theta(y\mid c_B,x).
\]

The difference is made by context, \(\theta\) is the same. Task switching has almost no training cost, but the model does not write new rules into long-term parameters.

## 7. Three levels of the word “learning”

|level|Change object|time scale|
|---|---|---|
|pretraining|Parameter \(\theta\)|Billions to hundreds of billions of tokens|
|context adaptation| activations / KV states |within a prompt|
|autoregressive generation|Token condition has been generated|each build step|

Distinguishing these three layers can avoid mistakenly writing in-context learning as small sample fine-tuning.
