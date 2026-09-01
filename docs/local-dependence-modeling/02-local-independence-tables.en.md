# Local independence and contingency tables

## Strong and weak LI

For binary items \(Q=\{q_1,\ldots,q_J\}\), strong LI is

\[
P(\boldsymbol X=\boldsymbol x\mid\Gamma,\theta)
=\prod_{i=1}^{J}P(X_i=x_i\mid\Gamma_i,\theta).
\tag{1}
\]

The 4PL item response function is

\[
P(X_i=1\mid\theta)
=c_i+(1-c_i-d_i)
\frac{e^{a_i(\theta-b_i)}}{1+e^{a_i(\theta-b_i)}}.
\tag{2}
\]

Here \(a_i,b_i,c_i,d_i\) are discrimination, difficulty, guessing, and slipping. Setting
\(d_i=0\) gives 3PL, additionally setting \(c_i=0\) gives 2PL, and \(a_i=1\) gives Rasch.

Weak or pairwise LI only requires

\[
\operatorname{cov}(X_i,X_{i'}\mid\theta)=0.
\tag{3}
\]

Integrating conditional covariance over \(f(\theta)\) gives the discrepancy between observed and LI-
expected cells, which underlies many pairwise LD diagnostics.

## Two key incomplete tables

The paper orders cells as

\[
\begin{pmatrix}p_{00}&p_{01}\\p_{10}&p_{11}\end{pmatrix}.
\]

Table A is a prerequisite pattern:

\[
q_1\to q_2,
\qquad
\begin{pmatrix}p_{00}&0\\p_{10}&p_{11}\end{pmatrix},
\qquad
\mathcal K_A=\{00,10,11\}.
\]

Table B represents jointly mastered or failed items:

\[
q_1\leftrightarrow q_2,
\qquad
\begin{pmatrix}p_{00}&0\\0&p_{11}\end{pmatrix},
\qquad
\mathcal K_B=\{00,11\}.
\]

KST calls the latter equally informative items: they distinguish the same latent states, although their
IRT difficulties need not be identical.

## How LI approximates the same patterns

With very large 2PL slopes, response curves become step functions. If \(b_2>b_1\), ability regions
produce mostly \(00,10,11\) and approximate Table A. If \(b_1=b_2\), the two items jump together
and approximate Table B. This generally requires extreme slopes or difficulty gaps and may distort
other cells, motivating direct structural modeling.

For example, under \(\theta\sim N(0,1)\):

| Model | Parameters | Table |
| --- | --- | --- |
| LI-1 | \(a_1=a_2=1,b_1=b_2=0\) | \(\begin{pmatrix}.293&.207\\.207&.293\end{pmatrix}\) |
| LI-3 | \(a_1=a_2=1,b_1=0,b_2=4\) | \(\begin{pmatrix}.491&.009\\.481&.019\end{pmatrix}\) |
| LI-4 | \(a_1=a_2=10,b_1=b_2=0\) | \(\begin{pmatrix}.461&.039\\.039&.461\end{pmatrix}\) |

