# DINA, DINO and A-CDM

## DINA

The success probability of DINA is

\[
P(\boldsymbol\alpha^*_{lj})
=
\begin{cases}
g_j,
&\boldsymbol\alpha^*_{lj}\prec\boldsymbol 1,\\
1-s_j,
&\boldsymbol\alpha^*_{lj}=\boldsymbol 1.
\end{cases}
\]

In identity-link G-DINA, only keep

\[
\delta_{j0}
\quad\text{and}\quad
\delta_{j12\cdots K_j^*}.
\]

Therefore

\[
g_j=\delta_{j0},
\qquad
1-s_j
=
\delta_{j0}
+\delta_{j12\cdots K_j^*}.
\]

DINA expresses a strict conjunctive process: the probability jump occurs only when all attributes are present at the same time.

## DINO

The success probability of DINO is

\[
P(\boldsymbol\alpha^*_{lj})
=
\begin{cases}
g'_j,
&\boldsymbol\alpha^*_{lj}=\boldsymbol 0,\\
1-s'_j,
&\boldsymbol\alpha^*_{lj}\neq\boldsymbol 0.
\end{cases}
\]

It expresses the disjunctive process: master any required attribute to enter the high-success group.

The identity-link parameter must satisfy the alternating sign and same absolute value constraints. When there are two attributes:

\[
\delta_1=\delta_2=-\delta_{12}.
\]

So

\[
P(10)=P(01)=P(11).
\]

## A-CDM

Let all interaction effects be zero:

\[
P(\boldsymbol\alpha^*_{lj})
=
\delta_{j0}
+\sum_{k=1}^{K_j^*}\delta_{jk}\alpha_{lk}.
\]

Each attribute contributes a fixed increment on the probability scale, so the number of parameters is

\[
K_j^*+1.
\]

When there are two attributes, A-CDM requires

\[
P(11)
=
P(10)+P(01)-P(00).
\]

This equation was later used directly in the paper's clinical data interpretation.

## Geometric constraints of the three models

Suppose the four probabilities of the two-attribute problem are

\[
\boldsymbol P_j=
\left(P_{00},P_{10},P_{01},P_{11}\right)^\top.
\]

Then:

|model|Equality constraints|free parameters|
| --- | --- | ---: |
| G-DINA |None| 4 |
| DINA | \(P_{00}=P_{10}=P_{01}\) | 2 |
| DINO | \(P_{10}=P_{01}=P_{11}\) | 2 |
| A-CDM | \(P_{11}-P_{10}-P_{01}+P_{00}=0\) | 3 |

The Wald test tests whether the estimated \(\boldsymbol P_j\) distance from these constraints is significant.

## Interpretation boundaries for guessing and slipping

The paper continues to use \(g,s\) as a name for easy memory, and reminds:

- High \(g\) may come from Q matrix omission;
- High \(g\) may come from alternative strategies;
- High \(s\) may result from carelessness, item ambiguity or additional capability requirements.

They are response probability parameters, and the students' real cognitive process cannot be restored by name alone.
