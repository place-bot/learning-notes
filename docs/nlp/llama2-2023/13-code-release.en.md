# Official code, chat templates and open borders

## 1. What does the warehouse provide?

The official [meta-llama/llama](https://github.com/meta-llama/llama) repository is a minimal inference implementation, including:

- PyTorch Transformer forward；
- RMSNorm、RoPE、SwiGLU、GQA；
- FairScale tensor model parallel layers；
- SentencePiece tokenizer wrapper；
- KV cache and top-p generation;
- text/chat completion example;
- Model cards, licenses and Responsible Use Guide.

The repository is currently marked deprecated and points to the subsequent Llama tool chain; for detailed reading of this topic, the minimum implementation of Llama 2 shall prevail.

## 2. `RMSNorm`

Code:

```python
x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + eps)
```

You can then learn `weight`. The calculation is temporarily converted to float, and then converted back to the original dtype to improve the stability of the normalized value.

## 3. `FeedForward`

```python
w2(F.silu(w1(x)) * w3(x))
```

Directly corresponds to SwiGLU. Three groups of bias-free linear layers are switched to tensor-parallel devices through Column/RowParallelLinear.

## 4. RoPE

`precompute_freqs_cis()` constructs complex polar coordinates:

\[
e^{it\omega_j}.
\]

`apply_rotary_emb()` Combine the last dimensions of Q/K into complex numbers in pairs, multiply them by the position phase, and then convert them back to real numbers.

## 5. GQA

```python
n_rep = n_local_heads // n_local_kv_heads
keys = repeat_kv(keys, n_rep)
values = repeat_kv(values, n_rep)
```

The K/V cache only stores a small amount of `n_kv_heads`, which is logically expanded to the number of query heads before attention.

## 6. KV cache

Pre-allocated per layer:

\[
\text{cache shape}
=
[B_{\max},T_{\max},H_{KV},d_h].
\]

Therefore, the README reminder `max_seq_len` and `max_batch_size` will directly affect the video memory pre-allocation. The generation step only writes the new K/V to `start_pos:start_pos+seqlen`.

## 7. Chat template

Official code definition:

```text
[INST] ... [/INST]
<<SYS>>
system message
<</SYS>>
```

The system message is merged into the first user content. Each round of history starts with BOS and ends with EOS. The last user turn ends with `[INST] ... [/INST]`, waiting for assistant generation.

Models are sensitive to templates. Missing BOS/EOS, whitespace, newlines, or role order may change behavior.

## 8. Template injection check

Official `chat_completion()` rejects special template tags appearing directly in user messages to prevent users from forging system/assistant boundaries. It's just a layer of string checking and doesn't cover all the semantics of prompt injection.

## 9. Sampling

When temperature is greater than 0:

\[
p=\operatorname{softmax}(z/\tau),
\]

Then use top-p to select tokens within the cumulative probability mass. When temperature is 0, argmax is used directly. When the code forms a batch with different prompt lengths, mask is used to prevent the tokens still in the prompt area from being overwritten by generation.

## 10. Release scope

Official model weight access and inference codes are provided, but all paper-level content has not yet been released:

- 2T-token complete corpus;
- All pretraining and RLHF codes;
- 27,540 SFT data;
- Meta preference data；
- reward model weights；
- rejection sampling/PPO production pipeline.

Therefore, external checkpoints can be run, fine-tuned, and studied, but the complete Llama 2-Chat training cannot be accurately reproduced.

## 11. License Boundaries

Llama 2 uses a custom Community License that includes restrictions such as attribution, acceptable use, specific redistribution requirements, additional commercial terms for very large monthly active products, and no use of materials to improve other large models. When using, you should read the official `LICENSE` and `USE_POLICY` directly.

"Downloadable" and "open source software in the OSI sense" involve different standards. This topic uses "open weighting" to describe its scientific and engineering accessibility.
