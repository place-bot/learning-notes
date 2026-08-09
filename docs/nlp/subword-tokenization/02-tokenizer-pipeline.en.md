# Complete pipeline of Tokenizer

## 1. Just saying “use BPE” is not enough

Even if both tokenizers use BPE, they may output completely different IDs due to differences in case, Unicode, spaces, and pre-tokenization. The complete tokenizer can be written as a function composition:

\[
T
=
P_{\mathrm{post}}
\circ L_{\mathrm{id}}
\circ S_{\mathrm{subword}}
\circ P_{\mathrm{pre}}
\circ N,
\]

Among them:

|symbol|stage|function|
|---|---|---|
| \(N\) | Normalizer |Unicode normalization, case, accents, and whitespace handling|
| \(P_{\mathrm{pre}}\) | Pre-tokenizer |Determine whitespace, punctuation, or regular boundaries|
| \(S_{\mathrm{subword}}\) | Subword model |BPE, WordPiece or Unigram segmentation|
| \(L_{\mathrm{id}}\) | Vocabulary lookup |token string mapped to integer ID|
| \(P_{\mathrm{post}}\) | Post-processor |Add `[CLS]`, `[SEP]`, BOS, EOS, etc.|

## 2. Normalization

Normalization may perform:

- Unicode NFC, NFD, NFKC or NFKD;
- Convert uppercase to lowercase;
- Remove combined accents;
- Control character filtering;
- Unification of multiple blank spaces;
- Full-width and compatible character conversion.

Normalization may not be reversible. For example, after uncased BERT lowercases `Café` and removes the accents, it may result in `cafe`. The token IDs cannot restore the original case and accents.

## 3. Pre-tokenization

Pre-tokenizer determines within which boundaries subword models can be merged. Common practices include:

- Press space tokenization;
- Separate punctuation points;
- Add spaces on both sides of Chinese characters;
- Use regular rules to distinguish letters, numbers, abbreviations and punctuation;
- Bind spaces to the next fragment.

GPT-2's byte-level BPE does not directly allow all bytes to be arbitrarily merged throughout the document. It first uses regular expressions to find local tokens, and then applies byte mapping and BPE to each local fragment.

## 4. Subword model

This stage determines how local fragments are decomposed into vocabulary units:

```text
BPE: Repeatedly merge according to the merge rank obtained by training
WordPiece: Find the longest available fragment in vocabulary from the current position
Unigram: Search for high-probability segmentation under candidate subword probabilistic model
```

Training tokenizer and using tokenizer are two different algorithms. The training phase learns vocabulary or merging rules; the encoding phase fixes these assets and no longer re-counts the input text.

## 5. Special tokens

Special tokens are defined by the model training goals and should not be guessed by strings:

|model route|Common special tokens|
|---|---|
| BERT | `[PAD]`、`[UNK]`、`[CLS]`、`[SEP]`、`[MASK]` |
| GPT-2 | `<|endoftext|>`;Original GPT-2 also used this for document boundaries|
|modern chat model|BOS, EOS, system/user/assistant, tool call boundaries, etc.|

The text form, ID and whether to automatically add special tokens all belong to the tokenizer configuration.

## 6. Offset mapping

Sequence annotation, extractive question answering and highlighting require mapping the token back to the original character range:

\[
(t_i)\longleftrightarrow [a_i,b_i).
\]

Normalization changes characters, and byte-level tokens are based on UTF-8 bytes, so the offset cannot be reconstructed solely from the token string length. Modern fast tokenizers track alignment relationships in the pipeline.

## 7. Two standards for round-trip

### Byte reversible

\[
\operatorname{decode}(\operatorname{encode}(x))=x.
\]

The GPT-2 byte-level BPE's byte mapping supports this goal.

### Reversible after normalization

\[
\operatorname{decode}(\operatorname{encode}(x))=N(x).
\]

If the tokenizer actively lowercasing or de-accents, it can only require the normalized text to be restored. When testing tokenizers it should be clear which standard to use.

