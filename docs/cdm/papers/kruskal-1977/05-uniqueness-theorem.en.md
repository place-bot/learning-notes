# Core uniqueness theorem

## Modern writing of Theorem 4a

Set

\[
\mathcal X=[A,B,C]
=
\sum_{r=1}^{R}
\boldsymbol a_r\otimes
\boldsymbol b_r\otimes
\boldsymbol c_r,
\]

Three of the factor matrices have \(R\) columns. remember

\[
k_A,\qquad k_B,\qquad k_C
\]

Kruskal rank for the columns of the three matrices.

If

\[
k_A+k_B+k_C\ge 2R+2,
\tag{K}
\]

Then:

1. \(\operatorname{rank}(\mathcal X)=R\)；
2. The decomposition of this \(R\) item is essentially unique;
3. Any other set of factors can only be obtained by column-by-column scaling with common column permutation and mutual cancellation.

That is, if

\[
[A,B,C]=[\bar A,\bar B,\bar C],
\]

Then there are permutation matrix \(P\) and invertible diagonal matrix \(\Lambda,M,N\), so that

\[
\bar A=AP\Lambda,\qquad
\bar B=BPM,\qquad
\bar C=CPN,
\]

And the three scaled products of the corresponding components are 1.

## Original expression and modern notation

The original text uses "each set of specified number of columns is independent" to describe the conditions of the three factors. Modern literature records these three designated quantities directly as \(k_A,k_B,k_C\).

Rhodes (2010) Order

\[
a_1=R-k_A,\qquad
a_2=R-k_B,\qquad
a_3=R-k_C.
\]

Then condition (K) is equivalent to

\[
a_1+a_2+a_3\le R-2.
\tag{6}
\]

\(a_\ell\) can be understood as how far away the \(k\)-rank of the \(\ell\)-th factor is from the full column rank.

## How to read conditions

The left side summarizes the ability to resist column confusion in three directions:

\[
k_A+k_B+k_C.
\]

The right-hand side increases linearly with the component fraction:

\[
2R+2.
\]

The more components there are, the more independence the three factors combined need to provide.

### \(R=2\)

If any two columns of the three matrices are independent,

\[
k_A=k_B=k_C=2,
\]

rule

\[
2+2+2=6=2R+2.
\]

The conditions are just borderline.

### \(R=3\)

If the three \(3\) column matrices all have full column ranks,

\[
3+3+3=9\ge 8.
\]

Allow the \(k\)-rank of one of the factors to drop to 2:

\[
3+3+2=8.
\]

### Completely indistinguishable components in a certain direction

If at least two columns in \(k_C=1\), that is, \(C\), are proportional, then even

\[
k_A=k_B=R,
\]

There is only one on the left

\[
R+R+1=2R+1<2R+2.
\]

The theorem cannot prove uniqueness. This is consistent with intuition: the third direction cannot separate those two components, and the problem may degenerate into matrix factorization.

## Why can the condition also ensure that the tensor rank is \(R\)

Assume there is a decomposition with less than \(R\) terms. You can add zero columns to it and write it as another \(R\) column triple product. Kruskal's conclusion would require that the new factors correspond to the causal factors by reversible scaling and permutation.

Condition (K) at least ensures that there are no zero columns in the causal factor; reversible scaling and permutation cannot turn non-zero columns into complemented zero columns, thus creating a contradiction. So there is no shorter decomposition.

## Logical boundary of sufficient conditions

\[
k_A+k_B+k_C\ge2R+2
\quad\Longrightarrow\quad
\text{Essentially unique}.
\]

When an inequality fails, only "No verification of the theorem is given" can be recorded. Some decompositions remain unique and require other weaker or more targeted conditions; other decompositions do have multiple solutions.

Therefore, if an empirical paper simply reports that an inequality fails, it cannot be directly interpreted as a parameter that is not identifiable.

## Location of Theorem 4b and 4c

Kruskal's original text also gives 4b and 4c which are thinner than 4a. They relax simple summation conditions through functions on the ranks of different column subsets and several piecewise inequalities, but are more expensive to formulate and verify.

This topic focuses on 4a for the following reasons:

- It is the version directly cited by Allman (2009) and most CDM identification papers;
- The conditions only require three \(k\)-rank, which is easy to connect with the block probability matrix;
- Rhodes' modern complete proof corresponds exactly to 4a;
- The existence of 4b and 4c reminds us that after the failure of 4a, there may still be more sophisticated uniqueness tools.
