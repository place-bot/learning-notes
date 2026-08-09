# Limitations, conclusions and future updates

## 1. What is this book suitable to solve?

It provides a map covering the LLM life cycle and is particularly suitable for:

- People who have understood basic deep learning and want to connect models and applications;
- People who need to choose between RAG, fine-tuning, agent and inference;
- Teams that want to understand the source of failure rather than just copy the demo;
- Researchers who want to upgrade a single-model prototype to a multi-component system.

## 2. What do you need to add when reading?

### Rapidly changing software interface

Models, frameworks, licenses and APIs will continue to be updated. The stable value in the book is the principle and decision-making dimension; specific commands should be returned to the current official documents.

### Single paper evidence

A comprehensive book spans many topics and is no substitute for the original papers, experiments, and code for each method. This website supplements the evidence through intensive reading of single articles such as Transformer, LoRA, GPT, and Llama 2.

### Domain evaluation

General benchmarks cannot replace the validity, fairness and risk assessment of medical, financial, education and CAT.

## 3. Prototype to Production Checklist

```text
task definition
→ Data and Privacy
→ tokenizer and model version
→ Baseline and evaluation set
→ prompt / RAG / fine-tuning selection
→ Reasoning cost and serving
→ tool permissions and guardrail
→ tracing and failure analysis
→ Online monitoring and rollback
```

## 4. Five core decisions

1. **Where is the knowledge placed**: parameters, prompts, search libraries or tools?
2. How does **behavior change**: prompts, SFT, preference optimization, or program constraints?
3. **How to verify correctness**: indicators, evidence, actuators or manual labor?
4. **How to control costs**: small model, cascade, cache, quantification or concurrency?
5. **Who is responsible for the risk**: Model rejection cannot replace system permissions and governance.

## 5. Final explanation of tokenizer recommendations

It is reasonable to recommend this book to go deep into tokenizer, because Chapter 3 not only lists BPE and WordPiece, but also puts them in the complete pipeline of vocabulary, normalization, pre-tokenization and special token.

If the goal is to accurately understand the algorithm, you should first read the formulas, hand calculations and official code of this site [Subword Tokenization Special Topic](../subword-tokenization/index.md)], and then return to the book to observe how tokenizer affects the entire LLM life cycle.

## 6. Final inspiration for CAT

Generative CAT does not tokenize items and then let the large model output a set of questions at a time. It is a multi-layered system:

```text
Real-time feedback from students
→ Calibration status update
→ Content and item bank constraints
→Long term strategies learned
→ Re-decision every step
```

The advantages of LLM are mainly in semantics, content, open answers and explanations; its adaptability comes from status updates and policy recalculation after each interaction step.

## 7. Conclusion

The most valuable framework of this book is: LLM application consists of data, model and system. Improvements at any one layer may be offset by errors at another layer.

```text
Good model + bad search = unfounded answer
Good retrieval + bad generation = evidence not used correctly
Good build + bad permissions = dangerous tool behavior
Good strategy + bad measurement = unreliable CAT
```

The goal of system design is to allow each layer's accountability, evidence, and failure boundaries to be independently inspectable.

