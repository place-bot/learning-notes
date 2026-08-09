# Derivation of the conditional probability of a single \(q_{jk}\)

## Which students will be affected by flipping?

Fixed item \(j\) and attribute \(k\), set

\[
\eta_{ij,-k}
=
I(\alpha_{ih}\ge q_{jh},\ \forall h\ne k).
\]

only satisfaction

\[
\eta_{ij,-k}=1,\qquad
\alpha_{ik}=0
\]

For students, their ideal response will change with \(q_{jk}\):

- If \(q_{jk}=0\), then \(\eta_{ij}=1\);
- If \(q_{jk}=1\), then \(\eta_{ij}=0\).

The contributions of other students to the conditional likelihood ratio cancel.

## Two key counts

Defined among affected students

\[
a_0
=
\sum_i
I(\eta_{ij,-k}=1,\alpha_{ik}=0,Y_{ij}=0),
\]

\[
a_1
=
\sum_i
I(\eta_{ij,-k}=1,\alpha_{ik}=0,Y_{ij}=1).
\]

The original code of `abcounts()` returns these two numbers.

## Conditional likelihood ratio

When \(q_{jk}=0\), these students are considered to have all:

\[
L_0
\propto
s_j^{a_0}(1-s_j)^{a_1}.
\]

They are considered incomplete when \(q_{jk}=1\):

\[
L_1
\propto
(1-g_j)^{a_0}g_j^{a_1}.
\]

So

\[
\frac{L_0}{L_1}
=
\left(\frac{s_j}{1-g_j}\right)^{a_0}
\left(\frac{1-s_j}{g_j}\right)^{a_1}.
\]

## Conditional probability of \(q_{jk}=1\)

In the case where both 0 and 1 are legal and a priori the same:

\[
P(q_{jk}=1\mid-)
=
\frac{L_1}{L_0+L_1}
=
\frac{1}{
1+
\left(\frac{s_j}{1-g_j}\right)^{a_0}
\left(\frac{1-s_j}{g_j}\right)^{a_1}
}.
\]

Order

\[
\tau
=
a_0\log\frac{s_j}{1-g_j}
+
a_1\log\frac{1-s_j}{g_j},
\]

rule

\[
P(q_{jk}=1\mid-)
=
\frac{1}{1+e^\tau}.
\]

## Corresponds to C++ judgment expression

The code extracts \(u\sim U(0,1)\), and then determines

```cpp
log(1-u) - log(u) > tau
```

because

\[
\log\frac{1-u}{u}>\tau
\quad\Longleftrightarrow\quad
u<\frac{1}{1+e^\tau},
\]

So this judgment accurately implements Bernoulli conditional sampling.

## A numerical example

Set

\[
s_j=0.10,\qquad
g_j=0.20,\qquad
a_0=8,\qquad
a_1=2.
\]

rule

\[
\tau
=
8\log(0.1/0.8)
+
2\log(0.9/0.2)
\approx-13.63.
\]

Therefore

\[
P(q_{jk}=1\mid-)
\approx0.999999.
\]

Affected students mostly answered incorrectly, and the data strongly supports placing them in the incomplete group, which supports \(q_{jk}=1\).

## Legality precedes probability

If a certain value causes Q to leave \(\mathcal Q\), its conditional prior probability is 0. At this time, there is no need to calculate the likelihood, and the only legal value is directly retained.

[Next page: Posterior mode and column permutation of the entire Q](18-posterior-summary.md)
