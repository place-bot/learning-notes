# Intensive reading of code status and implementation

## Original code status

After verifying the paper text, open full text, arXiv version and bibliographic information, it can be confirmed that:

- There is no code repository link in the text;
- No access to supplementary materials;
- No software version;
- No data files;
- No random seeds;
- No pseudocode to run directly.

This is consistent with the theoretical positioning of the paper. The original text's "estimator" is a mathematical definition, and the computational discussion focuses on quadratic programming, chunking, and truncation recommendations.

This site provides independent teaching implementation:

[`tools/liu_xu_ying_2013_theory_check.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/liu_xu_ying_2013_theory_check.py)

It is used to check structural identities and small-scale enumeration results, and is not implemented by pretending to be the author.

## Thesis formula to code object

|Thesis object|code object|meaning|
| --- | --- | --- |
| \(\{0,1\}^k\) | `attribute_profiles(k)` |Enumerate all attribute profiles|
| \(\xi^i(\boldsymbol A)\) | `ideal_response(q, profiles)` |Compute item—mode capability indication|
| \(B_{c,g,Q}(I_i)\) | `item_response_probabilities(...)` |conditional correct probability line|
|All non-empty question groups| `item_subsets(m)` |row index of saturation moment|
| \(T_{c,g}(Q)\) | `t_matrix_full(...)` |Stacked question set probability product|
| \(T(Q)\) | `deterministic_t_nonzero(q)` |Noiseless and excludes all-zero modes|
| \(\boldsymbol\alpha\) | `empirical_moments(...)` |Experience combined correct rate|
|Remove the bounds for \(\boldsymbol p\)| `fit_simplex(t_matrix, target)` |Simplex constrained quadratic programming|
|Q column substitution equivalence class| `canonical_q(q)` |Obtain the canonical representation after replacing the enumeration column|
|Candidate Q-space| `candidate_q_matrices(m, k)` |Enumerate candidates without all-zero rows|
|Proposition 6.6 of D| `guessing_removal_matrix(...)` |Inclusion-exclusion centralization transformation|

## ideal response

Code using broadcast comparison:

```python
np.all(
    profiles[None, :, :] >= q[:, None, :],
    axis=2,
).astype(float)
```

The output shape is

\[
m\times2^k.
\]

The \((i,a)\) element is equal to

\[
\mathbf1(\boldsymbol A_a\ge\boldsymbol q_i).
\]

## Conditional correct probability

Code implementation

```python
g + (c - g) * xi
```

Element-wise correspondence

\[
g_i+(c_i-g_i)\xi^i(\boldsymbol A).
\]

The output is still an "item × attribute profile" matrix.

## Saturated T-matrix

For each non-empty item subset `subset`:

```python
np.prod(probabilities[list(subset), :], axis=0)
```

Under partial independence, this is equal to the conditional probability that all items in the group are answered correctly. All rows are arranged in lexicographic order according to question group size.

## One difference between paper writing and code writing

The paper excludes all zero attribute profiles in \(T_{c,g}(Q)\), and then writes its contribution as

\[
p_0\boldsymbol g_{\mathrm{joint}}.
\]

The code directly retains all \(2^k\) pattern columns:

\[
\overline T_{c,g}(Q)
=
\left(
\boldsymbol g_{\mathrm{joint}},T_{c,g}(Q)
\right).
\]

The two representations are completely equivalent. The full column representation is more suitable for simplex optimization and numerical verification.

## Simplex profile optimization

`fit_simplex` minimize

\[
\frac12
\|T\boldsymbol p-\boldsymbol y\|_2^2
\]

and constrain

\[
0\le p_a\le1,\qquad
\sum_a p_a=1.
\]

The code uses SLSQP and provides analytic gradients

\[
\nabla_{\boldsymbol p}
\frac12\|T\boldsymbol p-\boldsymbol y\|_2^2
=
T^\top(T\boldsymbol p-\boldsymbol y).
\]

Since the target is convex with respect to \(\boldsymbol p\), there is no non-global local minimum problem under fixed T.

## Implementation of D

For the question group \(S\), the centralizing moment is expanded as

\[
E\!\left[\prod_{i\in S}(R^i-g_i)\right]
=
\sum_{U\subseteq S}
(-1)^{|S|-|U|}
\left(\prod_{i\in S\setminus U}g_i\right)
E\!\left[\prod_{i\in U}R^i\right].
\]

`guessing_removal_matrix` enumerates \(U\subseteq S\) and puts each coefficient into the corresponding position of D. This implementation gives an explicitly computed version of "there is D" in Proposition 6.6.

## Q Equivalence class normalization

`canonical_q` enumerates \(k!\) column replacements, and uses the flattened smallest tuple as the equivalence class identifier. This method is transparent and reliable for small \(k\); for large \(k\), the more efficient bipartite graph standard labeling can be used.

## Implementation scope

Script coverage:

- Saturated T construction;
- The attribute distribution profile of \(c,g\) is known;
- Small-scale Q full enumeration;
- D transformation;
- DINA data generation;
- Limited sample demo.

The script is not implemented:

- Nested profile of unknown \(c\);
- Search all candidate structures of formula (4.4);
- Large-scale blocking and alignment;
- Row-by-row hill-climbing algorithm of the 2012 paper;
- Automatic attribute number selection.

Such a scope is consistent with the purpose of this site to "verify theoretical objects".

[Next page: This site can calculate and verify](25-computational-check.md)
