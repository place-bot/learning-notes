#Hand Calculation: Conditional Probability and Perplexity

Assume vocabulary \(\{a,b,c\}\), and the current context obtains logits through the network:

\[
y=(1.2,\;0.3,\;-0.5).
\]

## 1. Softmax

\[
e^{1.2}\approx3.320,\quad
e^{0.3}\approx1.350,\quad
e^{-0.5}\approx0.607.
\]

\[
Z\approx5.277.
\]

\[
P(a)\approx0.629,\quad
P(b)\approx0.256,\quad
P(c)\approx0.115.
\]

The real next word is \(b\):

\[
L=-\log0.256\approx1.363.
\]

logits gradient:

\[
\frac{\partial L}{\partial y}
\approx(0.629,\;-0.744,\;0.115).
\]

It continues by updating the output layer, hidden layer, and context word embedding.

## 2. Perplexity

test set \(N\) tokens:

\[
\operatorname{PPL}
=
\exp\!\left(
-\frac1N\sum_t\log P(w_t\mid context_t)
\right).
\]

If the average NLL is 1.363:

\[
\operatorname{PPL}=e^{1.363}\approx3.91.
\]

It can be understood as an exponential scale of the model's average uncertainty; the lower, the better. The perplexity of different tokenization, vocabulary and OOV processing cannot be directly compared.

## 3. Vector generalization

If §cat§ is close to \(C(w)\) of §dog§, then the seen context containing cat can help the similar context of dog by sharing network parameters. This is the core path of the paper to combat the sparsity of discrete combinations.
