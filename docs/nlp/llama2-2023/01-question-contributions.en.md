# Paper questions, contributions and model families

## 1. Research questions

There are many public base models in 2023, but high-quality chat systems tend to come from closed-source products. The base model will continue to write text, but may not consistently follow instructions, reject dangerous requests, or sustain multiple rounds of dialogue. Dialog alignment requires extensive annotation, reward modeling, RLHF, and safety engineering, and these steps often lack transparent description.

The paper solves two problems at the same time:

1. How to train a competitive basic model that can obtain weights;
2. How to systematically align the basic model into a more helpful and secure chat model.

## 2. The two types of models must be separated

### Llama 2

General basic language model, only accepts autoregressive pretraining. It is suitable for completion, research and subsequent fine-tuning and does not target chat assistant behavior by default.

### Llama 2-Chat

Initialized from Llama 2, it accepts SFT, reward modeling, rejection sampling, PPO and safe fine-tuning in order. It uses specialized chat templates and is optimized for dialogue use cases.

Under the same parameter scale:

\[
\theta_{\mathrm{Chat}}
\ne
\theta_{\mathrm{Base}}.
\]

## 3. Model family

|model|pretraining token| context | GQA |peak learning rate|
|---|---:|---:|---|---:|
| Llama 2 7B | 2.0T | 4K |No| \(3.0\times10^{-4}\) |
| Llama 2 13B | 2.0T | 4K |No| \(3.0\times10^{-4}\) |
| Llama 2 34B | 2.0T | 4K |Yes| \(1.5\times10^{-4}\) |
| Llama 2 70B | 2.0T | 4K |Yes| \(1.5\times10^{-4}\) |

All models use a global batch size of 4M tokens. The paper studied 34B, but the main public download sizes for model families are 7B, 13B, and 70B.

## 4. Main contributions

### 4.1 Stronger basic model

Compared with Llama 1, the training tokens are increased by about 40%, the context is increased from 2K to 4K, data mixing and cleaning are updated, and GQA is used in large models to improve inference scalability.

### 4.2 Detailed alignment pipeline

Public description of the paper:

- 27,540 high-quality SFT annotations;
- Over 1.4 million Meta human preference comparisons;
- help/safety two independent reward models;
- preference margin ranking loss；
- Alternating iterations of rejection sampling and PPO;
- KL penalty and reward whitening;
- Ghost Attention for consistency over multiple rounds.

### 4.3 Security training and evaluation

Including secure SFT, secure RLHF, context distillation, more than 350 people on the red team and about 2000 human security evaluations against prompts.

### 4.4 Weight and inference code release

Meta provides model weights and minimal inference code through a custom Llama 2 Community License, allowing many research and commercial uses, with usage restrictions. The correct term is "open weight" or "accessible weight"; the license is not an unconditional open source license.

## 5. Core evidence of the paper

-Basic Llama 2 is generally better than Llama 1, MPT and Falcon of the same scale in the paper summary benchmark;
- Continuous improvements in rewards and artificial preferences from SFT to multi-round RLHF versions;
- Llama 2-Chat significantly outperformed the then open source chat baseline on the author's human evaluation prompt set;
- 70B has a win rate of 36% and a tie rate of 31.5% for ChatGPT;
- After safety tuning, 70B’s ToxiGen indicator dropped from 24.60 to 0.01, and TruthfulQA increased from 50.18 to 64.14.

These results depend on the prompt, review specifications, model version and decoding settings selected by the author, and cannot be directly extrapolated to all deployment scenarios.
