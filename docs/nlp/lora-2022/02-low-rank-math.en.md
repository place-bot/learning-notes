#Linear algebra for low-rank updates

## 1. Shape

\[
\mathbf W_0\in\mathbb R^{d_{\text{out}}\times d_{\text{in}}},
\quad
\mathbf A\in\mathbb R^{r\times d_{\text{in}}},
\quad
\mathbf B\in\mathbb R^{d_{\text{out}}\times r}.
\]

\[
\Delta\mathbf W=\mathbf B\mathbf A
\in\mathbb R^{d_{\text{out}}\times d_{\text{in}}}.
\]

From matrix rank inequality:

\[
\operatorname{rank}(\mathbf B\mathbf A)
\le r.
\]

## 2. Forward path

\[
\mathbf h
=
\mathbf W_0\mathbf x
+
s\mathbf B(\mathbf A\mathbf x),
\qquad
s=\alpha/r.
\]

First use \(A\) to push the input to the \(r\) dimension, and then use \(B\) to map it back to the output dimension.

## 3. Parameter quantity

Full matrix update parameters:

\[
d_{\text{out}}d_{\text{in}}.
\]

LoRA parameters:

\[
r(d_{\text{in}}+d_{\text{out}}).
\]

When the square matrix \(d_{\text{in}}=d_{\text{out}}=d\):

\[
\frac{\text{LoRA params}}{\text{full params}}
=
\frac{2dr}{d^2}
=
\frac{2r}{d}.
\]

For example, \(d=4096,r=8\), the ratio is

\[
\frac{16}{4096}\approx0.3906\%.
\]

## 4. LoRA constrains updates

\[
\mathbf W_{\text{task}}
=
\mathbf W_0+\mathbf B\mathbf A.
\]

\(\mathbf W_0\) can maintain full rank. The final matrix is ​​also usually full rank; only increments are constrained to the set whose rank does not exceed \(r\).

## 5. Expression skills

Any matrix \(\Delta W\) with rank \(r^\star\) can accurately represent this update when LoRA rank \(r\ge r^\star\). As rank increases, the representable update set expands; there is a trade-off between parameter efficiency and capacity.

## 6. Relationship with SVD

SVD writes the given matrix as

\[
\Delta W=U\Sigma V^\top.
\]

LoRA does not know the ideal \(\Delta W\) at the beginning of training and directly uses the gradient to learn \(A,B\). It does not require SVD to be performed at every step, nor is it guaranteed that \(A,B\) is orthogonal or equal to the singular vectors.

## 7. The factor is not unique

For any reversible \(\mathbf R\in\mathbb R^{r\times r}\):

\[
\mathbf B\mathbf A
=
(\mathbf B\mathbf R)
(\mathbf R^{-1}\mathbf A).
\]

Therefore, \(A,B\) itself has no unique explanation, and more attention should be paid to the product \(\Delta W\) or its subspace during analysis.
