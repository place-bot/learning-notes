# T-matrix and identification equivalence

## 1. Dimensions of T-matrix

Supplementary Material Definition

\[
T(Q,\Theta)\in\mathbb R^{2^J\times2^K}.
\]

- row indexed by \(\boldsymbol r\in\{0,1\}^{J}\);
- Column indexed by \(\boldsymbol\alpha\in\{0,1\}^{K}\).

## 2. Element meaning

\[
T_{\boldsymbol r,\boldsymbol\alpha}(Q,\Theta)
=
\Pr(\boldsymbol R\succeq\boldsymbol r
\mid Q,\Theta,\boldsymbol\alpha)
=
\prod_{j=1}^{J}
\theta_{j,\boldsymbol\alpha}^{r_j}.
\]

Here \(\boldsymbol R\succeq\boldsymbol r\) means that all questions satisfying \(r_j=1\) will have positive responses; questions \(r_j=0\) are not restricted.

For example

\[
\boldsymbol r=(1,0,1,0)^\top
\]

Correspond

\[
T_{\boldsymbol r,\boldsymbol\alpha}
=
\theta_{1,\boldsymbol\alpha}
\theta_{3,\boldsymbol\alpha}.
\]

## 3. Mixed latent classes

Right multiplied by the latent class proportion we get the overall observable moment:

\[
\left[T(Q,\Theta)\boldsymbol p\right]_{\boldsymbol r}
=
\sum_{\boldsymbol\alpha}
T_{\boldsymbol r,\boldsymbol\alpha}
p_{\boldsymbol\alpha}
=
\Pr(\boldsymbol R\succeq\boldsymbol r).
\]

All joint forward reaction moments and the complete reaction distribution can be mutually recovered by Möbius inversion, so no identification information is lost using \(T\boldsymbol p\).

## 4. Lemma 1

Identification is equivalent to:

\[
T(Q,\Theta)\boldsymbol p
=
T(\bar Q,\bar\Theta)\bar{\boldsymbol p}
\]

inevitable

\[
(Q,\Theta,\boldsymbol p)
\sim
(\bar Q,\bar\Theta,\bar{\boldsymbol p}).
\]

In the proof, a reversible linear transformation will also be performed on \(T\). to any

\[
\boldsymbol\theta^\star=(\theta_1^\star,\ldots,\theta_J^\star)^\top,
\]

There is an invertible matrix \(D(\boldsymbol\theta^\star)\), so that the transformed row is equivalent to shifting the probability of each question from \(\theta_{j,\alpha}\) to

\[
\theta_{j,\alpha}-\theta_j^\star.
\]

Choosing the appropriate \(\boldsymbol\theta^\star\) can zero out certain latent class columns or item rows, thereby isolating the target parameter.

## 5. The role of T-matrix in the proof

```text
Same complete reaction distribution
        │
        ▼
T(Q,Θ)p = T(Q̄,Θ̄)p̄
        │
        ├── Select specific rows: isolate item combinations
        ├── Reversible translation: creating zero elements
        ├── Comparing column structures: recovering Γ and Q
        └── Elimination: restore item parameters and p
```

## 6. T-matrix with Liu, Xu & Ying

The first two Q-learning papers on this site also use T-matrix. The difference is:

- The Q learning algorithm takes the distance between the empirical moment and the candidate \(T(Q)\boldsymbol p\) as the target;
- This article uses the equality of the two overall \(T\)-mappings as the starting point for identification proof;
- Generally, \(T\) of RLCM uses the complete \(\Theta\), and \(T\) of DINA can be further written as \(\boldsymbol c,\boldsymbol g\) and ideal response matrix \(\Gamma(Q)\).
