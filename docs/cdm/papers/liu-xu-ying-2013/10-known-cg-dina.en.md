# DINA of known errors and guessing parameters

## Two item parameters

For question \(i\):

- \(s_i\): The error probability of answering incorrectly despite having the required attributes;
- \(c_i=1-s_i\): The probability of answering correctly when having the required attributes;
- \(g_i\): Probability of correct guess when at least one required attribute is missing.

The paper uses \(\boldsymbol c=(c_1,\ldots,c_m)^\top\) and \(\boldsymbol g=(g_1,\ldots,g_m)^\top\).

## DINA reaction function

\[
\Pr(R^i=1\mid\xi^i)
=
c_i^{\xi^i}g_i^{1-\xi^i}.
\tag{3.1}
\]

There are two situations:

\[
\Pr(R^i=1\mid\xi^i=1)=c_i,
\]

\[
\Pr(R^i=1\mid\xi^i=0)=g_i.
\]

It can also be written as

\[
\Pr(R^i=1\mid\boldsymbol A)
=
g_i+(c_i-g_i)\xi^i(\boldsymbol A).
\]

The latter writing method directly leads to the structure of \(T_{c,g}(Q)\).

## Partially independent

The paper assumes that after all ability indicators are given, the responses to each question are jointly independent:

\[
\Pr(\boldsymbol R=\boldsymbol r\mid\boldsymbol\xi)
=
\prod_{i=1}^m
\Pr(R^i=r_i\mid\xi^i).
\]

Therefore, for the question group \(S=\{i_1,\ldots,i_\ell\}\),

\[
\Pr(R^{i_1}=\cdots=R^{i_\ell}=1\mid\boldsymbol A)
=
\prod_{h=1}^{\ell}
\Pr(R^{i_h}=1\mid\boldsymbol A).
\]

This corresponds exactly to element-wise multiplication of a B-vector.

## First look at \(g_i=0\)

If all guess probabilities are 0, a person lacking the required attribute cannot answer correctly. Definition of single question

\[
B_{c,Q}(I_i)
=c_iB_Q(I_i).
\]

question group definition

\[
B_{c,Q}(I_{i_1}\wedge\cdots\wedge I_{i_\ell})
=
\mathop{\Upsilon}_{h=1}^{\ell}
B_{c,Q}(I_{i_h}).
\tag{3.3}
\]

Let \(D_c\) be a diagonal matrix. If a row corresponds to the question group \(S\), its diagonal element is

\[
\prod_{i\in S}c_i.
\]

So

\[
T_c(Q)=D_cT(Q).
\tag{3.2}
\]

As long as all \(c_i\ne0\), \(D_c\) are invertible, row scaling does not change the column rank of \(T(Q)\).

## General \(g_i>0\)

Order

\[
\boldsymbol E=(1,\ldots,1)
\]

is a full 1-row vector. For the non-zero attribute profile column, the single question probability row is

\[
B_{c,g,Q}(I_i)
=
g_i\boldsymbol E
+(c_i-g_i)B_Q(I_i).
\tag{3.5}
\]

If an attribute profile has the capability, \(B_Q(I_i)=1\), the component is equal to \(c_i\); if it does not have the capability, the component is equal to \(g_i\).

The question group rows continue to be multiplied element by element:

\[
B_{c,g,Q}(I_{i_1}\wedge\cdots\wedge I_{i_\ell})
=
\mathop{\Upsilon}_{h=1}^{\ell}
B_{c,g,Q}(I_{i_h}).
\]

## Why all-zero attribute profiles need to be processed separately

When there is no noise, the all-zero pattern contributes 0 to all joint correct answer probabilities. When the guess exists, its contribution to the question group \(S\) is

\[
\prod_{i\in S}g_i.
\]

Therefore, the paper retains the non-zero attribute column of \(T_{c,g}(Q)\) and writes the all-zero mode contribution as

\[
p_0\boldsymbol g_{\mathrm{joint}},
\]

Among them, \(\boldsymbol g_{\mathrm{joint}}\) arranges the guess probability products according to each question group.

## Common conditions \(c_i>g_i\)

Cognitive explanations usually require

\[
c_i>g_i.
\]

This means that having all the required attributes increases the probability of getting the answer right. The original condition of Theorem 3.1 is slightly wider, requiring \(c_i\ne g_i\), and adding an additional non-zero moment condition. The subsequent Proposition 6.6 handles the difference between the two through \(\boldsymbol c-\boldsymbol g\).

[Next page: Noise T-matrix and objective function](11-noisy-tmatrix-objective.md)
