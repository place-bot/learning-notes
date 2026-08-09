# Code implementation and computable verification

## Original code status

The paper does not report software packages, GitHub repositories, supplementary code, or numerical algorithm implementations. The Study population in the main text is the identification of parameters in the overall distribution, which proves that it does not rely on an estimation procedure.

Therefore, this page maps formulas to teaching codes, and there is no official code from the author available for line-by-line review.

## Site script

[`tools/xu_2017_rlcm_identifiability.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/xu_2017_rlcm_identifiability.py)
Use only the Python standard library and preserve exact rational arithmetic with `Fraction`.

## Q structure check

|function|mathematical objects|
| --- | --- |
| `is_complete()` |Q Does it contain a \(I_K\)|
| `has_c1()` |Can two non-overlapping \(I_K\) be removed in sequence?|
| `dina_structural_c2()` |After removing two unit blocks, is each \(\boldsymbol e_k\) still included?|

The last item is specific to DINA and is \(1-s_j>g_j\). In DINA, the remaining questions can distinguish
The structural condition of \(\boldsymbol e_k\) and \(\boldsymbol0\) is that the question only requires the attribute \(k\).

Generally, C2 of RLCM needs to be viewed directly
\(\theta_{j,\boldsymbol e_k}\) and
\(\theta_{j,\boldsymbol0}\), you cannot rely solely on the structural check in the function name.

## Construct Theta

`dina_theta()` implementation

\[
\theta_{j,\boldsymbol\alpha}
=
\begin{cases}
1-s_j,&\boldsymbol\alpha\succeq\boldsymbol q_j,\\
g_j,&\text{Others}.
\end{cases}
\]

The attribute profile is arranged by Hamming weight by `binary_vectors(K)` to facilitate the correspondence in the paper proof.

\[
\boldsymbol0,\ \boldsymbol e_k,\ 
\boldsymbol e_{h_1}+\boldsymbol e_{h_2},\ldots
\]

order.

## Construct T matrix

`t_matrix()` for each item subset \(\boldsymbol r\) with attribute profile
\(\boldsymbol\alpha\) Calculation

\[
t_{\boldsymbol r,\boldsymbol\alpha}
=
\prod_{j:r_j=1}
\theta_{j,\boldsymbol\alpha}.
\]

`observed_distribution()` independent enumeration exact response pattern:

\[
\sum_{\boldsymbol\alpha}
p_{\boldsymbol\alpha}
\prod_j
\theta_{j,\boldsymbol\alpha}^{r_j}
(1-\theta_{j,\boldsymbol\alpha})^{1-r_j}.
\]

`subset_marginals()` and then summarize the exact pattern as
\(P(\boldsymbol R\succeq\boldsymbol r)\). The test is passed only if the two calculated routes are equal.

## Proposition 3

`translation_matrix()` structure

\[
d_{\boldsymbol r,\boldsymbol r'}
=
(-1)^{|\boldsymbol r|-|\boldsymbol r'|}
\prod_{j:r_j-r'_j=1}\theta_j^*
\]

And in
Fill in 0 when \(\boldsymbol r'\npreceq\boldsymbol r\).

The program calculates respectively:

\[
T(Q,\Theta-\boldsymbol\theta^*\boldsymbol1^\top)
\]

and

\[
D(\boldsymbol\theta^*)T(Q,\Theta),
\]

Then compare rational numbers one by one. It also verifies that the diagonal elements of \(D\) are all ones.

## Numerical collision of Proposition 2

The script has two sets of parameters built into [counterexample page](14-counterexample.md)], and use
`observed_distribution()` enumerate all

\[
(0,0),(1,0),(0,1),(1,1)
\]

reaction mode. `maximum_difference()` returns an exact score of 0.

## Run method

```bash
python3 tools/xu_2017_rlcm_identifiability.py
python3 tools/xu_2017_rlcm_identifiability.py --attributes 3
```

Default \(K=2\). When the number of attributes increases, three unit blocks generate \(J=3K\) questions, and the complete \(T\)-matrix has

\[
2^{3K}\times2^K
\]

units, so this script is positioned as a small-scale teaching check.

## Implement boundaries

The script doesn't have:

- Fit RLCM;
- Implement EM or MCMC;
- Estimate Q from data;
- Prove the general theorems of C1 and C2;
- Interpret a certain value \(T\)-matrix full rank into joint parameter identification;
- Implement CAT topic selection.

To make real data estimates, proven CDM software should be used and theoretical design conditions and numerical stability should be checked before and after estimation.
