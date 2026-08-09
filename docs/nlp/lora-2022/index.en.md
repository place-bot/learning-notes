# LoRA: low-rank adaptation of large language models

This topic is an intensive reading of Hu et al.'s **LoRA: Low-Rank Adaptation of Large Language Models**, which was officially published at ICLR 2022.

## Core formula

weight for pretraining

\[
\mathbf W_0\in\mathbb R^{d\times k},
\]

Freeze \(\mathbf W_0\) and write the task update as

\[
\Delta\mathbf W=\mathbf B\mathbf A,
\qquad
\mathbf B\in\mathbb R^{d\times r},
\quad
\mathbf A\in\mathbb R^{r\times k},
\quad
r\ll\min(d,k).
\]

Forward propagation:

\[
\mathbf h
=
\mathbf W_0\mathbf x
+
\frac{\alpha}{r}
\mathbf B\mathbf A\mathbf x.
\]

## Citation details

|item|information|
|---|---|
|Author|Edward J. Hu, Yelong Shen et al.|
|publish| ICLR 2022 |
|Official page| [OpenReview](https://openreview.net/forum?id=nZeVKeeFYf9) |
| arXiv | [2106.09685](https://arxiv.org/abs/2106.09685) |
|official code| [microsoft/LoRA](https://github.com/microsoft/LoRA) |

## Reading route

1. [Full fine-tuning issues and LoRA innovation](01-problem-and-contributions.md)
2. [Linear algebra with low rank update](02-low-rank-math.md)
3. [Parameter amount, video memory and training cost](03-parameter-memory-compute.md)
4. Which matrices](04-target-modules.md) should be changed in [Transformer
5. [Initialization, scaling and rank](05-initialization-scaling-rank.md)
6. [Training, saving, merging and task switching](06-training-merge-deployment.md)
7. [Complete hand calculation](07-worked-example.md)
8. [Compare with FT, Adapter, Prefix, BitFit](08-method-comparison.md)
9. [Experimental design and results](09-experiments-results.md)
10. [Low-rank update analysis](10-rank-analysis.md)
11. [`loralib` Intensive code reading and implementation of](11-code-reading-implementation.md) from scratch
12. [Limitations, modern extensions and conclusions](12-limitations-extensions-conclusion.md)
13. [Reference](references.md)

The key point of understanding LoRA is that it constrains the **weight changes** caused by the task to have a low-rank structure, and does not approximate the pretraining weight itself into a low-rank matrix.
