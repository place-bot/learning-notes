# Training and real student deployment

This page strings the previous goals, states, response models and Q-learning into two complete algorithms: offline training and online test-by-question.

## 1. Phase 1: pretraining response model

First use the historical responses of training students to estimate the global parameters of the response model \(M\):

- IRT: item difficulty, discrimination, etc.;
- MIRT: multi-dimensional item vector;
- NCDM: Neural parameters of students, items and knowledge points.

After entering NCAT training, the global item parameters remain fixed. For each simulated student, only the student's local parameters are updated with the currently selected support question.

In this way, the change in reward can be mainly attributed to the topic selection trajectory, rather than the simultaneous drift of the global parameters of the response model.

## 2. Phase 2: Generating a trajectory for a history student

For training students \(i\):

1. Randomly divide \(\mathcal D_i^s\) and \(\mathcal D_i^u\);
2. Initialize the empty state \(s_1\) and student local parameters;
3. Press epsilon-greedy to select \(q_t\) in the legal support question;
4. Read \(a_{i(t)}\) from the history log;
5. Update \(\widehat\theta_i^{\,t}\) with \(\mathcal D_i^s(t)\);
6. Calculate query BCE and \(r_i^t\);
7. Form \(s_{t+1}\);
8. Deposit \((s_t,q_t,r_i^t,s_{t+1},d_t)\).

The topic-by-topic evolution of status is as follows:

\[
s_1=\varnothing,
\]

\[
s_2=\{(q_7,1)\},
\]

\[
s_3=\{(q_7,1),(q_3,0)\}.
\]

The second step of action is decided after seeing the correct response of \(q_7\); the third step of action will be affected by the incorrect response of \(q_3\).

## 3. Phase 3: Update Q network from replay batch

After extracting mini-batch:

1. Convert each \(s_t\) into a wrong answer sequence, a correct answer sequence and a mask;
2. Calculate \(Q_\phi(s_t,\cdot)\);
3. `gather` predicts the real action \(q_t\);
4. Calculate the maximum Q value in legal actions for \(s_{t+1}\);
5. Construct TD target;
6. Minimize TD MSE;
7. Update online network;
8. Synchronize the target network as scheduled.

```python
q_all = online_net(state)
q_taken = q_all.gather(1, action[:, None]).squeeze(1)

with torch.no_grad():
    next_q = target_net(next_state)
    next_q = next_q.masked_fill(~next_valid_mask, float("-inf"))
    next_best = next_q.max(dim=1).values
    next_best = torch.where(done, torch.zeros_like(next_best), next_best)
    target = reward + gamma * next_best

loss = torch.nn.functional.mse_loss(q_taken, target)
optimizer.zero_grad()
loss.backward()
torch.nn.utils.clip_grad_norm_(online_net.parameters(), 5.0)
optimizer.step()
```

## 4. Offline training pseudocode

```text
Input:
    Historical student data D
    pretraining response model M
    Maximum test length T

Initialization:
    online Q network Q_phi
    target network Q_bar_phi
    replay buffer B

Repeat for several epochs:
    For each training student i drawn:
        Randomly split support D_i^s and query D_i^u
        state <- empty
        Reset the student's local parameters

        For t = 1,...,T:
            valid <- unselected support questions and other hard constraints
            action <- epsilon-greedy(Q_phi(state), valid)
            answer <- the answer to the question in the history log
            Update student local parameters theta_hat_i^t
            reward <- - query_BCE(D_i^u, theta_hat_i^t)
            next_state <- state + (action, answer)
            done <- whether T or stop condition is reached
            B.add(state, action, reward, next_state, done)
            state <- next_state

    If there are enough samples in B:
        Draw mini-batch from B
        Construct masked Bellman target
        Update phi

    Periodic synchronization bar_phi <- phi
    Select hyperparameter on the verification student and stop early
```

## 5. Complete closed loop of deploying new students

After training, new students have no support/query segmentation and no hidden rewards. The system uses the real item bank:

```text
Input:
    Global parameters of the trained response model
    Trained Q network
    Real item bank and constraints

Initialization:
    state <- empty
    theta_hat <- prior or initial student representation
    asked <- empty

Repeat:
    valid <- item bank minus asked, and then apply constraints such as content, question, exposure, etc.
    Calculate Q(state, ·)
    Select a question q from valid argmax or according to temperature distribution
    Present q to students
    Receive real-time answers a
    state <- state + (q, a)
    asked <- asked + q
    Update theta_hat with cumulative answers

    If the stopping rule is met:
        Output theta_hat, standard error or diagnostic result
        end
```

!!! tip "Where does real-time feedback go in"

    Each time a student submits an answer, \((q_t,a_t)\) immediately writes the status; the response model updates the student parameters; the NCAT encoder recalculates the dual-channel attention; the action mask deletes the answered questions; and then \(q_{t+1}\) is selected. This is question-by-question adaptation.

## 6. stopping rule

The original paper experiment is fixed length \(T=20\), but the real CAT can use:

- Reach the maximum number of questions;
- ability estimatestandard error is lower than the threshold;
- The posterior credible interval is narrow enough;
- The classification decision-making reliability reaches the threshold;
- The knowledge point blueprint has been met;
- Time budget exhausted;
- The marginal utility of asking one more question is expected to be less than the cost.

If \(T\) is always fixed during the training phase, and the deployment uses variable-length stops, the training goal is best to explicitly cover different stop steps, or to incorporate the `done` mechanism and stop state into the environment.

## 7. Three strategies of training, evaluation and deployment

|stage|Topic selection method|purpose|
|---|---|---|
|training| epsilon-greedy |Exploration state-action space|
|Offline review|argmax or paper temperature sampling|Compare measurements to exposure metrics|
|deploy|Constrained argmax/sampling|Compromising accuracy, safety and blueprints|

The random seed should be fixed and sampled multiple times during evaluation; otherwise, the single random trajectory generated by the temperature strategy will make the resultvariance very large.

## 8. How to access content and security constraints

The question \(q\) belongs to the content category \(c(q)\). Each type of question has a lower limit \(L_k\) and an upper limit \(U_k\). In step \(t\), a feasible set can be constructed first:

\[
\mathcal A_t^{\mathrm{feasible}}
=
\left\{
q\in\mathcal A_t:
\text{Select}q\text{There is still a feasible path to complete the blueprint}
\right\}.
\tag{1}
\]

Then compare the Q values only on that set:

\[
q_t
=
\arg\max_{q\in\mathcal A_t^{\mathrm{feasible}}}
Q_\phi(s_t,q).
\tag{2}
\]

Simple upper bounds can be handled with mask; when satisfying multiple content lower bounds, enemy questions, question groups, time and exposure constraints at the same time, shadow test or integer programming is more reliable. Soft punishment can be added to reward:

\[
r_t^{\mathrm{total}}
=
r_t^{\mathrm{measure}}
-\lambda_{\mathrm{content}}C_t
-\lambda_{\mathrm{exposure}}E_t
-\lambda_{\mathrm{time}}H_t.
\tag{3}
\]

Among them, \(C_t,E_t,H_t\) represents content bias, exposure risk and time cost respectively. Soft penalties are used for trade-offs, and hard masks or combinatorial optimization layers are used to ensure feasibility.

The next page uses a set of small data to completely walk through [status coding, topic selection, student update, reward and TD update](06-worked-example.md).
