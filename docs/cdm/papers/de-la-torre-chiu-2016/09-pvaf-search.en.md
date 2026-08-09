# PVAF exhaustive search and threshold

## Step 1: Calculate all non-zero candidates

\(K\) attributes in total

\[
2^K-1
\]

nonzero q-vector. Calculate each question one by one:

\[
\widehat{\varsigma}_j^2(\boldsymbol q).
\]

full attribute vector

\[
\boldsymbol 1=(1,\ldots,1)
\]

The smallest subgroup is generated and used as the sample maximum value benchmark.

## Step 2: Convert to PVAF

\[
\operatorname{PVAF}_j(\boldsymbol q)
=
\frac{
\widehat{\varsigma}_j^2(\boldsymbol q)
}{
\widehat{\varsigma}_j^2(\boldsymbol 1)
}.
\tag{12}
\]

The original text will

\[
\operatorname{PVAF}_j(\boldsymbol q)\ge\varepsilon
\]

Candidates are considered empirically appropriate. Both simulated and real data are used

\[
\varepsilon=.95.
\]

## Step 3: Minimum simplicity

Let the candidate set be

\[
\mathcal C_j(\varepsilon)
=
\left\{
\boldsymbol q:
\operatorname{PVAF}_j(\boldsymbol q)\ge\varepsilon
\right\}.
\]

Select the candidate with the fewest attributes:

\[
\widehat K_j
=
\min_{\boldsymbol q\in\mathcal C_j}
\sum_k q_k.
\]

If there are multiple candidates under the same attribute number, then select

\[
\widehat{\varsigma}_j^2
\]

The biggest one.

## Pseudocode

```text
for item j:
    for each nonzero q in {0,1}^K:
        collapse full latent classes using q
        calculate group weights and group success probabilities
        calculate GDI(q)

    PVAF(q) = GDI(q) / GDI(11...1)
    keep q with PVAF(q) >= epsilon
    keep the smallest number of required attributes
    break a same-size tie by the largest GDI
```

## Complexity

The number of candidates for a single question increases exponentially with \(K\):

| \(K\) |number of candidates|
| ---: | ---: |
| 5 | 31 |
| 10 | 1023 |
| 15 | 32767 |
| 20 | 1048575 |

The paper experiment is fixed at \(K=5\), which is very easy to exhaust. Large attribute spaces require preferential search, stepwise search, or structural constraints.

## The meaning of threshold

\(\varepsilon=.95\) indicates that the candidate needs to retain at least 95% of the inter-group success rate variance of the saturated group.

- Smaller \(\varepsilon\): easier to accept short q-vector, the risk of missed design increases;
- Larger \(\varepsilon\): closer to the saturated group, and the risk of addition increases;
- The sensitivity is stronger when the item effect is weak, the sample is small, or the attributes are highly correlated.

This threshold is a design parameter that regulates simplicity and information retention.

## Difference from 2008 threshold

The 2008 algorithm compares adjacent steps:

\[
\widehat\delta^{(s)}
-\widehat\delta^{(s-1)}
>\varepsilon.
\]

2016 Algorithm Comparison Candidates and Saturation Vectors:

\[
\frac{\widehat{\varsigma}^2(\boldsymbol q)}
{\widehat{\varsigma}^2(\boldsymbol1)}
\ge\varepsilon.
\]

One is the incremental threshold and the other is the retention ratio.
