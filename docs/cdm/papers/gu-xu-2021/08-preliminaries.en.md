# Zero rows, monotonicity and equivalence

## 1. Why is monotonicity needed?

General RLCM assumptions

\[
\theta_{j,\boldsymbol\alpha}>
\theta_{j,\boldsymbol\alpha'}
\]

As long as the former masters all the required attributes and the latter lacks at least one required attribute.

If this restriction is removed, any

\[
Q\ne \boldsymbol 1_{J\times K}
\]

It's possible to use the same set of \(\Theta,\boldsymbol p\) as an all-1 matrix and produce the same distribution. At this time, the restriction of parameter space by \(Q\) loses its observable meaning.

Monotonicity allows "mastering item requirements" to leave a directional difference in probability.

## 2. All-zero q-vector

If a certain topic

\[
\boldsymbol q_j=\boldsymbol0,
\]

This question does not require any attributes. Its success probability does not vary with the latent class, so it cannot provide information that distinguishes the attribute structure.

Proposition 1 Assume

\[
Q=
\begin{pmatrix}
Q^0\\
0
\end{pmatrix},
\]

Among them, \(Q^0\) collects all non-zero rows. rule

\[
(Q,\Theta,\boldsymbol p)
\]

Strictly or broadly identifiable if and only if

\[
(Q^0,\Theta^0,\boldsymbol p)
\]

Have the same identification properties.

Therefore, subsequent theories can first delete all zero rows.

## 3. All-zero column

If column \(k\) is all 0, attribute \(k\) has never been measured by any question. Latent classes different from \(\alpha_k\) cannot be distinguished by responses, and identification fails immediately.

All-zero rows and all-zero columns have different meanings:

|structure|meaning|Process|
| --- | --- | --- |
|All zero lines|One question does not measure any attributes|This question can be deleted without changing the recognition of other structures.|
|all-zero column|A property has never been measured|The attribute and related latent class ratio cannot be identified|

## 4. Column replacement equivalent

For any \(K\times K\) permutation matrix \(P\),

\[
\bar Q=QP
\]

Just rearrange the attribute labels. Latent class ratio synchronization press

\[
\bar{\boldsymbol\alpha}=P^\top\boldsymbol\alpha
\]

After relabeling, the reaction distribution remains unchanged.

Therefore, the uniqueness conclusions of the paper are all based on column permutation equivalence classes.

## 5. Structure cleaning before recognition

To check a candidate Q in practice, you can first do:

1. The verification element only contains 0/1;
2. Mark and remove all-zero rows;
3. Check the all-zero column;
4. Record column duplication and column replacement;
5. Apply the A/B/C or D/E conditions again.

The official `check_conditions` code directly assumes that the input is a legal binary matrix, and does not uniformly perform these five steps of input verification. The site checker verifies matrix shapes and binary values ​​at entry.
