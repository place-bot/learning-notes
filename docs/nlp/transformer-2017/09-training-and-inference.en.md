# Training, optimizer and autoregressive inference

## 1. Objective function

\[
\mathcal L
=
-\sum_t\log
p(y_t\mid y_{<t},\mathbf x).
\]

Target right shift with causal mask lets logits for all locations be computed once while maintaining conditional probability constraints.

## 2. Data

- WMT14 English-German: about 4.5 million sentence pairs, sharing about 37k BPE vocabulary;
- WMT14 English and French: about 36 million sentence pairs, about 32k word-piece vocabulary;
- batches are grouped by approximate length;
- About 25k source tokens and 25k target tokens per batch.

## 3. Adam and Noam schedule

\[
\operatorname{lr}
=
d_{\text{model}}^{-1/2}
\min(
\operatorname{step}^{-1/2},
\operatorname{step}\cdot
\operatorname{warmup}^{-3/2}).
\]

The paper adopts

\[
\beta_1=0.9,\quad
\beta_2=0.98,\quad
\epsilon=10^{-9},\quad
\operatorname{warmup}=4000.
\]

The learning rate increases linearly for the first 4000 steps, and then decreases reciprocally according to the square root of the number of steps.

## 4. Regularization

- residual dropout；
- dropout of the sum of embedding and positional encoding;
- base dropout 0.1；
- label smoothing \(\epsilon_{ls}=0.1\)。

Label smoothing will make the model's target probability of the correct class less than 1, which may improve cross-entropy/perplexity, but improve accuracy and BLEU.

## 5. Training scale

One machine, 8 pieces of P100:

- base: 100k steps, about 12 hours, about 0.4 seconds per step;
- big: 300k steps, about 3.5 days, about 1.0 seconds per step.

## 6. Decoding

The paper uses beam size 4, length penalty \(\alpha=0.6\), and the maximum output length is the input length plus 50. base averages the last 5 checkpoints, big averages the last 20 checkpoints.

## 7. KV cache

Modern autoregressive inference caches the K/V of previous layers to avoid recomputing the entire prefix each time. The new token still needs to wait for the previous token to be determined, so the cache reduces repeated calculations at each step without eliminating token-level serial generation.
