# Appendices: SLD, the Huynh extension, and disordered thresholds

## Appendix A: SLD from Ackerman-Spray transitions

Define

\[
\alpha^*_{ii'}=P^*(X_{i'}=1\mid X_i=0,\theta),
\qquad
\beta^*_{ii'}=P^*(X_{i'}=0\mid X_i=1,\theta),
\]

and set

\[
\alpha^*_{ii'}=\alpha P(X_{i'}=1\mid\theta),
\qquad
\beta^*_{ii'}=\beta P(X_{i'}=0\mid\theta).
\]

Total probability gives the Ackerman-Spray model. Setting
\(\pi_{LD}=1-\alpha=1-\beta\) yields the symmetric SLD mixture

\[
P^*(X_{i'}=1\mid\theta)
=(1-\pi_{LD})P(X_{i'}=1\mid\theta)
+\pi_{LD}P^*(X_i=1\mid\theta).
\]

## Appendix B: extending Huynh

For independent Rasch items and sum score \(R\),

\[
P(R=r\mid\theta)
=\frac{e^{r\theta}S_r}{\sum_{r'=0}^{J}e^{r'\theta}S_{r'}},
\tag{B.1}
\]

where

\[
S_r=\sum_{|\boldsymbol x|=r}e^{-\sum_ix_ib_i},
\qquad
\delta_r=\log\frac{S_{r-1}}{S_r}.
\]

For two items,

\[
\Delta\delta_2
=\log\frac{(e^{-b_1}+e^{-b_2})^2}{e^{-b_1-b_2}}
\ge\log4.
\tag{B.3}
\]

Thus \(\Delta\delta_2<\log4\) is incompatible with an independent-Rasch decomposition and signals
positive LD. However, probabilistic and deterministic LD alter the state sums and can also produce
well-separated steps. Hence

\[
\text{compressed/reversed steps}\Rightarrow\text{LD signal},
\qquad
\text{well-separated steps}\not\Rightarrow\text{proof of LI}.
\]

## Appendix C: disordered thresholds

In a power set of sufficiently separated independent items, PCM steps approximately follow item-
difficulty order. In a chain, prerequisite order and numerical difficulty order are distinct. The first
transition may be difficult and the second easy, producing \(\delta_2<\delta_1\) and an
underrepresented intermediate category.

Disordered thresholds may reveal problematic category definitions or scoring, but they are not a formal
failure of PCM. Their presence is diagnostically meaningful, not mathematically illegal.

