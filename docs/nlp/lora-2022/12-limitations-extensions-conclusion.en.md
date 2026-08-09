# Limitations, modern extensions and conclusions

## 1. Limitations

- rank and target modules depend on tasks;
- Base weights still need to reside in memory;
- Activation and long-context attention costs are still there;
- The merge mode makes it inconvenient to mix multiple tasks in the same batch;
- Small rank may not express strong domain transfer;
- There are optimization, learning rate and scaling sensitivity for low-rank factors;
- The original paper mainly studies the attention weight of language Transformer.

## 2. Common misunderstandings

### LoRA will compress the base

LoRA compression task updates checkpoint. Unquantized bases retain their original size.

### The trainable parameters are less than the video memory, which is reduced by the same multiple.

Activation, base weights, temporary tensors, and frame overhead are still present. The parameters of GPT-3 in the paper are reduced by about 10,000 times, and the training memory is reduced by about 3 times. It has been shown that the ratios of the two are different.

### Cannot switch after merging

The old increment can be subtracted and the new increment added while retaining \(A,B\); precision and concurrency need to be managed correctly.

## 3. Subsequent expansion

- QLoRA: Quantify frozen base and train LoRA;
- AdaLoRA: dynamically allocate rank;
- DoRA: Decompose weight amplitude and direction;
- LoRA+: use different learning rates for A/B;
- rsLoRA: adjust rank scaling;
- Multi-adapter synthesis, routing and weighted fusion.

These methods are not part of the original paper, and their respective assumptions and evidence should be independently checked.

## 4. When to consider full fine-tuning

When the distribution of tasks and pretraining is greatly different, the data is sufficient, extreme performance is pursued, and full training/deployment resources can be afforded, full fine-tuning may still be more appropriate. LoRA provides a strong resource-quality trade-off and does not theoretically dominate all fine-tuning.

## 5. Conclusion

LoRA will

\[
W_0+\Delta W
\]

re-parameterized as

\[
W_0+\frac{\alpha}{r}BA,
\]

Reduce per-task storage and optimizer state from a large matrix to two narrow matrices. It merges before inference, avoiding additional network depth, and supports the empirical hypothesis that downstream adaptation updates have low intrinsic rank with multiple sets of experiments and subspace analysis.
