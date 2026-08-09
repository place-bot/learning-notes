# Hierarchical map of LLM software stack

## 1. Model, runtime and application framework

A sentence of "running LLM" may include completely different tasks: downloading the model, reading the tokenizer, putting the weights into video memory, performing matrix multiplication, managing the conversation history, retrieving the document, calling the tool, and streaming the result to the web page.

Can be broken down into seven layers:

|layer|Typical objects|Responsible for content|
|---|---|---|
|model assets| config、tokenizer、weights、chat template |Describe the model and its parameters|
|Model library| Transformers |Implement the architecture in code and instantiate assets|
|inference runtime| llama.cpp、vLLM、TGI |Efficiently execute prefill and decode|
|Hardware backend| PyTorch、CUDA、Metal、BLAS、Vulkan |Perform tensor operators|
|service layer|llama-server, TGI server, self-built FastAPI|Concurrency, streaming response, authentication, health check|
|Application orchestration| LangChain / LangGraph |prompt, retrieval, tool, status, agent loop|
|user interface|Web page, desktop, command line|Display messages and collect user input|

The same tool can span adjacent layers. For example, Transformers can both define models and directly perform inference; llama.cpp also provides core libraries, CLI and HTTP server. The purpose of layering is to determine the main responsibilities, and it does not require that each item can only belong to one grid.

## 2. Why is the term backend easily confused?

In web development, backend often refers to server-side business logic. In deep learning, backend may also refer to operator implementations such as CUDA, Metal or CPU BLAS. In model applications, developers call the local inference server the model backend.

Therefore a more accurate expression is:

- llama.cpp: **Inference runtime/serving backend**;
- Transformers: **Model implementation and training inference library**;
- LangChain: **LLM application and agent orchestration framework**.

## 3. What does a generation go through?

Given a message \(m), the generation process can be written as:

\[
x_{1:n}=\operatorname{Tokenizer}(\operatorname{Template}(m)),
\]

\[
z_{n+1}=f_\theta(x_{1:n};K,V),
\]

\[
x_{n+1}\sim\operatorname{Sampler}(z_{n+1}),
\]

Then add the new token to the sequence, update the KV cache and repeat the decoding. The responsibilities of the different layers are:

1. LangChain or application code organization \(m\) and possible retrieval documents and tool results;
2. Chat template turns the message role into a control token used during model training;
3. tokenizer turns text into token IDs;
4. Transformers or llama.cpp execute \(f_\theta\);
5. The sampler selects the next token according to temperature, top-p and other rules;
6. The service layer returns the token stream to the application.

## 4. Model format is not a schema name

The same Llama schema can be saved in different file formats:

|Format|Common ecology|Features|
|---|---|---|
| SafeTensors | Transformers / Hugging Face |Safe tensor serialization, often saved in separate files with config and tokenizer|
| PyTorch checkpoint | PyTorch |Universal, but be careful about the code execution risk of pickle class format|
| GGUF |llama.cpp Ecology|A single file carries tensors and metadata, suitable for quantification and cross-platform local reasoning.|
| ONNX | ONNX Runtime |Static computation graph and cross-platform execution|

The model format only describes how assets are stored. It does not automatically determine training data, licenses, accuracy, or chat capabilities.

## 5. The presence or absence of a GUI is not the core difference.

Most of these items can be embedded into the server without an interface, and may also come with CLI, Notebook or Web UI. llama-server currently provides a simple web UI, Transformers are often used in notebooks, and LangChain also provides front-end integration. Production systems should still decouple the interface from the model runtime layer so that models or runtimes can be replaced without rewriting the production interface.

