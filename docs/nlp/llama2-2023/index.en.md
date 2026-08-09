# Llama 2: Open weight based model and dialogue alignment

This topic is an intensive reading of **Llama 2: Open Foundation and Fine-Tuned Chat Models** by Touvron et al. The paper was released in 2023 and includes two types of models: the Llama 2 basic model after 2 trillion token pretraining, and the Llama 2-Chat obtained through SFT and RLHF on this basis.

## Capture the paper in one sentence

First train the general autoregressive basic models of 7B, 13B, 34B, and 70B; then use a small number of high-quality dialogue demonstrations to build the SFT model, continue to collect human preference comparisons, train helpfulness and safety reward models, and alternately use rejection sampling and PPO to align the model as a chat assistant.

## Complete training route

```text
Publicly available online corpora
        ↓ 2T token autoregressive pretraining
Llama 2 base model
        ↓ 27,540 high-quality SFT annotations
Llama 2-Chat-SFT
        ↓ Preference comparison → Helpfulness RM + Safety RM
        ↓ Rejection Sampling + PPO, multiple rounds of iteration
        ↓ Safety SFT / Safety RLHF / Context Distillation / Red Teaming
Llama 2-Chat
```

## Citation details

|item|information|
|---|---|
|Author|Hugo Touvron and 68 other authors|
|publish| arXiv:2307.09288，2023 |
|Original text| [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) |
|Official warehouse| [meta-llama/llama](https://github.com/meta-llama/llama) |
|Official model card| [Llama 2 model card](https://github.com/meta-llama/llama-models/blob/main/models/llama2/MODEL_CARD.md) |
|Model size|7B, 13B, 34B, 70B; focus on 7B, 13B, 70B during public release|
|context| 4096 token |

## Reading route

1. [Paper question, contribution and model family](01-question-contributions.md)
2. [Complete pipeline of basic model and Chat model](02-base-chat-pipeline.md)
3. [pretraining data, tokenizer and optimization](03-pretraining-data-tokenizer.md)
4. [RMSNorm, SwiGLU, RoPE and GQA](04-architecture.md)
5. [Basic model experiment and evidence analysis](05-base-experiments.md)
6. [Supervised fine-tuning: Why a small amount of high-quality data is effective](06-supervised-finetuning.md)
7. [Preference data with double Reward Model](07-preference-reward-model.md)
8. [Rejection Sampling iteration fine-tuning](08-rejection-sampling.md)
9. [PPO, combination rewards and KL constraints](09-ppo-rlhf.md)
10. [Secure fine-tuning, Context Distillation and Red Team](10-safety-training.md)
11. [Ghost Attention and multi-round consistency](11-ghost-attention.md)
12. [Helpfulness, security experimentation and evaluation boundaries](12-chat-evaluation.md)
13. [Official code, chat templates and open borders](13-code-release.md)
14. [Limitations, conclusions and method evolution](14-limitations-conclusion.md)
15. [References and primary information](references.md)

## The position of this paper in the learning route

GPT-3 mainly studies in-context learning under fixed parameters. The focus of Llama 2 turns to: how to continuously train the pretraining basic model into a model that is more in line with human preferences and suitable for dialogue deployment, and at the same time release the weight and inference code for external research and development.

The key difference between the two can be first recorded as:

\[
\text{GPT-3 few-shot}
=
\text{Context changes behavior},
\]

\[
\text{Llama 2-Chat alignment}
=
\text{SFT/RLHF permanently change parameters}.
\]
