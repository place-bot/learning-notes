# Limitations, subsequent developments and conclusions

## 1. MLM pretraining—use differences

`[MASK]` rarely appears on downstream input; 80/10/10 only mitigates. MLM also only provides direct prediction losses on 15% tokens.

## 2. NSP

Random document negative examples may be too easy, mixing topic identification with sentence continuity. Subsequently, RoBERTa removed NSP, and ALBERT used sentence-order prediction, indicating that there is still room for design of inter-sentence targets.

## 3. Length and cost

The maximum number of learnable positions is 512, and the global attention increases quadratically with the length. BERT Large 340M already required 64 TPU chips to train for about 4 days.

## 4. Encoder-only task boundaries

BERT is good at understanding representation and extraction tasks, and does not natively provide an efficient autoregressive text generation interface. Build tasks typically use decoder-only or encoder–decoder architectures.

## 5. Fine-tuning instability and catastrophic forgetting

Large requires multiple random restarts on small data. Full fine-tuning also requires saving complete parameters for each task; subsequent PEFT methods such as LoRA, adapter, and prompt tuning are used to reduce costs.

## 6. Subsequent important corrections

|work|Main changes|
|---|---|
| RoBERTa |More data, longer training, dynamic mask, and NSP removal|
| ALBERT |Parameter sharing, factorized embedding, SOP|
| SpanBERT |span masking and span boundary|
| ELECTRA |replaced-token detection, improve sample efficiency|
| DistilBERT |distillation compression|
| DeBERTa | disentangled attention |

## 7. Historical contribution

BERT integrates Transformer encoder, MLM, sentence pair input and end-to-end fine-tuning into a unified pretraining paradigm. It advances a large number of NLP tasks from "designing a main network for each task" to "sharing pretraining models + small task heads".

## 8. Conclusion

The key mechanism of BERT is to use input destruction to eliminate bidirectional prediction leakage, and then pretrain the left and right context of each layer into a transferable representation. Its strong experimental results prove that large-scale unlabeled pretraining can significantly reduce downstream architecture engineering, but MLM, NSP, length, cost and full fine-tuning also leave clear problems for subsequent research.
