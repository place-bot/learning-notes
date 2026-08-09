# Alignment, Illusion and Reasoning

## 1. What does Alignment training change?

Pretraining learns a wide range of text distribution; alignment makes the output more consistent with helpfulness, safety, and task preferences. Typical process:

```text
Base model
  ↓ SFT demonstrations
Instruction model
  ↓ preference comparisons
Reward / preference model
  ↓ RLHF, DPO or other optimization
Aligned model
```

## 2. Preference data

For prompt \(x\), the annotator compares \(y^+\) with \(y^-\). Reward model is commonly used:

\[
\mathcal L_{RM}
=
-\log\sigma\left(r_\phi(x,y^+)-r_\phi(x,y^-)\right).
\]

Preference labels contain labeling norms and crowd values and are not objective truths.

## 3. KL constraints in RLHF

\[
R'(x,y)
=
r_\phi(x,y)
-\beta
\log\frac{\pi_\theta(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}.
\]

KL penalty limits the strategy away from the reference model, mitigating reward hacking and language degradation.

For the complete process of Llama 2, see [Llama 2 alignment topic](../llama2-2023/index.md).

## 4. Multiple sources of hallucinations

|Source|Example|major relief|
|---|---|---|
|Parameter knowledge error|Remember outdated facts|RAG, update data|
|Missing context|prompt no evidence|search, clarify|
|No context|Biased by interfering documents| rerank、context filtering |
|Decoding randomness|Sampling produces false details|Low temperature, verification|
|Alignment pressure|Always want to give answers|Training rejection and uncertainty|
|reasoning error|Intermediate steps fail|verifier, search, tool|

There is no single "dehallucination switch."

## 5. Self-consistency

Sampling multiple reasoning paths \(z_1,\ldots,z_K\), and aggregating the answers:

\[
\hat y
=
\arg\max_y
\sum_{k=1}^{K}
\mathbb I(g(z_k)=y).
\]

It can improve the stability of some verifiable reasoning tasks, but it increases the cost of reasoning exponentially and will still fail when most error paths are consistent.

## 6. Verifier

The generator proposes candidates, the verifier evaluation step or final result:

```text
Generate candidates
→ Check constraints / execute tests / score evidence
→ Select or revise
```

Calculator for math, run tests for code, and check references with RAG. When able to use external truth values, the verifier is more reliable than the model's self-confidence.

## 7. Inference-time computation

Improve the quality of individual questions through more sampling, searching, reflection or tool invocation. Its decision can be written as:

\[
\max_{c} Q(c)
\quad\text{s.t.}\quad
\operatorname{Cost}(c)\le B.
\]

Requests of different difficulty should use different computational budgets instead of a fixed maximum inference length for all requests.

## 8. Alignment in CAT

Educational feedback needs to be correct, age-appropriate, uninterrupted in measurement, and not reveal answers at the same time. Reward or preference goals should be broken into multiple indicators, retaining manual review and content policies. Model "friendliness" cannot trump measurement validity.

