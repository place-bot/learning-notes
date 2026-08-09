# Model selection, loading and decoding

## 1. Define the task first, then look at the ranking list

Model selection is constrained optimization:

\[
m^*
=
\arg\max_m Q(m)
\quad
\text{s.t.}
\quad
C(m)\le B,
\ L(m)\le L_{\max},
\ G(m)=1.
\]

Among them, \(Q\) is the service quality, \(C\) is the cost, \(L\) is the delay, and \(G\) is the license and governance feasibility.

## 2. Model flavor

|Type|Usage|
|---|---|
| Base |Continue pretraining, research and custom alignment|
| Instruct / Chat |Direct task following and dialogue|
| Code |Code completion, generation and software engineering|
| Embedding |Vector retrieval, clustering and reranking prefix|
| Reasoning |Difficult reasoning and more inference-time compute|
| Multimodal |Joint input of text, images, audio, etc.|

The corresponding chat template, tokenizer and generation config must be used after selection.

## 3. Open weight and API

Need to evaluate separately:

- Whether the weights can be downloaded;
- Commercial use and redistribution terms;
- Whether the data must leave the local area;
- Whether the model version is stable;
- Local hardware and operation and maintenance costs;
- API pricing, rates, and logging policies.

For detailed model family comparison, see [Open weight model family](../open-weight-model-families/index.md).

## 4. Decoding

Temperature：

\[
p_i(T)=\frac{\exp(z_i/T)}{\sum_j\exp(z_j/T)}.
\]

Top-k only retains the \(k\) tokens with the highest probability; top-p retains the smallest set with a cumulative probability of \(p\). Greedy decoding takes the maximum logit at each step, and beam search retains multiple sequence candidates.

The decoding strategy changes the output distribution without changing the model parameters. Structured extraction often uses low temperature or constrained decoding; creative generation can increase sampling diversity.

## 5. Structured output

Merely asking for JSON in the prompt does not guarantee correct syntax. More robust layers include:

```text
Natural language requirements
→ JSON mode
→ JSON Schema constrained decoding
→ Application layer validation
→ retry / repair / human review
```

Valid syntax does not guarantee that field values are true.

## 6. Unified evaluation protocol

Each candidate model uses:

- Same business sample;
- Correct chat templates for each;
- Fixed search results and tool schema;
- Identical or explicitly documented generation parameters;
- Target deployment accuracy and quantified version;
- Combination of blind evaluation and automatic indicators;
- Failure type instead of just average score.

## 7. Loading layer and application layer

Transformers, llama.cpp and LangChain are on different layers. See [LLM software stack](../llm-software-stack/index.md) for complete differentiation. Successful loading of the model only indicates that the weights can be executed, but does not indicate that prompts, tools, memory, and production concurrency have been designed.

