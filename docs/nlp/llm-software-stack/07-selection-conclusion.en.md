# How to choose and combine

## 1. Select by target

|target|Priority tools|Reason|
|---|---|---|
|Read and modify model structures| Transformers |Architecture implementation with PyTorch tensors can be inspected directly|
|Training, fine-tuning and LoRA| Transformers + PEFT |Complete gradient, optimizer and checkpoint pipelines|
|Mac/CPU/consumer GPU local inference| llama.cpp |GGUF, quantization, and multi-hardware backends mature|
|Expose lightweight native HTTP API| llama-server |Can run independently and provide compatible interfaces|
|Simple one-time generation|Transformers or llama.cpp call directly|No additional orchestration layer required|
|RAG, tools and multi-step agents|LangChain / LangGraph + any model backend|Manage searches, tools, status and control loops|
|Large GPU high concurrency service|Simultaneously evaluate vLLM, TGI, etc.|Dedicated batching and memory management may be more appropriate|

## 2. Three common misunderstandings

### After installing LangChain, you also need a model

LangChain does not come with a universal LLM weight. It requires connecting to a local runtime or model service.

### Downloading from Hugging Face is not the same as using Transformers for inference

Hugging Face Hub is a model asset hosting platform. GGUFs can be downloaded from the Hub and handed to llama.cpp; SafeTensors can be loaded by Transformers, vLLM or other runtimes.

### Smaller quantization files do not guarantee faster speed

Speed also depends on kernel, memory bandwidth, CPU/GPU division of labor, batch, context and whether the quantization format has hardware optimization.

## 3. Minimum dependency principle

Starting from the shortest link:

```text
Generate once
→ Direct model call

Shared services required
→ Add inference server

Need search or tool
→ Add explicit orchestration code

Requires long-term, recoverable agent
→ Add statecharts, persistence and observability
```

Each additional layer should solve an existing problem and add tests for it. In this way, when an error occurs, it can be determined whether it is caused by the model, template, retrieval, tool, runtime or application state.

## 4. Conclusion

Transformers, llama.cpp and LangChain can form the same system or be used independently:

- Transformers turn paper architecture and model assets into trainable and inferable Python objects;
- llama.cpp efficiently maps GGUF weights to local hardware and provides CLI, libraries and servers;
- LangChain embeds model calls into retrieval, tooling, and stateful agent processes.

By understanding their hierarchy, the existence of a GUI is no longer a critical issue. What really needs to be decided is where the weights run, who is responsible for token generation, who manages the application state, which calls can take external action, and how each layer is tested and audited.

