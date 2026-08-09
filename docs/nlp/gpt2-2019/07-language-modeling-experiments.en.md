# Language modeling experiments and scale effects

## 1. Experimental design

The authors trained four model sizes with approximately log-uniform distribution. The learning rate of each model is manually adjusted according to the WebText 5% set perplexity. The report states that all models are still underfitting WebText, and training and leaving perplexity will improve as they continue training.

A key limitation of language modeling transfer is that tokenizers are different. GPT-2 directly models byte-level BPE tokens, while many benchmarks have gone through forced lowercase, PTB tokenization, sentence shuffling, or UNK replacement. The author uses a reversible detokenizer to recover the text as much as possible, and then calculates the log probability of the target data.

## 2. Evaluation indicators

### 2.1 Perplexity

If words are used as the normative unit, the average negative log likelihood is

\[
\operatorname{NLL}
=
-\frac{1}{N}\sum_{t=1}^{N}\log p(x_t\mid x_{<t}),
\]

perplexity is

\[
\operatorname{PPL}=\exp(\operatorname{NLL}).
\]

The lower the PPL, the better.

### 2.2 Bits per byte / character

\[
\operatorname{BPB}
=
-\frac{1}{N_{\mathrm{byte}}}
\sum_t\log_2 p(x_t\mid x_{<t}).
\]

Models with different tokenizations can be normalized by byte or character, but text preprocessing will still affect comparability.

## 3. The core result of Table 3 of the paper

|Datasets/Metrics|SOTA listed at that time| 117M | 345M | 762M | 1542M |
|---|---:|---:|---:|---:|---:|
| LAMBADA PPL ↓ | 99.8 | 35.13 | 15.60 | 10.87 | **8.63** |
| LAMBADA Acc ↑ | 59.23 | 45.99 | 55.48 | 60.12 | **63.24** |
| CBT-CN Acc ↑ | 85.7 | 87.65 | 92.35 | **93.45** | 93.30 |
| CBT-NE Acc ↑ | 82.3 | 83.4 | 87.1 | 88.0 | **89.05** |
| WikiText-2 PPL ↓ | 39.14 | 29.41 | 22.76 | 19.93 | **18.34** |
| PTB PPL ↓ | 46.54 | 65.85 | 47.33 | 40.31 | **35.76** |
| enwik8 BPB ↓ | 0.99 | 1.16 | 1.01 | 0.97 | **0.93** |
| text8 BPC ↓ | 1.08 | 1.17 | 1.06 | 1.02 | **0.98** |
| WikiText-103 PPL ↓ | 18.3 | 37.50 | 26.37 | 22.05 | **17.48** |
| 1BW PPL ↓ | 21.8 | 75.20 | 55.72 | 44.575 | **42.16** |

Among the 8 major language modeling data sets counted in the paper, 7 of the largest models reached the zero-sample SOTA at the time; 1BW was the obvious exception.

## 4. Why 1BW performs poorly

One Billion Word Benchmark is larger and pre-processing disrupts the sentence order. The cross-sentence and long-distance structures learned by GPT-2 from WebText cannot be fully utilized on this benchmark; strong preprocessing also causes domain and tokenization shifts.

Therefore, the model's advantages on natural documents are not guaranteed to transfer to highly normalized distributions where sentence order is destroyed.

## 5. LAMBADA

To predict the last word of a paragraph, LAMBADA usually requires at least about 50 token context. The original prediction of the largest model is often a reasonable continuation, but it may not be a legal word at the end of the sentence. After the author added approximate stop-word filtering, the accuracy increased from 52.66% discussed in the article to 63.24%, exceeding the result at that time.

This means that the result also contains:

- Long-range condition capabilities of the model;
- Artificial constraints on task output space;
- Differences between review format and natural generation.

## 6. CBT

Children’s Book Test requires filling in the gaps among 10 candidate words. The largest model achieves 93.3% on common nouns and 89.1% on named entities. Since one of the test books, "The Jungle Book", appears in WebText, there is no significantly overlapping validation result in the revised paper.

## 7. How to interpret the scale curve

Multiple tasks improve with model size, supporting "capacity helps implicit task learning". However, there are only four points, and the architecture depth, width, learning rate and training dynamics change at the same time. It shows an empirical trend and is not a strictly fitting scaling law in the later sense.

A more secure conclusion is that on this set of training configurations and data, scaling up decoder-only LM generally improves both WebText modeling and multiple zero-shot transfer metrics.
