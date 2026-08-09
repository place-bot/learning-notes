#WordPiece Training: Boundaries of Ideas and Evidence

## 1. Historical goals

WordPiece was first used for Japanese and Korean voice search. The core idea is to start from the basic unit and gradually add sub-words to maximize the likelihood of training data under the language model.

If the current vocabulary is \(\mathcal V\) and the candidate new piece is \(z\), the original expression can be summarized as selection:

\[
z^*
=
\arg\max_z
\left[
\log p(\mathcal C\mid\mathcal V\cup\{z\})
-
\log p(\mathcal C\mid\mathcal V)
\right].
\]

It is different from BPE’s motivation of directly selecting the highest frequency pair: WordPiece is more concerned about the benefits of new units to the modeled training corpus.

## 2. What did BERT announce?

The BERT paper and official repository clearly state that 30,000 WordPiece tokens are used. The official repository is made public:

- `vocab.txt`；
- BasicTokenizer；
- WordpieceTokenizer；
- Token to ID mapping;
- longest-match-first encoding.

The official repository also clearly stated that the C++ code for learning the new WordPiece vocabulary relied on Google's internal libraries and was not open sourced with BERT.

Therefore the following must be distinguished:

1. The likelihood idea in WordPiece literature;
2. A trainer implemented by the community based on public information;
3. Directly verifiable greedy segmentation in BERT inference code.

## 3. Common Pair Score approximations

Many modern teachings and implementations describe WordPiece's merge preference in terms of:

\[
\operatorname{score}(a,b)
=
\frac{F(a,b)}{F(a)F(b)}.
\]

Compared to BPE's \(F(a,b)\), the denominator will de-prioritize pairs where both parts are common in favor of more associative pairs.

This formula is suitable for explaining the statistical difference between BPE and WordPiece, but it should not be written as "the published accurate source code of BERT's internal trainer". Google has not released this trainer, and specific smoothing, likelihood models, and tie-breaking cannot be fully restored from the BERT repository.

## 4. The meaning of `##` prefix

BERT English vocabulary usually writes non-initial piece as:

```text
play ##ing
```

Among them, `##ing` means that it can only be connected to the current position inside a word and cannot be used as the first token of the pre-cut tokenization. So the initial alphabet distinguishes:

```text
First character: p
Characters within words: ##l, ##a, ##y
```

`##` is a vocabulary convention, not an original character. Other WordPiece implementations can configure different continuing-subword prefixes.

## 5. Conceptual pseudocode of the training process

```python
splits = initialize_with_word_start_and_continuation_symbols(corpus)
vocab = special_tokens + initial_alphabet

while len(vocab) < target_size:
    pair_statistics = collect_statistics(splits)
    best_pair = choose_largest_likelihood_gain(pair_statistics)
    new_piece = merge(best_pair)
    vocab.add(new_piece)
    update_splits(new_piece)
```

`choose_largest_likelihood_gain` here is the core of the method. Different open source libraries may use computable score approximations, and it should not be assumed that they necessarily reproduce all the details of BERT's internal trainer.

## 6. Why frequency normalization makes sense

Suppose the pair \((a,b)\) appears 100 times, but \(a\) and \(b\) each appear 10,000 times. The combination of the two is not specific. If another pair occurs 30 times, and the two parts are almost exclusively adjacent to each other, the new merge may express the stable segment more efficiently.

Frequency ratios measure approximately:

\[
\text{Co-occurrence intensity}
\approx
\frac{\text{pair frequency}}
{\text{marginal frequencies}}.
\]

This is close to the normalized intuition of PMI, but the specific formula, counting caliber and probability model do not have to be completely equivalent to PMI.

## 7. What to save in the end

BERT's runtime mainly reads the final `vocab.txt`. WordPiece encoding directly performs the longest match on the vocabulary without replaying the training merge list.

This is in sharp contrast to the asset structure of classic merge-based BPE:

```text
BPE runtime：vocabulary + ordered merges
WordPiece runtime：vocabulary + continuation-prefix convention
```

