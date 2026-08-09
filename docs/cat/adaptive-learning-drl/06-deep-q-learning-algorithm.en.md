# Deep Q-learning complete algorithm

## 1. Input of the paper algorithm

First draft Algorithm 1 accepted:

|parameters|meaning|
|---|---|
| \(\gamma\) |discount factor|
| \(\alpha\) |DQN learning rate|
| \(\varepsilon_{\max}\) |Initial exploration probability|
| \(\varepsilon_{\min}\) |final exploration probability|
| \(\tau_\varepsilon\) |Total number of steps required to explore decay|
| \(M\) |mini-batch size|
| \(E\) |The number of episodes, that is, the number of training students|

The output is the DQN parameter \(\mathbf w\).

## 2. Episode and time step

An episode represents a student's complete learning process from initial ability to goal.

```text
Episode 1: Student 1’s complete learning path
episode 2: Student 2’s complete learning path
...
Episode E: Student E’s complete learning path
```

In real student training, the number of episodes corresponds to the number of students; when using the transition model, virtual episodes can be generated repeatedly.

## 3. Exploration rate decay

The paper uses linear attenuation:

\[
\varepsilon^{(t)}
=
\varepsilon_{\max}
-
\left(
\varepsilon_{\max}-\varepsilon_{\min}
\right)
\min\!\left(
\frac{\tau}{\tau_\varepsilon},
1
\right),
\tag{1}
\]

Among them, \(\tau\) is the accumulated number of environmental steps across episodes.

So:

- In the initial stage, \(\varepsilon\) is high, and materials are widely tried;
- As training progresses, the proportion of random actions decreases;
- Retain \(\varepsilon_{\min}\) after attenuation is complete.

## 4. epsilon-greedy action

\[
a^{(t)}
=
\begin{cases}
\text{from}\mathcal A\text{Randomly selected},
&
\text{Probability}\varepsilon^{(t)},
\\
\displaystyle
\arg\max_a
\widehat Q(s^{(t)},a;\mathbf w),
&
\text{Probability}1-\varepsilon^{(t)}.
\end{cases}
\tag{2}
\]

The role of exploration is to collect action results that are not currently favored by the current network. In the absence of exploration, early errors may result in data that may never be available for some materials.

## 5. Interacting with the student environment

After selecting materials:

1. Hand the material \(a^{(t)}\) to the students;
2. Take the test after the study is completed;
3. Use ability estimator to obtain \(s^{(t+1)}\);
4. Calculate \(r^{(t)}\) based on the target distance;
5. Save the transition.

\[
\left(
s^{(t)},
a^{(t)},
r^{(t)},
s^{(t+1)}
\right)
\longrightarrow
\mathcal H.
\tag{3}
\]

\(\mathcal H\) is the experience replay pool.

## 6. Experience replay

Each environment step randomly selects \(M\) transitions from \(\mathcal H\):

\[
\mathcal M
\sim
\operatorname{UniformMiniBatch}(\mathcal H,M).
\tag{4}
\]

Experience replay brings three effects:

1. The same expensive student transfer can be used multiple times;
2. Random sampling breaks up the strong correlation between adjacent steps;
3. Each update covers different students and different ability areas at the same time.

!!! warning "Explanation of the original text of the paper"

    The first draft stated that random resampling is used to reduce bias caused by samples. More precisely, experience replay primarily improves data reuse and correlation; it cannot automatically eliminate behavioral strategy undercoverage, measurement error, or selection bias.

## 7. Sample-by-sample TD target

For the transfer of item \(i\) in mini-batch:

\[
y_i
=
\begin{cases}
r_i,
&
\text{If}s_i'\text{terminated},
\\
r_i+\gamma\max_{a'}\widehat Q(s_i',a';\mathbf w),
&
\text{If it is not terminated yet}.
\end{cases}
\tag{5}
\]

Then minimize:

\[
\mathcal L_Q
=
\frac1M
\sum_{i=1}^M
\left(
\widehat Q(s_i,a_i;\mathbf w)-y_i
\right)^2.
\tag{6}
\]

Each transfer only supervises the output corresponding to the actual action \(a_i\).

## 8. Termination conditions

\[
\|s^{(t+1)}-\mathbf1_D\|_\infty<10^{-3}
\quad\Longrightarrow\quad
\text{episode ends}.
\tag{7}
\]

The maximum number of steps \(T_{\max}\) should also be set in the implementation to prevent the strategy from being unable to reach the target for a long time and causing an infinite loop.

The handling of timeout transition needs to be clear:

- Treat timeouts as truncation and retain bootstrap;
- Or treat the timeout as a failed termination and add a failure penalty.

The two treatments correspond to different goals.

## 9. Complete pseudocode

```python
initialize online_q
initialize replay_buffer
global_step = 0

for episode in range(num_episodes):
    state = environment.reset()

    for step in range(max_steps):
        epsilon = linear_decay(global_step)
        action = epsilon_greedy(online_q, state, epsilon)

        next_state = environment.step(state, action)
        done = max_abs(next_state - target) < 1e-3
        reward = 0.0 if done else -1.0

        replay_buffer.add(
            state, action, reward, next_state, done
        )

        batch = replay_buffer.sample(batch_size)
        update_q_network(batch)

        state = next_state
        global_step += 1

        if done:
            break
```

This code expresses the logic of the paper. The engineering version should also add warm-up, target network, gradient clipping, random seeds and checkpoints.

## 10. Hyperparameter used in paper simulation

|item|numerical value|
|---|---:|
|DQN hidden layer| 64、32 |
|training episode| 2000 |
| \(\gamma\) | 0.9 |
| \(\alpha\) | \(6\times10^{-4}\) |
| \(\varepsilon_{\max}\) | 1.0 |
| \(\varepsilon_{\min}\) | 0.1 |
| \(\tau_\varepsilon\) |2000 environment steps|
| mini-batch \(M\) | 256 |
|optimizer| Adam |

## 11. The difference between training and deployment

### Training

- Use \(\varepsilon\)-greedy;
- Collect and reuse transitions;
- Calculate TD target;
- Update network parameters.

### Deployment

- Receive real measurement status;
- Usually adopt greedy actions;
- No need to know the future state;
- Re-decision after each round of student feedback.

If the deployment still retains random exploration, it should undergo a security review, and random actions can only come from qualified material collections.

## 12. Legal action constraints

Collections of materials in real systems change with state:

\[
\mathcal A_{\text{valid}}(s)
\subseteq
\mathcal A.
\]

Possible hard constraints include:

- Prerequisite knowledge has not been met;
- Materials have been completed;
- Age or language does not apply;
- Accessibility conditions are not met;
- Teacher lock or class time not allowed.

Both greedy and bootstrap should only be evaluated on legal sets:

\[
\max_{a'\in\mathcal A_{\text{valid}}(s')}
Q(s',a').
\tag{8}
\]

Otherwise the network may achieve falsely high target values through unexecutable actions.

## 13. Additional issues with offline data

The algorithm of the paper is described by online interaction. If there are only historical logs, the data comes from the old policy \(\mu(a\mid s)\). Actions not chosen by the old strategy lack counterfactual results:

\[
\Pr_\mu(A=a\mid S=s)\approx0
\quad\Longrightarrow\quad
Q(s,a)\text{lack of direct evidence}.
\]

Things to consider before deploying:

- Behavioral policy coverage;
- Conservative offline RL;
- Importance weighted or doubly robust evaluation;
- Small-scale secure online verification.
