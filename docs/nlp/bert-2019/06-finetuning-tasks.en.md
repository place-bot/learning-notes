# Unify fine-tuning interface

The original paper adds a small output layer to each task and updates all BERT parameters.

## 1. Single sentence/sentence pair classification

Take `[CLS]` top-level representation \(\mathbf C\):

\[
p(y\mid x)
=
\operatorname{softmax}(
\mathbf W\mathbf C+\mathbf b).
\]

Single sentence emotions use A segment; NLI and paraphrase use A/B segments.

## 2. Token classification

\(\mathbf T_i\) of each token enters the shared classification layer:

\[
p(y_i\mid x)
=
\operatorname{softmax}(
\mathbf W\mathbf T_i+\mathbf b).
\]

Suitable for sequence annotation such as NER. Tag alignment after WordPiece splits needs to be handled explicitly by the implementation.

## 3. SQuAD extractive question answering

Input:

\[
[\text{CLS}]\ \text{Question}\ [\text{SEP}]\
\text{Passage}\ [\text{SEP}].
\]

Learning the starting point vector \(S\) and the end point vector \(E\):

\[
p_i^{start}
=
\frac{\exp(S^\top T_i)}
{\sum_j\exp(S^\top T_j)},
\quad
p_j^{end}
=
\frac{\exp(E^\top T_j)}
{\sum_k\exp(E^\top T_k)}.
\]

Candidate span scores:

\[
S^\top T_i+E^\top T_j,\qquad j\ge i.
\]

SQuAD 2.0 treats the `[CLS]` position as a no-answer span and selects the threshold in the development set.

## 4. SWAG Multiple Choice

Construct sentence pairs for the four candidates, take \(\mathbf C_k\) for each, and use a vector to score:

\[
s_k=\mathbf w^\top\mathbf C_k,
\qquad
p(k)=\operatorname{softmax}(s)_k.
\]

## 5. The meaning of unity

In the past, systems often designed a large number of dedicated networks for QA, NLI, and NER. BERT puts the main representation learning into the pretraining encoder, and the downstream only needs to adjust the input format and shallow output layer.

## 6. Fine-tuning and feature extraction

The paper also tests freezing BERT and extracting features from each layer for NER. The last four layers of splicing reached 96.1 dev F1, which is close to the full fine-tuning of 96.4; the description indicates that it can be used as a feature, but the main method is end-to-end fine-tuning.
