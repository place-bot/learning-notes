# Intensive reading of official code and modern implementation

## 1. GPT-2 `encoder.py`

Key objects officially implemented by OpenAI include:

|object|function|
|---|---|
| `bytes_to_unicode()` |Build a reversible table of 256 bytes into printable Unicode symbols|
| regex pattern |Cut input into abbreviations, letters, numbers, symbols and whitespace segments|
| `bpe_ranks` |Map ordered merge list to rank|
| `bpe()` |In each round, the adjacent pairs with the smallest current rank are merged.|
| `encoder` / `decoder` |Two-way mapping between token string and ID|
| cache |Deterministic BPE result that multiplexes the same fragments|

The encoding call chain can be summarized as:

```python
for piece in regex_pretokenize(text):
    byte_symbols = reversible_byte_map(piece.encode("utf-8"))
    subtokens = apply_ranked_bpe(byte_symbols, merge_ranks)
    ids.extend(vocab[token] for token in subtokens)
```

For decoding, reverse splicing, reverse byte map, and then do UTF-8 decoding.

## 2. BERT `tokenization.py`

Google’s official implementation is divided into three layers:

|class|Responsibilities|
|---|---|
| `BasicTokenizer` |Cleaning, CJK spacing, lowercase, accent removal, punctuation segmentation|
| `WordpieceTokenizer` |Do greedy longest-match-first for each basic token|
| `FullTokenizer` |Concatenate the two layers and complete token/ID mapping|

The key control logic of WordpieceTokenizer is:

```python
while start < len(chars):
    end = len(chars)
    while end > start:
        candidate = make_candidate(chars[start:end], is_continuation=start > 0)
        if candidate in vocab:
            break
        end -= 1
```

If there is no candidate match at this position, the entire basic token output is `[UNK]`.

## 3. A minimal BPE encoder

The following tutorial implementation assumes that the input is already a sequence of characters:

```python
def adjacent_pairs(symbols):
    return set(zip(symbols, symbols[1:]))

def encode_bpe(text, merge_ranks):
    symbols = tuple(text)
    while len(symbols) > 1:
        candidates = adjacent_pairs(symbols)
        ranked = [p for p in candidates if p in merge_ranks]
        if not ranked:
            break
        best = min(ranked, key=merge_ranks.get)

        merged = []
        i = 0
        while i < len(symbols):
            if i + 1 < len(symbols) and symbols[i:i+2] == best:
                merged.append(best[0] + best[1])
                i += 2
            else:
                merged.append(symbols[i])
                i += 1
        symbols = tuple(merged)
    return list(symbols)
```

Real implementation also requires pre-tokenization, byte mapping, cache, special tokens, error handling and ID mapping.

## 4. A minimal WordPiece encoder

```python
def encode_wordpiece(word, vocab, prefix="##", unk="[UNK]"):
    pieces = []
    start = 0
    while start < len(word):
        match = None
        for end in range(len(word), start, -1):
            candidate = word[start:end]
            if start > 0:
                candidate = prefix + candidate
            if candidate in vocab:
                match = candidate
                start = end
                pieces.append(candidate)
                break
        if match is None:
            return [unk]
    return pieces
```

It shows BERT-style runtime segmentation, not WordPiece vocabulary trainer.

## 5. Hugging Face Tokenizers component implementation

The modern `tokenizers` library breaks down the pipeline into composable components:

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import ByteLevel
from tokenizers.trainers import BpeTrainer

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = ByteLevel(add_prefix_space=False)
trainer = BpeTrainer(
    vocab_size=30_000,
    special_tokens=["[UNK]", "[PAD]"],
)
tokenizer.train(["corpus.txt"], trainer)
```

To reproduce GPT-2 or BERT, the tokenizer of the original checkpoint should be loaded first instead of just selecting the model class with the same name. If the default parameters, normalizer and pre-tokenizer are different, another set of tokenizers may be generated.

## 6. Recurring assets that must be saved

```text
tokenizer.json or equivalent component configuration
vocabulary
ordered BPE merges (if needed)
normalization configuration
pre-tokenization configuration
special token IDs
post-processing / chat template
library version and file hash
```

Saving just `vocab.txt` against the original BERT runtime is usually enough to reconstruct the WordPiece vocabulary lookup, but still requires logging both cased/uncased and BasicTokenizer behavior.

## 7. Security and correctness check

- Do not execute custom tokenizer code from untrusted repositories;
- Fixed model and tokenizer revision;
- Check whether the special token is overwritten by ordinary normalization;
- Test for empty strings, long words, control characters, emoji, combining characters and invalid UTF-8;
- Save offset mapping and verify span alignment;
- Compare the output consistency of slow and fast tokenizer before model deployment.

