# SGD, backpropagation and complete algorithm

## 1. Composition of training system

To reproduce the hierarchical-softmax version of this article, the following objects are required:

1. Training token sequence;
2. Mapping of word frequency table and word to integer index;
3. Huffman binary tree;
4. Enter the word vector matrix \(W_{\mathrm{in}}\);
5. Internal node vector matrix \(U\);
6. Context window sampler;
7. SGD or parallel optimizer.

## 2. Preprocessing

### 2.1 vocabulary

Word frequency in statistical corpus:

\[
f(w)=\sum_{t=1}^{T}\mathbb I(w_t=w).
\]

The paper experiment limits vocabulary by the most common words: 30K vocabulary is used for small-scale comparisons, and up to 1M high-frequency words are used for large-scale Google News experiments. Tokens outside the vocabulary cannot participate in analogy evaluation.

### 2.2 Huffman tree

Initialize the weight of each word to \(f(w)\), and repeatedly merge the two nodes with the lowest current frequency until only the root node remains. Record each word:

- Root to leaf binary code;
- Index of internal nodes passed by the path;
- Path length \(L_w\).

### 2.3 Parameter initialization

The input vector can be initialized with a small range uniform distribution:

\[
W_{\mathrm{in},ij}
\sim\operatorname{Uniform}
\left(-\frac{1}{2D},\frac{1}{2D}\right).
\]

The public C implementation initializes `syn0` to this magnitude, initializing the hierarchical-softmax node vector `syn1` to 0. The text of the paper does not specify the initialization distribution in detail.

## 3. learning rate

Table 2 and Table 4 correspond to experimental use:

\[
\eta_0=0.025,
\]

And linearly decreases within 3 epochs, bringing it close to 0 at the end of training. If the proportion of processed training positions is \(\rho\in[0,1]\), it can be written as

\[
\eta(\rho)
=\eta_0(1-\rho).
\]

Implementations usually set very small lower bounds to avoid negative learning rates caused by floating point numbers and asynchronous counting.

The distributed DistBelief experiment uses mini-batch asynchronous gradient and AdaGrad, which belongs to another set of optimization configurations.

## 4. Hierarchical-softmax core update

The input representation is \(\mathbf h\), and the target word is \(o\). For each node \(n_r\) on its path:

1. Calculation

    \[
    p_r=\sigma(\mathbf u_{n_r}^\top\mathbf h);
    \]

2. Calculation error

    \[
    \delta_r=p_r-y_r;
    \]

3. Cumulative input gradient

    \[
    \mathbf g_h\mathrel{+}=\delta_r\mathbf u_{n_r};
    \]

4. Update node vector

    \[
    \mathbf u_{n_r}
    \leftarrow
    \mathbf u_{n_r}-\eta\delta_r\mathbf h.
    \]

After traversing the path, update the source parameter represented by the input with the accumulated \(\mathbf g_h\).

## 5. CBOW complete pseudocode

```text
for epoch in 1..E:
    for position t in corpus:
        context = valid words around t
        h = average(W_in[word] for word in context)
        target = w_t

        grad_h = 0
        for (node, branch_label) in huffman_path[target]:
            p = sigmoid(U[node] dot h)
            delta = p - branch_label
            grad_h += delta * U[node] # Use pre-update parameters
            U[node] -= learning_rate * delta * h

        for word in context:
            W_in[word] -= learning_rate * grad_h / len(context)
```

An implementation detail is: if the context word appears repeatedly, the gradient can be added multiple times according to the number of occurrences; if a unique index is used to write back in batches, the repeated positions need to be accumulated explicitly.

## 6. Skip-gram complete pseudo code

```text
for epoch in 1..E:
    for position t in corpus:
        radius = UniformInteger(1, C)
        center = w_t

        for j in positions within radius around t, j != t:
            target = w_j
            h = W_in[center]
            grad_h = 0

            for (node, branch_label) in huffman_path[target]:
                p = sigmoid(U[node] dot h)
                delta = p - branch_label
                grad_h += delta * U[node]
                U[node] -= learning_rate * delta * h

            W_in[center] -= learning_rate * grad_h
```

If you want to strictly match a certain historical public version, you should further check the actual direction of its center words and window words in `syn0` and the target path.

## 7. An updated shape check

|object|shape|
|---|---|
| \(W_{\mathrm{in}}\) | \(V\times D\) |
| \(U\) | \((V-1)\times D\) |
| \(\mathbf h\) | \(D\) |
| \(\mathbf u_n\) | \(D\) |
| \(p_r,delta_r\) |scalar|
| \(\mathbf g_h\) | \(D\) |

The dot product \(\mathbf u_n^\top\mathbf h\) outputs a scalar, and both the node gradient and the input gradient maintain \(D\) dimensions.

## 8. Complexity check

If the target word path length is \(L_o\), a hierarchical-softmax target update requires about \(L_o\) \(D\) dimensional dot product and vector updates:

\[
O(DL_o).
\]

\(L_o\approx\log_2V\) under the balanced tree, and the average path length weighted by token frequency should be used under the Huffman tree.

CBOW reads \(N\) additional context vectors; Skip-gram performs multiple target updates per center position. This is consistent with equations (4) and (5) in the paper.

## 9. Single-machine and distributed training

### 9.1 Stand-alone SGD

The parameters are updated every time a position is read. Data order and thread scheduling will affect the specific result. The multi-threaded public implementation uses approximately lock-free updates, allowing different threads to modify shared vectors simultaneously.

### 9.2 DistBelief

A parallel version of the paper contains:

- Multiple model replicas;
- parameter server;
- mini-batch asynchronous gradient;
- AdaGrad；
- 50–100 replicas.

Asynchronous updates introduce stale gradients but significantly improve throughput. The paper uses the final analogy accuracy to verify that the training is still effective.

## 10. Epoch, data volume and dimensions

Table 5 compares three methods of scaling up training volume:

- The same 783M corpus training for 3 epochs;
- 1.6B corpus training 1 epoch;
- 783M corpus, expanded vector dimension, training 1 epoch.

The author found that one epoch of looking at more different tokens can reach or exceed the result of three repetitions on a smaller corpus. This supports the design orientation of "expanding data coverage".

## 11. Numerical stability

Implementing sigmoid should avoid directly calculating the extreme \(e^{-x}\). Common practices include:

- Truncate logit;
- Use stable `logsigmoid`;
- Use lookup tables to approximate sigmoid;
- Use `softplus` expression for probability loss.

The original C code constructs `expTable` to accelerate the sigmoid and apply bounds processing to fractions outside the interval.

## 12. What to export after training is completed

The final vocabulary expression usually takes

\[
W_{\mathrm{in}}.
\]

\(U\) of hierarchical-softmax corresponds to the internal nodes of the tree, and there is no direct alignment of one line and one word. After exporting, each word vector is often normalized by \(L_2\) to quickly calculate cosine nearest neighbors and analogies.

## 13. Reproducibility records

At least: should be saved:

- Corpus version, cleaning and tokenization rules;
- Vocabulary size and truncation method;
- \(D\), maximum window \(C\), number of epochs;
- CBOW or Skip-gram;
- Tree construction and branch coding of hierarchical softmax;
- Initial learning rate and decay;
- Random seed;
- Number of threads and parallel update methods;
- OOV processing and exclusion rules in analogy evaluation.

These factors will change the final accuracy, and the historical hardware times in the paper cannot be directly used as a speed baseline for modern reproduction.
