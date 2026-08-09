# Parameter amount, video memory and training cost

## 1. A Transformer projection

For the Q projection of \(d\times d\), the LoRA rank \(r\) parameter is \(2dr\). If each layer adapts to Q and V at the same time:

\[
\text{params per layer}=4dr.
\]

If there is \(L\) layer:

\[
|\Theta|=4Ldr.
\]

GPT-3 175B in \(L=96,d=12288,r=4\):

\[
4\cdot96\cdot12288\cdot4
=
18{,}874{,}368,
\]

About 18.9M; FP16 original data is about 37.7MB, which is consistent with the order of magnitude of the paper, which is about 35MB.

## 2. Why is the training memory reduced?

The frozen parameters still need to be saved and participated in the forward; what is saved is:

- Base weight gradient;
- Adam's first-order and second-order states;
- Storage and communication related to weight gradient in partial backpropagation;
- Complete checkpoint of each task.

The base model itself does not disappear, so LoRA does not automatically install a model that does not fit at all. QLoRA for quantified bases is a subsequent extension.

## 3. Activate video memory

Long sequences and large batches of activations may still dominate. LoRA mainly reduces trainable parameters and optimizer state, and cannot directly eliminate attention \(O(n^2)\) activation or all reverse activations.

## 4. Training FLOPs

Increase in low-rank branches

\[
O(r(d_{\text{in}}+d_{\text{out}}))
\]

Multiplication without calculating the weight gradient of \(W_0\). The gradient still needs to be passed to the activation of the earlier layer through \(W_0\), so the base back calculation will not all disappear.

## 5. Multi-task storage

\(T\) full models require approximately

\[
T|\Phi_0|.
\]

Shared base plus LoRA:

\[
|\Phi_0|+\sum_{t=1}^{T}|\Theta_t|.
\]

The more tasks, the greater the shared benefits.

## 6. Parameter efficiency and total resources

LoRA costs should be reported separately:

-Total model parameters;
- trainable parameters;
- optimizer state；
- checkpoint；
- Peak video memory;
- Training throughput;
- Whether to merge during reasoning;
- Base accuracy and quantization method.

Reporting only "training parameter percentage" does not fully describe the resource.
