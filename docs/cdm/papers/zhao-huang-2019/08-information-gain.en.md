# Information gain feature selection

## 1. Definition

Let the random variable \(X\) represent a text feature, and \(Y\) represent a cognitive attribute. The information gain is written as

\[
IG(X;Y)
=
H(Y)-H(Y\mid X).
\]

It is also equal to mutual information:

\[
I(X;Y)
=
\sum_{x,y}
p(x,y)
\log
\frac{p(x,y)}{p(x)p(y)}.
\]

Thesis formula is written

\[
IG(X;Y)=H(X)-H(X\mid Y),
\]

The two writing methods are equal due to mutual information symmetry.

## 2. Entropy

For discrete class \(Y\):

\[
H(Y)
=
-\sum_y p(y)\log p(y).
\]

If the category is more certain after observing the feature \(X\), then

\[
H(Y\mid X)<H(Y),
\]

So the information gain is positive.

## 3. Binary occurrence variables

In text feature selection, whether a word appears is often written as

\[
X_r=
\mathbb I\{\text{Features}r\text{appear in this question}\}.
\]

For the second category \(Y\in\{O,M\}\), each feature forms a frequency table \(2\times2\):

| | \(Y=O\) | \(Y=M\) |
| --- | ---: | ---: |
| \(X_r=1\) | \(n_{1O}\) | \(n_{1M}\) |
| \(X_r=0\) | \(n_{0O}\) | \(n_{0M}\) |

\(I(X_r;Y)\) can be calculated from four frequencies.

## 4. An intuitive example

If "integer" frequently appears in class O and rarely appears in class M, then:

\[
p(Y=O\mid X_{\text{integer}}=1)
\gg
p(Y=O).
\]

It is observed that this word significantly reduces category uncertainty and has a large information gain.

## 5. top-\(k\) selection

Calculate \(p\) candidate features

\[
IG_1,\ldots,IG_p,
\]

And sorted by:

\[
IG_{(1)}\ge IG_{(2)}\ge\cdots\ge IG_{(p)}.
\]

Given \(k\), select

\[
\mathcal S_k
=
\{(1),\ldots,(k)\}.
\]

paper order

\[
k=5,10,\ldots,300.
\]

There are 60 candidate values in total.

## 6. Advantages of filter method

Information gain is calculated before model training:

- fast;
- Decoupling from classifier;
- The same sorting can be used by three algorithms;
- Selected words can be interpreted by experts.

## 7. Implementation ambiguity in the original text

The text of the paper says "treat the frequency of the feature in the item as a variable", but does not explain the method used to calculate IG:

- Binary appearance;
- Original word frequency;
- Word frequency after discretization;
- TF--IDF continuous value.

These definitions will give different rankings.

The independent reconstruction of this site uses binary emergence variables that are more common and consistent with the definition of discrete mutual information:

\[
X_r=\mathbb I(\operatorname{TF}_{jr}>0).
\]

## 8. Prevent information leakage

IG uses labels and therefore must be estimated only on the training set:

\[
\widehat{IG}_r
=
\widehat I_{\mathcal T}(X_r;Y).
\]

If the test set tag is included, the selected words have already used test information, and the final score will be optimistic.
