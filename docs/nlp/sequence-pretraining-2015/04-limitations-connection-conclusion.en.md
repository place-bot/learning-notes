# Limitations, BERT interface and conclusions

## 1. Limitations

- One-way LSTM and final state bottleneck;
- sequence autoencoder is expensive to reconstruct very long documents;
- truncated BPTT limits the distal gradient;
- Word-level vocabulary and OOV;
- No unified large-scale general pretraining checkpoint;
- The main task is document classification;
- The learning rate and freezing strategy of pretrain/fine-tune are not yet mature.

## 2. From this article to ULMFiT

ULMFiT retains language model pretraining and target fine-tuning, further:

- Use large-scale universal WikiText-103 pretraining;
- Do LM fine-tuning of the target domain first;
- Use discriminative LR, STLR and gradual unfreezing;
- Provide a more versatile and stable classification process.

## 3. From this article to BERT

BERT replaces LSTM with a bidirectional Transformer encoder, replaces the next-token target with MLM, and expands it to unify sentence pairs, tokens and span tasks. The common paradigm remains:

\[
\text{Unlabeled prediction task}
\rightarrow
\text{Parameter initialization}
\rightarrow
\text{Supervision task fine-tuning}.
\]

## 4. Conclusion

Dai and Le's experiments clearly show that parameters learned from unlabeled sequence targets can improve the stability and generalization of supervised LSTM. The value of pretraining extends beyond static word vectors to the entire sequence model.
