# CBOW: Predict the center word from context

## 1. Task definition

given word sequence

\[
w_1,w_2,\ldots,w_T,
\]

CBOW collects context on both sides of the center word at position \(t\):

\[
\mathcal C_t
=\{w_{t-c},\ldots,w_{t-1},w_{t+1},\ldots,w_{t+c}\}.
\]

The training task is to predict \(w_t\) based on \(\mathcal C_t\):

\[
P(w_t\mid\mathcal C_t).
\]

The original paper reports that its optimal setting uses 4 historical words and 4 future words, which is a maximum of 8 context words.

## 2. The meaning of Continuous Bag-of-Words

"Bag-of-Words" means that the context order is ignored when aggregating; "Continuous" means that the learned continuous vectors are aggregated.

Let the actual number of valid context words be \(m_t\), and the input embedding be \(\mathbf v_w\in\mathbb R^D\). The projected representation can be written as average:

\[
\mathbf h_t
=\frac{1}{m_t}
\sum_{w\in\mathcal C_t}\mathbf v_w.
\]

The paper figure is marked `SUM`, and the text explains that the vectors are averaged. The only difference between the two is a scaling related to the context length; the public implementation uses averaging.

## 3. Prediction probability

With hierarchical softmax:

\[
P(w_t\mid\mathcal C_t)
=P(w_t\mid\mathbf h_t)
=\prod_{j=1}^{L_{w_t}}
p_j^{y_j}(1-p_j)^{1-y_j},
\]

Among them

\[
p_j
=\sigma(\mathbf u_{n_j}^\top\mathbf h_t).
\]

The maximum likelihood objective of the entire corpus can be written as

\[
\max_\Theta
\sum_{t=1}^{T}
\log P(w_t\mid\mathcal C_t),
\]

Among them, \(\Theta\) contains input word vectors and Huffman internal node vectors.

The paper does not fully list the objectives in this form; it is directly expanded from the model description and hierarchical softmax.

## 4. Single sample loss

For location \(t\):

\[
\mathcal L_t
=-\sum_{j=1}^{L_{w_t}}
\left[
y_j\log p_j+(1-y_j)\log(1-p_j)
\right].
\]

The gradient of the projection representation is

\[
\mathbf g_h
=\frac{\partial\mathcal L_t}{\partial\mathbf h_t}
=\sum_{j=1}^{L_{w_t}}
(p_j-y_j)\mathbf u_{n_j}.
\]

Since \(\mathbf h_t\) is the average of context vectors, each context word receives

\[
\frac{\partial\mathcal L_t}{\partial\mathbf v_w}
=\frac{1}{m_t}\mathbf g_h,
\qquad w\in\mathcal C_t.
\]

Context words in the same sample therefore share error signals in the same direction.

## 5. Step-by-step numerical example

Assume that the context has only two words, and its two-dimensional vector is

\[
\mathbf v_a=(0.2,0.6)^\top,
\qquad
\mathbf v_b=(0.4,0.2)^\top.
\]

CBOW is projected as

\[
\mathbf h
=\frac{\mathbf v_a+\mathbf v_b}{2}
=(0.3,0.4)^\top.
\]

The Huffman path of the target word passes through two nodes:

\[
\mathbf u_1=(1,-0.5)^\top,
\qquad y_1=1,
\]

\[
\mathbf u_2=(-0.2,0.8)^\top,
\qquad y_2=0.
\]

The two logits are

\[
z_1=\mathbf u_1^\top\mathbf h=0.1,
\qquad
z_2=\mathbf u_2^\top\mathbf h=0.26.
\]

The corresponding probability is approximately

\[
p_1=\sigma(0.1)\approx0.5250,
\qquad
p_2=\sigma(0.26)\approx0.5646.
\]

The target path probability is

\[
P(w\mid\mathcal C)
=p_1(1-p_2)
\approx0.2286.
\]

The loss is

\[
\mathcal L
=-\log(0.2286)
\approx1.476.
\]

The projected gradient is

\[
\begin{aligned}
\mathbf g_h
&=(p_1-1)\mathbf u_1+(p_2-0)\mathbf u_2\\
&\approx(-0.588,0.689)^{\top}.
\end{aligned}
\]

The two context words each receive half:

\[
\frac{\partial\mathcal L}{\partial\mathbf v_a}
=\frac{\partial\mathcal L}{\partial\mathbf v_b}
\approx(-0.294,0.345)^{\top}.
\]

Gradient descent will move both context vectors in the direction of reducing the target path loss.

## 6. Why is it fast?

The complexity given in the paper is

\[
Q_{\mathrm{CBOW}}
=ND+D\log_2V.
\]

- \(ND\): Read and aggregate context vectors;
- \(D\log_2V\): Compute and update Huffman path.

The model does not project to the \(NDH\) calculation of the nonlinear hidden layer.

## 7. What to learn from CBOW

A training sample requires that the context combination be able to distinguish the center word. Frequently occurring local collocations will be updated repeatedly:

- Input vector of context words;
- Internal node vector of the Huffman path for the target word.

Since multiple context words are averaged, CBOW tends to form a smooth and stable context representation. In Table 3 of the paper, CBOW's syntactic accuracy is 64%, higher than Skip-gram's 59%; its semantic accuracy is 24%, lower than Skip-gram's 55%. This is the result under a specific set of corpus, dimensions and training settings.

## 8. Loss of sequential information

If two contexts contain the same bag of words, then

\[
\operatorname{CBOW}(a,b,c)
=\operatorname{CBOW}(c,b,a).
\]

The model cannot distinguish the arrangement of contextual words, nor can it set independent transformations for different positions. It can still learn syntax-related rules through the co-occurrence distribution of words, but without explicit sequential encoding.

## 9. Boundary positions and repeated words

The effective context at the beginning and end of the sentence is less than \(2c\), and the average should be calculated based on the actual number of words \(m_t\). If the same word appears twice in the window, it contributes twice to the summation and receives two gradient contributions.

## 10. Complete data flow of CBOW

```text
contextual word index
   │ Check W_in
   ▼
Multiple D-dimensional vectors
   │ Average
   ▼
h_t
   │ Along the target word Huffman path
   ▼
Several sigmoid and path loss
   │ backpropagation
   ├── Update the internal node vector of the path
   └── Evenly distribute the aggregate gradient to the context input vector
```

When deployed, only the trained input word vectors are usually retained; CBOW's center word predictor is mainly a training tool for generating representations.
