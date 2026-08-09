#Llama: From research release to open weight ecosystem

## 1. Intergenerational main line

The influence of Llama comes not only from the model itself, but also from the fine-tuning, quantification, reasoning and data ecology formed around weights.

|intergenerational|Represent scale and context|Main changes|
|---|---|---|
| LLaMA 1 | 7B、13B、33B、65B |Proves that smaller models with more tokens can achieve strong basic capabilities; initially intended for research use|
| Llama 2 | 7B、13B、70B，4K |Added publicly available training data, GQA (70B), and Chat version of SFT + RLHF|
| Llama 3 | 8B、70B，8K |Larger tokenizer, improved data and training scale|
| Llama 3.1 | 8B、70B、405B，128K |Long context, multiple languages, and the 405B model|
| Llama 3.2 / 3.3 |1B, 3B, visual version and 70B update|Side dimensions, visual input and capabilities updates|
| Llama 4 |Scout, Maverick and other MoE versions|Sparse experts, multimodality, and longer context|

Tables are used to explain method evolution. Each generation contains different checkpoints such as base, instruct, or multimodal, and generation names cannot be used in place of exact model IDs.

## 2. What did Llama 2 establish?

Llama 2 clearly writes a complete open-weighted dialogue model route:

```text
2T token autoregressive pretraining
  ↓
High quality supervision fine-tuning
  ↓
Helpfulness/Security Preference Data
  ↓
Reward Models
  ↓
Rejection Sampling + PPO
  ↓
Llama 2-Chat
```

This site has explained this pipeline step by step in [Llama 2 Intensive Reading of Papers](../llama2-2023/index.md). The family topic focuses more on how it evolves into a multi-size, multi-modal and long-context ecology.

## 3. Why tokenizer extension is important

Llama 3 expands the vocabulary to about 128K tokens and adopts a tokenizer based on tiktoken. A larger vocabulary might use fewer tokens to represent common words and multilingual fragments, thus changing:

- The length of context occupied by the same text;
- embedding and output layer parameters;
- Multi-language and code segmentation granularity;
- Compatibility of old fine-tuning data and templates.

Therefore, the Llama 2 adapter cannot be directly installed on Llama 3 because the architecture names are similar. The tokenizer, vocabulary size and weight shape may be inconsistent.

## 4. Engineering implications of long context

Llama 3.1 extends the context to 128K. Long context brings more original materials, while increasing prefill calculation and KV cache:

\[
\text{KV cache}
\propto
L\times n\times h_{kv}\times d_h,
\]

Among them, \(L\) is the number of layers, \(n\) is the number of cache tokens, \(h_{kv}\) is the number of key/value heads, and \(d_h\) is the head dimension. GQA controls this cost by reducing \(h_{kv}\).

Just because a model states that it supports 128K does not mean that it utilizes 128K equally efficiently on all tasks. Long document question and answer still needs to measure the location of key information, interfering documents, citation accuracy and first token delay.

## 5. MoE direction for Llama 4

Llama 4's Scout and Maverick use mixture-of-experts. Similar to Mixtral, the model has a larger total parameter capacity, but each token only activates some experts. The advantages of MoE mainly come from increasing the model capacity that can be called by unit forward calculation, while the engineering costs include weight loading, expert parallelism and cross-device communication.

## 6. Why Llama has a huge ecosystem

Open weight enables the community to:

- Perform LoRA or full-parameter domain fine-tuning;
- Produce 8-bit, 4-bit or lower precision quantization;
- Deploy at runtime in llama.cpp, vLLM, Transformers, etc.;
- Research distillation, synthetic data and model merging;
- Independent safety evaluation of the same weight.

Ecological compatibility is still bounded by versions. Chat templates, special tokens, RoPE configurations, GQA headers, and licenses should all be saved with the model.

## 7. Llama’s license boundaries

Meta releases weights using various generations of the Llama Community License. Taking Llama 4 as an example, the license stipulates attribution, redistribution, acceptable use, and additional commercial terms for very large-scale monthly active products. These custom terms are different from Apache 2.0 or MIT.

Therefore, Llama's most accurate technical classification is the **Open Weight Model Family**. Some of the tools in the repository may be licensed under standard open source licenses, but the weighted license cannot be described as MIT or Apache 2.0.

