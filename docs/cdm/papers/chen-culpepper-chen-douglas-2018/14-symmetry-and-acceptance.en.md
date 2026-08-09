# Theorem 2: Symmetry and Acceptance Rate

## Symmetry conclusion

Order

\[
T(x,y)
\]

Represents the probability that DS2 proposes from state \(x\) to \(y\). Theorem 2 Proof

\[
T(Q^\star,Q^{(t)})
=
T(Q^{(t)},Q^\star).
\]

## Visual proof of \(B=1\)

DS2 will pin a location if it falls into one of the following three categories:

1. 1 in the unit row;
2. A 1 in a column whose sum is exactly 3;
3. When there are only two unit rows, the unit row is 0 on the target column.

These locations will not produce \(Q^\star\ne Q^{(t)}\).

The remaining legal positions can be 0 or 1, and the selection probabilities in both directions are

\[
\frac12.
\]

## Path probability of \(B>1\)

Given a specific proposed path \(p_i\), the probability consists of three parts:

\[
\frac{1}{K\binom JB}
\times
\frac{1}{
\prod_{i\ne k}
\binom{b_i}{2-l_i}^{I(l_i<2)}
}
\times
\frac{1}{M_B}.
\]

The three items correspond in turn:

1. Select the item subset with column \(k\) and size \(B\);
2. Select fixed 0 among the \(b_i\) positions that need to be protected;
3. Extract evenly from \(M_B\) legal free configurations.

For fixed blocks, \(k_1,l_i,b_i,k_0,m\) is consistent in forward and reverse directions. Each path from \(Q^{(t)}\) to \(Q^\star\) can be paired with a reverse path that selects the same block and guard position with equal probability. The transfer symmetry is obtained by summing over all paths.

## MH acceptance probability

The general MH acceptance rate is

\[
r
=
\min\left\{
1,
\frac{
p(Q^\star\mid-)
T(Q^\star,Q^{(t-1)})
}{
p(Q^{(t-1)}\mid-)
T(Q^{(t-1)},Q^\star)
}
\right\}.
\]

By symmetry, the proposed ratio cancels:

\[
r
=
\min\left\{
1,
\frac{
p(Q^\star\mid
\boldsymbol Y,\boldsymbol\alpha,\boldsymbol s,\boldsymbol g)
}{
p(Q^{(t-1)}\mid
\boldsymbol Y,\boldsymbol\alpha,\boldsymbol s,\boldsymbol g)
}
\right\}.
\]

Then use the uniform Q prior in the legal space:

\[
r
=
\min\left\{
1,
\frac{
p(\boldsymbol Y\mid
\boldsymbol\alpha,\boldsymbol s,\boldsymbol g,Q^\star)
}{
p(\boldsymbol Y\mid
\boldsymbol\alpha,\boldsymbol s,\boldsymbol g,Q^{(t-1)})
}
\right\}.
\]

## Accept steps

pump

\[
U\sim\operatorname{Uniform}(0,1).
\]

If \(U\le r\), set \(Q^{(t)}=Q^\star\); otherwise, keep \(Q^{(t-1)}\).

## Importance of symmetry

The number of legal configurations of DS2 depends on the current matrix bounds. The paper's path-pairing proof shows that these dependencies cancel out exactly in the forward and reverse directions. In the absence of this proof, directly omitting the proposal ratio may lead the chain to an incorrectly stationary distribution.

[Next page: Metropolis-within-Gibbs complete algorithm](15-metropolis-within-gibbs.md)
