# Public code and minimal implementation

## 1. Code Identity

Paper v3's Follow-Up Work points to a multi-threaded C implementation on Google Code. item is now saved in [Google Code Archive](https://code.google.com/archive/p/word2vec/). Core files include:

|File|Function|
|---|---|
| `word2vec.c` |Vocabulary, Huffman tree, CBOW, Skip-gram, HS, negative sampling and multi-thread training|
| `compute-accuracy.c` |Semantic-syntactic analogy accuracy|
| `distance.c` |nearest neighbor query|
| `word-analogy.c` |interactive word analogy|
| `word2phrase.c` |phrase discovery|
| `questions-words.txt` |19,544 analogy questions and 14 category headings|

The archived code has absorbed functionality from subsequent work in the same year. When reading the code, you need to distinguish between the "original method of this article" and the "subsequent Word2Vec tool".

## 2. Core parameter array

Expose C code using:

|C name|mathematical meaning|shape|
|---|---|---|
| `syn0` |Input word vector \(W_{\mathrm{in}}\)| \(V\times D\) |
| `syn1` |hierarchical-softmax internal node vector \(U\)|About \((V-1)\times D\)|
| `syn1neg` |negative-sampling output word vector| \(V\times D\) |
| `neu1` |CBOW aggregate representation \(\mathbf h\)| \(D\) |
| `neu1e` |Returns the cumulative error on the input side| \(D\) |
| `expTable` |sigmoid lookup table|fixed length|

The original hierarchical-softmax reproduction of this article only requires `syn0` and `syn1`.

## 3. Huffman tree implementation

The main steps of `CreateBinaryTree()` are:

1. Sort words by frequency;
2. Maintain unmerged word nodes and new internal nodes;
3. Take two minimum count nodes and merge them each time;
4. Save the parent node and binary branch;
5. Generate root-to-leaf code and internal node paths for each word.

The core invariants are:

\[
\operatorname{count}(\text{parent})
=\operatorname{count}(\text{left})
+\operatorname{count}(\text{right}).
\]

High-frequency words are merged later in the tree-building process and are therefore closer to the root.

## 4. Branch labels in code

The hierarchical-softmax update uses an approximate form:

```c
g = (1 - code[d] - sigmoid(f)) * alpha;
```

This code defines the expected sigmoid output as

\[
y=1-\operatorname{code}[d].
\]

If code is 0, \(y=1\) is expected; if code is 1, \(y=0\) is expected. This is just a coding convention for the left and right branches. The corresponding gradient ascent is updated as

\[
\eta(y-p),
\]

Exactly the same as \(-\eta(p-y)\) when cross-entropy is minimized.

## 5. Actual code for dynamic windows

Code sampling first

```c
b = next_random % window;
```

Then only the positions from `b` to `2*window-b` are traversed. The effective radius is

\[
R=\text{window}-b.
\]

because

\[
b\in\{0,1,\ldots,C-1\},
\]

So

\[
R\in\{1,2,\ldots,C\}
\]

Evenly distributed, consistent with the paper description.

## 6. CBOW code path

CBOW branch execution:

1. Accumulate the `syn0` vector in the window to `neu1`;
2. Divide by the number of valid contexts `cw`;
3. Calculate sigmoid for the Huffman path of the target word;
4. Accumulate the path error into `neu1e`;
5. Update `syn1`;
6. Add `neu1e` back to `syn0` for each context.

This verifies the implementation of the text's "average context vector".

## 7. Skip-gram code path

Skip-gram branch for each `last_word` in the window:

1. Read `syn0` of the word;
2. Calculate the loss along the Huffman path of the current `word`;
3. Update `syn1`;
4. Write the error back to `syn0` of `last_word`.

The direction of the variables is opposite to what is stated in Figure 1 of the paper: the code block ostensibly predicts the current word with the window word. The sliding window will produce a large number of bidirectional adjacent relationships in the corpus, but the target direction will still be different on a sample-by-sample basis. When it is necessary to accurately reproduce the experiment, the source code version used should be fixed and executed according to the code; when explaining the architecture, the central words defined in the paper are usually used to predict nearby words.

## 8. Why the public code cannot directly represent this article

The default parameters for archive versions include:

```text
negative = 5
hs = 0
sample > 0
```

and contains `word2phrase.c`. These functions correspond to those in subsequent papers in the same year:

- negative sampling；
- Downsampling of high-frequency words;
- Phrase learning.

If the goal is to follow the training mechanism of this article, the command configuration should be explicitly used:

```bash
./word2vec \
  -train corpus.txt \
  -output vectors.bin \
  -cbow 1 \
  -size 300 \
  -window 4 \
  -hs 1 \
  -negative 0 \
  -sample 0 \
  -iter 3 \
  -binary 1
```

Skip-gram changes `-cbow 1` to `-cbow 0`, and the maximum window of the main experiment of the paper is 10. The specific threads, word frequency thresholds and corpus processing in the command still need to be recorded separately.

## 9. Minimal Python data structure

```python
from dataclasses import dataclass
import numpy as np

@dataclass
class HuffmanPath:
    nodes: np.ndarray   # [path_length]
    labels: np.ndarray  # 0/1, [path_length]

class Word2VecHS:
    def __init__(self, vocab_size, dim, paths, seed=0):
        rng = np.random.default_rng(seed)
        self.w_in = rng.uniform(
            -0.5 / dim,
            0.5 / dim,
            size=(vocab_size, dim),
        )
        self.u_node = np.zeros((vocab_size - 1, dim))
        self.paths = paths
```

The tree has \(V-1\) internal nodes, so the first dimension of `u_node` is `vocab_size - 1`.

## 10. Stable sigmoid and path update

```python
def sigmoid(x):
    if x >= 0:
        z = np.exp(-x)
        return 1.0 / (1.0 + z)
    z = np.exp(x)
    return z / (1.0 + z)

def hs_update(h, path, u_node, learning_rate):
    grad_h = np.zeros_like(h)

    for node, label in zip(path.nodes, path.labels):
        u_old = u_node[node].copy()
        p = sigmoid(np.dot(u_old, h))
        delta = p - label

        grad_h += delta * u_old
        u_node[node] -= learning_rate * delta * h

    return grad_h
```

Copying `u_old` ensures that the input gradient uses the node parameters before updating.

## 11. CBOW single step

```python
def cbow_step(model, context_ids, target_id, learning_rate):
    context_ids = np.asarray(context_ids, dtype=np.int64)
    h = model.w_in[context_ids].mean(axis=0)

    grad_h = hs_update(
        h,
        model.paths[target_id],
        model.u_node,
        learning_rate,
    )

    grad_each = grad_h / len(context_ids)
    np.add.at(model.w_in, context_ids, -learning_rate * grad_each)
```

`np.add.at` can correctly handle indexing of repeated words in context.

## 12. Skip-gram single step

```python
def skipgram_step(model, center_id, target_ids, learning_rate):
    for target_id in target_ids:
        h = model.w_in[center_id].copy()
        grad_h = hs_update(
            h,
            model.paths[target_id],
            model.u_node,
            learning_rate,
        )
        model.w_in[center_id] -= learning_rate * grad_h
```

Each context target completes an independent path update.

## 13. Implementation of analogy evaluation

```python
def analogy(vectors, a, b, c):
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    unit = vectors / np.maximum(norms, 1e-12)
    query = unit[b] - unit[a] + unit[c]
    scores = unit @ query
    scores[[a, b, c]] = -np.inf
    return int(np.argmax(scores))
```

Blocked matrix multiplication or approximate nearest neighbor indexing can be used on large vocabulary to avoid saving all candidate scores at once.

## 14. Unit check

Implementations should pass the following checks:

- Each word path finally reaches a unique leaf node;
- Huffman The average path of high-frequency words is shorter;
- Target path loss decreases after single HS sample update;
- CBOW context replacement does not change the forward result;
- The actual window radius of Skip-gram is between \(1\) and \(C\);
- Both the input matrix and the node matrix get non-zero gradients;
- Analogy search excludes three input words;
- OOV questions are counted in coverage and not in the calculable accuracy denominator.

## 15. Paper-level and tool-level reproduction

It is recommended to maintain two sets of configurations:

|Configuration|purpose|Key options|
|---|---|---|
| paper-HS |Understand this article|CBOW/SG + Huffman HS, no negative sampling|
| later-word2vec |Use mature tools and techniques|Negative sampling, downsampling, phrases, etc.|

Only by separating the two sets of configurations can we accurately determine whether the performance comes from the original architecture or subsequent improvements.
