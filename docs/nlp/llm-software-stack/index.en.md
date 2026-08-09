# LLM software stack: Transformers, llama.cpp and LangChain

This group of topics is dedicated to explaining what software layers are needed when a large language model changes from "weight on disk" to "a system that can be called by applications". Focus on Hugging Face Transformers, llama.cpp, and LangChain, explaining what each is responsible for, how they are connected, and when they are not required to be used at the same time.

!!! info "Calibrate the original sentence first"
    "They are both backend packages without a GUI that are responsible for loading and running LLM on the device" only partially describes the situation accurately.

    - **llama.cpp** is a C/C++ runtime and toolset for efficient local inference; the core works through CLI, library or HTTP server, and currently also comes with a simple Web UI;
    - **Transformers** is a general Python library for model architecture, tokenizer, weight loading, training and inference;
    - **LangChain** is an application orchestration framework for model, tool, retrieval, state, and agent loops, typically calling another inference runtime or cloud API.

The three are at different levels, so the really useful classification criterion is "which layer of the request chain it is at" rather than "whether there is a graphical interface".

## A complete request chain

```text
UI/API
       ↓
Application orchestration: LangChain
  ├── prompt and message
  ├── Search / Tools / memory
  └── agent control loop
       ↓
Unified model interface or HTTP request
       ↓
Inference layer: Transformers or llama.cpp
  ├── tokenizer
  ├── Weight loading
  ├── forward pass
  ├── KV cache
  └── sampling
       ↓
PyTorch/CUDA/Metal/CPU and other computing backends
```

## Reading route

1. [First create a hierarchical map of the LLM software stack](01-stack-layers.md)
2. [Hugging Face Transformers: Model library, loader and training interface](02-transformers.md)
3. [llama.cpp: GGUF, quantization and local inference](03-llama-cpp.md)
4. [LangChain: Models, Tools, Retrieval and Agent Orchestration](04-langchain.md)
5. [How to connect the three into the same application](05-integration.md)
6. [Performance, Memory, Concurrency and Observability](06-performance-operations.md)
7. [How to select software according to research and deployment goals](07-selection-conclusion.md)
8. [Official documents and extension tools](references.md)

## Version range

These items are updated quickly. This topic explains the stable software boundaries and core mechanisms. The example interface is checked against the official documentation on August 4, 2026. The dependency version and model revision should be fixed during actual runtime.

