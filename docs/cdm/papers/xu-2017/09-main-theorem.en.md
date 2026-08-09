# Main theorem and test design implications

## Theorem 1

Under the model setting and restriction formulas (2.2)--(2.3) in Section 2.1 of the paper, if C1 and C2 hold, then

\[
(\Theta,\boldsymbol p)
\]

Recognizable.

The complete quantifier is:

\[
T(Q,\Theta)\boldsymbol p
=
T(Q,\bar\Theta)\bar{\boldsymbol p}
\Longrightarrow
\Theta=\bar\Theta,\quad
\boldsymbol p=\bar{\boldsymbol p}.
\]

The conclusion covers all allowed parameter points that satisfy the assumptions, and is therefore strict identifiability.

## What does the theorem cover?

When the corresponding parameter constraints hold, it provides uniform identification guarantees for the following models:

- DINA；
- DINO；
- G-DINA；
- linear logistic / logit-CDM；
- reduced RUM / log-CDM；
- Other dichotomous diagnostic models in the paper-restricted family.

The theorem directly identifies \(\Theta\) and \(\boldsymbol p\). The low-dimensional parameters of the specific model also require a one-to-one mapping of its parameterization to \(\Theta\).

## Design meaning

If single-attribute questions can be compiled, the paper recommends:

1. Prepare at least two complete single-attribute question blocks to ensure C1;
2. Check whether the remaining items can provide distinction between each \(\boldsymbol e_k\) and \(\boldsymbol 0\);
3. If it needs to be completely guaranteed by the Q structure, three \(I_K\) blocks can be prepared.

When the parameter estimates of existing tests are abnormal and Q does not meet the conditions, items can be added to bring the design into the theorem coverage.

## Comparison with Allman et al. (2009)

Allman et al. gave a generic identifiability result for a Bernoulli mixture containing \(2^K\) latent classes, in which a quantitative sufficient condition is

\[
J\ge 2K+1.
\]

Xu's C1 and C2 also contain \(J\ge2K+1\), but the conclusions and conditional properties of the two sets of theories are different:

|aspects| Allman et al. | Xu |
| --- | --- | --- |
|model|General latent class model| Q-restricted latent class model |
|Conclusion|generic, usually allows label swapping|strict, attribute labels fixed|
|Conditions|Rank/number of categories conditions after blocking|Q unit block and probability distinction|
|technology|Kruskal three-way tensor decomposition|Margin \(T\)-Matrix Transformation|

The item quantity condition cannot replace the Q structure condition, and the generic result cannot automatically cover all points in the constrained parameter space.

## The level guaranteed by the theorem

\[
\text{C1+C2}
\Longrightarrow
\text{The parameters in the population distribution are unique}
\Longrightarrow
\text{Support for consistent estimation under additional regularization conditions}.
\]

It is not given directly:

- \(N\) required for a limited sample;
- Parameter estimation error bound;
-Attribute classification accuracy;
- The lowest numerical threshold for item discrimination;
- Robustness when Q is misspecified;
- The shortest available test length;
- CAT next question selection rules.

## A safe design with K = 2

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&0\\
0&1\\
1&0\\
0&1
\end{pmatrix}
=
\begin{pmatrix}
I_2\\I_2\\I_2
\end{pmatrix}.
\]

The first four questions satisfy C1, and the last two questions are guaranteed by Equation (2.3) respectively.

\[
\theta_{5,(1,0)}>\theta_{5,(0,0)},
\qquad
\theta_{6,(0,1)}>\theta_{6,(0,0)}.
\]

So C2 holds and the main theorem applies.

If only the first four questions are retained, C1 is still true, and C2 has no remaining questions to provide distinction; Proposition 2 illustrates that such designs may indeed be unrecognizable.
