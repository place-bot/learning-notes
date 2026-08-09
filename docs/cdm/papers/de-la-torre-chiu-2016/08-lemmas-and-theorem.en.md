# Two lemmas, main theorem and proof

## Lemma 1: Folding does not change the overall mean

Group any thicker or thinner attributes:

\[
\bar p(\boldsymbol\alpha_{K:K''})
=
\bar p(\boldsymbol\alpha_{1:K''}).
\tag{9}
\]

The proof is directly substituted into the folding probability:

\[
\begin{aligned}
\bar p(\boldsymbol\alpha_{K:K''})
&=
\sum_{\boldsymbol\alpha_{K:K''}}
w(\boldsymbol\alpha_{K:K''})
p(\boldsymbol\alpha_{K:K''})\\
&=
\sum_{\boldsymbol\alpha_{K:K''}}
\sum_{\boldsymbol\alpha_{1:K-1}}
w(\boldsymbol\alpha_{1:K''})
p(\boldsymbol\alpha_{1:K''})\\
&=
\bar p(\boldsymbol\alpha_{1:K''}).
\end{aligned}
\]

So \(-\bar p^2\) in all candidate GDIs is the same constant. Compare GDI is equivalent to compare

\[
\sum w p^2.
\]

## Lemma 2: Restoring a valid attribute does not reduce \(\sum wp^2\)

Split the rough group into two groups based on an attribute that really affects the success rate. Record the weights and success rates of the two subgroups

\[
w_0,p_0,
\qquad
w_1,p_1.
\]

The crude group contribution is

\[
(w_0+w_1)
\left(
\frac{w_0p_0+w_1p_1}{w_0+w_1}
\right)^2.
\]

The contribution of the small group is

\[
w_0p_0^2+w_1p_1^2.
\]

The difference between the two:

\[
\begin{aligned}
&w_0p_0^2+w_1p_1^2
-
\frac{(w_0p_0+w_1p_1)^2}{w_0+w_1}\\
&\qquad=
\frac{w_0w_1}{w_0+w_1}(p_0-p_1)^2
\ge 0.
\end{aligned}
\tag{10}
\]

Adding up the differences across all remaining attribute combinations, we get paper Lemma 2:

\[
\sum w_{\text{thick}}p_{\text{thick}}^2
\le
\sum w_{\text{thin}}p_{\text{thin}}^2.
\]

The condition for the equality sign to be true is that the two subgroups of each split satisfy \(p_0=p_1\).

## Main Theorem

Let \(\boldsymbol q^*\) be the correct q-vector, and any candidate \(\boldsymbol q\) satisfies

\[
\varsigma_j^2(\boldsymbol q)
\le
\varsigma_j^2(\boldsymbol q^*).
\tag{11}
\]

### Scenario 1: Only add attributes

Candidates contain all truly required attributes, plus some extraneous attributes. The correct grouping is already homogeneous within the group, and the subgroups after further subdivision have the same success probability:

\[
p(\boldsymbol\alpha_{\boldsymbol q})
=
p(\boldsymbol\alpha_{\boldsymbol q^*}).
\]

So

\[
\varsigma_j^2(\boldsymbol q)
=
\varsigma_j^2(\boldsymbol q^*).
\]

### Scenario 2: Omission and addition at the same time

First ignore the added extraneous attributes, which do not change GDI; then restore the missing real attributes one by one. Each time an attribute is restored, according to Lemma 2, \(\sum wp^2\) is non-decreasing. According to Lemma 1, \(\bar p^2\) is unchanged. Finally, formula (11) is obtained.

### Scenario 3: Only missing attributes

This is a special case of case 2 without adding attributes, and is also obtained by Lemma 2.

## Conclusions that the theorem can support

- The correct q-vector reaches the maximum GDI when the overall success probability and overall weight are known;
- Strictly added vectors may be juxtaposed with correct vectors;
- The least attribute rule selects the correct vector from the tied maximum.

## What is left from theorem to sample algorithm?

used in practice

\[
\widehat w,\qquad
\widehat p,\qquad
\widehat{\varsigma}^2.
\]

These quantities result from the initial Q fit. Limited sample noise may make the estimated GDI of the full attribute vector slightly higher than the correct vector; the system bias of the initial Q may also change the ordering. Therefore, the theorem gives the rationality of the overall goal, and the sample estimation properties require additional conditions.
