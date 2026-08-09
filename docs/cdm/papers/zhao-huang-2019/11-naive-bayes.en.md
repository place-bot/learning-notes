# Gaussian Naive Bayes

## 1. Bayes classification

For category \(c\in\{O,M\}\):

\[
p(c\mid\boldsymbol x)
=
\frac{p(c)p(\boldsymbol x\mid c)}
{p(\boldsymbol x)}.
\]

When predicting \(p(\boldsymbol x)\) is the same for all categories, so

\[
\widehat c
=
\arg\max_c
p(c)p(\boldsymbol x\mid c).
\]

## 2. Conditional independence assumption

Naive Bayes assumes that each feature is conditionally independent given the category:

\[
p(\boldsymbol x\mid c)
=
\prod_{r=1}^{k}
p(x_r\mid c).
\]

So

\[
\widehat c
=
\arg\max_c
p(c)
\prod_{r=1}^{k}
p(x_r\mid c).
\]

The actual calculation usually takes the logarithm:

\[
\widehat c
=
\arg\max_c
\left[
\log p(c)
+\sum_{r=1}^{k}\log p(x_r\mid c)
\right].
\]

## 3. Gaussian hypothesis

The paper explicitly uses Gaussian NB:

\[
x_r\mid c
\sim
\mathcal N(\mu_{cr},\sigma_{cr}^2).
\]

The density is

\[
p(x_r\mid c)
=
\frac{1}
{\sqrt{2\pi\sigma_{cr}^2}}
\exp
\left[
-\frac{(x_r-\mu_{cr})^2}
{2\sigma_{cr}^2}
\right].
\]

## 4. Why Gaussian NB is used in TF--IDF is controversial

TF--IDF dimensions usually:

- non-negative;
- A large number is exactly 0;
- The distribution is highly skewed;
- It's hard to be normal.

The more common choices for text tasks are Multinomial NB or Complement NB. The paper does not compare these variants.

## 5. Why feature selection has a huge impact

NB result of unigram:

\[
21.3\%
\longrightarrow
84.0\%
\]

The accuracy increased by 62.7 percentage points.

Possible mechanisms are:

1. Most of the 2,943 features are extremely low frequency;
2. Gaussian NB estimates the mean and variance for each "category × feature";
3. The likelihood contribution of weak features continues to accumulate;
4. top-\(k\) reduces the dimension to up to 300;
5. The category signal of high information words dominates.

## 6. Three best results

|Features|There is IG accuracy|There is IG F1|
| --- | ---: | ---: |
| unigram | 84.0% | 84.7% |
| unigram+bigram | 84.6% | 85.2% |
| unigram+bigram+trigram | **85.2%** | **85.6%** |

## 7. Category prior

If estimated directly by frequency:

\[
\widehat p(O)\approx0.827,
\qquad
\widehat p(M)\approx0.173.
\]

The prior itself is strongly biased towards O. High-quality conclusions need to check M-type precision and recall at the same time, and the paper only reports the weighted total index.

## 8. Reproducibility Gap

Gaussian NB still has unreported settings:

- `priors`；
- `var_smoothing`；
- Whether the input is converted to dense array;
- TF--Normalization of IDF;
- Final selection value of \(k\).

These settings affect small sample minority class performance.
