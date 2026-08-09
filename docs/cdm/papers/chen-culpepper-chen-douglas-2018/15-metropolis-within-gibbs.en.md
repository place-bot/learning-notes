# Metropolis-within-Gibbs complete algorithm

## Initialization

Random initialization:

\[
\boldsymbol\alpha^{(0)},\quad
\boldsymbol\pi^{(0)},\quad
Q^{(0)}\in\mathcal Q,\quad
\boldsymbol g^{(0)},\quad
\boldsymbol s^{(0)}.
\]

item parameters need to meet

\[
0\le g_j^{(0)}<1-s_j^{(0)}\le1.
\]

The original code `random_Q(J,K)` first puts in two sets of \(I_K\), constructs non-zero remaining rows and columns, and then randomly shuffles the rows.

## One iteration

### Step A: Update guess rate

\[
\boldsymbol g^{(t)}
\sim
p(\boldsymbol g\mid
\boldsymbol Y,\boldsymbol s^{(t-1)},
\boldsymbol\alpha^{(t-1)},Q^{(t-1)}).
\]

Question by question using a truncated beta conditional distribution.

### Step B: Update error rate

\[
\boldsymbol s^{(t)}
\sim
p(\boldsymbol s\mid
\boldsymbol Y,\boldsymbol g^{(t)},
\boldsymbol\alpha^{(t-1)},Q^{(t-1)}).
\]

### Step C: Update student attributes

\[
\boldsymbol\alpha_i^{(t)}
\sim
\operatorname{Categorical}
\left(
\frac{w_{i1}}{\sum_cw_{ic}},\ldots,
\frac{w_{iC}}{\sum_cw_{ic}}
\right).
\]

### Step D: Update latent class proportions

\[
\boldsymbol\pi^{(t)}
\sim
\operatorname{Dirichlet}
(\boldsymbol\delta_0+\boldsymbol n^{(t)}).
\]

### Step E: Update Q

1. Use DS2 to generate \(Q^\star\in\mathcal Q\);
2. Calculate the conditional likelihood ratio;
3. Accept or reject according to MH rules.

## Pseudocode

```text
initialize alpha, pi, s, g, Q in identified space
for t = 1, ..., T:
    draw g from its truncated-Beta conditionals
    draw s from its truncated-Beta conditionals
    draw every alpha_i from 2^K class probabilities
    draw pi from its Dirichlet conditional
    choose one Q column and B item positions
    construct an identified DS2 proposal Q*
    accept Q* with min(1, likelihood(Q*) / likelihood(Q))
    after burn-in, save Q, s, g, pi, alpha
```

## Paper experimental settings

The MH method uses:

\[
B=2K,
\qquad
T=30{,}000,
\qquad
\text{burn-in}=15{,}000.
\]

The DS2 acceptance rate in preliminary experiments was between 18% and 25%.

## Main calculations for each round

A rough look:

- Property update requires \(O(NJ2^K)\);
- Item parameters update requires \(O(NJ)\);
- Candidate constructions of Q require inspection of local structures;
- MH ratio calculated for \(N\times B\) affected responses.

\(2^K\) in attribute updates is one of the main obstacles to attribute number expansion.

## Supplement the implementation sequence in the code

The actual sequence of exposing `DINA_MH_Q()` is:

1. `update_alpha()` updates \(\boldsymbol\alpha,\boldsymbol\pi\) at the same time;
2. `update_sg()` updates \(\boldsymbol s,\boldsymbol g\);
3. `updateQ_MH()` raised and updated Q.

Different Gibbs block orders can still use the same joint posterior as a stationary distribution, as long as the corresponding conditional distribution is used at each step.

[Next page: Restricted Gibbs complete algorithm](16-constrained-gibbs.md)
