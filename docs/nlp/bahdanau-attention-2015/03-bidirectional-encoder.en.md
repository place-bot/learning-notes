# Bidirectional encoder and source annotation

## 1. Why attention reads comments

Attention is assigned a weight on the source location \(j\). If there is only an isolated word embedding at each position:

\[
\mathbf E_x x_j,
\]

It is difficult for the model to determine word meaning, phrase boundaries, and syntactic roles based on this vector alone.

The paper first encodes each positional into contextual annotations:

\[
\mathbf h_j.
\]

\(\mathbf h_j\) is centered on \(x_j\) and contains both preceding and following information.

## 2. Directional restrictions of one-way RNN

Forward RNN:

\[
\overrightarrow{\mathbf h}_j
=
\overrightarrow f
\left(
\overrightarrow{\mathbf h}_{j-1},
\mathbf E_x x_j
\right).
\tag{1}
\]

\(\overrightarrow{\mathbf h}_j\) can access:

\[
x_1,\ldots,x_j.
\]

It has not yet read while processing \(x_j\):

\[
x_{j+1},\ldots,x_{T_x}.
\]

Word meaning and grammatical roles in machine translation often rely on right-hand context, so using only forward states limits annotations at each position.

## 3. Reverse RNN

Reverse RNN reads from the end of the clause to the beginning:

\[
\overleftarrow{\mathbf h}_j
=
\overleftarrow f
\left(
\overleftarrow{\mathbf h}_{j+1},
\mathbf E_x x_j
\right).
\tag{2}
\]

\(\overleftarrow{\mathbf h}_j\) can access:

\[
x_j,\ldots,x_{T_x}.
\]

The paper shares the source word embedding matrix \(\mathbf E_x\) in both directions, and the recursive weights are learned separately.

## 4. Splicing to form comments

The comment for source location \(j\) is:

\[
\mathbf h_j
=
\begin{bmatrix}
\overrightarrow{\mathbf h}_j\\
\overleftarrow{\mathbf h}_j
\end{bmatrix}.
\tag{3}
\]

If there are \(n\) hidden units in each direction:

\[
\overrightarrow{\mathbf h}_j,
\overleftarrow{\mathbf h}_j
\in\mathbb R^n,
\]

Then:

\[
\mathbf h_j\in\mathbb R^{2n}.
\]

Thesis experiments take:

\[
n=1000,
\]

So each annotation dimension is:

\[
2n=2000.
\]

## 5. Annotation matrix

Arrange all comments by source location:

\[
H
=
\begin{bmatrix}
\mathbf h_1^\top\\
\mathbf h_2^\top\\
\vdots\\
\mathbf h_{T_x}^\top
\end{bmatrix}
\in
\mathbb R^{T_x\times 2n}.
\tag{4}
\]

For batch training, add the batch dimension:

\[
H\in
\mathbb R^{B\times T_x\times 2n}.
\]

GroundHog/Theano uses time-first layout:

\[
H\in
\mathbb R^{T_x\times B\times 2n}.
\]

The order of shapes is different, but the mathematical content is the same.

## 6. The meaning of "focus around word \(j\)"

Theoretically, \(\mathbf h_j\) can contain the entire sentence of information:

- Forward status summary \(x_{\le j}\);
- Reverse status summary \(x_{\ge j}\).

The paper points out that RNNs tend to represent recent inputs more strongly, so \(\mathbf h_j\) will highlight the area around \(x_j\).

This is an inductive bias that does not require the annotation to contain only a local window. The actual information range is:

-Gating status;
- training data;
- hidden dimensions;
- Gradient propagation;
- Sentence length;
- Translation target

Decide together.

## 7. encoder uses gated hidden unit

The paper uses the gated hidden unit proposed by Cho et al., which is later often referred to as the GRU structure.

To simplify notation, let the source word embedding:

\[
\mathbf e_j=\mathbf E_x x_j.
\]

Take the forward encoder as an example.

### 7.1 Update Gate

\[
\overrightarrow{\mathbf z}_j
=
\sigma
\left(
\overrightarrow W_z\mathbf e_j
+
\overrightarrow U_z
\overrightarrow{\mathbf h}_{j-1}
\right).
\tag{5}
\]

### 7.2 Reset gate

\[
\overrightarrow{\mathbf r}_j
=
\sigma
\left(
\overrightarrow W_r\mathbf e_j
+
\overrightarrow U_r
\overrightarrow{\mathbf h}_{j-1}
\right).
\tag{6}
\]

### 7.3 Candidate status

\[
\widetilde{\overrightarrow{\mathbf h}}_j
=
\tanh
\left(
\overrightarrow W\mathbf e_j
+
\overrightarrow U
\left[
\overrightarrow{\mathbf r}_j
\odot
\overrightarrow{\mathbf h}_{j-1}
\right]
\right).
\tag{7}
\]

### 7.4 New status

\[
\overrightarrow{\mathbf h}_j
=
(1-\overrightarrow{\mathbf z}_j)
\odot
\overrightarrow{\mathbf h}_{j-1}
+
\overrightarrow{\mathbf z}_j
\odot
\widetilde{\overrightarrow{\mathbf h}}_j.
\tag{8}
\]

The reverse encoder uses independent parameters and applies the same formula in reverse order.

## 8. Update the door mark reminder

In formula (8):

- \(z\) close to 0: more retain the old state;
- \(z\) Close to 1: More adoption candidate states.

Different libraries may write the two items of the update gate as:

\[
z\odot h_{\text{old}}
+
(1-z)\odot\widetilde h.
\]

It's just the way the door is defined that is different. When reproducing a paper, the agreement between the paper and the corresponding code shall prevail.

## 9. Reset door position

Thesis candidate status uses:

\[
U(r\odot h_{\text{old}}).
\]

Some modern libraries' GRU implementations place the reset gate after the hidden linear transformation:

\[
r\odot(Uh_{\text{old}}).
\]

In general:

\[
U(r\odot h)
\neq
r\odot(Uh).
\]

Therefore, directly replacing the `GRUCell` that comes with the framework can maintain the overall structure, but it may not match the thesis units item by item.

## 10. Initial state and sentence boundaries

The forward state usually starts from zero:

\[
\overrightarrow{\mathbf h}_0=\mathbf 0.
\]

The reverse state starts at the sentence-end boundary:

\[
\overleftarrow{\mathbf h}_{T_x+1}=\mathbf 0.
\]

The implementation will add a terminator to the sequence and use mask to distinguish real tokens from padding.

## 11. How to enter bidirectional encoding in Mask

Sentence lengths vary within a batch. Assume:

\[
m_{bj}
\in
\{0,1\}
\]

Indicates whether the \(j\)-th position of the \(b\)-th sentence in the batch is valid.

Commonly used masked update:

\[
\mathbf h_{bj}
\leftarrow
m_{bj}\mathbf h_{bj}^{\text{new}}
+
(1-m_{bj})\mathbf h_{b,j-1}.
\]

The same source mask must also be used in the attention stage to avoid assigning probability to padding positions.

## 12. Why splicing

Splicing preserves independent coordinates in both directions:

\[
[\overrightarrow h_j;\overleftarrow h_j].
\]

The summation requires that both sets of state dimensions be identical and is forced to blend before entering attention. Splicing allows the \(U_a\) aligned network to learn on its own how to combine the two directions.

The cost is that the annotation dimension changes from \(n\) to \(2n\).

## 13. Coding differences from basic RNNencdec

The author's public configuration clearly distinguishes between the two.

### RNNencdec

```text
last_forward = True
forward      = False
backward     = False
search       = False
```

The base model copies the forward encoder's final state as a fixed context for all target positions.

### RNNsearch

```text
last_forward = False
forward      = True
backward     = True
search       = True
```

The new model retains the forward and reverse states of each position and enables dynamic search.

## 14. Three levels of encoder output

|object|shape|information|
|---|---|---|
|Source word embedding \(\mathbf e_j\)| \(m\) |Current word type|
|One-way status \(\overrightarrow{\mathbf h}_j\)| \(n\) |left to current position|
|One-way status \(\overleftarrow{\mathbf h}_j\)| \(n\) |Right to current position|
|Bidirectional annotation \(\mathbf h_j\)| \(2n\) |Two-way context centered on current location|
|Annotation sequence \(H\)| \(T_x\times2n\) |Source memory readable by attention|

## 15. From encoder to attention

The encoder is only responsible for generating \(H\). It does not decide in advance where each target word will be aligned.

When reaching the target position \(i\), align the network to read:

\[
\mathbf s_{i-1}
\quad\text{and}\quad
\mathbf h_1,\ldots,\mathbf h_{T_x},
\]

Then calculate the distribution of the current step. Source annotations are encoded once and read multiple times.

This is an early form of subsequent encoder memory and decoder cross-attention.
