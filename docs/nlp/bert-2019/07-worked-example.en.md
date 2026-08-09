# Complete hand calculation: MLM and NSP

## 1. Original sentence pair

\[
[\text{CLS}],\ \text{my},\ \text{dog},\ \text{is},\
\text{cute},\ [\text{SEP}],\
\text{he},\ \text{likes},\ \text{playing},\ [\text{SEP}].
\]

WordPiece may split playing into `play`, `##ing`.

## 2. Three kinds of embedding

Take the `dog` position \(i=2\) as an example:

\[
e_2=e_{\text{dog}}^{token}
+e_A^{segment}
+e_2^{position}.
\]

`he` of the second fragment uses \(e_B^{segment}\), and the positions are still numbered consecutively throughout the sequence.

## 3. MLM

Suppose `dog` is selected and takes the 80% branch, the input becomes `[MASK]`, and the label is still dog. The top-level mask representation produces three simplified logits:

\[
o=(1.2,\;2.0,\;-0.5)
\]

Corresponds to cat, dog, and book respectively.

\[
\operatorname{softmax}(o)
\approx(0.294,\;0.654,\;0.052).
\]

MLM losses:

\[
L_{\text{MLM}}=-\log0.654\approx0.425.
\]

Normal positions that are not selected do not enter MLM loss.

## 4. NSP

If the second clip is indeed the true follow-up, label `IsNext`. Let logits:

\[
u=(1.5,\;0.2)
\]

Corresponds to IsNext, NotNext:

\[
p(\text{IsNext})\approx0.786.
\]

\[
L_{\text{NSP}}=-\log0.786\approx0.241.
\]

Total loss:

\[
L\approx0.425+0.241=0.666.
\]

## 5. Gradient propagation

The MLM gradient propagates from the selected position to all tokens that can affect it through self-attention; the NSP gradient propagates from `[CLS]` to the entire sentence representation. Both update the embedding and 12/24 layer encoder together.

## 6. Fine-tuning

When doing sentiment classification, tokens are no longer masked and MLM/NSP is no longer calculated. Add a classification layer and update it with annotation cross-entropy:

\[
L_{\text{task}}
=
-\log p(y^\star\mid\mathbf C).
\]

This clearly distinguishes pretraining goals from downstream goals.
