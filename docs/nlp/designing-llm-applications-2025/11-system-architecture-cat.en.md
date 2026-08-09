# System architecture, Router and CAT interface

## 1. Why use multiple models

A single large model can be costly, have high latency, and not be good at all tasks. Multi-LLM systems assign requests to specialized components.

## 2. Cascade

Call the cheaper model first, and then upgrade if the reliability is insufficient:

```text
request
→ small model
→ confidence / verifier
   ├── pass → return
   └── fail → large model
```

Expected cost:

\[
\mathbb E[C]
=
C_s
+P(\text{escalate})C_l.
\]

The key is to define the conditions for reliable upgrades.

## 3. Router

\[
r^*(x)=\arg\max_r
\left[Q(r,x)-\lambda C(r,x)\right].
\]

Router can select models based on task type, language, risk, length, and difficulty. The Router itself also evaluates the misrouting rate.

## 4. Task-specialized models

A system can be used separately:

- embedding model；
- reranker；
- generator；
- moderation model；
- reward/verifier；
- OCR or vision model;
- Small structured extractor.

Specialized models are often more testable than having one chat model go through all the stages.

## 5. Programmatic LLM systems

Frameworks like DSPy treat prompts and examples as optimizable program components; languages like LMQL provide generation constraints and control structures. The value is in making the LLM pipeline closer to an explicit program rather than a scattering of strings.

## 6. A CAT-oriented system architecture

```text
students answer
   ↓
Response recording and real-time status
   ↓
Measurement layer: IRT/CDM/Student model
   ↓
Legal action layer: answered questions, content, exposure, enemy questions, item bank availability
   ↓
Topic selection strategy: traditional information volume / RL / learned policy
   ↓
item presentation
   ↓
Next time student feedback
```

LLM can access:

```text
item content embedding
Knowledge points and question types extraction
Open answer analysis
item retrieval and basis description
Natural language feedback
Generating candidate questions and manual review
```

## 7. The key to ensuring Adaptive

The status must be updated after each interaction:

\[
s_{t+1}=U(s_t,j_t,y_t),
\]

Then select:

\[
j_{t+1}\sim\pi(\cdot\mid s_{t+1},\Omega_{t+1}).
\]

If LLM generates the entire set of fixed sequences at once, it cannot use the intermediate answer \(y_t\). More reasonable generative interfaces are stepwise decision-making, rolling replanning, or generating contingent policies.

## 8. Division of labor between LLM and measurement layer

|layer|More suitable technology|
|---|---|
|Capacity and Error Estimation| IRT、CDM、Bayesian student model |
|Semantics and content representation| Transformer、embedding、LLM |
|serial long term value| RL、planning、learned policy |
|hard constraints|mask, shadow test, combination optimization|
|Explanation and feedback| LLM + evidence + template |

## 9. Evaluation matrix

Don’t just look at accuracy:

- Measurement error and test length;
- content balance；
- Exposure and item bank utilization;
- Individual real-time adaptation;
- fairness;
- delay;
- Interpretation fidelity;
- Security and privacy.

The systems perspective in the book supports exactly this kind of multi-layered evaluation.

