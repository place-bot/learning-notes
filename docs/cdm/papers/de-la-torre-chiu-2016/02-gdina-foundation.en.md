# G-DINA basic and reduced attribute profile

## item only reads the required attributes

The full attribute profile is written as

\[
\boldsymbol\alpha_l
=
(\alpha_{l1},\ldots,\alpha_{lK}),
\qquad
\alpha_{lk}\in\{0,1\}.
\]

The q-vector of item \(j\) is \(\boldsymbol q_j\). Number of attributes required:

\[
K_j^*
=
\sum_{k=1}^{K}q_{jk}.
\]

Delete all \(q_{jk}=0\) positions and get the item reduced attribute profile:

\[
\boldsymbol\alpha^*_{lj}.
\]

For example \(K=4\), \(\boldsymbol q_j=1011\). Full model \(1101\) The reduced model for this question is

\[
\boldsymbol\alpha^*_{lj}=101.
\]

Property 2 does not enter the reaction function of this question.

## identity-link saturated G-DINA

When the item requires \(K_j^*\) attributes, G-DINA sets aside parameters for all main effects and interaction effects:

\[
\begin{aligned}
P_j(\boldsymbol\alpha^*_{lj})
= {}&
\delta_{j0}
+\sum_{k=1}^{K_j^*}\delta_{jk}\alpha_{lk}\\
&+\sum_{k<k'}\delta_{jkk'}
\alpha_{lk}\alpha_{lk'}
+\cdots\\
&+\delta_{j12\cdots K_j^*}
\prod_{k=1}^{K_j^*}\alpha_{lk}.
\end{aligned}
\tag{1}
\]

Here:

- \(\delta_{j0}\): Baseline success probability of zero attribute group;
- \(\delta_{jk}\): main effect of attribute \(k\);
- \(\delta_{jkk'}\): dual attribute interaction;
- The highest order item: the additional effects produced by mastering all required attributes at the same time.

## Three attributes example

When \(K_j^*=3\):

\[
P_j(101)
=
\delta_{j0}
+\delta_{j1}
+\delta_{j3}
+\delta_{j13},
\]

\[
\begin{aligned}
P_j(111)
= {}&
\delta_{j0}
+\delta_{j1}
+\delta_{j2}
+\delta_{j3}\\
&+\delta_{j12}
+\delta_{j13}
+\delta_{j23}
+\delta_{j123}.
\end{aligned}
\]

A question has \(2^{K_j^*}\) reduction modes and the same number of saturation parameters. There is a one-to-one linear transformation between the probability vector and the effect parameter vector.

## Why the verification algorithm uses full mode

The initial Q only specifies local grouping for the item model. During Q verification, other candidate q-vectors need to be compared, so the algorithm retains all \(2^K\) complete attribute profiles:

\[
\{000\cdots0,\ldots,111\cdots1\}.
\]

Each candidate vector regroups the same set of complete patterns. In this way, candidates can be compared under the same posterior weight system.

## Interface with 2011 G-DINA paper

[de la Torre (2011) Topic](../de-la-torre-2011/index.md) explains:

- G-DINA’s design matrix;
- identity, logit and log link;
- MMLE/EM；
- Reduction models such as DINA, DINO, and A-CDM.

The 2016 paper uses this framework directly, turning the focus to the empirical verification of Q rows.
