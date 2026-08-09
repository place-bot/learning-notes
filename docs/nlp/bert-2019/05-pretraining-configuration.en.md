# pretraining data, configuration and optimization

## 1. Corpus

|corpus|scale|
|---|---:|
| BooksCorpus |About 800 million words|
| English Wikipedia |About 2.5 billion words|
|total|About 3.3 billion words|

Wikipedia keeps only text paragraphs and ignores lists, tables, and headings.

## 2. Training length

Total 1,000,000 steps, batch 256 sequence:

- Maximum length of first 90% steps 128;
- Maximum length for last 10% step is 512.

The last 10% is used to learn long position embeddings. A full-length batch is equivalent to

\[
256\times512=131{,}072
\]

token, the paper is approximately written in 128k words/batch.

## 3. Optimizer

- Adam with weight decay；
- learning rate \(10^{-4}\)；
- \(\beta_1=0.9,\beta_2=0.999\)；
- \(L_2\) weight decay 0.01；
- First 10,000 steps warmup;
-Linear decay afterwards;
- dropout 0.1；
- GELU activation.

## 4. Hardware and time

Appendix to the paper:

- Base: 4 Cloud TPU, total 16 TPU chips;
- Large: 16 Cloud TPU, total 64 TPU chips;
- Pretraining for both is about 4 days.

## 5. Initialization and structure

All layer FFN dimensions are \(4H\). BERT continues the multi-head attention, residual and LayerNorm of the original Transformer encoder, using learnable positional embedding and GELU.

## 6. fine-tuning suggestions

GLUE uses batch 32, 3 epochs, from

\[
\{5,4,3,2\}\times10^{-5}
\]

Select learning rate. Large has instability on small data sets, and the paper uses multiple random restarts and selects by development set.

## 7. pretraining and fine-tuning checkpoint

Each downstream task is initialized from the same pretraining weights and subsequently forms an independent fine-tuning model. Today, PEFT methods such as LoRA can also be used to replace the full fine-tuning of the original paper, but this is a subsequent adaptation strategy.
