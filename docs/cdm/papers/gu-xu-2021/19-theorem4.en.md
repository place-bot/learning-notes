# Theorem 4: D/E pan-recognition condition

## 1. Blocked form

After substitution, it is written as

\[
Q=
\begin{pmatrix}
Q_1\\
Q_2\\
Q^\star
\end{pmatrix},
\]

Among them, \(Q_1,Q_2\) is \(K\times K\).

## 2. Condition D

\(Q_1\) and \(Q_2\) do not overlap each other and are both complete.

Each block can match \(K\) attributes to \(K\) different questions.

## 3. Condition E

The remaining matrix \(Q^\star\) has at least one 1 in each column:

\[
\sum_{j\in Q^\star}q_{jk}\ge1,
\qquad k=1,\ldots,K.
\]

D and E together automatically guarantee that each attribute appears at least three times:

- once in a match of \(Q_1\);
- once in a match of \(Q_2\);
- at least once in \(Q^\star\).

## 4. Theorem 4

In general RLCM, if D and E hold, then

\[
(Q,\Theta,\boldsymbol p)
\]

Jointly identifiable.

## 5. Identifiable parameter subsets

Remark 3 Write the identifiable area as:

\[
\det T(Q_1,\Theta_{Q_1})\ne0,
\]

\[
\det T(Q_2,\Theta_{Q_2})\ne0,
\]

and

\[
T(Q^\star,\Theta_{Q^\star})
\operatorname{Diag}(\boldsymbol p)
\]

The column vectors of are pairwise different.

These determinants, or parameter sets with zero column difference, are defined by polynomial equations and have zero measure in the complete parameter space.

## 6. The role of three pieces of information

```text
Q1: The first set of latent class coordinates
Q2: The second set of independent coordinates
Q*: distinguish and mark latent class columns
          │
          ▼
Recover the structure of Θ, p, and Q constrained by Q
```

Two blocks of universally complete matrices make the corresponding T sub-matrices have full rank at general parameter points. The third block eliminates latent class column pairing ambiguity through different column codes.

## 7. Difference from known Q result

The same D/E structure has also been used for general RLCM parameter pan-identification when Q is known. Unknown Q adds the alternative structure \(\bar Q\), so Condition C becomes necessary again.

In scenarios where Q is known, sometimes only two questions are needed for a certain attribute; this article Theorem 3 explains that this relaxation fails when Q is unknown.

## 8. Number of questions required

D/E requires at least

\[
J\ge2K+1.
\]

Therefore, the general sufficient design of RLCM for pan-recognition is still close to the three-block structure. DINA's two-parameter constraint can further reduce the number of strict identification questions to

\[
K+\lceil\log_2K\rceil+1.
\]
