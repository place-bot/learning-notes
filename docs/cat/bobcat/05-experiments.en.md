#BOBCAT Experiments, Method Boundaries and Extensions

## 1. What should the experiment answer?

[Ghosh & Lan (2021)](references.md#ghosh2021bobcat)’s experiment revolves around four questions:

1. Can the response model after double-layer training use fewer items to predict the remaining responses of students?
1. Can data-driven topic selection strategies surpass Random and traditional uncertainty/Active topic selection?
1. How does the low-variance Approx gradient perform compared to the Unbiased policy gradient?
1. When the data scale increases, can learning-based topic selection continue to benefit?

Core Experiment Fixed Short Measurement Length

\[
n\in\{1,3,5,10\},
\]

Use this \(n\) question to adapt to the student parameters, and then predict the meta questions left by the student. The closer the performance-number of questions curve is to the upper left, the
It means that the prediction is more accurate for the same number of questions, or that fewer questions are needed for the same accuracy.

## 2. Dataset and preprocessing

### 2.1 Five real response data sets

|Data set|Number of students|number of items|Number of binary responses|Number of repetitions in the paper \(R\)|
| --- | ---: | ---: | ---: | ---: |
| EdNet | 312,372 | 13,169 | 76,489,425 | 1 |
| Junyi | 52,224 | 25,785 | 13,603,481 | 2 |
| Eedi-1 | 118,971 | 27,613 | 15,867,850 | 2 |
| Eedi-2 | 4,918 | 948 | 1,382,727 | 5 |
| ASSISTments | 2,313 | 26,688 | 325,359 | 10 |

The five data sets are organized into "student-item-correct or incorrect" triples. In EdNet and Junyi, the same student answers the same question
When answering multiple times, keep the first time; each student needs at least 20 responses. Supplementary material explains that Eedi’s record itself satisfies
Each student has many and non-repeated answers, so there is no need to go through the same duplicate removal steps. ASSISTments are selected from
4,217 students and 346,860 records resulted in the size in the table.

The code names the Eedi-2 data in the paper `eedi-3`, which corresponds to the 948-question version of Eedi Task 3/4. Reappearance
The data needs to be checked by item number to avoid using the paper name directly as the file name.

### 2.2 Two-layer data segmentation

The first level does cross-validation at a 50% discount per student. Use each discount:

\[
60\%\ \text{student training}
+20\%\ \text{student verification}
+20\%\ \text{student test}.
\]

The same student will only appear in one of the sets, so the test evaluation faces new students that have not been seen during the training phase.

The second level takes place within each student:

\[
\mathcal O_i
=
\Omega_i^{(1)}
\;\dot\cup\;
\Gamma_i,
\qquad
|\Omega_i^{(1)}|\approx 80\%|\mathcal O_i|,
\quad
|\Gamma_i|\approx 20\%|\mathcal O_i|.
\]

- \(\Omega_i^{(1)}\): training candidates allowed to be accessed by the question selector;
- \(\Gamma_i\): meta questions for calculating outer loss and final metrics.

During each epoch during training, candidate/meta questions within students are randomly re-divided. During verification and testing, each method uses
The same division is used to ensure that comparisons between methods are based on the same batch of targets. Experiments are repeated with multiple random partitions on small data sets,
The larger the \(R\) in the table is, the more repetitions are used to reduce the division fluctuation.

### 2.3 How to run offline CAT

On each test student, the item selector can only select items from \(\Omega_i^{(1)}\). Response of selected item from history
Query in the record, write the current status, and then select the next question:

\[
x_i^{(t)}
\to j_i^{(t)}
\to Y_{i,j_i^{(t)}}
\to x_i^{(t+1)}.
\]

The experiment therefore retains question-by-question adaptive feedback. It belongs to offline replay: if the student-item combination is not in the historical data
Observation, there is no counterfactual answer to query, and the code will not choose that combination.

## 3. Comparison methods and ablation design

The method name consists of "response model + topic selection method":

|method|response model|Response model training|Topic selection method|Main comparative effect|
| --- | --- | --- | --- | --- |
| IRT-Random | 1PL IRT |Conventional fitting|random|traditional lower bound|
| IRT-Active | 1PL IRT |Conventional fitting|\(p\) closest to 0.5|Traditional CAT baseline|
| BiIRT-Random | 1PL IRT |Two-tier meta goal|random|Isolated two-tier response training|
| BiIRT-Active | 1PL IRT |Two-tier meta goal|static uncertainty|Isolated two-tier response training|
| BiIRT-Unbiased | 1PL IRT |Two-tier meta goal| score-function/PPO |Unbiased high variance learning style topic selection|
| BiIRT-Approx | 1PL IRT |Two-tier meta goal|Approximate gradient|Low variance learning style topic selection|
| BiNN-Approx |neural response model|Two-tier meta goal|Approximate gradient|Testing the Flexible Response Model|

The prefix `Bi` indicates bilevel. The main table centrally reports IRT-Active, BiIRT-Active, BiIRT-Unbiased,
BiIRT-Approx and BiNN-Approx; Random results mainly appear in performance curves and ablation comparisons.

BiIRT-Active is critical ablation. It maintains traditional static topic selection while changing the response model to meta-target training.
The difference between IRT-Active and BiIRT-Active reflects the contribution of double-layer response training; BiIRT-Active and
The difference of BiIRT-Approx is closer to the gain of the data-driven item picker.

## 4. Model, optimization and hardware

### 4.1 Response model

BiIRT uses 1PL logistic response:

\[
p(Y_{ij}=1)=\sigma(\theta_i-b_j).
\]

BiNN feeds the student local vectors into a two-layer fully connected prediction network: 256 hidden units, ReLU, 20% dropout,
Finally, the probability of answering each question is output. The paper uses 256-dimensional student representation. Both models only adapt to the student's local area in the inner layer
Parameters, item/network parameters are shared across students in the outer layer.

### 4.2 Topic selection network

The question selector inputs the \(Q\) dimensional three-valued state, passes through two 256-unit fully connected layers and Tanh, and then selects the \(Q\) question
Output softmax probability. The Unbiased version adds a critic of the same scale, and the official code uses PPO; the Approx version uses
hard one-hot forward and softmax reverse straight-through estimator.

### 4.3 Main hyperparameter

|item|settings|
| --- | --- |
|Inner layer update steps| \(K=5\) |
|Inner layer learning rate candidate| \(\alpha\in\{0.05,0.1,0.2\}\) |
|Strategy learning rate candidate| \(0.002,\ 0.0002\) |
| PPO |4 updates, clip \(=0.2\)|
|item/network global parameters|Adam, learning rate \(10^{-3}\)|
|Global student initialization|SGD, learning rate \(10^{-4}\), momentum \(0.9\)|
|Student partial updates|\(K\) step gradient descent|
|Traditional IRT model \(L_2\) candidate| \(10^{-3},10^{-6},10^{-10}\) |
|Candidates for new student ability regularization| \(10,1,10^{-1},10^{-2},10^{-4},0\) |
| batch size | EdNet 200；Eedi-1/Junyi/ASSISTments 128；Eedi-2 512 |
|Hardware|NVIDIA Titan X or GTX 1080 Ti|

Supplementary material reports that Approx/Unbiased often takes about 10–20 hours and Active about 15–30 hours on large datasets,
Random about 5–10 hours. Running time is affected by data set, test length and hardware, and is mainly used to illustrate the magnitude.

## 5. How to calculate the indicator

### 5.1 Accuracy

For all test students’ meta-questions, first use a threshold of 0.5 to get the predicted category:

\[
\widehat Y_{ij}
=
\mathbb 1\!\left[\widehat p_{ij}>0.5\right].
\]

Calculate again

\[
\operatorname{Accuracy}
=
\frac{\sum_i\sum_{j\in\Gamma_i}
\mathbb 1(\widehat Y_{ij}=Y_{ij})}
{\sum_i|\Gamma_i|}.
\]

### 5.2 AUC

AUC ranks the predicted probabilities of all meta-questions and measures the accuracy of the correct answer when randomly selecting one correct answer and one incorrect answer.
Answers give you a chance to get a higher probability of prediction. It is less sensitive to a fixed 0.5 threshold.

!!! note "The main effect of the paper"

    "Test efficiency" here refers to using fewer selected questions to achieve similar held-out answer prediction Accuracy/AUC. Ability
    Recovering and measuring standard error, content validity, fairness, and online learning effects require additional experimental metrics.

## 6. Main experiment: Accuracy all results

The values in the table below are percentages. Each row corresponds to "data set + number of selected questions \(n\)".

|Data set| \(n\) | IRT-Active | BiIRT-Active | BiIRT-Unbiased | BiIRT-Approx | BiNN-Approx |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EdNet | 1 | 70.08 | 70.92 | 71.12 | 71.22 | 71.22 |
| EdNet | 3 | 70.63 | 71.16 | 71.30 | 71.72 | 71.82 |
| EdNet | 5 | 71.03 | 71.37 | 71.45 | 71.95 | 72.17 |
| EdNet | 10 | 71.62 | 71.75 | 71.79 | 72.33 | 72.55 |
| Junyi | 1 | 74.52 | 74.93 | 74.97 | 75.11 | 75.10 |
| Junyi | 3 | 75.19 | 75.48 | 75.53 | 75.76 | 75.83 |
| Junyi | 5 | 75.64 | 75.79 | 75.75 | 76.11 | 76.19 |
| Junyi | 10 | 76.27 | 76.28 | 76.19 | 76.49 | 76.62 |
| Eedi-1 | 1 | 66.92 | 68.22 | 68.61 | 68.82 | 68.78 |
| Eedi-1 | 3 | 68.79 | 69.45 | 69.81 | 70.30 | 70.45 |
| Eedi-1 | 5 | 70.15 | 70.28 | 70.47 | 70.93 | 71.37 |
| Eedi-1 | 10 | 71.72 | 71.45 | 71.57 | 72.00 | 72.33 |
| Eedi-2 | 1 | 63.75 | 64.83 | 65.22 | 65.30 | 65.65 |
| Eedi-2 | 3 | 65.25 | 66.42 | 67.09 | 67.23 | 67.79 |
| Eedi-2 | 5 | 66.41 | 67.35 | 67.91 | 68.23 | 68.82 |
| Eedi-2 | 10 | 68.04 | 68.99 | 68.84 | 69.47 | 70.04 |
| ASSISTments | 1 | 66.19 | 68.69 | 69.03 | 69.17 | 68.00 |
| ASSISTments | 3 | 68.75 | 69.54 | 69.78 | 70.21 | 68.73 |
| ASSISTments | 5 | 69.87 | 69.79 | 70.30 | 70.41 | 69.03 |
| ASSISTments | 10 | 71.04 | 70.66 | 71.17 | 71.14 | 69.75 |

## 7. Main experiment: AUC all results

|Data set| \(n\) | IRT-Active | BiIRT-Active | BiIRT-Unbiased | BiIRT-Approx | BiNN-Approx |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EdNet | 1 | 73.58 | 73.82 | 74.14 | 74.34 | 74.41 |
| EdNet | 3 | 74.14 | 74.21 | 74.49 | 75.26 | 75.43 |
| EdNet | 5 | 74.60 | 74.56 | 74.77 | 75.68 | 76.07 |
| EdNet | 10 | 75.35 | 75.21 | 75.39 | 76.35 | 76.74 |
| Junyi | 1 | 74.92 | 75.53 | 75.67 | 75.91 | 75.90 |
| Junyi | 3 | 76.06 | 76.52 | 76.71 | 77.11 | 77.16 |
| Junyi | 5 | 76.82 | 77.07 | 77.07 | 77.69 | 77.80 |
| Junyi | 10 | 77.95 | 77.95 | 77.86 | 78.45 | 78.60 |
| Eedi-1 | 1 | 68.02 | 70.22 | 70.95 | 71.34 | 71.33 |
| Eedi-1 | 3 | 71.63 | 72.47 | 73.26 | 74.21 | 74.44 |
| Eedi-1 | 5 | 73.69 | 73.97 | 74.54 | 75.47 | 76.00 |
| Eedi-1 | 10 | 76.12 | 75.90 | 76.34 | 77.07 | 77.51 |
| Eedi-2 | 1 | 69.00 | 70.15 | 70.64 | 70.81 | 71.24 |
| Eedi-2 | 3 | 71.11 | 72.18 | 73.11 | 73.37 | 73.88 |
| Eedi-2 | 5 | 72.42 | 73.21 | 74.19 | 74.55 | 75.20 |
| Eedi-2 | 10 | 74.36 | 75.17 | 75.37 | 75.96 | 76.63 |
| ASSISTments | 1 | 69.14 | 70.55 | 71.00 | 71.33 | 70.12 |
| ASSISTments | 3 | 71.17 | 71.60 | 72.35 | 73.16 | 71.57 |
| ASSISTments | 5 | 72.26 | 71.65 | 73.10 | 73.71 | 72.14 |
| ASSISTments | 10 | 73.62 | 72.52 | 74.38 | 74.66 | 73.59 |

## 8. result analysis

### 8.1 Overall advantages of Approx

BiIRT-Approx exceeds IRT-Active and BiIRT-Active in most settings, indicating that the learning topic selector brings
Gains beyond bi-layer training of response models. It also often exceeds BiIRT-Unbiased, consistent with having low variance gradients in finite
More stable judgment under samples and limited computing power.

The number of questions in the paper-performance curve shows:

- When BiNN-Approx reaches an accuracy similar to BiNN-Active, it can reduce the number of questions by about 50%–75%;
- When BiNN-Approx reaches an accuracy similar to BiNN-Unbiased, it can reduce the number of questions by about 10%–70%;
- On EdNet, Eedi-2 and Junyi, when BiIRT-Active achieves similar performance to IRT-Active, the number of questions can
  This is a reduction of approximately 30%, indicating that the two-layer training response model itself is also effective.

The "how much reduction question" is estimated by the horizontal axis position when the two discrete curves reach similar vertical axis values, which is suitable for explaining the efficiency trend.

### 8.2 Neural models depend on data size

BiNN-Approx generally achieves the best results on EdNet, Junyi, Eedi-1 and Eedi-2. ASSISTments size
Minimal, BiNN-Approx lags significantly behind BiIRT-Approx, showing that flexible neural response models are easier on small data
overfitting. This result also explains the reason why the paper emphasizes "large-scale student response data": Data-driven strategies and neural
The advantages of the responsive model require sufficient student and interaction support.

### 8.3 Consistency of Accuracy and AUC Conclusions

Approx leads overall in both categories of indicators, indicating that the benefits are reflected in both 0.5 threshold classification and probability ranking. individual grid
When there are inversions, such as ASSISTments, \(n=10\), the accuracy of BiIRT-Unbiased is slightly higher than
BiIRT-Approx, while the AUC of BiIRT-Approx is still higher. This reminds us to check classification thresholds, ranking, and calibration simultaneously.

## 9. Additional experiments

### 9.1 ability estimate error

The paper adds an analysis to Eedi-2 that is closer to the goals of traditional psychometrics. The author uses the student's entire history to estimate
A proxy value of "full question ability" is \(\widehat\theta_i^{\text{all}}\), and then compare the ability after the short test
\(\widehat\theta_i^{(n)}\)：

\[
\operatorname{AbilityError}(n)
=
\frac1N\sum_{i=1}^N
\left\|
\widehat\theta_i^{(n)}
-
\widehat\theta_i^{\text{all}}
\right\|_2^2.
\]

When BiIRT-Approx reaches a capability error similar to that of IRT-Active, it can use up to about 30% fewer questions. The "true ability" here
Estimated from the full history of responses, it is an empirical proxy; it is still affected by the IRT model, historical item coverage and estimation error
influence.

### 9.2 Training data volume ablation

The authors retrained students with 25%, 50%, and 100% of Eedi-2. BOBCAT continues to improve as training data increases,
IRT-Active showed smaller changes. This phenomenon conforms to the mechanism of two types of methods:

- The topic selection rules of IRT-Active are predetermined by the 1PL information structure, and the new data mainly improves parameter estimation;
- BOBCAT also learns \(\Pi_\phi\) from cross-student trajectories, and new data can directly improve the strategy.

### 9.3 Overlap of item exposure and test paper

Paper comparison on Eedi-2:

|indicator| IRT-Active | BiNN-Approx |
| --- | ---: | ---: |
|median item exposure rate| 0.51% | 0.00% |
|The proportion of items with an exposure rate exceeding 20%| 0.25% | 1.54% |
|Average overlap rate of students' pairs of test papers| 6.03% | 28.64% |

The median exposure of BiNN-Approx is 0%, and the proportion of high-exposure questions and test paper overlap is higher, indicating that the strategy concentrates the choices into a small
Some high-value items. Improved prediction efficiency is accompanied by obvious test security risks, which are also constraints added to C-BOBCAT later.
direct motivation.

### 9.4 Mutual Information Analysis: What the Strategy Learned

The author calculates the mutual information (MI) between the candidate question and the answers to other questions, and ranks them according to the frequency of occurrence of other questions.
weighted. For each selected question:

1. Find students who have answered another question;
1. Use binary joint distribution to calculate the MI of the responses to the two questions;
1. Weight it by the frequency of occurrence of another question in the data;
1. Divide the candidate questions into 10 equal frequency intervals according to weighted MI;
1. Count the ranges in which the selected questions fall.

BiNN-Approx favors the highest weighted-MI interval, and IRT-Active's selection distribution is more dispersed. This result shows
Learning strategies identify “pivot questions” that predict multiple other questions. The same mechanism will also result in increased overlap of test papers among students.

## 10. Conclusion of the paper

The paper's experiments support the following conclusions:

1. The dual-level meta goal can make the response model more suitable for the task of "predicting the remaining responses after a small number of responses";
1. Learning topic selection strategies from large-scale historical data can improve meta answer prediction under fixed short test length;
1. Approx’s biased low-variance approximation is generally more stable than the Unbiased policy gradient on five data sets;
1. The flexible neural response model has more obvious advantages in big data, while small data scenarios require stronger regularization or simpler models;
1. BOBCAT maintains question-by-question interaction, and each new answer will affect subsequent choices.

This evidence comes from offline replays on historical data, mainly evaluating held-out answer predictions. Formal high-stakes testing is also required
Evidence such as ability recovery, standard error, content validity, fairness, item exposure, and online randomized trials.

## 11. Future work

The follow-up directions clearly proposed by the paper include:

- **itemexposure control**: Limit a few items to be repeatedly selected by a large number of students;
- **Content Balance**: Ensure that the generated adaptive path meets the test blueprint;
- **bias and fairness**: Check whether the historical data bias has been amplified by policy learning.

Combining the paper results with the current generative recommendation discussion, we can continue to advance:

- **Constrained step-by-step generation**: Each step decodes the next question based on the latest answer, and uses shadow test or combined optimization to ensure
  Content, exposure, topic and item bank capacity constraints;
- **item semantic encoding**: Construct an item encoder using question stems, knowledge points and cognitive requirements to support cold start of new questions;
- **variable length and stop strategy**: use stop as an action, and use predicted risk and test cost to determine when to end;
- **Sequence and Learning Effects**: Explicit modeling of practice, feedback, fatigue and sequence effects;
- **Select bias-aware evaluation**: use propensity, doubly robust estimation or log data with exploration;
- **More complete psychometrics indicators**: adding ability/attribute recovery, conditional standard error, classification consistency and calibration;
- **Theoretical Analysis**: Study the generalization, stability and statistical properties of data-driven strategies in real CAT scenarios;
- **Online verification**: Test the causal effects of students' real interactions through small-scale randomized experiments.

## The relationship between BOBCAT and the four types of methods

### vs traditional Fisher-information CAT

The core loop of traditional CAT is

\[
\widehat\theta_i^{(t-1)}
\longrightarrow
\mathcal I_j(\widehat\theta_i^{(t-1)})
\longrightarrow
j_i^{(t)}
\longrightarrow
\widehat\theta_i^{(t)}.
\]

The topic selection criteria are predefined by the response model theory, which is highly interpretable and easy to add the standard errorstopping rule. The loop for BOBCAT is

\[
x_i^{(t)}
\longrightarrow
\Pi_\phi
\longrightarrow
j_i^{(t)},
\]

The strategy is trained by historical data, and deployment does not require \(\widehat\theta_i\) to be updated online before selecting a topic.

The two can be mixed. For example, use Fisher information, content categories, and current ability estimates as policy network inputs, or give
Measurement accuracy constraints are added to the outer layer of BOBCAT.

### and active learning

The common denominator is to progressively select the most valuable tag requests from the candidate pool. The difference is that ordinary pool-based active
learning typically selects samples to improve a global classifier, while an episode of BOBCAT targets a single student,
Responses are specific to that student, and observations are selected for local adaptation.

Uncertainty sampling only looks at current forecast uncertainty. BOBCAT learned strategies leverage historical response correlations and
The meta goal is theoretically able to learn non-local and non-greedy patterns.

### and reinforcement learning

BOBCAT's states, actions, policies, and endpoint losses can constitute RL style episodes. Equation (8) is a typical
score-function policy gradient, the official implementation uses PPO. The difference is that the environment transfer comes from a fixed history
In response to recording, the outer objective is defined by the inner optimization, and the Approx main method does not rely on unbiased RL gradients.

Therefore, it is correct to say "BOBCAT uses RL"; it is missing to say "BOBCAT is to write CAT as MDP and then run PPO"
Response model adaptation and dual-level goals.

### and meta-learning

Each student is a task, the selected question is the support set, the meta question is the query set, and the global response parameters are shared
Initialization, local parameters are task-adapted parameters. BOBCAT learns one more support than standard MAML
set selector。

It can be summarized as

\[
\text{learn an initialization}
\quad+\quad
\text{learn what adaptation data to acquire}.
\]

### and experimental design

Optimal experimental design in psychometrics selects questions that maximize parameter information. BOBCAT is also designing observations, but the evaluation function
is data-driven held-out response prediction and allows for complex neural response models. The influence function approximates the measure of candidate observation pairs
Marginal impact on downstream targets, which has a family resemblance to information matrix-based local design.

**Table: item value under five perspectives**

|perspective|What defines item value?|main intermediate quantity|
| --- | --- | --- |
|Traditional IRT-CAT|Reduce ability estimate uncertainty|Fisher information, inferior variance|
|Active learning|Reduce model uncertainty or error| entropy、margin、expected error reduction |
|reinforcement learning|Increase cumulative returns| value、advantage、policy gradient |
|meta-learning|Improve query performance after few-step adaptation| support loss、meta loss、meta-gradient |
| BOBCAT Approx |Reduce meta answer loss after adaptation| influence score、straight-through gradient |

## The most important assumptions and limitations

### Static capability assumption

The state vector does not record the order, and the paper assumes that the student's true ability does not change during the test. If the item itself brings learning, feedback or
Fatigue, which question to ask first may change the subsequent answering mechanism. At this time, the historical response carries information about both capability measurement and capability intervention.
The original BOBCAT model did not separate measurement and learning effects.

### Historical data selection bias

The history platform uses old strategies to determine who has viewed which questions. Some student-item combinations lack observations, and the response matrix presents strategy induction
The non-missing at random.
BOBCAT can only divide candidate and meta questions from the observation set \(\mathcal O_i\). If the old strategy systematically affects certain groups
If certain types of questions are shown less, the new strategies learned may inherit bias.

More rigorous offline policy learning may require propensity weighting, doubly robust estimation, exploring the data, or
Online randomized trials. The original paper does not address the complete off-policy identification problem.

### meta Prediction and measurement validity are two types of evidence

Low meta cross-entropy indicates that the model predicts the historical response pattern well. It does not automatically guarantee that the latent variable has the intended psychological interpretation,
There is no guarantee that scores will be consistent with external benchmarks, content standards or decision-making results. For high-stakes tests, reliability, validity,
Classification accuracy, group fairness, and standard setting.

### item exposure overlaps with test

If a small number of questions are useful for many students' meta-predictions, the strategy may select them repeatedly, resulting in high exposure and high test scores.
Overlap, threatening test security. The original paper has listed exposure control and content balancing as future work.
Subsequent C-BOBCAT adds constraints to the outer layer to balance accuracy, exposure, and overlap.
[Feng et al. (2023)](references.md#feng2023cbobcat)。

### Hessian invertibility and locality of influencing functions

Equation (11) requires the inner Hessian to be reversible or at least stable to solve the corresponding linear system. Hessian of deep networks
Bizarre or morbid. Damping

\[
H_\delta=H+\delta I
\]

Numerical stability can be improved, but changes affect scores. The influence function is still a local small perturbation approximation; change the question weight from 0 to
1 is a finite change, and the local approximation may be distorted when the nonlinearity is strong.

### There is more information during training than during deployment

Approx gradient training can utilize historical answers to unselected questions in the candidate pool, and these answers are not visible during deployment. As long as they only
Used for training policy parameters, this does not constitute a direct leak; but requires that the training distribution and deployment distribution are close enough. If deploying item bank,
Strategies may fail due to changes in courses, groups, or missing mechanisms.

### item bank change problem

Both status and policy output dimensions are bound to \(Q\). After adding an item, the fixed output head cannot naturally generate new actions. need
Cold-start item selection can be achieved by using the item encoder of item features, twin tower scoring or collection network.
The question number strategy of the original paper is more suitable for the same stable item bank.

### Interpretability and Auditing

The IRT information rule can be interpreted as maximizing information at current capabilities. The reasons for neural strategy selection are harder to audit. Can record
Action probabilities, candidate impact scores, content categories, group exposure and counterfactual alternatives, and establishment of decision logs. for formal
test, "better predictions" are not a sufficient substitute for interpretable blueprint constraints.

## Checklist when reproducing and extending

### Data check

1. Divide train/validation/test by students to prevent the same students from crossing different sets.
1. For each student, only divide training/meta from the observed questions \(\mathcal O_i\).
1. Make sure \(\Omega_i^{(1)}\cap\Gamma_i=\varnothing\).
1. Ensure that the number of candidate questions for each student is at least \(n\).
1. Record the observed coverage rates of different groups, items and content categories.

### Implementation check

1. Correctly mask the selected questions and unobservable questions to avoid choosing again.
1. Clarify whether each local parameter \(t\) is reset from \(\mu\).
1. Clarify whether to use exact second-order, first-order MAML or detach.
1. The unbiased version checks the reward/loss sign to prevent high losses from being regarded as high rewards.
1. Approx version checks whether hard forward and soft backward work as expected.
1. If using influence functions, check Hessian damping and linear solution errors.
1. Whether meta loss is based on the sum of questions or the average per person, training and reporting must be consistent.

### Experimental Check

1. Compare at least Random, traditional Active, Bi-level static, Unbiased and Approx.
1. Draw performance-number of questions curves for multiple \(n\) instead of just reporting one test length.
1. Also report accuracy, AUC, log loss or calibration.
1. If you care about psychometrics, add ability/attribute recovery, classification and uncertainty coverage.
1. Report item exposure rate, test paper overlap rate, content coverage and group differences.
1. Use multiple random seeds or cross-validation to give variance.

### Diagnose training failure

**Table: Common Symptoms, Causes and Checkup Directions**

|Symptoms|Possible reasons|Priority check|
| --- | --- | --- |
|Strategy almost always chooses the same question|Softmax collapses prematurely, lacks entropy, and the historical coverage of this question is too high|Action probability entropy, exposure distribution, mask and data coverage|
|meta loss decreases while test students do not increase|Meta segmentation overfitting for training students|Strict division according to students, re-marking question sets every epoch, early stop|
|Unbiased Not learning at all|The reward variance is large, the symbols are reversed, and the critic is unstable.|advantage distribution, gradient norm, PPO ratio, loss-to-reward symbol|
|Approx gradient explosion|Hessian pathological condition, inner step size is too large, STE is unstable|Damping, gradient clipping, \(\alpha\), \(K\)|
|New questions will never be selected|The strategy is output according to fixed question numbers and lacks item features.|Introduce itemcoder and variable candidate scoring|
|Short test lengths are good, long test lengths are degraded|The policy has not been learned to eliminate redundancy and the state encoding is insufficient.|Progressive Marginal Revenue, Duplicate Content, Sequence Networks|

### Extension to cognitive diagnostic CAT

If the local parameters are changed from continuous capability \(\theta_i\) to attribute mastery probability or low-dimensional continuous embedding, the response model can be replaced by
Differentiable CDM. The inner layer updates the student representation based on the selected answer, and the outer layer can use held-out answer loss, or add attributes.
Classification loss.

But be careful: discrete mastering modes are directly \(\operatorname*{arg\,min}\) non-differentiable and usually require continuous relaxation, variational posteriors or differentiable
Master logits. If the ultimate goal is to accurately diagnose attributes rather than predict answers, the meta goal should also be changed accordingly to avoid model
Only exploit item co-occurrence without recovering interpretable attributes.

### Expand to content balancing

Assume that item \(j\) belongs to the content category \(c(j)\). The short test requires that the number of questions in each category falls within the upper and lower limits. Can be blocked in action mask
Questions that violate hard constraints, or add penalties to the outer layer:

\[
\mathcal J_{\mathrm{total}}
=\mathcal J_{\mathrm{meta}}
+\lambda_{\mathrm{content}}
\sum_c
\left(\left|\{j\in S_i:c(j)=c\}\right|-m_c\right)^2.
\]

The hard mask ensures that each test paper is feasible, and the soft penalty allows for a trade-off between accuracy and content bias. Formal tests usually use shadow
test or combinatorial optimization layers as the primary feasibility mechanism, with simple penalties providing auxiliary trade-offs.

### Expand to variable length

The original paper experiment fixed \(n\). variable length CAT needs to add a stop action, or when the prediction uncertainty is below the threshold
time to stop. If stop is used as an action, the policy must weigh one less question against the loss of prediction accuracy. The outer layer can be written as

\[
\mathcal J
=\mathcal L_{\mathrm{meta}}
+c\,T,
\]

Among them, \(T\) is the actual number of questions, and \(c>0\) is the cost of each question. This way "shortened tests" are fixed from comparing different
\(n\) becomes an explicit trade-off within the objective function.
