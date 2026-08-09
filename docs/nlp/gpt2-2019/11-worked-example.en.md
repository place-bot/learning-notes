# Complete forward and generation example

## 1. Simplify settings

Consider prompt:

```text
Article: Cats sleep for many hours each day.
TL;DR:
```

To facilitate hand calculation, only four tokens are retained:

\[
(x_1,x_2,x_3,x_4)
=
(\text{Cats},\text{sleep},\text{TL;DR},\text{:}).
\]

The model needs to predict the 5th token.

## 2. Input vector

Per location:

\[
\mathbf h_t^{(0)}
=
\mathbf e(x_t)+\mathbf p_t.
\]

Suppose an attention head generates query \(\mathbf q_4\) at the last position and keys \(\mathbf k_1,\ldots,\mathbf k_4\) at four positions.

## 3. causal attention score

The last position allows viewing all existing positions:

\[
s_{4j}
=
\frac{\mathbf q_4^\top\mathbf k_j}{\sqrt{d_h}},
\qquad j\le4.
\]

Let the fraction be

\[
(s_{41},s_{42},s_{43},s_{44})
=(1.2,0.4,1.8,0.9).
\]

softmax gets approximate weights:

\[
\boldsymbol\alpha_4
\approx
(0.261,0.117,0.475,0.147).
\]

The context vector is

\[
\mathbf a_4
=
0.261\mathbf v_1
+0.117\mathbf v_2
+0.475\mathbf v_3
+0.147\mathbf v_4.
\]

Here `TL;DR` has a higher position weight, indicating that the final state will strongly read the task prompt; it also reads the article words to determine the summary content.

## 4. After residual, MLP and final LayerNorm

abbreviated as

\[
\mathbf h_4^{(1)}
=
\mathbf h_4^{(0)}
+\mathbf W_O\mathbf a_4
+\operatorname{MLP}(\cdot).
\]

Real GPT-2 will repeat 12–48 blocks, and finally get

\[
\mathbf h_4^{\mathrm{final}}.
\]

## 5. Output token probability

Assume that there are only three candidate tokens, and the logits are:

\[
z=(2.0,1.2,0.3)
\]

Correspond to `(Cats, They, Sleeping)` respectively. softmax is:

\[
p\approx(0.620,0.279,0.101).
\]

Greedy decoding will select `Cats`; sampling may select the other two.

## 6. Effect of temperature

When \(\tau=0.5\):

\[
z/\tau=(4.0,2.4,0.6),
\]

The distribution is sharper, and the token with the highest probability is more likely to be selected. When \(\tau=2\):

\[
z/\tau=(1.0,0.6,0.15),
\]

The distribution is flatter, the generation is more varied and less stable.

## 7. top-k

If \(k=2\), the third token is blocked and re-normalized within the first two tokens:

\[
p_{\mathrm{top\text{-}2}}
\approx
(0.690,0.310,0).
\]

Abstract: The experiment uses a very small \(k=2\) in order to reduce duplication and limit outrageous tokens, but it also significantly narrows the generation space.

## 8. The second step and KV cache

Assume that the first step generates `Cats`. The second step condition becomes:

\[
p(x_6\mid x_1,x_2,x_3,x_4,\text{Cats}).
\]

The K/V of the first four prompt tokens have been saved in the cache. You only need to calculate the query, key, and value of the new token, and then let the new query pay attention to all cached keys.

## 9. Where does task behavior come from?

There is no "summary module" for this forward process. The reason why `TL;DR:` is effective comes from its statistical correlation with the summary text in the training corpus. Model handle:

\[
\text{Task format} + \text{Article content} + \text{Already generated}
\]

They are jointly encoded into the hidden state and then output through the same next-token head. If there are insufficient prompt patterns in the training corpus, the article is out of context, or the decoding strategy is inappropriate, the summarization behavior will fail.
