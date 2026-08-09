#Relationship and conclusion with BERT

## 1. Put BERT into the definition

Source domain:

\[
\mathcal D_S=\text{BooksCorpus + Wikipedia}.
\]

Source task:

\[
\mathcal T_S=\text{MLM + NSP}.
\]

The target domain/task can be SQuAD QA, GLUE classification, or target domain text. BERT transfers encoder parameters and representations to the target task, which belongs to inductive transfer learning.

## 2. Levels of Pretraining, fine-tuning and transfer

- transfer learning: overall problem setting;
- pretraining: learning reusable parameters on source data/target;
- fine-tuning: adjust parameters using target data;
- Language modeling: one of the commonly used pretraining tasks.

These four words are at different levels of abstraction and cannot be used as synonyms for each other.

## 3. Modern Issues

Modern models need to continue to answer:

- How to quantify the similarity between the source corpus and the target domain;
- Which layer and type of parameters are most worth migrating;
- Full fine-tuning or LoRA;
- when to freeze;
- How to combine multi-source migration;
- How to detect negative transfer, forgetting and shortcuts.

## 4. Conclusion

Pan and Yang's framework uses three coordinates: domain, task, and transfer object to break down transfer learning. BERT's pretraining-fine-tuning is one of the most successful parameter/representation migration implementations, not all of transfer learning.
