#Full text result and evidence boundary

## First note: There is no empirical experiment in this article.

The full text of the paper includes theoretical settings, theorems, lemmas and proofs, without:

- Real data sets;
- Simulation data generation conditions;
- training set and test set;
- Comparison of estimation algorithms;
- Accuracy, RMSE, AIC, BIC or coverage rate;
-Official implementation warehouse.

Therefore, this page summarizes "theoretical results and their supporting evidence". Evaluating this type of paper as "experimentally effective" will change the nature of its evidence. It proves the conditions under which the population distribution uniquely determines the parameters without studying the finite sample estimation error.

## Main result map of the full text

|result|model|core conditions|Conclusion|
| --- | --- | --- | --- |
| Theorem 1 |Three-way tensor decomposition| \(I_1+I_2+I_3\ge 2r+2\) |Factor Unique to Common Permutation and Scaling|
| Corollary 2 |Three-variable finite latent class|Positive class proportion; point-state Kruskal condition|Probabilistic parameter unique to label permutation|
| Corollary 3 |Three-variable finite latent class| \(\sum_j\min(r,\kappa_j)\ge2r+2\) |Parameters are universally identifiable|
| Theorem 4 |\(p\) variable finite latent class|There is a partition that satisfies three block inequalities|All univariate parameters are universally identifiable|
| Corollary 5 |Bernoulli product mixture| \(p\ge2\lceil\log_2r\rceil+1\) |\(r\) class parameters are universally identifiable|
| Theorem 6 |Discrete HMM| \(\binom{k+\kappa-1}{\kappa-1}\ge r\) |Pan-recognition \(A,B\) from edge distribution of \(2k+1\) consecutive observations|
| Theorem 7 |Two-category random graph mixture|At least 16 nodes; \(p_{11},p_{12},p_{22}\) different|Parameters strictly recognized to label replacement|
| Theorem 8 |Non-parametric multiplicative distribution mixture|At least 3 variables; components in each direction measure linear independence|\(\pi_i,\mu_i^j\) strictly recognizes label replacement|
| Theorem 9 |Non-parametric block product mixing|At least 3 conditionally independent blocks; block components measure linear independence|Strict recognition of block measures and proportions|
| Lemma 10 / Corollary 11 |non-parametric mixture|The distribution rank of the two-variable edge is \(r\)|Express linear independence using observable edge conditions|

## Limited potential class result

The innovations in the limited latent class part focus on two points:

1. Extend Kruskal’s three-variable result to any number of finite state observation variables;
2. Lower a sufficient upper bound on the number of variables required for a Bernoulli mixture to the logarithmic order.

The paper defines \(C(r)\) as the minimum number of sufficient variables required to ensure universal recognition of the \(r\) class binary latent class model. Dimensionality comparison gives a logarithmic lower bound, Corollary 5 gives

\[
C(r)\le 2\lceil\log_2r\rceil+1.
\]

Therefore

\[
C(r)=\Theta(\log_2r)
\]

It is established in the growth stage sense. The paper also makes it clear that the constant factor may still be improved upon.

## Theorem 6：HMM

### Model parameters

Assume that the hidden chain \(Z_t\) has \(r\) states, and the observation \(X_t\) has \(\kappa\) states:

- \(A\in\mathbb R^{r\times r}\): hidden state transition matrix;
- \(\pi\): stationary distribution;
- \(B\in\mathbb R^{r\times\kappa}\): emission probability matrix,
  \(B(i,x)=P(X_t=x\mid Z_t=i)\)。

### Identify length

If the integer \(k\) satisfies

\[
\binom{k+\kappa-1}{\kappa-1}\ge r,
\tag{3}
\]

Then the general HMM parameters can be obtained from

\[
(X_0,\ldots,X_{2k})
\]

Hidden state permutations are identified in the marginal distribution of these \(2k+1\) consecutive observations.

### Three block embedding

The paper retains the intermediate hidden state \(Z_k\) and divides the observations into

\[
(X_0,\ldots,X_{k-1}),
\qquad
X_k,
\qquad
(X_{k+1},\ldots,X_{2k}).
\]

Given \(Z_k\), the left block, current observation, and right block are independent of each other. The three constitute a \(r\) type three-variable latent class model.

When \(\kappa=2\),

\[
\binom{k+1}{1}=k+1\ge r,
\]

The minimum is \(k=r-1\), so in the worst case \(2r-1\) consecutive observations are sufficient. If \(\kappa\) increases, the number of combinations increases faster, and the required \(k\) will decrease.

### Distance from CDM

HMM result is suitable for dynamic hidden states. Static CDM usually assumes that the attribute state is fixed within a test; longitudinal CDM, learning process model or knowledge tracking are closer to this structure.

## Theorem 7: Random Graph Mixing

Each node \(v_i\) has latent class \(Z_i\). The edge indicator variables are independent given all node categories:

\[
X_{ij}\mid Z_i,Z_j
\sim
\operatorname{Bernoulli}(p_{Z_iZ_j}).
\]

For two node categories, if

\[
p_{11},p_{12},p_{22}
\]

are distinct from each other and the number of nodes is at least 16, the paper proves that the parameters are strictly identified to class swapping.

It is proved that all node states are synthesized into a composite latent variable, and then three groups of subgraphs that do not share edges with each other are constructed as three composite observation variables. The difficulty is to prove that the subgraph conditional probability matrix has full row rank.

The formal theorem of the paper states 16 nodes; Remark 2 shows that a more complex argument can reduce the sufficient number of nodes to 10, but does not give this argument, nor does it claim to have found the minimum number of nodes.

## Theorem 8 and 9: non-parametric product mixture

consider

\[
P
=
\sum_{i=1}^{r}\pi_i
\prod_{j=1}^{p}\mu_i^j,
\]

where \(\mu_i^j\) is a general probability measure. If \(p\ge3\), and for each direction \(j\),

\[
\{\mu_1^j,\ldots,\mu_r^j\}
\]

Linearly independent, then mixture ratios and all component measures strictly identify label permutations.

The proof steps are:

1. Use tangent points to bin continuous variables into finite state variables;
2. Select the cut point to make the binning conditional probability matrix full row rank;
3. Use Kruskal on the three-way table after binning;
4. Let the specified cut point enter the bin and restore each cumulative distribution function point by point;
5. The probability measure is uniquely determined by the CDF.

Theorem 9 generalizes univariate directions to multidimensional observation blocks.

## Lemma 10 and Corollary 11

Theorem 8's linear independence condition is written on the unknown component measure. The paper further defines the rank of a two-variable distribution: If a two-variable measure can be written as the sum of the products of \(r\) signed univariate measures and cannot be expressed in fewer terms, then its rank is \(r\).

Lemma 10 Description

\[
P(X_1,X_2)
=
\sum_{i=1}^{r}\pi_i\mu_i^1\mu_i^2
\]

The distribution rank is \(r\), if and only if the set of components on both sides

\[
\{\mu_i^1\}_{i=1}^{r},
\qquad
\{\mu_i^2\}_{i=1}^{r}
\]

are linearly unrelated.

Corollary 11 The condition can thus be written as the bivariate marginal rank of the observed distribution. This is closer to a testable condition than directly mentioning the linear independence of the unknown components, but the paper also admits that it will be difficult to test the distribution rank from the data.

## How does the paper support its conclusion?

|evidence|role in the paper|
| --- | --- |
|Kruskal's uniqueness theorem|Provides core uniqueness for three-way decomposition|
|Determinants and algebraic subvarieties|Generalize specific full-rank points to be universally identifiable|
|Vandermonde construction|Show that the associated full-rank polynomial is indeed not constant zero.|
|conditional independent chunking|Embedding multivariate, HMM and random graphs into three-variable models|
|marginalized|Recover original univariate parameters from composite block matrix|
|Binning and CDF recovery|Extending finite state tools to nonparametric distributions|

These are logical proofs. There are no finite-sample Monte Carlo results, nor is there a demonstration of how an estimator performs near the identification boundary.

## result does not cover the level

1. **Unknown number of categories**: The full text assumes that \(r\) is known.
2. **Finite sample estimation**: No convergence rate, standard error or sample size recommendations.
3. **Computation algorithm**: The uniqueness proof does not give a stable tensor recovery procedure.
4. **Near degeneration problem**: A bad set with measure 0 may still be numerically unstable near it.
5. **Model missetting**: When local independence is not established, the three-piece scale display may be wrong.
6. **CDM structure restored**: no Q matrix, attribute naming, item parameterization or attribute hierarchy.
7. **Minimum conditions**: Most results provide sufficient conditions and do not claim to be necessary everywhere.

## Requirements for subsequent empirical papers

When subsequent CDM papers cite this article as the basis for identification, they should continue to check:

- Whether the structured CDM parameter space meets the required full rank;
- How the Q matrix eliminates latent class label permutations;
- Whether all allowed attribute profiles are proportional;
- Estimating whether the algorithm can approach the theoretical unique solution under limited samples;
- Identify whether the parameter recovery near the condition is stable;
- Whether model comparison evaluates "identification" and "prediction/fitting" separately.

