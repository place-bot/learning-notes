# BERT: Deep bidirectional Transformer pretraining

This topic is an intensive reading of Devlin et al.'s **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**. The paper was released as a preprint in 2018 and officially published at NAACL-HLT 2019.

## Core Idea

BERT uses a Transformer encoder to allow each token to read the left and right context simultaneously at each layer. In order to prevent the target token from directly seeing itself, pretraining randomly masks part of the input and predicts the original word:

\[
\mathcal L_{\text{pretrain}}
=
\mathcal L_{\text{MLM}}
+
\mathcal L_{\text{NSP}}.
\]

After pretraining, a small number of task heads and the same set of BERT parameters are used to complete classification, sentence pair inference, sequence annotation and extractive question answering.

## Citation details

|item|information|
|---|---|
|Author| Jacob Devlin、Ming-Wei Chang、Kenton Lee、Kristina Toutanova |
|publish| NAACL-HLT 2019，4171–4186 |
|Formal paper| [ACL Anthology](https://aclanthology.org/N19-1423/) |
| arXiv | [1810.04805](https://arxiv.org/abs/1810.04805) |
|original code| [google-research/bert](https://github.com/google-research/bert) |

## Reading route

1. [Problems, innovations and encoder-only architecture](01-problem-architecture.md)
2. [WordPiece, CLS, SEP and three kinds of embedding](02-input-representation.md)
3. [MLM vs. 80/10/10](03-masked-language-model.md)
4. [NSP and pretraining sample structure](04-nsp-and-data-construction.md)
5. [pretraining data, configuration and optimization](05-pretraining-configuration.md)
6. [Unified fine-tuning interface](06-finetuning-tasks.md)
7. [Complete hand calculation](07-worked-example.md)
8. [Experiment result](08-experiments-results.md)
9. [Ablation, bidirectionality and model size](09-ablations.md)
10. [Intensive reading of Google’s original code and modern implementation](10-code-reading-implementation.md)
11. [Limitations, subsequent development and conclusions](11-limitations-followups-conclusion.md)
12. [Reference](references.md)

## Relationship with previous and previous topics

- Word2Vec: a static vector for each word;
- Bahdanau/Transformer: tokens in the sequence obtain context through attention;
- BERT: pretraining deep bidirectional Transformer encoder with unlabeled corpus;
- LoRA: Freeze this type of pretraining model and use low-rank updates to complete efficient parameter adaptation.
