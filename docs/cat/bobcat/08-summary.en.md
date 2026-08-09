#BOBCAT Summary

### One formula summarizes the entire framework

BOBCAT can be compressed into

\[
\min_{\gamma,\phi}
\frac1N\sum_{i=1}^{N}
\mathbb{E}_{j_i^{(1:n)}\sim\Pi_\phi}
\left[
\mathcal L_{\mathrm{meta}}
\left(
\operatorname{Adapt}_K
\left(
\gamma;
\{Y_{i,j_i^{(t)}}\}_{t=1}^{n}
\right),
\Gamma_i
\right)
\right].
\]

Read from the inside out:

1. Strategy \(\Pi_\phi\) selects \(n\) questions;
1. Read the answers to these questions from historical data;
1. `Adapt` starts from the global response parameters and takes \(K\) steps to obtain the student's local parameters;
1. Calculate the meta loss on \(\Gamma_i\) that does not participate in adaptation;
1. Average the randomness of students and topic selection;
1. Update the global response model and topic selector.

### The four most memorable distinctions

1. **Inner-level training questions and meta questions**: The former is used for adaptation, and the latter is used to evaluate the quality of adaptation.
1. **Ideal argmin and \(K\) step approximation**: The paper problem definition gives the exact inner-level optimal, and the actual solver uses
    \(K\) step truncated approximation.
1. **Unbiased and low variance**: Unbiased strategy gradient may have high variance; Approx is biased but has dense signals.
1. **Prediction accuracy and psychometrics quality**: meta response prediction is an important indicator; validity, fairness and test security requirements
    respective evidence.

### If you only remember one sentence

!!! note "Key points"
    BOBCAT uses held-out answers to supervise "which small number of questions are most worth asking": topic selection determines the inner layer students' adaptation, and the inner layer adapts
    The outer layer prediction is determined, and the outer layer gradient in turn trains the response model and topic selection strategy.
