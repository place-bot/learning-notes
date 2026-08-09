#Basic model experiment and evidence analysis

## 1. Evaluation Group

The paper summarizes the standard benchmarks as:

- Code: pass@1 for HumanEval and MBPP;
- Commonsense：PIQA、SIQA、HellaSwag、WinoGrande、ARC、OpenBookQA、CommonsenseQA；
- World Knowledge：NaturalQuestions、TriviaQA；
- Reading Comprehension：SQuAD、QuAC、BoolQ；
- Math: GSM8K and MATH;
- MMLU、BBH、AGI Eval。

Different groups use 0-shot, 3-shot, 4-shot, 5-shot, 7-shot or 8-shot. Each column in the table is not of the same data size and difficulty.

## 2. Summarize results

|model| Code | Commonsense | World Knowledge | Reading | Math | MMLU | BBH | AGI Eval |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Llama 1 7B | 14.1 | 60.8 | 46.2 | 58.5 | 6.95 | 35.1 | 30.3 | 23.9 |
| Llama 2 7B | 16.8 | 63.9 | 48.9 | 61.3 | 14.6 | 45.3 | 32.6 | 29.3 |
| Llama 1 13B | 18.9 | 66.1 | 52.6 | 62.3 | 10.9 | 46.9 | 37.0 | 33.9 |
| Llama 2 13B | 24.5 | 66.9 | 55.4 | 65.8 | 28.7 | 54.8 | 39.4 | 39.1 |
| Llama 1 65B | 30.7 | 70.7 | 60.5 | 68.6 | 30.8 | 63.4 | 43.5 | 47.6 |
| Llama 2 70B | **37.5** | **71.9** | **63.6** | **69.4** | **35.2** | **68.9** | **51.2** | **54.2** |

Llama 2 is generally better than Llama 1 at similar scales, indicating that more training tokens, data updates, 4K context and architecture adjustments are jointly effective.

## 3. Comparison with the open model at that time

The paper will be re-evaluated internally by MPT and Falcon, and the higher of the internal result and the public result will be chosen. Llama 2 70B outperforms the listed open base models in summary tables; 7B and 34B also generally outperform adjacent scale Falcons, with the exception of code benchmarks.

## 4. Comparison with closed source model

| Benchmark | GPT-3.5 | GPT-4 | PaLM | PaLM-2-L | Llama 2 70B |
|---|---:|---:|---:|---:|---:|
| MMLU 5-shot | 70.0 | 86.4 | 69.3 | 78.3 | 68.9 |
| TriviaQA 1-shot | — | — | 81.4 | 86.1 | 85.0 |
| Natural Questions 1-shot | — | — | 29.3 | 37.5 | 33.0 |
| GSM8K 8-shot | 57.1 | 92.0 | 56.5 | 80.7 | 56.8 |
| HumanEval 0-shot | 48.1 | 67.0 | 26.2 | — | 29.9 |
| BBH 3-shot | — | — | 52.3 | 65.7 | 51.2 |

Llama 2 70B is close to the MMLU/GSM8K of GPT-3.5, obviously lagging behind GPT-4, and there is also a large gap in code tasks.

## 5. Security benchmark: base model

| Base model | TruthfulQA ↑ | ToxiGen ↓ |
|---|---:|---:|
| Llama 1 7B | 27.42 | 23.00 |
| Llama 2 7B | 33.29 | 21.25 |
| Llama 2 13B | 41.86 | 26.10 |
| Llama 2 34B | 43.45 | 21.19 |
| Llama 2 70B | 50.18 | 24.60 |

Truthfulness generally improves with larger base models, and toxicity does not decrease monotonically with size. The base model of the 70B still needs safety tuning.

## 6. Compare boundaries

- The benchmark comes from different documents, and the prompt and implementation may be different;
- Optimal selection of internal framework reruns and public figures will bring selection advantages;
- Closed source model versions may change over time;
- Group averaging masks subtask differences;
- Unequal training data size, permissions, context and computation;
- Data contamination can only do partial auditing.

These tables support Llama 2 base competitiveness and are not a substitute for mission-level, deployment-level assessments.
