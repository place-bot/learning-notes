# Problems, Innovations and Encoder-Only Architecture

## 1. Two pretraining routes in 2018

### Feature-based

Models such as ELMo generate contextualized features that are then handed over to task-specific networks.

### Fine-tuning

OpenAI GPT first pretrains the Transformer, and then fine-tunes the overall parameters with a small number of task headers. It uses left-to-right causal attention.

BERT hopes to retain a unified fine-tuning interface, while allowing each layer of token representation to jointly utilize the left and right contexts.

## 2. Why does the ordinary two-way language model leak?

If the goal is still to predict the current position \(x_i\), but also allows the representation to directly read the complete input containing \(x_i\), the network can copy the answer. BERT first destroys the selected token, and then lets the model restore the original word from the remaining context.

## 3. Architecture

BERT is a multi-layer Transformer encoder:

\[
\mathbf H^{(L)}
=
\operatorname{TransformerEncoder}^{(L)}
(\mathbf E).
\]

There is no decoder cross-attention and no target-side causal mask. Each valid position can focus on the entire input sequence.

## 4. Base and Large

|model|Layer \(L\)|Hide \(H\)|Header \(A\)| FFN |parameters|
|---|---:|---:|---:|---:|---:|
| BERT Base | 12 | 768 | 12 | 3072 | 110M |
| BERT Large | 24 | 1024 | 16 | 4096 | 340M |

Base deliberately maintains a similar model size to OpenAI GPT to facilitate comparison of pretraining directions and input forms.

## 5. Deep bidirectional

Each layer of BERT's self-attention allows left and right interactions. ELMo concatenates an independently trained left-direction LM with a right-direction LM at the output, with no joint conditioning of the two directions inside the deep layers. The paper uses "deeply bidirectional" to emphasize this difference.

## 6. Two-stage paradigm

### Pre-training

Training MLM and NSP using unlabeled BooksCorpus and Wikipedia.

### Fine-tuning

The same pretraining checkpoint initializes an independent model for each task, adds small task headers, and updates all parameters. The original paper's "small number of task-specific parameters" does not indicate freezing BERT.

## 7. Contribution

- MLM supports deep two-way pretraining;
- NSP provides pretraining signals for sentence pair relationships;
- Unified input representation covers single sentences and sentence pairs;
- 11 tasks can be handled with minimal task architecture modifications;
- System ablation bidirectionality, NSP, scale and feature-based usage.
