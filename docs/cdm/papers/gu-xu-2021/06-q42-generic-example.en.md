# Example of general recognition of four questions and two attributes

## 1. Q matrix

For papers

\[
Q_{4\times2}
=
\begin{pmatrix}
1&0\\
0&1\\
1&0\\
0&1
\end{pmatrix}
\]

Explain the difference between strict identification and general identification. Each attribute was measured by two single-attribute questions.

This Q violates Condition C because there are only two 1's in each column, so strict identification fails.

## 2. Determine the proportion constraints for general recognition

latent class ratio writing

\[
\boldsymbol p=(p_{00},p_{01},p_{10},p_{11}).
\]

When

\[
p_{01}p_{10}\ne p_{00}p_{11}
\]

When , the model parameters can be identified; when

\[
p_{01}p_{10}=p_{00}p_{11}
\]

When , there are infinite sets of parameters that produce the same reaction distribution.

The latter equation only defines an algebraic surface in the parameter space, and the Lebesgue measure is 0, so the DINA model corresponding to this Q is universally identifiable.

## 3. Equivalence relationship with attribute independence

Arrange the latent class proportions into the \(2\times2\) table:

\[
P=
\begin{pmatrix}
p_{00}&p_{01}\\
p_{10}&p_{11}
\end{pmatrix}.
\]

Two binary attributes are independent if and only if the table rank is 1, that is

\[
\det(P)
=p_{00}p_{11}-p_{01}p_{10}=0.
\]

Therefore, the general recognition condition is equivalent to the existence of overall dependence between two attributes.

An interesting mechanism appears here: when there are only two questions for each attribute, the dependency between attributes can provide additional connection information; when the attributes happen to be independent, this information disappears.

## 4. Scenario (a): Points on the zero measurement set

Thesis design

\[
s_j=g_j=0.2,\qquad
p_{00}=p_{01}=p_{10}=p_{11}=0.25.
\]

The uniform latent class ratio satisfies

\[
p_{01}p_{10}=p_{00}p_{11}=0.0625.
\]

The author constructs three sets of DINA parameters with obvious differences and verifies that they are effective for all

\[
2^4=16
\]

response patterns give exactly the same probability.

## 5. Scenario (b): Random parameters

Randomly generate 100 sets of true parameters:

\[
s_j,g_j\sim U(0.1,0.3),
\qquad
\boldsymbol p\sim\operatorname{Dirichlet}(3,3,3,3).
\]

Sampling from a continuous distribution will rarely fall exactly on a surface with determinant 0. The author is at

\[
N=10^2,10^3,10^4,10^5
\]

Simulate and run EM with 10 random initial values, retaining the maximum likelihood solution. As \(N\) increases, the MSE of \(\boldsymbol p,\boldsymbol s,\boldsymbol g\) approaches 0.

## 6. It is still difficult to get close to the zero test set

The paper marks the largest 20% parameter points of \(\boldsymbol p\) MSE in red when \(N=10^5\). The red dots are concentrated in

\[
p_{00}p_{11}\approx p_{01}p_{10}
\]

near the straight line.

This means that "measure 0" only describes the size of the exact missing recognition point. Neighboring areas will still form weak recognitions, and limited sample errors may be large.

## 7. A typesetting point in the original text

When the main text explains Figure 3, one text writes the vertical axis product as \(p_{01}p_{01}\). Combining the before and after formulas, the diagonal line in the figure and the independence condition, the vertical axis corresponds to \(p_{01}p_{10}\).
