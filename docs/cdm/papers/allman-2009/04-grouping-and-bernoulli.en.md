# Blocking theorem mixed with Bernoulli

## Why should we divide variables into three pieces?

The three-variable theorem requires that the three factor matrices have sufficiently high Kruskal ranks. The single question matrix of dichotomous item has only two columns, even if there are many potential classes

\[
\operatorname{rank}_K(M_j)\le 2.
\]

After merging multiple questions into a composite variable, if a block contains \(m\) two-point questions, the composite variable has

\[
2^m
\]

a reaction pattern. The corresponding block conditional probability matrix has \(2^m\) columns, possibly reaching higher row ranks.

## Three divisions

Set variable index

\[
\{1,\ldots,p\}
\]

Divide into three non-empty, disjoint sets

\[
S_1,\ S_2,\ S_3.
\]

The \(a\)th composite variable is

\[
X_{S_a}=(X_j:j\in S_a).
\]

Its status number is

\[
K_a=\prod_{j\in S_a}\kappa_j,
\qquad a=1,2,3.
\]

The original text used \(\kappa_a\) to represent this block status number in Theorem 4; this site uses \(K_a\) instead to avoid confusion with the single-variable status number \(\kappa_j\).

## Row tensor product

If

\[
A_1\in\mathbb R^{r\times a_1},
\qquad
A_2\in\mathbb R^{r\times a_2},
\]

Their row tensor product is written as

\[
A_1\otimes_{\mathrm{row}}A_2
\in\mathbb R^{r\times a_1a_2}.
\]

Row \(i\) is equal to the Kronecker product of row \(i\) of the two matrices:

\[
\bigl(A_1\otimes_{\mathrm{row}}A_2\bigr)(i,\cdot)
=
A_1(i,\cdot)\otimes A_2(i,\cdot).
\]

For block \(S_a\), define

\[
N_a
=
\mathop{\otimes_{\mathrm{row}}}_{j\in S_a}M_j
\in\mathbb R^{r\times K_a}.
\]

Given \(Z=i\), the original variables are independent, so the \(i\) line of \(N_a\) is the conditional joint distribution of the composite variable \(X_{S_a}\).

## A block of two two-point questions

If

\[
M_1(i,\cdot)=(1-\theta_{1i},\theta_{1i}),
\qquad
M_2(i,\cdot)=(1-\theta_{2i},\theta_{2i}),
\]

Then the \(i\) behavior of the two question block matrices

\[
\begin{aligned}
N(i,\cdot)
=\bigl(&
(1-\theta_{1i})(1-\theta_{2i}),\\
&(1-\theta_{1i})\theta_{2i},\\
&\theta_{1i}(1-\theta_{2i}),\\
&\theta_{1i}\theta_{2i}
\bigr).
\end{aligned}
\]

The four columns correspond to the reaction patterns in sequence.

\[
(0,0),(0,1),(1,0),(1,1).
\]

To marginalize a certain question, you only need to sum the status of the other question. For example

\[
\theta_{1i}
=
N_i(1,0)+N_i(1,1).
\]

This is the probabilistic intuition of paper Lemma 14: if the block matrix is obtained by row tensor product of several random matrices, the original univariate matrix can be uniquely restored by marginalization.

## Lemma 12, 13, 14 What do each do?

|Lemma|function|
| --- | --- |
| Lemma 12 |Conditional independence guarantees that the block conditional probability matrix is equal to the row tensor product of the univariate matrix|
| Lemma 13 |The row tensor product of a general matrix has the maximum possible Kruskal rank \(\min(r,K_a)\)|
| Lemma 14 |Unique recovery from random block matrix \(N_a\) by marginalizing each \(M_j\) within the block|

These three items completely connect the "multivariable problem" back to the "three-variable Kruskal problem".

## Theorem 4: Multi-variable universal recognition

If there are three divisions, let

\[
\min(r,K_1)+\min(r,K_2)+\min(r,K_3)
\ge 2r+2,
\tag{2}
\]

rule

\[
\mathcal M(r;\kappa_1,\ldots,\kappa_p)
\]

The parameter pan can recognize the label replacement. Fixing positive class proportions does not change the conclusions either.

The proof chain is:

\[
\{M_j\}_{j=1}^{p}
\overset{\text{row tensor product}}{\longrightarrow}
(N_1,N_2,N_3)
\overset{\text{Kruskal}}{\longrightarrow}
(\pi,N_1,N_2,N_3)
\overset{\text{marginalized}}{\longrightarrow}
(\pi,M_1,\ldots,M_p).
\]

## Lemma 13 Why can we get the maximum rank?

The paper uses a Vandermonde construction to prove that "there is at least one full-rank point."

Select the mutually distinct prime numbers \(x_{a1},\ldots,x_{a\kappa_a}\) for the \(a\)th univariate matrix, and the command line \(i\) consists of these numbers raised to the \(i-1\) power:

\[
A_a(i,\ell)=x_{a\ell}^{i-1}.
\]

Column corresponding product in row tensor product

\[
\prod_a x_{a,\ell_a}.
\]

Prime factorization uniqueness guarantees that different column indices give different products, so the row tensor product becomes a Vandermonde-type matrix with the maximum possible rank.

A full-rank subexpression is a polynomial over the elements of the original matrix, and this construction makes a subexpression nonzero, so the subexpression is not always equal to 0. Rank degradation occurs only on its zero point set.

## Corollary 5: Concise upper bound for dichotomous variables

Now let all variables be Bernoulli:

\[
\kappa_1=\cdots=\kappa_p=2.
\]

Set

\[
k=\lceil\log_2r\rceil.
\]

Take the size of three blocks as

\[
|S_1|=k,\qquad
|S_2|=k,\qquad
|S_3|=1.
\]

The number of block states is

\[
K_1=2^k,\qquad
K_2=2^k,\qquad
K_3=2.
\]

Due to \(2^k\ge r\), the left side of Theorem 4 becomes

\[
\min(r,2^k)+\min(r,2^k)+\min(r,2)
=
r+r+2
=
2r+2.
\]

So as long as

\[
p\ge 2\lceil\log_2r\rceil+1,
\tag{B}
\]

A finite mixture of \(r\) Bernoulli product distributions is universally identifiable to label permutations.

## How the upper bound grows with the number of potential classes

|Number of potential classes \(r\)| \(\lceil\log_2r\rceil\) |Corollary 5 gives the sufficient number of variables|
| ---: | ---: | ---: |
| 2 | 1 | 3 |
| 3 | 2 | 5 |
| 4 | 2 | 5 |
| 5--8 | 3 | 7 |
| 9--16 | 4 | 9 |
| 17--32 | 5 | 11 |

The upper bound increases by \(\log_2r\). The paper also uses dimension comparison to point out that the growth order with the smallest number of variables is also \(\log_2r\), so Corollary 5 has obtained the correct growth order, but the constant may not be optimal.

## Translated into complete attribute profile CDM

If there are \(K\) binary attributes and all are allowed

\[
r=2^K
\]

attribute profile, then

\[
\lceil\log_2r\rceil=K.
\]

Corollary 5 becomes

\[
J\ge 2K+1.
\tag{CDM intuition}
\]

This expression only describes the universal recognition upper bound of unconstrained Bernoulli latent class mixtures. It cannot directly replace CDM's Q-matrix design conditions for several reasons:

1. \(\theta_{j,\boldsymbol\alpha}\) of CDM is constrained by the Q matrix and model function, and is not a free parameter of the general position;
2. Some attribute profiles may be structurally missing, and the actual number of categories is less than \(2^K\);
3. Different attribute profiles may produce the same ideal response under a given Q;
4. Generally, latent class recognition only retains categories without names and cannot automatically restore attribute coordinates;
5. DINA’s \(g_j,s_j\) needs to be further identified using the conjunctive structure of the model.

Therefore, \(J\ge 2K+1\) is suitable for explaining "why enough dichotomous items can support potential class recovery", but is not suitable for directly serving as a CDM test composition rule.

## General \(\kappa\) state variable

If each observed variable has the same \(\kappa\) states, the same blocking argument gives

\[
p\ge 2\lceil\log_\kappa r\rceil+1.
\]

The richer the univariate state, the fewer variables are needed to reach \(r\) distinct block states. This rule also appears in the HMM result of the paper: when the number of observable states increases, the length of continuous observations required for identification can decrease.

