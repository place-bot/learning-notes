# Proof steps 1--2

## Prove target and column order

Assume that the two sets of allowed parameters satisfy

\[
T(Q,\Theta)\boldsymbol p
=
T(Q,\bar\Theta)\bar{\boldsymbol p}.
\tag{3.5}
\]

Sort the latent class column by the number of mastered attributes:

\[
\boldsymbol 0,\ 
\boldsymbol e_1,\ldots,\boldsymbol e_K,\ 
\boldsymbol e_1+\boldsymbol e_2,\ldots,\ 
\boldsymbol 1.
\]

The first \(2K\) question is split into two \(I_K\) blocks by C1. The proof is to deal with the remaining questions of \(j>2K\) first.

## Conclusion of step 1

prove

\[
\theta_{j,\boldsymbol 0}
=
\bar\theta_{j,\boldsymbol 0},
\qquad j>2K.
\tag{S1}
\]

### Select translation vector

take

\[
\boldsymbol\theta^*
=
\left(
\bar\theta_{1,\boldsymbol 1},
\ldots,
\bar\theta_{K,\boldsymbol 1},
\theta_{K+1,\boldsymbol 1},
\ldots,
\theta_{2K,\boldsymbol 1},
0,\ldots,0
\right)^\top.
\]

The first block uses the highest probability of the parameter with a dash, and the second block uses the highest probability of the parameter without a dash.

For question \(k\) in the first block, as long as
\(\boldsymbol\alpha\succeq\boldsymbol e_k\), there is

\[
\bar\theta_{k,\boldsymbol\alpha}
-\bar\theta_{k,\boldsymbol 1}
=0.
\]

The same goes for the second block:

\[
\theta_{K+k,\boldsymbol\alpha}
-\theta_{K+k,\boldsymbol 1}
=0.
\]

### Multiply 2K anchor rows

Take the \(T\)-matrix row containing the previous \(2K\) question. Any non-zero attribute profile contains at least one attribute \(k\), and the corresponding zero suppression factor appears, so this line can only be in
\(\boldsymbol 0\) column is non-zero:

\[
T_{\sum_{\ell=1}^{2K}\boldsymbol e_\ell,\cdot}
\left(
Q,\Theta-\boldsymbol\theta^*\boldsymbol1^\top
\right)
=
(c_0,0,\ldots,0).
\]

Two technical lemmas and equation (2.3) guarantee

\[
c_0\ne0.
\]

### Add a remaining question line

Then add question \(j>2K\) to the same item subset:

\[
T_{\boldsymbol e_j+\sum_{\ell=1}^{2K}\boldsymbol e_\ell,\cdot}
=
\theta_{j,\boldsymbol0}
T_{\sum_{\ell=1}^{2K}\boldsymbol e_\ell,\cdot}.
\]

There are also corresponding formulas for parameters with horizontal lines. Multiply the two equations separately
\(\boldsymbol p\) and \(\bar{\boldsymbol p}\), and then using the transformed equation, the ratio of the two non-zero scalars is given

\[
\theta_{j,\boldsymbol0}
=
\bar\theta_{j,\boldsymbol0}.
\]

The essence of step 1 is to first construct a "select row" that only sees zero attribute classes.

## Conclusion of step 2

prove

\[
\theta_{j,\boldsymbol e_k}
=
\bar\theta_{j,\boldsymbol e_k},
\qquad
j>2K,\quad k=1,\ldots,K.
\tag{S2}
\]

### Take the single attribute class e₁ as an example

Change the translation benchmark of question 1 in the first block and question 1 in the second block from the highest probability to zero attribute probability, and the other anchor questions will still use the highest probability as the benchmark:

\[
\boldsymbol\theta^*
=
\left(
\bar\theta_{1,\boldsymbol0},
\bar\theta_{2,\boldsymbol1},
\ldots,
\bar\theta_{K,\boldsymbol1},
\theta_{K+1,\boldsymbol0},
\theta_{K+2,\boldsymbol1},
\ldots,
\theta_{2K,\boldsymbol1},
0,\ldots,0
\right)^\top.
\]

The Hadamard product of the first \(2K\) row is now only possible in
\(\boldsymbol e_1\) column is non-zero:

\[
T_{\sum_{\ell=1}^{2K}\boldsymbol e_\ell,\cdot}
\left(
Q,\Theta-\boldsymbol\theta^*\boldsymbol1^\top
\right)
=
(0,c_1,0,\ldots,0),
\]

Among them \(c_1\ne0\).

Non-zeroness requires the exclusion of equality across arguments, e.g.

\[
\theta_{k,\boldsymbol e_1}
=
\bar\theta_{k,\boldsymbol1},
\]

This is accomplished by Lemma 1, Lemma 2 and the strict order of the model.

### Use row ratio again

After adding question \(j>2K\):

\[
T_{\boldsymbol e_j+\sum_{\ell=1}^{2K}\boldsymbol e_\ell,\cdot}
=
\theta_{j,\boldsymbol e_1}
T_{\sum_{\ell=1}^{2K}\boldsymbol e_\ell,\cdot}.
\]

Comparing between two sets of parameters, we get

\[
\theta_{j,\boldsymbol e_1}
=
\bar\theta_{j,\boldsymbol e_1}.
\]

For each \(h=2,\ldots,K\), use the zero attribute benchmark for the anchor question \(h\), and repeat the same construction to get all
\(\boldsymbol e_h\) column.

## What was established in the first two steps?

Step 1--2 has identified the \(Q'\) item

\[
\left\{
\theta_{j,\boldsymbol0},
\theta_{j,\boldsymbol e_1},
\ldots,
\theta_{j,\boldsymbol e_K}
\right\},
\qquad j>2K.
\]

The known contrasts on these remaining questions are then passed through C2 in turn to identify the first two unit blocks and
\(p_{\boldsymbol0},p_{\boldsymbol e_k}\)。
