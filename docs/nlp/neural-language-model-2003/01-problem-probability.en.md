# language model, curse of dimensionality and distributed representation

## 1. language model

\[
P(w_1,\ldots,w_T)
=
\prod_{t=1}^{T}
P(w_t\mid w_{<t}).
\]

n-grams are approximated with finite context:

\[
P(w_t\mid w_{<t})
\approx
P(w_t\mid w_{t-n+1:t-1}).
\]

## 2. Curse of dimensionality

The vocabulary size is \(|V|\), and there are \(|V|^n\) discrete combinations of length \(n\). Most combinations do not appear in training, and counting models rely on back-off, interpolation, and category smoothing.

## 3. Distributed representation

Learn for every word

\[
C(w)\in\mathbb R^m.
\]

Similar words can be nearby in vector space. The training sentences shape both word vectors and conditional probability functions, so that an unseen sequence can also obtain a reasonable probability because its constituent words are similar to the seen sequence.

## 4. Three joint learning parts

The paper clearly lists:

1. Mapping of words to vectors \(C\);
2. Use the context vector to predict the probability function \(g\) of the next word;
3. Optimize the parameters of \(C\) and \(g\) at the same time.

This makes embedding part of the task training rather than a priori handcrafted categories.

## 5. With Word2Vec, BERT

- NPLM: word vector serves next-word likelihood;
- Word2Vec: simplify the target and network, expand the training scale;
- BERT: Learning contextual token representation using Transformer and MLM.

All three make use of distribution assumptions, but the output representation and pretraining goals are different.
