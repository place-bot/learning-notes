# BLEU result and length analysis

## 1. Main result

|system| All BLEU | No-UNK BLEU |
|---|---:|---:|
| RNNencdec-30 | 13.93 | 24.19 |
| RNNsearch-30 | 21.50 | 31.44 |
| RNNencdec-50 | 17.82 | 26.71 |
| RNNsearch-50 | 26.75 | 34.16 |
| RNNsearch-50* | 28.45 | **36.15** |
| Moses | **33.30** | 35.63 |

## 2. Pairing gain

Under the same maximum training length:

\[
21.50-13.93=7.57
\]

It is the improvement of the 30-word model on the complete test set;

\[
26.75-17.82=8.93
\]

It is an improvement of the 50-word model.

The No-UNK subset is correspondingly promoted to

\[
31.44-24.19=7.25,
\qquad
34.16-26.71=7.45.
\]

RNNsearch-50*, which is trained longer, is 10.63 BLEU higher on All and 9.44 higher on No-UNK than RNNencdec-50.

## 3. Comparison with Moses

On the complete test set, Moses' 33.30 is still higher than RNNsearch-50*'s 28.45, with a difference of 4.85. On the No-UNK subset, RNNsearch-50*’s 36.15 is slightly higher than Moses’ 35.63.

This shows that closed vocabulary was an important shortcoming of the nervous system at that time. The No-UNK subset eliminates many non-vocabulary problems and also changes the composition of the test sample, so it cannot be claimed that the neural system has surpassed Moses on the complete task.

## 4. Sentence length analysis

The papers are grouped by source sentence length to draw the BLEU curve:

- The fixed vector RNNencdec decreases significantly as the length increases;
- RNNsearch’s curve is more stable;
- RNNsearch-30 can still outperform RNNencdec-50 on long sentences.

This last point is critical: increasing the training sentence length of fixed vector models does not eliminate the bottleneck. The changes in information paths brought about by dynamic access to source annotations are more effective than simply letting the baseline see longer training sentences.

## 5. Why dynamic context is good for long sentences

Fixed vectors require that all source information pass through a single \(\mathbf c\). RNNsearch builds a shorter path for each target word:

\[
\mathbf h_j
\longrightarrow
\alpha_{ij}
\longrightarrow
\mathbf c_i
\longrightarrow
y_i.
\]

When the source sentence becomes longer, the target word can still directly access the annotation at the corresponding position, without relying on a fixed vector to completely preserve all the details.

## 6. NLL and BLEU

The training/development NLL and BLEU in the table measure different things:

- NLL measures the probability assigned by the model to the reference target sequence;
- BLEU measures the n-gram overlap of the search translation with the reference translation.

Probabilistic modeling, search strategies, length preferences, and \([UNK]\) all influence the relationship. Lower development NLL generally favors BLEU, but there is no strict one-to-one correspondence.

## 7. Conclusion Strength

result directly supports:

- RNNsearch overall is significantly better than the fixed vector baseline in the paper;
- The advantage is especially obvious in long sentences;
- Questions outside the vocabulary limit the performance of the complete test set.

result has not been isolated yet:

- How much does the two-way encoder contribute alone;
- How much attention contributes alone;
- How much longer training contributes to the star model;
- The range of gain under random seed changes.

## Summary of this page

The most convincing evidence consists of three parts: the paired BLEU is improved, the length curve is more stable, and long sentence translation examples retain more details. Together they point to the limitations of fixed vector information paths.
