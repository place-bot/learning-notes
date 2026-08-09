# How to interpret the scale curve and experimental results

## 1. The overall trend observed in the paper

On the aggregated 42 accuracy class benchmarks:

- zero-shot improves steadily with model size;
- One-shot is usually higher than zero-shot;
- few-shots tend to grow the fastest;
- The larger the scale, the more obvious the differences between the three settings are often.

This supports the behavioral conclusion that large models are better at exploiting contextual examples.

## 2. Relationship with loss scaling

Early scaling law research found that validation loss approximately decreases as a power law with parameters, data, and calculations. It can be conceptualized as:

\[
L(N)\approx L_\infty+aN^{-\alpha}.
\]

GPT-3 further checks whether downstream task performance also changes smoothly with \(N\). Many tasks are roughly smooth, but accuracy has threshold and saturation effects and is not always accurately described by a single power law.

## 3. Why does a small decrease in loss bring about a large change in accuracy?

Classification only cares about whether the correct candidates outnumber the incorrect candidates. Let margin:

\[
m
=
\log p(y_{\mathrm{correct}}\mid c)
-
\log p(y_{\mathrm{wrong}}\mid c).
\]

As soon as scale growth takes \(m\) from slightly less than 0 to slightly greater than 0 for many samples, accuracy may suddenly rise, even if the average LM loss only improves smoothly.

## 4. Task heterogeneity

Scaling trends did not eliminate task structure differences:

- LAMBADA, TriviaQA, COPA, ReCoRD are strong;
- WiC, DROP, and high-digit arithmetic are still weak;
- one-shot is sometimes lower than zero-shot;
- few-shot examples may introduce formatting confusion.

Therefore, there is no unified breakpoint that "all tasks are automatically resolved after 175B".

## 5. Amount of training information compared with SuperGLUE

In the paper picture:

- fine-tuned BERT-Large using SuperGLUE ~125K training examples;
- BERT++ also pre-fine-tuned MultiNLI 392K and SWAG 113K, totaling about 630K fine-tuning examples;
- GPT-3 few-shot uses up to 32 examples per task context and does no gradient updates.

This shows that GPT-3's task-specific tags are efficient. However, GPT-3 has used 300B unlabeled pretraining tokens and Yuanda Computing. The two "data efficiencies" cannot be summarized only by the number of downstream labels.

## 6. Parameter efficiency and calculation efficiency

The 175B model implements adaptation with very few task labels, but activates all model parameters and reads demonstrations repeatedly in each inference. It is efficient in task switching, but expensive in terms of single computing power, video memory and latency.

## 7. What ablations are missing?

The paper mainly compares the model size and the number of shots, but there is no complete separation:

- Number of training tokens;
- Data filtering and mixture;
- dense/sparse attention；
- width and depth;
- tokenizer；
- prompt template;
- Example selection strategies.

So "scale" represents the resulting change in the entire scaling recipe.

## 8. A careful understanding of emergence

Some discrete indicators seem to appear suddenly in large models, which may come from:

- The underlying probability margin smoothly crosses the decision threshold;
- Indicators are saturated or discontinuous;
- prompt and decoding are non-linear;
- Small sample variation.

GPT-3 provides early critical evidence of large-scale capability curves. Determining the true mechanistic phase transition also requires denser model scale, continuous indicators and statistical uncertainty.
