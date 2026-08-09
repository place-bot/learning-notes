# Counterexamples, necessity and identification boundaries

## Counterexample 1: Everyone has all the attributes

Set

\[
\Pr(\boldsymbol A=\boldsymbol1)=1.
\]

Any Q is given when it is noise-free and requires at least one attribute per question

\[
\boldsymbol R=\boldsymbol1
\]

Probability 1. The response distribution is completely independent of Q.

Therefore, "all attribute profiles have positive probability" in C4 is not a purely technical decoration. The population needs to include people who can differentiate between different attribute requirements.

## Counterexample 2: Two attributes are always synchronized in the population

If

\[
\Pr(A^i=A^j)=1,
\]

Then the data cannot distinguish a certain question:

-Only requires attribute \(i\);
-Only requires attribute \(j\);
- Also requires \(i,j\).

Because \(A^i\ne A^j\) students have never appeared in the population.

## Boundary 3: Attribute column label exchange

Even if all conditions hold, column permutations are still indistinguishable from the reaction data:

\[
Q\sim QP.
\]

This is an inherent symmetry of the model. To give specific semantics to attribute columns, it is necessary to combine item content, expert annotations, or other external variables.

## Boundary four: \(c_i=g_i\)

If

\[
c_i=g_i,
\]

rule

\[
\Pr(R^i=1\mid\boldsymbol A)=g_i
\]

Same for all attribute profiles. The response to this question does not carry q-vector information.

## Boundary 5: Only use marginal accuracy

If \(T\)-matrix only retains a single question row, different Q can often match the same marginal probability by changing \(\boldsymbol p\). The joint constraints provided by question pairs and higher-order question groups are an important part of the result identification in this article.

The original theorem requires saturation \(T\). Low-order truncation is feasible in empirical algorithms, but its structural conditions need to be studied separately.

## Boundary 6: Insufficient integrity

If there is no pure question for a certain attribute, the unit matrix anchor point disappears. The full column rank construction of this article cannot be implemented, and some designs may still be identifiable but rely on other structures. This paper does not claim that completeness is necessary point-by-point on every specific Q.

## Boundary 7: Insufficient redundancy of C5

If an attribute is required by only one question, deleting the question will cause the attribute coverage to be lost, and the row proportion identification mechanism in the appendix will be ineffective. The original text shows that it is possible to construct examples in which Q cannot be recognized at this time.

## Boundary eight: \((\boldsymbol p,\boldsymbol c)\) joint identification

Even if Q is known, the attribute distribution and the master's probability of being correct may have too many parameters. The original text is displayed with \(Q=I_k\):

\[
\text{Response degrees of freedom}=2^k-1,
\]

\[
\text{parameter dimension}=(2^k-1)+k.
\]

Therefore Theorem 4.2 additionally assumes that \(\widetilde{\boldsymbol c}\) is consistent with the consistency of \(\boldsymbol p\).

## Boundary Nine: Unknown \(g_i\)

The author points out that it is conceivable that:

- insert consistent \(\widehat g_i\);
- Section \(g_i\) together.

However, the strict consistency of unknown guessing parameters requires new technical conditions, and the original article is left for future work.

## Boundary ten: Unknown attribute number \(k\)

The entire text treats \(k\) as known. If \(k\) is set incorrectly, the candidate Q space, the number of attribute profiles, and the number of columns of T will all change. The authors suggest introducing a BIC-like penalty in the future, along with the choice of attribute dimensionality and Q.

## The difference between identification, consistency and algorithm

|concept|This article deals with|
| --- | --- |
|identifiability|Inequivalent Q produces different overall reaction moments|
|Consistency|The global moment distance estimator recovers the true equivalence class as \(N\) increases|
|Limited sample accuracy|The original article does not give simulation or error bounds|
|Global optimization reachability|Defines exhaustive estimators without providing large-scale global solution guarantees|

These four levels of conclusions cannot replace each other. What is theoretically identifiable can also be extremely difficult to estimate in limited samples; a consistent objective function can also be stuck by local optimizers.

[Next page: Saturation moment, search complexity and practical truncation](22-computation-and-truncation.md)
