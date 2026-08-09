# Appendix proves the key role of C5

## What does the appendix prove?

The main text puts the two most combined results into the appendix:

- Proposition 6.3: The first \(k\) lines of the error candidate are complete;
- Proposition 6.4: The first \(k\) lines of the error candidate are incomplete.

Both proofs are looking for a row proportional relationship that the candidate column space is forced to satisfy but the true moment violates.

## Basic line proportion tools

In the guessless \(T_c(Q)\), if the two B-vectors are the same and the second question group has one more question \(i\) than the first, then the corresponding two rows only differ by the factor \(c_i\).

The question group \(S\) has covered all attributes of the question \(i\):

\[
B_Q(I_i\wedge I_S)=B_Q(I_S).
\]

Then

\[
B_{c,Q}(I_i\wedge I_S)
=
c_iB_{c,Q}(I_S).
\]

Any vector located in the \(T_c(Q)\) column space inherits this row scale.

## C5 How to lock \(c_i\)

Take:

- Row A: combination of all \(m\) questions;
- Row B: The combination of all questions except question \(i\).

Each attribute required by C5 guarantee question \(i\) is also required by other questions, so

\[
B_Q(A)=B_Q(B).
\]

In \(T_c(Q)\),

\[
\text{row}_A
=
c_i\,\text{row}_B.
\]

For candidate \(Q'\), if the relevant structure makes the same two binary rows the same, then its row ratio is \(c_i'\). If the true moment belongs to the candidate column space, the two ratios must be compatible, forcing

\[
c_i'=c_i.
\]

The appendix then shows with additional lines that even if the scaling parameters are forced to be the same, the wrong structure still produces unsatisfied proportions.

## Three types of differences in Proposition 6.3

Suppose that a certain subsequent question row \(l\) in the candidate is the same as the anchor question combination row \(h\), but the two rows in the true Q are different. There are three possible set relations under true Q.

### Real question \(l\) requires strict requirements for more attributes

Exists:

- People who can complete \(h\) but cannot complete \(l\), quality \(p_1>0\);
- People who can do both at the same time, quality \(p_2>0\).

The candidate treats two rows as the same and requires the moment components to be in a fixed proportion. \(p_1>0\) in the real model breaks this ratio.

### The real question \(l\) has strict requirements and fewer attributes.

There are people of positive quality who can complete \(l\) but cannot complete \(h\). The same paradox of proportion appears.

### The two sets of attributes are not inclusive of each other.

There are at least three types of positive quality people:

- Only complete \(l\);
- Only complete \(h\);
- Complete both at the same time.

By adding the question group row of \(I_l\wedge I_h\), we can construct a relationship that candidates must satisfy and true moments violate.

C4 ensures that the attribute profiles of these witness groups have positive probabilities.

## Situation division of Proposition 6.4

If \(Q'_{1:k}\) is incomplete, the appendix will be considered:

1. There are two identical q-vectors in the first \(k\) row;
2. There are no repeated lines, but at least one line contains two or more 1's;
3. There is coverage between multi-attribute rows and single-attribute rows;
4. Multiple multi-attribute rows form a closed substructure.

In the first three categories, a pair of question groups can be directly found to form a proportional contradiction.

The last category uses proof by contradiction. If deleting any multi-attribute row changes the attribute union, then each row has a unique attribute that is only covered by it. The gradual decrease of the collection cardinality will force the last row to contain at most one attribute, which is inconsistent with being set as a multi-attribute row. Therefore there is always a row that can be deleted without changing the union, and the desired proportional relationship is obtained.

## Where does C5 break when missing?

If an attribute only appears in question \(i\), deleting question \(i\) will lose the attribute:

\[
B_Q(A)\ne B_Q(B).
\]

The difference between the "All Questions" and "Delete Questions \(i\)" lines is no longer \(c_i\), proving that the scaling factor cannot be locked. The original article points out that one can further construct counterexamples to which Q is not identifiable.

## Overall logic of appendix proof

Follow these three steps every time:

1. Error Q makes two rows the same or in a fixed proportion in the candidate \(T\)-matrix;
2. C5 uses redundant coverage to lock the scaling factors of the candidate and true models;
3. C4 provides positive quality discriminative populations such that true moments violate candidate proportions.

This shows that C4 and C5 have a clear division of labor: the former ensures that "someone can see the difference", and the latter ensures that "the item structure provides comparable repetition constraints."

[Next page: Counterexamples, necessity and identification boundaries](21-counterexamples-and-boundaries.md)
