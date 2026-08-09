# Experiment: unigram+bigram result of Table 2

## 1. Feature changes

After adding two adjacent words, the candidate vocabulary is significantly expanded. The paper does not report the exact dimensions, only that more than 90% of the features appear in less than 5 questions.

## 2. Complete result

|model| IG top-\(k\) accuracy | IG top-\(k\) F1 |Full feature accuracy|Fully Featured F1|
| --- | ---: | ---: | ---: | ---: |
| LR | 74.6% | 72.5% | 72.7% | 69.7% |
| SVM | 74.9% | 72.0% | 71.1% | 68.1% |
| NB | **84.6%** | **85.2%** | 69.1% | 67.3% |

## 3. Feature selection gain

|model|accuracy gain|F1 gain|
| --- | ---: | ---: |
| LR | +1.9 pp | +2.8 pp |
| SVM | +3.8 pp | +3.9 pp |
| NB | **+15.5 pp** | **+17.9 pp** |

## 4. Compare with unigram

### With feature selection

|model| unigram accuracy | +bigram accuracy |change|
| --- | ---: | ---: | ---: |
| LR | 74.1% | 74.6% | +0.5 pp |
| SVM | 74.3% | 74.9% | +0.6 pp |
| NB | 84.0% | 84.6% | +0.6 pp |

The three types of models all improved by 0.5--0.6 percentage points.

### No feature selection

- LR：72.5% \(\rightarrow\) 72.7%；
- SVM：71.1% \(\rightarrow\) 71.1%；
- NB：21.3% \(\rightarrow\) 69.1%。

The large recovery in NB illustrates that the feature space changes the behavior of Gaussian density estimation, but 69.1% is still lower than the majority class baseline.

## 5. Information brought by bigram

Adjacent phrases can express:

- Computational actions;
- Quantitative relationship;
- Chart reading tips;
- Inference sentence structure;
- Question templates.

These local phrases have additional discriminating power for O/M.

## 6. Scale of result difference

If the test set has about 81 questions, 0.6 percentage points are smaller than the corresponding value of one question.

\[
\frac{1}{81}\times100\%=1.23\%.
\]

Since the tables may be from the same test set but different error combinations, 0.6 pp may still result from rounding. The paper does not have a paired test, so it is impossible to confirm that the small gain of the bigram is stable.

## 7. Conclusion

Table 2 supports:

- bigram may bring a small gain;
- Information gain continues to be effective;
- NB is still the best among the three models.

It provides no evidence of robustness across random partitions.
