# Horizontal comparison of architecture, context and deployment

## 1. Unify objects before comparison

At least four items are fixed when comparing models: base or instruction version, model date, exact parameter size, and inference accuracy. Putting the 7B instruction model and the 100B level basic model in an accuracy table, the conclusion is difficult to interpret.

Below, we select the version of each family that best embodies the design ideas, rather than claiming to cover all the latest models.

|Dimensions| Command R | Mistral / Mixtral | Phi | Llama |
|---|---|---|---|---|
|Main form|decoder-only, directive and RAG optimization|decoder-only dense and sparse MoE|Small to medium decoder-only, and extended to multi-modal and inference versions|decoder-only dense, subsequent expansion of MoE and multi-modality|
|represents efficiency technology|GQA, long context| GQA、SWA、sparse MoE |Small parameter scale, data screening, quantitative deployment|GQA, long context, follow-up MoE|
|Ability to be clearly strengthened|grounded generation, references, tool calls|Generic build, code, local deployment, MoE|Small model reasoning, client-side and cost efficiency|General basic capabilities, dialogue alignment, and extensive ecology|
|weighted open features|Research weights, often with NC restrictions|change by checkpoint|Multiple official versions for MIT|Custom community license|

## 2. Dense and MoE

The Dense Transformer uses the same set of feedforward parameters for each token:

\[
h'=\operatorname{FFN}(h).
\]

MoE lets routers choose a small number of experts:

\[
h'=\sum_{e\in\operatorname{TopK}(g(h))}g_e(h)E_e(h).
\]

MoE can increase total capacity without excessively increasing single-token calculations, and should be reported at the same time when deployed:

- General parameters;
- Per-token activation parameters;
- Number of experts and top-\(k\);
- Number of devices required and communication method.

Just writing "17B active" underestimates weight residency and cross-device costs.

## 3. Long context and RAG

Long contexts and RAGs can complement each other:

```text
RAG: filter relevant fragments from large corpus
Long context: accommodate more candidate evidence and history in one inference
```

If you put all documents directly into the long context, the input cost and attention interference will increase. If you rely solely on retrieval, failure to recall will prevent the generative model from seeing the answer. Practical systems typically retrieve and rearrange first, and then synthesize a limited amount of evidence using long context.

Command R's training is more explicitly geared toward this process; other families can also perform RAG through prompts, fine-tuning, and tool frameworks. The difference should be verified by citation accuracy, rejection rate, and end-to-end latency.

## 4. Cost structure of small model and large model

The cost of a deployment includes at least:

\[
C_{	ext{total}}
=
C_{	ext{weights}}
+C_{	ext{prefill}}
+C_{	ext{decode}}
+C_{	ext{KV}}
+C_{	ext{serving}}.
\]

- Phi’s small parameter size mainly reduces weights and decoding costs;
- GQA mainly compresses KV cache;
- SWA mainly reduces attention connection costs;
- MoE mainly controls the calculation of activation per token, but still needs to save a large amount of total weight;
- RAG will increase the cost of retrieval, rearrangement, and input tokens, but may improve knowledge timeliness and traceability.

## 5. Base, Instruct and RAG specializations

|Type|training status|more suitable|
|---|---|---|
| Base |Mainly complete pretraining|Continue pretraining, domain adaptation, and mechanism research|
| Instruct / Chat |Add SFT and preference alignment|Direct dialogue, task following, product prototype|
| RAG / tool optimized |Specialized training on document formats, citations, or tool trajectories|Enterprise search, agent and grounded generation|

Using chat prompts directly on a base model is usually not a fair assessment; when continuing to train an already aligned chat model, you also need to prevent catastrophic forgetting of its instructions and safe behaviors.

## 6. Recommended unified assessment matrix

The selection experiment at least covers:

|indicator group|Example|
|---|---|
|task quality|Accuracy, F1, code test pass rate, artificial preference|
|Reliability|Hallucination rate, rejection rate, citation precision rate and recall rate|
|multilingual|Each target language is reported separately, without simple averaging to cover up weaknesses.|
|System cost|First token latency, tokens/s, peak memory, concurrent throughput|
|Robustness|Prompt changes, long context positions, adversarial documentation, tool failure|
|governance|Licensing, data residency, logging and auditing capabilities|

The final selection should be based on controlled experiments on the same hardware, the same quantification, the same prompt template, and the same business data.

