#Distributed vocabulary presentation basis

## 1. From discrete index to embedding matrix

Let the vocabulary size be \(V\) and the embedding dimension be \(D\). Model maintenance input embedding matrix

\[
W_{\mathrm{in}}\in\mathbb R^{V\times D}.
\]

The one-hot vector of the word \(w_i\) is \(\mathbf e_i\). The table lookup operation can be written as matrix multiplication:

\[
\mathbf v_{w_i}
=W_{\mathrm{in}}^\top\mathbf e_i.
\]

Since \(\mathbf e_i\) only has a 1 in one position, this multiplication is equivalent to reading row \(i\) of \(W_{\mathrm{in}}\). Implemented without actually creating huge one-hot vectors.

## 2. What does "distributed" mean?

In one-hot representation, the identity of a word is concentrated at a single coordinate. Dense word vectors disperse information in \(D\) real-number dimensions:

\[
\mathbf v_w=(v_{w1},v_{w2},\ldots,v_{wD})^\top.
\]

The same coordinate will participate in the representation of many words, and the properties of the same word will also be encoded by multiple coordinates. This leads to parameter sharing: similar context imposes similar gradients on multiple words, thus forming a geometric structure between words.

Individual coordinates often do not have stable human labels. The overall direction, distance, and difference of vectors are more important than dimension-by-dimensional naming.

## 3. How distribution assumptions enter training

The basic intuition of distributional semantics is that words appearing in similar contexts tend to have related functions or meanings. Word2Vec does not build the complete co-occurrence matrix first, but continuously generates local prediction tasks from sliding windows.

given word sequence

\[
w_1,w_2,\ldots,w_T,
\]

When the window radius is \(c\), the context index set of location \(t\) is

\[
\mathcal C_t
=\{j:1\le j\le T,\ 0<|j-t|\le c\}.
\]

local co-occurrence pairs

\[
(w_t,w_j),\qquad j\in\mathcal C_t.
\]

CBOW combines multiple contexts at the same position into one center word prediction; Skip-gram treats each center-context combination as one prediction.

## 4. Static word vector

There is only one input vector per word type:

\[
w\mapsto \mathbf v_w.
\]

Therefore `bank` shares the same representation in "river bank" and "bank loan". The trained vectors will be a mixture of different word meanings, with more frequent meanings generally contributing more strongly.

This is different from contextualized representation. BERT-type models generate token representations based on complete sentences:

\[
(w,\text{context})\mapsto \mathbf h_{w,\text{context}}.
\]

Understanding this difference avoids interpreting 2013 static word vectors with the capabilities of modern language models.

## 5. Input representation and output representation

Predictive models involve at least two types of parameters:

1. Word vector \(W_{\mathrm{in}}\) on the input side;
2. The vector used by the output side to calculate the target probability.

If full softmax is used, the output matrix can be written as

\[
W_{\mathrm{out}}\in\mathbb R^{V\times D}.
\]

If hierarchical softmax is used, the output vector belongs to the internal node of the Huffman tree:

\[
U\in\mathbb R^{(V-1)\times D}.
\]

The vector \(\mathbf v_w\) of the input word \(w\) and the output node vector \(\mathbf u_n\) play different roles. After training is complete, the original Word2Vec tool usually exports the input matrix `syn0` as a word vector.

## 6. Similarity

The most commonly used word vector similarity is cosine similarity:

\[
\operatorname{cos}(\mathbf a,\mathbf b)
=\frac{\mathbf a^\top\mathbf b}
{\lVert\mathbf a\rVert_2\lVert\mathbf b\rVert_2}.
\]

Cosines compare directions, weakening the effect of differences in vector lengths. If normalized first

\[
\widetilde{\mathbf v}_w
=\frac{\mathbf v_w}{\lVert\mathbf v_w\rVert_2},
\]

Then the cosine similarity is the dot product of the normalized vectors.

## 7. Why local prediction can produce similar representations

Taking Skip-gram as an example, if `cat` and `dog` often predict similar context words, then their input vectors will repeatedly receive gradients with similar directions. In the end, the two have similar effects on the output decision boundary.

In CBOW, if `cat` and `dog` often become target words in similar contexts, the model will also adjust the context words and output path parameters to make these targets easier to predict from similar environments.

This is an operational explanation. The paper does not claim that a single vector is completely equivalent to the word meaning; the vector preserves the statistical structure shaped by the training target and the corpus distribution.

## 8. Matrix perspective

After training is completed, the entire vocabulary forms a matrix

\[
W_{\mathrm{in}}
=\begin{bmatrix}
\mathbf v_{w_1}^\top\\
\mathbf v_{w_2}^\top\\
\vdots\\
\mathbf v_{w_V}^\top
\end{bmatrix}.
\]

Its rank is at most \(D\), which is much smaller than the vocabulary dimension \(V\). The model uses low-dimensional continuous space to compress local co-occurrence rules. Subsequent theoretical studies further revealed connections between certain Word2Vec targets and weighted co-occurrence matrix factorization, but this belongs to a later explanatory framework.

## 9. Indicates what determines quality

Word vectors are not an object separate from the training process. It is affected by the following factors:

- Corpus field and scale;
- tokenization and vocabulary truncation;
- Context window width;
- Predicted direction of CBOW or Skip-gram;
- Output approximation method;
- vector dimensions;
- Word frequency and sampling strategy;
- Optimize the number of steps and learning rate;
-Use input vector, output vector or a combination of both.

The paper's experiments focus on the trade-offs between the first three sets of scale factors and model architecture.
