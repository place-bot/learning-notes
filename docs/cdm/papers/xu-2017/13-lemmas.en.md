# Two technical lemmas

The main proof is to multiply a number of differences multiple times. To ensure that the selected row actually leaves a usable non-zero element, it is necessary to exclude some accidental equality "across two sets of parameters". Lemma 1 and Lemma 2 undertake this work.

## Lemma 1

If the main theorem conditions hold and equation (3.5) holds, for any \(k\) and any
\(\boldsymbol\alpha^*\succeq\boldsymbol e_k\)：

\[
\theta_{k,\boldsymbol0}
\ne
\bar\theta_{k,\boldsymbol\alpha^*},
\qquad
\theta_{k,\boldsymbol\alpha^*}
\ne
\bar\theta_{k,\boldsymbol0},
\]

\[
\theta_{K+k,\boldsymbol0}
\ne
\bar\theta_{K+k,\boldsymbol\alpha^*},
\qquad
\theta_{K+k,\boldsymbol\alpha^*}
\ne
\bar\theta_{K+k,\boldsymbol0}.
\]

### Prove logic

hypothesis

\[
\theta_{k,\boldsymbol0}
=
\bar\theta_{k,\boldsymbol\alpha^*}.
\]

Question \(k\) is a single attribute question. Limited by monotonicity, in the parameter without horizontal line

\[
\theta_{k,\boldsymbol\alpha}
\ge
\theta_{k,\boldsymbol0}
\quad\forall\boldsymbol\alpha,
\]

and there is a direct proportion of falling into strictly higher ability-adequate classes, so

\[
\sum_{\boldsymbol\alpha}
\theta_{k,\boldsymbol\alpha}p_{\boldsymbol\alpha}
>
\theta_{k,\boldsymbol0}.
\]

Parameters with horizontal lines
\(\bar\theta_{k,\boldsymbol\alpha^*}\) is the highest probability of this question, therefore

\[
\sum_{\boldsymbol\alpha}
\bar\theta_{k,\boldsymbol\alpha}
\bar p_{\boldsymbol\alpha}
<
\bar\theta_{k,\boldsymbol\alpha^*}.
\]

After substituting the equating assumptions, the marginal success rates of question \(k\) of the two sets of models cannot be equal, which is inconsistent with equation (3.5).

The remaining three inequalities are obtained by the same symmetry argument.

## Lemma 2

For any \(1\le k\ne h\le K\):

\[
\theta_{k,\boldsymbol e_h}
\ne
\bar\theta_{k,\boldsymbol1},
\qquad
\theta_{k,\boldsymbol1}
\ne
\bar\theta_{k,\boldsymbol e_h},
\]

\[
\theta_{K+k,\boldsymbol e_h}
\ne
\bar\theta_{K+k,\boldsymbol1},
\qquad
\theta_{K+k,\boldsymbol1}
\ne
\bar\theta_{K+k,\boldsymbol e_h}.
\]

Here, the single attribute question \(k\) requires the attribute \(k\), and
\(\boldsymbol e_h\) has no attribute \(k\).

## Lemma 2 Why is it harder?

Lemma 1 To compare the lowest value and the highest value across models for a certain question, strict clamping of the marginal mean can be directly used.

Lemma 2 compares:

- The probability of the insufficient ability class \(\boldsymbol e_h\) in a set of models;
- Probability of sufficiently capable class \(\boldsymbol1\) in another set of models.

You cannot complete the same challenge by just looking at the margins of one question. The paper also needs to borrow:

1. The \(T\)-submatrix corresponding to the second \(I_K\) block;
2. The triangular structure and full rank of the submatrix after translation;
3. A linear combination to select a potential class sequence;
4. Comparison of \(\boldsymbol0/\boldsymbol e_k\) provided by C2 in the remaining questions;
5. The highest probability in the model is strictly greater than the probability of insufficient ability.

Together, these structures transform assumed cross-model equality into intra-model order contradictions.

## The role of full-rank submatrix

The second \(I_K\) block forms a

\[
2^K\times2^K
\]

The \(T\)-submatrix. After appropriate translation and rearrangement, it takes the shape of a triangle, with the diagonal elements consisting of strict probability differences and therefore non-zero and full rank.

Full rank means that a row vector \(\boldsymbol m\) can be found such that

\[
\boldsymbol m
T(Q_1,\bar\Theta_{K+1:2K})
\]

Only the specified attribute column takes the value 1, and the remaining columns are 0. This "column selector" allows the proof to track potential classes that would otherwise be mixed together.

## The joint effect of the two lemmas

The key coefficients appearing in the proof are of the form

\[
\prod_k
\left(
\theta_{k,\boldsymbol\alpha}
-\bar\theta_{k,\boldsymbol\beta}
\right).
\]

As soon as a factor is zero, the column that was originally scheduled to be quarantined disappears. The lemma gives exactly the necessary non-zero guarantees to make every ratio or elimination legal.

## Assume dependencies

Lemma depends on:

- each \(p_{\boldsymbol\alpha}>0\);
- Strict separation of single-attribute questions (2.3);
- Two unit blocks of C1;
- Lemma 2 also uses the remaining problem comparison formed by C2.

Therefore, it cannot be copied directly in models that allow zero structure, no strict monotonicity, or lack a second anchor block.
