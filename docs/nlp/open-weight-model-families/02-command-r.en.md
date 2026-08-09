# Command R: Designing around RAG and tool usage

## 1. Family positioning

The Command R is not a base model series simply aiming for universal leaderboard scores. Cohere focuses its training on three links common to enterprise applications:

1. Retrieve evidence from external documents;
2. Generate cited or traceable answers based on evidence;
3. Call one or more tools to complete the task.

This makes Command R more suitable for understanding in a RAG system or agent pipeline.

```text
User issues
   ↓
Query rewriting/retrieval
   ↓
Document fragment + metadata
   ↓
Command R grounded generation
   ├── Generate answer
   └── Match answer fragments to evidence
```

## 2. Representative version

|version|scale|context|focus|weight clause|
|---|---:|---:|---|---|
| C4AI Command R v01 | 35B | 128K |Multi-language, RAG, tool call|CC-BY-NC + Acceptable Use Request|
| C4AI Command R 08-2024 | 32B | 128K |Reasoning, summarization, Q&A, RAG, single-step and multi-step tool usage|CC-BY-NC + Acceptable Use Request|
| C4AI Command R+ 08-2024 | 104B | 128K |Larger RAG usage with complex multi-step tools|CC-BY-NC + Acceptable Use Request|
| Command R7B 12-2024 | 7B | 128K |Smaller deployment sizes, multiple languages, and long contexts|Subject to specific model card|

Described in the table are downloadable study weights published by Cohere Labs. Model aliases, lifecycles, and recommended models in the Cohere API will continue to change, and local weight terms cannot be inferred just from the family name.

## 3. How Grounded generation works

Ordinary language model learning:

\[
p(y\mid x),
\]

Among them, \(x\) is the user prompt and \(y\) is the answer. The RAG scenario adds the retrieved document \(D\) to the input:

\[
p(y,c\mid x,D),
\]

Among them, \(c\) represents the reference relationship between the answer and the location of the evidence. The ideal model needs to satisfy both:

- **Relevance**: answer the question itself;
- **Fidelity**: Key statements can be supported by documentation;
- **Attributability**: The quote points to a fragment that actually supports the statement;
- **Rejection ability**: Do not over-complete when the document does not contain answers.

Long contexts only increase the number of documents that can be accommodated in one input, but do not automatically guarantee that evidence is relevant, references are correct, or answers are free of illusions. Retrieval quality and document segmentation still determine the upper limit of the system.

## 4. Tool usage and multi-step agent

Tool calls can be written as a loop:

\[
s_t=(x,h_{<t},o_{<t}),
\]

\[
a_t\sim p_\theta(a\mid s_t),
\]

Among them, \(h_{<t}\) is the previous conversation, \(o_{<t}\) is the result returned by the tool, and \(a_t\) can be a natural language reply or a structured tool request. After executing the tool, \(o_t\) is obtained, and the model determines the next step.

The model card of Command R+ emphasizes multi-step tool use, which means that the training target covers the multi-round process of "calling the tool - reading the result - continuing planning". The actual system still has to be added outside the model:

- JSON schema verification;
- Permission control and parameter whitelist;
- Maximum number of calling steps;
- Timeouts, retries and manual confirmations;
-Prompt injection protection for content returned by tools.

## 5. How to interpret multilingual ability

The model card for Command R 08-2024 was trained in 23 languages and evaluated in 10 of them. The two have different meanings: the fact that the training corpus contains one language does not mean that the language has received verification of the same intensity and task scope. Chinese RAG items need to be evaluated separately for Chinese search recall, citation boundaries and long document question and answer.

## 6. Application and limitations

Scenarios suitable for priority testing include enterprise knowledge base Q&A, evidence-based research assistants, multilingual customer service, and tool orchestration. Major limitations include:

- Local deployment costs are higher for 32B, 35B or 104B weights;
- CC-BY-NC research weight cannot be directly considered as a general commercial license;
- RAG capabilities rely on specified chat templates and document formats;
- References to model output still need to be automatically verified;
- API products and open weight versions may have different version numbers and capabilities.

Therefore, the core rationale for choosing Command R should be "the need for specially trained retrieval, referencing, and tooling behaviors," with licensing and deployment options being independent decisions.

