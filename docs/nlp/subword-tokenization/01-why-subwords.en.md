# Why do we need subword units?

## 1. The language is open and the model vocabulary is fixed

The trained model usually has a fixed vocabulary:

\[
\mathcal V=\{v_1,v_2,\ldots,v_{|\mathcal V|}\}.
\]

The tokenizer maps the string \(x\) to an ID sequence:

\[
T(x)=(t_1,t_2,\ldots,t_n),
\qquad t_i\in\{1,\ldots,|\mathcal V|\}.
\]

Natural language, on the other hand, is constantly filled with new names, spelling variations, numbers, URLs, terms, and compound words. If the vocabulary unit only allows complete words, new words that appear after training cannot be mapped to existing IDs.

## 2. Choice of three granularities

|Granularity|Advantages|cost|
|---|---|---|
|whole word|The sequence is short and the semantics of common words are concentrated.|The vocabulary is huge, and long-tail words and new words become OOV|
|characters/bytes|Small basic vocabulary, strong coverage ability|The sequence is long, and the model needs to combine word meanings across more positions.|
|subword|The high-frequency segment is longer and the low-frequency segment is detachable.|Segmentation is determined by statistics and rules, and the boundaries may not conform to linguistic forms.|

The core compromise of the subword approach is:

\[
\text{high frequency string}\longrightarrow\text{fewer tokens},
\]

\[
\text{low frequency string}\longrightarrow\text{More but representable tokens}.
\]

For example, a vocabulary might encode `playing` as `play + ing`, breaking rare names into shorter fragments. The model shares a portion of the statistical strength between related words by sharing the embedding of `play` or `ing`.

## 3. Two meanings of OOV

### Word level OOV

The complete word is not in vocabulary. The subword algorithm can usually break it into known units, thus avoiding the whole word `[UNK]`.

### Basic alphabet OOV

Not even the smallest unit is in the initial alphabet. This situation may still be encountered with character-level BPE or WordPiece; the byte-level approach is based on 256 bytes and has a representation path for any UTF-8 byte sequence.

"No OOV" only guarantees coding, but does not guarantee efficient coding or good model understanding. A rare character may be split into multiple byte tokens and barely appear during training, so the corresponding representation will still be weak.

## 4. The number of Tokens directly affects the model cost

Assume that the length of the original text after tokenizer is \(n\). The main matrix size for standard self-attention is approximately:

\[
O(n^2).
\]

The same piece of Chinese, code or mathematical text may account for 500 and 800 tokens respectively under two tokenizers. The latter not only uses up the context faster, but also increases prefill calculation and KV cache.

## 5. Vocabulary size also has costs

The embedding matrix shape is usually:

\[
E\in\mathbb R^{|\mathcal V|\times d},
\]

Where \(d\) is the hidden size. If the input embedding and output projection do not share parameters, vocabulary related parameters will appear twice. Increasing vocabulary can shorten the sequence, but increase embedding, output layer and softmax costs.

The Tokenizer design therefore optimizes both directions simultaneously:

\[
\text{sequence length}
\quad\text{with}\quad
\text{vocabulary scale}.
\]

## 6. Subwords are not equal to morpheme analysis

BPE and WordPiece learn string fragments from frequency or likelihood targets without explicit use of roots, prefixes, suffixes, or grammar rules. `un + happy` may fit the morphology exactly, or it may be cut into `unh + app + y`.

The direct goal of statistical subwords is to improve encoding and model training under limited vocabulary, and is not guaranteed to produce linguistically correct morphemes.

