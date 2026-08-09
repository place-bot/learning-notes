# Compare with the full range of fine-tuning, Adapter, Prefix, and BitFit

|method|Training content|extra depth|Occupy token length|Can be merged into the original weight|
|---|---|---:|---:|---:|
| Full FT |All parameters|None|None|Already full weight|
| BitFit | bias |None|None|Yes|
| Adapter |Insert bottleneck layer|Yes|None|It is usually not possible to directly combine equivalents|
| Prefix/Prompt tuning |Learnable prefix activation/token|None|Yes|No|
| LoRA |weight low rank increment|parallel branch|None|Yes|

## 1. Adapter latency

The adapter is located between layers and requires additional execution on the main path. In the case of GPT-2 medium, batch 1, and sequence length 128, the paper shows that the two adapter variants increase latency by approximately 20.7% and 30.3% relative to FT/LoRA. The overhead is relatively small for large batches.

## 2. Prefix sequence budget

The learnable prefix occupies the contextual position and reduces the available length of real task tokens. The original paper also observed that the performance is not monotonic when the prefix parameter is increased, and cited optimization difficulties as one of the problems.

## 3. LoRA’s unique trade-offs

Advantages:

- Does not increase network depth;
- Can be merged;
- Does not occupy context;
- Small checkpoint for easy switching;
- Can be combined with other methods.

Price:

- rank and target modules need to be selected;
- Each mission still requires training;
- There is a conflict between the mixed task batch and the merge weight;
- Very low rank may limit tasks with large distribution differences.

## 4. Keep comparisons fair

It is necessary to unify the base, data, step count, hyperparameter search, trainable parameter budget, random seed and inference settings. Some of the baselines in the original paper come from existing literature, and are marked with asterisks in the table. Not all of them were rerun in the exact same code environment.
