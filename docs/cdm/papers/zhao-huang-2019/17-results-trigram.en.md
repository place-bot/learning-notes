# Experiment: trigram result of Table 3

## 1. Complete result

|model| IG top-\(k\) accuracy | IG top-\(k\) F1 |Full feature accuracy|Fully Featured F1|
| --- | ---: | ---: | ---: | ---: |
| LR | 75.3% | 73.1% | 72.5% | 69.4% |
| SVM | 74.9% | 72.0% | 71.3% | 68.3% |
| NB | **85.2%** | **85.6%** | 68.9% | 67.2% |

## 2. Feature selection gain

|model|accuracy gain|F1 gain|
| --- | ---: | ---: |
| LR | +2.8 pp | +3.7 pp |
| SVM | +3.6 pp | +3.7 pp |
| NB | **+16.3 pp** | **+18.4 pp** |

## 3. Three best models under \(n\)-gram

|Feature range|best model| accuracy | F1 |
| --- | --- | ---: | ---: |
| unigram | NB | 84.0% | 84.7% |
| unigram+bigram | NB | 84.6% | 85.2% |
| unigram+bigram+trigram | NB | **85.2%** | **85.6%** |

## 4. Gradual changes

NB accuracy：

\[
84.0
\rightarrow
84.6
\rightarrow
85.2.
\]

NB weighted F1：

\[
84.7
\rightarrow
85.2
\rightarrow
85.6.
\]

The total change is:

\[
+1.2\text{ pp accuracy},
\qquad
+0.9\text{ pp F1}.
\]

## 5. LR and SVM

The best accuracy of LR increases from 74.1% to 75.3%. SVM increases from 74.3% to 74.9%, which is the same in both bigram and trigram configurations.

Both are below the majority class accuracy of 82.7%.

## 6. Explanation of the original text

The author believes that different orders of \(n\)-gram can complement each other:

- unigram represents core words;
- bigram means partial matching;
- trigram means a more complete phrase.

As the feature range expands, the screening stage can select useful signals from a richer set of candidates.

## 7. Strength of evidence

The optimal 85.2% is likely to equal

\[
\frac{69}{81}=85.185\%.
\]

The former configuration 84.6% could not be produced exactly by integer correct numbers on 81 questions, so there is unreported information on rounding, test size, or metric calculation details for different configurations. Even considering the table to be accurate to one decimal place, 0.6 pp is less than the single question resolution.

## 8. More robust comparison method

To record question-by-question predictions for the same test question, use:

- McNemar test；
- paired bootstrap；
- repeated splits；
- Mean and standard deviation for each division.

These analyzes are not provided in the original article.
