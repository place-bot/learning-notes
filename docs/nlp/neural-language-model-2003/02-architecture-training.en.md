# Network structure, formulas and parameters

## 1. Context vector

Use the first \(n-1\) words to splice embedding:

\[
x=
[C(w_{t-1});C(w_{t-2});\ldots;C(w_{t-n+1})].
\]

## 2. Hidden layer

\[
h=\tanh(d+Hx).
\]

## 3. Output and direct connection

\[
y=b+Wx+Uh.
\]

\(Wx\) is an optional input-to-output direct connection, and \(Uh\) is a nonlinear hidden path. For each candidate word \(i\):

\[
P(w_t=i\mid context)
=
\frac{\exp(y_i)}
{\sum_{j\in V}\exp(y_j)}.
\]

## 4. Parameters

- \(C\): word embedding table;
- \(H,d\): context to hidden layer;
- \(U,b\): hidden to vocabulary output;
- \(W\): Optional direct connection.

The output matrix grows with \(|V|\), which is the main parameter and calculation bottleneck.

## 5. Maximum likelihood

\[
\max_\theta
\sum_t
\log P_\theta(w_t\mid w_{t-n+1:t-1})
-R(\theta).
\]

The paper uses stochastic gradient updates, and word embedding only updates the rows involved in the current context; output normalization still requires traversing the entire vocabulary.

## 6. Computational Challenges

The AP News model training took about three weeks and 40 CPUs for 5 epochs. The paper also discusses parallel computing and subsequent energy/sampling directions, showing that full vocabulary softmax was very expensive at the time.

## 7. The role of direct connection

The direct path quickly learns approximately linear n-gram patterns, and the hidden layers learn nonlinear shared structures. In Brown's experiment, the convergence was slower if the direct connection was removed, but some configurations generalized slightly better, and the result was not enough to conclude that the direct connection must be effective.
