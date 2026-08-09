# From Bellman equation to DQN

## 1. Why function approximation is needed?

The state space is a continuous set:

\[
\mathcal S=[0,1]^D.
\]

Any two ability values may be different, making it impossible to build a finite Q-table. The paper uses neural network approximation:

\[
Q^*(s,a)
\approx
\widehat Q(s,a;\mathbf w),
\tag{1}
\]

Among them, \(\mathbf w\) summarizes all network weights and biases.

## 2. Input and output of DQN

The input layer accepts \(D\) dimension capabilities:

\[
s\in\mathbb R^D.
\]

The output layer has \(L\) units:

\[
\widehat{\mathbf Q}(s;\mathbf w)
=
\begin{bmatrix}
\widehat Q(s,1;\mathbf w)\\
\vdots\\
\widehat Q(s,L;\mathbf w)
\end{bmatrix}.
\tag{2}
\]

A single forward pass yields the long-term value of all materials.

## 3. Basic expression of neural network of the paper

Take a hidden layer as an example:

\[
\mathbf h
=
\phi(\mathbf W_{hx}\mathbf x+\mathbf b_h),
\tag{3}
\]

\[
\mathbf y
=
\mathbf W_{yh}\mathbf h+\mathbf b_y.
\tag{4}
\]

The paper uses ReLU as a typical activation function:

\[
\phi(z)=\max(z,0).
\]

When used for DQN, \(\mathbf x=s\), \(\mathbf y=\widehat{\mathbf Q}(s;\mathbf w)\).

## 4. Why the ideal supervision target cannot be obtained directly

If the true \(Q^*(s,a)\) is known, it can be minimized:

\[
\min_{\mathbf w}
\mathbb E
\left[
\left(
\widehat Q(S,A;\mathbf w)-Q^*(S,A)
\right)^2
\right].
\tag{5}
\]

In practice \(Q^*\) is unknown, and the state distribution is also affected by policies and transitions. Q-learning uses Bellman's one-step expansion to construct computable objectives.

## 5. Bellman target

to transfer

\[
(s,a,r,s'),
\]

If \(s'\) has not been terminated:

\[
y
=
r+\gamma
\max_{a'\in\mathcal A}
\widehat Q(s',a';\mathbf w).
\tag{6}
\]

If \(s'\) has reached the target:

\[
y=r=0.
\tag{7}
\]

Together they are:

\[
y
=
\begin{cases}
r,
&
\|s'-\mathbf1_D\|_\infty<10^{-3},
\\
r+\gamma\max_{a'}\widehat Q(s',a';\mathbf w),
&
\text{Other situations}.
\end{cases}
\tag{8}
\]

## 6. TD error and loss

\[
\delta
=
y-\widehat Q(s,a;\mathbf w).
\tag{9}
\]

The squared loss on mini-batch \(\mathcal M\) can be written as:

\[
\mathcal L_Q(\mathbf w)
=
\frac{1}{|\mathcal M|}
\sum_{(s,a,r,s')\in\mathcal M}
\left[
\widehat Q(s,a;\mathbf w)-y
\right]^2.
\tag{10}
\]

gradient descent update:

\[
\mathbf w
\leftarrow
\mathbf w
-\alpha\nabla_{\mathbf w}\mathcal L_Q(\mathbf w).
\tag{11}
\]

## 7. Numerical examples

Assume:

\[
r=-1,\qquad
\gamma=0.9,
\qquad
\max_{a'}\widehat Q(s',a')=-4.0.
\]

Then:

\[
y=-1+0.9(-4.0)=-4.6.
\]

If the current forecast

\[
\widehat Q(s,a)=-3.8,
\]

rule

\[
\delta=-4.6-(-3.8)=-0.8.
\]

The action's prediction is too optimistic, and the update will push its Q-value in a more negative direction.

If \(s'\) is in the terminated state:

\[
y=0.
\]

The next state value cannot be added at this time, otherwise the fictitious reward will continue to be calculated after the episode ends.

## 8. Same-network bootstrap in the paper algorithm

The first draft equations (15)–(16) use the same set of parameters \(\mathbf w^{(t)}\):

\[
y
=
r+\gamma\max_{a'}
\widehat Q(s',a';\mathbf w^{(t)}).
\]

The target moves with the network being updated, potentially causing estimation oscillations and overestimation.

Modern DQN often joins the target network:

\[
y
=
r+\gamma\max_{a'}
\widehat Q(s',a';\mathbf w^-),
\tag{12}
\]

And execute periodically:

\[
\mathbf w^-\leftarrow\mathbf w.
\]

This is engineering stabilization. When reproducing a paper, it should be clear whether the original algorithm or the modern version should be used.

## 9. Double DQN

Double DQN uses online networks to select actions and target network valuations:

\[
a^*
=
\arg\max_{a'}
\widehat Q(s',a';\mathbf w),
\]

\[
y
=
r+\gamma
\widehat Q(s',a^*;\mathbf w^-).
\tag{13}
\]

It alleviates Q-value overestimation caused by maximization operations.

## 10. Educational implications of Q value

\[
\widehat Q(s,a)
\]

means:

> When the current ability is \(s\), first recommend the material \(a\), and then continue to use the current optimal strategy. How much discount cumulative reward is expected to be obtained.

Under the paper award, it is highly correlated with "how many rounds are expected to reach the goal." It is not equivalent to:

-Next capability increment;
- Probability of students completing the material;
- Material difficulty;
- Correct answer rate;
- item information.

## 11. Conditions for DQN to learn strategies

The representational ability of a neural network does not guarantee the reliability of the strategy. Also required:

1. The training data covers key states—action areas;
2. Each action has enough transfer samples;
3. The reward and termination rules are correct;
4. The ability estimate error is controllable;
5. The training distribution is close to the deployment distribution;
6. Extrapolation actions are subject to safety constraints.

The next page puts these objects into a full training loop.
