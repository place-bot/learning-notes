# Fine-tuning, PEFT and domain adaptation

## 1. When is fine-tuning needed?

Fine-tuning is suitable for changing stable behavior:

- Fixed output format;
- Professional style and terminology;
- Classification, extraction and scoring rules;
- Tool calling mode;
- Task-specific decision boundaries.

Facts that change frequently are better suited for retrieval. Problems that Prompt can solve reliably may not require training.

## 2. Supervise fine-tuning goals

Given instruction \(x\) and target answer \(y\):

\[
\mathcal L_{\mathrm{SFT}}
=
-\sum_{t=1}^{|y|}
\log p_\theta(y_t\mid x,y_{<t}).
\]

Normally loss is calculated only on assistant output, with system/user token used as condition.

## 3. Optimize parameters

Need to decide together:

- learning rate and scheduler;
- batch size and gradient accumulation;
- sequence packing；
- epochs and early stopping;
- weight decay；
- max sequence length；
- mixed precision；
- gradient checkpointing。

The small amount of data does not mean that the validation set can be ignored. Too large a learning rate will destroy the existing capabilities, and too many epochs will memorize the format and samples.

## 4. LoRA

Freeze the original weights \(W_0\) and train low-rank increments:

\[
W=W_0+\frac{\alpha}{r}BA,
\]

\[
A\in\mathbb R^{r\times d_{\mathrm{in}}},
\quad
B\in\mathbb R^{d_{\mathrm{out}}\times r}.
\]

LoRA reduces trainable parameters and optimizer state. For detailed mechanisms, see [LoRA topic](../lora-2022/index.md).

## 5. Continual pre-training

When the domain corpus does not have the instruction-output tag, you can continue to use the language-model objective:

\[
\mathcal L_{\mathrm{DAPT}}
=
-\sum_t\log p_\theta(x_t\mid x_{<t}).
\]

It changes the domain language distribution, and subsequently requires instruction tuning to restore the task interface.

## 6. Replay and forgetting

Training only on new domain data can cause catastrophic forgetting. Replay mixes in common data:

\[
\mathcal L
=
\lambda\mathcal L_{\mathrm{domain}}
+(1-\lambda)\mathcal L_{\mathrm{general}}.
\]

\(\lambda\) Control domain adaptation and general capability maintenance.

## 7. Adapter merging and model fusion

Multiple adapters can be dynamically loaded, weighted, or merged per task. Risks include:

- The target module is incompatible;
- tokenizer and base revision are inconsistent;
- Parameter directions interfere with each other;
- Each adapter is effective individually and degrades after combination.

Needs to be re-evaluated on the combined version and cannot be inferred from single adapter scores.

## 8. Data quality is greater than format quantity

High-quality SFT data should contain clear instructions, correct output, failure boundaries, rejections, and difficult examples. Large amounts of templated synthetic data can lead to style collapse and over-congratulation.

## 9. CAT adaptation

The model can be fine-tuned to understand item content, extract knowledge points, or generate feedback, but the ability estimate and topic selection constraints should still have an explicit measurement layer. The training set must be isolated by student and item to prevent the model from remembering specific answer results.

