# Step by step hand calculation: from attention to gradient

## 1. Three source comments

\[
\mathbf h_1=\begin{bmatrix}1\\0\end{bmatrix},
\quad
\mathbf h_2=\begin{bmatrix}0\\1\end{bmatrix},
\quad
\mathbf h_3=\begin{bmatrix}1\\1\end{bmatrix}.
\]

The score of the current target step is

\[
e_{i1}=1,\qquad e_{i2}=0,\qquad e_{i3}=2.
\]

## 2. Softmax

\[
\exp(1)\approx2.7183,\quad
\exp(0)=1,\quad
\exp(2)\approx7.3891,
\]

\[
\boldsymbol\alpha_i
\approx
(0.2447,\;0.0900,\;0.6652).
\]

The sum of these three terms is approximately 1.

## 3. Context

\[
\begin{aligned}
\mathbf c_i
&=\sum_j\alpha_{ij}\mathbf h_j\\
&\approx
0.2447\begin{bmatrix}1\\0\end{bmatrix}
+0.0900\begin{bmatrix}0\\1\end{bmatrix}
+0.6652\begin{bmatrix}1\\1\end{bmatrix}\\
&\approx
\begin{bmatrix}0.9099\\0.7552\end{bmatrix}.
\end{aligned}
\]

## 4. Vocabulary output

Suppose the logits of \(A,B,C\) are

\[
\mathbf o_i=(0.2,\;1.0,\;-0.5)^\top,
\]

rule

\[
\mathbf p_i\approx(0.2687,\;0.5979,\;0.1334)^\top.
\]

When the correct word is \(B\)

\[
\mathcal L_i=-\log(0.5979)\approx0.514,
\]

\[
\frac{\partial\mathcal L_i}{\partial\mathbf o_i}
\approx
(0.2687,\;-0.4021,\;0.1334)^\top.
\]

## 5. Attention score gradient

Assume that the gradient passed downstream to the context is

\[
\mathbf g_i
=
\frac{\partial\mathcal L}{\partial\mathbf c_i}
=
(0.4,\;-0.2)^\top.
\]

\[
\mathbf g_i^\top\mathbf c_i\approx0.2129.
\]

take advantage of

\[
\frac{\partial\mathcal L}{\partial e_{ik}}
=
\alpha_{ik}
\left(
\mathbf g_i^\top\mathbf h_k
-
\mathbf g_i^\top\mathbf c_i
\right)
\]

available

\[
\begin{aligned}
\frac{\partial\mathcal L}{\partial e_{i1}}&\approx0.0458,\\
\frac{\partial\mathcal L}{\partial e_{i2}}&\approx-0.0372,\\
\frac{\partial\mathcal L}{\partial e_{i3}}&\approx-0.0086.
\end{aligned}
\]

The sum of the three terms is approximately 0, reflecting that softmax is insensitive to simultaneous translation of all logits.

## 6. Direction after gradient descent

\[
e_{ik}^{\text{new}}
=
e_{ik}
-
\eta
\frac{\partial\mathcal L}{\partial e_{ik}}.
\]

So position 1 scores go down, position 2 goes up, and position 3 goes up slightly. Under this assumed gradient, the model expects the second dimension of the context to increase and the first dimension to decrease.

## 7. Continue to pass in the alignment network

\[
e_{ij}
=
\mathbf v_a^\top\tanh(\mathbf q_{ij}),
\qquad
\mathbf q_{ij}
=
\mathbf W_a\mathbf s_{i-1}
+\mathbf U_a\mathbf h_j.
\]

Remember \(\delta_{ij}=\partial\mathcal L/\partial e_{ij}\), then

\[
\frac{\partial\mathcal L}{\partial\mathbf q_{ij}}
=
\delta_{ij}
\left[
\mathbf v_a\odot
(1-\tanh^2(\mathbf q_{ij}))
\right].
\]

Then do the outer product with \(\mathbf s_{i-1}\) and \(\mathbf h_j\) to get the gradient of \(\mathbf W_a,\mathbf U_a\). Single-sentence errors are thus transformed into alignment rules that can be reused across samples.

## 8. Padding example

If position 3 is padding, \(e_{i3}=-\infty\) should be specified before softmax. The effective weight becomes

\[
\alpha_{i1}\approx0.7311,\qquad
\alpha_{i2}\approx0.2689,\qquad
\alpha_{i3}=0.
\]

Multiplying the third term by 0 directly after the softmax will break the normalization unless normalized again.

## Summary of this page

\[
\text{Alignment score}
\rightarrow
\text{softmax}
\rightarrow
\text{context}
\rightarrow
\text{target word loss}
\rightarrow
\text{attention gradient}.
\]

The operation from \(e_{ij}\) to translation loss is continuously differentiable, so soft alignment can be learned jointly with translation.
