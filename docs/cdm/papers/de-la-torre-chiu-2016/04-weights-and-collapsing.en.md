# Posterior weight, folded grouping and conditional mean

## Two quantities of complete mode

For each complete attribute profile \(\boldsymbol\alpha\), the algorithm requires:

1. Pattern weight

   \[
   w(\boldsymbol\alpha);
   \]

2. item success probability

   \[
   p_j(\boldsymbol\alpha)
   =
   P(Y_j=1\mid\boldsymbol\alpha).
   \]

weight satisfies

\[
\sum_{\boldsymbol\alpha}w(\boldsymbol\alpha)=1.
\]

## Get weights from student posterior

Let the posterior of student \(i\)’s attribute profile be

\[
w_i(\boldsymbol\alpha)
=
P(\boldsymbol\alpha_i=\boldsymbol\alpha
\mid\boldsymbol Y_i,\widehat\Theta,Q_0).
\]

The overall model weight is estimated to be

\[
\widehat w(\boldsymbol\alpha)
=
\frac{1}{N}\sum_{i=1}^{N}w_i(\boldsymbol\alpha).
\]

\(Q_0\) is the initial Q, and \(\widehat\Theta\) is the item and structure parameters under this Q.

## Complete mode success probability

For item \(j\):

\[
\widehat p_j(\boldsymbol\alpha)
=
\frac{
\sum_{i=1}^{N}
w_i(\boldsymbol\alpha)Y_{ij}
}{
\sum_{i=1}^{N}
w_i(\boldsymbol\alpha)
}.
\tag{2}
\]

The numerator is the posterior expected number of correct answers for the pattern \(\boldsymbol\alpha\), and the denominator is the posterior expected number of people. This formula is explicitly written out in the review of Liu (2017), and the current `GDINA` implementation also uses the same calculation.

## How to collapse categories of candidate q-vector

Assume that the candidate only retains the attribute \(K',\ldots,K''\), and the reduction model is written as

\[
\boldsymbol\alpha_{K':K''}.
\]

The same reduced pattern corresponds to multiple complete patterns. Weight after folding:

\[
w(\boldsymbol\alpha_{K':K''})
=
\sum_{\text{Omitted attributes}}
w(\boldsymbol\alpha_{1:K}).
\tag{3}
\]

Success probability after folding:

\[
p_j(\boldsymbol\alpha_{K':K''})
=
\frac{
\sum_{\text{Omitted attributes}}
w(\boldsymbol\alpha_{1:K})
p_j(\boldsymbol\alpha_{1:K})
}{
w(\boldsymbol\alpha_{K':K''})
}.
\tag{4}
\]

This is a posterior weighted conditional mean.

## How to write probability theory

Let \(Z=\boldsymbol\alpha_{K':K''}\), then

\[
p_j(Z)
=
E(Y_j\mid Z).
\]

Candidate verification actually compares the degree of information compression of different \(Z\) versus \(E(Y_j\mid\boldsymbol\alpha)\).

## A key risk

\(w_i(\boldsymbol\alpha)\) is obtained by fitting the initial \(Q_0\). If the error in the initial Q is enough to seriously distort the attribute classification, the weight of equation (2) will also be biased, and subsequent GDI will inherit this bias. The simulations cover only a small to moderate number of misconfigurations, and the applicability of the method is based on this practical premise.
