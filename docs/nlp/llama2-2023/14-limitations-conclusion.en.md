# Limitations, conclusions and method evolution

## 1. Model limitations

Thesis acknowledges:

- Knowledge will no longer be automatically updated after pretraining;
- Will hallucinate, give inaccurate or unqualified advice;
- Mainly for English, other languages are fragile;
- May generate harmful, offensive or biased content;
- Security fine-tuning is sometimes excessive, resulting in false refusal;
- Conversation models may be used for malicious purposes such as disinformation and cybercrime;
- The base model lacks sufficient security alignment and the deployment risk is higher.

## 2. Limitations of methodological evidence

### 2.1 Data opacity

The corpus is described only as a "mixture of publicly available sources", which cannot fully reproduce data selection, copyright status, contamination and group representativeness.

### 2.2 Alignment data is not public

The core SFT, Meta preference and reward models have not been released, and it is difficult to reproduce the most valuable chat alignment pipeline of the paper externally.

### 2.3 Manual evaluation scope

Helpfulness is about 4K prompts, excluding coding/reasoning; security is about 2K adversarial prompts. Version, description, and review group all influence conclusions.

### 2.4 RM optimization bias

The reward model is an approximation of human preferences. PPO and best-of-N will actively search for their blind spots. KL, manual review and continuous new data can only alleviate but not eliminate them.

### 2.5 Security and Helpful Dynamic Conflict

Increased security data will reduce dangerous output and may also increase normal request rejections. A single violation metric rewards short, overly conservative responses.

## 3. Interesting but preliminary observation

Thesis report:

- RLHF makes the output of the factual prompt more stable as the temperature changes, while the creative prompt remains diverse;
- A certain time organization capability appears with only 1000 strips of date SFT data;
- When tool calls are not specifically annotated, the model can still understand the calculator/API semantics and combine calls in the prompt.

These observations are derived from limited manual testing or specific experiments, require more rigorous replication and mechanism research, and cannot be regarded as a general guarantee.

## 4. From GPT-3 to Llama 2

|Dimensions| GPT-3 | Llama 2 |
|---|---|---|
|Main questions|How scale enhances in-context learning|How to publish a strong base model and train a secure chat model|
|Parameter update|The downstream main experiment is not updated|SFT/RLHF continuously updated|
|largest model| 175B | 70B |
|training token| 300B | 2T |
| context | 2K | 4K |
|Alignment|The focus of the paper is not on RLHF| SFT + dual RM + RS + PPO + safety |
|publish|no weight|Weights available under custom license|

Llama 2 has fewer parameters, but uses more tokens for training, and devotes a lot of research resources to post-training. This reflects a paradigm change: model capability is determined by pretraining and alignment.

## 5. The most important methodological inspiration of the paper

### 5.1 Base and assistant layering

Language proficiency, task knowledge, and deployment behavior need to be assessed separately. A strong basic model benchmark does not mean that the chat is safe; a large number of chat rejections does not mean that the basic knowledge is weak.

### 5.2 High quality SFT responsible for startup

Tens of thousands of carefully designed demonstrations establish conversational formats and initial behaviors, but full alignment still relies on large-scale preference feedback.

### 5.3 Preference pipeline must be on-distribution

After the policy is changed, new answers must be continuously collected and compared to allow RM to keep up with the generated distribution.

### 5.4 Security is an iterative system

Security SFT, RM, RLHF, context distillation, red teaming, deployment filtering and monitoring need to form a closed loop.

### 5.5 Inference efficiency enters model design

GQA directly targets KV cache and throughput, indicating that open deployment costs have become part of the architecture choice.

## 6. Conclusion

Llama 2's contribution is more than just a set of downloadable models. The paper breaks the training of modern chat models into discussable modules: pretraining, SFT, preference data, double RM, rejection sampling, PPO, KL, safe fine-tuning, multi-round consistency and red team.

It also leaves key open questions: how training data and alignment data are released transparently, how reward models avoid exploitation, how security generalizes across languages and scenarios, and how open weight models balance researchability, licensing, and deployment responsibilities.
