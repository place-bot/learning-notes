# State encoding and dual-channel attention

NCAT's neural network needs to turn a variable-length set state \(s_t\) with a mixture of correct and incorrect answers into a fixed-dimensional vector, and then output the Q-values of all candidate questions.

## 1. Why are there two channels?

Assume before step \(t\):

- The collection of incorrect answers contains \(k_0\) questions;
- The set of correct answers contains \(k_1\) questions.

Correct responses and incorrect responses to the same question carry different measurement information, so the paper uses two independent embedding tables:

\[
E^0\in\mathbb R^{|\mathcal J|\times d},
\qquad
E^1\in\mathbb R^{|\mathcal J|\times d}.
\]

Look up the wrongly answered questions and get

\[
\mathbf E_t^0
=
[\mathbf e_{q_1}^0,\ldots,\mathbf e_{q_{k_0}}^0]^\top
\in\mathbb R^{k_0\times d},
\]

Look up the correctly answered questions to get

\[
\mathbf E_t^1
=
[\mathbf e_{q_1}^1,\ldots,\mathbf e_{q_{k_1}}^1]^\top
\in\mathbb R^{k_1\times d}.
\]

The padding question number in the implementation cannot participate in attention and pooling.

## 2. Performance Learning: In-channel modeling

There may be relationships between knowledge points, difficulty and question types between correct and incorrect questions. NCAT uses self-attention for the two channels respectively:

\[
\mathbf S_t^z
=
\operatorname{Attention}
\left(
\mathbf E_t^zW_{1,c}^z,
\mathbf E_t^zW_{1,k}^z,
\mathbf E_t^zW_{1,v}^z
\right),
\qquad z\in\{0,1\}.
\tag{1}
\]

Scaled dot product attention is defined as

\[
\operatorname{Attention}(C,K,V)
=
\operatorname{softmax}
\left(
\frac{CK^\top}{\sqrt d}
\right)V.
\tag{2}
\]

Then through the position-by-position feed-forward network:

\[
\mathbf F_t^z
=
\operatorname{FFN}(\mathbf S_t^z)
=
\sigma(\mathbf S_t^zW^{(1)}+b^{(1)})W^{(2)}+b^{(2)}.
\tag{3}
\]

The paper uses ReLU as \(\sigma\). The real code also includes multi-head projection, residual, LayerNorm and dropout.

### A two-question self-attention small example

Suppose there are two questions in a channel, \(d=2\). For the highlighting mechanism, the projection matrices are all unit matrices:

\[
\mathbf E
=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}.
\]

The score matrix is

\[
\frac{\mathbf E\mathbf E^\top}{\sqrt2}
=
\begin{bmatrix}
1/\sqrt2&0\\
0&1/\sqrt2
\end{bmatrix}.
\]

After line-by-line softmax, the diagonal weight is larger, indicating that each question pays more attention to itself; if the embeddings of two questions are similar, the off-diagonal weight will increase, and the output will integrate the information of the other question.

## 3. Contradiction Learning: Cross-channel modeling

Simply looking at the set of correct answers or the set of incorrect answers is not sufficient to identify response contradictions. For example:

- The student correctly answered a difficult multiplication problem;
- At the same time, they answered incorrectly a relatively simple addition question related to knowledge points.

This may come from guesses, mistakes, item ambiguities, or local knowledge structures. NCAT calculates a contradiction score for each "wrong answer-correct answer" pairing:

\[
\alpha_{ij}
=
\frac{
(W_{2,c}^0\mathbf e_{q_i}^0)
(W_{2,k}^1\mathbf e_{q_j}^1)^\top
}{
\sqrt d
}.
\tag{4}
\]

All fractions make up

\[
A\in\mathbb R^{k_0\times k_1}.
\]

Softmax row-wise and column-wise for \(A\):

\[
\widetilde A^0_{ij}
=
\frac{\exp(\alpha_{ij})}
{\sum_{j'=1}^{k_1}\exp(\alpha_{ij'})},
\qquad
\widetilde A^1_{ij}
=
\frac{\exp(\alpha_{ij})}
{\sum_{i'=1}^{k_0}\exp(\alpha_{i'j})}.
\tag{5}
\]

Then aggregate the output of Performance Learning across channels:

\[
\mathbf F_t^{1\rightarrow0}
=
\operatorname{FFN}
\left(
\widetilde A^0\mathbf F_t^1
\right)
\in\mathbb R^{k_0\times d},
\tag{6}
\]

\[
\mathbf F_t^{0\rightarrow1}
=
\operatorname{FFN}
\left(
(\widetilde A^1)^\top\mathbf F_t^0
\right)
\in\mathbb R^{k_1\times d}.
\tag{7}
\]

Two normalizations answer different questions:

- Which correct questions should be most referred to for each wrong answer question;
- Which wrong questions should be most referred to for each correct answer?

## 4. From four matrices to one student state vector

The paper performs average pooling on four matrices:

\[
\operatorname{pool}(\mathbf X)
=
\frac{1}{m}\sum_{r=1}^{m}\mathbf X_{r,:}.
\tag{8}
\]

spliced to get

\[
\mathbf u_t
=
\operatorname{concat}
\left[
\operatorname{pool}(\mathbf F_t^0),
\operatorname{pool}(\mathbf F_t^1),
\operatorname{pool}(\mathbf F_t^{1\rightarrow0}),
\operatorname{pool}(\mathbf F_t^{0\rightarrow1})
\right]
\in\mathbb R^{4d}.
\tag{9}
\]

policy layer output:

\[
Q_\phi(s_t,\cdot)
=
\delta(\mathbf u_tW^{(1)}+b^{(1)})W^{(2)}+b^{(2)}
\in\mathbb R^{|\mathcal J|}.
\tag{10}
\]

Among them \(W^{(1)}\in\mathbb R^{4d\times d_p}\), \(W^{(2)}\in\mathbb R^{d_p\times|\mathcal J|}\).

## 5. Differences in pooling between papers and warehouses

Thesis formula (8) performs average pooling on all four features. The actual forward of the public warehouse `NCAT.py` is:

- Two contradiction outputs are averaged in the sequence dimension;
- The two self-attention channels take their respective "last valid positions";
- Then spell it into \(4d\) vector.

Core code corresponds to:

```python
input_01, input_10 = self.contradiction(
    item_emb_0, item_emb_1, item_per_1, item_per_0
)
input_01, input_10 = input_01.mean(-2), input_10.mean(-2)

input_0 = item_per_0[torch.arange(batch_size), p_0_target]
input_1 = item_per_1[torch.arange(batch_size), p_1_target]
state_vector = torch.cat([input_0, input_1, input_01, input_10], dim=-1)
q_values = self.policy_layer(state_vector)
```

This makes the warehouse representation more sensitive to sequence fill position and "last valid question". The paper also assumes that ability is stable during the short test and the order of responses is not important. Therefore, if the goal is to reproduce the formula of the paper, masked mean is more consistent.

## 6. How to deal with empty channels

In the first step, both channels are empty; later, there may be only correct answers or only wrong answers. Implementations must define:

1. Dedicated empty status token;
2. Or a padding token plus effective length;
3. The denominator of masked pooling is at least 1;
4. cross-attention returns a zero vector or a learnable empty vector when one side is empty.

A safe masked mean:

```python
def masked_mean(x, mask):
    weight = mask.unsqueeze(-1).to(x.dtype)
    total = (x * weight).sum(dim=1)
    denom = weight.sum(dim=1).clamp_min(1.0)
    return total / denom
```

!!! warning "padding leaks can create false patterns"

    If padding embedding, illegal questions, and empty channels are handled inconsistently, the network may learn data partitioning features from sequence length or padding values. It should be specifically tested that the Q value of the same real state does not change after adding padding.

## 7. How does the network remain adaptive at each step?

After students answered the questions, at least three changes occurred:

1. New questions enter the correct or incorrect answer channel;
2. Recalculation of attention weight and cross-channel contradiction;
3. Answered questions are removed from the legal action set.

So

\[
Q_\phi(s_{t+1},\cdot)
\neq
Q_\phi(s_t,\cdot)
\]

Generally true, the next question will branch based on the real-time answer. For the complete training and online process, see [Training and Real Student Deployment](05-training-and-deployment.md).
