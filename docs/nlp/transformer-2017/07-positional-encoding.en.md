# Sine and cosine positional encoding

self-attention is equivariant to the arrangement of input rows. Without position information, the model cannot distinguish tokenization order by attention alone.

## 1. Original paper formula

\[
PE_{(pos,2i)}
=
\sin\!\left(
\frac{pos}{10000^{2i/d_{\text{model}}}}
\right),
\]

\[
PE_{(pos,2i+1)}
=
\cos\!\left(
\frac{pos}{10000^{2i/d_{\text{model}}}}
\right).
\]

Use sine for even dimensions and cosine for odd dimensions. The wavelength extends in a geometric progression from \(2\pi\) to approximately \(10000\cdot2\pi\).

## 2. How to enter the model

\[
\mathbf x_{pos}
=
\sqrt{d_{\text{model}}}\,\mathbf e_{token}
+\mathbf{PE}_{pos}.
\]

Positional encoding and embedding are both 512-dimensional and can be added directly. The paper also performs dropout on the addition results.

## 3. Why can sine express relative displacement?

take advantage of

\[
\sin(a+b)=\sin a\cos b+\cos a\sin b,
\]

\[
\cos(a+b)=\cos a\cos b-\sin a\sin b,
\]

For fixed offset \(k\), frequency for

\[
[\sin(\omega(pos+k)),\cos(\omega(pos+k))]
\]

It can be obtained from the sine-cosine pair at position \(pos\) by a linear rotation dependent on \(k\). This facilitates learning of relative position relationships.

## 4. Fixed and learnable positions

In the paper ablation, the development set of learning position embedding BLEU 25.7, the sine version 25.8, the performance is similar. The authors chose the sinusoidal version on the grounds that it may extrapolate to longer sequences not seen during training.

Extrapolation ability is not automatically guaranteed: the rest of the model, training length, numerical frequency, and task distribution all affect actual performance.

## 5. Subsequent position method

RoPE, relative position bias, ALiBi, etc. are subsequent developments. They cannot be written as part of the original 2017 Transformer.
