# Complete hand calculation: how to update three tokens with one head

## 1. Input projection

Let the two-dimensional Q/K/V of three tokens be

\[
\mathbf Q=
\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix},
\quad
\mathbf K=
\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix},
\quad
\mathbf V=
\begin{bmatrix}1&2\\3&0\\2&1\end{bmatrix}.
\]

\(d_k=2\), the scaling factor is \(\sqrt2\).

## 2. Score matrix

\[
\mathbf Q\mathbf K^\top
=
\begin{bmatrix}
1&0&1\\
0&1&1\\
1&1&2
\end{bmatrix}.
\]

The first row after scaling is

\[
(0.7071,\;0,\;0.7071).
\]

## 3. Softmax at the first position

\[
\exp(0.7071)\approx2.028,\qquad
\exp(0)=1.
\]

\[
\mathbf a_1
\approx
(0.401,\;0.198,\;0.401).
\]

The output is

\[
\begin{aligned}
\mathbf o_1
&=
0.401(1,2)+0.198(3,0)+0.401(2,1)\\
&\approx(1.797,\;1.203).
\end{aligned}
\]

The new representation of position 1 is determined by the three positions.

## 4. Add causal mask

If this is the first position of decoder self-attention, future positions 2 and 3 are not visible:

\[
\widetilde{\mathbf s}_1
=(0.7071,-\infty,-\infty).
\]

So

\[
\mathbf a_1=(1,0,0),
\qquad
\mathbf o_1=(1,2).
\]

Second position visible positions 1, 2:

\[
\widetilde{\mathbf s}_2=(0,0.7071,-\infty),
\]

\[
\mathbf a_2\approx(0.330,\;0.670,\;0),
\]

\[
\mathbf o_2\approx0.330(1,2)+0.670(3,0)
=(2.340,\;0.660).
\]

## 5. Two heads

If the other head uses a different projection, the output \(\mathbf O^{(2)}\) may be produced. Multi-head output is spliced first:

\[
\mathbf H
=
[\mathbf O^{(1)};\mathbf O^{(2)}],
\]

Multiply by \(\mathbf W^O\) to mix. Each head has independent attention distribution.

## 6. Residuals and LayerNorm

Let the attention projection result be \(\mathbf m_i\), and the original input be \(\mathbf x_i\):

\[
\mathbf r_i=\mathbf x_i+\mathbf m_i,
\qquad
\mathbf z_i=\operatorname{LN}(\mathbf r_i).
\]

Then FFN transforms each \(\mathbf z_i\) independently, and then does the second Add & Norm. This completes an encoder layer.

## 7. Parallelism during training

Although the hand calculation is shown line by line, the actual calculation is complete in one go.

\[
\mathbf S\in\mathbb R^{3\times3},
\quad
\mathbf A\in\mathbb R^{3\times3},
\quad
\mathbf O\in\mathbb R^{3\times2}.
\]

The causal mask is also added to the entire matrix at once.
