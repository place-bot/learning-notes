# Revuelta (2004): Modeling difficulty choices in self-adapted testing as underlying strategies

!!! abstract "Key takeaway"
    **What was done:** Revuelta put the correct and incorrect questions, difficulty selection and actual test items in self-adapted testing into the 3PL IRT plus latent class selection model to analyze when the selection mechanism can be ignored. **What is gained: **Unpresented items can be regarded as missing at random under its sequential model, but if the potential selection strategy is related to ability, the selection category probability itself also contains \(\theta\) information, which must be jointly estimated with the answer; only when the two are independent can it only be used as the answer likelihood. **Conclusion on this topic:** Self-selected difficulty is process data that may mix ability, risk preference, anxiety and feedback response. It cannot be regarded as unbiased self-report or directly become prior without calibration.

## Citation details

> Revuelta, J. (2004). Estimating ability and item-selection strategy in self-adapted testing: A latent class approach. *Journal of Educational and Behavioral Statistics, 29*(4), 379–396. [DOI](https://doi.org/10.3102/10769986029004379)

- Research type: psychometrics method paper, with an actual data example
- Test format: self-adapted testing (Self-Adapted Testing, SAT)
- Core data: correct and incorrect questions, difficulty level selected before each question, actual test items
- Core model: three-parameter Logistic Item Response Theory (3PL IRT) plus latent class selection model
- Main statistical issue: When can you ignore examinee's difficulty selection mechanism and estimate ability only based on item response?
- Example: 72 high school students took the 20-question English Vocabulary SAT

!!! important "The most important inspiration for this topic"
    The level of difficulty chosen by examinee is itself a piece of process data, but does not necessarily equal an unbiased ability report. It may reflect ability, but it may also reflect risk preferences, feedback responses, goals, anxiety, or tentative behavior. If difficulty selection is used to construct prior or participation scores, it is necessary to clarify what role it plays in the measurement model and to examine the risks of incorrect selection and strategic manipulation.

## 1. What exactly is the paper going to solve?

In computerized adaptive testing (CAT), the computer chooses the next question based on responses it has already observed. SAT gives part of the control to the examinee:

1. Exame first selects the difficulty level of the next question;
2. The system selects the statistically most appropriate question from the unused items at this level;
3. Examine your answers and receive correctness feedback;
4. Select the difficulty level of the next question.

This results in two interrelated sequences:

\[
\text{difficulty selection sequence}
\quad\text{and}\quad
\text{item response sequence}.
\]

Traditional IRT scoring typically uses only the second sequence. Revuelta asked:

> After examinee actively participates in topic selection, is it still valid to estimate ability based only on actual answers? Does the difficulty selection strategy also have to go into ability likelihood?

The paper accomplishes three things to do this:

1. Use missing data theory to prove that under its sequential selection hypothesis, the potential response of an untested item is MAR;
2. Distinguish between the two different propositions "untested responses can be ignored" and "topic selection strategy parameters can be ignored";
3. Use the latent class model to estimate different difficulty selection strategies and allow strategies to be related to abilities.

## 2. First distinguish the three types of variables

For a SAT with a length of \(N\), the observation at step \(k\) is:

\[
S_k=(I_k,D_k,U_{I_k}),
\]

Among them:

- \(I_k\): The item number actually tested in step \(k\);
- \(D_k\): The difficulty level selected by examinee;
- \(U_{I_k}\in\{0,1\}\): Correct or incorrect responses to this question.

Therefore, the complete sequence of observations is:

\[
S=(S_1,\ldots,S_N).
\]

If the item bank has a total of \(B\) questions, the potential responses of all items can be written as:

\[
\mathbf U=(\mathbf U_{\mathrm{obs}},\mathbf U_{\mathrm{mis}}),
\]

Among them, \(\mathbf U_{\mathrm{obs}}\) is the reaction of the actual tested item, and \(\mathbf U_{\mathrm{mis}}\) is the potential reaction that was not tested and therefore cannot be seen.

There are three components required to generate a single SAT data.

### 2.1 Answer model

\[
f_i(u;\theta)
=
P(U_i=u\mid\theta).
\]

It represents the probability of observing the reaction \(u\) on item \(i\) when the capability is \(\theta\). This article assumes that the item has been calibrated using the three-parameter Logistic Item Response Theory (3PL IRT) model.

### 2.2 Difficulty selection model

\[
g(D_k\mid S_{1:k-1}).
\]

It indicates how examinee chooses the difficulty level \(D_k\) of question \(k\) based on the answer and selection history observed in the previous \(k-1\) step.

### 2.3 Specific topic selection mechanism within the level

\[
h(I_k\mid D_k,S_{1:k-1}).
\]

It indicates that after the difficulty level \(D_k\) has been determined, how does the system select the specific item \(I_k\) from this level based on previous history.

These three parts cannot be mixed into one concept. In particular: **which questions were actually tested**, **why the examinee chose this level of difficulty**, and **how well they answered these questions**, are three different pieces of information.

## 3. What exactly does MAR prove?

### 3.1 Sequential selection only relies on observed history

In step \(k\), the specific item and difficulty are generated based on the previously observed sequence \(S_{1:k-1}\), rather than based on the unknown reaction of the item that has not yet been tested. Therefore, given the observed history:

\[
P(\mathbf I\mid
\mathbf D,\mathbf U_{\mathrm{obs}},\mathbf U_{\mathrm{mis}})
=
P(\mathbf I\mid
\mathbf D,\mathbf U_{\mathrm{obs}}).
\]

In other words, the distribution of the specific item indicator \(\mathbf I\) no longer depends on \(\mathbf U_{\mathrm{mis}}\). According to Rubin's (1976) definition, responses to unpresented items are MAR under this model.

### 3.2 MAR does not mean that all selection information can be discarded

To ignore the missing mechanism in maximum likelihood inference, a second condition must be met: the parameters of the missing mechanism and the ability parameter \(\theta\) are distinct from each other, that is, the joint parameter space can be separated.

Revuelta thus distinguishes between two cases:

- If \(g(D_k\mid S_{1:k-1})\) does not contain \(\theta\), strategy and ability are independent in the model, and the difficulty selection mechanism does not need to enter ability scoring;
- If the strategy category probability or difficulty selection probability depends on \(\theta\), the strategy parameters are no longer distinct from \(\theta\), and the ability must be jointly estimated with the strategy.

!!! warning "MAR, ignorability and valid scoring are not synonyms"
    The MAR conclusion of this article is a conditional conclusion based on the specified sequential model. It does not mean that Examinee's selection is equivalent to a random selection of questions, nor does it mean that any self-selected test is automatically fair, unbiased, or comparable. If the selection also relies on unmodeled future information, item content, leaked question information, or other latent variables, the author's factor decomposition may not still hold true.

## 4. How does the author compress complex topic selection behaviors?

If you directly estimate "how to jump between seven difficulty levels", there will be many parameters. The author makes three simplifications.

### 4.1 First-order dependencies

The \(k\)th difficulty selection only depends on:

\[
(D_{k-1},U_{I_{k-1}}),
\]

That is, the difficulty and correctness of the previous question without using the earlier complete history.

### 4.2 The strategy within the test remains unchanged

The same examinee uses the same selection strategy throughout the test. This assumption was later significantly challenged by actual data.

### 4.3 Only modeling the direction of difficulty change

The author does not directly predict which level of the seven levels the next question will be, but compresses the choices into three changes:

\[
X_k=
\begin{cases}
1,&D_k<D_{k-1}\quad\text{easier},\\
2,&D_k=D_{k-1}\quad\text{unchanged},\\
3,&D_k>D_{k-1}\quad\text{more difficult}.
\end{cases}
\]

Let the response to the previous question be \(Y_{k-1}=U_{I_{k-1}}\in\{0,1\}\), and define the strategy category \(c\):

\[
\pi_{x\mid y,c}
=
P(X_k=x\mid Y_{k-1}=y,\tau=c).
\]

For each previous question response \(y\), the sum of the three transition probabilities is 1, so there are only two free parameters. The sum of the two reaction states:

\[
2\times(3-1)=4
\]

free parameters instead of 84 parameters when directly modeling seven levels.

!!! note "The price of compression"
    "Going from level 1 to 2" and "going from level 1 to 7" are both just "harder" in this model; it is impossible to get any easier or harder at the boundaries, and they need to be truncated and renormalized. The model therefore identifies coarse-grained reaction rules rather than the complete difficulty selection utility function.

## 5. Why do we need latent class?

The author assumes that there are \(C\) strategies in the population that are not directly observed:

\[
\tau_t\in\{1,\ldots,C\}.
\]

People in the same category share a set of \(\pi_{x\mid y,c}\). The observation likelihood of individual \(t\) can be summarized as:

\[
L_t
=
\left[
\prod_{k=1}^{N}
f_{I_{tk}}(u_{tk};\theta_t)
\right]
\left[
\prod_{k=1}^{N}
h(I_{tk}\mid D_{tk},S_{t,1:k-1})
\right]
\left[
\sum_{c=1}^{C}
P(\tau_t=c\mid\theta_t)
\prod_{k=2}^{N}
g_c(D_{tk}\mid D_{t,k-1},u_{t,k-1})
\right].
\]

Intuitively, the first item explains whether the answer is correct or wrong, the second item explains which question the system issued within the same difficulty level, and the third item explains the difficulty jump sequence of Examinee.

## 6. Case 1 and Case 2: the most critical comparison in the full text

### Case 2: Strategies and capabilities are independent

If:

\[
P(\tau=c\mid\theta)=P(\tau=c),
\]

Then the response model and the strategy model can be estimated separately:

\[
\widehat\theta_t
=
\arg\max_{\theta_t}
\prod_{k=1}^{N}
f_{I_{tk}}(u_{tk};\theta_t).
\]

At this point, selecting a difficulty level is not considered additional evidence of ability. Different strategies will still change the actual items and accuracy, but the final point estimate is only determined by the accuracy of these items and item parameters.

### Case 1: Strategy category probability dependence ability

The authors use multinomial logistic regression:

\[
P(\tau=c\mid\theta)
=
\frac{
\exp(\lambda_{c0}+\lambda_{c1}\theta)
}{
\sum_{q=1}^{C}
\exp(\lambda_{q0}+\lambda_{q1}\theta)
}.
\]

One category is set as the reference category, with its intercept and slope fixed at 0.

At this point, what difficulty path one chooses changes which \(\theta\) is more likely because:

\[
\text{Difficulty selection}
\longrightarrow
P(\tau=c\mid\theta)
\longrightarrow
L(\theta).
\]

Therefore, the ability update is no longer just the IRT response score, but also includes the derivative of the policy mixture with respect to \(\theta\).

!!! danger "This is not free extra information"
    If the empirical correlation between strategies and abilities is written directly into the score, the examinee may affect the score through selection. The author clearly points out: Case 1 is valuable when studying behavioral mechanisms, but it is not ideal in measurement practice because strategies may be used to artificially improve the ability estimate.

## 7. What does the EM algorithm estimate?

The potential policy \(\tau_t\) is not visible, so the author uses the Expectation-Maximization (EM) algorithm.

### 7.1 E-step: Assign soft class probability to each person

For the current parameters, calculate:

\[
w_{tc}
=
P(\tau_t=c\mid
\mathbf D_t,\mathbf U_{t,\mathrm{obs}},\theta_t).
\]

Given \(\theta_t\), the answer IRT items are the same for each category, so the category posterior is mainly given by:

- Current class probability \(P(\tau_t=c\mid\theta_t)\);
- The probability of this category generating this difficulty transition sequence;

Decide together.

Then accumulate the posterior number and transfer frequency of each category:

\[
n_c=\sum_t w_{tc},
\qquad
n_{xy\mid c}=\sum_t n_{xyt}w_{tc}.
\]

### 7.2 M-step: Update strategy parameters and capabilities

The transition probability is updated to:

\[
\widehat\pi_{x\mid y,c}
=
\frac{n_{xy\mid c}}
{\sum_{x'}n_{x'y\mid c}}.
\]

Case 1 also needs to update multiple Logistic parameters \(\lambda\) and everyone’s \(\theta_t\). The capability equation also includes:

1. IRT response likelihood score function;
2. The score function generated by the change of strategy category probability with \(\theta_t\).

Case 2 fixes all policy slopes to 0, so \(\theta_t\) degenerates into ordinary IRT maximum likelihood estimation, and policy parameters and capabilities are updated separately.

## 8. Why does the ordinary IRT information function underestimate the standard error?

Common asymptotic standard errors are:

\[
SE_{\mathrm{asymp}}(\widehat\theta)
=
I(\widehat\theta)^{-1/2}.
\]

But it treats the actual item number \(\mathbf I\) as fixed. When adaptive or self-adapted testing is repeated, early response and difficulty selection may produce another item path, so the true repeated sampling variation also includes:

\[
\text{Answer randomness}
+
\text{Randomness of topic selection path}
+
\text{Uncertainty in strategy classification and parameter estimation}.
\]

The author therefore uses parameter Bootstrap:

1. First fit the ability and strategy parameters, and classify each person into the category with the largest posterior probability;
2. Simulate new answers and difficulty sequences according to the person’s abilities, categories and boundary rules;
3. Re-estimate all capability and strategy parameters in each simulation sample;
4. Use the standard deviation of repeated estimates to approximate the true standard error.

Instead of just fixing the item parameters and then recalculating the IRT information, the entire SAT generation and estimation process is repeated.

## 9. Actual data and test design

### 9.1 Samples and Level of Interest

- Sample: 72 high school students;
- Quiz: English vocabulary;
- Grade purpose: accounting for 20% of the final grade of the course;
- fixed length: 20 questions;
- Before the official test: seven training questions, one question for each difficulty level;
- After each formal answer: the system will inform you whether it is correct or incorrect, and then let the students choose the difficulty of the next question.

This is not a low-risk health self-assessment scenario. Both grade proportions and immediate feedback may change risk preferences and difficulty selection strategies.

### 9.2 item bank

The item bank contains 221 five-choice questions, calibrated using the 3PL model, and divided into seven layers according to the difficulty parameter \(b\):

|Difficulty range|Number of questions|
|---|---:|
| \(b<-2.5\) | 13 |
| \(-2.5\le b<-1.5\) | 30 |
| \(-1.5\le b<-0.5\) | 38 |
| \(-0.5\le b<0.5\) | 59 |
| \(0.5\le b<1.5\) | 47 |
| \(1.5\le b<2.5\) | 29 |
| \(b\ge2.5\) | 5 |

The first question is fixed from level 4 of medium difficulty, because most people in the actual sample initially choose this level. The author fitted Case 1 and Case 2 models of \(C=1,\ldots,5\) categories respectively; in addition, the first 10 questions and the last 10 questions of the test were separately fitted to four categories of models.

## 10. Model comparison result: Don’t just copy the author’s sentence

The author uses the Akaike Information Criterion (AIC):

\[
AIC=-2\log L+2p.
\]

A smaller AIC indicates a better relative trade-off between fit and model complexity. The key result of the original table is:

|model| Case 1 AIC | Case 2 AIC |
|---|---:|---:|
|Category 1| - | 5550 |
|Category 2| 5468 | 5471 |
|Category 3| 5451 | **5467** |
|Category 4| 5451 | 5468 |
|Category 5| 5459 | 5471 |
|4 categories, front and rear half-field fitting respectively| - | **5228** |

Three points can be gained:

1. A type of model is obviously poor, and the data really requires more than one selection mode;
2. Under the same number of categories, the AIC of Case 1 is usually lower than that of Case 2, indicating that allowing capabilities to be related to strategies improves the relative fit;
3. Separate fitting of the front and rear halves reduces the AIC from about 5468 to 5228, which strongly opposes the assumption that the "strategy remains unchanged throughout the field".

!!! warning "There is a direct contradiction between the text and Table 1"
    The text says that the four-category model is selected because it minimizes the AIC under Case 2; but in the original table, the AIC of the three-category model is 5467 and the four-category model is 5468. According to the surface value, the third category is 1 lower. This difference is small, but it means that "strictly selecting four categories based on the lowest AIC" does not hold. The four categories can be used as approximate schemes for ease of explanation, but the main text statements cannot be regarded as undisputed numerical facts.

Furthermore, the class number test for finite mixture models does not meet the standard conditions of conventional likelihood ratio tests. The authors therefore use AIC descriptively and do not provide class number uncertainty, cross-validation, or independent sample replication.

## 11. What are the four strategies specifically?

The following explanations are primarily based on the Case 2 four-category model used by the authors for subsequent analyses.

### Strategy 1: Partly rigid, partly flexible

- After answering the previous question incorrectly: 31% chose easier, 68% chose maintain, 1% chose harder;
- After answering the previous question correctly: 1% choose easier, 72% choose maintain, 27% choose harder;
- Estimated class proportion: 68.8%, maximum number of posterior classifiers 49.

Most of the time, the original difficulty is maintained, but the direction of change is usually in line with "if it's wrong, it will decrease, if it's right, it will increase."

### Strategy 2: Be flexible

- After wrong answers: 52% easier, 31% maintain, 17% harder;
- After correct answer: 9% easier, 46% maintain, 45% harder;
- Estimated category proportion: 20.8%, number of categories 15.

This is the closest to an intuitive strategy of adjusting difficulty up and down based on immediate feedback, but it won't be followed strictly every time.

### Strategy 3: Rigidity

- Approximately 95% of the answers will remain at the original difficulty level;
- Approximately 99% of correct answers will remain the original difficulty level;
- Estimated category proportion: 6.3%, number of categories: 5.

### Strategy 4: Tolerate Failure

- After wrong answers, about 50% will be maintained and 44% will be reduced;
- After answering correctly, it is estimated to be 100%, increasing the difficulty;
- Estimated category proportion: 4.1%, number of categories: 3.

The samples of the last two categories are very small, and some transition probability estimates fall on the boundary of 0 or 1, and the Bootstrap standard error is also large. They are more suitable to be regarded as exploratory behavioral prototypes and cannot be regarded as stable population types.

## 12. The same person does not stick to the same strategy throughout the game

Among the first 10 questions, the difficulty changes more frequently; among the last 10 questions, the original difficulty is more common. The author's explanation is:

\[
\text{Explore the appropriate difficulty level in the first half}
\longrightarrow
\text{Stay in the preferred zone in the second half}.
\]

The significant decrease in AIC for the split-half model is also consistent with this explanation.

However, there is still a layout or numerical problem in the original table that cannot be ignored: the proportions of the four categories listed in the second half are:

\[
0.581, 0.280, 0.130, 0.081,
\]

The sum is:

\[
1.072,
\]

cannot be a valid probability vector. There is no errata in the original text, and this page does not change any of the numbers to 0.208 or other values ​​without authorization. It is safe to cite "the split-half model fit is significantly improved" and this set of second-half category ratios should not be directly reused.

## 13. What does it mean when strategies are related to capabilities?

Case 1 has polynomial logistic slopes far away from 0, with two estimates reaching the parameter bounds \(-12\) or \(12\) set by the authors. The fitting curve mainly divides people with low abilities into strategy 2, and people with medium and high abilities mainly fall into strategy 1.

The author therefore believes that there is a strong correlation between strategy and ability. However, there are two levels that need to be seen:

1. **Essential explanation**: People with different abilities may indeed adopt different difficulty adjustment methods;
2. **Statistical warning**: Boundary estimates with class probabilities approaching step functions may also indicate small sample separation, local extremes, or model overdetermination.

The ability estimates of Case 1 and Case 2 are approximately the same for most people, but there is a significant difference near \(\theta\approx-0.25\). The steep class boundaries of Case 1 make it almost impossible for someone with Strategy 2 to estimate above that threshold, and almost impossible for someone with Strategy 1 to estimate below it.

This shows that once the selection strategy is written into the ability model, it not only fine-tunes the scores, but also may rearrange the ability estimates near artificially formed category boundaries.

## 14. bias and standard errorresult

The author conducted an approximate variance analysis (analysis of variance, ANOVA) under Case 2 according to the maximum posterior category, and compared the ability bias, asymptotic standard error and standard error ratio of the four categories.

|Category|average bias|Asymptotic standard error mean|Asymptotic SE / Bootstrap SE|Category number of people|
|---|---:|---:|---:|---:|
| 1 | -0.04 | 0.14 | 0.41 | 49 |
| 2 | -0.05 | 0.14 | 0.38 | 15 |
| 3 | -0.04 | 0.14 | 0.41 | 5 |
| 4 | -0.06 | 0.14 | 0.41 | 3 |

None of the category differences are significant:

- Asymptotic standard error: \(F(3,68)=0.02,\ p=.99\);
- bias: \(F(3,68)=0.34,\ p=.79\);
- standard error ratio: \(F(3,68)=0.27,\ p=.85\).

All this supports is: **With this sample and Case 2 scoring, no differences in accuracy or bias were detected between the policy categories. **It does not prove that the four categories are completely equivalent, because the categories are estimated with errors, and the latter two categories only have 5 and 3 people, so the testing power is very low.

The more striking result is that the ratio is only about 0.38 to 0.41:

\[
\frac{SE_{\mathrm{asymp}}}{SE_{\mathrm{bootstrap}}}
\approx0.4.
\]

In other words, the conventional asymptotic SE based on fixed item paths is only about 40% of the complete simulated SE, which significantly underestimates the uncertainty of repeated measurements.

!!! note "The title of Table 3 also has residual problems"
    The title of Table 3 reads “Impact of Test Type and Strategy”, but this section does not compare different test types, only strategy categories. The safest place to cite is between the table values ​​and the text ANOVA, rather than copying the title.

## 15. This paper proves nothing

This article **does not** directly test:

- Whether the SAT is a shorter test than the standard CAT;
- Let people choose whether the previous \(k\) question improves the starting point of subsequent CAT;
- Whether difficulty selection can form a well-calibrated individualized prior;
- Can the external validity be improved after selecting data for scoring?
- Whether the same strategy will still appear when correctness feedback is not provided;
-Whether the same category structure exists in low-risk mental health scenarios;
- Whether the strategy category can be stably reproduced in new samples;
- Use selection information to improve item exposure.

Its contribution is to establish a joint analysis framework and use a small sample example to prove that selection strategies are heterogeneous, may change with test stages, and may also be strongly related to ability.

## 16. Implications for the method of “entering self-assessment information into CAT”

### 16.1 The use of selection for routing and the use of selection for scoring must be separated

The safest primary analysis can be:

\[
s_i
\longrightarrow
p_0(\theta\mid s_i)
\longrightarrow
\text{Topic selection path},
\]

But ultimately both scores are reported simultaneously:

1. Only use response-only estimates of actual responses;
2. Preserve the Bayesian estimate of the self-evaluation prior.

The difference between the two can show whether the efficiency gain comes from finding the right item faster, or from continuously writing self-evaluation signals into the final score.

### 16.2 Previous \(k\) Question selection should not assume a static strategy

Revuelta's data clearly challenges the "unchanged strategy." If we record the difficulty choices of the first \(k\) questions, we should at least compare:

- static latent class;
- Transition model that changes according to question order or before and after stages;
- hidden Markov model (Hidden Markov Model, HMM);
- Dynamic models that allow individuals to switch between exploration and exploitation states.

The follow-up Arieli-Attali et al. (2019) advanced exactly along the HMM direction.

### 16.3 Self-assessment accuracy and selection strategy are two dimensions

A person can know exactly which \(b\) area he is roughly in, but choose easier questions out of conservatism; he can also overestimate himself, but quickly correct himself after a mistake. Therefore should be recorded separately:

\[
\text{initial self-assessment error}
=
s_i-\theta_i,
\]

and:

\[
\text{Transfer strategy after feedback}
=
P(\Delta D_{it}\mid U_{i,t-1},D_{i,t-1}).
\]

Don't directly code "selected high difficulty" as "high ability".

### 16.4 If you choose to enter the ability estimate, you must do a control stress test

At least simulate or experimentally verify:

-Whether deliberately choosing difficult questions can improve your score;
-Whether deliberately choosing easy questions all the time results in too narrow or too wide a posteriori;
- When there is a conflict between self-assessment and answering, how many questions need to be corrected by the algorithm;
- Changes in bias, coverage rate and ranking of response-only and joint-score;
- Whether strategy categories are stable under different conditions of ability, anxiety, motivation and risk.

### 16.5 standard error should cover the entire adaptation process

If the final algorithm causes self-assessment to affect the prior, first question, or first \(k\) question, the repeated sampling verification should be re-run:

\[
\text{Self-assessment generation}
\rightarrow
\text{Topic selection}
\rightarrow
\text{answer}
\rightarrow
\text{stop}
\rightarrow
\text{Scoring}.
\]

Calculating the IRT information function only on realized item paths may underestimate the true uncertainty. Monte Carlo standard error, empirical RMSE and interval coverage rate should be reported simultaneously.

## 17. Chinese paraphrases that can be quoted safely

### About ignorability

> Under the sequential SAT model of Revuelta (2004), the potential response of the untested item satisfies missing at random; but only when the parameters of the difficulty selection strategy and the ability parameter are separable, the selection mechanism can be ignored from the ability likelihood.

### About strategy heterogeneity

> Revuelta (2004) used the latent class model to summarize difficulty selection as "the probability of choosing an easier, same or more difficult item after answering the previous question correctly or incorrectly." Actual samples show that examinee does not share a unified strategy.

### About strategy changes

> Fitting the two halves of the test separately significantly reduces the AIC, suggesting that the examinee may explore the difficulty in the first half and stay in the preferred area in the second half; therefore, it may be too simplistic to regard the entire selection behavior as a fixed category.

### About ability scoring risks

> When policy class probabilities are modeled as a function of ability, the choice sequence directly participates in the ability estimate; this joint model facilitates the study of behavior, but also makes it possible for the examinee to influence the score through the choice of strategies.

### About evidence boundaries

> This study established a measurement model of the SAT selection mechanism. It did not test whether the starting point of self-assessment shortens CAT, nor did it prove that the selection data can form an accurate individualized prior.

## 18. How to divide the work of key references

|Literature|Role in Revuelta (2004)|
|---|---|
| Rubin（1976）；Little and Rubin（1987） |MAR and ignorability conditions|
| Mislevy and Wu（1996）；Mislevy and Chang（2000） |Adaptive topic selection, missing responses and ability inference|
| Bradlow and Thomas（1998） |This shows that in tests that allow direct selection of questions, the missing mechanism may not be ignored.|
| Rocklin and O'Donnell（1987）；Rocklin（1994） |Research on the introduction, motivation and early behavior of SAT|
| Hontangas et al.（2000） |Preliminary Evidence of Difficulty Selection Behavior on the SAT|
| Dempster et al.（1977） |EM algorithm|
| Langeheine and Rost（1988） |latent class model background|
| Efron and Tibshirani（1993） |Bootstrap standard error|
| Rosseel（2002） |AIC evaluation of mixed models|

## 19. Summary

What Revuelta (2004) adds to this topic is not another “individualized prior efficiency experiment”, but a measurement theory of the selection process:

\[
\boxed{
\text{Untested reactions can be ignored}
\not\Rightarrow
\text{Difficulty selection strategy can be ignored}
}
\]

If choice strategies are independent of ability, ability can continue to be scored only by actual answers; if the two are correlated and jointly modeled, the choice itself will change the ability estimate. Actual data also shows that examinee may explore first and then stabilize, and the static category is only an approximation.

For our design, this meant that “self-assessment used for routing”, “self-assessment retained in prior” and “item-by-item choice as evidence of ability” should be split into different experimental conditions. The real contribution of the method is not to simply claim that the examinee knows itself, but to explain: what signals enter the topic selection, what signals enter the scoring, how the algorithm forgets the wrong signals, and whether the uncertainty of the entire adaptive process is correctly estimated.
