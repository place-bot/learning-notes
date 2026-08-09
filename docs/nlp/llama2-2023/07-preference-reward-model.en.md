# Preference data and double Reward Model

## 1. How to collect data

The annotator first writes a prompt, and the system samples two answers from different model versions and different temperatures. The annotator must choose the better one and mark the preference strength:

- significantly better；
- better；
- slightly better；
- negligibly better / unsure。

Helpful and safe use different guidelines. Safety data also notes:

1. preferred safe, another unsafe;
2. Both are safe;
3. Both are unsafe.

The paper does not retain the pairing "preferred unsafe, another safe" because the safe answer should be preferred according to the guidelines.

## 2. Data scale

Meta self-collected safety + helpfulness preference comparisons total:

\[
1{,}418{,}091.
\]

Then mixed with public data such as Anthropic Helpful/Harmless, OpenAI Summarize/WebGPT, StackExchange, Stanford SHP and Synthetic GPT-J, the total number of comparisons is:

\[
2{,}919{,}326.
\]

A comparison includes shared prompt, chosen response and rejected response.

## 3. Reward model architecture

Initialized from pretrained chat checkpoint, it is the same as the main structure of the language model; remove the next-token vocabulary head and replace it with a regression head that outputs a scalar:

\[
r_\phi(p,y)\in\mathbb R.
\]

Initializing from the chat model allows the RM to inherit language and factual knowledge, reducing the risk of the reward model preferring hallucination due to insufficient knowledge.

## 4. Pairwise ranking loss

For preferred \(y_c\) and rejected \(y_r\):

\[
\mathcal L_{\mathrm{rank}}
=
-\log\sigma
\left(
r_\phi(p,y_c)-r_\phi(p,y_r)
\right).
\]

Optimization will increase the reward gap between chosen and rejected.

## 5. Preference margin

The paper uses preference strength to add margin:

\[
\mathcal L_{\mathrm{rank}}
=
-\log\sigma
\left(
r_\phi(p,y_c)-r_\phi(p,y_r)-m(q)
\right),
\]

Where \(q\) is the preference level. Use larger margins for answers that differ significantly; use smaller margins for close or uncertain comparisons.

## 6. Training mixture of two RMs

### Helpfulness RM

Use all Meta helpfulness, and then draw equal parts from Meta safety and public data.

### Safety RM

Use all Meta safety and Anthropic Harmless, with a 90/10 mix of safety master data and helpfulness data. A small amount of helpfulness is helpful for fine-grained comparisons of "both are safe".

## 7. Training configuration

- 1 epoch, continuing training will cause overfitting;
- Same optimizer parameters as base model;
- 70B max learning rate \(5\times10^{-6}\)；
- The rest of the scale \(1\times10^{-5}\);
- cosine decay to maximum 10%;
- Warmup is about 3% of the total steps, at least 5 steps;
- effective batch 512 pairs, that is, 1024 rows.

## 8. Reward model result

| RM | Meta Helpful | Meta Safety |average|
|---|---:|---:|---:|
| Safety RM | 56.2 | **64.5** | 64.3 |
| Helpfulness RM | **63.2** | 62.8 | **70.6** |

Helpfulness RM is stronger in its own domain, and Safety RM is stronger in the safety domain. The more obvious the preference, the higher the accuracy; for the negligibly better / unsure pairing, both are close to the mid-low 50%, reflecting task subjectivity and noise.

## 9. On-policy distribution problem

Preference batches are collected weekly. The distribution of new Chat model generation is constantly changing, so RM wants to see the latest model answers. Otherwise

\[
p_{\mathrm{new\ policy}}(y\mid p)
\ne
p_{\mathrm{RM\ train}}(y\mid p),
\]

RM accuracy will decrease, and policy will be more likely to exploit scoring blind spots.
