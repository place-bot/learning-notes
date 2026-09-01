# Structures, states, and processes

## Decomposing the 4PL

The 4PL can be written as

\[
P(X_i=1\mid\theta)
=c_i\pi(K_i=0\mid\theta)
+(1-d_i)\pi(K_i=1\mid\theta),
\tag{6}
\]

with

\[
\operatorname{logit}\pi(K_i=1\mid\theta)=a_i(\theta-b_i).
\tag{7}
\]

This separates a \(p\)-process \(\theta\to K_i\), describing mastery, from a \(g\)-process
\(K_i\to X_i\), describing guessing and slipping.

## Structures

For a nonempty domain \(D\), a structure is \((D,\mathcal Y)\) with

\[
\{\varnothing,D\}\subseteq\mathcal Y\subseteq2^D.
\]

Each \(Y\in\mathcal Y\) is a state. A chain retains cumulative states; a power set retains every
combination; an arbitrary structure can encode branches and exclusions.

Map a state to a binary vector by

\[
Y_i=1\Longleftrightarrow d_i\in Y.
\]

A probability distribution \(P(Y)\) turns the structure into a contingency table. The power set gives a
complete table; a proper subset gives structural zeros.

Structures can represent item mastery \((Q,\mathcal K,\pi)\), skill states
\((S,\mathcal C,\nu)\), cumulative categories, or--after extending a finite chain to an uncountable
one--a continuous trait.

## Processes

For discrete states,

\[
P(X)=\sum_{Y\in\mathcal Y}P(X\mid Y)P(Y).
\tag{8}
\]

For a continuous trait,

\[
P(X)=\int P(X\mid\theta)f(\theta)d\theta.
\tag{9}
\]

A \(p\)-process maps competence to mastery; a \(g\)-process maps mastery to observed response:

\[
\Theta\xrightarrow{p}K\xrightarrow{g}\boldsymbol X.
\]

## Factorization versus reparameterization

Factorization asserts a product or conditional order, such as

\[
P(X_1,X_2\mid\theta)=P(X_1\mid\theta)P(X_2\mid X_1,\theta).
\]

Reparameterization supplies a link and kernel,

\[
\ell[P(X\mid Y)]=f(X,Y).
\tag{22}
\]

The first specifies conditional structure; the second specifies functional coordinates. A model can use
both.

