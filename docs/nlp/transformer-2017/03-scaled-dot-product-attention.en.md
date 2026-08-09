# Scaled Dot-Product Attention

## 1. Formula

\[
\boxed{
\operatorname{Attention}(\mathbf Q,\mathbf K,\mathbf V)
=
\operatorname{softmax}\!\left(
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}
\right)\mathbf V
}
\]

The order of calculation is matrix multiplication, scaling, mask, row softmax, value weighted sum.

## 2. What does the dot product represent?

single score

\[
s_{ij}=\mathbf q_i^\top\mathbf k_j
\]

Measures the compatibility between query and key in the learned projection space. It is not a pre-specified semantic similarity; the projection parameters are trained by the task loss.

## 3. Why divide by \(\sqrt{d_k}\)

Assume \(q_\ell,k_\ell\) is independent, mean 0, variance 1:

\[
\mathbf q^\top\mathbf k
=
\sum_{\ell=1}^{d_k}q_\ell k_\ell.
\]

Its variance is approximately

\[
\operatorname{Var}(\mathbf q^\top\mathbf k)=d_k.
\]

The standard deviation increases with \(\sqrt{d_k}\). After scaling

\[
\operatorname{Var}\!\left(
\frac{\mathbf q^\top\mathbf k}{\sqrt{d_k}}
\right)\approx1.
\]

Without scaling, large logits can easily push softmax into the saturation zone close to one-hot, making the gradient at most locations very small.

## 4. Stable softmax

\[
\operatorname{softmax}(s_j)
=
\frac{\exp(s_j-\max_k s_k)}
{\sum_\ell\exp(s_\ell-\max_k s_k)}.
\]

Subtracting the row maximum does not change the probability and prevents exponential overflow. The softmax of modern frameworks is usually stabilized.

## 5. With additive attention

Bahdanau：

\[
e_{ij}
=
\mathbf v^\top\tanh(
\mathbf W\mathbf q_i+\mathbf U\mathbf k_j).
\]

Transformer：

\[
e_{ij}
=
\mathbf q_i^\top\mathbf k_j/\sqrt{d_k}.
\]

The theoretical complexity of the two is similar; the dot product form can submit all position pairs to highly optimized matrix multiplication.

## 6. Gradient intuition

Let \(\mathbf o_i=\sum_j A_{ij}\mathbf v_j\), the downstream gradient be \(\mathbf g_i\). Yes to fractions

\[
\frac{\partial\mathcal L}{\partial s_{ik}}
=
A_{ik}\,
\mathbf g_i^\top(\mathbf v_k-\mathbf o_i).
\]

When a value is more in line with the downward direction relative to the current average output, its score will be increased. This is consistent with the gradient structure of Bahdanau soft attention.
