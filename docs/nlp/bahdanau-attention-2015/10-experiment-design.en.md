# Experimental design, data and training configuration

The paper compares fixed vector RNN Encoder–Decoder, RNNsearch and the statistical machine translation system Moses on the WMT 2014 English to French translation task.

## 1. Data source

|corpus|scale|
|---|---:|
| Europarl |About 61 million words|
| News Commentary |About 5.5 million words|
| UN |About 421 million words|
|Two parts web-crawled news|About 90 million vs. 272.5 million words|
|total|About 850 million words|

After the papers were filtered using the data selection method of Cho et al. (2014), the neural model training data was approximately 348 million words.

## 2. Data partitioning

- Development set: news-test2012 and news-test2013;
- test set: news-test2014, 3003 sentences in total;
- tokenization: Moses tokenizer;
- No lowercasing or stemming.

## 3. Vocabulary and length

The most frequent 30,000 words are retained at both the English and French ends, and other words are mapped to \([UNK]\). Train models with maximum sentence lengths of 30 and 50 respectively:

|model|Maximum training sentence length|Dynamic attention|
|---|---:|---|
| RNNencdec-30 | 30 |No|
| RNNsearch-30 | 30 |Yes|
| RNNencdec-50 | 50 |No|
| RNNsearch-50 | 50 |Yes|
| RNNsearch-50* | 50 |Yes, train longer|

“30/50” describes the maximum sentence length included during training, and does not mechanically truncate the test sentences to this length.

## 4. Model size

|Configuration|numerical value|
|---|---:|
|Hidden state| 1000 |
|word embedding| 620 |
| maxout | 500 |
| alignment hidden | 1000 |
| batch size | 80 |

RNNsearch uses a bidirectional encoder, and a single annotation is 2000 dimensions. Fixed vector baselines share much of the training setup with attention models, but the architectural capacity and information paths are not exactly the same.

## 5. Optimization details

- Adadelta：\(\rho=0.95,\epsilon=10^{-6}\)；
- Global gradient norm is clipped to 1;
- Fetch 1600 sentence pairs every 20 updates and sort them by length;
- Divide into 20 mini-batches of size 80;
- Circular matrix orthogonal initialization;
- Alignment projection standard deviation \(0.001\), most other matrices standard deviation \(0.01\).

Sorting by length can reduce batch padding and increase the effective computing ratio of the GPU at that time.

## 6. Actual training volume

|model|Update times| epoch |hours| GPU |Training NLL|Develop NLL|
|---|---:|---:|---:|---|---:|---:|
| RNNencdec-30 | \(8.46\times10^5\) | 6.4 | 109 | TITAN BLACK | 28.1 | 53.0 |
| RNNencdec-50 | \(6.00\times10^5\) | 4.5 | 108 | Quadro K-6000 | 44.0 | 43.6 |
| RNNsearch-30 | \(4.71\times10^5\) | 3.6 | 113 | TITAN BLACK | 26.7 | 47.2 |
| RNNsearch-50 | \(2.88\times10^5\) | 2.2 | 111 | Quadro K-6000 | 40.7 | 38.1 |
| RNNsearch-50* | \(6.67\times10^5\) | 5.0 | 252 | Quadro K-6000 | 36.7 | 35.2 |

The advantages of the asterisk version include the benefits of longer training. Different GPUs and training steps also prevent wall-clock time from being directly compared to pure architecture speed.

## 7. Moses comparison

The paper uses the powerful Moses phrase-based SMT system. Moses also used about 418 million words of monolingual corpus to train the language model, and the neural model did not use these additional monolingual data. This difference must be preserved when interpreting system-level BLEU.

## 8. Evaluation indicators

The main metric is BLEU. The paper also reports:

- Complete test set All;
- No-UNK subset without unknown words.

BLEU aggregates n-gram precision with a length penalty, a measure of the apparent overlap between the system translation and the reference translation. It does not directly measure human acceptability, alignment quality, or semantic correctness of each sentence.

## 9. Questions that experiments can answer

Key design inspections:

1. Can dynamic context be better than fixed vector;
2. Whether the advantage becomes more obvious as the sentence length increases;
3. Whether the learned weights form interpretable soft alignment;
4. Can the neural system approach a strong SMT baseline using additional monolingual corpus.

## 10. Evidence boundaries

The experiment only has one language direction: English and French, and the paper does not report multiple random seeds, confidence intervals or significance tests. There are also differences in bidirectional encoder, dynamic context and training time between models. Therefore, result strongly supports the entire RNNsearch architecture and cannot accurately allocate all gains to a single component.
