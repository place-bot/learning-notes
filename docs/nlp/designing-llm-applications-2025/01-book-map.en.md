# Full book map and reading strategies

## 1. Why talk about model raw materials first?

LLM applications often start with an API demo:

```text
prompt → model → answer
```

A series of questions will arise during actual deployment: why the model does not understand the terminology, why the token costs of different languages vary greatly, why long context fails, why fine-tuning destroys the original ability, and why RAG still answers incorrectly even if there is evidence.

The book traces these questions back into longer causal chains:

\[
\text{Behavior}
=
f(
\text{data},
\text{tokenizer},
\text{architecture},
\text{objective},
\text{adaptation},
\text{inference},
\text{system}
).
\]

Part I is therefore not a background knowledge appendix, but a layer of reasons for subsequent application decisions.

## 2. Part I：LLM Ingredients

### Chapter 1：Introduction

Enter the question from LLM history, prompting, API and chatbot prototype, and propose the distance from prototype to production.

### Chapter 2：Pre-Training Data

Discusses data requirements, public corpora, synthetic data, filtering, deduplication, PII, decontamination, data mixture, and fairness.

### Chapter 3：Vocabulary and Tokenization

Discuss vocabulary size, normalization, pre-tokenization, BPE, WordPiece and special tokens.

### Chapter 4：Architectures and Learning Objectives

Advance from Transformer parts to encoder-only, encoder-decoder, decoder-only, MoE, and full, prefix, masked language modeling.

## 3. Part II：Utilizing LLMs

|Chapter|core decisions|
|---|---|
| 5. Adapting LLMs |Which model to choose, how to load, how to decode and evaluate|
| 6. Fine-Tuning |How to design optimization parameters, data, and PEFT processes|
| 7. Advanced Fine-Tuning |continual pretraining, replay, adapter merging and model fusion|
| 8. Alignment and Reasoning |Human feedback, hallucinations, verifiers and inference-time compute|
| 9. Inference Optimization |cache, early exit, distillation, speculative decoding and quantization|

The main thread of this part is:

\[
\text{Already have a basic model}
\longrightarrow
\text{Task available models}
\longrightarrow
\text{Affordable cost service}.
\]

## 4. Part III：LLM Application Paradigms

### Chapter 10：External Tools

Advance from passive model calls to explicit tool calls and autonomous agents, discussing model, tool, store, loop, guardrail, verifier and orchestration.

### Chapter 11：Representation Learning and Embeddings

Covers semantic search, embedding fine-tuning, Matryoshka, quantization, chunking and vector database.

### Chapter 12：RAG

Split RAG into rewrite, retrieve, rerank, refine, insert, generate, and compare long context and fine-tuning.

### Chapter 13：Design Patterns and System Architecture

Discusses multi-LLM, cascade, router, task-specialized models, DSPy and LMQL.

## 5. Three ways of reading

### Model research route

```text
Chapter 2 → 3 → 4 → 6 → 7 → 8 → 9
```

Suitable for studying pretraining, tokenizer, fine-tuning and model mechanisms.

### Application engineering route

```text
Chapter 1 → 5 → 10 → 11 → 12 → 13 → 9
```

Suitable for readers who already have models and need to build systems.

### CAT Study Route

```text
Chapter 3
→ Chapter 5
→ Chapter 10
→ Chapter 11/12
→ Chapter 13
```

The focus is on item content encoding, model selection, tool constraints, item bank retrieval and adaptive system orchestration.

## 6. Recommended reading record template

Each chapter is recorded according to five questions:

1. Which layer of the LLM life cycle does this chapter control?
2. What are input, status and output?
3. What are the optimization goals or evaluation indicators?
4. Which conclusions come from experiments and which are engineering experience?
5. How to connect with CAT’s measurement goals, content constraints and real-time feedback?

This avoids reading a large number of technical terms into a list of unrelated tools.

