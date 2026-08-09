# Which matrices should be changed in Transformer?

## 1. Candidate matrix

Each layer of attention usually has

\[
W_q,\quad W_k,\quad W_v,\quad W_o,
\]

FFN has

\[
W_{\text{up}},\quad W_{\text{down}}.
\]

The LoRA principle can be used for any dense layer. The experiment in the original paper is to control variables, mainly studying self-attention projection, and many settings are only suitable for \(W_q,W_v\).

## 2. GPT-3 experiment under the same budget

Parameter budget is about 18M:

|Adaptation matrix| rank | WikiSQL | MultiNLI |
|---|---:|---:|---:|
| \(W_q\) | 8 | 70.4 | 91.0 |
| \(W_k\) | 8 | 70.0 | 90.8 |
| \(W_v\) | 8 | 73.0 | 91.0 |
| \(W_o\) | 8 | 73.2 | 91.3 |
| \(W_q,W_k\) | 4 | 71.4 | 91.3 |
| \(W_q,W_v\) | 4 | 73.7 | 91.3 |
| Q/K/V/O | 2 | 73.7 | 91.7 |

A small rank spread over more matrices can be better than a large rank concentrating its budget into a single matrix.

## 3. The roles of Q and V

- \(W_q\) How to change the current location to make a search request;
- \(W_v\) changes what content is passed after being read;
- \(W_k\) changes how candidates are matched;
- \(W_o\) Change how the output of each head is mixed.

The Q/V selection in the original paper is an empirical result and does not constitute a universal optimal theorem for all models and tasks.

## 4. Fused QKV

Some implementations combine QKV into a linear layer. The official `loralib.MergedLinear` allows LoRA to be enabled for only some of these slices via `enable_lora`, such as Q and V on, K off.

## 5. Modern configuration

Modern decoder-only models may also have GQA/MQA, SwiGLU and different module names. When selecting target modules, you must check the actual model structure, weight shape and naming, and cannot mechanically copy `q_proj,v_proj`.
