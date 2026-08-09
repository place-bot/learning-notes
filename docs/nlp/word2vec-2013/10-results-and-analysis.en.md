# Experimental results and evidence analysis

## 1. Table 2: Data and dimensions must expand together

The accuracy rates on CBOW and 30K vocabulary subsets are as follows:

|Dimensions/training tokens| 24M | 49M | 98M | 196M | 391M | 783M |
|---:|---:|---:|---:|---:|---:|---:|
| 50 | 13.4 | 15.7 | 18.6 | 19.1 | 22.5 | 23.2 |
| 100 | 19.4 | 23.1 | 27.8 | 28.7 | 33.4 | 32.2 |
| 300 | 23.2 | 29.2 | 35.3 | 38.6 | 43.7 | 45.9 |
| 600 | 24.0 | 30.1 | 36.5 | 40.8 | 46.6 | 50.4 |

### 1.1 Look at the data volume horizontally

Fixed 600 dimensions, expanded from 24M to 783M, and the accuracy increased from 24.0% to 50.4%. More corpus continues to provide benefits.

### 1.2 Look at the dimensions vertically

Fixed 783M, expanded from 50 dimensions to 600 dimensions, and the accuracy increased from 23.2% to 50.4%. High-dimensional spaces provide more representation capacity for multiple relationships.

### 1.3 Diminishing Returns

When lower dimensions are fixed, the benefits of continuing to add data will become smaller; when smaller data are fixed, expanding dimensions will quickly saturate. Based on this, the author proposes that \(T\) and \(D\) should be increased together.

The 32.2% of 100 dimensions and 783M is slightly lower than the 33.4% of 391M, indicating that the result of a single training is not strictly monotonic, and also indicates the existence of randomness and optimization fluctuations. The original article did not report replicate experimental variability.

## 2. Table 3: Architecture comparison

All models use 320M training words, 82K vocabulary and 640-dimensional vectors:

|Architecture|Semantic accuracy|syntactic accuracy| MSR test |
|---|---:|---:|---:|
| RNNLM | 9 | 36 | 35 |
| NNLM | 23 | 53 | 47 |
| CBOW | 24 | **64** | **61** |
| Skip-gram | **55** | 59 | 56 |

### 2.1 The semantic advantages of Skip-gram

Skip-gram's semantic accuracy is 55%, which is 31 percentage points higher than CBOW's 24%. Predicting nearby words one by one, large windows, and finer-grained training pairs may preserve more semantic co-occurrence information.

### 2.2 Syntactic advantages of CBOW

CBOW was highest on both syntax tests. Contextual aggregation forms stable signals for local morphological and syntactic patterns.

### 2.3 Simplified model exceeds complex baseline

Both new models outperform NNLM and RNNLM on several metrics. Table 3 is a key comparison in the paper that supports "simple architecture can learn better vocabulary expressions".

## 3. Table 4: Comparison with public word vectors

|model|Dimensions|training tokens|Semantics|syntax|Overall|
|---|---:|---:|---:|---:|---:|
| Collobert–Weston NNLM | 50 | 660M | 9.3 | 12.3 | 11.0 |
| Turian NNLM | 50 | 37M | 1.4 | 2.6 | 2.1 |
| Turian NNLM | 200 | 37M | 1.4 | 2.2 | 1.8 |
| Mnih NNLM | 50 | 37M | 1.8 | 9.1 | 5.8 |
| Mnih NNLM | 100 | 37M | 3.3 | 13.2 | 8.8 |
| Mikolov RNNLM | 80 | 320M | 4.9 | 18.4 | 12.7 |
| Mikolov RNNLM | 640 | 320M | 8.6 | 36.5 | 24.6 |
| Huang NNLM | 50 | 990M | 13.3 | 11.6 | 12.3 |
|Author NNLM| 20 | 6B | 12.9 | 26.4 | 20.3 |
|Author NNLM| 50 | 6B | 27.9 | 55.8 | 43.2 |
|Author NNLM| 100 | 6B | 34.2 | **64.5** | 50.8 |
| CBOW | 300 | 783M | 15.5 | 53.1 | 36.1 |
| Skip-gram | 300 | 783M | **50.0** | 55.9 | **53.3** |

Skip-gram has the highest overall accuracy of 53.3%; the 100-dimensional NNLM syntax accuracy on the author's 6B data has the highest accuracy of 64.5%.

This table changes the corpus, dimensions and structure at the same time. It supports that "the new model is competitive within realistic budgets" and cannot attribute the entire difference to the architecture itself.

## 4. Table 5: More new data is better than repeating smaller corpus

|model|Dimensions|training tokens|Semantics|syntax|Overall|time/day|
|---|---:|---:|---:|---:|---:|---:|
| 3 epoch CBOW | 300 | 783M | 15.5 | 53.1 | 36.1 | 1.0 |
| 3 epoch Skip-gram | 300 | 783M | 50.0 | 55.9 | 53.3 | 3.0 |
| 1 epoch CBOW | 300 | 783M | 13.8 | 49.9 | 33.6 | 0.3 |
| 1 epoch CBOW | 300 | 1.6B | 16.1 | 52.6 | 36.1 | 0.6 |
| 1 epoch CBOW | 600 | 783M | 15.4 | 53.3 | 36.2 | 0.7 |
| 1 epoch Skip-gram | 300 | 783M | 45.6 | 52.2 | 49.2 | 1.0 |
| 1 epoch Skip-gram | 300 | 1.6B | 52.2 | 55.1 | 53.8 | 2.0 |
| 1 epoch Skip-gram | 600 | 783M | **56.7** | 54.5 | **55.5** | 2.5 |

### 4.1 CBOW

- 783M × 3 epoch：36.1%；
- 1.6B × 1 epoch: 36.1%, time dropped from 1 day to 0.6 days;
- 783M, 600 dimensions × 1 epoch: 36.2%, about 0.7 days.

### 4.2 Skip-gram

- 783M × 3 epoch：53.3%；
- 1.6B × 1 epoch: 53.8%, time dropped from 3 days to 2 days;
- 783M, 600 dimensions × 1 epoch: 55.5%, about 2.5 days.

For this corpus and evaluation set, increasing data coverage or dimensionality is more efficient than repeating the same corpus.

## 5. Table 6: Distributed result of 6B data

|model|Dimensions|training tokens|Semantics|syntax|Overall|Number of days × CPU cores|
|---|---:|---:|---:|---:|---:|---:|
| NNLM | 100 | 6B | 34.2 | 64.5 | 50.8 | 14 × 180 |
| CBOW | 1000 | 6B | 57.3 | **68.9** | 63.7 | 2 × 140 |
| Skip-gram | 1000 | 6B | **66.1** | 65.1 | **65.6** | 2.5 × 125 |

### 5.1 Accuracy

Skip-gram reaches 65.6% overall, and CBOW reaches 63.7%, which are significantly higher than 50.8% of 100-dimensional NNLM.

### 5.2 Time

About 14 days for NNLM and 2–2.5 days for new models. The vector dimensions are not the same: the new model uses 1,000 dimensions, the NNLM only has 100 dimensions, because the authors judged that a 1,000-dimensional NNLM would take too long to train.

Therefore, the result reflects the model that can be completed in the same real-world computing environment, rather than a pure architectural comparison of the same dimension.

## 6. Table 7: Sentence completion

|method|Accuracy|
|---|---:|
| 4-gram | 39.0 |
| Average LSA similarity | 49.0 |
| Log-bilinear model | 54.8 |
| RNNLMs | 55.4 |
| Skip-gram | 48.0 |
| Skip-gram + RNNLMs | **58.9** |

Skip-gram alone is 48.0%, lower than LSA and language model. The weighted combination with RNNLM reaches 58.9%, exceeding the previous 55.4%.

This result illustrates that word vector scores provide complementary information to RNNLM. It does not prove that Skip-gram alone has stronger sentence modeling capabilities because Skip-gram lacks complete word order and long-distance structure.

## 7. The most powerful conclusion of the paper

Based on Table 2–7, the evidence supports:

1. When the amount of data and vector dimensions increase together, the accuracy of the analogy increases significantly;
2. CBOW and Skip-gram achieve strong representation quality with low single-step cost;
3. Skip-gram is stronger in the semantic analogy of this article, and CBOW is stronger in several syntactic tests;
4. The simplified structure makes training of billions of tokens and thousands of dimensional vectors a reality;
5. Word vector signals can be complementary to language models.

## 8. Parts not covered by the evidence

The paper does not provide:

- Mean and standard deviation of multiple random seeds;
- Statistical significance test;
- Strictly match architectural ablation of FLOPs;
- Multi-language and low-resource corpus experiments;
- System’s suite of downstream tasks;
- Fairness, bias and privacy analysis;
- Training energy consumption reporting in the modern sense.

These gaps do not weaken its historical contribution, but they limit the scope to which experimental conclusions can be extrapolated.

## 9. How to pronounce "higher accuracy, lower cost"

The core advantage of the paper comes from the end-to-end system design: low \(Q\) allows for larger \(T\) and \(D\). The experimental results compare representations that can be trained under real-world resources. If the goal is to identify the causal effects of the architecture itself, it should be further fixed:

\[
T,D,V,E,\text{optimizer},\text{parameter count},\text{FLOPs},
\]

and perform multiple random repetitions.

## 10. Final experimental judgment

The paper successfully proved a very important engineering-statistical proposition at the time: for vocabulary representation learning, direct local prediction targets combined with extremely low single-step costs can transform large-scale data into stronger geometric laws. The result does not indicate that complex sequence models lose value; Table 7 instead shows that the combination of word vectors and RNNLM is the best.
