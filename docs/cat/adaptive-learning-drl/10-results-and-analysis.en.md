# Experiment result and evidence boundary

## 1. Study I: Training convergence

Figure 5 of the paper shows the smoothed rewards of the first 1500 episodes, with a total training volume of 2000 simulated students.

Author reports:

- reward continues to improve in the first few hundred episodes;
- Stabilized around \(-15\) after about 600 episodes;
- The author believes that the strategy has found a stable and good solution in this simulation environment.

"About 600 students" is an observation for this particular 2D simulation and hyperparameter, and does not constitute the general DQN sample size law.

## 2. Complete numerical results of the three strategies

Essay evaluation strategy on 200 new simulated students:

|strategy|episode reward mean|standard deviation|
|---|---:|---:|
| DQN | **-13.49** | **4.59** |
|heuristic| -21.55 | 4.76 |
|random| -24.85 | 5.59 |

All rewards are negative, and the larger the value, the closer it is to 0, the better.

## 3. Translate reward into learning steps

Under the reward of \(-1\) for each step of the paper, the absolute value of reward approximately represents the number of non-terminating steps before termination. Therefore:

\[
21.55-13.49=8.06,
\]

DQN has about 8 fewer non-terminating steps on average than the heuristic.

If the absolute value of reward is used as a proxy for the number of steps, the relative reduction is approximately:

\[
\frac{21.55-13.49}{21.55}
\approx
37.4\%.
\]

Relatively random strategy:

\[
\frac{24.85-13.49}{24.85}
\approx
45.7\%.
\]

These percentages are quadratic conversions based on the means in the table. Whether the final step is included in the material count will produce a counting difference of about one step.

## 4. Variability

The standard deviation of DQN is 4.59, which is lower than the 4.76 of the heuristic and the 5.59 of the random policy. This shows that in this simulation:

- DQN average path is shorter;
- The degree of dispersion of different simulated student path lengths is also slightly lower.

The paper does not report the confidence interval, significance test, independent random seed distribution or effect size, so the impact of training randomness on the result cannot be independently judged from the text.

## 5. Learned path structure

Figure 7 shows a DQN path, the action sequence is:

\[
1,1,1,1,
3,3,3,3,3,
2,2,2,2,2,2.
\]

It embodies a three-stage strategy:

1. First use material 1 repeatedly to improve the first ability;
2. Switch to material 3 that acts in two dimensions at the same time in the appropriate area;
3. Finally, use material 2 to supplement the second ability.

This path demonstrates DQN's ability to exploit artificial cross-dimensional dependencies in a simulation environment. A single trajectory is not equal to the overall strategy explanation, it also needs to be drawn in the entire state space:

\[
\pi^*(\theta_1,\theta_2).
\]

## 6. ability estimate error

Figure 8 compares the rewards of DQN and heuristics under different \(\sigma\). Thesis report:

- Under various conditions from no error to \(\sigma=5\%\), the average reward of DQN is higher than the heuristic;
- The advantage of DQN is maintained within the additive normal error range studied.

The exact tabulated values for each noise condition are not given in the figure, and this site does not back-end the numbers from the curve pixels.

This robustness is limited to:

- Two-dimensional independent and identical variance normal error;
- Zero mean error;
- The same simulated transfer environment;
- The training method used in the paper.

Systematic bias, correlation error, capability boundary cutoff and model mismatch still need to be measured separately.

## 7. Study II: transition model prediction

Complete result:

|real number of students| 10 | 20 | 30 | 40 | 50 | 100 | 150 | 200 | 2000 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Training \(R^2\)| 0.96 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 |
|Test \(R^2\)| 0.95 | 0.97 | 0.96 | 0.96 | 0.97 | 0.97 | 0.97 | 0.97 | 0.97 |
| RMSE | 0.11 | 0.08 | 0.09 | 0.09 | 0.08 | 0.08 | 0.08 | 0.08 | 0.08 |

In this set of smooth 2D simulations, the transition model quickly reaches higher one-step prediction scores.

## 8. Actual DQN and Virtual DQN

Figure 9 Comparison:

- **Actual**: directly train DQN with a given number of real students;
- **Virtual**: First fit the transition model, and then train 2000 episodes in the model.

The main observations of the paper:

- When the number of real students does not exceed 200, the average reward of Virtual DQN is significantly higher;
- As the number of real students increases, both routes gradually approach the optimal;
- Performance is similar when using 2000 real students.

Therefore, the benefits of the transition model are concentrated in areas where real interactions are scarce.

## 9. Why can a small number of students achieve high R²?

This result may come from:

1. The state has only two dimensions;
2. There are only three types of actions;
3. True transitions are generated by smooth, regular Beta parametric functions;
4. All students share the same homogeneous MDP;
5. No complex behaviors, loss to follow-up, or non-stationary instructional changes.

High-dimensional, heterogeneous, and partially observable real-life environments usually require more data and stronger uncertainty control.

## 10. Core conclusions supported by result

Thesis evidence supports:

1. In the continuous capability state, DQN can learn material selection strategies;
2. In simulations with cross-capability dependencies, long-term value strategies can outperform local heuristics;
3. Additive normal capability noise does not eliminate the simulation advantages of DQN;
4. The learned transition model can improve the data efficiency of policy training in small sample intervals.

## 11. The part not covered by result

The paper does not provide:

- Real student experiments;
- Real learning platform log;
- Comparison with contextual bandit, model-based planning or modern offline RL;
- Stabilization ablation of target network, Double DQN, etc.;
- Statistical distribution of different random seeds;
- fairness, safety, cognitive load or dropout rate;
- transition model long rollout error;
- Individual heterogeneity and group migration;
- Open the official code repository.

## 12. How to design stronger follow-up experiments

### Simulation layer

- Multiple transfer function families;
- Different state dimensions and material scales;
- Forgetting, fatigue and non-stationarity;
- Individual random effects;
- Comparison between point prediction model and probability model;
- model-free, model-based, offline RL ablation.

### Offline real data layer

- Split training and testing according to time;
- Check behavioral policy coverage;
- Use conservative offline RL;
- Use off-policy evaluation;
- Evaluate ability gain, time, exit and fairness.

### Online layer

- Carry out safety small flow test first;
- Pre-register for the main ending;
- Comparison with teacher strategies and current rules;
- Document side effects and idiosyncratic effects;
- Allows teacher intervention and policy rollback.

## 13. The most accurate result summary

This paper gives a complete algorithm prototype: continuous capabilities enter DQN, learning material changes capabilities, and transition model expands training data. Simulations show that the prototype is able to learn paths that exploit cross-competency structures and benefit from virtual students when interaction samples are small. True educational effectiveness remains a follow-up empirical question.
