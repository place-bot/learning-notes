# Embedding, Chunking & RAG

## 1. Embedding

The encoder maps text to vectors:

\[
e(x)\in\mathbb R^d.
\]

Commonly used cosine similarity:

\[
\operatorname{cos}(q,d)
=
\frac{e(q)^\top e(d)}
{\|e(q)\|\|e(d)\|}.
\]

Semantic similarity does not equal factual support. Embedding is used for candidate recall, which still requires reranking and generation verification.

## 2. Embedding fine-tuning

Training comparison targets for query, positive, and negative:

\[
\mathcal L_i
=
-\log
\frac{\exp(s(q_i,d_i^+)/\tau)}
{\exp(s(q_i,d_i^+)/\tau)+
\sum_j\exp(s(q_i,d_{ij}^-)/\tau)}.
\]

Hard negatives are especially important for domain retrieval.

## 3. Chunking

|method|Advantages|risk|
|---|---|---|
| Fixed window |Simple and stable|truncate semantic unit|
| Sliding window |Preserve boundary information|Duplication and index bloat|
| Metadata-aware |Keep chapter/title numbers|Depend on document structure|
| Layout-aware |Work with tables and PDFs|Parsing is complex|
| Semantic |More in line with the theme|High costs and unstable borders|
| Late chunking |Use long context representation before cutting|Model and implementation requirements are higher|

## 4. RAG Six Stages

```text
Rewrite
→ Retrieve
→ Rerank
→ Refine
→ Insert
→ Generate
```

Each stage has independent errors: query rewrite deviation, missing recall, ordering errors, document pollution, context overlongness, and generation infidelity.

## 5. Retrieval indicators

\[
\operatorname{Recall@k}
=
\frac{\text{Number of relevant documents in top-k}}
{\text{Number of all related documents}}.
\]

The generation phase also evaluates citation precision, claim support, rejections, and answer completeness.

## 6. RAG, Long Context and Fine-tuning

|method|more suitable for solving|
|---|---|
| RAG |External, updateable, referenced knowledge|
| Long context |A large amount of material already available for this request|
| Fine-tuning |Stable behavior, format, style and domain decisions|

The three can be combined. RAG is responsible for evidence collection, long context is responsible for synthesis, and fine-tuning is responsible for behavior.

## 7. Memory and RAG

Conversational memory can be thought of as a private retrieval library:

```text
historical interaction
→ structuring / embedding
→ Permission and time filtering
→ Retrieve related memory
→ Put into current round context
```

Long-term memory requires user-visible deletion and error correction mechanisms.

## 8. CAT item bank RAG

The retrieval objects can include question stems, knowledge points, item parameters, exposure, enemy-question relationships and solution basis. Vector similarity is only responsible for semantic candidates. The final topic selection must also satisfy measurement information, content blueprint, available item bank and exposure constraints.

