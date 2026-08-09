# Limitations, Conclusions and Paths to GPT-3

## 1. Method limitations

### 1.1 Task learning is indirect

The model treats all tokens equally. Use the same prediction loss for factual answers, HTML residue, rhetorical passages, and misstatements:

\[
\mathcal L
=
-\sum_t\log p(x_t\mid x_{<t}).
\]

The goal does not explicitly express factuality, helpfulness, safety, or user intent.

### 1.2 Task format is sensitive

`TL;DR:`, `A:`, sample separators and candidate scoring methods will all affect the result. The paper has not systematically studied prompt variations, sample order and randomness.

### 1.3 One-way context

Only the text on the left can be read at the current position. Classification and bidirectional understanding tasks often benefit from BERT-style bidirectional encoders; the GPT-2 report also lists the upper limit of the efficiency of unidirectional representation as an issue to be studied.

### 1.4 Output reliability

The official model card clearly reminds: the model does not distinguish between fact and fiction, and does not support uses that require the content to be true. Fluency can mask subtle inconsistencies and errors.

### 1.5 Data and bias

WebText inherits the bias of web pages and filtering communities, and the complete corpus is not disclosed. Models may generate stereotypes, harmful content, and personally informative text.

### 1.6 Reproduction range is limited

The official repository provides the inference model, but lacks complete training data and training code. Researchers can reproduce the structure and generation, but cannot accurately reconstruct WebText training experiments.

## 2. Experimental limitations

- Different prompts, decoding and post-processing are used for different tasks;
- Some zero-shot experiments with contextual examples;
- The resultvariance of small data sets is larger;
- There is superficial overlap between webpage pretraining and benchmark;
- The scale of the four models is not enough to rigorously describe the scaling law;
- Not symmetrical to the data, computation, and output constraints that supervise SOTA.

## 3. What does the paper really change?

Before GPT-2, pretraining models were often understood as initializers of transferable representations. GPT-2 presents another interface:

\[
\text{Task call}
=
\text{Put tasks into context}
+
\text{Let the same LM continue to generate}.
\]

It promotes prompt from "beginning of generation" to "task description interface". Even though the performance was not stable at the time, this interface led directly to the later in-context learning.

## 4. Continuous changes from GPT-2 to GPT-3

|Dimensions| GPT-2 | GPT-3 |
|---|---|---|
|Maximum number of parameters|About 1.5B| 175B |
|context length| 1024 | 2048 |
|data|About 40 GB WebText|A mixed corpus of about 300B training tokens|
|Task settings|Broadly called zero-shot|Clear distinction between zero/one/few-shot|
|Research focus|Multitasking behavior begins to emerge|How scale enhances in-context learning|
|Contamination inspection| 8-gram Bloom filter |13-gram based clean subset analysis|

GPT-3 follows the autoregressive architecture, pre-LN and reversible tokenization of GPT-2, and mainly advances research through larger models, larger data, more training, and systematic contextual evaluation.

## 5. Conclusion

The conclusions of GPT-2 can be compressed into three levels:

1. Next-token prediction on large-scale and diverse texts can learn cross-domain language rules;
2. Task demonstrations in natural text can be transformed into task behaviors without parameter updates;
3. These behaviors usually increase with model capacity, but there is still a clear distance from a stable and reliable universal system.

The core question of the next GPT-3 article is: after expanding the model size by another two orders of magnitude, can a small number of examples in the context become a stronger and more systematic rapid adaptation mechanism.
