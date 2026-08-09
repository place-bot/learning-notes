# WordPiece, [CLS], [SEP] and three kinds of Embedding

## 1. Sequence format

Single sentence:

\[
[\text{CLS}],\;A,\;[\text{SEP}].
\]

Sentence pair:

\[
[\text{CLS}],\;A,\;[\text{SEP}],\;B,\;[\text{SEP}].
\]

A "sentence" in a paper can be a continuous text fragment and does not require strict linguistic sentences.

## 2. WordPiece

The vocabulary is about 30,000. Low-frequency words can be split into sub-words, for example

\[
\text{playing}\rightarrow
\text{play},\;\text{\#\#ing}.
\]

"##" marks the segment as a continuation of the previous word. The original MLM paper was sampled by WordPiece token position, not the whole-word masking published later.

## 3. [CLS]

Add `[CLS]` at the beginning of each sequence, the top vector

\[
\mathbf C\in\mathbb R^H
\]

For NSP and downstream classification. It aggregates full sequence information through self-attention. \(\mathbf C\) without task fine-tuning does not necessarily naturally become a universal sentence vector; the footnote of the paper clearly reminds that NSP-trained C requires fine-tuning.

## 4. [SEP]

`[SEP]` marks segment boundaries. There is also a `[SEP]` at the end of the sentence pair.

## 5. Addition of three embeddings

The \(i\)th input vector:

\[
\mathbf e_i
=
\mathbf e_i^{\text{token}}
+
\mathbf e_i^{\text{segment}}
+
\mathbf e_i^{\text{position}}.
\]

- token embedding: WordPiece identity;
- segment embedding: segment A or B;
- position embedding: absolute position.

BERT's original position embedding is a learnable parameter with a maximum length of 512; this is different from the original Transformer's fixed sinusoidal position.

## 6. Attention mask and segment id

attention mask blocks padding; segment id distinguishes A/B. Segment ID itself does not prohibit cross-sentence attention. After the sentence pairs are assembled into a sequence, all valid tokens can pay attention to each other, which provides bidirectional cross-attention for NLI and QA.

## 7. Output

The top-level token representation is recorded as

\[
\mathbf T_i\in\mathbb R^H.
\]

Taxonomy usually reads \(\mathbf C\), and sequence annotation and question answering each read \(\mathbf T_i\).
