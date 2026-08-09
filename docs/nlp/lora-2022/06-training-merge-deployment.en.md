# Training, saving, merging and task switching

## 1. Training

Freeze \(W_0\) and let only `lora_A`, `lora_B` and optional bias get gradients. Forward:

\[
y=xW_0^\top
+s\,xA^\top B^\top.
\]

## 2. Save

checkpoint only needs to save the LoRA parameters and necessary configuration:

- target module；
- rank \(r\)；
- \(\alpha\)；
- dropout；
- bias strategy;
- Base model identity and version.

Only \(A,B\) and missing the base version, the full mission model cannot be restored.

## 3. Merge

Pre-deployment calculations

\[
W_{\text{merged}}
=
W_0+sBA.
\]

Inference restores ordinary linear layers:

\[
y=W_{\text{merged}}x.
\]

So no extra serial layer like adapter is added.

## 4. Cancel merge and switch

\[
W_0
=
W_{\text{merged}}-sBA.
\]

Then add \(s'B'A'\) of another task. Actual systems need to avoid repeated merges, low-precision cumulative errors, and concurrent modification of shared weights by multiple threads.

## 5. Trade-offs between merging and dynamic routing

- Merge: the simplest single-task inference path, no low-rank branch latency;
- Not merged: The same base can dynamically select adapters based on samples, but low-rank branches will be counted in each forward direction;
- Mixing different merged LoRAs in one batch is difficult because the shared \(W\) cannot represent multiple tasks simultaneously.

## 6. Official `loralib` behavior

By default, `model.eval()` will be merged, and `model.train()` will be canceled; `merge_weights=False` can be set to disable it. When loading, load the base first, and then load the LoRA state dict with `strict=False`.

## 7. Verify the correctness of the merge

\[
\max|f_{\text{unmerged}}(x)-f_{\text{merged}}(x)|
\]

There should be only floating point errors. Also test that train/eval switches multiple times without repeated additions and subtractions.
