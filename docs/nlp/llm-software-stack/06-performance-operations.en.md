# Performance, memory, concurrency and observability

## 1. Prefill and decode should be tested separately

LLM requests have two phases:

- **prefill**: Process the input token once and establish the KV cache;
- **decode**: Generate a new token each time and reuse the cache.

So common indicators include:

|indicator|What does it reflect?|
|---|---|
| time to first token |Queuing, tokenization and prefill delays|
| inter-token latency |Single step decode speed|
| output tokens/s |Generation speed perceived by users|
| total tokens/s |Service throughput for all concurrent requests|
| peak memory |Weight, KV cache, activation and total runtime usage|

Only reporting single-user tokens/s cannot explain high concurrent service capabilities.

## 2. Batch processing and continuous batching

Static batch waits for tasks of the same size to run together; continuous batching dynamically adds new requests to the currently executing schedule. The inference server trades off throughput and single-request latency.

llama-server supports parallel decoding and multi-user; Transformers' ordinary `generate()` requires the application to organize batches by itself; specialized serving runtimes usually provide more complex scheduling. When choosing a tool, you should first determine whether the goal is interactive low latency or offline high throughput.

## 3. What parts does memory consist of?

\[
M_{\text{peak}}
=
M_{\text{weights}}
+M_{KV}
+M_{\text{activations}}
+M_{\text{workspace}}
+M_{\text{runtime}}.
\]

Quantization mainly reduces \(M_{\text{weights}}\). Increasing context and concurrency mostly pushed up \(M_{KV}\). A certain 4-bit model can be successfully loaded, which only proves that the weights and initial buffer can be loaded, but does not guarantee the stable operation of high concurrency and long context.

## 4. Cache and state boundaries

Need to distinguish:

- Model download cache;
- tokenizer cache;
- KV cache generated once;
- prefix / prompt cache；
- LangChain’s short-term task state;
- Cross-task long-term memory;
- RAG vector store。

Their lifecycle, privacy, and expiration policies differ. Deleting chat history does not necessarily clear the vector library or server logs.

## 5. Observability

Each request logs at least:

```text
request ID
model ID + revision + quantization
prompt template version
input/output token counts
retrieved document IDs
tool calls and statuses
latency breakdown
stop reason
error class
```

When containing student data, the full prompt and output should not be saved by default. Hash, masked fields or controlled sampling can be recorded and retention periods and access permissions set.

## 6. Regression testing

Run a fixed test set before software or model upgrade:

1. Whether the tokenizer result changes;
2. Whether the chat template has changed;
3. Whether the greedy output is within the allowed range;
4. Whether structured output and tool calls still satisfy the schema;
5. Whether the RAG citation still points to the correct evidence;
6. Whether peak memory, first token latency and throughput are degraded;
7. Whether timeouts, cancellations, concurrency and error responses comply with the contract.

Even if the generative model sets the same seed, numerical differences may occur due to different hardware and kernels. Regression criteria should prioritize checking task correctness and structural constraints, and do not necessarily require that all sampled text be equal character-by-character.

