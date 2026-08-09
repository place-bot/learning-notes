# Questions and historical locations

## Start with matrix decomposition

A matrix with rank \(R\) can be written as

\[
X=AB^\mathsf T
=\sum_{r=1}^{R}\boldsymbol a_r\boldsymbol b_r^\mathsf T.
\]

Given any invertible matrix \(Q\), and

\[
X
=AQQ^{-1}B^\mathsf T
=(AQ)(BQ^{-\mathsf T})^\mathsf T.
\]

So the rank-one components in a matrix can generally be blended by any reversible linear transformation. Even if \(X\) is fully known, \(\boldsymbol a_r,\boldsymbol b_r\) alone may not be recoverable.

## Constraints brought by the third direction

The three-way array is written as

\[
x_{ijk}
=\sum_{r=1}^{R}
a_{ir}b_{jr}c_{kr}.
\]

The same ingredient number \(r\) must run through three directions at the same time:

\[
\boldsymbol a_r
\longleftrightarrow
\boldsymbol b_r
\longleftrightarrow
\boldsymbol c_r.
\]

If you try to mix the columns of \(A\) and \(B\) with a general invertible matrix, you also want the third factor \(C\) to maintain a component-wise multiplication structure. This additional compatibility condition significantly compresses the possible transformations.

Kruskal's core discovery is that as long as the columns of the three factor matrices have a strong enough property of "any number of columns are still independent", generally reversible mixtures will be eliminated, and only:

- Make the same substitution for \(R\) components;
- Scale the same component in three directions, and the product of the three scaling amounts is 1.

## Three logical questions in the paper

### Question 1: How many triads are needed at least?

\[
\operatorname{rank}(\mathcal X)
=
\min\left\{
R:
\mathcal X
=\sum_{r=1}^{R}
\boldsymbol a_r\otimes\boldsymbol b_r\otimes\boldsymbol c_r
\right\}.
\]

This is a tensor rank problem. The paper establishes several lower bounds to prove that a given decomposition can no longer be shortened.

### Question 2: Is the decomposition of a given length unique?

Even if a certain decomposition happens to use the fewest \(R\) terms, there may be another set of three factor matrices that yield the same array. Comparison of uniqueness issues

\[
[A,B,C]=[\bar A,\bar B,\bar C].
\]

### Question 3: Can statistical parameters be identified?

In the latent class model, the three factor matrices can be composed of the conditional distribution of three groups of observed variables under each latent class. If the triple integral decomposition is essentially unique and probability normalization is added, the category proportion and conditional distribution can be restored, allowing category label exchange.

This step also requires the structure of the statistical model itself:

- Can factor columns be interpreted as probability vectors;
- How the scaling is fixed by the constraint that the columns sum to 1;
- How to connect the replaced latent class to the attribute profile;
- Whether Q-matrix or cognitive diagnostic parameterization also introduces new equivalence relations.

Therefore, Kruskal's theorem provides the algebraic core, and complete CDM identifiability requires subsequent bridging.

## Historical location of 1977 paper

The paper ties together three areas:

|field|Objects in three-way array|The role provided by the paper|
| --- | --- | --- |
|multilinear algebra|sum of triad|Rank definition, rank lower bound and decomposition uniqueness|
|arithmetic complexity|bilinear calculation scheme|Use tensor rank to characterize the number of multiplications required|
|Statistics and Psychometrics|Three-way data, latent structure, or INDSCAL class model|Explain when the factor can be determined from the population array|

Later literature on CANDECOMP/PARAFAC, latent class identification, phylogenetic models, and CDM identification continued to reuse this uniqueness theorem.

## Four words that are easily confused

|word|Question content|
| --- | --- |
| matrix rank |The column space dimensions of a matrix|
| tensor rank |What is the minimum number of rank quantities required for a three-way array?|
| Kruskal rank |A factor matrix is guaranteed to be independent no matter how many columns it takes.|
| identifiability |Whether the observed distribution can uniquely determine the statistical parameters, allowing for equivalence relationships declared in advance|

The most important reading discipline throughout the text is to keep these four concepts separate.
