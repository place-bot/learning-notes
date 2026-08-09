# Limitations, method comparison and future work

## 1. NCAT, BOBCAT and Traditional CAT

|Dimensions|Traditional Information CAT| BOBCAT | NCAT |
|---|---|---|---|
|Basis for topic selection|Fisher/KL/posterior variance and other default criteria|Double-layer optimization of meta question loss|The long-term Q value of query loss reward|
|Decision frequency|Re-select each question|Rerun the strategy for each question|Rerun the Q network after answering each question|
|learning source|Response models and human inference|History student answers|History student answers|
|training method|Usually no strategy training|meta-gradient / approximate gradient| Q-learning |
|Status representation|Current capabilities and uncertainties|response state vector|Correct/wrong answer dual-channel attention|
|long term portfolio value|criterion is mostly a local step|Outer objective evaluation of the entire group of selected topics|Bellman returns explicitly represent the future|
|response model|Often closely integrated with IRT|Can be connected to IRT or neural models|Can be connected to IRT or neural models|
|Main explanatory|high|medium|lower|
|Major engineering risks|model mismatch|meta-gradient and approximate bias|Offline RL, training stability, and representation leakage|

For more detailed BOBCAT objectives and algorithms, see [Double-layer Optimization](../bobcat/02-bilevel.md) and [Framework and Algorithm](../bobcat/03-framework.md).

If the action is changed to learning materials and the status is changed to continuous ability after learning, Q-learning corresponds to the outer teaching recommendation. The complete model, transfer estimator and simulation evidence are available in [Deep RL Adaptive Learning](../adaptive-learning-drl/index.md).

## 2. Key differences from recommendation system “generated sequence”

Recommendation pages often display multiple products at the same time, and users may click on one of them or not. CAT typically presents only one question per step, and the answer to that question is the key observation that updates the measurement state.

Therefore, the core object of CAT should be written as a closed-loop strategy:

\[
\pi:
s_t
\longmapsto
q_t,
\]

A real test path is generated jointly by the strategy and the students:

\[
q_1,a_1,q_2(a_1),a_2,\ldots,q_T(a_{1:T-1}).
\]

If a fixed sequence is output at one time

\[
(q_1,q_2,\ldots,q_T),
\]

The subsequent questions do not use the students' midway answers, so the question-by-question branching is lost. A "generative CAT" that remains adaptive can generate:

- The next question token will be regenerated after receiving the answer;
- Conditional strategy tree;
- Short horizon with rolling re-planning according to the status;
- Action distribution with legality constraints.

NCAT falls into the first category: output the next question each time.

## 3. Support domain for historical logs

The offline environment can only read answers that actually happened in history. If the old system has never presented the question \(q\) to a certain type of students, there is no result of "Choose \(q\) in this state" in the data.

Random support/query sharding is still within the supported scope of the old logging policy. Strategies might:

- Prefer questions that are often presented in the old system;
- Mistaking presentation bias for item value;
- Unstable for new questions, low-frequency questions and new content;
- Benefit from the overlap of simulated environments with old logs in offline evaluations.

Should be recorded in the future

\[
\mu(q_t\mid s_t),
\]

That is, the probability of selecting the question under the current state of the old strategy, and study IPS, doubly robust, FQE or conservative offline RL. Actions without mutual support still cannot be restored with stat modifiers.

## 4. Query prediction only measures proxy

For NCAT

\[
\mathcal L_M(\mathcal D_i^u,\widehat\theta_i)
\]

Proxy for unobservable true capability errors. This proxy will inherit the assumption of response model \(M\):

- IRT dimension setting is wrong;
- NCDM is insufficiently calibrated;
- item parameters drift;
- Partial independence is not established;
- query is inconsistent with the target measurement blueprint.

Future experiments should also report:

- query BCE、ACC、AUC；
- Ability parameter recovery under simulation conditions;
- standard error, coverage rate and calibration;
- mastery classification accuracy and decision-making consistency;
- Downstream teaching decision-making utility.

## 5. Reward design and training are similar

The outer target of the paper gives equal weight to each step of query loss; when DQN uses \(\gamma<1\), it will bias towards early performance. Absolute negative loss reward will also produce strongly correlated, overall negative feedback.

Comparable:

\[
r_t^{\mathrm{absolute}}=-L_t,
\]

\[
r_t^{\mathrm{gain}}=L_{t-1}-L_t,
\]

\[
r_t^{\mathrm{risk}}
=
-\mathbb E
\left[
\text{decision loss after step }t
\right],
\]

As well as directly using posterior entropy, parameter error or multi-objective reward. Each reward corresponds to a different test effect and cannot be selected based solely on the training curve.

## 6. Content, question types and examination constraints

The paper observes a high coverage of knowledge points, but does not guarantee a content blueprint. Formal exams may also include:

- Upper and lower limits for the number of questions in each content category;
- Question type and cognitive level ratio;
- Completeness of the question set;
- Rival questions cannot be in the same paper;
- Reading materials come before subordinate questions;
- response time budget;
- upper limit of item exposure;
- Accessibility and language version requirements.

Let \(z_j\in\{0,1\}\) represent the question whether \(j\) enters the current shadow test, which can be solved:

\[
\max_{\mathbf z}
\sum_{j\in\mathcal J}
z_jQ_\phi(s_t,q_j)
\]

satisfy

\[
L_k
\le
\sum_{j:c(j)=k}z_j
\le
U_k,
\qquad
\sum_jz_j=H,
\]

Then present the first question from the optimal shadow test. Each time a new answer is obtained, the solution is solved again and the closed-loop adaptation is still maintained.

## 7. Exposure and Safety

Temperature sampling reduces the average exposure in the paper, but randomization only provides soft dispersion. Formal controls can be used:

- Accept/reject mechanisms such as Sympson-Hetter;
- Real-time maximum exposure quota for each question;
- item bank stratification and rotation;
- Constraint MDP;
- Incorporate exposure status into \(s_t\);
- Block quota-exceeded questions in the legal action mask.

Fairness assessments should examine exposure, measurement error, stop length, and content coverage by group to prevent overall averages from masking local differences.

## 8. Whether status and students are really static

The paper adopts the assumption that ability in short-term tests is stable and order is not important, and uses pooling to aggregate history. Educational practice scenarios may co-exist:

- Learning effect;
- fatigue;
- Warm up;
- Speed-accuracy trade-off;
- Strategy changes resulting from feedback;
- Forgetting caused by time lag.

If the process spans a long time, you can add time, sequence and feedback to the state, use a sequence model with position/time encoding, and clearly distinguish between knowledge tracking and measurement models.

## 9. New questions and item bank changes

The original NCAT policy head was

\[
\mathbb R^{4d}\to\mathbb R^{|\mathcal J|},
\]

Output dimension binding training item bank. After adding a new question, the last layer does not have a corresponding output unit, and the embedding is not trained.

A more transferable form is the learning state-item scorer:

\[
Q_\phi(s_t,q)
=
f_\phi
\left(
h_\phi(s_t),
e_\psi(q)
\right),
\]

The item representation \(e_\psi(q)\) can come from parameters, knowledge points, question stem semantics, problem-solving steps and multi-modal content. In this way, the strategy can be extended to items not seen during the training period, and an interface can be established for calibration after generating new questions.

## 10. Explainability and Auditing

Attention scores can serve as diagnostic clues but should not be taken directly as causal explanations. Can be added:

- Counterfactual: How will the next question change after removing a certain answer;
- Action value decomposition: how much measurement, content, exposure, and time contribute respectively;
- Partial comparison with Fisher information and inferior variance;
- Sensitivity testing for input answer flipping, item swapping, and padding;
- Item-level and group-level strategy cards.

## 11. Suggested research lines

### Route A: Reproduce closed-loop benefits first

1. Fixed IRT/NCDM and paper segmentation;
2. Reproduce random, MFI/KLI, MAAT, BOBCAT, NCAT;
3. Unify the legal candidate set and random seeds;
4. Simultaneously report query prediction, ability recovery and question number-accuracy curve;
5. Eliminate code differences item by item.

### Route B: Write content balance into the strategy

Compare three options:

1. Hard mask for Q value post-processing;
2. The content in reward is biased;
3. Optimization of NCAT Q value and shadow test combination.

Key metrics include blueprint feasibility rate, measurement error, coverage, maximum exposure, and solution time for each quiz.

### Route C: Offline to Online

1. Record logging probability and available set;
2. Conduct OPE within the scope of common support;
3. Use conservative strategies to improve and limit deviations from old strategies;
4. Small traffic goes online safely;
5. Monitor capability calibration, abnormal exposure, and group differences.

### Route D: Generative, migratory item representation

Change the item ID head to a state-item matcher, and use the question stem semantics, IRT/CDM parameters and knowledge points to jointly encode candidate questions. The LLM can be responsible for generating or characterizing items, and the CAT controller is still re-planning after each real answer and filtering through calibration, content, exposure and security layers.

## 12. Conclusion of this topic

The NCAT demonstrates an important possibility: question-by-question selection rules can be learned from historical responses and trained using long-term test results. It also retains the most critical interactive structure of CAT - a question, a real-time answer, a status update, and the next decision.

The paper's current evidence covers offline support/query prediction, concept coverage, synthetic noise, and average exposure. Using the method for formal testing also requires systematic extension of historical policy bias, hard constraints, item bank changes, measurement calibration, and online security.

All letters and frequently asked questions can be quickly reviewed in [symbol table and FAQ](10-symbols-faq.md).
