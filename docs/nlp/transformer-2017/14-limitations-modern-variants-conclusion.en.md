# Limitations, modern variations and conclusions

## 1. Quadratic attention cost

Global self-attention produces a \(n\times n\) score matrix. Short sentence training is efficient, while long documents, audio and high-resolution visual tokens will bring significant memory and computing costs.

## 2. Autoregressive generation delay

Training is parallelized across locations, and generation still relies on prefixes. Research on KV cache, speculative decoding and parallel decoding is used to reduce this bottleneck and is a follow-up work.

## 3. Sequential induction bias

Transformer injects order using positional encoding, without the temporal recursion of RNN or the local neighborhood prior of CNN. It obtains global relationships and hardware efficiency, and may also rely more on data to learn local structures.

## 4. Deep stability of original Post-LN

Original paper Six-layer Post-LN can be effectively trained. Deeper models are often changed to Pre-LN or use other normalization, residual scaling and initialization schemes.

## 5. Original paper and modern LLM

|Original Transformer|Common modern variations|
|---|---|
| encoder–decoder | decoder-only、encoder-only |
|sine absolute position| RoPE、relative bias、ALiBi |
| ReLU FFN | GELU、SwiGLU |
| Post-LN | Pre-LN/RMSNorm |
| multi-head attention | GQA/MQA |
|Machine translation supervised training|Large-scale self-supervised pretraining and instruction tuning|

These developments follow the main body of attention, residual, and position-wise FFN, but the specific equations have changed.

## 6. Historical innovation of the paper

The contribution portfolio includes:

- Completely remove sequence-aligned recurrence/convolution;
- scaled dot-product attention；
- multi-head attention；
- Full attention stacking of encoder and decoder;
- positional encoding;
- Parallel training and short and long distance path analysis;
- Achieve strong results with low training cost on WMT14.

## 7. Next step of connecting with LoRA

Transformer puts a lot of capabilities into the matrix

\[
\mathbf W^Q,\mathbf W^K,\mathbf W^V,\mathbf W^O,
\mathbf W_1,\mathbf W_2.
\]

Full fine-tuning will update every element of these large matrices. LoRA assumes that the updates \(\Delta\mathbf W\) required by the downstream task have low intrinsic rank, represented by two small matrices, thus training only very few parameters.

## 8. Conclusion

The key breakthrough of Transformer is to rewrite the inter-position dependence into matrixizable attention and use mask to retain causal constraints. It shortens long-distance information paths and significantly improves training parallelism, while leaving long-context quadratic costs and autoregressive inference serialization problems.
