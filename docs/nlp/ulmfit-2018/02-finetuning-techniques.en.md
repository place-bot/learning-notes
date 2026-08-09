# Discriminative LR, STLR and Gradual Unfreezing

## 1. Discriminative fine-tuning

Use different learning rates for each layer:

\[
\theta_t^\ell
=
\theta_{t-1}^\ell
-
\eta^\ell\nabla_{\theta^\ell}J.
\]

First find the top-level learning rate, and then order

\[
\eta^{\ell-1}=\eta^\ell/2.6.
\]

The low-level general language features have been slightly changed, while the top-level task features have been significantly changed.

## 2. Slanted triangular learning rate

\[
cut=\lfloor T\cdot cut_{\text{frac}}\rfloor.
\]

\[
p=
\begin{cases}
t/cut,&t<cut,\\
1-\dfrac{t-cut}{cut(1/cut_{\text{frac}}-1)},&t\ge cut.
\end{cases}
\]

\[
\eta_t
=
\eta_{\max}
\frac{1+p(ratio-1)}{ratio}.
\]

Commonly used in papers

\[
cut_{\text{frac}}=0.1,\quad ratio=32.
\]

The learning rate increases rapidly in the short term, and then decreases linearly in the long term: adapt quickly first, and then refine.

## 3. Numerical examples

Let \(\eta_{\max}=0.01,ratio=32\). Starting point:

\[
\eta_0=0.01/32=0.0003125.
\]

to cut:

\[
\eta_{cut}=0.01.
\]

Ends back to about 0.0003125.

## 4. Gradual unfreezing

Classifier training first unfreezes the last layer; in the next round, the penultimate layer is unfrozen, and is expanded to the bottom layer round by round, and finally fine-tuning the whole. It reduces the risk of underlying generic features being corrupted by large gradients of random classification heads in the early stages.

## 5. Cooperation of the three

- Gradual unfreezing controls "when to update which layer";
- discriminative LR controls "how fast each layer is updated";
- STLR controls "how the learning rate changes during training."

They solve problems in different dimensions.
