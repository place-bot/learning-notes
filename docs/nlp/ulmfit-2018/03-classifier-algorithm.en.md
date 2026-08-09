# Concat Pooling and classification algorithm

## 1. Why just using the final state is not enough

Discriminators in long documents may appear anywhere. Read only \(h_T\) Early strong signals may be lost.

## 2. Concat pooling

to hidden state

\[
H=\{h_1,\ldots,h_T\},
\]

Splicing

\[
h_c
=
[h_T;\operatorname{maxpool}(H);
\operatorname{meanpool}(H)].
\]

It also retains:

- final sequence status;
- The strongest activation in each dimension;
- Average activation across the entire text.

## 3. Category header

\(h_c\) enters two linear blocks, using batch norm, dropout, ReLU in the middle, and finally softmax.

## 4. BPT3C

Long documents are segmented according to fixed length batch, and the next segment is initialized with the final state of the previous segment; the system continues to accumulate mean/max pooling, and the gradient is transmitted back by segment. This allows processing of documents that exceed video memory.

## 5. Complete process

```text
WikiText-103 LM pretraining
  → target-text LM fine-tuning (Discr + STLR)
  → add concat-pooling classifier
  → train head
  → gradual unfreezing
  → all unfrozen with layer-wise LR + STLR
```

## 6. With BERT [CLS]

ULMFiT explicitly splices last/max/mean; BERT usually uses `[CLS]` to summarize by self-attention, and can also do token pooling. Both convert variable-length sequences into fixed classification representations, with different mechanisms.
