#Objective function and three estimators

## Parameters are known

\[
S_{\boldsymbol c,\boldsymbol g,\boldsymbol p}(Q)
=
\left\|
T_{\boldsymbol c,\boldsymbol g}(Q)\boldsymbol p
-\boldsymbol\beta
\right\|_2.
\tag{14}
\]

The original text uses Euclidean distance. When the parameters and Q are correct,

\[
S_{\boldsymbol c,\boldsymbol g,\boldsymbol p}(Q)\to0.
\]

The natural estimator is

\[
\widehat Q
=
\arg\inf_{Q'}S_{\boldsymbol c,\boldsymbol g,\boldsymbol p}(Q').
\]

## Unknown parameters: joint profile

\[
S(Q')
=
\inf_{\boldsymbol c,\boldsymbol g,\boldsymbol p}
S_{\boldsymbol c,\boldsymbol g,\boldsymbol p}(Q'),
\tag{15}
\]

The constraint is

\[
c_j,g_j,p_{\boldsymbol\alpha}\in[0,1],
\qquad
\sum_{\boldsymbol\alpha}p_{\boldsymbol\alpha}=1.
\]

then

\[
\widehat Q=\arg\inf_{Q'}S(Q').
\tag{16}
\]

When \((Q',\boldsymbol c,\boldsymbol g)\) is fixed, the optimization of \(\boldsymbol p\) is quadratic programming with simplex constraints. Joint optimization for \(\boldsymbol c,\boldsymbol g\) is more complex.

## Unknown parameters: MLE insert

For each candidate \(Q'\), first use DINA marginal likelihood to get

\[
\widehat{\boldsymbol c}(Q'),
\quad
\widehat{\boldsymbol g}(Q'),
\quad
\widehat{\boldsymbol p}(Q').
\]

redefine

\[
\widehat S(Q')
=
S_{
\widehat{\boldsymbol c}(Q'),
\widehat{\boldsymbol g}(Q'),
\widehat{\boldsymbol p}(Q')
}(Q').
\tag{17}
\]

eventually

\[
\widetilde Q
=
\arg\inf_{Q'}\widehat S(Q').
\tag{18}
\]

The calculation section of Algorithm 1 clearly adopts the route of equation (17)--(18).

## Division of labor between likelihood and S

|object|Purpose|
| --- | --- |
| DINA marginal likelihood |Estimate \(\widehat c,\widehat g,\widehat p\) after fixing candidate Q|
| \(\widehat S(Q)\) |Compares how well candidate Q matches selected joint moments|

This means that every time a new Q is evaluated, the nuisance parameters are refitted. If we only fix the same group of \((\widehat c,\widehat g,\widehat p)\) and compare all candidates, we will get another approximate algorithm.

## Why write \(\inf\)

The space of Q is a finite discrete set, and under suitable conditions it can be written \(\min\). The original text maintains the notation \(\inf\) in order to express profile optimization of continuous parameters simultaneously.

## An important risk

Wrong Q may also be obtained by rescaling \(c,g,p\) to obtain a very small \(S\). The core question to be answered in the discussion of identifiability is exactly this: whether different Qs are likely to generate the same observable distribution or the same set of moments.
