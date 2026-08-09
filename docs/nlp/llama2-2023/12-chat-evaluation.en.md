# Helpfulness, security experimentation and evaluation boundaries

## 1. Helpful human evaluation

The authors compare Llama 2-Chat with Falcon, MPT, Vicuna, ChatGPT, and PaLM-chat on more than 4000 single-turn and multi-turn prompts. Each comparison was scored by three judges.

Main result:

- 7B vs. MPT-7B-chat, about 60% prompts win;
- 34B vs. Vicuna-33B and Falcon-40B, the total win rate exceeds 75%;
- 70B vs. ChatGPT: win 36%, tie 31.5%;
- 70B significantly outperforms PaLM-bison chat on this prompt set.

Taking half of the tie into account gives an approximate preference score:

\[
36+\frac{31.5}{2}=51.75.
\]

This explains the paper saying that 70B is competitive with ChatGPT, but does not mean that it is significantly better than others across the board.

## 2. Inter-rater reliability

Helpfully using a 7-point Likert scale, Gwet’s AC2 is approximately 0.37–0.55. The closer the model is, the more difficult it is for the review to be consistent; the generated evaluation itself is obviously subjective.

## 3. Limitations of manual helpful evaluation

The paper clearly lists:

- About 4K prompts cannot cover real use;
- prompt does not include coding/reasoning;
- Only the last generation of multiple rounds of dialogue will be evaluated;
- Different evaluator instructions will change the result;
- ChatGPT is fixed to `gpt-3.5-turbo-0301`, and the model version is temporal.

## 4. Safety manual evaluation

Collect about 2000 adversarial prompts:

- 1351 single-turn；
- 623 multi-turn。

Each answer is scored on a scale of 1–5: 1–2 counts as a safety violation, 3–5 does not count as a violation. Three judges majority vote. Safe Gwet’s AC2 is around 0.70–0.95 across batches, Llama 2-Chat averages around 0.92.

## 5. Multiple rounds are more dangerous

The paper observes that most models have higher violation rates on multi-turn prompts. An attacker can gradually establish context, hide intent, or cause the model to lose security constraints between front and rear wheels.

Falcon's single-round violation rate is low, but its answers are short and less helpful; looking only at violation percentage rewards a "say nothing" strategy, so it is also necessary to combine average helpfulness with safety scores.

## 6. Automatic security benchmark

| Fine-tuned model | TruthfulQA ↑ | ToxiGen ↓ |
|---|---:|---:|
| ChatGPT | 78.46 | 0.20 |
| Falcon-instruct 7B | 28.03 | 7.89 |
| MPT-instruct 7B | 29.99 | 16.33 |
| Llama 2-Chat 7B | 57.04 | 0.00 |
| Llama 2-Chat 13B | 62.18 | 0.00 |
| Llama 2-Chat 34B | **67.20** | 0.02 |
| Llama 2-Chat 70B | 64.14 | 0.01 |

70B base to chat:

\[
\text{TruthfulQA}:50.18\to64.14,
\]

\[
\text{ToxiGen}:24.60\to0.01.
\]

## 7. Limitations of automatic indicators

- toxicity classifier may have subgroup bias;
- Templated rejection reduces toxicity but reduces helpfulness;
- TruthfulQA only covers specific misconceptions;
- BOLD sentiment cannot fully represent fairness;
- There are product and social intermediaries between indicators and real harm.

## 8. Circularity of Reward-model evaluation

If you use your own RM to select a model and use the same RM to evaluate the model, you will be biased towards Llama 2-Chat. Therefore, the paper also uses GPT-4 judge and manual evaluation for cross-validation. GPT-4 judge also has issues with bias, prompt sensitivity, and closed-source versions.

The most reliable way to read it is to see if multiple reviews give consistent directions while preserving the boundaries of the prompt set and review scope.
