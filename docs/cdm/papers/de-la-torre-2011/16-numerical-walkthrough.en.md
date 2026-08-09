# Decompose the value of two attribute items

## Saturation probability

Assuming that a certain question requires two attributes, the estimated success probability is

\[
\begin{aligned}
P(00)&=0.20,\\
P(10)&=0.35,\\
P(01)&=0.50,\\
P(11)&=0.80.
\end{aligned}
\]

in order

\[
00,10,01,11,
\]

Yes

\[
\boldsymbol P
=
\begin{pmatrix}
0.20\\0.35\\0.50\\0.80
\end{pmatrix},
\qquad
M^{(S)}
=
\begin{pmatrix}
1&0&0&0\\
1&1&0&0\\
1&0&1&0\\
1&1&1&1
\end{pmatrix}.
\]

## G-DINA EFFECT

\[
\boldsymbol\delta
=(M^{(S)})^{-1}\boldsymbol P.
\]

Calculate item by item:

\[
\begin{aligned}
\delta_0&=0.20,\\
\delta_1&=0.35-0.20=0.15,\\
\delta_2&=0.50-0.20=0.30,\\
\delta_{12}
&=0.80-0.35-0.50+0.20\\
&=0.15.
\end{aligned}
\]

The main effect of the second attribute alone is greater than the first; combined mastery also brings an additional 0.15 improvement.

## A-CDM Constraints

A-CDM requirements

\[
\delta_{12}=0.
\]

If the first three saturation effects are retained directly, it predicts

\[
P_{\mathrm{A-CDM}}(11)
=
0.20+0.15+0.30
=
0.65.
\]

The actual saturation probability is 0.80 and the constrained residual is

\[
0.80-0.65=0.15.
\]

The Wald test compares this residual to its standard error.

## Posterior headcount weight

Assume that the expected number of people in the four reduced groups is

\[
(100,80,60,40),
\]

The expected number of correct answers is

\[
(20,28,30,32).
\]

The probability of each group is exactly

\[
\left(
\frac{20}{100},
\frac{28}{80},
\frac{30}{60},
\frac{32}{40}
\right)
=(0.20,0.35,0.50,0.80).
\]

### DINA weighted estimate

DINA merges the first three non-full control groups:

\[
\widehat g
=
\frac{20+28+30}{100+80+60}
=
0.325.
\]

Full mastery group gives

\[
1-\widehat s
=
\frac{32}{40}
=
0.80.
\]

### DINO weighted estimate

DINO reserves \(00\) as the low group and merges the remaining three groups:

\[
\widehat g'
=
\frac{20}{100}
=
0.20,
\]

\[
1-\widehat s'
=
\frac{28+30+32}{80+60+40}
=
0.50.
\]

## A-CDM weighted least squares

Use

\[
M^{(A)}
=
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&0&1\\
1&1&1
\end{pmatrix}
\]

and

\[
W=\operatorname{diag}(100,80,60,40),
\]

get

\[
\widehat{\boldsymbol\delta}^{(A)}
\approx
\begin{pmatrix}
0.1766\\
0.2026\\
0.3623
\end{pmatrix}.
\]

The fitting probability is

\[
(0.1766,0.3792,0.5390,0.7416).
\]

It distributes the error caused by the additive constraint among the four modes, giving greater weight to the mode that expects more people.

## The core of this teardown display

The same set of saturation probabilities can be:

- Transformed into main effect and interaction effect;
- Merge potential groups by DINA or DINO;
- Use A-CDM for weighted reduction;
- Use the Wald test to determine whether the reduced residuals are significant.

These four steps correspond to the probability layer, parameter layer, constraint layer and inspection layer of G-DINA framework.
