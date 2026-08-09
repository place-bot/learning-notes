# llama.cpp: GGUF, quantization and local inference

## 1. item target

llama.cpp implements LLM inference in C/C++, emphasizing less dependence, cross-platform and consumer-grade hardware operation. It was originally developed around LLaMA and has subsequently supported many model architectures and multiple hardware backends, including CPU BLAS, Apple Metal, NVIDIA CUDA, AMD HIP, and Vulkan.

It provides three common entrances:

|entrance|Purpose|
|---|---|
| `llama-cli` |Command line dialogue, completion and quick experimentation|
| `llama-server` |HTTP serving, concurrency, streaming responses, and OpenAI-compatible endpoints|
| `libllama` |Embed as library in C/C++ or language bindings|

## 2. What does GGUF save?

GGUF is a commonly used model file format for llama.cpp. It's saved in the same container:

- weight tensor;
- Tensor shape and data type;
- Architectural metadata;
- tokenizer and special token information;
- Quantification type;
- Configuration of context and RoPE etc.

Transformers warehouses are often composed of multiple configuration and weight shards, and GGUF emphasizes a self-describing file to facilitate transmission and loading. The transformation must accurately preserve tensor name, tokenizer, and chat template metadata.

## 3. Quantification principle

Mapping the floating point weight block \(w\) to the lower integer \(q\), the simplest form is:

\[
q=\operatorname{round}\left(\frac{w-z}{s}\right),
\qquad
\widehat w=sq+z,
\]

Among them, \(s\) is the scale and \(z\) is the zero point. Formats like llama.cpp's K-quants use more granular metadata and grouping strategies for weight blocks to trade off file size, speed, and error.

`Q4_K_M`, `Q5_K_M`, etc. in the model name represent the specific quantification scheme, not the model parameter scale. Different quantizers, calibration methods and source weights may cause two quantizations with the same name to produce different results. The file hash and source should be preserved.

## 4. CPU/GPU mixed offloading

When the local device has insufficient video memory, some layers can be placed on the GPU, while the rest remain on the system memory and CPU. The rough process is:

```text
token IDs
  ↓
CPU embedding / partial layer
  ↓ PCIe or Unified Memory Transfer
GPU layers
  ↓
logits and sampling
```

Apple Silicon uses unified memory, where the CPU and GPU share a memory pool, but bandwidth and usable capacity are still limited. Discrete GPU hybrid offload may be subject to PCIe transfer limitations. The optimal `n_gpu_layers` needs to be based on model, quantification and actual equipment measurement.

## 5. KV cache and context

Autoregressive decoding caches the keys and values of previous tokens to avoid recalculating the entire history at each step. The cache size is approximately:

\[
M_{KV}
\approx
2Lnh_{kv}d_hb,
\]

Among them, 2 corresponds to K and V, \(L\) is the number of layers, \(n\) is the number of context tokens, \(h_{kv}\) is KV heads, \(d_h\) is the dimension of each head, and \(b\) is the number of bytes per element.

Increasing context size or parallel slots will significantly increase cache, even if the weights are quantized. The total context of llama-server can be distributed among concurrent slots, so both context and concurrency must be planned.

## 6. Basic commands

```bash
#Run the local GGUF directly
llama-cli -m /absolute/path/model.gguf

#Get and run GGUF from a compatible repository
llama-cli -hf organization/model-GGUF:Q4_K_M

#Start the local service
llama-server -m /absolute/path/model.gguf --port 8080
```

After the service is started, the application can call:

```text
POST http://127.0.0.1:8080/v1/chat/completions
```

OpenAI-compatible means that common request shapes are compatible, and does not guarantee that all fields and error semantics are completely consistent with the vendor API. Before integration, you should refer to the current documentation and automated tests of llama-server.

## 7. Chat template and constraint generation

llama.cpp can read chat templates in GGUF and also supports explicitly specifying templates. Tool calls and multiple rounds of conversations rely on template accuracy. Item also supports GBNF grammar or JSON schema constraint output, which is suitable for generating structured data.

Structural constraints ensure that the output satisfies the syntax, but do not guarantee that the field values are true. For example, a date in JSON may be formatted correctly, but it may still be a date made up by the model.

## 8. Application and limitations

llama.cpp is suitable for personal computers, local offline, low-dependency applications, GGUF quantitative evaluation and embedded services. It is not the highest throughput solution for every scenario: large GPU clusters, high concurrency continuous batching, or training tasks may be better suited for vLLM, TGI, TensorRT-LLM, or PyTorch/Transformers. Model transformation and quantification also introduce additional version management responsibilities.

