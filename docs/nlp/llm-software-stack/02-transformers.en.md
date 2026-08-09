# Hugging Face Transformers

## 1. The core problem it solves

Transformers from different papers vary in the number of layers, attention, positional encoding, tokenizer, and output heads. Transformers encapsulate a large number of architectures with a unified interface, allowing researchers to read configurations, tokenizers, and weights from the model warehouse and complete inference, evaluation, or training.

A typical loading process is:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
```

The `Auto*` class first reads `model_type` in `config.json`, and then selects the corresponding specific Python class. It does not create a new common architecture, but automates the mapping of configurations to implementation classes.

## 2. What does a set of model assets include?

|file or object|function|
|---|---|
| `config.json` |Structural parameters such as number of layers, hidden size, number of heads, RoPE, etc.|
|tokenizer file|Vocabulary, merge rules, normalizer and special token|
| `tokenizer_config.json` |tokenizer behavior and chat templates|
| SafeTensors shards |Model weight tensor|
| generation config |Default sampling and stopping settings|
| model card |Training, Competencies, Limitations, Licensing and Instructions for Use|

`from_pretrained()` downloads and caches these assets, or they can be read from a local directory. The production environment should fix `revision` to avoid result changes after the warehouse content of the same model ID is updated.

## 3. chat template

Chat messages are structured objects:

```python
messages = [
    {"role": "system", "content": "The answer should be concise."},
    {"role": "user", "content": "Explain Fisher information."},
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
)
```

Different models use different control tokens. The template is responsible for:

\[
\{
\text{role},\text{content}
\}
\longrightarrow
\text{token sequence seen during training}.
\]

Wrong templates can lead to role confusion, unexpected continuations, or tool call format failures. Copying the `[INST]` string that looks similar to the naked eye on the web page cannot replace the template that comes with the model.

## 4. `pipeline` and underlying API

`pipeline` combines preprocessing, model forward and postprocessing:

```python
from transformers import pipeline

generator = pipeline(
    task="text-generation",
    model=model_id,
)
result = generator("The goal of CAT is to", max_new_tokens=80)
```

It is suitable for quick verification. When you need fine control over batch processing, KV cache, logits processor, token-level scores, or training loops, you should use the tokenizer and model API directly.

## 5. The role of generated parameters

Model output logits \(z\), temperature \(T\) change probability distribution:

\[
p_i=\frac{\exp(z_i/T)}{\sum_j\exp(z_j/T)}.
\]

- \(T<1\): distribution is sharper;
- \(T>1\): The distribution is flatter;
- Greedy decoding: directly take the maximum logit;
- top-p: Only sample from the smallest candidate set whose cumulative probability reaches \(p\).

`max_new_tokens` limits the new generation length and is generally easier to interpret than `max_length` which counts input and output mixed together.

## 6. Quantification and equipment placement

Transformers can be used with tools such as Accelerate, bitsandbytes, AWQ, GPTQ, etc. to use low-precision weights and automatic device maps. What changes the quantization configuration is the weight representation and some operators:

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

quant = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quant,
    device_map="auto",
)
```

Quantization reduces video memory and may introduce task-related errors. Evaluation must be done on the final quantized version, not substituted with full precision scores.

## 7. Training ability

The important boundary of Transformers is that it not only does inference, but also supports:

- pretraining or continuing pretraining;
- supervised fine-tuning；
- Fine-tuning tasks such as classification, annotation, and question and answer;
- Training LoRA with PEFT;
- Save, load and upload new checkpoints.

The core goal of llama.cpp is efficient inference; if the research focus is on modifying the model structure, calculating training gradients, or performing large-scale fine-tuning, the Transformers/PyTorch ecosystem is usually more straightforward.

## 8. Main limitations

- Generic abstraction brings Python and framework overhead;
- Support for an architecture does not mean that all quantization, tool calls, and multimodal paths are mature;
- `trust_remote_code=True` allows execution of model warehouse code and should only be used for trusted revisions;
- Single process `generate()` is suitable for experiments and does not equal high concurrent production serving;
- The Model Weights license is two different things than the Apache 2.0 license for the Transformers library.

