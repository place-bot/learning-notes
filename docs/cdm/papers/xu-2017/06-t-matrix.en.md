# Marginal T matrix

## Rewritten from exact pattern to subset success

Complete reaction pattern probability

\[
P(\boldsymbol R=\boldsymbol r)
\]

It is required to record the correct or incorrect answers for each question at the same time. Paper conversion event

\[
\boldsymbol R\succeq\boldsymbol r,
\]

That is, all questions that meet \(r_j=1\) must be answered correctly, and the remaining questions are not required.

## Definition

\(T(Q,\Theta)\) is a

\[
2^J\times 2^K
\]

matrix. Row by item subset indicator
\(\boldsymbol r\in\{0,1\}^J\) number, listed by attribute profile
\(\boldsymbol\alpha\in\{0,1\}^K\) Number:

\[
t_{\boldsymbol r,\boldsymbol\alpha}(Q,\Theta)
=
P(\boldsymbol R\succeq\boldsymbol r
\mid Q,\Theta,\boldsymbol\alpha).
\]

If \(\boldsymbol r=\boldsymbol 0\), the event has no requirements:

\[
t_{\boldsymbol 0,\boldsymbol\alpha}=1.
\]

If \(\boldsymbol r\ne\boldsymbol 0\), locally given independently

\[
t_{\boldsymbol r,\boldsymbol\alpha}
=
\prod_{j:r_j=1}
\theta_{j,\boldsymbol\alpha}.
\tag{T}
\]

## The single question line is Theta

Let \(\boldsymbol e_j\) represent the \(J\)-dimensional unit vector whose \(j\)th position is 1, then

\[
t_{\boldsymbol e_j,\boldsymbol\alpha}
=
P(R_j=1\mid\boldsymbol\alpha)
=
\theta_{j,\boldsymbol\alpha}.
\]

Therefore

\[
T_{\boldsymbol e_j,\cdot}(Q,\Theta)
=
\Theta_{j,\cdot}.
\]

As long as all single question rows of the two sets of \(T\)-matrices are finally proved to be equal, we will get \(\Theta=\bar\Theta\).

## Hadamard product of rows

Let \(\odot\) be the element-wise product. Any item subset row can be constructed from a single question row:

\[
T_{\boldsymbol r,\cdot}(Q,\Theta)
=
\bigodot_{j:r_j=1}
T_{\boldsymbol e_j,\cdot}(Q,\Theta).
\tag{3.3}
\]

This multiplication structure is the basis for the later "choose a translation amount to eliminate certain units to zero".

## Multiply the attribute distribution

\[
\begin{aligned}
T_{\boldsymbol r,\cdot}(Q,\Theta)\boldsymbol p
&=
\sum_{\boldsymbol\alpha}
t_{\boldsymbol r,\boldsymbol\alpha}
p_{\boldsymbol\alpha}\\
&=
P(\boldsymbol R\succeq\boldsymbol r
\mid Q,\Theta,\boldsymbol p).
\end{aligned}
\]

So \(T(Q,\Theta)\boldsymbol p\) collects the marginal all-pair probability of all item subsets.

## Why is it equivalent to the complete observation distribution?

The subset margin can be found directly from the exact pattern probability:

\[
P(\boldsymbol R\succeq\boldsymbol r)
=
\sum_{\boldsymbol r'\succeq\boldsymbol r}
P(\boldsymbol R=\boldsymbol r').
\]

Use inclusion--exclusion in reverse:

\[
P(\boldsymbol R=\boldsymbol r)
=
\sum_{\boldsymbol u\succeq\boldsymbol r}
(-1)^{|\boldsymbol u|-|\boldsymbol r|}
P(\boldsymbol R\succeq\boldsymbol u),
\]

where the summation is performed over the superset compatible with the positive reaction position of \(\boldsymbol r\). The two representations are a one-to-one mapping.

## Proposition 1

\((\Theta,\boldsymbol p)\) is identifiable if and only if for any different
\((\bar\Theta,\bar{\boldsymbol p})\), at least one exists
\(\boldsymbol r\) use

\[
T_{\boldsymbol r,\cdot}(Q,\Theta)\boldsymbol p
\ne
T_{\boldsymbol r,\cdot}(Q,\bar\Theta)\bar{\boldsymbol p}.
\tag{3.4}
\]

Therefore the master proof only needs to establish

\[
T(Q,\Theta)\boldsymbol p
=
T(Q,\bar\Theta)\bar{\boldsymbol p}
\Longrightarrow
\Theta=\bar\Theta,\quad
\boldsymbol p=\bar{\boldsymbol p}.
\tag{3.5}
\]

## Two small examples

If \(J=2\), the row order is
\(\boldsymbol 0,\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_1+\boldsymbol e_2\), then a certain attribute is listed as

\[
T_{\cdot,\boldsymbol\alpha}
=
\begin{pmatrix}
1\\
\theta_{1,\boldsymbol\alpha}\\
\theta_{2,\boldsymbol\alpha}\\
\theta_{1,\boldsymbol\alpha}\theta_{2,\boldsymbol\alpha}
\end{pmatrix}.
\]

The last row is the conditional probability of answering both questions correctly at the same time. This "constant, linear term, product term" structure enables the \(T\)-matrix to have exploitable polynomial algebra.
