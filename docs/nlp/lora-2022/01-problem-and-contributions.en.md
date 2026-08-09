# Full fine-tuning issues and LoRA innovation

## 1. Multi-task deployment cost

Full fine-tuning starts from \(\Phi_0\) and learns the same-dimensional update \(\Delta\Phi_t\) for each task:

\[
\Phi_t=\Phi_0+\Delta\Phi_t.
\]

If the base has 175B parameters, saving a complete model per task will quickly expand the storage, loading and serving costs; Adam also maintains gradients and two momentum states for trainable parameters.

## 2. Parameter efficiency goal

The paper hopes to update the encoding task with a small parameter set \(\Theta_t\):

\[
\Delta\Phi_t=\Delta\Phi(\Theta_t),
\qquad
|\Theta_t|\ll|\Phi_0|.
\]

Training only optimizes \(\Theta_t\):

\[
\max_{\Theta}
\sum_{(x,y)\in\mathcal Z}\sum_t
\log p_{\Phi_0+\Delta\Phi(\Theta)}
(y_t\mid x,y_{<t}).
\]

## 3. Low intrinsic rank assumption

Inspired by the research on "fine-tuning has low intrinsic dimensions", the paper proposes that the matrix updates \(\Delta W\) required for downstream adaptation may be concentrated in low-dimensional subspaces. So \(\Delta W=BA\) is used to directly limit its rank.

## 4. Contribution

- Freeze pretraining weights and train parallel low-rank branches;
- Parameters and optimizer state are greatly reduced;
- \(BA\) can be merged into \(W_0\) during deployment without additional network depth;
- It is equivalent to or better than full fine-tuning on RoBERTa, DeBERTa, GPT-2, and GPT-3;
- Compare Q/K/V/O projections with different ranks;
- Explaining low-rank updates using singular subspace analysis.

## 5. Conclusion on the scale of the original paper

GPT-3 175B setting, paper report:

-Trainable parameters can be reduced by up to about 10,000 times;
- Training video memory reduced from approximately 1.2TB to approximately 350GB;
- Rank 4. When only Q/V is adapted, the task checkpoint is about 35MB;
- Training throughput increased from 32.5 tokens/s per V100 to 43.1 tokens/s;
- Inference latency will not be increased after merging weights.

These numbers depend on the specific model, accuracy, sharding, and optimizer settings and cannot be directly applied to any modern training stack.
