# Introduction to the special topic "Designing Large Language Model Applications"

This topic builds a set of Chinese reading maps around Suhas Pai's **Designing Large Language Model Applications: A Holistic Approach to LLMs**. The book will be published by O’Reilly Media in 2025 and is targeted at intermediate to advanced practitioners. The text connects LLM applications from training data, tokenizer and model architecture to fine-tuning, inference optimization, agent, embedding, RAG and system design.

## Key Values of this Book

The *Applications* in the title of the book may lead people to think that the content is mainly about API calls. It actually uses a more complete engineering chain:

```text
data
  ↓
Vocabulary and Tokenizer
  ↓
Architecture and training goals
  ↓
Select / fine-tuning / alignment / inference optimization
  ↓
Tools, Embedding, RAG
  ↓
Multi-model system architecture
```

That is, app behavior is determined by more than just prompt. Training data, input encoding, model target, decoding, retrieval and system control jointly determine the final result.

## Citation details

|item|information|
|---|---|
|Author| Suhas Pai |
|full name| *Designing Large Language Model Applications: A Holistic Approach to LLMs* |
|publishing house| O’Reilly Media |
|version|First edition, March 2025|
|difficulty| Intermediate to advanced |
|structure| 3 Parts，13 Chapters |
|Official page|[O’Reilly Book Page](https://www.oreilly.com/library/view/designing-large-language/9781098150495/)|

## Three-part structure

| Part |book chapter|questions to answer|
|---|---|---|
| I. LLM Ingredients | 1–4 |What data, input units, structures and goals does a language model consist of?|
| II. Utilizing LLMs | 5–9 |How to select, fine-tune, align and run models efficiently|
| III. LLM Application Paradigms | 10–13 |How to connect models to tools, knowledge bases, embeddings and complete systems|

## Reading route for this topic

1. [Structure of the book, knowledge dependence and reading strategies](01-book-map.md)
2. [pretraining data: quality, deduplication, mixing and contamination](02-pretraining-data.md)
3. [Vocabulary and Tokenization: How to connect with the BPE/WordPiece topic](03-vocabulary-tokenization.md)
4. [Transformer Architecture, Backbone and Learning Objectives](04-architectures-objectives.md)
5. [Model selection, loading, decoding and structured output](05-model-selection-inference.md)
6. [Fine-tuning, PEFT and domain adaptation](06-finetuning-domain-adaptation.md)
7. [Alignment, hallucination relief and reasoning ability](07-alignment-reasoning.md)
8. [KV Cache, quantization, distillation and inference acceleration](08-inference-optimization.md)
9. [External Tools, Agent Loop and Security Control](09-tools-agents.md)
10. [Embedding, Chunking and RAG](10-embeddings-rag.md)
11. [Multi-model architecture, Router and CAT system interface](11-system-architecture-cat.md)
12. [Boundaries of evidence, limitations, conclusions and future updates](12-limitations-conclusion.md)
13. [Official page and extended literature](references.md)

##Relationship with existing topics on this site

This topic is responsible for horizontal connections and does not repeat all the mathematical details that have been studied intensively:

- For tokenization details, see [BPE, Byte-level BPE and WordPiece](../subword-tokenization/index.md);
- For architectural details, see [Attention Is All You Need](../transformer-2017/index.md);
- For efficient fine-tuning of parameters, see [LoRA](../lora-2022/index.md);
- For the alignment process, see [Llama 2](../llama2-2023/index.md);
- For operation and orchestration tools, see [LLM software stack](../llm-software-stack/index.md);
- For model selection, see [Open weight model family](../open-weight-model-families/index.md).

!!! note "Content Boundaries"
    This website provides structured introduction, method derivation and systematic extension, and does not copy the entire chapter text protected by copyright. Specific cases, charts and the author's complete discussion should be read back to the original book.

