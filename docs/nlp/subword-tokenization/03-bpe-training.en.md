# BPE: from data compression to subword vocabulary

## 1. Objectives of original BPE

When Philip Gage introduced BPE in 1994, he discussed lossless data compression. The algorithm finds the most frequent pair of adjacent bytes, replaces it with an unused byte, and saves a replacement table:

```text
Original sequence: A A A B A A A B
High frequency pair: A A
New notation: X := A A
After replacement: X A B X A B
```

When decompressing, recursively expand \(X\) according to the replacement table. This version is limited by available bytes and is designed to compress the file size.

## 2. What has changed in NLP BPE?

Sennrich, Haddow, and Birch applied this idea of "repeatedly merging high-frequency adjacent symbols" to neural machine translation:

- The initial symbol is usually a character, not necessarily a real byte;
- The newly merged item is a growable sub-word vocabulary entry;
- No need to stuff merged result into an unused byte;
- The goal is to process rare words under a fixed vocabulary, rather than directly outputting compressed files;
- merge operations are saved as models encoding new words.

## 3. Start with vocabulary with frequency numbers

First perform pre-tokenization on the training corpus to obtain words and frequencies:

\[
\mathcal C=\{(w_i,f_i)\}_{i=1}^{M}.
\]

Each word is broken down into an initial sequence of characters. The classic subword-nmt example also adds the word-suffix token `</w>` to distinguish the fragments within the tokenization and the word-suffix fragments:

```text
low   → l o w </w>
lower → l o w e r </w>
```

Different modern implementations represent boundaries differently, and `</w>` cannot be considered a required rule for all BPEs.

## 4. Count adjacent pairs

Let the current segmentation be \(s(w_i)=(u_{i1},\ldots,u_{im_i})\). The weighted frequency of the adjacent pair \((a,b)\) is:

\[
F(a,b)
=
\sum_{i=1}^{M} f_i
\sum_{j=1}^{m_i-1}
\mathbb I(u_{ij}=a,\ u_{i,j+1}=b).
\]

Select the pair with the highest frequency in each round:

\[
(a^*,b^*)=\arg\max_{(a,b)}F(a,b),
\]

And merge all adjacent \(a^*,b^*\) into the new symbol \(a^*b^*\).

## 5. Save merge rank

Assume that in the first three rounds we learned:

```text
u g
u n
h ug
```

The order itself is part of the model:

\[
r(u,g)=0,\quad r(u,n)=1,\quad r(h,ug)=2.
\]

The smaller the rank, the higher the priority. Saving only the last set of occurrences of strings will lose some of the merging order required for BPE encoding.

## 6. Stop condition

Common ways to stop:

- Perform a fixed number of merge operations;
- Reach the target vocabulary size;
- The highest pair frequency is lower than the threshold;
- Adding new tokens no longer brings enough revenue.

If the initial alphabet size is \(|\mathcal A|\), the number of special tokens is \(S\), and \(K\) effective mergers are performed, the ideal vocabulary size is approximately:

\[
|\mathcal V|\approx |\mathcal A|+S+K.
\]

Actual implementation will also be affected by minimum frequency, duplicate tokens, reserved tokens and alphabet coverage.

## 7. Training pseudocode

```python
splits = initialize_as_characters(word_frequencies)
merges = []

while vocabulary_not_large_enough():
    pair_freq = count_weighted_adjacent_pairs(splits)
    best = argmax(pair_freq)
    splits = merge_every_occurrence(splits, best)
    merges.append(best)
```

Simple implementation of scanning the entire corpus in each round is very costly. The actual trainer will cache pair counts and only update the adjacencies affected by this merge.

## 8. Merged frequencies are not final model probabilities

BPE training uses frequency decision merging, but the downstream language model still learns:

\[
p_\theta(t_i\mid t_{<i}).
\]

The tokenizer's merge frequency will not directly become the Transformer's token probability. It only determines how the discrete sequence is constructed.

