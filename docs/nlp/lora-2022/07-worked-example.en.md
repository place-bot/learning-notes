# Complete hand calculation: a \(3\times4\) linear layer

## 1. Freeze weights and rank 1 branches

\[
W_0=
\begin{bmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{bmatrix},
\quad
A=\begin{bmatrix}1&-1&0&2\end{bmatrix},
\quad
B=\begin{bmatrix}0.5\\-1\\0.25\end{bmatrix}.
\]

\(A\in\mathbb R^{1\times4}\), \(B\in\mathbb R^{3\times1}\), so \(\operatorname{rank}(BA)\le1\).

## 2. Calculate increment

\[
BA=
\begin{bmatrix}
0.5&-0.5&0&1\\
-1&1&0&-2\\
0.25&-0.25&0&0.5
\end{bmatrix}.
\]

Let \(\alpha=r=1\), scale \(s=1\).

## 3. An input

\[
x=(2,1,-1,0)^\top.
\]

Base output:

\[
W_0x=(2,1,-1)^\top.
\]

The low-rank path first reduces the dimensionality:

\[
Ax=2-1+0+0=1.
\]

Upgrading the dimension again:

\[
B(Ax)=(0.5,-1,0.25)^\top.
\]

Finally:

\[
h=(2.5,0,-0.75)^\top.
\]

## 4. Parameter saving

Full matrix update has \(3\times4=12\) parameters. Rank 1 LoRA has \(4+3=7\) parameters. The savings are limited in this small example; the scale drops off quickly when \(d\) is in the thousands and \(r\) is in the single digits.

## 5. A gradient

If the loss is the gradient of the output

\[
g_h=(1,-2,0.5)^\top,
\]

Let \(u=Ax=1\), then

\[
\frac{\partial L}{\partial B}
=
g_hu^\top
=
\begin{bmatrix}1\\-2\\0.5\end{bmatrix}.
\]

\[
\frac{\partial L}{\partial A}
=
B^\top g_h\,x^\top.
\]

\[
B^\top g_h
=
0.5(1)+(-1)(-2)+0.25(0.5)
=
2.625.
\]

\[
\frac{\partial L}{\partial A}
=
2.625(2,1,-1,0)
=(5.25,2.625,-2.625,0).
\]

The gradient of \(W_0\) is not stored, but the input gradient is still propagated through the two paths of the base and LoRA.

## 6. Merge verification

\[
W_{\text{merged}}=W_0+BA.
\]

Direct calculation of \(W_{\text{merged}}x\) must yield the same \((2.5,0,-0.75)^\top\). This is the algebraic basis for "no extra layer of reasoning after merging".
