# Symbol table, conclusion and reading map

## 1. Symbol table

|symbol|meaning|
|---|---|
| \(\mathcal V\) |vocabulary|
| \(V\) |Vocabulary size|
| \(D\) |word vector dimensions|
| \(T\) |Number of tokens in the training corpus|
| \(E\) |number of epochs|
| \(Q\) |Approximate computational effort for a single training position|
| \(N\) |Number of context words used by CBOW/NNLM|
| \(C\) |Skip-gram maximum window distance|
| \(R\) |Randomly sampled actual window radius|
| \(H\) |NNLM / RNNLM hidden layer dimensions|
| \(w_t\) |Word with sequence position \(t\)|
| \(\mathbf e_w\) |One-hot vector of word \(w\)|
| \(\mathbf v_w\) |Input vector for word \(w\)|
| \(W_{\mathrm{in}}\) |Input word vector matrix|
| \(\mathbf h\) |The representation fed into the output layer|
| \(\mathbf u_n\) |Output vector of Huffman internal node \(n\)|
| \(U\) |All internal node vector matrices|
| \(L_w\) |Huffman path length for word \(w\)|
| \(n_{w,j}\) |The \(j\) internal node on the path \(w\)|
| \(y_{w,j}\) |Target label of the \(j\) second category|
| \(p_j\) |Predicted probability of path branch \(j\)|
| \(\eta\) |learning rate|
| \(\sigma\) |sigmoid function|

## 2. Complexity of the four models

Total training complexity:

\[
O=E\times T\times Q.
\]

Feedforward NNLM:

\[
Q=ND+NDH+HV.
\]

RNNLM：

\[
Q=H^2+HV.
\]

CBOW + hierarchical softmax：

\[
Q=ND+D\log_2V.
\]

Skip-gram + hierarchical softmax：

\[
Q=C(D+D\log_2V).
\]

## 3. Two core goals

CBOW：

\[
\max_\Theta
\sum_{t=1}^{T}
\log P(w_t\mid\mathcal C_t).
\]

Skip-gram：

\[
\max_\Theta
\sum_{t=1}^{T}
\sum_{\substack{-c\le j\le c\\j\neq0}}
\log P(w_{t+j}\mid w_t).
\]

## 4. Hierarchical-softmax probability

\[
P(w\mid\mathbf h)
=\prod_{j=1}^{L_w}
p_j^{y_{w,j}}(1-p_j)^{1-y_{w,j}},
\]

\[
p_j
=\sigma(\mathbf u_{n_{w,j}}^\top\mathbf h).
\]

Single path node error:

\[
\delta_j=p_j-y_{w,j}.
\]

The input represents the gradient:

\[
\frac{\partial\mathcal L}{\partial\mathbf h}
=\sum_j\delta_j\mathbf u_{n_{w,j}}.
\]

Node vector gradient:

\[
\frac{\partial\mathcal L}{\partial\mathbf u_{n_{w,j}}}
=\delta_j\mathbf h.
\]

## 5. The shortest difference between CBOW and Skip-gram

```text
CBOW
Context word vector ──average──► h ──HS──► center word

Skip-gram
Center word vector ─────────► h ──HS──► each nearby word
```

CBOW aggregates each center position once; Skip-gram expands the center position into multiple prediction pairs.

## 6. Analogical evaluation

given

\[
a:b::c:d,
\]

Query:

\[
\mathbf q
=\mathbf v_b-\mathbf v_a+\mathbf v_c.
\]

Output:

\[
\widehat d
=\arg\max_{w\notin\{a,b,c\}}
\operatorname{cos}(\mathbf v_w,\mathbf q).
\]

The public data contains 19,544 questions: 8,869 semantic analogies and 10,675 syntactic analogies.

## 7. Core experimental facts of the paper

1. Table 2: When more data and higher dimensions are added together, the accuracy is highest.
2. Table 3: After fixing 320M data and 640 dimensions, Skip-gram has the highest semantic accuracy and CBOW has the highest syntactic accuracy.
3. Table 4: 300-dimensional Skip-gram achieves 53.3% on comprehensive analogy.
4. Table 5: Looking at 1.6B new tokens in one epoch, it can reach or exceed three epochs repeated on 783M tokens.
5. Table 6: 6B data, 1,000-dimensional Skip-gram reaches 65.6%, about 2.5 days × 125 CPU cores.
6. Table 7: Skip-gram alone reaches 48.0% sentence completion, and combined with RNNLM reaches 58.9%.

## 8. Level of contribution to the paper

### Model layer

Two log-linear architectures, CBOW and Continuous Skip-gram, are proposed.

### Computing layer

Remove expensive hidden layers with Huffman hierarchical softmax and distributed training.

### Data layer

Expand training to billions of tokens, million-level vocabulary, and thousands of dimensional representations.

### Evaluation layer

Building a semantic-syntactic analogy test to quantify linear relationships using vector difference and top-1 retrieval.

### Application layer

We demonstrate that word vector scoring can complement RNNLM and discuss applications such as retrieval, translation, question answering, and knowledge bases.

## 9. Three common confusions

### 9.1 Word2Vec and a single model

Word2Vec usually refers to a set of architectures and tools for training word vectors, including at least two directions: CBOW and Skip-gram.

### 9.2 This article and negative sampling

The output mechanism of this article is mainly hierarchical softmax. Negative Sampling, frequent word down-sampling and phrase learning were proposed by the follow-up NIPS paper system in the same year.

### 9.3 Analogy and complete language understanding

Vector analogy measures stable linear relationships. Complete language understanding also requires context disambiguation, word order, combination, factual and reasoning skills.

## 10. Inspiration for modern NLP

The thoughts left behind by this paper include:

- Learning transferable representations with self-supervised local prediction;
- Map sparse symbols to continuous space through parameter sharing;
- Make single-step training cheap enough, and then expand the data and dimensions;
- Handle huge class spaces with approximate output targets;
- Use probing tasks to analyze the structure retained in the representation;
- Export and reuse pretraining representations for downstream tasks.

Modern pretraining language models expand the context, model depth, and training goals, but these basic design principles remain clearly visible.

## 11. Final conclusion

The most important result of the paper can be written as a calculation budget chain:

\[
\text{Remove expensive hidden layers}
\Longrightarrow
Q\downarrow
\Longrightarrow
T,D,V\uparrow
\Longrightarrow
\text{Improved word vector relationship quality}.
\]

The impact of CBOW and Skip-gram comes from this complete link. The simplicity of the architecture, training scale, and evaluation methods together constitute a historical breakthrough for Word2Vec.

## 12. Follow-up reading map

It is recommended to continue by the question:

|question|Directions for follow-up papers|
|---|---|
|How to further reduce output training costs?| SGNS、NCE |
|How to explain the relationship between Word2Vec and co-occurrence matrix?|SGNS implicit matrix factorization|
|How to use global co-occurrence statistics?| GloVe |
|How to add characters and shapes?| fastText |
|How to deal with polysemy?|Multi-prototype embedding, ELMo|
|How to learn deep bidirectional context?| BERT |
|How to unify the understanding of large-scale self-supervised representation?|Transformer language model|

For reference entry, see [References and Materials](references.md).
