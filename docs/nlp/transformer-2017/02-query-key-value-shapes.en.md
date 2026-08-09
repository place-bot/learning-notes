# Query, Key, Value: meaning and shape

## 1. Retrieve analogies

attention matches a query with multiple sets of key–values:

- query: what you are looking for at the current location;
- key: What features are used for each candidate position to accept matching;
- value: the content actually retrieved after matching.

The key determines the weight, and the value determines the weighted result. Both can come from the same input but be projected with different parameters.

## 2. Single header matrix

Assume batch is omitted and enter

\[
\mathbf X\in\mathbb R^{n\times d_{\text{model}}}.
\]

\[
\begin{aligned}
\mathbf Q&=\mathbf X\mathbf W^Q
\in\mathbb R^{n_q\times d_k},\\
\mathbf K&=\mathbf M\mathbf W^K
\in\mathbb R^{n_k\times d_k},\\
\mathbf V&=\mathbf M\mathbf W^V
\in\mathbb R^{n_k\times d_v}.
\end{aligned}
\]

\(\mathbf M=\mathbf X\), and \(n_q=n_k=n\) in self-attention. In cross-attention, \(\mathbf X\) comes from decoder, and \(\mathbf M\) comes from encoder.

## 3. Score and output shape

\[
\mathbf S
=
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}
\in\mathbb R^{n_q\times n_k}.
\]

Row \(i\) contains the scores of query \(i\) for all keys. After running softmax

\[
\mathbf A=\operatorname{softmax}_{\text{key}}(\mathbf S)
\in\mathbb R^{n_q\times n_k},
\qquad
\sum_j A_{ij}=1.
\]

\[
\mathbf O=\mathbf A\mathbf V
\in\mathbb R^{n_q\times d_v}.
\]

## 4. Batch and long shapes

Common implementation uses

\[
[B,h,n,d_h].
\]

Score matrix:

\[
[B,h,n_q,d_k]
\times
[B,h,d_k,n_k]
\rightarrow
[B,h,n_q,n_k].
\]

This is then multiplied by \(\mathbf V\) to get \([B,h,n_q,d_v]\), transposed and spelled back to \([B,n_q,hd_v]\).

## 5. Why reproject each layer

The input representation carries multiple features simultaneously. Different \(\mathbf W^Q,\mathbf W^K,\mathbf W^V\) allows model learning:

- Use a set of features to determine relevance;
- Use another set of features as the delivered content;
- Use different relationship spaces for each layer and each head.

## 6. Self-attention is still a contextual representation

The embedding of the same token is initially fixed, but its output

\[
\mathbf o_i=\sum_j A_{ij}\mathbf v_j
\]

Changes with the whole sentence token, position and number of layers. Transformers therefore produce contextualized token representations.
