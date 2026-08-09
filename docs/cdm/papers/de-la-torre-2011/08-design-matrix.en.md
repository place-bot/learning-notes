# design matrix

## Matrix form

For item \(j\), the transformed success probabilities of all reduced modes are composed into a vector:

\[
h(\boldsymbol P_j)
=
\left(
h[P(\boldsymbol\alpha^*_{1j})],
\ldots,
h[P(\boldsymbol\alpha^*_{2^{K_j^*}j})]
\right)^\top.
\]

The model is written as

\[
h(\boldsymbol P_j)
=
M_j\boldsymbol\phi_j.
\]

Among them:

- \(M_j\)：design matrix；
- \(\boldsymbol\phi_j\): intercept, main effect and interaction effect;
- \(h\): identity, logit or log.

## Three-attribute saturation matrix

According to the pattern order of the paper

\[
000,100,010,001,110,101,011,111,
\]

The order of parameters is

\[
1,\alpha_1,\alpha_2,\alpha_3,
\alpha_1\alpha_2,
\alpha_1\alpha_3,
\alpha_2\alpha_3,
\alpha_1\alpha_2\alpha_3.
\]

The saturated design matrix is

\[
M_j^{(S)}
=
\begin{pmatrix}
1&0&0&0&0&0&0&0\\
1&1&0&0&0&0&0&0\\
1&0&1&0&0&0&0&0\\
1&0&0&1&0&0&0&0\\
1&1&1&0&1&0&0&0\\
1&1&0&1&0&1&0&0\\
1&0&1&1&0&0&1&0\\
1&1&1&1&1&1&1&1
\end{pmatrix}.
\]

Each column corresponds to a subset of attributes, and each row corresponds to a reduced attribute profile.

## Get parameters from probability

The saturation matrix is square and invertible. The paper is written in least squares form

\[
\widehat{\boldsymbol\phi}_j
=
\left[
(M_j^{(S)})^\top M_j^{(S)}
\right]^{-1}
(M_j^{(S)})^\top
h(\widehat{\boldsymbol P}_j).
\]

In the case of square matrix reversibility, it is equivalent to

\[
\widehat{\boldsymbol\phi}_j
=
(M_j^{(S)})^{-1}
h(\widehat{\boldsymbol P}_j).
\]

Substituting three types of \(h\) respectively, you can get

\[
\widehat{\boldsymbol\delta}_j,
\qquad
\widehat{\boldsymbol\lambda}_j,
\qquad
\widehat{\boldsymbol\nu}_j.
\]

## design matrix How to define a reduced model

Delete columns or merge groups to define different models.

The matrix of three-attribute DINA has only two columns:

\[
M_j^{(\mathrm{DINA})}
=
\begin{pmatrix}
1&0\\
1&0\\
1&0\\
1&0\\
1&0\\
1&0\\
1&0\\
1&1
\end{pmatrix}.
\]

Three-attribute DINO allows all modes except \(000\) to enter the second group:

\[
M_j^{(\mathrm{DINO})}
=
\begin{pmatrix}
1&0\\
1&1\\
1&1\\
1&1\\
1&1\\
1&1\\
1&1\\
1&1
\end{pmatrix}.
\]

A-CDM retains the first \(K_j^*+1\) columns, which are the intercept and main effect columns.

## The pattern order must be consistent

The design matrix, \(\boldsymbol P_j\), covariance matrix and constraint matrix must be in the same row order. Sequence errors usually do not trigger dimension errors, but result in completely wrong effect interpretations and Wald results.

The code implementation should also be saved:

- Reduction mode tag;
- design matrix row;
- success probability vector;
- covariance matrix row and column names.
