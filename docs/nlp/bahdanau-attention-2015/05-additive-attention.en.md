# Additive Attention: from alignment scores to dynamic context

Before generating the \(i\) target word, Bahdanau attention calculates the correlation for each source position \(j\) based on the current translation progress, and then summarizes all source annotations into the current context:

\[
(\mathbf s_{i-1},\mathbf h_j)
\longrightarrow e_{ij}
\longrightarrow \alpha_{ij}
\longrightarrow \mathbf c_i.
\]

## 1. What does each subscript represent?

|symbol|meaning|
|---|---|
| \(i\) |The current target location to be generated|
| \(j\) |The source location being investigated|
| \(T_x\) |Source sentence length|
| \(\mathbf s_{i-1}\in\mathbb R^n\) |The decoder state before generating the current word|
| \(\mathbf h_j\in\mathbb R^{2n}\) |Bidirectional annotation for source location \(j\)|
| \(e_{ij}\in\mathbb R\) |Unnormalized match score of target location \(i\) to source location \(j\)|
| \(\alpha_{ij}\in(0,1)\) |Attention weight assigned to source location \(j\) at step \(i\)|
| \(\mathbf c_i\in\mathbb R^{2n}\) |Source context used at step \(i\)|

The same \(\mathbf h_j\) will participate in multiple target steps; the same target step will also compare all source locations.

## 2. Align the network

The paper writes the alignment model as

\[
e_{ij}=a(\mathbf s_{i-1},\mathbf h_j).
\]

The specific form given in the appendix is a single hidden layer feed-forward network:

\[
e_{ij}
=
\mathbf v_a^\top
\tanh\!\left(
\mathbf W_a\mathbf s_{i-1}
+
\mathbf U_a\mathbf h_j
\right).
\]

Let the aligned hidden layer dimension be \(n'\), then

\[
\begin{aligned}
\mathbf W_a&\in\mathbb R^{n'\times n},&
\mathbf U_a&\in\mathbb R^{n'\times 2n},&
\mathbf v_a&\in\mathbb R^{n'},\\
\mathbf W_a\mathbf s_{i-1}
+\mathbf U_a\mathbf h_j&\in\mathbb R^{n'},&
e_{ij}&\in\mathbb R.
\end{aligned}
\]

The paper uses \(n=n'=1000\). The bidirectional annotation dimension is 2000, so \(\mathbf U_a\) projects the 2000-dimensional source annotation into the 1000-dimensional alignment space.

### Why is it called additive attention?

The state projection and the annotation projection are first added, and then scored by \(\tanh\) and vector \(\mathbf v_a\). Later dot-product attention directly computes the inner product of the query and the key; both use different compatibility functions.

## 3. Do softmax on the source position

\[
\alpha_{ij}
=
\frac{\exp(e_{ij})}
{\sum_{k=1}^{T_x}\exp(e_{ik})}.
\]

So

\[
\alpha_{ij}>0,
\qquad
\sum_{j=1}^{T_x}\alpha_{ij}=1.
\]

The normalization range of softmax is the source position \(j\) of the current sentence, and cannot be normalized across target steps or across sentences in the batch.

### Padding mask

Let \(m_j=1\) represent the real token, and \(m_j=0\) represent padding. For stable implementation, first set the padding logit to \(-\infty\):

\[
\widetilde e_{ij}
=
\begin{cases}
e_{ij},&m_j=1,\\
-\infty,&m_j=0,
\end{cases}
\qquad
\boldsymbol\alpha_i
=
\operatorname{softmax}(\widetilde{\mathbf e}_i).
\]

This way the padding weight is strictly 0.

## 4. Dynamic context

\[
\mathbf c_i
=
\sum_{j=1}^{T_x}
\alpha_{ij}\mathbf h_j
=
\mathbb E_{J\sim\boldsymbol\alpha_i}[\mathbf h_J].
\]

\(\mathbf c_i\) is the expected annotation under the attention distribution. Rather than discretely picking out unique source words, the model retains a continuous soft distribution, so the entire computational graph is differentiable.

## 5. Matrix form of a target step

Arrange source comments in columns:

\[
\mathbf H=[\mathbf h_1,\ldots,\mathbf h_{T_x}]
\in\mathbb R^{2n\times T_x}.
\]

The source projection can be calculated once before decoding begins:

\[
\mathbf K_a=\mathbf U_a\mathbf H
\in\mathbb R^{n'\times T_x}.
\]

Calculation at step \(i\)

\[
\begin{aligned}
\mathbf q_i&=\mathbf W_a\mathbf s_{i-1}\in\mathbb R^{n'},\\
\mathbf E_i&=\mathbf v_a^\top\tanh(
\mathbf q_i\mathbf 1^\top+\mathbf K_a)
\in\mathbb R^{1\times T_x},\\
\boldsymbol\alpha_i&=\operatorname{softmax}(\mathbf E_i)
\in\mathbb R^{T_x},\\
\mathbf c_i&=\mathbf H\boldsymbol\alpha_i
\in\mathbb R^{2n}.
\end{aligned}
\]

Within the same target step, the scoring of all source locations can be completed in parallel. The target steps are still subject to the decoder recursive relationship.

## 6. How alignment learns from translation targets

The training data only contains source sentences and target sentences, without word-by-word alignment labels. Model minimization

\[
\mathcal L
=
-\sum_{i=1}^{T_y}
\log p(y_i\mid y_{<i},\mathbf x).
\]

Gradient of translation error across context, softmax, alignment network and bidirectional encoder, updated

\[
\mathbf W_a,\quad \mathbf U_a,\quad \mathbf v_a
\]

and the rest of the translation parameters. Alignment is the underlying structure formed within the translation task.

## 7. Soft attention and hard attention

The current paper calculates a weighted sum of all source positions, the calculation is deterministic and can be directly backpropagated. If sampling discrete locations

\[
J_i\sim\operatorname{Categorical}(\boldsymbol\alpha_i),
\qquad
\mathbf c_i=\mathbf h_{J_i},
\]

Sampling cuts off ordinary path derivatives, often requiring policy gradient or other estimation methods. Soft attention keeps training end-to-end.

## 8. Calculation amount

Each target location is calculated with a compatibility score with all source locations, and the core score is approximately

\[
O(T_xT_y n').
\]

Precomputing \(\mathbf U_a\mathbf H\) avoids duplication of source projections, but still requires processing of all target-source position combinations.

## 9. Understand boundaries

- Weights come from translation supervision and are not supervised by artificial word alignment; phrases, function words and reordering may produce scattered weights.
- \(\mathbf h_j\) already contains left and right context, so contextual comments are read.
- Dynamic reading shortens the information path; encoder capacity, vocabulary, search error and recursive calculation will still limit the model.

## Summary of this page

\[
\boxed{
e_{ij}=a(\mathbf s_{i-1},\mathbf h_j),\quad
\alpha_{ij}=\operatorname{softmax}_j(e_{ij}),\quad
\mathbf c_i=\sum_j\alpha_{ij}\mathbf h_j
}
\]

The compatibility function, the source position softmax, and the weighted sum together form a dynamic retrieval that changes with the target position.
