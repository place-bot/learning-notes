# Proof of the three main theorems

## Theorem 2.4

### True candidate

Established sample by sample without noise

\[
\boldsymbol\alpha=T(Q)\widehat{\boldsymbol p}.
\]

Therefore

\[
S(Q)=0
\]

The probability is 1.

### Any error candidate

For \(Q'\not\sim Q\), Corollary 6.5 gives

\[
T(Q)\boldsymbol p^*
\notin\mathcal C(T(Q')).
\]

So \(\delta_{Q'}>0\) exists. And because

\[
\boldsymbol\alpha
=T(Q)\widehat{\boldsymbol p}
\longrightarrow
T(Q)\boldsymbol p^*,
\]

Yes

\[
\Pr\!\left[
\inf_{\boldsymbol p}
\|T(Q')\boldsymbol p-\boldsymbol\alpha\|_2
>\delta_{Q'}
\right]
\longrightarrow1.
\]

### Exclude all error candidates at the same time

There are a limited number of binary Qs, so they can be true for all error candidates simultaneously. The global minimizer ends up belonging to \([Q]\).

### \(\boldsymbol p\) consistent

Proposition 6.1 Make

\[
T(Q)\boldsymbol p=\boldsymbol\alpha
\]

The only solution. On event \(\widehat Q=Q\),

\[
\widetilde{\boldsymbol p}=\widehat{\boldsymbol p}.
\]

From the law of large numbers we get \(\widetilde{\boldsymbol p}\to\boldsymbol p^*\).

## Theorem 3.1

### True candidate loss tends to 0

Local independence and the law of large numbers give

\[
\left\|
T_{c,g}(Q)\boldsymbol p^*
+p_0^*\boldsymbol g_{\mathrm{joint}}
-\boldsymbol\alpha
\right\|_2
\overset{\text{a.s.}}{\longrightarrow}0.
\]

So

\[
S_{c,g}(Q)\overset{\text{a.s.}}{\longrightarrow}0.
\]

### There is a uniform interval between error candidates

Empirical augmented moment convergence:

\[
\begin{pmatrix}\boldsymbol\alpha\\1\end{pmatrix}
\longrightarrow
\widetilde T_{c,g}(Q)\boldsymbol p_0^*.
\]

Proposition 6.6 states that the right-hand side does not belong to any candidate column space for error \(Q'\). The distance to each \(\boldsymbol c'\) is recorded as \(\delta(\boldsymbol c')\). Continuity and compactness give

\[
\delta
=
\inf_{\boldsymbol c'\in[0,1]^m}
\delta(\boldsymbol c')
>0.
\]

After the empirical moment is close enough to the overall moment, the optimal loss of the wrong Q is greater than \(\delta/2\), and the loss of the true Q is close to 0.

### \(\boldsymbol p\) consistent

Proposition 6.6 also proves

\[
\widetilde T_{c,g}(Q)
\]

Full rank. After the Q equivalence class is restored, the attribute distribution solution of the augmented linear equation is unique, so the estimated distribution converges to \(\boldsymbol p^*\).

## Theorem 4.2

### The combination \(c\) under true Q is estimated to make the loss tend to 0

The components satisfying (4.2) are consistently estimated by Proposition 4.1. The remaining components are processed through profile minimization of Equation (4.1). The objective function is continuous with respect to \(\boldsymbol c\), so

\[
\inf_{\boldsymbol p_0}
\left\|
\widetilde T_{\widehat c(Q,g),g}(Q)\boldsymbol p_0
-
\begin{pmatrix}\boldsymbol\alpha\\1\end{pmatrix}
\right\|_2
\overset{p}{\longrightarrow}0.
\]

### Error Q still keeps distance

The separation of Proposition 6.6 is for any

\[
\boldsymbol c'\in[0,1]^m
\]

holds, thus including \(\widehat{\boldsymbol c}(Q',g)\), which was chosen by the erroneous candidate himself. Q is consistent by following the compact set argument of Theorem 3.1.

### Attribute distribution part

If

\[
\widetilde{\boldsymbol c}(Q,g)
\overset{p}{\longrightarrow}\boldsymbol c,
\]

The combined estimate \(\widehat{\boldsymbol c}(Q,g)\) is also consistent. Combined with Q-consistency and augmented matrix full column rank, we derive

\[
\widetilde{\boldsymbol p}_{\widehat c}(g)
\overset{p}{\longrightarrow}
\boldsymbol p^*.
\]

## Statistical template shared by three proofs

\[
\text{Empirical moment convergence}
\quad+\quad
\text{Error model positive distance}
\quad+\quad
\text{Candidate space is limited}
\]

\[
\Longrightarrow
\Pr(\widehat Q\sim Q)\to1.
\]

The difference between noiseless, known parameters and unknown \(c\) focuses on two points:

- How to prove that the optimal loss of true Q tends to 0;
- How to construct column space separation suitable for the current noise structure.

[Next Page: Appendix Proof and C5](20-appendix-and-c5.md)
