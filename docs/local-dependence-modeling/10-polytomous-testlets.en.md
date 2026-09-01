# Polytomous items, testlets, and knowledge structures

## A polytomous item as a binary chain

For \(R\in\{0,1,\ldots,m\}\), define cumulative indicators

\[
X_j=I(R\ge j).
\]

Then

\[
R=r
\Longleftrightarrow
(X_1,\ldots,X_m)
=(\underbrace{1,\ldots,1}_{r},\underbrace{0,\ldots,0}_{m-r})
\Longleftrightarrow K_r=\{q_1,\ldots,q_r\}.
\]

Thus a cumulative polytomous item is formally equivalent to dependent binary elements on a chain.
Patterns such as \(01\) are structurally impossible because crossing a higher threshold entails crossing
the lower one.

LKS on a chain is the partial credit model. An arbitrary knowledge structure is more general: two
different branch states can have the same sum score but different mastery meanings, which PCM merges.

## Testlets

A testlet is a group of items linked by a common stimulus, sequence, content, or response procedure.

- A **linear testlet** can retain a power-set structure when every pattern remains possible.
- A **fully hierarchical testlet** can be represented by a chain when each stopping outcome uniquely
  identifies a state and all other responses are inferred without error.
- A **partially hierarchical testlet** has items appearing on multiple administration paths. Outcomes no
  longer identify full patterns, and a \(g\)-process is needed for patterns outside the chain.

The assumption of no \(g\)-process in the ideal fully hierarchical example is not a requirement that
chains be noiseless. Guessing, slipping, or routing errors can be added whenever substantively needed.

## Hamming distance and error neighborhoods

\[
d_H(x,y)=\sum_iI(x_i\ne y_i).
\]

Restricting a \(g\)-matrix to Hamming distance one means at most one item differs between a latent
state and an observed pattern. Allowing distance two or more permits multiple errors. Distance is a
compact modeling device, but item content must determine whether equally distant errors are equally
plausible.

The tree in the paper's Figure 2 is an administration flowchart, not itself a knowledge structure. One
describes routing; the other describes allowable latent mastery sets.

Because well-separated PCM step difficulties do not rule out probabilistic or deterministic LD, fitting
only the testlet sum score cannot identify the item-level mechanism. KST-IRT retains response patterns,
branches, and explicit error processes.

