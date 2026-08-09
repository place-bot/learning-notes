# Experiment result

## 1. GLUE

|model| MNLI m/mm | QNLI | SST-2 | CoLA | MRPC | RTE |average|
|---|---:|---:|---:|---:|---:|---:|---:|
| OpenAI GPT | 82.1/81.4 | 87.4 | 91.3 | 45.4 | 82.3 | 56.0 | 75.1 |
| BERT Base | 84.6/83.4 | 90.5 | 93.5 | 52.1 | 88.9 | 66.4 | 79.6 |
| BERT Large | **86.7/85.9** | **92.7** | **94.9** | **60.5** | **89.3** | **70.1** | **82.1** |

The average column excludes WNLI and differs slightly from the official GLUE score at the time. Each task uses accuracy, F1, Spearman or Matthews correlation, and column values ​​cannot be treated as the same statistic.

## 2. SQuAD 1.1

- BERT Large single model + TriviaQA: test EM 85.1, F1 91.8;
- 7 model ensemble + TriviaQA: EM 87.4, F1 93.2;
- Developing F1 without TriviaQA is only about 0.1–0.4 lower.

Additional TriviaQA data and ensembles should be distinguished from the base single model.

## 3. SQuAD 2.0

BERT Large single model test EM 80.0, F1 83.1, which is 5.1 higher than the previous best F1 listed in the paper.

## 4. SWAG

|model| Test accuracy |
|---|---:|
| ESIM + ELMo | 59.2 |
| OpenAI GPT | 78.0 |
| BERT Large | 86.3 |

The human expert reported in the paper is about 85.0, and 5 people labeled it about 88.0; small sample human estimates need to be compared with caution.

## 5. Why is result important?

The same pretraining encoder achieves strong results in sentence classification, sentence pair inference, common sense selection and token span prediction through very few task heads, supporting the proposition of transferable universal representation.

## 6. Evidence boundaries

- Many results select learning rate/random restart based on the development set;
- Large models are unstable in small data fine-tuning;
- Leaderboard result may contain additional data and ensemble;
- Benchmark improvement is not the same as comprehensive language understanding;
- Datasets may contain shortcuts, annotation biases, and domain restrictions.
