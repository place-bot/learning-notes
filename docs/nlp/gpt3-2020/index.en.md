# GPT-3: in-context learning in language model

This topic focuses on Brown et al.'s **Language Models are Few-Shot Learners**, which was officially published in NeurIPS 2020. The paper expands the context task call of GPT-2 to 175 billion parameters, and systematically distinguishes between zero-shot, one-shot and few-shot.

## Capture the paper in one sentence

First, use 300 billion tokens to train a general autoregressive language model; when facing a new task, put the task description and a few "input-answer" examples into the 2048-token context, and let the model directly predict new answers without gradient updates throughout the process.

## Core Mechanism

to demonstrations

\[
D_K=\{(x_1,y_1),\ldots,(x_K,y_K)\}
\]

and new input \(x_*\), model calculation

\[
p_\theta(y_*\mid D_K,x_*).
\]

The pretraining parameter \(\theta\) remains fixed. The example changes the hidden state and conditional distribution in the current context.

## Citation details

|item|information|
|---|---|
|Author|Tom B. Brown and 31 other authors|
|publish| Advances in Neural Information Processing Systems 33，2020，1877–1901 |
|Formal paper| [NeurIPS Proceedings](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) |
|full version| [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) |
|Official release warehouse| [openai/gpt-3](https://github.com/openai/gpt-3) |
|model|Eight decoder-only Transformers for 125M–175B|

## Reading route

1. [Research questions, innovations and core evidence](01-question-contributions.md)
2. [Zero-shot, One-shot, Few-shot and Fine-tuning](02-learning-settings.md)
3. [Probabilistic form of In-context learning](03-in-context-mechanism.md)
4. [Model architecture, eight scales and sparse attention](04-architecture-scaling.md)
5. [Training data, filtering and hybrid sampling](05-data-pipeline.md)
6. [Training process, parallelization and computational cost](06-training-compute.md)
7. [Prompt Construction and Evaluation Protocol](07-evaluation-protocol.md)
8. [Language Modeling, Question Answering, Translation and SuperGLUE](08-core-experiments.md)
9. [Arithmetic, word manipulation, news generation and other abilities](09-synthetic-qualitative.md)
10. [Why the author calls it Meta-learning](10-meta-learning-interpretation.md)
11. [How to interpret the scale curve and experimental results](11-scaling-analysis.md)
12. [Benchmark pollution and clean subset](12-contamination.md)
13. [Official repository, reproduction boundaries, limitations and conclusions](13-repository-limitations-conclusion.md)
14. [References and primary information](references.md)

## Relationship with the previous article

```text
GPT-2
  Large models can reveal multi-tasking behavior without downstream parameter updates
       ↓ The scale is expanded by about two orders of magnitude
GPT-3
  Systematic study of how 0/1/K examples in context change task performance
       ↓ Follow-up questions
instruction tuning, retrieval, tool usage, alignment and more reliable reasoning
```

The core innovation of GPT-3 mainly comes from large-scale experiments and interface verification. It does not invent new training objectives or train new modules for each task; the key contribution of the paper is to demonstrate that in-context adaptation of large models increases significantly with scale.
