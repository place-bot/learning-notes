# Special topic on subword tokenization: BPE, Byte-level BPE and WordPiece

Neural networks cannot read strings directly. The text must first pass through the tokenizer and become an integer ID in a limited vocabulary. Both BPE and WordPiece look for sub-word units between "whole words" and "single characters", so that common fragments can be merged into longer tokens, while rare words can still be split and processed.

!!! info "First make common expressions accurate"
    "BPE is widely used in GPT, WordPiece is used in BERT" is suitable as an entry-level index, but two qualifications need to be added:

    - GPT-2 uses **byte-level BPE**: it first reversibly maps UTF-8 bytes into processable symbols, and then applies BPE merging; the subsequent GPT tokenizer follows the overall byte-level, merge-based route, but the specific regularization, vocabulary, and special tokens will change.
    - BERT uses **BasicTokenizer + WordPieceTokenizer**: normalization, casing, and punctuation occur first, and WordPiece then does greedy longest-match-first for each pre-sliced tokenization.

## A general picture

```text
original text
   ↓ normalization
normalized text
   ↓ pre-tokenization
local fragment/word boundary
   ↓ subword model
subword token
   ↓ vocabulary lookup
token IDs
   ↓ special-token post-processing
Model input
```

BPE and WordPiece mainly describe the **subword model** in the middle. Their actual output is also affected by normalization, pre-tokenization, whitespace representation, and special token rules.

## Reading route

1. [Why subwords are needed: The contradiction between whole words, characters and fixed vocabulary](01-why-subwords.md)
2. [Tokenizer’s complete pipeline and responsibilities of each layer](02-tokenizer-pipeline.md)
3. [BPE from data compression to NLP vocabulary learning](03-bpe-training.md)
4. [BPE encoding: How to split new text](04-bpe-encoding.md) according to merge rank
5. [GPT-2 Byte-level BPE: Byte, regular and reversible encoding](05-byte-level-bpe.md)
6. [WordPiece vocabulary training: Maximum likelihood thinking and public evidence boundary](06-wordpiece-training.md)
7. [BERT WordPiece encoding: BasicTokenizer with longest match](07-wordpiece-encoding.md)
8. [BPE vs. WordPiece head-to-head comparison](08-bpe-wordpiece-comparison.md)
9. [Complete hand calculation: How to produce different combinations of the same small corpus](09-worked-example.md)
10. [Official code intensive reading and modern implementation](10-code-implementation.md)
11. [How to evaluate tokenizer, limitations and conclusions](11-evaluation-limitations-conclusion.md)
12. [Papers, official code and reference materials](references.md)

## Questions you should be able to answer after studying

- Why can the subword method alleviate OOV but cannot automatically understand the lexical structure?
- What is the relationship between raw BPE, NLP BPE and byte-level BPE?
- Why should the vocabulary training and tokenization stages of WordPiece be discussed separately?
- What do `Ġ` in GPT-2 and `##` in BERT mean respectively?
- Why does changing tokenizer change context capacity, speed and model parameters?
- Why does the same string get different IDs under different normalization and pre-tokenization?

