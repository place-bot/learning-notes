# Interfaces with CDM, CAT and RecCAT

## 1. The paper is located at the item bank preparation level

```text
item content
   │
   ▼
Semantic model generates Q candidates ← Zhao & Huang
   │
   ▼
Expert/Response Data Calibration
   │
   ▼
Available item bank parameters
   │
   ▼
CAT selects the next question based on students’ real-time responses
```

The paper does not define a CAT strategy. It can provide item attribute metadata to CAT.

## 2. Question-by-question update of CAT

Suppose the question \(t\) is \(j_t\), and the student response is \(Y_t\). Update student status after observation:

\[
\pi_t(\boldsymbol\alpha)
\propto
p
\left(
Y_t
\mid
\boldsymbol\alpha,
\boldsymbol q_{j_t},
\boldsymbol\theta_{j_t}
\right)
\pi_{t-1}(\boldsymbol\alpha).
\]

The next question is selected based on the updated \(\pi_t\):

\[
j_{t+1}
=
\arg\max_{j\in\Omega_t}
U
\left(
j;\pi_t,Q,\Theta
\right).
\]

So every time a response is received, the next question can be changed.

## 3. How does the text Q model enter topic selection?

For new questions without stable Q, the text model gives:

\[
p_\psi(\boldsymbol q_j\mid d_j).
\]

The topic utility can be integrated over the Q uncertainty:

\[
\widetilde U_t(j)
=
\mathbb E_{
\boldsymbol q_j
\sim
p_\psi(\cdot\mid d_j)
}
\left[
U(j;\pi_t,\boldsymbol q_j,\boldsymbol\theta_j)
\right].
\]

Risk penalties can also be added:

\[
\operatorname{Score}_t(j)
=
\widetilde U_t(j)
-
\lambda
H
\left[
p_\psi(\boldsymbol q_j\mid d_j)
\right].
\]

The more uncertain the Q semantics, the greater the penalty.

## 4. Content balance

If the CAT needs to cover multiple content areas, a measured count can be maintained

\[
\boldsymbol c_t=(c_{t1},\ldots,c_{tK}).
\]

Add target gaps when selecting topics:

\[
B_t(j)
=
\sum_{k=1}^{K}
w_k
\left(
r_{tk}-c_{tk}
\right)_+
p_\psi(q_{jk}=1\mid d_j).
\]

Finally:

\[
j_{t+1}
=
\arg\max_{j\in\Omega_t}
\left\{
U_t(j)
+\gamma B_t(j)
-\lambda R_j
\right\}.
\]

Here \(R_j\) can represent Q uncertainty, exposure or other risk.

## 5. Relationship with fixed sequence generation

A candidate plan can be generated initially:

\[
(j_1,\ldots,j_T).
\]

Receding-horizon is used for actual execution:

1. Only execute the current first question;
2. Receive student responses;
3. Update student posterior and content status;
4. Re-plan the remaining questions;
5. Go to the next question.

This retains the generative planning capabilities and the real-time adaptation of CAT.

## 6. What can the paper provide?

- Cold start content tag for new questions;
- Attribute probabilities required for content balance;
- Semantic filtering of item bank search space;
- Lower the review priority of reliability questions.

## 7. What the paper alone cannot provide

- Posterior to student abilities or attributes;
- Amount of information per question;
- stopping rule;
- exposure control;
- Test security;
- Real-time topic selection strategy;
- Long-term learning benefits.

## 8. Direct inspiration for RecCAT

The system can be split into two models:

\[
\underbrace{
p_\psi(Q\mid\text{item content})
}_{\text{item semantic model}}
\quad+\quad
\underbrace{
\pi_\phi(\text{next item}\mid
\text{history},Q,\text{constraints})
}_{\text{adaptive strategy}}.
\]

Zhao and Huang cover an early form of the previous module. The focus of your generative CAT research will fall on the second module and their joint training.
