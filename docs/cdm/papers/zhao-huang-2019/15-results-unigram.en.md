# Experiment: unigram result of Table 1

## 1. Feature scale

unigram generation

\[
p=2943
\]

features, more than 80% appear in less than 5 questions.

## 2. Complete result

|model| IG top-\(k\) accuracy | IG top-\(k\) F1 |Full feature accuracy|Fully Featured F1|
| --- | ---: | ---: | ---: | ---: |
| LR | 74.1% | 73.5% | 72.5% | 69.5% |
| SVM | 74.3% | 72.8% | 71.1% | 68.1% |
| NB | **84.0%** | **84.7%** | 21.3% | 22.4% |

## 3. Feature selection gain

|model|accuracy gain|F1 gain|
| --- | ---: | ---: |
| LR | +1.6 pp | +4.0 pp |
| SVM | +3.2 pp | +4.7 pp |
| NB | **+62.7 pp** | **+62.3 pp** |

Here `pp` represents percentage points.

## 4. The most striking phenomenon

Gaussian NB is extremely sensitive to high-dimensional noise:

\[
21.3\%
\xrightarrow{\text{IG}}
84.0\%.
\]

LR and SVM have positive improvements with modest magnitudes.

## 5. Why NB’s full feature result is lower than random intuition

Binary classification random guessing often brings to mind 50%, but models can be systematically biased toward the wrong class. Gaussian NB uses 2,943 normal conditional densities on a sparse TF--IDF, where each low-frequency dimension may contribute unstable log likelihood. After multiple small biases accumulate, decisions can be reversed on a large scale.

The paper does not provide a confusion matrix, so the 21.3% error direction cannot be determined.

## 6. Comparison with majority class baseline

Class O account

\[
82.7\%.
\]

Therefore:

- LR 74.1% is lower than most class accuracy;
- SVM 74.3% is lower than most class accuracy;
- NB 84.0% is about 1.3 percentage points higher.

Looking at accuracy alone, only filtered NB exceeds all-O under unigram.

## 7. Supplementary information for F1

NB's F1 84.7% is higher than accuracy 84.0%, indicating that it may identify a part of the minority class M. Accurate judgment still requires each type of precision/recall.

## 8. Conclusion of the paper

The author believes that:

1. Information gain is helpful for all three types of models;
2. All sparse features seriously damage NB;
3. NB is better than LR and SVM under limited training data.

The first two points are directly supported by the table. The third point only holds true for this data partition and the parameters used.
