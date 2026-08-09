# Questions, CAT and offline data

## 1. Basic objects of CAT

Let item bank be

\[
\mathcal J=\{q_1,q_2,\ldots,q_{|\mathcal J|}\}.
\]

The student’s true ability or knowledge status is recorded as

\[
\theta_i^0\in\mathbb R^d,
\]

It is often considered fixed but unknown in short CAT. Student \(i\)’s binary response to question \(q\) is recorded as \(a\in\{0,1\}\), where 1 indicates a correct answer and 0 indicates an incorrect answer.

The response model \(M\) is given

\[
M(q\mid \theta_i)
\approx
\Pr(a=1\mid q,\theta_i).
\]

A CAT with a fixed length of \(T\) is run in the following sequence:

1. Starting from the current student parameter estimate \(\widehat\theta_i^{\,t-1}\) and answer history;
2. The question selection algorithm selects the unanswered question \(q_t\);
3. Observe the students’ answers \(a_{i(t)}\);
4. Update \(\widehat\theta_i^{\,t}\) with accumulated answers;
5. Repeat to step \(T\), or reach the stopping conditions such as accuracy and time.

Traditional IRT-CAT commonly uses predefined criteria such as Fisher information, Kullback-Leibler information or posterior variance. NCAT makes the question selection function itself learn from the data.

## 2. Three easily confused learning objects

### Student parameters

\(\theta_i\) is the local state for student \(i\). Each time a new answer is obtained, the response model can reestimate it.

### Response model parameters

Item difficulty, discrimination, guessing parameter, or NCDM's item/knowledge point network parameter are global parameters learned in advance from large-scale training data. CAT usually freezes these global parameters when administering the test and only updates the local representation of new students.

### Topic selection network parameters

\(\phi\) is a global parameter of the NCAT policy. After offline training is complete, \(\phi\) is typically frozen when deployed to new students. The policy remains adaptive because its input state \(s_t\) changes at every step.

!!! tip "Parameter freezing and adaptation do not conflict"

    Adapt to real-time changes in function inputs:

    \[
    q_t=\arg\max_{q\in\mathcal A_t} Q_\phi(s_t,q).
    \]

    Even if \(\phi\) is fixed, the student's just answer will change the ordering of \(s_t\), the legal action set \(\mathcal A_t\), and all candidate questions.

## 3. What are the minimum requirements for historical logs?

The minimum answer record can be expressed as:

|Field|Example|Purpose|
|---|---:|---|
| `user_id` | 18 |Identify students|
| `exer_id` | 1370 |Identify item|
| `score` |0 or 1|Constructing status and reading offline answers|
| `knowledge_code` | `[3, 11]` |Compute knowledge point coverage and support NCDM|

Formal research should also retain the timestamp, response time, item version, number of attempts, presentation location, original logging policy, and presentation probability. They relate to duplicate response processing, time drift, and offline policy evaluation.

The original warehouse organized a student as:

```json
{
  "user_id": 18,
  "log_num": 4,
  "logs": [
    {"exer_id": 2, "score": 1, "knowledge_code": [3]},
    {"exer_id": 7, "score": 0, "knowledge_code": [3, 11]},
    {"exer_id": 9, "score": 1, "knowledge_code": [11]},
    {"exer_id": 12, "score": 0, "knowledge_code": [5]}
  ]
}
```

## 4. First segment by students, and then cut topics within students.

NCAT uses two levels of splitting.

### Student level segmentation

The paper undergoes 5-fold cross-validation; the students in each fold are divided into training, verification and testing students according to 60%/20%/20%. Test students will not participate in the training of policy parameters \(\phi\).

### Internal segmentation of students

For each student \(i\), his historical answers are randomly divided into:

\[
\mathcal D_i^s \quad\text{support set},
\qquad
\mathcal D_i^u \quad\text{query set},
\qquad
\mathcal D_i^s\cap\mathcal D_i^u=\varnothing.
\]

The paper uses about 70% support, 30% query, and re-randomly splits each training epoch to reduce overfitting.

- The questions in support form candidate actions; the corresponding historical answers are allowed to be read only after the strategy is selected;
- The query questions are isolated from the candidate set, and only whether the current student parameters can be generalized to questions not used for adaptation are evaluated.

At step \(t\), the record selected from support is

\[
\mathcal D_i^s(t)
=
\{(q_1,a_{i(1)}),\ldots,(q_t,a_{i(t)})\}.
\]

The current set of legal actions is

\[
\mathcal A_i^t
=
\{q:(q,a)\in\mathcal D_i^s\}
\setminus
\{q_1,\ldots,q_{t-1}\}.
\]

## 5. How to simulate question-by-question feedback in offline training

Assume that student \(i\)'s answers to 100 questions are known in the history log. You can select some of them as support during training, but the algorithm cannot stuff all the support answers into the state in advance.

An offline interaction is:

1. The strategy only looks at the revealed answer history;
2. Select \(q_t\) in the unselected support question;
3. The historical answer \(a_{i(t)}\) for \(q_t\) in the environment query log;
4. Append \((q_t,a_{i(t)})\) to the state;
5. Update student parameters;
6. Calculate the prediction loss on the query set and form reward.

This preserves the chronological order of information in CAT: future answers are not visible until they are selected.

## 6. Correspondence between training environment and real deployment

|stage|Where does the answer to the next question come from?|The role of query set|Whether to update strategy parameters|
|---|---|---|---|
|Offline training|History log|Calculate reward and train \(Q_\phi\)|Yes|
|Verification/offline testing|History log|Calculate ACC/AUC/BCE|No|
|New student deployment|Students answer in real time|There is no visible query truth value|No|

Query reward is not required during deployment. Training has compressed "what historical states and actions usually lead to better subsequent measurements" into \(Q_\phi\).

## 7. Differences in segmentation between the original paper and the public code

The current snapshot of the public warehouse is not completely consistent with the experimental protocol of the paper:

|item|Paper|Public warehouse snapshot|
|---|---|---|
|Student level segmentation|60%/20%/20%, 50% off|About 80%/10%/10% in `env.py`|
|support/query within students| 70%/30% |`split_data(ratio=0.5)`, that is 50%/50%|
|Maximum test length| \(T=20\) |The shell example is \(T=10\)|
|replay capacity| 10,000 |`Train.py` constant is 50,000|

When reproducing paper results, the paper protocol should be used as the main focus, and code changes should be recorded in the experimental configuration. Commit and run configurations should be accurately reported when reproducing repository behavior.

## 8. Offline support for domain restrictions

Questions that have not been answered by history students have no answers that can be queried in this offline environment. Therefore, the candidate set can only come from support questions that the student has actually answered.

This creates an important boundary: the model learns the rearrangement strategy within historical observable items. If the old system rarely presents certain questions to certain types of students, NCAT also lacks the result data for these state-actions.

!!! warning "Randomly switching support/query cannot eliminate logging-policy bias"

    Random segmentation only prevents the same question from entering adaptation and evaluation at the same time. It does not create counterfactual answers that the old strategy never collected, nor does it automatically correct bias caused by different item presentation probabilities. Offline conclusions still need to be reinforced by joint support, propensity scores, OPE or online experiments.

The next page will write this environment as [double-level goal, MDP and reward](02-objective-and-mdp.md).
