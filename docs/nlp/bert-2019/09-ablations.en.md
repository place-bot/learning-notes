#Ablation: bidirectionality, NSP and model size

## 1. pretraining target ablation

|model| MNLI | QNLI | MRPC | SST-2 | SQuAD F1 |
|---|---:|---:|---:|---:|---:|
| BERT Base | 84.4 | 88.4 | 86.7 | 92.7 | 88.5 |
| No NSP | 83.9 | 84.9 | 86.5 | 92.6 | 87.9 |
| LTR & No NSP | 82.1 | 84.3 | 77.5 | 92.1 | 77.8 |
| LTR + BiLSTM | 82.1 | 84.1 | 75.7 | 91.6 | 84.9 |

Under this recipe:

- Removing NSP will significantly reduce QNLI;
- left-to-right suffers a big loss in token-level QA;
- Temporarily adding BiLSTM during fine-tuning cannot make up for the deep bidirectional pretraining.

## 2. Subsequent corrections to NSP

RoBERTa uses larger data, longer training, dynamic mask and other improvements and removes NSP to achieve stronger results. This shows that BERT's ablation proves that "NSP is helpful under its training control conditions" and does not prove that NSP is required for all bidirectional pretraining.

## 3. Model size

The paper trains multiple sets of layers, hidden dimensions, and heads, and observes that increasing scale brings continuous improvement on tasks such as MNLI, MRPC, and SST-2, even if the downstream data is small. A fully pretrained large representation model can migrate capacity to small tasks through fine-tuning.

## 4. 80/10/10 Ablation

Appendix compares different replacement ratios. Criterion 80/10/10 is overall robust on MNLI, NER, and SST-2; there is little difference across schemes. 80/10/10 is a valid engineering choice, but not the only correct ratio.

## 5. Long training

Base training with 1M steps is still about 1 point higher on MNLI than 500k steps, indicating that the model can still benefit from more pretraining updates.

## 6. Feature-based result

On NER:

- only use embedding:dev 91.0;
- Penultimate level: 95.6;
- Last four layers of splicing: 96.1;
- Full fine-tuning Base: 96.4;
- Full fine-tuning Large: 96.6.

The features captured by different layers are complementary, and fine-tuning is still slightly stronger.

## 7. Dissolving causal boundaries

The scale of pretraining is huge, and rigorous full-factorial experiments are expensive. There are interactions between different objectives, data, and number of training steps; Table 5 alone cannot attribute all of BERT's benefits.
