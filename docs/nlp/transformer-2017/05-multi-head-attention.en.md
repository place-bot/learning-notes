# Multi-Head Attention

## 1. Complete formula

\[
\operatorname{head}_i
=
\operatorname{Attention}(
\mathbf Q\mathbf W_i^Q,
\mathbf K\mathbf W_i^K,
\mathbf V\mathbf W_i^V),
\]

\[
\operatorname{MultiHead}(\mathbf Q,\mathbf K,\mathbf V)
=
\operatorname{Concat}(
\operatorname{head}_1,\ldots,\operatorname{head}_h)
\mathbf W^O.
\]

## 2. Dimensions of the base of the original paper

\[
d_{\text{model}}=512,\qquad
h=8,\qquad
d_k=d_v=64.
\]

Each head outputs 64 dimensions, after splicing

\[
8\times64=512.
\]

\(\mathbf W^O\in\mathbb R^{512\times512}\) then mixes the information from each header.

## 3. Parameter shape

\[
\mathbf W_i^Q,\mathbf W_i^K,\mathbf W_i^V
\in\mathbb R^{512\times64},
\qquad
\mathbf W^O\in\mathbb R^{512\times512}.
\]

In actual code, a piece of \([512,3\times512]\) weight is commonly used to generate QKV at the same time, and then reshaped into 8 heads.

## 4. The role of bulls

The single-head output will compress multiple positions into a weighted average. Using different projections, multiple heads can be retrieved independently in different subspaces and positional patterns, such as local collocations, long-distance reference, or syntactic relations. The paper's attention visualization shows that different heads form different structures, but there is no guarantee that each head has a stable human label.

## 5. Why is the amount of calculation not multiplied eight times?

If a single head uses the full 512 dimensions, the QK dot product size is approximately \(n^2\cdot512\). Each of the eight heads uses 64 dimensions, and the total is still

\[
8\cdot n^2\cdot64=n^2\cdot512.
\]

The projection and output matrices will increase constant overhead, and the main attention multipliers remain of the same order.

## 6. Paper ablation

Under similar computing budgets, the BLEU of the single-head development set is 24.9, and the base eight-head BLEU is 25.8; the BLEU of the 16-head development set is the same as 25.8, and the BLEU of the 32-head development set drops to 25.4. Too few heads will limit the subspace, and too many heads will make the dimensions of each head too narrow.

## 7. Interface with LoRA

Subsequent LoRA papers will focus on

\[
\mathbf W^Q,\mathbf W^K,\mathbf W^V,\mathbf W^O
\]

regarded as adaptable weights. It freezes the original matrix and only learns low-rank increments; the original LoRA experiment often preferentially adapts \(W_q\) and \(W_v\).
