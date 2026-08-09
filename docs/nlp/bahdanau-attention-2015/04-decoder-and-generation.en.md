# Stepwise decoding and conditional generation

## 1. What does the decoder accomplish at each step?

The decoding process of the target position \(i\) includes:

1. Query source comments based on the previous status \(\mathbf s_{i-1}\);
2. Get the weight \(\alpha_{ij}\) and context \(\mathbf c_i\);
3. Combine the previous target word \(y_{i-1}\) to update the decoding status;
4. Calculate vocabulary distribution;
5. Read the real \(y_i\) during training, and select a generated word during inference.

## 2. Target conditional probability

The paper writes the probability of the \(i\) word as:

\[
p(y_i\mid y_1,\ldots,y_{i-1},\mathbf x)
=
g(y_{i-1},\mathbf s_i,\mathbf c_i).
\tag{1}
\]

The decoding status is:

\[
\mathbf s_i
=
f
(\mathbf s_{i-1},y_{i-1},\mathbf c_i).
\tag{2}
\]

Here \(\mathbf c_i\) changes at every step.

## 3. Decoding order

Attention scoring uses \(\mathbf s_{i-1}\):

\[
e_{ij}
=
a(\mathbf s_{i-1},\mathbf h_j).
\tag{3}
\]

So a clear chronology is:

```text
s(i-1)
   │
   ├── Score with all hj
   ▼
αi1, ..., αiTx
   │
   ▼
ci
   │
   ├── Updated together with y(i-1), s(i-1)
   ▼
si
   │
   ▼
p(yi | y<i, x)
```

## 4. Target word embedding

When the target word \(y_{i-1}\) is expressed as one-hot:

\[
\mathbf e(y_{i-1})
=
\mathbf E_y y_{i-1}.
\tag{4}
\]

The target word embedding dimension of the paper experiment is:

\[
m=620.
\]

The source and target are in different languages and use different vocabulary and embedding matrices.

## 5. Context enters three gated channels

The decoding gated unit in the appendix of the paper is:

\[
\widetilde{\mathbf s}_i
=
\tanh
\left(
W\mathbf e(y_{i-1})
+
U[\mathbf r_i\odot\mathbf s_{i-1}]
+
C\mathbf c_i
\right),
\tag{5}
\]

\[
\mathbf z_i
=
\sigma
\left(
W_z\mathbf e(y_{i-1})
+
U_z\mathbf s_{i-1}
+
C_z\mathbf c_i
\right),
\tag{6}
\]

\[
\mathbf r_i
=
\sigma
\left(
W_r\mathbf e(y_{i-1})
+
U_r\mathbf s_{i-1}
+
C_r\mathbf c_i
\right),
\tag{7}
\]

\[
\mathbf s_i
=
(1-\mathbf z_i)\odot\mathbf s_{i-1}
+
\mathbf z_i\odot\widetilde{\mathbf s}_i.
\tag{8}
\]

The context is affected by \(C\), \(C_z\), and \(C_r\) respectively:

- Candidate status content;
- How many statuses to update;
- How much history is reset.

## 6. Shape check

Thesis experiments use:

\[
\mathbf e(y_{i-1})\in\mathbb R^{620},
\quad
\mathbf s_{i-1}\in\mathbb R^{1000},
\quad
\mathbf c_i\in\mathbb R^{2000}.
\]

So:

|parameters|shape|
|---|---|
| \(W,W_z,W_r\) | \(1000\times620\) |
| \(U,U_z,U_r\) | \(1000\times1000\) |
| \(C,C_z,C_r\) | \(1000\times2000\) |
| \(\mathbf z_i,\mathbf r_i,\widetilde{\mathbf s}_i,\mathbf s_i\) | \(1000\) |

Each term is mapped to 1000 dimensions before being added.

## 7. Initial decoding status

The appendix defines the initial state as:

\[
\mathbf s_0
=
\tanh
\left(
W_s\overleftarrow{\mathbf h}_1
\right).
\tag{9}
\]

The end of the reverse encoder clause is read toward the beginning of the sentence, so \(\overleftarrow{\mathbf h}_1\) has read the entire sentence. It provides the decoder with an initial global overview.

After each step, position-related information is obtained through attention.

## 8. Ending character

The target sequence contains the terminator `<eos>`. The generation process stops when the model outputs this symbol.

The training goals include predicting end characters:

\[
p(y_{T_y}=\texttt{<eos>}
\mid
y_{<T_y},\mathbf x).
\]

The terminator enables target sentences of different lengths to be represented by the same autoregressive model.

## 9. Training phase

During training, step \(i\) usually reads the real preceding words:

\[
\mathbf e(y_{i-1}^{\text{gold}}).
\]

The current word loss is:

\[
\ell_i
=
-\log
p_\theta
\left(
y_i^{\text{gold}}
\mid
y_{<i}^{\text{gold}},
\mathbf x
\right).
\tag{10}
\]

The loss of the whole sentence is the sum of all valid positions.

## 10. Reasoning stage

During inference, the model starts from the start symbol:

\[
y_0=\texttt{<bos>}.
\]

Then recurse:

\[
\widehat y_i
\sim
p_\theta
(y_i\mid\widehat y_{<i},\mathbf x)
\]

Or use beam search to retain multiple high-probability prefixes.

The predicted word affects the next step:

- Target word embedding;
- Decoding status;
- Attention query;
- subsequent context;
- Subsequent word distribution.

An early error may propagate along the entire remaining sequence.

## 11. The output layer is not a single layer softmax

The paper uses deep output:

\[
\widetilde{\mathbf t}_i
=
U_o\mathbf s_{\text{read}}
+
V_o\mathbf e(y_{i-1})
+
C_o\mathbf c_i,
\tag{11}
\]

Then do maxout on adjacent units in pairs:

\[
t_{i,j}
=
\max
\left(
\widetilde t_{i,2j-1},
\widetilde t_{i,2j}
\right).
\tag{12}
\]

Finally:

\[
p(y_i=k\mid\cdot)
=
\frac{
\exp(\mathbf w_k^\top\mathbf t_i)
}{
\sum_{k'=1}^{K_y}
\exp(\mathbf w_{k'}^\top\mathbf t_i)
}.
\tag{13}
\]

The paper appendix and implementation use a specific time index, and the output read status is written in the formula \(\mathbf s_{i-1}\). The updated \(\mathbf s_i\) is commonly used in modern explanations. The key to both notations is that the input, state, context, and supervision goals must be aligned as a whole.

## 12. Vocabulary scale

The target vocabulary retains 30,000 high-frequency words, and other words are mapped to `[UNK]`.

Therefore, the softmax scale of equation (13) is approximately:

\[
K_y\approx30{,}000.
\]

The paper does not use subword tokenization. The rare word problem is very obvious in the full test set BLEU.

## 13. Dependency graph for one-step decoding

\[
\mathbf s_{i-1}
\longrightarrow
\alpha_i
\longrightarrow
\mathbf c_i
\longrightarrow
\mathbf s_i
\longrightarrow
p(y_i).
\]

At the same time:

\[
y_{i-1}
\longrightarrow
\mathbf s_i
\quad\text{and}\quad
p(y_i).
\]

This shows that attention is inside recursive dynamics:

- \(\mathbf s_{i-1}\) determines the current read;
- Current read affects \(\mathbf s_i\);
- \(\mathbf s_i\) determines the next read.

## 14. Where does the coverage information come from?

The model does not have an explicit coverage vector recording which source words have been translated. Historical information is mainly hidden in:

\[
\mathbf s_{i-1}.
\]

If the decoded state can summarize past outputs and the context of past reads, the alignment network can move the focus accordingly.

This implicit coverage may cause:

- Duplicate translation;
- Missing translation;
- End prematurely;
- Focusing on the same spot repeatedly.

Subsequent NMT work specifically introduces coverage mechanisms to alleviate these problems.

## 15. Gradually generated core

The decoder of RNNsearch can be summarized as:

\[
\boxed{
\text{prefix status}
\rightarrow
\text{Read source sentence}
\rightarrow
\text{update status}
\rightarrow
\text{Predict target word}
}
\]

The next chapter goes to the core of reading source sentences: scoring, normalization, context and shape of additive attention.
