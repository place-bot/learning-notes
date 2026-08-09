# Tensor2Tensor with modern PyTorch implementation

## 1. Original code location

The paper points to [TensorFlow Tensor2Tensor](https://github.com/tensorflow/tensor2tensor). Key modules include:

- `tensor2tensor/models/transformer.py`: encoder, decoder and hparams;
- `tensor2tensor/layers/common_attention.py`: dot-product and multi-head attention;
- `tensor2tensor/layers/common_layers.py`：pre/postprocess、LayerNorm；
- Data generator: subword vocabulary, length bucket and batch.

The warehouse has continued to evolve since then, and the latest code includes subsequent configurations such as Pre-LN. The `transformer_base_v1`/paper configuration needs to be separated from the modern defaults when reading.

## 2. Minimum attention

```python
import math
import torch
from torch import nn

def scaled_attention(q, k, v, mask=None):
    scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
    if mask is not None:
        scores = scores.masked_fill(~mask, float("-inf"))
    weights = torch.softmax(scores, dim=-1)
    output = weights @ v
    return output, weights
```

## 3. Long reshape

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=512, heads=8):
        super().__init__()
        assert d_model % heads == 0
        self.heads = heads
        self.d_head = d_model // heads
        self.qkv = nn.Linear(d_model, 3 * d_model)
        self.out = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        batch, length, width = x.shape
        qkv = self.qkv(x).view(
            batch, length, 3, self.heads, self.d_head
        )
        q, k, v = qkv.unbind(dim=2)
        q, k, v = [
            t.transpose(1, 2) for t in (q, k, v)
        ]
        y, weights = scaled_attention(q, k, v, mask)
        y = y.transpose(1, 2).contiguous().view(
            batch, length, width
        )
        return self.out(y), weights
```

Cross-attention needs to project the decoder query and encoder key/value separately, and cannot reuse the simplified interface that only receives one `x`.

## 4. Causal mask

```python
def causal_mask(length, device):
    return torch.ones(
        length, length, dtype=torch.bool, device=device
    ).tril()[None, None, :, :]
```

When combined with padding mask, it will be broadcast as \([B,1,T_q,T_k]\).

## 5. Original paper Post-LN block

```python
class PostNormBlock(nn.Module):
    def __init__(self, d_model, sublayer, dropout=0.1):
        super().__init__()
        self.sublayer = sublayer
        self.dropout = nn.Dropout(dropout)
        self.norm = nn.LayerNorm(d_model)

    def forward(self, x, **kwargs):
        y = self.sublayer(x, **kwargs)
        if isinstance(y, tuple):
            y = y[0]
        return self.norm(x + self.dropout(y))
```

## 6. Test Checklist

- The sum of the weights of each attention row is 1;
- The padding and future position weights are 0;
- Use \(d_k\) for QK scaling, do not misuse \(d_{\text{model}}\);
- The order of tokens remains unchanged after head reshape;
- residual has the same dimensions at both ends;
- The target embedding is indeed moved to the right;
- loss ignores target padding;
- The training and inference position numbers are consistent;
- beam/KV cache is properly rearranged.

## 7. Code interface with LoRA

QKV and output projection are both `nn.Linear`. LoRA will

\[
\mathbf x\mathbf W^\top
\]

Change to

\[
\mathbf x\mathbf W_0^\top
+
\frac{\alpha}{r}\mathbf x\mathbf A^\top\mathbf B^\top,
\]

and freeze \(\mathbf W_0\). The next topic will be implemented line by line.
