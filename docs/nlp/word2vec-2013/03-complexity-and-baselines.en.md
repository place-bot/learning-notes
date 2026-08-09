# Computational complexity and neural language model baseline

## 1. Unified cost framework for papers

The paper uses equation (1) to compare different architectures:

\[
O=E\times T\times Q.
\tag{1}
\]

Here \(O\) represents the approximation of the total training calculation amount. The three factors are:

|symbol|meaning|enlarged effect|
|---|---|---|
| \(E\) |Number of training epochs|Repeat processing of the same corpus more times|
| \(T\) |Number of training tokens per epoch|use more text|
| \(Q\) |The number of parameters accessed or updated per training position|Determined by model structure|

Paper reports commonly report \(E\) between 3–50, and \(T\) can reach one billion. If \(Q\) is large, increasing the corpus and vector dimensions will quickly exhaust the budget.

The \(Q\) here is the calculation agent amount implemented at that time. It omits constants, memory accesses, parallel communication, and hardware differences and is suitable for comparing orders of magnitude for major matrix multiplications.

## 2. Feedforward neural network language model

### 2.1 Structure

Feedforward NNLM predicts the current word using the previous \(N\) words:

```text
N one-hot words
      │ Shared embedding matrix
      ▼
Splicing projection layer, dimension N×D
      │Dense matrix
      ▼
Nonlinear hidden layer, dimension H
      │
      ▼
Class V output probability
```

Input the lookup table to generate \(N\) \(D\)-dimensional vectors, which after splicing are \(ND\)-dimensional. The weight matrix size from the projection layer to the hidden layer is \(ND\times H\), and the size from the hidden layer to the output layer is \(H\times V\).

### 2.2 Complexity

Thesis formula (2) is

\[
Q_{\mathrm{NNLM}}
=ND+NDH+HV.
\tag{2}
\]

Three meanings:

1. \(ND\): Read \(N\) word vectors;
2. \(NDH\): Dense transformation from projection layer to hidden layer;
3. \(HV\): Calculate the output score for each word in vocabulary.

Under full softmax, \(HV\) tends to be the largest. hierarchical softmax reduces it approximately to

\[
H\log_2V.
\]

At this point \(NDH\) usually becomes the main cost.

## 3. Recurrent neural network language model

### 3.1 Structure

RNNLM uses recursive hidden states to save history:

\[
\mathbf h_t
=f(W_{xh}\mathbf x_t+W_{hh}\mathbf h_{t-1}+\mathbf b).
\]

The model does not need to fix the \(N\) order history, but a hidden state transformation of \(H\times H\) is required at each time step.

### 3.2 Complexity

Thesis formula (3) is

\[
Q_{\mathrm{RNNLM}}
=H^2+HV.
\tag{3}
\]

Approximately using hierarchical softmax is

\[
Q_{\mathrm{RNNLM+HS}}
\approx H^2+H\log_2V.
\]

The main cost is converted to \(H^2\).

## 4. Complexity of CBOW

CBOW removes non-linear hidden layers. Reading \(N\) context vectors and summing or averaging the cost is about \(ND\); using hierarchical softmax to predict the target word, the cost is about \(D\log_2V\). Thesis formula (4) is

\[
Q_{\mathrm{CBOW}}
=ND+D\log_2V.
\tag{4}
\]

The key changes are:

- No \(NDH\);
- No \(H^2\);
- The output path interacts directly with the \(D\) dimensional projection.

## 5. Complexity of Skip-gram

Skip-gram predicts multiple nearby words for a central word. The maximum window radius is \(C\), and the paper formula (5) is

\[
Q_{\mathrm{SG}}
=C\bigl(D+D\log_2V\bigr).
\tag{5}
\]

The external factor \(C\) means that each central word will generate multiple context predictions. The original text randomly draws the actual radius \(R\in\{1,\ldots,C\}\) for each center position, so the probability of distant words being included is low.

## 6. An order of magnitude example

take

\[
V=10^6,\quad D=300,\quad N=8,\quad H=600,
\quad C=10,
\]

And use \(\log_2V\approx20\). After ignoring the constants:

|model|Main calculations|Approximately \(Q\)|
|---|---|---:|
|NNLM + full softmax| \(ND+NDH+HV\) | \(6.01\times10^8\) |
| NNLM + HS | \(ND+NDH+H\log_2V\) | \(1.45\times10^6\) |
| RNNLM + HS | \(H^2+H\log_2V\) | \(3.72\times10^5\) |
| CBOW + HS | \(ND+D\log_2V\) | \(8.4\times10^3\) |
| Skip-gram + HS | \(C(D+D\log_2V)\) | \(6.3\times10^4\) |

This example only shows the order of magnitude in the formula. Actual throughput is also affected by cache locality, vectorization, thread conflicts, and tree path length.

## 7. Why simple models may be better represented

On a single sample, complex models have stronger function expression capabilities; under a fixed total budget, simple models can see more tokens, use larger vectors, and cover larger vocabulary. The proposition of the paper is that the latter scale advantage can exceed the single-sample fitting advantage brought by complex structures in vocabulary representation tasks.

This can be written as a budget constraint:

\[
B\approx E T Q.
\]

When \(B\) is fixed and \(Q\) is reduced by \(k\) times, the trainer can approximately expand \(T\), \(D\), epoch or their combination. The paper's experiments then examine which combinations improve analogy accuracy.

## 8. DistBelief parallel training

The author also implements the model on DistBelief:

- Multiple model copies process mini-batch in parallel;
- Gradient synchronization through central parameter server;
- Use asynchronous gradient updates;
- Use AdaGrad to adjust learning rate;
- Experiments use ~50–100 replicas and a large number of CPU cores.

Parallelization does not change the statistical objectives of CBOW and Skip-gram, but it changes the wall clock time, communication overhead, and update timing. The "number of days × number of CPU cores" in Table 6 can only be regarded as an approximate resource record on the system at that time.

## 9. Design judgment supported by complexity formula

The paper derives three design principles from equations (1)–(5):

1. Large vocabulary output requires tree shape or other approximation methods;
2. The nonlinear hidden layer was the main computational bottleneck of NNLM at that time;
3. After reducing the single-step cost, the data scale and representation dimensions must increase together.

Table 2 specifically tests the third point: increasing only data or only increasing dimensions will gradually lead to diminishing returns, and increasing both at the same time will have more obvious effects.
