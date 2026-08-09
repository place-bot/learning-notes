# How to connect the three into the same application

## 1. Three common combinations

### Combination A: Transformers Direct Inference

```text
Python Application → Transformers → PyTorch → GPU/CPU
```

Suitable for research, training, reading logits, modifying model structure and small-scale batch processing. There is no LangChain and no independent model server.

### Combination B: llama.cpp local service

```text
Web/Script → HTTP → llama-server → GGUF → Metal/CUDA/CPU
```

Suitable for native quantization models, language-agnostic HTTP clients, and simple standalone deployment.

### Combination C: LangChain orchestration llama.cpp

```text
Application → LangChain agent
          ├── retriever / database / tools
          └── OpenAI-compatible client
                         ↓
                    llama-server
                         ↓
                    GGUF model
```

LangChain is responsible for loops and tools, and llama.cpp is responsible for token generation. Transformers do not have to participate in online requests, but can be used for offline fine-tuning before converting GGUF.

## 2. A local server request

Start the model:

```bash
llama-server \
  -m /absolute/path/model.Q4_K_M.gguf \
  --host 127.0.0.1 \
  --port 8080
```

Call with a compatible client:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="local-only",
)

response = client.chat.completions.create(
    model="local-model",
    messages=[{"role": "user", "content": "Explain CAT."}],
)
```

Running on the same device is not automatically safe. If the server is bound to `0.0.0.0`, the LAN or external network may access the port; production deployment requires authentication, TLS, network restrictions and log desensitization.

## 3. Offline training to local deployment

A complete model life cycle may be:

```text
Hugging Face base checkpoint
        ↓ Transformers + PEFT
Domain LoRA / merged SafeTensors
        ↓ Verify tokenizer and output
Convert to GGUF
        ↓ Quantification
Q4_K_M / Q5_K_M and other files
        ↓ llama.cpp regression testing
local deployment
```

Each arrow may change the output. Must be verified separately:

1. Before and after adapter merger;
2. Before and after conversion from SafeTensors to GGUF;
3. From floating point GGUF to quantized GGUF before and after;
4. Official chat template and deployment template;
5. Target context and build parameters.

## 4. API abstraction leak

Even if both servers provide `/v1/chat/completions`, they may still differ in the following ways:

- system message support;
- tool call schema；
- JSON constrained decoding；
- token usage calculation;
- stop sequences；
- streaming chunk format;
- Error codes, timeouts and cancellations;
- Multimodal input format.

Therefore, contract tests should be established for each backend instead of just verifying "can return a piece of text".

## 5. CAT Research System Example

```text
students answer
   ↓
CAT status updates (IRT/CDM/Strategy Model)
   ↓
Select the next question ───────────────┐
   ↓                      │
Need explanation or content retrieval?       │
   ↓ is │
LangChain retrieves item metadata │
   ↓                      │
Local llama.cpp / Remote model │
   ↓                      │
Generate constrained explanations │
   ↓                      │
Auditing and interface display ────────────┘
```

IRT estimation and topic selection constraints should be controlled by deterministic measurement codes; LLM is suitable for content understanding, retrieval, and natural language interpretation. Leaving the ability estimate entirely to the chat history will lose the calibrable measurement model and error quantification.

