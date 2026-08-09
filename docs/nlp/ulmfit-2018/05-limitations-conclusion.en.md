# Limitations, BERT/LoRA interface and conclusion

## 1. Limitations

- One-way LSTM cannot fuse the left and right contexts at the same layer like BERT;
- Mainly verify text classification;
- Long documents rely on truncated BPTT;
- Three-stage training and multiple dropout/LR strategies are complex;
- Each task still generates complete fine-tuning parameters;
- Tokenizer and word-level LM have OOV limitations.

## 2. With BERT

BERT extends the general pretraining-target fine-tuning paradigm embodied in ULMFiT to Transformer encoder, and uses MLM to obtain deep bidirectional representation. BERT's downstream configuration is more unified, usually with full fine-tuning.

## 3. With LoRA

ULMFiT studies how to stably update different layers; LoRA studies how to represent updates with low-rank parameters. Modern training can be combined with:

\[
\text{layer-wise schedule}
\quad+\quad
\text{parameter-efficient update}.
\]

However, the optimal learning rate level of LoRA parameters may not necessarily copy the 2.6 ratio of ULMFiT.

## 4. The precise meaning of “Fine-tuning”

Starting from the pretraining parameters, continue optimization with the target data. Possible updates:

- all parameters;
- partial layer;
- bias；
- adapter；
- prompt；
- LoRA low-rank delta.

The ULMFiT main method updates the gradually unfrozen complete LM; LoRA is a later parameter-efficient fine-tuning.

## 5. Conclusion

ULMFiT proves that the fine-tuning strategy will substantially affect the migration effect. The pretraining checkpoint is just the starting point; the learning rate, hierarchical update sequence, target domain adaptation and classification readout jointly determine whether general knowledge can be retained and the target task can be learned.
