# Summary and further reading

## A formula summarizes the main result

For a limited latent class model, if the observed variables can be divided into three non-empty blocks, and let

\[
K_a=\prod_{j\in S_a}\kappa_j,
\]

make

\[
\min(r,K_1)+\min(r,K_2)+\min(r,K_3)
\ge2r+2,
\]

Then the general parameter point is

\[
\pi,\ M_1,\ldots,M_p
\]

It can be recovered from the observed joint distribution to the latent class joint permutation.

## Shortest version of proof method

\[
P(X_1,\ldots,X_p)
\longrightarrow
[\operatorname{diag}(\pi)N_1,N_2,N_3]
\]

\[
\overset{\text{Kruskal}}{\longrightarrow}
\pi,N_1,N_2,N_3
\overset{\text{marginalized}}{\longrightarrow}
\pi,M_1,\ldots,M_p.
\]

Among them

\[
N_a
=
\mathop{\otimes_{\mathrm{row}}}_{j\in S_a}M_j.
\]

## Five conclusions that must be remembered

1. Three-way tensors provide stronger decomposition uniqueness than two-way matrices.
2. Kruskal's rank condition is a sufficient condition for point states; the maximum possible rank condition gives universal identification.
3. Multiple observation variables can be combined into three composite variables, and the number of block states increases multiplicatively.
4. \(r\) class Bernoulli product mixture in
   \[
   p\ge2\lceil\log_2r\rceil+1
   \]
   Tag substitutions are generally recognized.
5. The same set of conditionally independent blocking ideas can also handle HMM, random graphs and non-parametric product mixtures.

## Five borders

1. The latent class number \(r\) is assumed to be known.
2. generic allows unrecognizable parameter points with measure 0.
3. Theoretical uniqueness does not guarantee the stability of finite sample estimation.
4. The paper does not contain estimation algorithms, data experiments or official code.
5. General latent class identification does not directly recover the Q matrix and attribute meaning.

## Accurate conclusions about CDM

If attribute profile is used as latent class, this article supports

\[
P(\boldsymbol Y)
\longrightarrow
\text{Latent class proportion and class conditional itemresponse probability}
\]

Theoretical ideas for this step. Follow-up still requires CDM special conditions to be completed

\[
\text{Unnamed latent class table}
\longrightarrow
Q,\boldsymbol\alpha,g,s
\quad\text{or other CDM parameters}.
\]

Under the complete attribute profile \(r=2^K\), Corollary 5 is given

\[
J\ge2K+1
\]

The underlying mixture model is sufficiently upper bounded. It provides theoretical intuition and does not replace Q-matrix completeness, repeated measurements of attributes, and model-specific identification conditions.

## Kruskal (1977) The topic has been completed

Allman et al.'s proof uses Kruskal's theorem as a core tool. The corresponding mathematical tools topic has been completed:

> Kruskal, J. B. (1977). Three-way arrays: Rank and uniqueness of trilinear decompositions, with application to arithmetic complexity and statistics.

[Enter Kruskal (1977) complete topic](../kruskal-1977/index.md), you can continue to view:

- The essential difference between Kruskal rank and ordinary rank;
- Where does \(I_1+I_2+I_3\ge2r+2\) come from;
- How to strictly express permutation and scaling in uniqueness;
- Whether the condition is sufficient or necessary;
- How to distinguish between tensor degradation and numerical instability;
- Which part of the theorem is specifically called in the subsequent CDM three-block proof.

## The subsequent sequence of CDM main line

After completing the Kruskal tool, the CDM main line enters in sequence:

1. de la Torre (2009): DINA model and parameter estimation;
2. de la Torre (2011): G-DINA framework;
3. Xu (2017): Bipartite RLCM identifiability;
4. Gu and Xu: DINA identification and estimability conditions;
5. Gu and Xu (2021): Necessary and sufficient identification conditions for Q matrices.

This reading can connect the three lines of "what is the model", "why can it be recognized" and "how to estimate".
