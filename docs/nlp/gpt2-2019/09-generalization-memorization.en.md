# Generalization, memory and data overlap

## 1. Why overlapping auditing is needed

The training set comes from the Internet, and the original text of the benchmark may also be published on the Internet. If test text or near-duplicate text enters WebText, zero-sample results may be mixed with memory effects.

The paper writes this question as: whether a certain evaluation token 8-gram also appears in the WebText training set.

## 2. Bloom filter method

The author first normalizes the string into lowercase alphanumeric words and connects them with single spaces, and then puts the 8-gram of the WebText training set into the Bloom filter.

A Bloom filter may produce false positives, but it will not produce false negatives. The parameters are set so that the theoretical false positive rate is no higher than

\[
10^{-8}.
\]

The author checked with 1 million generated strings and found no false positives.

## 3. Overlap rate of language model benchmark

|test set|Overlaps with itself train|Overlaps with WebText train|
|---|---:|---:|
| PTB | 2.67% | 0.88% |
| WikiText-2 | 0.66% | 1.63% |
| enwik8 | 7.50% | 6.31% |
| text8 | 2.34% | 3.94% |
| WikiText-103 | 9.09% | 2.42% |
| 1BW | 13.19% | 3.75% |

The average overlap between common LM test sets and WebText is about 3.2%; the average overlap between the train/test of these benchmarks is about 5.9%. This shows that overlapping is not unique to WebText, but it does not negate contamination.

## 4. Task analysis

### 4.1 Winograd

Only 10 schemas have 8-gram overlap with WebText; 2 of them are spurious matches, and only 1 of the remaining 8 has context that reveals the answer.

### 4.2 CoQA

About 15% of the news domain documents are already in WebText, and the model is about 3 F1 higher on these documents. Combining the 5 development domains, the authors estimate that the overlap brings about 0.5–1.0 F1. CoQA is released after the WebText time cutoff, so there are no formal training questions and answers in the training corpus.

### 4.3 LAMBADA

The average overlap is about 1.2%. After removing all overlapping examples:

- perplexity changed from 8.6 to 8.7;
- accuracy changed from 63.2% to 62.9%.

The overall change is small because the proportion of significantly overlapping samples is low.

## 5. What does it mean to train and improve with hold-out loss?

The paper shows that as the model increases, WebText train and held-out loss decrease at the same time, and the gap does not show serious expansion. Based on this, the author determines that the maximum GPT-2 is still in an underfitting state.

This evidence reflects a fit at the level of the overall distribution and is not sufficient to exclude individual documents from being memorized verbatim. A model can be overall underfitting while accurately remembering a few high-frequency or repeated segments.

## 6. Method limitations

8-gram overlap can only find superficially identical fragments:

- Adaptations, translations and formatting changes may be missed;
- Common phrases produce harmless matches;
- The appearance of the document does not mean the appearance of the answer;
- The overlap ratio is not directly equivalent to performance expansion;
- WebText is not public and outside researchers cannot review the full index.

The paper recommends using n-gram deduplication as a sanity check in new data set segmentation. GPT-3 extends this problem to 13-gram clean set evaluation and exposes more complex contamination detection challenges in large-scale training.
