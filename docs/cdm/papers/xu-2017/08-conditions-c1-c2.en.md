# C1, C2 and three sets of unit arrays

## Condition C1

After changing the order of items,

\[
Q=
\begin{pmatrix}
I_K\\
I_K\\
Q'
\end{pmatrix}.
\tag{C1}
\]

The first question \(K\) and questions \(K+1\) to \(2K\) each form a complete unit block. C1 ensures that each attribute is measured by at least two single-attribute questions.

## Condition C2

For each \(k=1,\ldots,K\), the two probability vectors on the remaining items are required to be different:

\[
\left(
\theta_{j,\boldsymbol e_k}:j>2K
\right)^\top
\ne
\left(
\theta_{j,\boldsymbol 0}:j>2K
\right)^\top.
\tag{C2}
\]

Equivalent statement: for each attribute \(k\), there is at least one question in \(Q'\) that satisfies

\[
\theta_{j,\boldsymbol e_k}
\ne
\theta_{j,\boldsymbol 0}.
\]

C2 is a condition about the actual response probability, which is not completely determined by the general Q structure.

## The exact role of C2 in the proof

Define two vectors

\[
\boldsymbol a_k
=
\left(
1,\theta_{2K+1,\boldsymbol e_k},
\ldots,\theta_{J,\boldsymbol e_k}
\right)^\top,
\]

\[
\boldsymbol a_0
=
\left(
1,\theta_{2K+1,\boldsymbol 0},
\ldots,\theta_{J,\boldsymbol 0}
\right)^\top.
\]

The first element of both is 1. C2 states \(\boldsymbol a_k\ne\boldsymbol a_0\), so they cannot be proportional. Linear algebra guarantees that there exists a row vector \(\boldsymbol u_k\) such that

\[
\boldsymbol u_k\boldsymbol a_0=0,
\qquad
\boldsymbol u_k\boldsymbol a_k=b_k\ne0.
\]

This \(\boldsymbol u_k\) eliminates zero attribute columns and retains single attribute columns in proof step 3, thereby identifying item parameters in two unit blocks.

## A stronger condition that is easier to enforce

If all remaining questions satisfy the strict minimum of zero attribute class:

\[
\theta_{j,\boldsymbol 0}
<
\min_{\boldsymbol\alpha\ne\boldsymbol 0}
\theta_{j,\boldsymbol\alpha},
\qquad j>2K,
\]

As long as \(Q'\) is not empty, C2 is automatically established.

This is stronger than C2, which only requires that each \(\boldsymbol e_k\) differs from \(\boldsymbol 0\) on at least one remaining question.

## Three sets of unit blocks

If

\[
Q=
\begin{pmatrix}
I_K\\
I_K\\
I_K\\
\widetilde Q
\end{pmatrix},
\]

Then the third \(I_K\) is located at \(Q'\). For its \(k\) single attribute question, equation (2.3) gives

\[
\theta_{j,\boldsymbol e_k}
>
\theta_{j,\boldsymbol 0}.
\]

Therefore, both C1 and C2 are satisfied. This results in a sufficient design that can be executed with the Q structure alone:

> Each attribute is configured with at least three questions that only measure that attribute.

## Three common misunderstandings

### C1 and C2 are sufficient conditions

The main theorem proves that they can be identified if they are satisfied. In general, some designs in RLCM that do not satisfy this structure may also be identifiable, and the paper does not give a complete necessary and sufficient description.

### C2 does not equal "at least three 1's per column"

In the general model, the Q line of a certain question contains the attribute \(k\), which is not automatically guaranteed.
\(\theta_{j,\boldsymbol e_k}\ne\theta_{j,\boldsymbol 0}\). If the question also requires other attributes, \(\boldsymbol e_k\) may still be in the insufficient ability category; whether the two probabilities are different depends on the model.

### J ≥ 2K + 1 is just the lower bound of quantity

C1 and C2 imply that \(Q'\) is not empty, thus

\[
J\ge2K+1.
\]

The number of items reaching this lower bound does not mean that the row structure and probability distinction conditions have been met.

## Design Checklist

1. Can the first \(I_K\) be found in Q?
2. Can another \(I_K\) be found after deletion?
3. For each \(k\), \(Q'\), is there a question that can distinguish \(\boldsymbol e_k\) from \(\boldsymbol 0\)?
4. If you want to do only structural review, can you directly add the third \(I_K\)?
5. Does the attribute hierarchy cause some \(\boldsymbol e_k\) to not be in the allowed potential class space at all?

Term 5 goes beyond the proportional model of the original theorem and requires the use of subsequent hierarchical or partial-identifiability theories.
