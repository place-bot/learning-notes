# L2 Logistic Regression

## 1. Probabilistic model

For the binary \(Y\), let

\[
p_j
=
\Pr(Y_j=1\mid\boldsymbol x_j).
\]

The logit model is

\[
\log
\frac{p_j}{1-p_j}
=
\alpha+\boldsymbol\beta^\top\boldsymbol x_j.
\]

Therefore

\[
p_j
=
\sigma
\left(
\alpha+\boldsymbol\beta^\top\boldsymbol x_j
\right),
\]

Among them

\[
\sigma(z)=\frac{1}{1+e^{-z}}.
\]

## 2. Log likelihood

\[
\ell(\alpha,\boldsymbol\beta)
=
\sum_{j=1}^{n}
\left[
y_j\log p_j
+(1-y_j)\log(1-p_j)
\right].
\]

The paper Equation (7) is written

\[
\ell(\alpha,\boldsymbol\beta)
=
\sum_{j=1}^{n}
\log p(y_j\mid\boldsymbol x_j,\alpha,\boldsymbol\beta).
\]

## 3. L2 regular

Paper use

\[
\ell'(\alpha,\boldsymbol\beta)
=
\ell(\alpha,\boldsymbol\beta)
-
\frac{\lambda}{2}
\left(
\alpha^2+\sum_{r=1}^{m}\beta_r^2
\right).
\]

Maximizing \(\ell'\) is equivalent to minimizing the negative log-likelihood plus an L2 penalty.

## 4. Interpretation of characteristic coefficients

If \(Y=1\) is defined as M, then:

\[
\beta_r>0
\]

Representation feature \(r\) improves the log-odds of M class;

\[
\beta_r<0
\]

Representation feature \(r\) supports class O more.

LR can provide interpretable keyword directions, but the paper does not report coefficients.

## 5. Paper result

|Features|There is IG accuracy|Full feature accuracy|
| --- | ---: | ---: |
| unigram | 74.1% | 72.5% |
| unigram+bigram | 74.6% | 72.7% |
| unigram+bigram+trigram | **75.3%** | 72.5% |

The corresponding accuracy improvements are 1.6, 1.9, and 2.8 percentage points.

## 6. Differences from NB

LR directly optimizes conditional probabilities:

\[
p(Y\mid X).
\]

NB modeling:

\[
p(X\mid Y)p(Y).
\]

When the sample is small, the strong structural assumption of NB can sometimes reduce the estimation variance; as the data increases, the discriminant learning of LR may be more flexible. There are only 805 questions in this article, and the results are relatively consistent with this classic.

## 7. “Default parameters” are still not sufficient

The default value of scikit-learn changes from version to version. At least required:

- sklearn version;
- `solver`；
- `C`；
- `class_weight`；
- `max_iter`；
- intercept whether to punish;
- Convergence status.

The paper only explains the L2 regularization and default parameters.

## 8. Reconstruction of this site

To stay close to a common 2019 setting, the standalone code explicitly uses:

```python
LogisticRegression(
    C=1.0,
    penalty="l2",
    solver="liblinear",
    max_iter=5000,
    random_state=2019
)
```

This is a set of transparent, repeatable choices.
