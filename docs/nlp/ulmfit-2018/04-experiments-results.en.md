# Experiment, ablation and low sample results

## 1. Six classification data sets

|Data set| ULMFiT test error |
|---|---:|
| IMDb | 4.6% |
| TREC-6 | 3.6% |
| AG | 5.01% |
| DBpedia | 0.80% |
| Yelp binary | 2.16% |
| Yelp full | 29.98% |

In most data sets, the paper reduces the relative error by about 18–24% compared to the previous SOTA.

## 2. Low sample

When IMDb and AG only have 100 labels, supervised ULMFiT can match the de novo training using 10×/20× labels; and using unlabeled text in the target domain, it can match the de novo training with 100×/50× label volume.

## 3. pretraining ablation

|settings| IMDb | TREC-6 | AG |
|---|---:|---:|---:|
|No general pretraining| 5.63 | 10.67 | 5.52 |
|WikiText-103 pretraining| 5.00 | 5.69 | 5.38 |

The benefit was particularly pronounced with small TREC-6.

## 4. Target LM fine-tuning

IMDb：

- Without target LM fine-tuning: 6.99;
- Normal full fine-tuning: 5.86;
- + discriminative LR：5.55；
- + Discr + STLR：5.00。

## 5. Classifier fine-tuning

IMDb：

- Train classifier from scratch: 9.93;
- full：6.87；
- full + discriminative：4.57；
- gradual + discriminative + STLR：5.00。

The best local variants differ slightly across different datasets; full ULMFiT is the most stable across tasks, and the paper emphasizes universal accordingly.

## 6. Evidence boundaries

- The main model is one-way AWD-LSTM, and the task focuses on text classification;
- Hyperparameter is mainly adjusted in IMDb;
- The difference in some small test sets is not significant;
- "100×" refers to specific low-sample curve matching and does not mean a fixed 100x label saving for all tasks.
