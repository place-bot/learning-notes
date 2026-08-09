# Theorem 5 and \(K=2\) necessary and sufficient conditions

## 1. Theorem 5

Generally, RLCM joint pan recognition requires Q pan to be complete:

\[
\text{Joint pan-recognition}
\Longrightarrow
\text{Q pan-complete}.
\]

This gives the necessity of the first block of universally complete structures in Condition D.

## 2. Prove intuition

If Q is not universally complete, according to the Hall condition, there exists a subset of attributes \(S\) that are connected to less than \(|S|\) questions.

These questions cannot provide independent observation directions for each attribute in \(S\). The parameter freedom of general RLCM allows changing the item parameters and latent class proportions under Q constraints along some continuous direction while keeping the complete response distribution unchanged.

Therefore, the unrecognizable set has positive dimensions and universal recognition fails.

## 3. Proposition 3

When \(K=2\), D/E constitutes a necessary and sufficient condition for the joint pan-recognition of general RLCM.

\[
D+E
\quad\Longleftrightarrow\quad
\text{Joint pan-recognition}.
\]

This is more complete than the normal \(K\) result.

## 4. Counting counterexamples

If \(K=2\), Condition C is established but D/E fails, the structure can be classified into two categories.

The first category only has \(J=3\) all-attribute questions:

\[
Q_1=
\begin{pmatrix}
1&1\\
1&1\\
1&1
\end{pmatrix}.
\]

The observed distribution is given at most

\[
2^J=8
\]

There are response probability constraints, and the relevant free parameters reach 16.

The second category has \(J=4\), and the candidate substitution matrix can be all ones:

\[
\bar Q_2=
\begin{pmatrix}
1&1\\
1&1\\
1&1\\
1&1
\end{pmatrix}.
\]

At this time, the number of constraints is

\[
2^J=16,
\]

The number of free parameters of the candidate model is 20.

The dimensions of the unknowns are greater than the number of equations, and there are infinitely many alternative solutions.

## 5. General open part of \(K\)

Thesis proves:

- C necessary;
- Pan-complete and necessary;
- D/E sufficient;
- D/E required for \(K=2\).

When \(K>2\), whether D/E can be further relaxed, the main article does not give a complete and necessary description.

## 6. Practical explanation

Pan-completeness only guarantees "the matching of a set of attributes to different questions." Theorem 4 also requires a second set of matches and additional coverage. \(K=2\) The proof shows that the three parts are very close to the structural bottom line; there may still be more sophisticated combination designs in high-dimensional scenarios.
