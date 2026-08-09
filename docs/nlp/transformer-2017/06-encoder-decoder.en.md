# Encoder, Decoder and three kinds of Attention

## 1. Encoder layer

input

\[
\mathbf X^{(0)}
=
\sqrt{d_{\text{model}}}\,\operatorname{Embed}(\mathbf x)
+\mathbf{PE}.
\]

Layer \(\ell\):

\[
\begin{aligned}
\widetilde{\mathbf X}^{(\ell)}
&=
\operatorname{LayerNorm}\!\left(
\mathbf X^{(\ell-1)}
+\operatorname{Dropout}(
\operatorname{MHA}_{\text{self}}(\mathbf X^{(\ell-1)}))
\right),\\
\mathbf X^{(\ell)}
&=
\operatorname{LayerNorm}\!\left(
\widetilde{\mathbf X}^{(\ell)}
+\operatorname{Dropout}(
\operatorname{FFN}(\widetilde{\mathbf X}^{(\ell)}))
\right).
\end{aligned}
\]

Q, K, V of encoder self-attention all come from the same layer input.

## 2. Decoder layer

The \(\ell\) layer is executed in sequence:

\[
\begin{aligned}
\mathbf U&=\operatorname{AddNorm}(
\mathbf Y,\operatorname{MaskedMHA}(\mathbf Y)),\\
\mathbf V&=\operatorname{AddNorm}(
\mathbf U,\operatorname{CrossMHA}(\mathbf U,\mathbf Z,\mathbf Z)),\\
\mathbf Y'&=\operatorname{AddNorm}(
\mathbf V,\operatorname{FFN}(\mathbf V)).
\end{aligned}
\]

\(\mathbf Z\) is the top-level encoder output. In cross-attention, query comes from decoder, and key/value comes from encoder.

## 3. Three types of attention responsibilities

- encoder self-attention: construct contextualized source representation;
- masked decoder self-attention: summarize already visible target prefixes;
- cross-attention: Read the source sentence based on the current target representation.

The Bahdanau model only uses attention for the third type of connection; the Transformer also gives attention to the first and second type sequence modeling.

## 4. Information flow between layers and locations

All positions in the same layer are parallel, but the layers are still serial:

\[
\mathbf X^{(0)}
\rightarrow\mathbf X^{(1)}
\rightarrow\cdots\rightarrow\mathbf X^{(6)}.
\]

Therefore, "no recursion" means that there is no time step state chain of length \(n\), which does not mean that all network layers can be calculated simultaneously.

## 5. Autoregressive output

The top-level decoder represents the linear transformation and softmax of shared vocabulary weights to obtain the next token distribution at each position. Training can generate all position logits at once; generation only determines one new token at a time.
