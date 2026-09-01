# Parameter interpretation and identifiability

## Marginal IRFs

Item parameters retain their ordinary IRT meaning only when the joint model reproduces the intended
marginal IRFs. In the prerequisite Theta-SLM,

\[
P(X_1=1\mid\theta)
=\eta_1+(1-\beta_1-\eta_1)\pi(K_1=1\mid\theta),
\tag{40}
\]

which is a standard 4PL if the mastery probability is 2PL. For item 2,

\[
P(X_2=1\mid\theta)
=\eta_2+(1-\beta_2-\eta_2)
\pi(K_1=1\mid\theta)\pi(K_2=1\mid\theta).
\tag{41}
\]

Its difficulty is conditional: it is the ability location at which half of those who have reached the
previous state master the next item. In LKS, a difficulty marks equality of adjacent state weights, as in
a partial-credit step rather than an independent binary item.

For the equally informative structure, both margins use

\[
\frac{e^{2(\theta-\bar b_{12})}}{1+e^{2(\theta-\bar b_{12})}},
\]

so the pair acts as a virtual item with average difficulty and doubled discrimination, while each item
may retain its own guessing and slipping rates.

## Left-side-added parameters

\[
P(X_i=1\mid\theta)
=\eta_i+(1-\eta_i-\beta_i)\pi_i(\theta).
\]

The parameters \(\eta_i,\beta_i\) are “left-side-added” because they belong to the observation layer
\(K\to X\), not to the mastery layer \(\theta\to K\).

## Dimension counts

A \(2\times2\) table has only three independent probabilities, so it cannot identify eight item
parameters. With \(n\) items, a pairwise count gives

\[
\frac{3n(n-1)}2\ge4n,
\]

whose smallest solution is \(n=4\). A full-pattern count gives

\[
2^n-1\ge4n,
\]

whose smallest solution is \(n=5\).

These are only necessary dimension checks. They do not rule out label switching, parameter symmetries,
boundary degeneracy, or distinct structures with the same response distribution. General KST-IRT
identifiability remains open and should be studied through formal proofs and parameter-recovery
simulations.

