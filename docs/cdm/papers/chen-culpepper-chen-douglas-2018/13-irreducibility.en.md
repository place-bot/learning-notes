# Theorem 1: Irreducibility

## Theorem

When

\[
J-2K\ge2
\]

When , DS2 can reach any target \(Q^\star\in\mathcal Q\) from any current state \(Q^{(t)}\in\mathcal Q\) through finite steps under \(B=1\).

This shows that the Markov chain consisting of legal single-element updates is irreducible.

## Prove route

The proof is divided into two parts:

1. When the positions of the two sets of unit arrays are fixed, any \(\widetilde Q\) can become any \(\widetilde Q^\star\);
2. Any two rows can be exchanged, so the position of the unit matrix can also be moved.

## Part 1: Transformation \(\widetilde Q\)

Write the current status as

\[
Q^{(t)}
=
\begin{bmatrix}
I_K\\
I_K\\
\widetilde Q
\end{bmatrix}.
\]

Since \(\widetilde Q\) has at least two rows, you can select one of the rows, \(l\), and turn it into a full row element by element.

This line becomes temporary "insurance":

- Each column gets an extra 1;
- The remaining \(\widetilde Q\) rows can be changed element by element to the target configuration;
- Finally, change the insurance bank to the corresponding target bank of \(\widetilde Q^\star\).

Column sums, nonzero rows, and two unit row limits are maintained at each step.

## Part 2: Swap any two lines

Proof Consider three types of exchanges.

### Both lines are in \(\widetilde Q\)

The first part has shown that \(\widetilde Q\) can be changed into any legal configuration, so swapping is possible.

### One row is in the unit array area, and one row is in \(\widetilde Q\)

Let the unit array row be \(\boldsymbol e_k\). Another set of \(I_K\) also has a \(\boldsymbol e_k\) as an anchor point. Select another \(\widetilde Q\) row to temporarily change it to all 1s, copy and swap the target row element by element, and finally restore the temporary row.

### Both lines are in the unit array area

Use a \(\widetilde Q\) line for transfer:

1. Exchange the first line and the intermediary line;
2. Swap the second line with the current first line;
3. Swap the current second row and the transit row.

This is equivalent to completing the target swap with three legal swaps.

## Why is \(B>1\) also irreducible?

Single-element paths can be embedded in any larger block: select \(B\) positions containing the target element, leave the other positions as they are, and change only that one element. Therefore every reachable path to \(B=1\) is also a possible path to \(B>1\).

The entire column update of DS1 also includes single-element changes as a special case, so it is also irreducible.

## Boundary \(J-2K=1\)

At this time

\[
Q=P
\begin{bmatrix}
I_K\\
I_K\\
\boldsymbol1_K^{\mathsf T}
\end{bmatrix}.
\]

Legal Q only needs item row replacement. The authors recommend swapping two lines at a time to generate dependent samples.

## Where does the theorem guarantee?

Irreducibility ensures that there are no disconnected regions in the state space. It does not explain:

- The mixing speed of the chain is fast;
- 30,000 iterations is sufficient to cover the high posterior region;
- The mode is stable under limited samples;
- Accessing all important modes remains easy when using large \(K\).

These require empirical checks such as acceptance rate, diagnosis, multi-chain comparison and effective sample size.

## Accurate verification of this site

This site enumerates 230 labeled Q pictures that meet the restriction for \(K=2,J=6\), and uses "flip with a difference of one legal element" as the edge of the picture. A breadth-first search visits all 230 states, giving a small-scale instance check of the theorem.

[Next page: Theorem 2 - Symmetry and Acceptance Rate](14-symmetry-and-acceptance.md)
