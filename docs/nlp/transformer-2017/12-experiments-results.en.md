# Experimental design, results and ablation

## 1. WMT14 main result

|model| EN-DE BLEU | EN-FR BLEU |training cost|
|---|---:|---:|---:|
| ConvS2S | 25.16 | 40.46 | \(9.6\times10^{18}\) / \(1.5\times10^{20}\) FLOPs |
| MoE | 26.03 | 40.56 | \(2.0\times10^{19}\) / \(1.2\times10^{20}\) |
| ConvS2S Ensemble | 26.36 | 41.29 | \(7.7\times10^{19}\) / \(1.2\times10^{21}\) |
| Transformer base | 27.3 | 38.1 | \(3.3\times10^{18}\) |
| Transformer big | **28.4** | **41.0** | \(2.3\times10^{19}\) |

big exceeded the ensemble listed at the time by more than two BLEU on the British and German tasks; the British and French 41.0 was the strong single model result at the time, but lower than the ConvS2S ensemble 41.29 in the table.

## 2. Official version and subsequent arXiv summary

NeurIPS official version reports English and French 41.0. A later arXiv version summary appears at 41.8. The main result of the topic uses the numbers in Table 2 of the official proceedings to avoid mixing versions.

## 3. Base and big

|Configuration| base | big |
|---|---:|---:|
| \(N\) | 6 | 6 |
| \(d_{\text{model}}\) | 512 | 1024 |
| \(d_{\text{ff}}\) | 2048 | 4096 |
| heads | 8 | 16 |
| dropout | 0.1 |0.3 (big is 0.1 in English and French)|
| steps | 100k | 300k |
| params | 65M | 213M |

## 4. Head number ablation

|Number of heads| \(d_k=d_v\) | dev BLEU |
|---:|---:|---:|
| 1 | 512 | 24.9 |
| 4 | 128 | 25.5 |
| 8 | 64 | 25.8 |
| 16 | 32 | 25.8 |
| 32 | 16 | 25.4 |

Result supports long positions, but does not present a monotonic relationship of "more is better".

## 5. Width, depth and regularity

- 2-layer development BLEU 23.7, 4-layer 25.3, base 6-layer 25.8, 8-layer 25.5;
- \(d_{\text{model}}=1024\) variant reaches 26.0;
- \(d_{\text{ff}}=4096\) variant reaches 26.2;
- No dropout is 24.6, base 0.1 is 25.8;
- No label smoothing is 25.3, 0.1 is 25.8.

These are development set ablations near a single factor and cannot be independently proven to be optimal at all modern scales.

## 6. positional encoding

Sine position 25.8, learned position 25.7, small difference. The paper chooses the sinusoidal scheme mainly based on the consideration of potential length extrapolation.

## 7. Additional tasks

The paper also applies Transformer to English constituency parsing, demonstrating generalization in big data and limited data settings. The main arguments still center around machine translation quality, cost and parallelism.

## 8. Evidence boundaries

- Training cost is calculated based on time, number of GPUs and estimated sustained FLOPs;
- The data processing, hardware and codes of different documents are different;
- The main table does not report multiple random seed confidence intervals;
- BLEU does not cover all semantics and artificial quality;
- What the paper proves is the encoder–decoder Transformer on the task at that time, which cannot be directly equivalent to all subsequent large language model phenomena.
