# GPT-2: Zero-shot task migration in language model

This topic is an intensive reading of Radford et al.’s technical report **Language Models are Unsupervised Multitask Learners**. Reported by OpenAI in 2019, the study population was a decoder-only Transformer later known as GPT-2.

## Capture the paper in one sentence

Only use large-scale, multi-source webpage text to train the same autoregressive language model, without updating parameters for downstream tasks; then write documents, questions, task prompts or a few examples into the context, and let the model complete reading comprehension, summary, translation and question and answer by "continue writing".

The training goal is still only next-token prediction:

\[
\mathcal L_{\mathrm{LM}}(\theta)
=
-\sum_{t=1}^{T}\log p_\theta(x_t\mid x_{<t}).
\]

The important proposition of the paper is that when the corpus naturally contains a lot of text in the form of "input-output", a language model with a large enough capacity will incidentally learn the hidden task structure in order to better predict the text.

## Citation details

|item|information|
|---|---|
|Author| Alec Radford、Jeffrey Wu、Rewon Child、David Luan、Dario Amodei、Ilya Sutskever |
|publish| OpenAI technical report，2019 |
|official report| [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) |
|Official description| [Better language models and their implications](https://openai.com/index/better-language-models/) |
|official code| [openai/gpt-2](https://github.com/openai/gpt-2) |
|Model type|Autoregressive language model with only Transformer decoder|

This document is usually cited as OpenAI Technical Report. Some secondary literature lists write it as "OpenAI Blog 1.8 (2019): 9", which is not official journal volume and issue information.

## Reading route

1. [Research questions, innovation and evidence boundaries](01-question-contributions.md)
2. [From language model to implicit multi-task learning](02-lm-to-multitask.md)
3. [WebText: How data is structured](03-webtext-data.md)
4. [Byte-level BPE: Any string can encode](04-byte-bpe.md)
5. [Differences between GPT-2 architecture and GPT-1](05-architecture.md)
6. [How to write tasks as context](06-zero-shot-protocol.md)
7. [Language modeling experiment and scale effect](07-language-modeling-experiments.md)
8. [Reading comprehension, abstract, translation and Q&A result](08-transfer-experiments.md)
9. [Generalization, memory and data overlap](09-generalization-memorization.md)
10. [Official code intensive reading](10-code-reading.md)
11. [Complete forward and generation example](11-worked-example.md)
12. [Limitations, Conclusions and Directions GPT-3](12-limitations-conclusion.md)
13. [References and primary information](references.md)

## After reading the main line that should be formed

```text
Diverse web corpus
   ↓ Only do next-token prediction
Shared decoder-only Transformer
   ↓ Task description, input and examples are all written as token
Conditional generation p(output | prompt)
   ↓ Do not update parameters
Cross-task zero-shot or contextual example migration
```

GPT-2 takes the "fine-tuning for each task after pretraining" route one step further: downstream tasks can be called directly through text context. GPT-3 then clearly defines and systematically compares zero-shot, one-shot, and few-shot in context.
