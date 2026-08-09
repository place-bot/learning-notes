# Proof details and hand calculation examples

## The complete proof chain of Theorem 4

The multivariable theorem appears to have only one block inequality, and five things are actually accomplished in the proof.

### Step 1: Divide the observed variables into three pieces

Choose

\[
S_1\dot\cup S_2\dot\cup S_3=\{1,\ldots,p\}.
\]

For each block

\[
N_a
=
\mathop{\otimes_{\mathrm{row}}}_{j\in S_a}M_j,
\qquad a=1,2,3.
\]

Due to local independence, \(N_a\) is the conditional probability matrix of the block reaction mode under each latent class.

### Step 2: The observation distribution gives a three-way tensor

Order

\[
\widetilde N_1=\operatorname{diag}(\pi)N_1.
\]

The observed joint distribution of the three blocks is

\[
\mathcal T
=
[\widetilde N_1,N_2,N_3].
\]

When the original joint distribution \(P(X_1,\ldots,X_p)\) is known, the joint probability of any three blocks is of course also known, so \(\mathcal T\) is known.

### Step 3: The general block matrix reaches the maximum Kruskal rank

Each \(N_a\) has \(r\) rows and \(K_a\) columns. Lemma 13 proves that under general parameters

\[
\operatorname{rank}_K(N_a)=\min(r,K_a).
\]

If the partitioning satisfies

\[
\sum_{a=1}^{3}\min(r,K_a)\ge2r+2,
\]

Kruskal's theorem can be applied.

### Step 4: Restore block parameters

Kruskal's theorem is restored first

\[
\pi,N_1,N_2,N_3
\]

to common label replacement. Probabilistic row and constraint elimination scaling.

### Step 5: Restore single variable parameters from block parameters

Each \(N_a\) is the row tensor product of \(M_j\) within the block. Summing the states of other variables yields any \(M_j\).

For example, \(S_a=\{1,2\}\), then

\[
N_a(i;x_1,x_2)
=
M_1(i,x_1)M_2(i,x_2).
\]

Sum \(x_2\):

\[
\sum_{x_2}N_a(i;x_1,x_2)
=
M_1(i,x_1)
\underbrace{\sum_{x_2}M_2(i,x_2)}_{1}
=
M_1(i,x_1).
\]

Therefore, intra-block factors can be uniquely separated by marginalization in the probabilistic model, without the need to do a non-unique matrix factorization.

## Vandermonde Proof of Lemma 13

Lemma 13 To show: Row tensor products have the maximum possible Kruskal rank under general parameters.

Set

\[
A_s\in\mathbb C^{r\times a_s},
\qquad s=1,\ldots,q.
\]

Select a set of mutually distinct prime numbers for each \(A_s\)

\[
x_{s1},\ldots,x_{sa_s},
\]

And order

\[
A_s(i,\ell)=x_{s\ell}^{i-1}.
\]

row tensor product

\[
A=\mathop{\otimes_{\mathrm{row}}}_{s=1}^{q}A_s
\]

In , the base corresponding to column index \((\ell_1,\ldots,\ell_q)\) is

\[
y_{\ell_1,\ldots,\ell_q}
=
\prod_{s=1}^{q}x_{s\ell_s}.
\]

Different column indexes produce different prime products, so these \(y\) are different from each other. The rows of matrix \(A\) have the form

\[
\begin{bmatrix}
1\\y\\y^2\\\vdots\\y^{r-1}
\end{bmatrix}^{\!\top},
\]

That is, the first \(r\) rows of the Vandermonde matrix.

- If the total number of columns is \(a=\prod_sa_s\ge r\), \(r\) mutually different \(y\) can be obtained to obtain the non-singular \(r\times r\) sub-matrix;
- If \(a<r\), arbitrarily choose the largest subformula corresponding to the required row of \(a\). In general, the Kruskal rank \(a\) can also be obtained through non-zero polynomial argument.

Therefore there is at least one maximum rank parameter point. The rank-decreasing subformulas are polynomials of parameters. The non-zero construction shows that they are not constant zero, and the maximum rank is established at general parameter points.

## Hand calculation: four potential classes, five two-point questions

Set

\[
r=4,\qquad p=5.
\]

Choose three pieces

\[
S_1=\{1,2\},\qquad
S_2=\{3,4\},\qquad
S_3=\{5\}.
\]

The number of states is

\[
K_1=4,\qquad K_2=4,\qquad K_3=2.
\]

Theorem 4 condition is

\[
\min(4,4)+\min(4,4)+\min(4,2)
=
4+4+2
=
10
=
2r+2.
\]

Therefore, the model can recognize category replacement under general parameters.

### Set category ratio

\[
\pi=(0.10,0.20,0.30,0.40).
\]

For five questions, let the probability of correct answers for each category form a matrix

\[
\Theta=
\begin{bmatrix}
0.15&0.20&0.25&0.30&0.35\\
0.30&0.40&0.50&0.60&0.70\\
0.55&0.65&0.35&0.75&0.45\\
0.80&0.70&0.85&0.65&0.90
\end{bmatrix}.
\]

The single question matrix row of class \(i\) and question \(j\) is

\[
M_j(i,\cdot)
=
(1-\theta_{ij},\theta_{ij}).
\]

### Construct a line of the first block

For the first latent class,

\[
\theta_{11}=0.15,\qquad
\theta_{12}=0.20.
\]

The probabilities of the four response modes for questions 1--2 are

\[
\begin{aligned}
P(00\mid Z=1)&=0.85\times0.80=0.68,\\
P(01\mid Z=1)&=0.85\times0.20=0.17,\\
P(10\mid Z=1)&=0.15\times0.80=0.12,\\
P(11\mid Z=1)&=0.15\times0.20=0.03.
\end{aligned}
\]

Therefore

\[
N_1(1,\cdot)=(0.68,0.17,0.12,0.03).
\]

The sum of the rows is 1.

For the second latent class,

\[
\theta_{21}=0.30,\qquad\theta_{22}=0.40,
\]

So

\[
N_1(2,\cdot)
=
(0.42,0.28,0.18,0.12).
\]

The remaining two rows are calculated in the same way.

### Restore single question probabilities from block rows

Recovery question 1 from block rows of type 1 Probability of correct answer:

\[
P(X_1=1\mid Z=1)
=
P(10\mid Z=1)+P(11\mid Z=1)
=
0.12+0.03
=
0.15.
\]

Recovery question 2:

\[
P(X_2=1\mid Z=1)
=
P(01\mid Z=1)+P(11\mid Z=1)
=
0.17+0.03
=
0.20.
\]

This shows the Lemma 14 in action.

### Calculate an overall response pattern probability

Consider answering all five questions correctly:

\[
\boldsymbol x=(1,1,1,1,1).
\]

The overall probability is

\[
P(\boldsymbol X=\boldsymbol 1)
=
\sum_{i=1}^{4}\pi_i\prod_{j=1}^{5}\theta_{ij}.
\]

Contributions by category are

\[
\begin{aligned}
i=1:&\quad
0.10(0.15)(0.20)(0.25)(0.30)(0.35)
=0.00007875,\\
i=2:&\quad
0.20(0.30)(0.40)(0.50)(0.60)(0.70)
=0.00504,\\
i=3:&\quad
0.30(0.55)(0.65)(0.35)(0.75)(0.45)
=0.01266890625,\\
i=4:&\quad
0.40(0.80)(0.70)(0.85)(0.65)(0.90)
\approx0.111384.
\end{aligned}
\]

Therefore

\[
P(\boldsymbol X=\boldsymbol 1)
=0.12917165625.
\]

The observation distribution contains the probability of all \(2^5=32\) reaction patterns. The theorem shows that under general parameters, this entire probability table is sufficient to uniquely derive \(\pi\) and \(\Theta\), allowing the four categories to be renamed together.

## Why does label replacement not change the distribution?

Take replacement

\[
\sigma=(1\ 4),
\]

Swap Category 1 and Category 4. definition

\[
\pi_i'=\pi_{\sigma(i)},
\qquad
\theta_{ij}'=\theta_{\sigma(i),j}.
\]

rule

\[
\sum_{i=1}^{4}\pi_i'
\prod_{j=1}^{5}
P_{\theta'_{ij}}(X_j=x_j)
=
\sum_{i=1}^{4}\pi_{\sigma(i)}
\prod_{j=1}^{5}
P_{\theta_{\sigma(i),j}}(X_j=x_j).
\]

Because \(\sigma\) only rearranges the summation terms, the result is the same as the original distribution.

This is why general latent class theory cannot automatically name classes. CDM needs to use the Q matrix and attribute structure to map the unnamed category rows back to attribute profiles such as \((0,0),(0,1),(1,0),(1,1)\).

## Why did the condition fail during the fourth question?

Still assuming \(r=4\), if there are only \(p=4\) dichotomous variables, the most balanced size of the three non-empty blocks can only be

\[
(2,1,1).
\]

The number of block states is

\[
(4,2,2),
\]

So

\[
\min(4,4)+\min(4,2)+\min(4,2)
=
4+2+2
=
8
<
10.
\]

Theorem 4 cannot authenticate this set of dimensions. The indiscernibility theorem is not obtained here, but it can only show that the five-variable sufficient condition cannot be shortened to four variables.

## A clear point of unrecognizable degradation

If two latent classes have exactly the same response profile

\[
\theta_{1j}=\theta_{2j},
\qquad j=1,\ldots,p,
\]

Then their product distributions are the same:

\[
P_1=P_2.
\]

Only appears in the observation mix

\[
\pi_1P_1+\pi_2P_2
=(\pi_1+\pi_2)P_1.
\]

Keep \(\pi_1+\pi_2\) unchanged and continuously change the distribution of the two, and the observation distribution remains unchanged. This is the degenerate parameter point that pan-identification allows to exclude.

## Sufficient conditions, necessary conditions and algorithms should be separated

The hand calculation of this paper can examine three levels:

1. **Dimension-level sufficient conditions**: Whether the number of block states satisfies Theorem 4;
2. **Specific parameter point conditions**: Whether the Kruskal rank of the actual block matrix is sufficient;
3. **Numerical recovery algorithm**: How to stably recover parameters from frequency tables containing sampling errors.

The paper addresses the theoretical uniqueness of the first two levels, and the third level is outside the scope of its research.
