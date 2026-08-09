# Experimental design and results

## 1. Model and tasks

|model|Task|
|---|---|
| RoBERTa base/large | GLUE |
| DeBERTa XXL 1.5B | GLUE |
| GPT-2 medium/large | E2E、DART、WebNLG |
| GPT-3 175B | WikiSQL、MNLI、SAMSum |

The experiment uses NVIDIA V100; some baseline numbers refer to existing papers, and the author's own runs report mean/range or typical fluctuations.

## 2. GLUE

- RoBERTa base: LoRA 0.3M parameters, average 87.2; full volume 125M, average 86.4;
- RoBERTa large: LoRA 0.8M, average 89.0; full size 355M, average 88.9;
- DeBERTa XXL: LoRA 4.7M, average 91.3; full volume 1.5B, average 91.1.

Metrics for different GLUE subtasks are not exactly the same, and averages are used for summary purposes and are not a substitute for task-by-task reading.

## 3. GPT-2 E2E

|method|GPT-2 M parameters| BLEU |GPT-2 L parameters| BLEU |
|---|---:|---:|---:|---:|
| Full FT | 354.92M | 68.2 | 774.03M | 68.5 |
| LoRA | 0.35M | \(70.4\pm0.1\) | 0.77M | \(70.4\pm0.1\) |

The paper also reports NIST, METEOR, ROUGE-L, CIDEr, and DART/WebNLG results.

## 4. GPT-3

|method|Trainable parameters| WikiSQL | MNLI-m | SAMSum R1/R2/RL |
|---|---:|---:|---:|---:|
| Full FT | 175,255.8M | 73.8 | 89.5 | 52.0/28.0/44.5 |
| LoRA | 4.7M | 73.4 | 91.7 | 53.8/29.8/45.9 |
| LoRA | 37.7M | 74.0 | 91.6 | 53.4/29.2/45.1 |

Increasing the LoRA parameters did not improve each indicator monotonically, indicating that there are also optimization and task matching issues in addition to budget.

## 5. Training and deployment resources

GPT-3 case report training memory is reduced from about 1.2TB to 350GB, training throughput is increased by about 25%, and task checkpoint is about 35MB. Deployments still have to hold a 350GB base; 100 tasks is about the base plus 100 small LoRAs, not 100 copies of the full base.

## 6. Evidence boundaries

- GPT-3 training cost limits complete multi-seed experiments;
- Some baselines come from different papers;
- Test models and tasks are representative of the 2021 environment;
- The result supports parameter efficiency in these scenarios, without proving that low-rank updates are optimal for all tasks, modalities, and training sizes.
