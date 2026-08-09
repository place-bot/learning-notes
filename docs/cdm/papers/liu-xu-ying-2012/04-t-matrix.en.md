# B-vector and T-matrix

## Column: All attribute profiles

\(T\)-matrix has column \(2^K\). Each column corresponds to an attribute profile \(\boldsymbol\alpha\). The column order can be chosen arbitrarily, but \(T\) and \(\boldsymbol p\) must use the same order.

## Single question B-vector

For item \(j\), define a row vector of length \(2^K\)

\[
B_{Q',\boldsymbol c,\boldsymbol g}(j)
=
\left(
\Pr(R^j=1\mid\boldsymbol\alpha,Q',\boldsymbol c,\boldsymbol g)
:
\boldsymbol\alpha\in\{0,1\}^K
\right).
\tag{5}
\]

If the attribute profile is arranged according to \(\boldsymbol\alpha_1,\ldots,\boldsymbol\alpha_{2^K}\), the \(a\) element is

\[
g_j+(c_j-g_j)\xi^j(\boldsymbol\alpha_a,Q').
\]

## Multiple questions B-vector

locally given independently

\[
B(j_1,j_2)
=
B(j_1)\odot B(j_2),
\]

where \(\odot\) represents element-wise multiplication. Generally,

\[
B(j_1,\ldots,j_\ell)
=
\bigodot_{h=1}^{\ell}B(j_h).
\]

The \(a\) element is the probability of answering the \(\ell\) questions simultaneously under the attribute profile \(\boldsymbol\alpha_a\).

## Row: selected item combination

Selected question group collection

\[
\mathcal C=\{A_1,\ldots,A_L\},
\]

Stack corresponding B-vectors:

\[
T_{\boldsymbol c,\boldsymbol g}(Q')
=
\begin{pmatrix}
B(A_1)\\
\vdots\\
B(A_L)
\end{pmatrix}.
\]

Therefore the dimensions of \(T\) are

\[
L\times 2^K.
\]

## Multiply attribute distribution

\[
T_{\boldsymbol c,\boldsymbol g}(Q')\boldsymbol p
\tag{6}
\]

Make a weighted average of the conditional joint correct answer probabilities of each attribute profile to obtain the overall joint correct answer rate.

If the candidate structure and parameters are correct,

\[
\boldsymbol\beta
\xrightarrow{\text{a.s.}}
T_{\boldsymbol c,\boldsymbol g}(Q)\boldsymbol p,
\qquad N\to\infty.
\tag{7}
\]

## Dimension check

\[
\underbrace{T}_{L\times2^K}
\underbrace{\boldsymbol p}_{2^K\times1}
=
\underbrace{\text{model moment}}_{L\times1},
\qquad
\underbrace{\boldsymbol\beta}_{L\times1}.
\]

Doing this check first every time you push a formula can avoid mixing the student's posterior matrix, category proportions and question group moments.

## The relationship between T and Q

Q changes the ideal response grouping of a question, thereby changing the B-vector of the question; the B-vectors of all multiple questions containing this question will also change. Therefore a q-vector update affects multiple moment constraints simultaneously.
