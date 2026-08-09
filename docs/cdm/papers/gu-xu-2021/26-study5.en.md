# Experiment：G-DINA Study V

## 1. Goal

Study V verifies the sufficient conditions for D/E pan-recognition of general RLCM.

In the author's \(5\times2\) candidate file, structural representatives that satisfy D/E include:

\[
Q^{15},Q^{18},Q^{27},Q^{54},Q^{81},
\]

and \(Q^{121}\) which is all 1's. The main text shows the first five non-1 scenarios.

## 2. Five true queens

\[
Q^{15}=
\begin{pmatrix}
0&1\\1&1\\1&0\\1&0\\0&1
\end{pmatrix},
\quad
Q^{18}=
\begin{pmatrix}
0&1\\1&1\\1&1\\1&0\\0&1
\end{pmatrix},
\]

\[
Q^{27}=
\begin{pmatrix}
0&1\\1&1\\1&1\\1&1\\0&1
\end{pmatrix},
\]

\[
Q^{54}=
\begin{pmatrix}
0&1\\1&1\\1&1\\1&1\\1&0
\end{pmatrix},
\quad
Q^{81}=
\begin{pmatrix}
0&1\\1&1\\1&1\\1&1\\1&1
\end{pmatrix}.
\]

## 3. Design

- Model: G-DINA;
- sample size: \(N=10^5\);
- Latent class ratio: uniform;
- True item parameters: randomly generated and satisfying monotonicity;
- Each candidate Q: 5 random initial values EM;
- Illustration candidates: estimated increments are all positive.

## 4.result

In all five scenarios, true Q achieves the highest log-likelihood among the presented candidates.

This supports:

\[
D+E
\Longrightarrow
\text{Joint uniqueness at general parameter points}.
\]

## 5. Why \(Q^{81}\) is also pan-complete

\(Q^{81}\) There is only one question \((0,1)\), and the other four questions are all \((1,1)\). You can match attribute 1 with different questions from the all-attribute questions, and at the same time match attribute 2 with the \((0,1)\) question or another all-attribute question, thus forming two pan-complete \(2\times2\) submatrices; the remaining all-attribute questions cover two columns.

This reflects that the pan-integrity is looser than the integrity of \(I_K\).

## 6. Evidence boundaries

Each scenario only shows the likelihood map of a large sample data set, without reporting:

- Q recovery rate for multiple repetitions;
- parameter MSE;
- Small sample performance;
- Stability of different optimizers;
- Running time.

Therefore, Study V is a numerical illustration of structural adequacy, and the algorithm performance still requires independent experiments.
