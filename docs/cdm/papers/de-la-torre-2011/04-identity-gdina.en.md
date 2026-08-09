# identity-link G-DINA

## Saturation reaction function

For item \(j\) that requires \(K_j^*\) attributes, G-DINA is written

\[
\begin{aligned}
P(\boldsymbol\alpha^*_{lj})
=\;&
\delta_{j0}
+\sum_{k=1}^{K_j^*}\delta_{jk}\alpha_{lk}\\
&+
\sum_{k<k'}\delta_{jkk'}
\alpha_{lk}\alpha_{lk'}
+\cdots\\
&+
\delta_{j12\cdots K_j^*}
\prod_{k=1}^{K_j^*}\alpha_{lk}.
\end{aligned}
\]

This is equivalent to performing a complete main effect and interaction decomposition on a binary attribute cube.

## Two attributes item

When \(K_j^*=2\),

\[
P(\alpha_1,\alpha_2)
=
\delta_0
+\delta_1\alpha_1
+\delta_2\alpha_2
+\delta_{12}\alpha_1\alpha_2.
\]

The probabilities of the four modes are

\[
\begin{aligned}
P(00)&=\delta_0,\\
P(10)&=\delta_0+\delta_1,\\
P(01)&=\delta_0+\delta_2,\\
P(11)&=\delta_0+\delta_1+\delta_2+\delta_{12}.
\end{aligned}
\]

Solved in reverse

\[
\begin{aligned}
\delta_0&=P(00),\\
\delta_1&=P(10)-P(00),\\
\delta_2&=P(01)-P(00),\\
\delta_{12}
&=
P(11)-P(10)-P(01)+P(00).
\end{aligned}
\]

\(\delta_{12}\) measures the joint mastery beyond the sum of two separate increments.

## Three attributes item

When \(K_j^*=3\), there are eight parameters:

\[
\delta_0,
\delta_1,\delta_2,\delta_3,
\delta_{12},\delta_{13},\delta_{23},
\delta_{123}.
\]

Third-order interactions can be obtained from the inclusion-exclusion form:

\[
\begin{aligned}
\delta_{123}
=\;&P(111)
-P(110)-P(101)-P(011)\\
&+P(100)+P(010)+P(001)
-P(000).
\end{aligned}
\]

## Parameter symbols

The typical explanation given in the paper is:

- \(\delta_0\geq 0\)；
- The main effect is usually non-negative;
- The interaction effect can be positive or negative.

Negative interactions do not automatically indicate model anomalies. It means that the joint effect is less than the simple sum of lower-order effects. For example, when two attributes each bring significant improvement, after the probability of success approaches the upper bound, the additional increment of the combination of the two may be negative.

## Parameter cost of saturated model

The number of parameters for each question depends on \(K_j^*\):

| \(K_j^*\) |Probability of success/number of parameters|
| ---: | ---: |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

The flexibility of G-DINA grows exponentially with the number of properties required. When the sample size is limited, the number of posteriors for some reduction models is very small, and the probability estimate and standard error will quickly become unstable.

## Direct relationship with DINA

DINA handle

\[
P(000),P(100),\ldots
\]

The probability constraints except for the full control group are the same \(g_j\). G-DINA allows these partial mastery groups to be presented at different levels, thus revealing:

- Which attribute contributes more;
- Whether there is compensation;
- Whether necessary joint control exists;
- Whether DINA's second set of compression is too strong.
