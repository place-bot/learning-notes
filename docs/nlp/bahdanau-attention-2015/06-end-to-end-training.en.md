# End-to-end training: How to update alignment of translation errors

RNNsearch does not manually align labels. The encoder, alignment network, decoder and output layer jointly accept the gradient of the translation loss.

## 1. Training objectives and teacher forcing

\[
p(\mathbf y\mid\mathbf x)
=
\prod_{i=1}^{T_y}
p(y_i\mid y_{<i},\mathbf x),
\qquad
\mathcal L
=
-\sum_{i=1}^{T_y}
\log p(y_i\mid y_{<i},\mathbf x).
\]

Training step \(i\) reads the real previous target word:

\[
\mathbf s_i=f(\mathbf s_{i-1},y_{i-1},\mathbf c_i).
\]

All target sentences are known, and state recursion still needs to be executed in order. During inference, the model sends its own generated words back to the next step, thus forming a training-inference input distribution difference.

## 2. Batch mask

Let \(m_i^{(b)}\) mean that the \(i\)th target position of the \(b\)th sample is valid:

\[
\mathcal L_{\text{batch}}
=
-\frac{
\sum_b\sum_i m_i^{(b)}
\log p(y_i^{(b)}\mid y_{<i}^{(b)},\mathbf x^{(b)})
}{
\sum_b\sum_i m_i^{(b)}
}.
\]

Normalizing by valid tokens avoids padding that changes the loss scale.

## 3. Backtransmission from the output layer

If \(\mathbf p_i=\operatorname{softmax}(\mathbf o_i)\), the correct word one-hot vector is \(\mathbf y_i\), then

\[
\frac{\partial\mathcal L_i}{\partial\mathbf o_i}
=
\mathbf p_i-\mathbf y_i.
\]

The error continues to the attention through deep output, state \(\mathbf s_i\) and context \(\mathbf c_i\).

## 4. Gradient of context on attention score

known

\[
\mathbf c_i=\sum_j\alpha_{ij}\mathbf h_j,
\qquad
\boldsymbol\alpha_i=\operatorname{softmax}(\mathbf e_i),
\]

remember

\[
\mathbf g_i=\frac{\partial\mathcal L}{\partial\mathbf c_i}.
\]

softmax Jacobian is

\[
\frac{\partial \alpha_{ij}}{\partial e_{ik}}
=
\alpha_{ij}
\bigl[\mathbb I(j=k)-\alpha_{ik}\bigr].
\]

Organized and available

\[
\boxed{
\frac{\partial\mathcal L}{\partial e_{ik}}
=
\alpha_{ik}\,
\mathbf g_i^\top(\mathbf h_k-\mathbf c_i)
}
\]

Among them:

- \(\alpha_{ik}\) is the current weight of position \(k\);
- \(\mathbf h_k-\mathbf c_i\) is the unique orientation of this annotation relative to the average context;
- \(\mathbf g_i\) indicates how to move the context to reduce the loss;
- The inner product measures whether the weight of the increased position \(k\) is in a favorable direction.

## 5. Gradient path of source annotation

\[
\frac{\partial\mathcal L}{\partial\mathbf h_j}
=
\underbrace{
\sum_i\alpha_{ij}
\frac{\partial\mathcal L}{\partial\mathbf c_i}
}_{\text{direct path to weighted sum}}
+
\underbrace{
\sum_i
\frac{\partial\mathcal L}{\partial e_{ij}}
\frac{\partial e_{ij}}{\partial\mathbf h_j}
}_{\text{Align fractional paths}}
+
\text{encoder recursive path}.
\]

A translation loss can thus update the output layer, decoder, alignment network, bidirectional encoder, and word embedding at both ends.

## 6. Optimization settings of the paper

- Adadelta，\(\rho=0.95,\epsilon=10^{-6}\)；
- mini-batch size 80;
- Global gradient \(L_2\) norm upper limit 1;
- Take 1600 sentence pairs each time, sort them by length and divide them into 20 batches;
- The training data is randomly shuffled once at the beginning.

If the upper limit of the gradient is \(\tau\), the cropping is written as

\[
\widetilde{\mathbf g}
=
\mathbf g
\min\!\left(1,\frac{\tau}{\|\mathbf g\|_2}\right).
\]

It limits the update amplitude and helps alleviate gradient explosion in recurrent networks.

## 7. Parameter initialization

Appendix report:

- The circular connection matrix uses a random orthogonal matrix;
- \(\mathbf W_a,\mathbf U_a\) is sampled from a Gaussian distribution with standard deviation \(0.001\);
- \(\mathbf v_a\) and bias are initialized to 0;
- The remaining weights are sampled from a Gaussian distribution with standard deviation \(0.01\).

## 8. One training iteration

```python
annotations = encoder(source, source_mask)
state = initialize(annotations)
loss = 0.0

for i in range(target_length):
    scores = alignment(state, annotations)
    alpha = masked_softmax(scores, source_mask)
    context = weighted_sum(alpha, annotations)
    state = decoder_gru(target[i - 1], state, context)
    logits = deep_output(state, target[i - 1], context)
    loss += masked_cross_entropy(logits, target[i])

loss.backward()
clip_global_grad_norm_(parameters, 1.0)
adadelta.step()
```

The implementation will vectorize batch, vocabulary projection and precomputable items, and the pseudo code retains the information dependencies of the paper.

## 9. Boundaries of training parallelization

Can be parallelized:

- Different sentences in batch;
- Attention score of all source positions within the same target step;
- Matrix operations for embedding, linear layers and softmax;
- The two directions of the bidirectional encoder can be run separately.

Must wait for:

\[
\overrightarrow{\mathbf h}_j
\leftarrow
\overrightarrow{\mathbf h}_{j-1},
\qquad
\mathbf s_i
\leftarrow
\mathbf s_{i-1}.
\]

This critical path limits the GPU's ability to process all locations simultaneously. The following article will compare RNN, Word2Vec and Transformer separately.

## Summary of this page

\[
\frac{\partial\mathcal L}{\partial e_{ik}}
=
\alpha_{ik}\,
\mathbf g_i^\top(\mathbf h_k-\mathbf c_i)
\]

Description The model compares a single source annotation to the current average context and adjusts the attention score based on whether it improves translation.
