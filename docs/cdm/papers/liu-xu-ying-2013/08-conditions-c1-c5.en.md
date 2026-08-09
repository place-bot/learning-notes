# C1--C5: What does each condition control?

## Condition original text

### C1: Q Complete

\[
Q\ \text{contains}\ I_k\ \text{all rows of}.
\]

Each attribute has a question that requires only that attribute.

### C2: \(T(Q)\) saturated

The joint correct answer events of all non-empty item subsets enter \(T(Q)\) and \(\boldsymbol\alpha\).

### C3: Student attributes are independently and identically distributed

\[
\boldsymbol A_1,\ldots,\boldsymbol A_N
\overset{\text{i.i.d.}}{\sim}\boldsymbol p^*,
\]

and

\[
\Pr(\boldsymbol A_r=\boldsymbol A)
=p_{\boldsymbol A}^*.
\]

### C4: Completely diverse overall

\[
(p_{\boldsymbol0}^*,\boldsymbol p^*)\succ\boldsymbol0.
\]

That is, all \(2^k\) attribute profiles have strict positive probability.

### C5: Each attribute is required by at least two questions

For each column \(j\),

\[
\sum_{i=1}^m Q_{ij}\ge2.
\]

## Which step does each condition enter?

|Conditions|Mathematical effects|Risk if missing|
| --- | --- | --- |
| C1 |Building block upper triangular full-rank submatrix|Property direction lacks pure question anchor point|
| C2 |Use all question group rows for spatial comparison|Key joint constraints are not in the objective function|
| C3 |Using the law of large numbers for empirical attribute proportions and empirical moments|The sample moments may not converge to the fixed population moment|
| C4 |Each type of population used to distinguish Q has positive mass|Some structural differences never appear in the data|
| C5 |After deleting any question, its attribute coverage will still be retained.|Unable to lock row scaling and structure with duplicate question group rows|

## Meaning of C4

C4 is very strong. It requires:

\[
p_{00\cdots0}^*>0,\quad
p_{00\cdots1}^*>0,\quad\ldots,\quad
p_{11\cdots1}^*>0.
\]

When \(k\) is large, it will be very difficult to have enough samples for all modes. The theorem only requires that the overall probability is strictly positive, and a rare pattern may still not appear at all in a limited sample, resulting in unstable recovery.

## Why can C4 distinguish item requirements?

Suppose there are differences between two candidates Q for a certain question:

- a candidate requirement attribute 1;
- Another candidate requires attribute 1 and attribute 2.

People with pattern \(10\) can distinguish between these two structures. If \(p_{10}^*=0\), no students in the population provide information for this distinction direction. C4 guarantees that every such witness pattern has positive quality.

## Collection explanation for C5

Write the attribute set required by question \(i\) as

\[
\mathcal K_i=\{j:Q_{ij}=1\}.
\]

C5 means that each attribute belongs to at least two \(\mathcal K_i\).

Therefore, the attributes of all items are combined

\[
\bigcup_{i=1}^m\mathcal K_i
\]

It remains unchanged after deleting any question:

\[
\bigcup_{h=1}^m\mathcal K_h
=
\bigcup_{h\ne i}\mathcal K_h.
\]

Therefore, the binary B-vectors of the two rows of "all questions" and "all questions except question \(i\)" in saturated \(T(Q)\) are the same. After adding \(c_i\), the two rows only differ by one multiplication factor, \(c_i\). The appendix demonstrates repeated use of this property.

## Sufficient conditions and weakest conditions

What this article proves is:

\[
\text{C1--C5}
\quad\Longrightarrow\quad
\text{consistent recovery}.
\]

This logic does not imply that each condition is individually necessary in all models. The original text gives:

- Clear and unrecognizable counterexamples to C4 failure;
- Unrecognizable instances can be constructed when C5 fails;
- C1 and C2 are the guarantee conditions currently used in the proof, and weaker requirements may be adopted for some specific designs.

## Relationship with subsequent identifiability literature

This article establishes an early framework of sufficient conditions. Subsequent work further searches for more refined necessary and sufficient conditions, deals with general restricted latent class models, and reduces the reliance on complete saturation moments or strong population diversity. When reading this article, C1--C5 should be viewed as a set of transparent, provable, and design-interpretable baseline conditions.

[Next page: Theorem 2.4](09-theorem-2-4.md)
