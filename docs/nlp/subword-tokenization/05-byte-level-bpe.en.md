# Byte-level BPE of GPT-2

## 1. Why change to byte layer?

The number of Unicode code points is much larger than the common 32K–64K subword vocabulary. If all possible characters are used as the base alphabet, the initial vocabulary itself will be very large. UTF-8 consists of only 256 byte values:

\[
\mathcal B=\{0,1,\ldots,255\}.
\]

Therefore any valid UTF-8 text can be represented first as a sequence of bytes and then merged to obtain common long fragments.

## 2. GPT-2 does not operate directly on non-printable bytes

GPT-2 official encoder establishes reversible mapping:

\[
\phi:\{0,\ldots,255\}\longrightarrow\mathcal U_{256},
\]

Among them, \(\mathcal U_{256}\) are 256 Unicode symbols that facilitate regular and string code processing. Printable characters are kept as intuitive as possible; whitespace and control bytes are mapped to extra symbols.

So:

```text
text
→ UTF-8 bytes
→ Printable Unicode surrogate symbols
→ BPE merges
→ vocabulary IDs
```

## 3. What exactly is `Ġ`?

In the GPT-2 mapping, the space byte will be displayed as `Ġ`. For example, token `Ġcat` usually means that its underlying bytes begin with a space, followed by `cat`.

`Ġ` is not an English lexical symbol, nor does the original text really contain this character. It is a visual result of a byte-to-printable Unicode mapping.

This makes:

```text
"cat" and "cat"
```

Can have different tokens. The leading space becomes part of the token pattern.

## 4. Regular Pre-tokenization

The official implementation of GPT-2 first uses regular rules to distinguish:

- Common English abbreviations and suffixes;
- consecutive letters;
- consecutive numbers;
- Non-whitespace, non-alphanumeric symbols;
- Blank.

Some branches allow fragments to have a leading space. Each regex match performs byte mapping and BPE separately, so the merge will not arbitrarily cross these match boundaries.

## 5. Coding process

For each regex fragment \(q\):

\[
b(q)=\operatorname{UTF8}(q),
\]

\[
u(q)=\phi(b_1)\phi(b_2)\cdots\phi(b_m),
\]

\[
s(q)=\operatorname{BPE}_{r}(u(q)),
\]

Finally, look up each subtoken into an ID.

## 6. Decoding process

\[
\text{IDs}
\rightarrow
\text{BPE token strings}
\rightarrow
\text{Splicing Agent Unicode}
\rightarrow
\phi^{-1}
\rightarrow
\text{UTF-8 decode}.
\]

As long as the input is valid text and there is no additional irreversible normalization, the entire process can recover the original bytes.

## 7. What does "no UNK" mean?

The 256 base bytes always provide a fallback, so any UTF-8 string can be encoded. Rare characters may be split into multiple tokens. For example, the UTF-8 representation of an emoji usually occupies multiple bytes.

Coverage guarantee and efficiency are two different things:

- Common English fragments may have one token covering multiple characters;
- Rare text in training may account for multiple tokens per character;
- seemingly identical Unicode character sequences may have different bytes if normalization is different.

## 8. Representation boundaries of the GPT family

GPT-2 explicitly exposes byte-to-Unicode maps, regex, merge ranks, and vocabulary. The subsequent GPT tokenizer still adopts the core idea of ​​byte-level and merge-based, but the vocabulary size, regularity, merge list and special token have changed.

Therefore, "GPT uses BPE" should be understood as a summary of the architectural route, and all subsequent GPT models cannot be directly encoded with GPT-2's `encoder.json`.

