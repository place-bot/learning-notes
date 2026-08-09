# Experimental results and migration hand calculation

## 1. Summary

|Data set| SA-LSTM error |Best before|
|---|---:|---:|
| IMDB | 7.24% | 7.42% |
| Rotten Tomatoes | 16.7% |18.5% (similar comparison without additional phrase tags)|
| 20 Newsgroups | 15.6% | 17.1% |
| DBpedia | 1.19% | 1.74% |

## 2. IMDB

|model| Test error |
|---|---:|
| LSTM + tuning/dropout | 13.50% |
|word2vec initialization| 10.00% |
| LM-LSTM | 7.64% |
| SA-LSTM | **7.24%** |
| SA-LSTM joint training | 14.70% |

Pretraining recursive parameters is significantly better than just migrating word vectors.

## 3. External unlabeled data

On Rotten Tomatoes, the error using IMDB unannotated text pretraining SA is 18.6%, and using Amazon reviews drops to 16.7%. More domain-related unlabeled data can compensate for the lack of labels.

## 4. A two-parameter migration example

Let the supervised optimal neighborhood loss be:

\[
L(\theta_1,\theta_2)
=(\theta_1-2)^2+10(\theta_2-1)^2.
\]

The gradient of the random starting point \((0,0)\) is

\[
(-4,-20).
\]

The gradient of the pretraining starting point \((1.8,0.9)\) is

\[
(-0.4,-2).
\]

Pretraining does not change the supervision objective, only changes the initialization, so that the optimization starts from a more favorable area. The real deep network loss is far more complicated. This example only illustrates the parameter initialization mechanism.

## 5. Evidence boundaries

The previous best results for different data sets come from different methods; the paper does not construct a unified large-scale multi-seed comparison. The advantages of SA are also closely related to the difficulty of LSTM long document optimization.
