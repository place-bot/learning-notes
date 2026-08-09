# Byte-level BPE: any string can be encoded

## 1. Enter the target represented

A general language model hopes to assign a probability to any string. If vocabulary only contains common words, unknown words will appear:

\[
\text{unseen word}\longrightarrow \langle\mathrm{UNK}\rangle.
\]

When multiple different strings are squashed into the same UNK, the original text cannot be recovered, and the model cannot accurately generate names, codes, spelling variations, and rare characters.

## 2. Trade-offs between three granularities

|Granularity|Advantages|cost|
|---|---|---|
| word |Short sequences and complete semantics of common words|Huge vocabulary, OOV|
| character/byte |Overwrite any string|Repeated learning of long sequences and common word structures|
| subword |High-frequency fragments are represented as a whole and low-frequency words are separated.|Need to learn tokenization vocabulary|

GPT-2 uses byte-level BPE: the basic atoms are UTF-8 bytes, and then BPE is used to merge frequent byte sequences into longer tokens.

## 3. Why the basic vocabulary is 256

One byte has

\[
2^8=256
\]

kind of value. Any Unicode string can first be encoded into a UTF-8 byte sequence. So only 256 basic symbols are needed for complete coverage; BPE merging is only responsible for improving compression efficiency.

The paper points out that if it is directly based on all Unicode code points, the basic vocabulary will exceed 130,000, without adding any multi-character tokens, and the cost will be too high.

## 4. Reversible byte mapping

Official `encoder.py`'s `bytes_to_unicode()` creates a bijection:

\[
b\in\{0,\ldots,255\}
\quad\leftrightarrow\quad
u_b\in\text{Collection of printable Unicode symbols}.
\]

This way the BPE implementation can still work on the string while preserving the original bytes. When decoding, execute in sequence:

\[
\text{token IDs}
\to
\text{BPE string}
\to
\text{Bytes}
\to
\text{UTF-8 text}.
\]

## 5. BPE merge

Assume that the current word is split into a sequence of symbols:

\[
(s_1,s_2,\ldots,s_m).
\]

The algorithm iteratively finds the top adjacent pair in the training corpus and merges it. Simplified example:

```text
l o w e r
lo w e r
low e r
low er
lower
```

A common word may become a token; a rare word may still be composed of multiple subwords or bytes.

## 6. Why can’t we merge across categories unconditionally?

The paper found that greedy merging directly on the byte string will waste multiple vocabulary slots for surface forms such as `dog`, `dog!`, `dog?`. The authors restrict merging across character categories and make exceptions for spaces to reduce fragmentation caused by punctuation variants.

The official rules roughly divide the text into:

- English abbreviation and suffix;
- Optional leading space plus letter string;
- Optional leading space plus numeric string;
- Optional leading space plus symbol string;
- Empty string.

## 7. Vocabulary and boundaries

The reported vocabulary size is 50,257. It can usually be understood as:

\[
256\ \text{byte basic symbols}
+
50{,}000\ \text{Merge result of about times}
+
1\ \text{special token}.
\]

GPT-2 uses `<|endoftext|>` to mark document boundaries. Spaces are often absorbed into the following token, so the same word may correspond to different token sequences when there are spaces at the beginning and before the sentence.

## 8. What does it solve and what does it leave behind?

It provides:

- OOV-free reversible encoding;
- Basic coverage of spelling, URLs, codes, and multilingual characters;
- Shorter sequences than the pure byte model.

It still has limitations:

- The merge learned from the English center corpus is less efficient in compressing other text;
- Token boundaries are not equal to lexical or semantic boundaries;
- The same character may occupy multiple bytes in UTF-8;
- The computational cost is determined by the number of tokens, and the actual cost varies in different languages.
