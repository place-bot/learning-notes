# How to choose: three lines: tasks, computing power and licenses

## 1. Start from the task link

### Enterprise knowledge base and traceability Q&A

Test the grounded generation of Command R first, and also use Mistral, Phi or Llama with the unified RAG framework as a baseline. The core metric is whether the quote actually supports the answer, not just natural language fluency.

### Local, offline and end-side operation

Prioritize starting with a Phi mini, small Llama, Minitral or Mistral 7B class model. Determine the device's available memory, context length, and concurrency before selecting the quantization precision.

### High throughput general service

Compare the batch processing efficiency of the dense model with the device communication cost of the MoE model. Parameter rankings cannot replace real service stress testing.

### Continue training in the field

It is necessary to confirm whether there is a base checkpoint, whether the tokenizer is stable, whether the license allows derivative models and redistribution, and whether the training framework can fully load the architecture.

### Tool agent

Compare tool calling schema accuracy, parameter filling accuracy, failure recovery, multi-step completion rate and unnecessary call rate. Specialized training of Command R is a meaningful candidate starting point, and instruct versions of other families should also be tested in the same agent harness.

## 2. An executable funnel

```text
Licensing and data governance hard constraints
        ↓ Filter
Hardware, latency and context budget
        ↓ Filter
Target task offline evaluation
        ↓ Sort
Small-scale real traffic/manual blind review
        ↓
Deployment, monitoring and rollback
```

Applying hard constraints first can avoid spending a lot of evaluation resources on models that are impossible to go online.

## 3. License decision table

|question|What to check if the answer is "Yes"|
|---|---|
|Will the product be charged or used for internal business within the company?|Whether commercial use is allowed; NC terms usually require additional authorization|
|Will the weights or adapter be sent to customers?|Redistribution, Attribution, License Copy and Naming Requirements|
|Will the output be used to train another model?|Output usage and model improvement terms|
|Is the monthly service scale large?|Scale threshold in custom community license|
|Will it operate in high-risk areas such as healthcare, education scoring, or finance?|Acceptable use policies, industry regulations, and manual review|

## 4. Rough calculation of video memory

Assume that the model parameter quantity is \(P\), the weight bit width is \(b\), and only the theoretical occupation of the weight is:

\[
M_{\text{weights}}=P\frac{b}{8}.
\]

For example 7B model:

|Accuracy|Only weight theoretical value|
|---|---:|
| BF16 / FP16 |Approximately 14 GB|
| INT8 |About 7 GB|
| INT4 |Approx. 3.5 GB|

The deployment also needs to add KV cache, runtime workspace, activation and quantification metadata. Long contexts and high concurrency may overwhelm KV cache weight savings, so this must be measured with target batch and sequence lengths.

## 5. A minimal evaluation protocol

1. Fix 200–1000 representative business samples and retain difficult subsets;
2. Fixed system prompt, search result and tool definition;
3. Each model uses its official chat template;
4. Test the original accuracy and the quantitative accuracy of the planned deployment respectively;
5. Report average value, failure type and confidence interval;
6. Anonymous random sorting and double review of open-ended responses;
7. Save model revision, dependency versions, random seeds, and complete output.

## 6. Inspiration for education and CAT research

If these models are used for CAT, model family selection should be guided by the measurement objectives:

- Item content encoding can use small Phi or Llama representation models, but measurement invariance needs to be verified;
- item bank document retrieval and basis description testable Command R-style grounded generation;
- Local security deployments can compare to small Mistral, Phi and Llama;
- When generating items or explanations, item parameters, content blueprints and audit rules should be placed as external constraints on the model;
- No LLM can rely on language fluency to replace item calibration, exposure control, fairness and validity evidence.

The model is the content understanding or strategy component of the CAT system, and the final measurement quality still needs to be verified through student response data.

