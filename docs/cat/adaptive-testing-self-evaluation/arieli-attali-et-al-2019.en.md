# Arieli-Attali et al. (2019): Using hidden Markov model to understand question-by-question difficulty selection

!!! abstract "Key takeaway"
    **What was done:** Arieli-Attali et al. used the item-by-item difficulty selection, correctness and error, reliability and feedback data of 583 examinees to establish a three-state hidden Markov model, and summarized the selection process into three difficulty preference states of low, medium and high that can be converted with the item. **What was gained:** Target instructions, cumulative accuracy and cumulative placement reliability can predict the initial state and state transition, indicating that difficulty selection is neither a fixed personality category nor a simple "upgrade for correct answers and downgrade for incorrect answers". **Conclusion on this topic:** Self-selected difficulty contains dynamic process information, but these states cannot be directly regarded as abilities or prior; this article only provides post-mortem explanations and does not allow HMM to drive CAT topic selection.

## Citation details

> Arieli-Attali, M., Ou, L., & Simmering, V. R. (2019). Understanding test takers' choices in a self-adapted test: A hidden Markov modeling of process data. *Frontiers in Psychology, 10*, Article 83. [DOI](https://doi.org/10.3389/fpsyg.2019.00083)

- Research type: Secondary process analysis of existing randomized experimental data
- Sample: 583 U.S. or Canadian native English-speaking adults
- Test: 24-question fixed pre-test plus 40-question adaptive general knowledge test
- Process data: seven levels of difficulty, correct or incorrect, 0–100 placement reliability and feedback for each question
- Manipulated variables: performance goal and learning goal
- Core method: three-state hidden Markov model (Hidden Markov Model, HMM)
- Main conclusion: The selection sequence can be summarized into three relatively stable potential difficulty preference states of low, medium and high; target conditions, cumulative accuracy and cumulative placement reliability jointly predict the initial state and state transition

!!! danger "The easiest place to read this article wrong"
    The paper does not let HMM drive CAT topic selection, nor does it turn the potential state into an individualized prior. It is a post hoc explanatory model of the complete 40-item choice sequence. The eye-catching transition probabilities such as 66.1% or 73.8% in the article are model predictions calculated on extreme and sparse correct rate-position reliability combinations, and are not common observation proportions in the sample.

## 1. How is this article an improvement over Revuelta (2004)?

Revuelta (2004) treats each person as using one potential selection strategy for the entire field, but his actual data have shown that exploration in the first half, stability in the second half, and static category assumptions are not good enough.

This study allows the same person to change potential states in question order:

\[
S_{i1}
\rightarrow
S_{i2}
\rightarrow
\cdots
\rightarrow
S_{i40}.
\]

Each state produces a period of different levels of difficulty choices, and the previous state, target conditions, cumulative accuracy and cumulative reliability determine the probability of the next state.

Therefore, the study population starts from:

\[
\text{“Which strategy does this person fall into?”}
\]

Steering:

\[
\text{"This person is in the}t\text{What status is the question in and when will it be converted? "}
\]

This is suitable for analyzing the dynamic self-assessment signal in the previous question \(k\).

## 2. Why the choice of difficulty may have multiple psychological sources

Also choose high difficulty, which may come from:

-Higher real ability;
- A high estimate of one's abilities;
- Like challenges;
- Active exploration under learning goal;
- Overconfidence;
- Strategic responses to feedback.

The same choice of low difficulty may also come from:

- Low real ability;
- Lack of self-confidence;
- Hope to maximize the number of correct answers;
- Reduce stress;
- Complete the task with minimum effort.

So choice level is not a pure measure of ability. The author introduces Feeling of Knowledge (FOK) and goal orientation into the model, trying to distinguish how external correct feedback and internal confidence judgment jointly promote choice changes.

## 3. What experiment does the data come from?

### 3.1 Sample

Data from Arieli-Attali (2016):

- \(N=583\)；
- Age 18–74 years, mean 33.09 years;
- 45% female;
- Recruited via Amazon Mechanical Turk;
- Native English speakers and residents of the United States or Canada only.

The original experiment lasted for two days, and this article only uses the data from day 1.

### 3.2 Fixed pre-test

Participants first completed 24 non-adaptive open-ended general knowledge questions. The range of pre-test accuracy is:

\[
.22\text{to}1.00,
\qquad
M=.75,
\qquad
SD=.16.
\]

### 3.3 Random target conditions

Then randomly divided into:

- Performance goal: 286 people were asked to maximize their test scores and were given incentives;
- learning goal: 297 people were asked to use the test on that day as a learning tool for the test on the next day.

Therefore, between-group differences in target conditions are closer to causal explanations than within-group correlations between accuracy and reliability.

### 3.4 40 questions self-adapted testing

The process for each question is:

1. Choose difficulty from seven levels;
2. Answer an open-ended general knowledge question;
3. Report reliability as 0, 10, 20, ..., 100;
4. Get correctness feedback and correct answers after submission;
5. Select the difficulty level of the next question.

Correct is recorded as 1 and incorrect as 0; set reliability and scale it to \([0,1]\); divide the difficulty level by 7 to convert it to a value of approximately \([.14,1]\).

The author mentioned that the original experiment also studied different feedback conditions, but this HMM did not include this factor into the model. If the feedback manipulation affects choice shifting, this omission may leave some of the variance in the residuals or other covariates.

## 4. How difficult are the seven difficulty levels?

The average IRT difficulty and average correct answer probability of the seven-layer items are:

|level|average item difficulty|average probability of correct answer|
|---:|---:|---:|
| 1 | -3.3 | 92% |
| 2 | -1.8 | 80% |
| 3 | -0.9 | 68% |
| 4 | -0.2 | 55% |
| 5 | 0.5 | 41% |
| 6 | 1.0 | 30% |
| 7 | 1.8 | 16% |

The author treats the seven-level selection as a continuous variable because the number of categories reaches seven and it can approximate a continuous difficulty axis.

!!! warning "The level numbers are equidistant, but the actual \(b\) is not"
    The model uses a normal emission distribution for \(1/7,2/7,\ldots,7/7\), which is equivalent to treating adjacent grade spacing as the same. However, the actual average intervals of \(b\) are approximately 1.5, 0.9, 0.7, 0.7, 0.5 and 0.8, which are not equidistant. If the research goal is to precisely connect selection to item parameters, it would be more natural to use the actual \(b\) or ordered category emission model.

## 5. Two-layer structure of HMM

### 5.1 Observation layer: How does the potential state generate difficulty selection?

Remember that the potential state of individual \(i\) in question \(j\) is:

\[
S_{ij}\in\{1,\ldots,M\},
\]

The observed difficulty choice is \(Y_{ij}\). The author assumes:

\[
Y_{ij}\mid S_{ij}=m
\sim
N(\mu_m,\sigma_m^2).
\]

After the potential state is given, the selection conditions of each question are independent. The larger the state mean value is, the more difficult the question is that the examinee tends to choose at that point in time.

### 5.2 State layer: how the state changes over time

The potential state satisfies a first-order Markov process:

\[
P(S_{ij}\mid S_{i,1:j-1})
=
P(S_{ij}\mid S_{i,j-1},\mathbf h_{ij}).
\]

Here \(\mathbf h_{ij}\) is a covariate that changes with the question. Although the state only directly depends on the previous state, the cumulative accuracy and cumulative reliability compress the earlier history into covariates, so this is not "completely forgetting the earlier items", but retaining the history through summaries.

## 6. Initial state model

Initial state probabilities use multinomial logistic regression:

\[
P(S_{i1}=m\mid\mathbf I_i)
=
\frac{
\exp(a_m+\mathbf b_m^\top\mathbf I_i)
}{
\sum_{k=1}^{M}
\exp(a_k+\mathbf b_k^\top\mathbf I_i)
}.
\]

The covariates are:

\[
\mathbf I_i
=
(d_i,p_i,d_ip_i),
\]

Among them:

- \(d_i\): target conditions, performance=1, learning=0;
- \(p_i\): 24 questions pre-test accuracy rate;
- \(d_ip_i\): The two interact.

This part asks how target instructions and existing ability performance change the starting probabilities of low, medium, and high states before seeing the first self-choice question.

## 7. State transition model

The probability of going from the previous state \(l\) to the current state \(m\) is:

\[
P(S_{ij}=m\mid S_{i,j-1}=l,\mathbf h_{ij})
=
\frac{
\exp(c_{lm}+\mathbf d_{lm}^\top\mathbf h_{ij})
}{
\sum_{k=1}^{M}
\exp(c_{lk}+\mathbf d_{lk}^\top\mathbf h_{ij})
}.
\]

The covariates for the full model are:

\[
\mathbf h_{ij}
=
(d,r,f,dr,df,rf,drf),
\]

Among them:

- \(r\): cumulative average accuracy;
- \(f\): cumulative average reliability;
- The rest are second- and third-order interactions.

The model is estimated by `depmixS4` using the Expectation-Maximization (EM) algorithm; the Viterbi algorithm is used to give the most likely state path.

## 8. Why does the number of model parameters increase so quickly?

For \(M\) states, the complete number of model parameters is:

\[
2M
+
4(M-1)
+
8M(M-1).
\]

The three parts are:

1. Each state has a mean and a variance, totaling \(2M\);
2. \(M-1\) logistic equations in the initial state, each containing an intercept and three covariates, totaling \(4(M-1)\);
3. Transition equations from each source state to \(M-1\) non-reference target states, each containing an intercept and seven covariates, totaling \(8M(M-1)\).

When \(M=3\):

\[
6+8+48=62
\]

parameters, consistent with the full model B3 in Table 1. The large number of higher-order interactions makes interpretation dependent on plotting predicted probabilities rather than reading regression coefficients directly.

## 9. What does the original selection sequence tell us first?

### 9.1 People who are fixed at extreme levels

Always choose level 1 for the entire 40-question session:

- Performance goal: 33 people, accounting for 11.54%;
- learning goal: 10 people, accounting for 3.37%.

Always choose level 7 throughout the game:

- performance goal: 3 people, accounting for 1.05%;
- learning goal: 5 people, accounting for 1.68%.

The learning group was significantly less likely to take the “easiest of the whole” path.

### 9.2 learning group switches more often

Average number of observed grade increases:

\[
7.43\text{（learning）}
\quad\text{vs.}\quad
6.07\text{（performance）}.
\]

Average number of downward adjustments:

\[
6.51\text{（learning）}
\quad\text{vs.}\quad
5.40\text{（performance）}.
\]

### 9.3 Select distribution

Among all \(583\times40=23{,}320\) choices, level 1 accounts for 22.85%, level 4 accounts for 19.67%, and level 3 accounts for 16.13%; the difficulty selection is not a unimodal normal distribution, but more like a mixture of multiple preference distributions.

### 9.4 Correlation of three variables

\[
\operatorname{Cor}(\text{Difficulty selection},\text{Correct})=-.30,
\]

\[
\operatorname{Cor}(\text{Difficulty selection},\text{Confidence})=-.28,
\]

\[
\operatorname{Cor}(\text{Correct},\text{Confidence})=.60,
\]

Both report \(p<.001\). When the choice is more difficult, the correct answer rate and reliability are on average lower; correctness and confidence are generally more consistent.

### 9.5 Why is sequence model needed?

After removing participant and item effects, the average first-order autocorrelation of difficulty selection residuals is approximately:

\[
\rho_1\approx.44.
\]

There is a clear time dependence between the choices, and the 23,320 choices cannot be treated as independent observations.

## 10. Why choose three states in the end?

The two-state and three-state models without covariates are:

|model|Number of states| AIC | BIC |
|---|---:|---:|---:|
| A | 2 | -16658.95 | -16602.55 |
| B | 3 | -27223.54 | -27110.74 |

Both AIC and BIC clearly support the three-state model. The three emission distributions are:

\[
\mu_L=.19,\quad \sigma_L=.07,
\]

\[
\mu_M=.51,\quad \sigma_M=.12,
\]

\[
\mu_H=.86,\quad \sigma_H=.13.
\]

After multiplying back to 7, the state center approximately corresponds to the observation level:

\[
1.33,quad3.57,quad6.02.
\]

So low, medium, and high are concise labels for difficulty selection preferences.

!!! warning "Latent state is not a validated psychological construct"
    The three states are low, medium, and high difficulty preferences identified from the choice distribution. The authors further interpret them as self-assessed abilities and/or motivational states, but there are no external scales or experimental manipulations to verify these two meanings respectively. To call it a "low ability state" or a "low motivation state" would be more than the data supports.

## 11. How stable are the three states?

The transfer matrix for model B without covariates is approximately:

\[
\mathbf P=
\begin{pmatrix}
.93 & .05 & .02\\
.04 & .92 & .04\\
.04 & .06 & .90
\end{pmatrix}.
\]

Rows represent the current state and columns represent the next state. All three states have self-maintenance probabilities of at least .90.

This explains an apparent contradiction: the observed rank may frequently change from 3 to 4 or from 6 to 5, but these changes may simply be random fluctuations in the same underlying preference state and do not imply a true shift in motivation or self-judgment.

The same observation level can also belong to different potential states. For example, if level 4 is sandwiched in a series of high-difficulty choices, it may be judged by the HMM as an accidental low choice of high status; if it appears after a lower sequence, it may belong to the medium status.

## 12. The initial state is affected by pretest and target conditions

The B1 model that adds pretest, target conditions, and interactions fits better than the B model without covariates:

\[
\Delta\chi^2=71.26,
\qquad
\Delta df=6,
\qquad
p<.05.
\]

The main modes are:

- The higher the pre-test, the greater the probability of initially being in a medium or high state;
- After controlling for the pretest, the performance group has a higher probability of initially being in a low state;
- Below about 50% on the pretest, both groups have more than half the predicted probability of entering the low state.

For example, when the pretest is .50, the low state probability given in Figure 6 is approximately:

\[
.619\text{（performance）}
\quad\text{vs.}\quad
.507\text{（learning）}.
\]

This shows that the difficulty selection of the first question contains both ability clues and goal orientation clues. Directly equating choice levels with ability would misinterpret preference differences caused by experimental instructions as ability differences.

## 13. How target conditions affect state transitions

B2a, which only adds the target condition to the transition model, has a better likelihood ratio test than B1:

\[
\Delta\chi^2=35.89,
\qquad
\Delta df=6,
\qquad
p<.05.
\]

Starting from a low state:

|Conditions|stay in low state|Go to mid state|Go to high state|
|---|---:|---:|---:|
| performance | .943 | .041 | .016 |
| learning | .906 | .071 | .023 |

The total probability of upgrading from a low state is about .094 for the learning group and about .057 for the performance group. The transitions from the medium and high states of the two groups are very similar.

Thus, the difference in goal conditions was not primarily about making people in all positions upregulate generally, but rather making people in the low-difficulty preference state more likely to leave the low state.

## 14. How accuracy and reliability jointly predict transfers

B2b uses cumulative accuracy \(r\), cumulative reliability \(f\) and interactive prediction transfer, compared to B1:

\[
\Delta\chi^2=219.83,
\qquad
\Delta df=18,
\qquad
p<.05.
\]

The main modes are:

1. When the cumulative accuracy rate is high, most people remain in the original state regardless of reliability;
2. When the cumulative accuracy rate is low, both up and down transfers increase;
3. When the accuracy rate is low and the confidence is low, the prediction probability of downgrading from the medium state is 22.3%;
4. When the accuracy rate is low and the confidence is high, the prediction probability of downgrading from the high state is 27.7%;
5. Also at the extreme point of low accuracy and high confidence, the total prediction probability of upward adjustment from the low state reaches 66.1%.

Point 5 may seem counter-intuitive: People who have answered a lot of questions wrong but are still very confident may actually jump up from a low state. The author borrows the attention/surprise mechanism explanation of hypercorrection and believes that high-confidence error feedback may make people change strategies or increase effort.

!!! warning "66.1% is an extreme prediction, not a common observation frequency"
    Figure 8 shows the continuous model using the four extreme combinations of "all wrong answers/all correct answers" and "lowest/highest reliability". Figure 9 shows that as the number of questions increases, the accuracy and reliability are increasingly clustered on the diagonal, and the samples in the overconfidence and underconfidence quadrants are very sparse. So 66.1% is sensitive to parameter form and extrapolation and should not be written as "about two-thirds of overconfident people adjust the difficulty".

## 15. Complete interaction model and model selection differences

B3 adds the target conditions and all second-order and third-order interactions with accuracy and reliability to the transition model. Compared to B2b:

\[
\Delta\chi^2=68.67,
\qquad
\Delta df=24,
\qquad
p<.05.
\]

When the accuracy is extremely low, the confidence is high, and starting from a low state, the upward adjustment probability is approximately:

\[
73.8\%\text{（performance）}
\quad\text{vs.}\quad
65.2\%\text{（learning）}.
\]

The full model also predicts more upregulation in the performance group at the extreme points of high accuracy, low confidence.

However, different criteria give different conclusions:

|model|Shift predictors|Number of parameters| AIC | BIC |
|---|---|---:|---:|---:|
| B1 |No new transfer predictors| 20 | -27282.80 | -27121.66 |
| B2a | goal condition | 26 | -27306.69 | -27097.20 |
| B2b |Accuracy, placement reliability and interaction| 38 | -27466.63 | **-27160.46** |
| B3 |goal, accuracy, reliability and all interactions| 62 | **-27487.31** | -26987.77 |

AIC supports the most complex B3; BIC explicitly supports B2b and considers B2a to be worse than B1 and B3 to be worse than B2b. The authors acknowledge these two BIC reversals in footnotes.

!!! important "How to quote model selection result"
    It can be said that goal interaction improves fit under LRT versus AIC, but it cannot be said that all model selection evidence supports full B3. If the research purpose is robust prediction or online use, the simplicity advantage of B2b deserves priority verification; high-order goal interactions require independent samples or cross-validation.

## 16. A chronological ambiguity that requires special checking

The research goal and discussion of the paper say that the accuracy and reliability of the "previous item" are used to predict the next state transition. But the method section also says: The cumulative accuracy and reliability of question \(j\) are calculated based on "from the beginning to question \(j\)", and \(\mathbf h_{ij}\) is used to predict the transfer from \(S_{i,j-1}\) to \(S_{ij}\).

If the implementation actually includes item \(j\) itself, temporal leakage occurs: the difficulty of item \(j\) is selected before that item's correctness and confidence are observed, so they cannot be used to predict the state of item \(j\) in real time.

The original text did not resolve this ambiguity with a code or a more precise index. Subsequent reproductions should explicitly use:

\[
r_{i,j-1}
=
\frac{1}{j-1}
\sum_{t=1}^{j-1}U_{it},
\]

\[
f_{i,j-1}
=
\frac{1}{j-1}
\sum_{t=1}^{j-1}C_{it},
\]

to predict \(S_{ij}\) instead of containing the current question result.

## 17. Why can’t HMM status directly become prior?

HMM estimate for this article:

\[
P(S_{ij}\mid Y_{i,1:40},\text{covariates}),
\]

What CAT prior requires is:

\[
p(\theta_i\mid\text{Pre-test or currently available information}).
\]

There is still a proven bridge between the two:

\[
S_{ij}
\longrightarrow
p(\theta_i\mid S_{ij}).
\]

Although low, medium, and high states are related to pretest scores, states are also affected by goal instructions, confidence bias, and feedback responses. If set directly:

\[
\mu_L<\mu_M<\mu_H
\]

And by treating them as prior means of ability, it is possible to miscalculate motivation or risk preference as ability.

A safe approach is to jointly estimate using independent calibration samples:

\[
\theta_i\mid S_{it}=m
\sim
N(\mu_m,\tau_m^2),
\]

And check the bias, coverage rate and error state transfer risk in the verification sample.

## 18. Direct inspiration for the self-assessment design of the previous \(k\) question

### 18.1 Separate comparison of static self-evaluation and dynamic status

Recommended ablation:

1. Only use the first difficulty selection;
2. Use the average value of \(k\) question selection before use;
3. Use HMM with selection plus correct error;
4. Use HMM of selection, error and reliability;
5. Add or not add target/situation variables.

Only in this way can we judge whether the complex dynamic model really exceeds the simple starting point.

### 18.2 Filtering is required for online use, and no peeking into the future is allowed.

The Viterbi path shown in the paper is a post hoc decoding of the complete sequence. Online CAT at step \(t\) can only be used:

\[
p(S_{it}\mid
Y_{i,1:t},
U_{i,1:t-1},
C_{i,1:t-1}).
\]

The choices after question \(t+1\) cannot be used to re-judge the current status. A clear distinction should be made in the simulation:

- filtering: only use current and past information, deployable;
- Smoothing/Viterbi: Utilize longer sequences, suitable for post hoc interpretation.

### 18.3 Setting reliability may increase information and interaction burden.

Asking about reliability for each question can help identify "correct answers but not confident" and "wrong answers but confident", but it will increase the test length and response burden. Comparable:

- Ask only in the first question;
- Ask the previous question \(k\);
- Ask every few questions;
- No questions at all, just answers and choices.

### 18.4 Choosing a path creates a feedback loop

\[
\text{Choose difficulty}
\rightarrow
\text{item difficulty}
\rightarrow
\text{correct and confident}
\rightarrow
\text{next time choice}.
\]

Therefore, the relationship between accuracy, placement reliability and transfer is an endogenous correlation within the system, and is not a simple effect of "increasing placement reliability will cause an increase in causality". To identify causal mechanisms requires random manipulation of feedback, confidence cues, or target conditions.

### 18.5 Dynamic state should trigger safety mechanism instead of direct force contraction

A testable design is:

- When the state posterior is concentrated and consistent with the answer, narrower prior or higher \(a\) questions are allowed to be opened earlier;
- When the status is uncertain or conflicts with the answer, the prior variance is expanded;
- The extreme overconfidence state is only used for exploratory routing and does not trigger early stopping;
- Set a minimum number of questions to prevent error states from causing short and biased tests.

This use of the HMM as a "self-rated reliability controller" is more reliable than directly translating H/M/L into capability scores.

## 19. This paper proves nothing

This article has not tested:

- Whether HMM shortens CAT;
- Whether HMM status improves the accuracy of ability estimate;
- Can the potential state construct a calibration prior;
- Whether using status topic selection improves exposure;
- Can the three-state structure be replicated across item bank, age, or mental health constructs;
- Whether the full B3 outperforms the simpler model on new samples;
- Whether the state probability is used as the basis for stopping has the correct coverage rate.

It demonstrates that a three-state HMM can provide interpretable dynamic summaries of this set of 40 question choice sequences and reveal patterns of association between goals, performance, and confidence.

## 20. Chinese paraphrases that can be quoted safely

### About dynamic strategy

> Arieli-Attali et al. (2019) used a three-state HMM to summarize the seven-level question-by-question difficulty selection into low, medium, and high difficulty preference states, and allowed the same examinee to transition between states with the order of questions.

### About state stability

> The self-maintenance probabilities for the three states in the covariate-free model are all above .90, indicating that many changes in observed levels are random fluctuations within the same underlying preference state rather than true changes in psychological state.

### About target conditions

> After controlling for pretest performance, the performance-goal group is more likely to start from a low-difficulty state and is less likely to transition upward from a low state; the difference between groups starting from a medium and high state is small.

### About correctness and confidence

> When the cumulative accuracy rate is low, state transitions increase, and there is an interaction between accuracy rate and reliability; however, the large transition probability in extreme overconfidence conditions comes from model predictions in sparse areas and should be interpreted with caution.

### About evidence boundaries

> This study is a post hoc HMM analysis of the selection process and does not let the latent state drive the online CAT, nor does it prove that the state can be directly converted into individualized capabilities prior.

## 21. How to divide the work of key references

|Literature|role in this article|
|---|---|
| Koriat（1993, 2000） |Feeling of Knowledge and Confidence Judgments|
| Dweck and Leggett（1988）；Dweck（2006） |performance and learning goal theory|
| Arieli-Attali（2016） |Original experiment, item bank and main group results|
| Rocklin and O'Donnell（1987） |Proposal of S-AT|
| Revuelta（2004） |Static latent class selection model|
| Vermunt et al.（1999） |Latent Markov model with covariates|
| Visser and Speekenbrink（2010） |`depmixS4` Software and Estimation|
| Viterbi（1967） |most likely state path algorithm|
| Butterfield and Metcalfe（2001, 2006） |High confidence errors and hypercorrection explanations|

## 22. Summary

Revuelta (2004) tells us that there is heterogeneity in selection strategies; Arieli-Attali et al. (2019) further explains that strategies also change over time:

\[
\boxed{
\text{topic by topic selection}
=
\text{latent preference status}
+
\text{Fluctuation within the state}
+
\text{Conversions influenced by feedback and goals}
}
\]

This is important for our study because first question choice is not necessarily a stable, pure signal of ability. It is affected by pretest ability, goal instruction, cumulative success, and confidence calibration.

HMM can help determine whether the self-evaluation signal is stable, consistent with the answers, and when the prior should be relaxed; however, the paper did not complete the calibration from status to ability prior, nor did it verify the benefits of online topic selection. The next methodological question is not to simply replicate the HMM, but to compare: how much predictive value is added by the dynamic state relative to a self-evaluation, and whether these increments are sufficient to compensate for the additional interaction burden and model risk.
