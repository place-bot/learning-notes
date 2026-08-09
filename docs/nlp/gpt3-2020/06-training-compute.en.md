# Training process, parallelization and computational cost

## 1. Optimizer

All models use Adam:

\[
\beta_1=0.9,
\qquad
\beta_2=0.95,
\qquad
\epsilon=10^{-8}.
\]

The global gradient norm is clipped to

\[
\|g\|_2\le1.0,
\]

weight decay is 0.1.

## 2. learning rate scheduling

Linear warmup for the first 375 million tokens. Then cosine decay is used, which drops to 10% of the initial value within the first 260 billion tokens; the last approximately 40 billion tokens remain at 10% of the initial learning rate.

Simplified and written as:

\[
\eta(s)=
\begin{cases}
\eta_0\dfrac{s}{S_{\mathrm{warm}}},
&s<S_{\mathrm{warm}},\\[6pt]
\eta_0\left[0.1+0.9\dfrac{1+\cos(\pi q)}{2}\right],
&S_{\mathrm{warm}}\le s\le260\mathrm B,\\[6pt]
0.1\eta_0,&s>260\mathrm B,
\end{cases}
\]

Among them, \(q\) is the decay interval normalization progress.

## 3. Batch size warmup

The batch size is about 32K tokens at the beginning of training, and linearly increases to the full batch within the first 4-12 billion training tokens. The complete batch size of different models is 0.5M to 3.2M tokens.

The author uses gradient noise scale to guide batch selection: larger models can usually effectively utilize larger batches, while requiring a smaller learning rate.

## 4. Sequence packing

All training sequence lengths are fixed to 2048. Shorter documents are packed into the same sequence, separated by end-of-text tokens:

```text
document A <|endoftext|> document B <|endoftext|> ...
```

There is no additional attention mask between different documents. The model can see boundary tokens and learn that there is no regular semantic continuity on either side of the boundary.

## 5. Data sampling

Before reaching the epoch boundary of a certain data set, samples are extracted without-replacement to reduce short-term repetition and overfitting. Small high-quality corpora will still be repeated multiple times across epochs due to different mixing weights.

## 6. Training calculation

The paper's broader impacts estimate that GPT-3 175B pretraining consumes thousands of PF-days. The training calculation amount given by the official chart is approximately

\[
3.14\times10^{23}\ \text{FLOPs},
\]

This is equivalent to approximately 3640 PF-days. This number describes the final training run, excluding the full cost of search, failed experiments, small models, and system development.

## 7. Approximate sources of calculations

For dense Transformer, a common training FLOPs rough estimate is:

\[
C\approx6NT,
\]

Among them, \(N\) is the non-embedding parameter quantity, \(T\) is the number of training tokens; the coefficient 6 roughly covers the forward and reverse matrix multiplication. With sparse attention and specific system optimization, the exact value requires actual operator statistics.

## 8. Energy consumption and reasoning

The paper points out that large-scale training consumes high energy; after the same model training is completed, the incremental inference cost of a single sample may be much lower than retraining the task model. This comparison still depends on:

- Volume of service requests;
- prompt length and output length;
- KV cache；
- batch and hardware utilization;
- Whether the model is permanent for a long time;
- How many fine-tuning models each task replaces.

## 9. Reproducibility

The paper explains that the model is trained on the high-bandwidth V100 cluster provided by Microsoft, and uses intra-layer and inter-layer model parallelism. No official training code, parallel topology, checkpoints, or full hardware schedule have been released, and the 175B experiment is beyond the budget of most research teams.

Therefore, the paper results can be scientifically reviewed, but complete computational reproduction is limited by code, data, model weights, and cost.
