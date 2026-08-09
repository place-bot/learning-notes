# Propositions 6.3--6.6: Column space separation

## Target proposition

The author wishes to establish:

\[
Q'\not\sim Q
\quad\Longrightarrow\quad
T_c(Q)\boldsymbol p^*
\notin
\mathcal C(T_{c'}(Q'))
\]

True for all candidates \(\boldsymbol c'\).

It's stronger than "some fixed \(\boldsymbol c'\) fit failed" because error Q cannot replicate the true moments even by adjusting the row scaling parameters.

## First fix the anchor question of true Q

For completeness and without loss of generality, it can be assumed that

\[
Q_{1:k}=I_k.
\]

For error candidate \(Q'\), there are only two situations in the first \(k\) row:

1. \(Q'_{1:k}\) complete;
2. \(Q'_{1:k}\) is incomplete.

These two categories exhaust all candidates.

## Proposition 6.3: The candidate anchor block is complete

If \(Q'_{1:k}\) is complete, the candidate attribute columns can be rearranged so that

\[
Q'_{1:k}=I_k=Q_{1:k}.
\]

If \(Q'\ne Q\), the difference must appear in a subsequent question. The paper proves that under the conditions of Theorem 4.2, for any \(\boldsymbol c'\in\mathbb R^m\),

\[
T_c(Q)\boldsymbol p^*
\notin
\mathcal C(T_{c'}(Q')).
\]

Intuitively, candidate Q will mistakenly regard the attribute requirements of a certain follow-up question as the same as a certain anchor question combination. The corresponding two rows in the candidate \(T\)-matrix have a fixed ratio; in the true model, the two rows do not reach this ratio due to the presence of differentiated populations guaranteed by C4.

## Proposition 6.4: Candidate anchor block is incomplete

If \(Q'_{1:k}\) is incomplete, then:

- Two candidate anchor questions have the same q-vector;
- A certain candidate anchor question requires multiple attributes at the same time;
- An overlay relationship is formed between several multi-attribute rows.

The appendix proves, class by class, that it is always possible to find a pair or group of three rows such that the column space of error candidates must satisfy some fixed scaling relation that the true moments violate for a fully diverse population.

The conclusion is also

\[
T_c(Q)\boldsymbol p^*
\notin
\mathcal C(T_{c'}(Q')).
\]

## Corollary 6.5

Propositions 6.3 and 6.4 merge to cover all \(Q'\not\sim Q\). The original text is written:

\[
T_c(Q)\boldsymbol p^*
\notin
\mathcal C(T_{c'}(Q'))
\]

True for all candidates \(\boldsymbol c'\in[0,1]^m\).

Noise free conditions order

\[
\boldsymbol c=\boldsymbol1,
\qquad
\boldsymbol g=\boldsymbol0
\]

This conclusion can be used.

## Proposition 6.6: Add guesswork

Define the complete mode distribution

\[
\boldsymbol p_0^*
=
\begin{pmatrix}
p_{\boldsymbol0}^*\\
\boldsymbol p^*
\end{pmatrix}
\]

and augmented matrix

\[
\widetilde T_{c,g}(Q)
=
\begin{pmatrix}
\boldsymbol g_{\mathrm{joint}}&T_{c,g}(Q)\\
1&\boldsymbol E
\end{pmatrix}.
\]

If Q is complete, T is saturated, \(Q'\not\sim Q\), each \(c_i\ne g_i\), and the remaining conditions of Theorem 4.2 are met, then for all \(\boldsymbol c'\in[0,1]^m\),

\[
\widetilde T_{c,g}(Q)\boldsymbol p_0^*
\notin
\mathcal C\!\left(
\widetilde T_{c',g}(Q')
\right).
\]

In addition,

\[
\widetilde T_{c,g}(Q)
\]

Full rank.

## Why "any \(c'\)" is important

In the estimation of unknown \(\boldsymbol c\), each error candidate Q will choose the one that is most beneficial to itself

\[
\widehat{\boldsymbol c}(Q',\boldsymbol g).
\]

If separation holds only for true \(\boldsymbol c\), false Q may eliminate the distance by changing \(\boldsymbol c'\). Proposition 6.6 excludes the entire set of tight parameters \([0,1]^m\).

## Exclude from set to positive distance

\(\mathcal C(\widetilde T)\) is a closed linear subspace. True moments do not belong to it, so for the fixed errors \(Q'\) and \(\boldsymbol c'\), the distance is strictly positive.

Reuse:

- \(\boldsymbol c'\mapsto\widetilde T_{c',g}(Q')\) continuous;
- \([0,1]^m\) tight;
- The number of candidate Qs is limited;

A uniform positive separation interval for all error candidates can be obtained. This step converts the linear algebra identification conclusion into statistical consistency.

[Next page: The matrix that eliminates the guesswork \(D\)](18-guessing-removal-transform.md)
