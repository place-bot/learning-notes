# Restricted Gibbs complete algorithm

## Get element-wise updates from \(B=1\)

Theorem 1 shows that DS2's single element movement is sufficient to connect \(\mathcal Q\). Based on this, the author rewrites the Q update as Gibbs sampling of \(q_{jk}\) one by one.

Each round is updated according to the complete conditional distribution mentioned above.

\[
\boldsymbol s,\quad
\boldsymbol g,\quad
\boldsymbol\alpha,\quad
\boldsymbol\pi.
\]

Then traverse in a fixed order

\[
j=1,\ldots,J,
\qquad
k=1,\ldots,K.
\]

## Three types of positions that cannot be flipped

If the current \(q_{jk}\) belongs to one of the following situations, the original value will be maintained.

### Case 1: 1 in the unit row

If

\[
\boldsymbol q_j=\boldsymbol e_k,
\]

Changing \(q_{jk}=1\) to 0 will produce an all-zero row.

### Case 2: 1 when the column sum is 3

If

\[
\sum_jq_{jk}=3
\]

And the current position is 1. Deleting it will leave only two questions for this attribute.

### Scenario 3: Key 0 when there are only two unit rows

If \(\boldsymbol q_j=\boldsymbol e_i\), \(i\ne k\), and only two rows in current Q are equal to \(\boldsymbol e_i\), changing \(q_{jk}=0\) to 1 will destroy the second set of unit matrix requirements.

## Flip position

If both 0 and 1 can maintain \(Q\in\mathcal Q\), press

\[
P(q_{jk}=x\mid-)
\propto
p(\boldsymbol Y\mid
\boldsymbol s,\boldsymbol g,\boldsymbol\alpha,
Q_{jk\leftarrow x}),
\qquad x\in\{0,1\}
\]

Sampling.

## Sequential update

When updating \(q_{jk}\):

- Elements that have been traversed use the new value of this round;
- Elements that have not yet been traversed use the previous round value.

The original text uses \(Q_{\text{new}}^{(t)}\) and \(Q_{\text{old}}^{(t-1)}\) to express this type of systematic-scan Gibbs.

## Pseudocode

```text
draw s, g, alpha, pi
for j in 1, ..., J:
    for k in 1, ..., K:
        make Q_flip by changing q[j,k]
        if Q_flip violates identification:
            keep q[j,k]
        else:
            compute conditional probabilities for 0 and 1
            sample q[j,k]
```

## Difference from MH

|aspects| MH + DS2 |Restricted Gibbs|
| --- | --- | --- |
|A Q move|\(B\) positions in a column|a location|
|candidate|Extract in legal block configuration|0/1 two values|
|accept/reject|Yes|Conditional sampling itself completes the update|
|Paper setting| \(B=2K\) |Element-by-element scan of \(B=1\)|
|simulated performance|\(K=3\) Very good|\(K=4\) is significantly more stable|

## Why element-by-element mixing may also be slow

If two high posterior Q's differ by multiple elements that are consistent with each other, the likelihood of the intermediate single-element state may be low. Constrained Gibbs must pass through these intermediate states block by block. MH's block moves have a chance to cross directly.

In Table 1 of the paper, the recovery rate of restricted Gibbs decreases under certain conditions of \(N=4000\), which also suggests that the mixing and posterior concentration under fixed chain length may interact.

[Next page: Derivation of conditional probability for a single q](17-q-full-conditional.md)
