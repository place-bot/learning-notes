# Conditional posterior and uniform prior of Q

## Conditional Posterior

Given the current student attributes, error rate and guessing rate,

\[
p(Q\mid
\boldsymbol Y,\boldsymbol\alpha,\boldsymbol s,\boldsymbol g)
\propto
p(\boldsymbol Y\mid
\boldsymbol\alpha,\boldsymbol s,\boldsymbol g,Q)
I(Q\in\mathcal Q).
\]

Since \(\mathcal Q\) is limited, the prior can be written more clearly:

\[
p(Q)
=
\begin{cases}
1/|\mathcal Q|,&Q\in\mathcal Q,\\
0,&Q\notin\mathcal Q.
\end{cases}
\]

## Posterior ratio between legitimate candidates

If \(Q,Q^\star\in\mathcal Q\), then

\[
\frac{p(Q^\star\mid-)}{p(Q\mid-)}
=
\frac{
p(\boldsymbol Y\mid
\boldsymbol\alpha,\boldsymbol s,\boldsymbol g,Q^\star)
}{
p(\boldsymbol Y\mid
\boldsymbol\alpha,\boldsymbol s,\boldsymbol g,Q)
}.
\]

The a priori constants completely cancel.

## When only updating a subset of items

If the candidate only changes the q element in the item set \(\mathcal B\), the likelihood contributions of the other items cancel:

\[
\frac{p(Q^\star\mid-)}{p(Q\mid-)}
=
\prod_{i=1}^{N}
\prod_{j\in\mathcal B}
\frac{
p(Y_{ij}\mid
\boldsymbol\alpha_i,s_j,g_j,\boldsymbol q_j^\star)
}{
p(Y_{ij}\mid
\boldsymbol\alpha_i,s_j,g_j,\boldsymbol q_j)
}.
\]

The supplemental code `updateQ_MH()` calculates this ratio exactly for the selected row `index`.

## Logarithmic domain implementation

Raw C++ student-by-student cumulative probability ratio:

```cpp
ratio = ratio * pynext / pyold;
```

It is easy to underflow under larger \(N\) or \(J\). A robust implementation should compute

\[
\log r
=
\min\left\{
0,\
\ell(Q^\star)-\ell(Q)
\right\},
\]

Compare again

\[
\log U\le \log r.
\]

This is a numerical engineering suggestion put forward by the intensive reading of the code on this site. The formula of the paper itself allows this equivalent implementation.

## The meaning of uniform prior

Uniformity means uniformity over the entire labeled matrix. Different column permutations of Q represent attribute label exchanges and will produce the same observation model. The paper sorts the column codes in the aggregation stage to merge these states.

If each equivalence class contains the same number of column permutations, the corresponding classes will still have uniform weights after merging. The track size will change when there are duplicate columns; the two sets of unit matrices in this article make different attribute columns have their own unit row structures, and the columns themselves will not be exactly the same.

## What does posterior learning rely on?

The information for Q comes from the match between the current attribute sample and the answer. For example, after changing \(q_{jk}\) from 0 to 1, only students who meet other required attributes and lack the attribute \(k\) will change \(\eta_{ij}\). The correct and incorrect answer counts of these students determine the posterior tendency of the flip.

[Next page: Overview of three types of candidate generators](10-proposal-overview.md)
