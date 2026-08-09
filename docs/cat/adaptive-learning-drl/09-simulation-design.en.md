# Simulation environment and experimental design

The paper does not use real learning platform data. The two sets of experiments share the same artificially constructed continuous state MDP to verify policy learning, measurement noise robustness, and data efficiency of the transition model.

## 1. Experimental questions

### Study I

1. Can DQN learn stable policies?
2. Is DQN better than heuristics and random selection?
3. When the ability estimate error exists, is the advantage maintained?

### Study II

1. Can a small number of real students fit an effective transition model?
2. Is a virtual DQN trained with a transition model better than an actual DQN trained with the same number of students?

## 2. Status and action

States are two-dimensional capabilities:

\[
\boldsymbol\Theta^{(t)}
=
\begin{bmatrix}
\Theta_1^{(t)}\\
\Theta_2^{(t)}
\end{bmatrix}.
\]

Action collection:

\[
\mathcal A=\{1,2,3\}.
\]

The two abilities can be understood as addition and subtraction:

- Material 1 mainly improves ability 1;
- Material 2 mainly improves ability 2;
- Material 3 involves both abilities and includes cross-dimensional dependencies.

The initial status of all students is:

\[
\boldsymbol\Theta^{(0)}=(0,0)^\top.
\tag{1}
\]

## 3. Capacity increment

\[
\Delta\boldsymbol\Theta^{(t)}
=
\boldsymbol\Theta^{(t+1)}
-\boldsymbol\Theta^{(t)}
=
\begin{bmatrix}
\Delta\Theta_1^{(t)}\\
\Delta\Theta_2^{(t)}
\end{bmatrix}.
\tag{2}
\]

The transfer core is written as:

\[
\mathcal P(\boldsymbol\theta'\mid\boldsymbol\theta,a)
=
\Pr\!\left(
\Delta\boldsymbol\Theta^{(t)}
=
\Delta\boldsymbol\theta
\mid
\boldsymbol\Theta^{(t)}
=
\boldsymbol\theta,
A^{(t)}=a
\right).
\tag{3}
\]

The paper assumes no regression in ability, therefore:

\[
\Delta\theta_d\in[0,1-\theta_d].
\tag{4}
\]

## 4. Beta incremental distribution

For material 1 or 3:

\[
\Delta\theta_1
\sim
\operatorname{Beta}
\left(
1,
g_1(\boldsymbol\theta,a)
\right).
\tag{5}
\]

For material 2 or 3:

\[
\Delta\theta_2
\sim
\operatorname{Beta}
\left(
1,
g_2(\Delta\theta_1,\boldsymbol\theta,a)
\right).
\tag{6}
\]

Special circumstances:

\[
\Delta\theta_2=0
\quad\text{when}a=1,
\]

\[
\Delta\theta_1=0
\quad\text{when}a=2.
\]

## 5. Parametric function of the first dimension

\[
g_1(\boldsymbol\theta,a)
=
\begin{cases}
3+8\theta_1-0.2\theta_2,
&
a=1,
\\
15+15\theta_1-0.4\theta_2,
&
a=3.
\end{cases}
\tag{7}
\]

In \(\operatorname{Beta}(1,b)\), the larger \(b\) is, the more the mass is concentrated near 0, and the smaller the typical increment is. Therefore:

- The higher the \(\theta_1\), the harder it is to continue improving ability 1;
- \(\theta_2\) There is a slight positive transfer to capability 1 because its coefficient is negative.

## 6. Parametric function of the second dimension

\[
g_2(\Delta\theta_1,\boldsymbol\theta,a)
=
\begin{cases}
10-\theta_1+5\theta_2,
&
a=2,
\\
\displaystyle
20
-28\theta_1
\exp\!\left[
-\frac{(\theta_1-0.6)^2}{0.3}
\right]
+30\theta_2
-0.3\Delta\theta_1,
&
a=3.
\end{cases}
\tag{8}
\]

Equation (8) expresses:

- The higher the \(\theta_2\), the harder it is to continue improving ability 2;
- Ability 1 has migration to ability 2;
- Material 3 is more beneficial for learners of medium to high ability 1;
- When \(\Delta\theta_1\) is larger in this round, \(\Delta\theta_2\) is also more likely to be larger.

## 7. A detail that must be completed when reproducing

The value of the standard Beta distribution is \([0,1]\), and the paper also states:

\[
\Delta\theta_d\in[0,1-\theta_d].
\]

The text does not clearly state how to satisfy the remaining space constraints after sampling. Optional implementations include:

\[
\Delta\theta_d
=
(1-\theta_d)Z_d,
\qquad
Z_d\sim\operatorname{Beta}(1,g_d),
\tag{9}
\]

Or truncate the updated status:

\[
\theta_d'
=
\min(1,\theta_d+\Delta\theta_d).
\tag{10}
\]

The transfer distribution is different between the two implementations. Recurrence reports should specify which one is used.

## 8. ability estimate error

The observation status is:

\[
\widehat{\boldsymbol\theta}
=
\boldsymbol\theta+\mathbf e,
\]

\[
e_1,e_2
\overset{\text{iid}}{\sim}
\mathcal N(0,\sigma^2).
\tag{11}
\]

About 99.7% of the error under normal distribution falls on:

\[
(-3\sigma,3\sigma).
\]

The horizontal axis of Figure 8 uses \(\sigma\):

\[
0\%,0.5\%,1\%,2\%,3\%,3.3\%,4\%,5\%.
\]

When \(\sigma=5\%\), about 99.7% of the single-dimensional error is located at \(\pm15\%\), so the "1% to 15% error" mentioned in the text mainly corresponds to a range of three standard deviations.

## 9. Study I training conditions

|item|settings|
|---|---:|
|Number of training students| 2000 |
|Number of test students| 200 |
|DQN hidden layer| 64、32 |
|Discount \(\gamma\)| 0.9 |
|learning rate \(\alpha\)| \(6\times10^{-4}\) |
|initial exploration rate| 1.0 |
|final exploration rate| 0.1 |
|Explore decay steps| 2000 |
| mini-batch | 256 |
|optimizer| Adam |
|Curve smoothing window| 20 episodes |

## 10. Study I Comparative Strategies

### DQN

Outputs the long-term Q value of three copies of the material based on the current continuous capacity.

### Heuristics

Choose materials that will enhance abilities that are not yet fully mastered. The text does not give enough pseudocode to reproduce the entire tie-breaking independently.

### Random

Choose randomly from three materials.

## 11. Study II Design

transition model structure:

- Input: current 2D state and action;
- Hidden layer: 1 layer, 32 units;
- Output: next 2D state.

The actual number of students is:

\[
10,20,30,40,50,100,150,200,2000.
\]

Compare the two routes for each sample size.

### Actual DQN

Directly use the episodes generated by this batch of real students to train DQN.

### Virtual DQN

First, use the same batch of real students to fit the transition model, and then let DQN train 2000 virtual episodes on the estimated model.

Both use the same real student budget, the difference lies in the way the data is reused.

## 12. Evaluation indicators

### Strategy reward

The closer the episode reward is to 0, the fewer non-terminating steps are required to reach the goal.

### transition model

- training \(R^2\);
- Test \(R^2\);
- Next state RMSE.

### Robustness

Compare the average episode reward of DQN and heuristic strategies under different \(\sigma\).

## 13. Conclusions supported by experimental design

It can verify:

- Under known simulation rules, whether DQN can learn from transfer samples;
- whether nonlinear cross-capability dependencies might allow long-term strategies to outperform local heuristics;
- Whether the learned transition model can improve sample reuse;
- Robust to additive Gaussian measurement errors.

It cannot be verified directly:

- Real students learn according to these Beta functions;
- Strategies can improve real course performance;
- The material has the same causal effect on different groups;
- Virtual student models are trustworthy in out-of-distribution actions.
