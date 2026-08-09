#Write adaptive learning as MDP

## 1. Decision object

The paper's MDP answers in each round:

> Given the student's current continuous ability vector, which learning material should be selected for the next one so that the student can achieve all goals in as few rounds as possible?

The corresponding relationship is:

|MDP object|Thesis definition|
|---|---|
|Status \(s\)|Student's current latent ability vector|
|Action \(a\)|a study material number|
|Transfer \(\mathcal P\)|Changes in abilities caused by learning materials|
|Reward \(r\)|Target not reached is \(-1\), target reached is 0|
|terminate|All capability dimensions are close enough to the target|

## 2. State space

Thesis definition:

\[
s=\boldsymbol\theta,
\qquad
\mathcal S=[0,1]^D.
\tag{1}
\]

For example \(D=3\):

\[
s=
\begin{bmatrix}
0.20\\
0.70\\
0.40
\end{bmatrix}.
\]

Three components may represent algebraic, geometric, and probability abilities. The continuous state means that tabular Q-learning cannot store each state cell by cell.

## 3. Action space

If there are \(L\) materials:

\[
\mathcal A=\{1,\ldots,L\}.
\tag{2}
\]

Action \(a=\ell\) indicates the recommended material \(\ell\). Materials can correspond to:

- Textbook chapters;
- Video;
- interactive tasks;
- Exercise set;
- Teacher support methods;
- Teaching rhythm.

The paper treats materials as atomic numbers. Realistic implementation can add knowledge points, difficulty, duration and form to the action characteristics.

## 4. State transfer

\[
s'\sim\mathcal P(\cdot\mid s,a).
\tag{3}
\]

Transfer rules also include:

- The effect of materials on each ability dimension;
- Adjustment of learning gain based on current basis;
- Transfer between capabilities;
- The randomness of individual learning effects.

The basic algorithm of the paper does not require prior knowledge of \(\mathcal P\). This is exactly the reason for using model-free DQN.

## 5. Target distance

The target vector is:

\[
\mathbf 1_D
=
\begin{bmatrix}
1\\
\vdots\\
1
\end{bmatrix}.
\]

The paper uses infinite norm:

\[
\|s'-\mathbf 1_D\|_\infty
=
\max_{d=1,\ldots,D}
|s_d'-1|.
\tag{4}
\]

It examines the capability dimension furthest from the target.

For example:

\[
s'=(0.9995,0.9998,0.9980).
\]

The distance in each dimension is:

\[
(0.0005,0.0002,0.0020),
\]

So

\[
\|s'-\mathbf 1_3\|_\infty=0.0020.
\]

## 6. Reward function

First draft (8):

\[
r
=
\mathcal R(s,a,s')
=
\begin{cases}
-1,
&
\|s'-\mathbf 1_D\|_\infty\ge 10^{-3},
\\
0,
&
\|s'-\mathbf 1_D\|_\infty<10^{-3}.
\end{cases}
\tag{5}
\]

The threshold \(10^{-3}\) avoids requiring the value to be exactly equal to 1 in the continuous state.

## 7. How to express the shortest path by negative one per step

Suppose the student enters the target area after the \(T\) transfer, but has not yet reached the target area after the \(T-1\) transfer. If \(\gamma=1\), the return is

\[
G
=
\underbrace{-1-\cdots-1}_{T-1\text{times}}
+0
=
-(T-1).
\tag{6}
\]

Maximizing \(G\) is equivalent to minimizing the number of non-terminating steps taken before reaching the goal.

If \(0<\gamma<1\):

\[
G
=
-\sum_{t=0}^{T-2}\gamma^t
=
-\frac{1-\gamma^{T-1}}{1-\gamma}.
\tag{7}
\]

The smaller \(T\) is, the closer the reward is to 0, and the ranking still favors the path to the goal faster.

## 8. An easily overlooked counting detail

The reward for terminating transfers is defined as 0. If the system performs \(T\) material interactions, the cumulative negative rewards may only be \(T-1\). When the paper verbally explains the total reward as the opposite of the number of learning steps, it uses an approximate expression; it should be made clear when reproducing:

- How to count episode length;
- Whether the termination action is included in the cost;
- How much does the reward in the evaluation table differ from the number of materials.

## 9. The meaning of discount factor

Thesis simulation uses:

\[
\gamma=0.9.
\]

It has three effects:

1. Strengthen the preference to achieve goals earlier;
2. Limit the impact of forward rewards on the current Q value;
3. Make the Bellman operator a compressed map.

When the goal is to strictly minimize the expected number of materials, the stochastic shortest path model of \(\gamma=1\) is more straightforward, but requires additional conditions to ensure that the episodes are limited. The paper uses \(\gamma<1\) to obtain a more stable infinite time domain expression.

## 10. Strategy and real-time adaptation

The final strategy is:

\[
\pi^*(s)
\in
\arg\max_{a\in\mathcal A}
Q^*(s,a).
\tag{8}
\]

Deployment loop:

```text
Read current capability s_t
    ↓
Select a_t = argmax_a Q(s_t,a)
    ↓
Student learning materials a_t
    ↓
Test and estimate new capabilities s_{t+1}
    ↓
Calculate again all materials Q(s_{t+1},a)
```

The path is not fixed at the beginning. Real feedback after each learning update will update the state and change the next action.

## 11. Differences from one-time sequence generation

If the system outputs once

\[
(a_1,a_2,\ldots,a_T),
\]

Subsequent materials no longer rely on student feedback after they are generated, which is an open-loop plan.

The paper studies the function from state to action:

\[
\pi:\mathcal S\rightarrow\mathcal A.
\]

The sequence expanded from the policy satisfies:

\[
a_t=\pi(s_t),
\qquad
s_{t+1}\sim\mathcal P(\cdot\mid s_t,a_t).
\]

A sequence is the result of a closed-loop interaction. Even if two students start from the same \(s_0\) and have different random learning gains or measurement feedback, they may branch from the next step.

## 12. Extension of reward design

Realistic educational goals can be written as:

\[
r_t
=
-c_{\text{time}}(a_t)
-\lambda_1 c_{\text{load}}(s_t,a_t)
-\lambda_2 c_{\text{risk}}(s_t,a_t)
+\lambda_3 g(s_t,s_{t+1}),
\tag{9}
\]

Among them:

- \(c_{\text{time}}\): time-consuming;
- \(c_{\text{load}}\): cognitive load;
- \(c_{\text{risk}}\): frustration, withdrawal or security risk;
- \(g\): Ability gain.

Each step of the paper \(-1\) isolates the goal of "minimum rounds" to facilitate verification of the algorithm; formal deployment requires re-proofing the consistency of rewards and educational goals.
