# LangChain: models, tools, retrieval and agent orchestration

## 1. Which layer is LangChain on?

LangChain mainly manages "what happens before and after model calls". It connects to cloud models or on-premises services through a unified interface and combines models with prompts, retrievers, tools, structured output, and state.

It is generally not responsible for performing Transformer matrix multiplication inside the model. The actual forward pass can happen in llama.cpp, Transformers, vLLM, or some remote API.

## 2. Basic model interface

LangChain encapsulates different providers or local services into message interfaces:

```python
response = model.invoke([
    {"role": "system", "content": "You are a CAT research assistant."},
    {"role": "user", "content": "Explain the exposure control of the project."},
])
```

This abstraction facilitates replacement of providers, but "unified interface" does not mean that the underlying model has the same capabilities. Tool call format, context, structured output, and error handling still need to be verified per provider.

## 3. RAG pipeline

A two-stage RAG can be written as:

```text
Documentation → Segmentation → embedding → vector store
                              ↑
question → query embedding → retrieve top-k
                              ↓
              prompt + retrieved context
                              ↓
                            LLM
```

Search stage:

\[
D_k=\operatorname{TopK}_{d\in\mathcal D}
\operatorname{sim}(e(q),e(d)).
\]

Generation phase:

\[
y\sim p_\theta(y\mid q,D_k).
\]

LangChain provides interfaces to document loaders, splitters, embeddings, vector stores, and retrievers. It reduces the concatenation code and does not automatically select the correct chunk size, embedding model or top-\(k\).

## 4. Tool calling

A tool consists of a name, description, input schema, and executable functions:

```python
from langchain.tools import tool

@tool
def item_statistics(item_id: str) -> dict:
    """Read the calibration parameters of the specified test."""
    return {"item_id": item_id, "difficulty": 0.42}
```

The model outputs a request for "which tool to call and what parameters to fill in." The framework is responsible for actually executing the function and then returning the result to the model. Safety boundaries must be established by code:

- Tool minimum permissions;
- schema verification;
- Network and file sandbox;
- Manual confirmation of high-risk operations;
- Timeouts, retries, idempotence and audit logs.

## 5. Agent loop

The current LangChain agent is built on the LangGraph runtime. The simplified loop is:

\[
s_{t+1}=
\begin{cases}
\operatorname{ExecuteTool}(a_t,s_t),&a_t\text{is a tool call},\\
\operatorname{Finish}(a_t),&a_t\text{is the final answer}.
\end{cases}
\]

The loop stops when the model gives its final answer, reaches the iteration limit, or triggers an abort condition. The framework can add middleware for logging, retrying, model routing, PII detection, human approval and output formatting.

## 6. Memory and model context

Short-term memory is usually messages and status within the same task; long-term memory is user or application information saved across tasks. Saving information and putting information into this prompt are two actions:

```text
Persistent storage
   ↓ Query/Filter/Summary
Context of this round
   ↓
Model call
```

Cramming the entire history unconditionally into context adds latency, expense, and disruption. Memory policies need to delete, digest, or retrieve old information and clarify user privacy and data retention rules.

## 7. When is LangChain too heavy?

If your program only does local text generation once, it's clearer to call Transformers or llama-server directly. LangChain is more valuable in the following scenarios:

- Need to switch multiple model providers;
- There are search, tools and multi-step agents;
- Requires durable state, streaming or human-in-the-loop;
- Hope to unify tracing, retries and middleware.

Framework abstraction increases dependencies, upgrade costs, and debugging layers. Application design should start with minimal direct calls and add components as clear orchestration needs arise.

