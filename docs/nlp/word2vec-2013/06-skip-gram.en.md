# Skip-gram: Predict context from center word

## 1. Task direction

Skip-gram takes the center word \(w_t\) as input and predicts each nearby word:

\[
P(w_{t+j}\mid w_t),
\qquad -c\le j\le c,\quad j\neq0.
\]

It expands a central location into multiple training pairs:

\[
(w_t,w_{t-c}),\ldots,(w_t,w_{t-1}),
(w_t,w_{t+1}),\ldots,(w_t,w_{t+c}).
\]

## 2. Corpus target

When the window radius is fixed \(c\), the common writing method is

\[
\max_\Theta
\sum_{t=1}^{T}
\sum_{\substack{-c\le j\le c\\j\neq0}}
\log P(w_{t+j}\mid w_t).
\]

When using hierarchical softmax, the input representation is the center word vector:

\[
\mathbf h_t=\mathbf v_{w_t}.
\]

The probability of each context target \(o=w_{t+j}\) is

\[
P(o\mid w_t)
=\prod_{r=1}^{L_o}
p_r^{y_r}(1-p_r)^{1-y_r},
\]

\[
p_r
=\sigma(\mathbf u_{n_{o,r}}^\top\mathbf v_{w_t}).
\]

## 3. Gradient of a single center-context pair

For the training pair \((i,o)\), where \(i\) is the input center word and \(o\) is the output context word:

\[
\mathcal L(i,o)
=-\sum_{r=1}^{L_o}
\left[y_r\log p_r+(1-y_r)\log(1-p_r)\right].
\]

The gradient of the input center word vector is

\[
\frac{\partial\mathcal L(i,o)}{\partial\mathbf v_i}
=\sum_{r=1}^{L_o}
(p_r-y_r)\mathbf u_{n_{o,r}}.
\]

The gradient of the output path node is

\[
\frac{\partial\mathcal L(i,o)}
{\partial\mathbf u_{n_{o,r}}}
=(p_r-y_r)\mathbf v_i.
\]

A central word will be cumulatively updated for multiple context targets, and its total gradient is the sum of the gradients of each training pair.

## 4. Dynamic window

The paper sets the maximum distance to \(C\). For each central word, randomly select

\[
R\sim\operatorname{Uniform}\{1,2,\ldots,C\},
\]

Then use \(R\) words on the left and right.

A word whose distance from the center is \(d\) is included in the window if and only if \(R\ge d\). Therefore

\[
P(\text{inclusion distance}d)
=P(R\ge d)
=\frac{C-d+1}{C}.
\]

Nearby words appear more frequently. For example \(C=5\):

|Distance \(d\)|inclusion probability|
|---:|---:|
| 1 | \(1\) |
| 2 | \(4/5\) |
| 3 | \(3/5\) |
| 4 | \(2/5\) |
| 5 | \(1/5\) |

The expected number of predictions for each center word is

\[
2\mathbb E[R]
=2\cdot\frac{C+1}{2}
=C+1.
\]

The complexity of the paper is represented by \(C\), which ignores the constant difference.

## 5. Why are large windows more semantic?

Closer contexts often contain local syntactic constraints, such as determiners, tenses, and word forms; distant contexts are more likely to reflect topics and semantic fields. Expanding the window will increase the number of distant co-occurring signals and also mix in more noise.

The paper reports that as the scope expands, the quality of vectors increases, but the amount of calculation increases simultaneously. The experiment uses \(C=10\). This conclusion relies on its analogy test and news corpus, and cannot directly infer that large windows should be selected for all tasks.

## 6. Structural comparison between CBOW and Skip-gram

|Dimensions| CBOW | Skip-gram |
|---|---|---|
|input|multiple context words|a central word|
|aggregation|sum or average|Context-free aggregation|
|output|a central word|multiple nearby words|
|Single center position training items|about 1|About \(C+1\)|
|Original text complexity| \(ND+D\log_2V\) | \(C(D+D\log_2V)\) |
|Table 3 Advantages|syntax|Semantics|

Both use the same corpus window, but have different prediction directions and sample decomposition methods.

## 7. Complete update of a central word

Assume that the actual window of the center word `bank` contains four targets:

\[
\{\text{river},\text{near},\text{loan},\text{approved}\}.
\]

Skip-gram forms four losses:

\[
\mathcal L_t
=\mathcal L(\text{bank},\text{river})
+\mathcal L(\text{bank},\text{near})
+\mathcal L(\text{bank},\text{loan})
+\mathcal L(\text{bank},\text{approved}).
\]

The single input vector of `bank` receives four gradients. Different contexts of polysemous words are thus pressed into the same static vector, resulting in a hybrid representation.

## 8. Complexity

Thesis formula (5) is

\[
Q_{\mathrm{SG}}
=C\left(D+D\log_2V\right).
\]

Among them:

- Each prediction needs to access the input vector, recorded as \(D\);
- Huffman path takes about \(D\log_2V\);
- A center position produces predictions proportional to the window width.

Skip-gram is slower than CBOW, but gets an independent training signal for each word-context pair. In Table 5 of the paper, CBOW with 300 dimensions, 783M words, and 3 epochs takes about 1 day, and Skip-gram takes about 3 days.

## 9. Training direction and representation direction

Model training \(P(\text{context}\mid\text{center})\). The final use is the center word input vector \(\mathbf v_w\). The vector of a word should give its common context a high probability on its respective Huffman path.

The variable naming and loop direction in the exposed C code can easily confuse the reader: the code uses `syn0` for `last_word` within the window, and updates along the output path of the current `word`. Since the sliding corpus will repeatedly generate adjacent word pairs, the whole still learns the two-way co-occurrence structure; the actual input-output direction of the code should be used for accurate reproduction, and the theoretical explanation is based on the definition of "center word predicting surrounding words" in Figure 1 of the paper.

## 10. Skip-gram’s information flow

```text
central word index
   │ Check W_in
   ▼
Center word vector v_i
   │ Repeat for each sampled context target
   ▼
Target word Huffman path
   │ Multiple sigmoid
   ▼
path cross-entropy
   │
   ├── Update target path node vector
   └── Update the center word input vector
```

This structure transforms the sequence learning problem into a local prediction problem with a large number of shared parameters.
