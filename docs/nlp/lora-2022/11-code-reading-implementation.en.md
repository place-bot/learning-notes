# `loralib` Intensive code reading and implementation from scratch

## 1. Official documents

- `loralib/layers.py`：Embedding、Linear、MergedLinear、ConvLoRA；
- `loralib/utils.py`: Freeze non-LoRA parameters and filter state dict;
- `examples/NLU`：RoBERTa/DeBERTa；
- `examples/NLG`：GPT-2。

## 2. `Linear` core

Official implementation created

\[
A\in\mathbb R^{r\times d_{\text{in}}},
\qquad
B\in\mathbb R^{d_{\text{out}}\times r},
\]

set `weight.requires_grad=False`, scale `lora_alpha / r`, forward join

```python
(dropout(x) @ A.T @ B.T) * scaling
```

## 3. Implement from scratch

```python
import math
import torch
from torch import nn
from torch.nn import functional as F

class LoRALinear(nn.Linear):
    def __init__(self, in_features, out_features,
                 r=8, alpha=8, dropout=0.0, bias=True):
        super().__init__(in_features, out_features, bias=bias)
        self.r = r
        self.scaling = alpha / r
        self.lora_dropout = nn.Dropout(dropout)
        self.weight.requires_grad = False

        self.lora_A = nn.Parameter(torch.empty(r, in_features))
        self.lora_B = nn.Parameter(torch.zeros(out_features, r))
        nn.init.kaiming_uniform_(self.lora_A, a=math.sqrt(5))

    def forward(self, x):
        base = F.linear(x, self.weight, self.bias)
        update = F.linear(
            F.linear(self.lora_dropout(x), self.lora_A),
            self.lora_B,
        )
        return base + self.scaling * update

    @torch.no_grad()
    def merged_weight(self):
        return self.weight + self.scaling * (
            self.lora_B @ self.lora_A
        )
```

## 4. Official merge

`model.eval()` Add \(sBA\) to `weight.data`, subtract `model.train()`, and mark it with `merged` to prevent repeated operations. Pay attention to the transposition convention for the weight direction of PyTorch's `nn.Linear`.

## 5. Tool function

`mark_only_lora_as_trainable` freezes other weights based on the parameter name `lora_`, and supports three bias strategies: `none`, `all`, and `lora_only`. `lora_state_dict` uses the same policy to filter checkpoints.

## 6. Verification

```python
layer.eval()
y_unmerged = layer(x)
w = layer.merged_weight()
y_merged = F.linear(x, w, layer.bias)
torch.testing.assert_close(y_unmerged, y_merged)
```

Also check:

- Initial LoRA output is 0;
- Only LoRA parameters have gradients;
- The merge/unmerge cycle is stable;
- fused QKV only updates the specified slice;
- checkpoint loads to the exact base version;
- No accidental unfreezing of the base for distributed training.
