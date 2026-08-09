# WordPiece encoding for BERT

## 1. FullTokenizer has two layers

BERT official `FullTokenizer` first calls BasicTokenizer, and then calls WordpieceTokenizer for each basic token:

```text
raw text
  ↓ BasicTokenizer
basic tokens
  ↓ WordpieceTokenizer
word pieces
  ↓ vocabulary lookup
token IDs
```

Only discussing longest-match-first will miss out on case, accent, punctuation and Chinese character processing.

## 2. BasicTokenizer

A typical flow for raw uncased BERT includes:

1. Delete invalid or unnecessary control characters;
2. Unify the blank space;
3. Add spaces on both sides of the CJK unified ideogram;
4. Lowercase;
5. Decompose and remove combining marks through Unicode NFD;
6. Cut out the punctuation points independently.

For example, the idea given by the official document is:

```text
John Johanson's,
→ john johanson ' s ,
→ john johan ##son ' s ,
```

Cased models retain case and accents and must match the tokenizer configuration of the corresponding checkpoint.

## 3. Greedy Longest-Match-First

For a basic token character sequence \(c_1\cdots c_m\), starting at position `start`:

1. First try the longest substring to the end of the word;
2. If it is not in the vocabulary, gradually shorten the right end;
3. Add `##` to non-word-initial candidates;
4. After finding the first vocabulary item, move `start`;
5. Repeat until the entire word is covered.

Pseudo code:

```python
start = 0
pieces = []
while start < len(chars):
    end = len(chars)
    found = None
    while end > start:
        candidate = chars[start:end]
        if start > 0:
            candidate = "##" + candidate
        if candidate in vocab:
            found = candidate
            break
        end -= 1
    if found is None:
        return ["[UNK]"]
    pieces.append(found)
    start = end
```

## 4. `unaffable` example

If vocabulary contains:

```text
un, ##aff, ##able
```

The algorithm gets:

```text
unaffable
→ un | ##aff | ##able
```

In the first paragraph, try the complete word, `unaffabl`,... until `un`; in the second paragraph, all candidates are with `##`, and find `##aff`; finally, `##able` is found.

## 5. Why does the failure of one character make the whole word become `[UNK]`

If any position cannot be overwritten, the original BERT implementation will output the entire basic token as `[UNK]` instead of retaining the found prefix and replacing only the remaining characters.

In addition, basic tokens longer than `max_input_chars_per_word` also directly become `[UNK]`; the official default upper limit is 200 characters.

This is different from the fallback of byte-level BPE. The latter always falls back to UTF-8 byte units.

## 6. Performance of Chinese BERT

BERT BasicTokenizer will add spaces on both sides of each CJK unified ideogram, making these Chinese characters independent basic tokens. WordPiece does not re-merge them across basic-token boundaries, so consecutive Chinese characters of the original Chinese BERT usually enter subsequent vocabulary lookups word by word.

You cannot simply say “WordPiece always does Chinese tokenization first”. The original BERT mainly separated Chinese characters according to Unicode range and did not call an external Chinese lexical tokenizer.

## 7. Add `[CLS]` and `[SEP]`

Sentence pair tasks typically form:

\[
[\mathrm{CLS}]
\;A\;
[\mathrm{SEP}]
\;B\;
[\mathrm{SEP}].
\]

This is post-processing, not the WordPiece longest-match algorithm. `[MASK]` in MLM is also added by the training sample construction.

## 8. Label alignment

An original word in NER may be split into multiple pieces:

```text
Johanson → johan | ##son
```

Common strategies include:

- Calculate label loss only on the first piece;
- Copy labels to all pieces and adjust BIO rules;
- Save `word_ids` or offset mapping for aggregation.

The same alignment rule must be used for training and evaluation, otherwise token-level indicators cannot be compared.
