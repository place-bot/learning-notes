# Huffman Hierarchical Softmax

## 1. Cost of large vocabulary softmax

Given the hidden representation \(\mathbf h\in\mathbb R^D\), full softmax computes the score for each word

\[
z_w=\mathbf u_w^\top\mathbf h,
\]

And normalize:

\[
P(w\mid\mathbf h)
=\frac{\exp(z_w)}
{\sum_{w'\in\mathcal V}\exp(z_{w'})}.
\]

The denominator needs to traverse \(V\) words, and each fraction contains a \(D\) dimensional dot product, so one prediction is about \(O(VD)\). With a vocabulary of millions, this will dominate the training costs.

## 2. Rewrite multi-classification into tree decision-making

Hierarchical softmax places each word at a binary leaf node. Predicting a word is equivalent to starting from the root node, selecting left or right in sequence, and finally reaching the word.

If the path of word \(w\) passes through internal nodes

\[
n_{w,1},n_{w,2},\ldots,n_{w,L_w},
\]

The corresponding branch label is

\[
y_{w,1},y_{w,2},\ldots,y_{w,L_w},
\qquad y_{w,j}\in\{0,1\},
\]

Then you only need to calculate \(L_w\) secondary classifications.

Each internal node \(n\) in the tree has an output vector

\[
\mathbf u_n\in\mathbb R^D.
\]

The probability of selecting label 1 at node \(n\) is defined as

\[
p_n(1\mid\mathbf h)
=\sigma(\mathbf u_n^\top\mathbf h),
\qquad
\sigma(x)=\frac{1}{1+e^{-x}}.
\]

The probability of selecting label 0 is \(1-p_n\).

## 3. Probability of a word

The conditional probability of the word \(w\) is the product of the branch probabilities along the entire path:

\[
P(w\mid\mathbf h)
=\prod_{j=1}^{L_w}
p_{n_{w,j}}^{\,y_{w,j}}
(1-p_{n_{w,j}})^{1-y_{w,j}}.
\]

Here each factor of the multiplication sign should be understood as

\[
p_{n_{w,j}}^{\,y_{w,j}}
(1-p_{n_{w,j}})^{1-y_{w,j}}
=
\begin{cases}
p_{n_{w,j}}, & y_{w,j}=1,\\
1-p_{n_{w,j}}, & y_{w,j}=0.
\end{cases}
\]

Since each leaf node corresponds to a unique root-to-leaf path, the sum of the probabilities of all leaf words is 1. The model still gives a normalized word distribution.

## 4. Why are Huffman trees faster?

The path length of a balanced binary tree is approximately

\[
\log_2V.
\]

Huffman coding builds a tree based on word frequency:

- High-frequency words get shorter codes;
- Low frequency words allow longer encoding;
- The average path length is close to the coding lower bound of this frequency distribution.

The training samples themselves also appear by word frequency, so high-frequency target words are visited frequently, and they happen to have short paths. The original article uses "about \(\log_2(\text{unigram perplexity})\)" to describe the average output number, and reports that millions of vocabulary can be about twice as fast as a balanced tree.

## 5. Loss of a single target word

For the target word \(w\), the negative log likelihood is

\[
\mathcal L(w,\mathbf h)
=-\log P(w\mid\mathbf h).
\]

Expansion gives binary cross-entropy along the path:

\[
\mathcal L(w,\mathbf h)
=-\sum_{j=1}^{L_w}
\left[
y_{w,j}\log p_j
+(1-y_{w,j})\log(1-p_j)
\right],
\]

Among them

\[
p_j=\sigma(\mathbf u_{n_{w,j}}^\top\mathbf h).
\]

Therefore, one-time word prediction only trains \(L_w\) binary classifiers on the target path.

## 6. Gradient

remember

\[
z_j=\mathbf u_{n_{w,j}}^\top\mathbf h.
\]

The derivative of logistic regression cross-entropy with respect to logit is

\[
\frac{\partial\mathcal L}{\partial z_j}
=p_j-y_{w,j}.
\]

Then the gradient of the internal node vector is

\[
\frac{\partial\mathcal L}
{\partial\mathbf u_{n_{w,j}}}
=(p_j-y_{w,j})\mathbf h,
\]

The gradient of the input representation is

\[
\frac{\partial\mathcal L}{\partial\mathbf h}
=\sum_{j=1}^{L_w}
(p_j-y_{w,j})\mathbf u_{n_{w,j}}.
\]

When the learning rate is \(\eta\), SGD is updated to

\[
\mathbf u_{n_{w,j}}
\leftarrow
\mathbf u_{n_{w,j}}
-\eta(p_j-y_{w,j})\mathbf h,
\]

\[
\mathbf h
\leftarrow
\mathbf h
-\eta\sum_j(p_j-y_{w,j})\mathbf u_{n_{w,j}}.
\]

In implementation, the node vector before update should be used to accumulate \(\partial\mathcal L/\partial\mathbf h\), and then the input vector should be written back to avoid sequential updates changing the gradient of the same sample.

## 7. Numerical example of three-layer path

Let the path label of a word be

\[
(y_1,y_2,y_3)=(1,0,1),
\]

model gets

\[
(p_1,p_2,p_3)=(0.8,0.3,0.6).
\]

The target word probability is

\[
P(w\mid\mathbf h)
=0.8\times(1-0.3)\times0.6
=0.336.
\]

The loss is

\[
\mathcal L=-\log(0.336)\approx1.0906.
\]

The three logit gradients are

\[
(p_1-y_1,p_2-y_2,p_3-y_3)
=(-0.2,0.3,-0.4).
\]

The first and third nodes need to increase the probability of label 1, and the second node needs to decrease the probability of label 1.

## 8. Parameter scale

A full binary tree with \(V\) leaf nodes has \(V-1\) internal nodes. The output parameters are approximately

\[
(V-1)D,
\]

Same order as \(VD\) for full softmax. Hierarchical softmax mainly saves the number of output vectors involved in the calculation of each sample, rather than significantly reducing the total parameters.

## 9. Boundary with negative sampling

The experiments in this article mainly use Huffman hierarchical softmax. Negative Sampling was proposed in the follow-up paper **Distributed Representations of Words and Phrases and their Compositionality** in the same year. It uses a real word and several noise words to construct a two-category target.

The differences between the two include:

|Dimensions| Hierarchical softmax | Negative sampling |
|---|---|---|
|output structure|Huffman tree internal nodes|Output word vector in vocabulary|
|cost per sample|target path length|\(1+k\) positive and negative samples|
|Whether to form a standardized whole-word distribution|Yes|The training target itself does not directly give the complete normalized distribution|
|position in this article|Core output mechanism|Not proposed yet|

The later public `word2vec.c` supports both `-hs` and `-negative`, and its functional scope has exceeded the original experiment of this article.

## 10. Key to reading hierarchical softmax

It completes three substitutions:

1. \(V\) class softmax is replaced by tree path;
2. A huge normalization is replaced by several sigmoid;
3. Each update step \(V\) output vectors are replaced by updating internal nodes on the target path.

The difference between CBOW and Skip-gram determines where \(\mathbf h\) comes from; hierarchical softmax is responsible for converting this \(\mathbf h\) into target word probability.
