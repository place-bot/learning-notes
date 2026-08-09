# BPE vs. WordPiece side-by-side comparison

## 1. Core difference table

|Dimensions| Merge-based BPE | BERT-style WordPiece |
|---|---|---|
|Training starting point|Basic units such as characters or bytes|Initial and intra-word character units|
|Merge selection|Usually choose the highest frequency adjacent pair|The original idea is to maximize likelihood improvement; common implementation uses normalized pair score|
|runtime assets| vocabulary + ordered merge list |Mainly the final vocabulary|
|new text encoding|Repeatedly apply lowest merge rank| greedy longest-match-first |
|intra-word tag|Use `</w>`, `Ġ`, `▁`, etc. according to the implementation|BERT commonly uses `##` to represent continuation|
|unknown character|Character version may be OOV; byte-level version may fall back to bytes|The original BERT may turn the entire basic token into `[UNK]`|
|Typical model|GPT-2, RoBERTa’s byte-level BPE, etc.|BERT, DistilBERT, MobileBERT, etc.|

## 2. Common points

Both:

- Establish limited vocabulary from small units;
- Let high-frequency clips obtain independent tokens;
- Divide rare words into smaller units;
- Compromise between vocabulary size and sequence length;
- The production of linguistic morphemes is not guaranteed;
- Needs to be defined together with normalization, pre-tokenization and special tokens.

## 3. "Which pair to choose" is different

BPE：

\[
\operatorname{score}_{\mathrm{BPE}}(a,b)=F(a,b).
\]

Common WordPiece approximations:

\[
\operatorname{score}_{\mathrm{WP}}(a,b)
=
\frac{F(a,b)}{F(a)F(b)}.
\]

Therefore BPE favors pairs with high absolute frequency; WordPiece-like score penalizes components with high marginal frequencies.

## 4. "How to encode" is different

### BPE

Encoding is subject to merge order:

```text
Current adjacent pair → Check rank → Merge the one with the smallest rank first
```

### WordPiece

Encoding only requires the current vocabulary:

```text
Current position → Take the longest available prefix in vocabulary → Move to the next position
```

Therefore, even if the final set of vocabulary strings is the same, the two runtime algorithms may give different segmentations.

## 5. `Ġ`, `##` and `▁` should not be confused

|surface symbol|common sources|meaning|
|---|---|---|
| `Ġcat` | GPT-2 byte mapping |The underlying fragment usually contains leading space bytes|
| `##ing` | BERT WordPiece |token is at the non-first position of the same basic token|
| `▁cat` | SentencePiece |`▁` usually represents normalized whitespace boundaries|

These symbols belong to the tokenizer's internal textual representation and may not necessarily appear in the user's original text.

## 6. Algorithm names and software libraries are at different levels

- BPE, WordPiece, and Unigram are subword models;
- SentencePiece is a tokenizer software that can be trained and decoded from raw text, and supports BPE and Unigram;
- Hugging Face Tokenizers is an implementation library that combines normalizer, pre-tokenizer, model and post-processor;
- tiktoken is a fast implementation of some OpenAI tokenizers;
- Transformers are responsible for loading the tokenizer together with the specific model checkpoint.

"Use SentencePiece" cannot directly infer the use of BPE; "download from Hugging Face" cannot infer the tokenizer algorithm.

## 7. Cannot replace tokenizer without checkpoint

The \(i\) row of the model embedding corresponds to the \(i\) token of the tokenizer during training:

\[
\operatorname{Embed}(t_i)=E[i,:].
\]

If you directly change a set of vocabulary, even if the vocabulary size is the same, the meaning of the same ID will change. Unless retrained or initialized with controlled vocabulary extension and embedding, the tokenizer must be used in conjunction with the checkpoint.

