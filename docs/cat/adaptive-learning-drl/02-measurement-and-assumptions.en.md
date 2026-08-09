# Measurement model, capability status and assumptions

## 1. Where does ability come from?

The paper expresses the student's current level as a \(D\) dimensional latent ability vector:

\[
\boldsymbol\theta^{(t)}
=
\left[
\theta_1^{(t)},
\ldots,
\theta_D^{(t)}
\right]^\top.
\]

latent ability cannot be observed directly. The system gives students a test or assignment after each round of learning, and then uses IRT/MIRT to estimate \(\boldsymbol\theta^{(t)}\) from the response data.

The complete closed loop is:

```text
study materials
   ↓
student learning
   ↓
Test/Assignment Response
   ↓
IRT or MIRT ability estimate
   ↓
Give estimation power to DQN
```

## 2. Universal IRT expression

The paper first writes a general measurement model:

\[
\Pr(U=u\mid\boldsymbol\theta)
=
f(\boldsymbol\theta,\boldsymbol\eta,u).
\tag{1}
\]

The meaning of each symbol is as follows:

|symbol|meaning|
|---|---|
| \(U\) |Random variable for the score of a certain test question|
| \(u\) |a specific score, such as 0 or 1|
| \(\boldsymbol\theta\) |student potential ability parameter|
| \(\boldsymbol\eta\) |item parameters|
| \(f\) |Mapping abilities, item parameters, and scores into probabilistic response functions|

This representation allows bipartite, hierarchical, multinomial and multidimensional models.

## 3. M2PL Example

The paper uses a multidimensional two-parameter logistic model to illustrate:

\[
\Pr(U_{ij}=1\mid\boldsymbol\theta_i,\mathbf a_j,d_j)
=
\frac{
\exp\!\left(\mathbf a_j^\top\boldsymbol\theta_i+d_j\right)
}{
1+\exp\!\left(\mathbf a_j^\top\boldsymbol\theta_i+d_j\right)
}.
\tag{2}
\]

Among them:

- \(i\) means student;
- \(j\) represents test questions;
- \(\boldsymbol\theta_i\in\mathbb R^D\) is the student ability;
- \(\mathbf a_j\in\mathbb R^D\) is the item’s distinguishing parameter for each capability dimension;
- \(d_j\) is the intercept;
- \(U_{ij}=1\) means correct answer.

linear predictor

\[
\mathbf a_j^\top\boldsymbol\theta_i+d_j
\]

Condensing multi-dimensional abilities into effective abilities for this question. If the components of \(\mathbf a_j\) are non-negative, improving the correlation ability will increase the probability of correct answers.

## 4. How does each round of measurement enter the decision-making process?

Let the real ability be \(\boldsymbol\theta^{(t)}\), and the estimated value is

\[
\widehat{\boldsymbol\theta}^{(t)}
=
\boldsymbol\theta^{(t)}
+\mathbf e^{(t)}.
\]

What DQN actually receives is an estimate:

\[
a^{(t)}
=
\pi\!\left(\widehat{\boldsymbol\theta}^{(t)}\right).
\]

Measurement errors therefore affect the system via two paths:

1. The current material may be wrongly selected due to bias in status judgment;
2. \(s\) and \(s'\) in the training data are noisy, and both the Q network and the transition model will learn contaminated mappings.

The simulation of the paper specifically adds a normal ability estimate error to check whether the strategy performance is robust.

## 5. Mapping from IRT scale to unified state space

IRT capabilities are typically defined on the real axis. The paper points out that the actual estimation can limit the \(d\) dimension to

\[
[-5,h_d],
\]

where \(h_d\) is the target level of the capability.

A natural linear bijection is:

\[
x_d
=
\frac{\theta_d+5}{h_d+5}.
\tag{3}
\]

The endpoint satisfies:

\[
\theta_d=-5\Rightarrow x_d=0,
\qquad
\theta_d=h_d\Rightarrow x_d=1.
\]

The inverse transformation is:

\[
\theta_d=(h_d+5)x_d-5.
\tag{4}
\]

After all dimensions are transformed:

\[
\mathbf x\in[0,1]^D.
\]

!!! warning "scale explanation"

    \(x_d\) is the capability after rescaling. The value \(0.8\) represents its relative position in the set interval; it can only be interpreted as "80% mastery probability" if the measurement model is otherwise defined.

## 6. Target state

After scaling, the \(d\) dimension reaches the target corresponding to \(x_d=1\). The common goal for all dimensions is

\[
\mathbf 1_D
=
\begin{bmatrix}
1\\
\vdots\\
1
\end{bmatrix}.
\]

The 1 here represents the pre-specified target level \(h_d\) and does not represent absolute perfection in reality.

## 7. Two assumptions clearly stated in the paper

### Assumption A1: Ability does not regress

\[
\theta_d^{(t+1)}
\ge
\theta_d^{(t)},
\qquad
d=1,\ldots,D.
\tag{5}
\]

It excludes forgetting, performance degradation due to fatigue, knowledge interference, and real regression due to measurement fluctuations.

### Assumption A2: The number of materials is limited

\[
\mathcal A=\{1,\ldots,L\}.
\tag{6}
\]

Finite discrete actions allow DQN to output the Q values of all materials at once.

## 8. Assumptions also implicit in modeling

The complete algorithm also relies on the following conditions:

|hypothesis|position in algorithm|risk|
|---|---|---|
|Ability vector fully summarizes learning history|Markov state|The same ability points may correspond to different prerequisite experiences.|
|ability estimate is accurate enough|DQN input|Measurement errors may alter material selection|
|The same group shares transfer rules|Unify \(\mathcal P\)|individual differences are averaged|
|Transfer time is complete|Use fixed \(\mathcal P(s'\mid s,a)\)|Fatigue, semester phases, and instructional changes undermine stability|
|Same material cost per copy|Unify every step \(-1\)|Video duration, load and monetary costs are not reflected|
|All dimension targets are 1|Termination condition|Personalized goals and elective abilities are difficult to express|

These assumptions determine the scope to which the results of the paper can be generalized.

## 9. Ability point estimation and belief state

If two students have the same point estimate:

\[
\widehat{\boldsymbol\theta}_A
=
\widehat{\boldsymbol\theta}_B,
\]

However, A's posterior distribution is very concentrated and B's posterior distribution is very wide. The risks of the two facing the same material may be different. Rigorous partially observable modeling would use

\[
b_t(\boldsymbol\theta)
=
\Pr(\boldsymbol\theta_t=\boldsymbol\theta\mid H_t),
\tag{7}
\]

Among them, \(H_t\) is the entire observed history.

The paper uses point estimation as the state, and the calculation is more direct; the author also regards POMDP as a future direction.

## 10. The role of CAT in the measurement process

If a fixed long test is used after each round of learning, measurement will take up a lot of time. CAT can select questions one by one based on the current answers and estimate \(\boldsymbol\theta^{(t)}\) with fewer questions. As a result, the system forms two layers of self-adaptation:

```text
Outer layer: Choose learning materials based on ability
  └─ Inner layer: Use CAT to select measurement items one by one and estimate abilities
```

The inner CAT pursues measurement efficiency, and the outer learning strategy pursues ability growth efficiency. The two-tier objectives should be defined and verified separately.
