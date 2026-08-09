# Negative transfer and reweighted hand calculation

## 1. Negative migration

If the target performance after using source knowledge is lower than without migration:

\[
R_T(f_{\text{transfer}})
>
R_T(f_{\text{target-only}}),
\]

A negative transfer occurs. It can be caused by a weak source/target relationship, different label meanings, or distribution bias.

## 2. Reweighting under Covariate shift

If

\[
P_S(Y\mid X)=P_T(Y\mid X),
\qquad
P_S(X)\ne P_T(X),
\]

The target risk can be written as

\[
\begin{aligned}
R_T(f)
&=\mathbb E_{(X,Y)\sim P_T}[\ell(f(X),Y)]\\
&=\mathbb E_{(X,Y)\sim P_S}
\left[
\frac{P_T(X)}{P_S(X)}
\ell(f(X),Y)
\right].
\end{aligned}
\]

weight

\[
w(x)=P_T(x)/P_S(x)
\]

Let source samples that are more like the target domain contribute more.

## 3. Numerical examples

There are two types of input frequencies in the source domain:

\[
P_S(a)=0.8,\quad P_S(b)=0.2.
\]

Target domain:

\[
P_T(a)=0.2,\quad P_T(b)=0.8.
\]

Weight:

\[
w(a)=0.25,\qquad w(b)=4.
\]

Ordinary source training will be dominated by \(a\); after reweighting, the \(b\) sample contribution is amplified and closer to the target distribution.

## 4. Inspiration for pretraining models

- The large scale of general corpus does not guarantee matching with target domains such as education and medical care;
- Continuing pretraining in the field can reduce the \(P(X)\) difference;
- The downstream validation set is used to determine whether the transfer is valid;
- You cannot only compare the source task loss;
- Check for negative migration when data and tag definitions change.

## 5. Boundary of Survey

This article is a review of classification and methods. It does not propose a BERT-style algorithm, nor does it cover foundation model, prompting or PEFT. What it provides is a conceptual coordinate system.
