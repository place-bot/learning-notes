# BPE encoding: merge by Merge Rank

## 1. What things are fixed after training is completed?

A merge-based BPE tokenizer requires at least:

- normalization and pre-tokenization rules;
- initial alphabet;
- Sequential merge list;
- vocabulary from token to ID;
- special-token configuration.

When encoding new text, the pair frequency is no longer recalculated, but the merge rank obtained by training is checked.

## 2. Encoding algorithm

Assume that the pre-sliced fragment has become the initial symbol sequence \(s=(s_1,\ldots,s_m)\). Each round:

1. Enumerate all current adjacent pairs;
2. Find the rank of each pair;
3. Select the mergeable pair with the smallest rank;
4. Merge all non-overlapping occurrences of it;
5. Stop when no pairs appear in the merge table.

\[
(a^*,b^*)
=
\arg\min_{(a,b)\in\operatorname{Pairs}(s)}r(a,b).
\]

## 3. A simple example

The merge list is:

```text
rank 0: u + g  → ug
rank 1: h + ug → hug
rank 2: hug + s → hugs
```

Enter `hugs`:

```text
h u g s
→ h ug s       # rank 0
→ hug s        # rank 1
→ hugs         # rank 2
```

If `hug + s` is not in the merge list, the encoding will stop at `hug | s`.

## 4. Why can’t we just do the longest match?

Let vocabulary also contain:

```text
a, b, c, ab, bc
```

The longest prefix algorithm starts from `abc` and will take `ab | c`. BPE If the merge rank stipulates that `b+c` is earlier than `a+b`, it is possible to get `a | bc`.

BPE encoding is constrained by merge history; WordPiece’s classic encoding does longest-match-first directly based on the final vocabulary. This is an important difference between the two in the reasoning stage.

## 5. Tie-breaking must be stable

If multiple pairs have the same frequency during training, which one to choose will change the subsequent merge history. Implementations may break ties by first occurrence, lexicographic order, internal heap order, or explicit rules.

Recurring tokenizer cannot just save:

```text
vocab size = 30,000
algorithm = BPE
```

Training corpus order, normalizer, pre-tokenizer, minimum frequency, special token, alphabet and trainer versions are also required.

## 6. Cache

The same pre-segmented segments appear repeatedly in natural corpus. GPT-2 official encoder uses cache for the BPE result of the fragment:

\[
\text{piece string}\longrightarrow\text{BPE segmentation}.
\]

This only reuses the deterministically encoded result and does not change the tokenization.

## 7. Decoding

Normal character BPE decoding is typically performed:

1. ID is mapped back to token string;
2. Splice tokens;
3. Restore word endings or space marks;
4. Reverse normalization if possible.

If normalization loses capitalization or accents, the final step cannot restore the original text. BPE merge itself is string splicing, which is usually reversible; the irreversibility mostly comes from pre- and post-processing.

