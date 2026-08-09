# Proposition 3: Reversible translation transformation

## Proposition content

to any

\[
\boldsymbol\theta^*
=
(\theta_1^*,\ldots,\theta_J^*)^\top
\in\mathbb R^J,
\]

There exists an invertible matrix that depends only on \(\boldsymbol\theta^*\)
\(D(\boldsymbol\theta^*)\), satisfied

\[
T\!\left(
Q,\Theta-\boldsymbol\theta^*\boldsymbol 1^\top
\right)
=
D(\boldsymbol\theta^*)T(Q,\Theta).
\tag{P3}
\]

\(D(\boldsymbol\theta^*)\) is a lower triangular matrix, and all diagonal elements are 1.

## What did the left side do?

Line \(j\) of \(\boldsymbol\theta^*\boldsymbol 1^\top\) is

\[
(\theta_j^*,\ldots,\theta_j^*).
\]

So the new single question line element is

\[
\theta_{j,\boldsymbol\alpha}-\theta_j^*.
\]

If you choose

\[
\theta_j^*
=
\theta_{j,\boldsymbol\alpha_0},
\]

Then the attribute column \(\boldsymbol\alpha_0\) becomes zero in this single question row. If Q restricts a batch of latent classes to share the same probability, this choice will eliminate the entire batch of units simultaneously.

## Two questions expanded

For \(J=2\), one column of the original \(T\)-matrix is

\[
\begin{pmatrix}
1\\
\theta_1\\
\theta_2\\
\theta_1\theta_2
\end{pmatrix}.
\]

After translation, it is

\[
\begin{pmatrix}
1\\
\theta_1-\theta_1^*\\
\theta_2-\theta_2^*\\
(\theta_1-\theta_1^*)
(\theta_2-\theta_2^*)
\end{pmatrix}.
\]

The last item expands to

\[
\theta_1\theta_2
-\theta_2^*\theta_1
-\theta_1^*\theta_2
+\theta_1^*\theta_2^*.
\]

So each row after translation is a linear combination of the lower order rows of the original \(T\)-matrix.

The corresponding transformation matrix can be written as

\[
D(\boldsymbol\theta^*)
=
\begin{pmatrix}
1&0&0&0\\
-\theta_1^*&1&0&0\\
-\theta_2^*&0&1&0\\
\theta_1^*\theta_2^*&-\theta_2^*&-\theta_1^*&1
\end{pmatrix}.
\]

It is a lower triangle with a determinant of 1 and must be invertible.

## General elements

If the row indicators are sorted by the subset inclusion relationship, then
\(\boldsymbol r'\preceq\boldsymbol r\)，
The coefficients of \(D\) come from the polynomial expansion:

\[
d_{\boldsymbol r,\boldsymbol r'}
=
(-1)^{|\boldsymbol r|-|\boldsymbol r'|}
\prod_{j:r_j-r'_j=1}\theta_j^*.
\]

When \(\boldsymbol r'\npreceq\boldsymbol r\), the coefficient is 0; when
The coefficient is 1 when \(\boldsymbol r'=\boldsymbol r\).

## Why not change the observable equation

If

\[
T(Q,\Theta)\boldsymbol p
=
T(Q,\bar\Theta)\bar{\boldsymbol p},
\]

Multiplying both sides by the same invertible matrix gives

\[
T(Q,\Theta-\boldsymbol\theta^*\boldsymbol 1^\top)
\boldsymbol p
=
T(Q,\bar\Theta-\boldsymbol\theta^*\boldsymbol 1^\top)
\bar{\boldsymbol p}.
\]

Therefore, studying the translated matrix is completely equivalent to studying the original observation distribution.

## The "eliminator" in the proof

The usage of Proposition 3 can be summarized as:

1. Select a group \(\theta_j^*\);
2. Use Q restriction to change a large number of columns to zero;
3. Take the Hadamard product of several single question lines;
4. Get rows that are non-zero in only one or a few attribute columns;
5. Multiply the row by \(\boldsymbol p\) to isolate a probability or a class proportion;
6. In \((\Theta,\boldsymbol p)\) and
   Compare between \((\bar\Theta,\bar{\boldsymbol p})\).

It is equivalent to performing latent class column-oriented symbolic elimination on the \(T\)-matrix.

## Why is it allowed to leave the probability interval after translation?

The elements of \(\Theta-\boldsymbol\theta^*\boldsymbol 1^\top\) may be negative and are no longer probabilities. The paper extends the algebraic definition of equation (3.3) to
\(\Theta\notin[0,1]^{J\times2^K}\). The proof only uses polynomial equations and reversible transformations, and does not require that the transformed values ​​still have probabilistic interpretations.
