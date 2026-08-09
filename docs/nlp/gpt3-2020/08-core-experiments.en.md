# Language modeling, question answering, translation and SuperGLUE

## 1. Cloze and completion

|settings| LAMBADA Acc | LAMBADA PPL | StoryCloze Acc | HellaSwag Acc |
|---|---:|---:|---:|---:|
|SOTA at that time| 68.0 | 8.63 | 91.8 | 85.6 |
| GPT-3 zero-shot | 76.2 | 3.00 | 83.2 | 78.9 |
| GPT-3 one-shot | 72.5 | 3.35 | 84.7 | 78.1 |
| GPT-3 few-shot | **86.4** | **1.92** | 87.7 | 79.3 |

LAMBADA few-shot uses the fill-in-the-blank format, allowing the model to only fill in one word. One-shot is lower than zero-shot. The author speculates that one example is not enough for the model to stably recognize the fill-in-the-blank format.

GPT-3 is strong in LAMBADA, but StoryCloze and HellaSwag are still lower than fine-tuned SOTA, indicating that the scale effect has task differences.

## 2. Closed book questions and answers

|method| Natural Questions | WebQuestions | TriviaQA |
|---|---:|---:|---:|
| RAG，fine-tuned + retrieval | 44.5 | 45.5 | 68.0 |
| T5-11B+SSM，closed-book | 36.6 | 44.7 | 60.5 |
| GPT-3 zero-shot | 14.6 | 14.4 | 64.3 |
| GPT-3 one-shot | 23.0 | 25.3 | 68.0 |
| GPT-3 few-shot | 29.9 | 41.5 | **71.2** |

TriviaQA few-shot is strong; Natural Questions still lags significantly behind fine-tuned T5 and retrieval systems. NQ prefers fine-grained Wikipedia knowledge, and parameter memory and extensive pretraining distribution cannot replace precise retrieval.

## 3. Reading Comprehension and Science Questions and Answers

|settings| ARC Easy | ARC Challenge | CoQA F1 | DROP F1 |
|---|---:|---:|---:|---:|
| Fine-tuned SOTA | 92.0 | 78.5 | 90.7 | 89.1 |
| GPT-3 zero-shot | 68.8 | 51.4 | 81.5 | 23.6 |
| GPT-3 one-shot | 71.2 | 53.2 | 84.0 | 34.3 |
| GPT-3 few-shot | 70.1 | 51.5 | 85.0 | 36.5 |

CoQA is close to the human baseline; DROP requires numerical and discrete reasoning. Although the few-shot is higher than the BERT baseline of the original paper, it is still far lower than the system and human performance of the signed module.

## 4. Translation

|settings| En→Fr | Fr→En | En→De | De→En | En→Ro | Ro→En |
|---|---:|---:|---:|---:|---:|---:|
| GPT-3 zero-shot | 25.2 | 21.2 | 24.6 | 27.2 | 14.1 | 19.9 |
| GPT-3 one-shot | 28.3 | 33.7 | 26.2 | 30.4 | 20.6 | 38.6 |
| GPT-3 few-shot | 32.6 | **39.2** | 29.7 | **40.6** | 21.0 | **39.5** |

Translating to English is significantly better than translating from English to other languages, matching 93% of the English training distribution with the English-centric tokenizer. few-shot uses paired translation examples, so it is not strictly equivalent to unsupervised MT with no parallel data at all.

## 5. SuperGLUE

|model|average| BoolQ | CB Acc | COPA | RTE | WiC | WSC | MultiRC F1a | ReCoRD F1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Fine-tuned SOTA | 89.0 | 91.0 | 93.9 | 94.8 | 92.5 | 76.1 | 93.8 | 88.2 | 93.3 |
| Fine-tuned BERT-Large | 69.0 | 77.4 | 75.7 | 70.6 | 71.7 | 69.6 | 64.6 | 70.0 | 72.0 |
| GPT-3 few-shot | **71.8** | 76.4 | 52.0 | 92.0 | 69.0 | 49.4 | 80.1 | 75.4 | 91.1 |

GPT-3 few-shot outperforms fine-tuned BERT-Large on average, but is still below the overall SOTA. There are huge differences between tasks:

- COPA, ReCoRD are close to SOTA;
- WSC, BoolQ, MultiRC, and RTE are close to or exceed some of the BERT-Large indicators;
- WiC is close to random levels;
- CB is inconsistent.

The authors believe that the model is particularly weak on tasks that require comparing two sentences or fragments, which is related to the one-way autoregressive objective and prompt form.

## 6. How to summarize result

GPT-3 few-shot has been able to approach the fine-tuned system in some tasks, but there is no unified lead:

\[
\text{Revenue size}
=
f(\text{task structure},\text{Data coverage},\text{prompt},K,N).
\]

The paper's central evidence is broad scaling trends and fast task switching, rather than a league table that comprehensively overwhelms supervised methods.
