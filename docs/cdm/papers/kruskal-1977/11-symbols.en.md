# symbol table

## Three-way array and rank

|symbol|Dimension or type|meaning|
| --- | --- | --- |
| \(\mathbb F\) |number field|The original text focuses on real numbers; modern proofs cover more general domains|
| \(I,J,K\) |positive integer|The size of the three array directions|
| \(\mathcal X=(x_{ijk})\) | \(I\times J\times K\) |Three-way array or third-order tensor|
| \(i,j,k\) |indicator|position in three directions|
| \(\boldsymbol a,\boldsymbol b,\boldsymbol c\) |vector|three factors of a triad|
| \(\boldsymbol a\otimes\boldsymbol b\otimes\boldsymbol c\) |three-way array|Rank tensor, that is, triad in the original text|
| \(\operatorname{rank}(\mathcal X)\) |integer|The minimum number of triads required to represent \(\mathcal X\)|
| \(X_{i::}\) | \(J\times K\) |Fixed slab of first indicator|
| \(\dim_\ell(\mathcal X)\) |integer|The dimension of the space spanned by slabs in the \(\ell\) direction|
| \(X_{(\ell)}\) |matrix|Expand the \(\ell\) mode|

## Triple integral solution

|symbol|Dimensions|meaning|
| --- | ---: | --- |
| \(R\) |positive integer|number of components in decomposition|
| \(A\) | \(I\times R\) |first factor matrix|
| \(B\) | \(J\times R\) |second factor matrix|
| \(C\) | \(K\times R\) |The third factor matrix|
| \(\boldsymbol a_r\) | \(I\) |Column \(r\) of \(A\)|
| \(\boldsymbol b_r\) | \(J\) |Column \(r\) of \(B\)|
| \(\boldsymbol c_r\) | \(K\) |Column \(r\) of \(C\)|
| \([A,B,C]\) | \(I\times J\times K\) | \(\sum_r\boldsymbol a_r\otimes\boldsymbol b_r\otimes\boldsymbol c_r\) |
| \(\odot\) |Operation|Khatri--Rao product by column|

## Uniqueness

|symbol|meaning|
| --- | --- |
| \(k_A,k_B,k_C\) |Column Kruskal rank of three factor matrix|
| \(P\) |\(R\times R\) common permutation matrix|
| \(\Lambda,M,N\) |Reversible diagonal scaling matrix|
| \(\lambda_r,\mu_r,\nu_r\) |Scaling of the \(r\) component in three directions|
| \(\lambda_r\mu_r\nu_r=1\) |Scaling cancels out conditions|
| \(a_i=R-k_{M_i}\) |\(k\)-rank defect count in Rhodes proof|
| \(\Pi_i\) |Eliminate the projection of the specified column space in the \(i\) direction|
| \(S_i\) |Matrix slice obtained by fixing the coordinates in the third direction|

## CDM interface

|symbol|meaning|
| --- | --- |
| \(\mathcal A\) |The set of potential attribute profiles allowed|
| \(R=|\mathcal A|\) |Number of potential components or attribute profiles|
| \(\boldsymbol\alpha_r\) |attribute profile \(r\)|
| \(\pi_r\) |The overall proportion of the \(r\) attribute profile|
| \(\mathcal J_t\) |The \(t\) item block, \(t=1,2,3\)|
| \(M_t\) |Class conditional response pattern probability matrix of block \(t\)|
| \(\mathcal P\) |Overall joint probability array for three block reaction patterns|
| \(Q\) |item—attribute relationship matrix; responsible for connecting potential components to cognitive labels|

## Mark direction check

The topic of this article follows the CP literature and places the components in the columns of the factor matrix:

\[
A\in\mathbb F^{I\times R}.
\]

Allman's (2009) note on latent classes puts categories in rows:

\[
M\in\mathbb R^{R\times\kappa}.
\]

The two correspond through transposition. If I write a follow-up article

\[
\operatorname{rank}_K(M),
\]

You need to first check whether the author defines row Kruskal rank or column Kruskal rank.
