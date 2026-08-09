# Petersen et al. (2026): How much CAT accuracy can be improved by personalizing only the first question

!!! abstract "Key takeaway"
    **What they did:** Petersen et al. used another quality of life domain score that the patient had completed to predict the location of the target domain, and only selected the first question based on this; after the first question, they restored the original EORTC CAT scoring and question selection. **What was gained:** The improvement in the personalized first question mainly appeared in the very short test of questions 1 to 3 and in patients far away from the overall mean. After reaching questions 4 to 5, the difference was basically corrected by the subsequent adaptive process. **Conclusion on this topic:** Changing only the first question is a clean comparison to isolate the routing effect, but it is difficult to produce lasting benefits; if the goal is to stop significantly early, it may be necessary to allow reliable information to continue to enter the estimation or dynamic topic selection.

## Citation details

> Petersen, M. A., Vachon, H., Giesinger, J. M., & Groenvold, M., on behalf of the European Organisation for Research and Treatment of Cancer Quality of Life Group. (2026). Evaluating the use of prior information to individualise start item selection for the EORTC CAT Core. *Quality of Life Research, 35*, Article 7. [DOI](https://doi.org/10.1007/s11136-025-04101-y)

- Study type: Cross-domain prediction on real patient data + Monte Carlo CAT simulation
- Application tools: European Organization for Research and Treatment of Cancer computerized adaptive testing core scale (European Organization for Research and Treatment of Cancer Computerized Adaptive Testing Core, EORTC CAT Core)
- Supporting information: Another health-related quality of life domain score that the same patient has completed
- Actual changes: only change the first question in the target area
- No changes: standard CAT question selection process after question 1, and CAT scoring model
-Main gain position: Very short CAT of questions 1 to 3, especially for patients far from the population mean

!!! note "Why is it the closest research to the mentor program before this major?"
    This paper does not continuously put auxiliary information into the ability estimate as a Bayesian prior, but only uses one prediction point to select the first question. After the first question is answered, the test returns to the original CAT. Therefore, it directly answers the question "Is it enough to personalize only the first question?" and also provides the cleanest comparison for us to distinguish the "first question routing effect" and the "estimated effect of continuously changing the prior".

## 1. The cold start problem to be solved in the paper

Standard CAT at step \(t\) usually selects the most informative question based on current estimates:

\[
i_t
=
\arg\max_{i\in\mathcal R_t}
I_i(\widehat\theta_{t-1}).
\]

But there is no target field to answer before the first question, \(\widehat\theta_0\) does not exist. EORTC CAT Core's current practice is to use the domain average of the development sample, \(M_d\), as a common starting point:

\[
i_1^{\mathrm{fixed}}
=
\arg\max_{i\in\mathcal B_d}
I_i(M_d).
\]

This question is suitable for patients who are near the overall mean, but may not be suitable for patients with very high or very low scores. With a very short CAT of only 1 to 3 questions, the test is over before you even have time to correct the starting point.

Petersen et al. proposed that, in multidomain quality-of-life measurement, patients have usually completed at least one other domain. The score \(T_{pk}\) from a completed domain \(k\) can be used to predict the target domain \(d\):

\[
\widehat T_{pd\mid k}
=
\alpha_{dk}
+
\beta_{dk}T_{pk}.
\]

Then only use this predicted value for the first question:

\[
i_{p1}^{\mathrm{individualised}}
=
\arg\max_{i\in\mathcal B_d}
I_i(\widehat T_{pd\mid k}).
\]

After answering the first question, subsequent questions are still driven by responses that have been observed in the target domain.

This is not:

\[
\theta_p\mid T_{pk}
\sim
N(\mu_p,\tau_p^2)
\]

Sense of individualized Bayesian prior. It is a **point prediction \(\rightarrow\) start-item routing** design.

## 2. What is EORTC CAT Core?

The EORTC CAT Core measures the same core health-related quality of life (HRQoL) domains as the EORTC QLQ-C30, including:

- 5 functional areas;
- 9 symptom domains;
- 1 general health/quality of life domain measured by two fixed questions.

There is one CAT item bank for each of the first 14 areas, with a total of 260 questions. A single item bank contains 7 to 34 questions:

|field|Number of questions|field|Number of questions|
|---|---:|---|---:|
|body functions| 31 |fatigue| 34 |
|role function| 10 |nausea and vomiting| 19 |
|emotional function| 24 |pain| 16 |
|Cognitive function| 34 |difficulty breathing| 32 |
|social function| 13 |insomnia| 8 |
|decreased appetite| 7 |constipation| 10 |
|Diarrhea| 13 |financial difficulties| 9 |

General health/quality of life has only two fixed questions and does not use the CAT, but can be used as an auxiliary variable to predict other areas.

All fields converted to T-score:

\[
M=50,
\qquad
SD=10
\]

scale. Need to pay attention to the direction of the score:

- The higher the score in the functional area, the better the function;
- The higher the symptom domain score, the more severe the symptom.

Therefore, the sign of correlation between different fields will be affected by the scoring direction. The paper is mainly concerned with prediction accuracy rather than directly interpreting the correlation sign as a positive or negative health relationship.

## 3. Part 1: Can real patient data predict another domain?

### 3.1 Sample

The authors combined the EORTC CAT Core development and validation data and obtained:

\[
N=10{,}084
\]

Cancer patient assessment. Samples were drawn from 12 countries and included a variety of cancer sites, disease stages, and treatment statuses.

Randomly divided into:

\[
N_{\mathrm{train}}=8{,}068
\quad(80\%),
\]

\[
N_{\mathrm{test}}=2{,}016
\quad(20\%).
\]

The training set is used to estimate regression models, and the test set is used to evaluate predictions to avoid fitting and reporting performance on the same batch of data.

### 3.2 Only use one prediction field at a time

For each target domain \(d\) where CAT can be implemented, the authors build a simple linear regression using each of the remaining 14 domains:

\[
T_{pd}
=
\alpha_{dk}
+
\beta_{dk}T_{pk}
+
\varepsilon_{pdk}.
\]

So there are 14 single-predictor models for each target domain, rather than putting all completed domains together into multiple regression.

The practical rationale for this design is that as soon as the patient completes one area, the system can already predict the starting point for the next area. The cost is not taking advantage of joint information from multiple established domains.

### 3.3 Evaluation indicators

On the test set, the authors compare the predicted score \(\widehat T_{pd\mid k}\) with the observed domain score \(T_{pd}\), reporting:

1. Average difference;
2. Pearson correlation;
3. The proportion of absolute errors less than 5 points;
4. Proportion where the absolute error is less than 10 points.

Since the standard deviation of the T-score is 10:

\[
5\text{points}=0.5SD,
\qquad
10\text{points}=1SD.
\]

## 4. How to accurately read cross-domain prediction results

### 4.1 The average unbiased does not mean that the personal prediction is accurate

The average absolute prediction error for all domains does not exceed 0.5 points. The authors therefore claim that the predictions are generally unbiased.

But an average error close to 0 only means that the positive and negative errors can cancel each other out. For example, if half of the patients overestimated by 10 points and the other half underestimated by 10 points, the average error would still be 0. Therefore one must also look at the correlation and individual absolute errors.

The range of raw correlation absolute values among the 15 domains is:

\[
0.03\text{to}0.71,
\qquad
\operatorname{median}=0.37.
\]

Fatigue, role functioning, physical functioning, and overall quality of life generally had strong relationships with multiple domains; specific symptoms such as diarrhea and constipation had weaker cross-domain relationships.

### 4.2 72%-89% in the abstract refers to the “best predictor for each target domain”

Summary report:

- The prediction-observation correlation is \(0.31\) to \(0.72\), with an average of \(0.55\);
- Predictions \(72\%\) to \(89\%\) are within 1 standard deviation of the observations, with an average of \(83\%\).

Combined with Table 4, we can see that these numbers are obtained by first selecting the best-performing prediction field for each target field, and then summing it up across the target fields:

|Summary caliber|Related cross-domain averages|Cross-domain average with error less than 10 points|
|---|---:|---:|
|Best predictor for each target area| 0.55 | 83% |
|Averaged across 14 predictors per target domain| 0.39 | 76% |
|Worst predictor for each target domain| 0.21 | 69% |

So the summary cannot be written as "any other field can be predicted to within 1SD with 83% probability". A more accurate statement is:

> If there is a predictor in the completed domain that has a strong relationship with the target domain, the cross-domain starting point usually has usable accuracy; if only a domain with a weak relationship can be used, the performance will drop significantly.

### 4.3 Which areas are easy or difficult to predict?

Best forecasters by each target area:

- The highest prediction related: fatigue and character function, both about \(0.72\);
- Lowest "best correlation": diarrhea, about \(0.31\);
- Best ratio with error less than 10 points: approximately \(72\%\) to \(89\%\).

Decreased appetite was the only area where no prediction area reached the target of “at least 80% within 10 points.” There may also be low correlations between more specific gastrointestinal symptoms, indicating that apparent similarity in content does not guarantee a statistically good starting point.

## 5. Part 2: CAT simulation changing only the first question

### 5.1 Simulation Capability Grid

For each HRQoL domain, the authors centered the development sample mean \(M_d\) on:

\[
M_d-30
\quad\text{to}\quad
M_d+30
\]

Set a true score point every 0.5 points. Each score point generates 200 sets of responses to all items in the item bank.

Then simulate:

- CAT with fixed length questions 1 to 10;
- If the item bank has less than 10 questions, the entire item bank will be tested at most;
- Also do a fixed-accuracy CAT to achieve the reliability target or administer a maximum of 10 questions.

### 5.2 Four conditions for the first question

#### Fixed: Standard common first question

\[
i_1
=
\arg\max_i I_i(M_d).
\]

Everyone starts by developing the same question that is most informative at the sample mean.

#### True: Completely accurate individualized first question

\[
i_1
=
\arg\max_i I_i(T_{pd}^{\mathrm{true}}).
\]

This is a theoretical upper limit and cannot be obtained directly before actual testing.

#### Diff 0.5SD: The prediction error is plus or minus 5 points

Half of the simulation is at:

\[
T_{pd}^{\mathrm{true}}-5
\]

Choose the first question, and the other half is:

\[
T_{pd}^{\mathrm{true}}+5
\]

Choose the first topic.

#### Diff 1SD: Prediction error is plus or minus 10 points

In the same way, choose the first question 10 points above or below the true score.

### 5.3 A very important design boundary

The CAT simulation does not directly feed the regression prediction values actually obtained for each patient in the test set to the question selection algorithm, nor does it extract errors from the empirical prediction error distribution. The author uses controlled:

\[
0,\quad \pm5,\quad \pm10
\]

Third gear bias.

Therefore, the entire study consists of two adjacent but not yet fully connected modules:

\[
\text{Real patient data: How accurate can cross-domain predictions be?}
\]

and:

\[
\text{CAT simulation: If the starting point error is fixed to}0,\pm5,\pm10，
\text{What impact does the first question have?}.
\]

It is not an end-to-end simulation:

\[
\text{true regression model}
\rightarrow
\text{person by person prediction}
\rightarrow
\text{First question per person}
\rightarrow
\text{CAT result}.
\]

This does not negate the value of the research, but it limits our estimates of actual average returns.

## 6. How to measure the effect of changing only the first question

The author divides the true score into three intervals:

- Low score: 1 to 3 standard deviations below the field mean;
- Middle: 1 standard deviation above and below the mean;
- High score: 1 to 3 standard deviations above the mean.

For each length and first question condition, compare:

### Average estimated bias

\[
\overline{\widehat T-T^{\mathrm{true}}}.
\]

### Proportion of errors less than 5 points

\[
P\left(
\left|\widehat T-T^{\mathrm{true}}\right|<5
\right).
\]

### Average reliability

Thesis uses:

\[
\operatorname{Rel}
=
1-\frac{SE^2}{SD^2},
\]

Among them:

\[
SE^2
=
\frac{1}{I(\theta)}.
\]

The paper also simulates reliability exceeding \(0.90\) or a variable length CAT of up to 10 questions, saying that this approximately corresponds to \(SE\leq0.33\) on the standard normal scale.

Strictly follow the above formula and convert \(SD=1\):

\[
SE
\leq
\sqrt{1-0.90}
\approx
0.316.
\]

Therefore, \(0.33\) is a looser approximation. When quoting, it is best to write "reliability exceeds 0.90" instead of treating \(0.33\) as an exact equivalent.

## 7. The main result of fixed length simulation

### 7.1 After four questions, the impact of the first question is usually very small

Except for low pain scores, when the CAT reaches more than 4 questions, the differences between the different first-question conditions are usually small. Under low pain conditions, the reliability of the fixed first question is lower than that of the individualized first question \(0.2\) to \(0.4\) at questions 1 to 4; it basically disappears after reaching 5 questions.

Therefore, the paper will mainly focus on questions 1 to 3.

### 7.2 Table 5 does not compare the “real regression starting point”

Table 5 reports the difference between the Diff 0.5SD condition and the Fixed condition, averaged across questions 1 to 3. In other words, the individualized first question in the table assumes that the prediction error is exactly plus or minus 5 points, rather than using the person-by-person error of the first part of the empirical regression.

The directions of positive and negative values are explained separately:

- mean deviation is less than 0: the individualized first question is closer to the true score;
- "Proportion of error less than 5 points" is greater than 0: individualized first question is better;
- Reliability is greater than 0: the individualized first question is more reliable.

### 7.3 Average result of three score intervals

|Score range|average bias difference|Proportional differences with an error of less than 5 points|reliability differences|
|---|---:|---:|---:|
|low score| \(-0.4\) |\(+4.1\) percentage points| \(+0.11\) |
|middle| \(+0.1\) |\(-2.1\) percentage points| \(-0.01\) |
|high score| \(+0.1\) |\(+0.8\) percentage points| \(+0.05\) |

This is consistent with design intuition:

- The common first question is inherently most informative at the mean, so the middle group has no benefit;
- The main value of individualized first questions is to send the first questions of extreme patients to a more appropriate position;
- The average revenue of low partitions is significantly greater than that of high partitions, but this depends on the information distribution of each item bank and should not be directly generalized to all CATs.

### 7.4 Some of the biggest benefits

CAT for Questions 1 to 3:

- Low body function: reliability increased by \(0.26\), and the proportion of errors less than 5 points increased by 11.0 percentage points;
- Low Pain: Reliability improved by \(0.33\), average estimation error improved by 2.5 points;
- Low insomnia: reliability increased by \(0.27\), and the proportion of errors less than 5 points increased by 11.9 percentage points;
- High emotion function: reliability increased by \(0.11\), and the proportion of errors less than 5 points increased by 4.2 percentage points.

But not all areas have improved. For example, in the middle interval, the individualized first question reduces the proportion of "error less than 5 points" by 2.1 percentage points on average; if the fixed first question already matches the target position, changing the first question may only bring random or slight negative returns.

## 8. How many “less questions” does variable length simulation support?

The authors simulate a CAT of up to 10 questions with reliability exceeding \(0.90\) in the supplementary material. The main article only gives a summary:

- For patients with low physical function, the number of individualized first questions can be reduced by an average of 1.4 questions at most;
- The difference in the average number of questions for other conditions does not exceed 0.7 questions.

Therefore, this article does provide evidence that "the number of questions may decrease under the same reliability target", but the benefits are not universal and huge:

1. The maximum value comes from the specific field and tail fraction;
2. Most conditions are less than 1 question;
3. Detailed Table S1 is not in the current local PDF text;
4. Fixed length CAT is the main simulation of the paper and the core result in Table 5.

A safe summary is:

> Individualized first questions mainly improve the early accuracy of very short tests; under a few tail conditions, this accuracy advantage can be converted into a fixed-precision question saving of about 1 question.

## 9. Why the order of different fields becomes a design issue

Cross-domain forecasting can only be used for the second and subsequent domains. There is still no secondary score for the first domain in the entire multi-domain test.

The author recommends testing a field that is more general, has strong predictive power for other fields, and has low demand for individualized first questions:

- Fatigue is generally a good predictor of multiple domains, and has limited benefits on its own from the individualized first question;
- If fatigue is the main outcome, you can test the character function first and then use the character function to predict fatigue;
- You can also take the overall health/quality of life test with only two fixed questions first, and then individualize the first question for all CAT areas.

This effectively turns a single CAT cold start problem into a quiz battery sequencing problem:

\[
\text{Which area to test first?}
\longrightarrow
\text{Which follow-up areas can provide a starting point?}
\longrightarrow
\text{Overall Burden and Accuracy}.
\]

If our research includes multiple psychological dimensions, domain order can also be used as a new optimization layer instead of treating each CAT completely independently.

## 10. This paper has not changed prior

The "prior information" in the title of the paper refers to "information available before the test" in a broad sense. The actual algorithm is:

\[
\text{Scores in other areas}
\rightarrow
\widehat T^{(0)}
\rightarrow
\text{Question 1}
\rightarrow
\text{Standard CAT}.
\]

It is not defined:

\[
p_0(\theta\mid x),
\]

It also does not allow prior variance to enter the posterior standard error, final estimate, or stopping rule.

This makes it a clear complement to Frans et al. (2023):

|Research|Auxiliary information affects the first question|Sustainability estimate|Enter stopping accuracy|
|---|---:|---:|---:|
|Petersen et al. (2026)|Yes|No|No|
|Frans et al. (2023)|Yes|Yes|Yes|

For our four-condition ablation:

- Petersen et al. correspond to "only change the first question route";
- Frans et al. correspond to "complete individualized prior + maximum information amount at current estimate";
- We still need to directly compare the two, and a combination of the two.

## 11. Evidence boundaries and limitations

### 11.1 Supporting information is not a direct self-assessment of the target area

There is another HRQoL domain that patients do answer themselves, but instead the system asks “What level do you think you are at with your target symptoms?” It uses the scale score obtained from another set of formal items.

So it supports:

> Patient-generated collateral information You can choose the individualized first question.

But it cannot be directly proved:

> Single explicit self-assessment or self-selection difficulty has the same prediction quality.

### 11.2 The two phases have not yet been combined end-to-end.

Real patient data demonstrate the usable predictive power of certain cross-domain regressions; CAT simulations demonstrate how the first question changes accuracy given starting point errors of \(0\), \(\pm5\), \(\pm10\). The paper does not directly simulate the overall question volume and accuracy corresponding to the real regression error distribution.

### 11.3 “On average unbiased” is not enough to ensure safety

The average error of linear regression on the test set is small, but individual errors may still be large. The paper does not specifically report:

- Prediction error at the worst quantile;
-Which patient groups are more likely to be severely misrouted;
- Whether the error direction is related to the item bank information tail system;
- The consequences of conditional exposure for wrongly answering the first question.

### 11.4 Real patient responses did not enter the CAT run

The regression model uses real patient data, but the CAT portion uses responses generated by the model. The authors explicitly recommend further validation with independent real-world testing.

### 11.5 No report on item exposure and fairness

Individualized first questions will send different score groups to different difficulty areas, which may reduce the exposure of common middle questions, and may also increase the conditional exposure of a few questions at the end. The paper does not report:

\[
P(A_i),\qquad
P(A_i\mid\theta),\qquad
\text{test overlap}.
\]

### 11.6 Clinical significance not yet established

Whether the increased reliability of \(0.05\) or \(0.11\) would improve individual monitoring, clinical decision-making, or patient management was not verified by the paper. Statistical accuracy gains do not automatically equal clinical gains.

### 11.7 The current paper does not fully recap all CAT scoring details

The methods section explains the first question conditions, simulation range, reliability definition and evaluation indicators, and points the remaining details to previous body function research. Therefore, it cannot be concluded from this article alone that it uses a specific ability estimator at each step, such as MAP, EAP, or MLE; this page does not supplement the original text.

## 12. Direct implications for our experimental design

### 12.1 Only changing the first question must be used as an independent baseline

Keep at least:

\[
\text{Standard common first question}
\]

with:

\[
\text{Select the first question for the self-assessment position and then return to the standard CAT}.
\]

If this condition has reaped the full benefits, there is no need for self-assessment to continue into the prior; if it only improves the first 1 to 3 questions but does not shorten the fixed accuracy test, then a more permanent mechanism is needed.

### 12.2 Feed the real self-assessment error into the end-to-end simulation

Don't just set the fixed \(\pm0.5SD\) and \(\pm1SD\). A more realistic solution is to first create:

\[
s_p\longrightarrow
p(\theta_p\mid s_p),
\]

Then simulate each person's from the joint distribution:

\[
(\theta_p,s_p)
\]

And let the actual \(s_p\) determine the first question. This preserves:

- Continuous distribution of errors;
- Variance of different self-assessment levels;
- Extreme levels of accumulation;
- Asymmetry between overestimation and underestimation;
- Correlation structure of error self-evaluation and true ability.

### 12.3 Focus on the first three questions and the final result

The results of Petersen et al. suggest two time scales:

1. Early Questions 1 to 3: The first questions may significantly change reliability;
2. After question 4 to 5: Standard CAT usually has the first question corrected.

So the experiment should simultaneously draw:

\[
t=1,2,3,\ldots
\]

bias, RMSE, posterior variance and correct item area arrival rate, rather than just looking at the final result.

### 12.4 Must be stratified according to capability ranges

Overall averaging can mask true gains. Report at least:

- Center capabilities;
- Low-end capabilities;
- High-end capabilities;
- Self-assessment is accurate or inaccurate;
- The self-evaluation error points to the high information area and low information area of the item bank.

### 12.5 Add exposure indicators

Individualized first questions may achieve the instructor's wish to "make everyone's first questions as different as possible." Suggested special reports:

\[
\max_i P(A_{i,1}),
\]

\[
\operatorname{Entropy}(A_1),
\]

\[
P(A_{i,1}\mid s=c),
\]

and cumulative total and conditional exposure after the first question.

Only in this way can we judge whether personalization really disperses the first questions in the middle, or just concentrates some self-assessment groups into the same tail questions.

### 12.6 Doing complete ablation with sustained prior

It is recommended to form:

|Conditions|First question position|Follow-up estimates|
|---|---|---|
|A standard CAT|common mean|standard prior|
|B Only change the first question|Self-assessed position|Return to standard after the first question prior|
|C only changes the estimate|Current estimate of individualized prior|individualized prior continuous updates|
|D first question routing + prior|Candidate interval or exposure control for self-evaluation position|individualized prior continuous updates|

Petersen et al. mainly support the feasibility of B; Frans et al. explain the benefits and risks of C. Whether D can simultaneously obtain early matching, item bank dispersion and robust estimation still needs to be answered by our ablation.

## 13. Chinese paraphrases that can be quoted safely

### Support "Only changing the first question is useful for very short CAT"

> Petersen et al.'s (2026) EORTC CAT Core simulations showed that using another quality-of-life domain to predict target domain location and select the first question accordingly improved measurement accuracy on very short CATs of questions 1 to 3, with gains concentrated in patients far from the population mean; after reaching questions 4 to 5, first question differences have generally been corrected by subsequent adaptive processes.

### Support "best cross-domain predictions are usually within 1SD"

> When selecting the single best-performing prediction domain for each target domain across 10,084 cancer patient assessments, prediction-observation correlations ranged from 0.31 to 0.72, with an average of 0.55; 72% to 89% of predictions were within 1 standard deviation of the observation score.

The qualification "best prediction area" must be retained here. When averaged across all predicted domains, Table 4 corresponds to a correlation of approximately 0.39, with a 1SD ratio of approximately 76%.

### Supports "The benefits of only changing the first question are limited and heterogeneous"

> In the variable length simulation with a reliability exceeding 0.90, the individualized first question can reduce the average number of questions by at most 1.4 questions for patients with low physical function; the difference in the average number of questions for the other conditions does not exceed 0.7 questions, indicating that the question volume benefit is highly dependent on the field and the true score position.

### Cannot be quoted like this

- It cannot be written as "any other field can accurately predict the target field with a probability of 83%";
- It cannot be written as "CAT on real patients has been verified to reduce an average of 1.4 questions";
- cannot be written as "the paper estimates cross-domain scores as Bayesian prior continuous participation estimates";
- Scores in another formal scale area cannot be directly equated to the examinee's explicit self-evaluation;
- It cannot be claimed that there is absolutely no effect for more than four questions. The original article is that the difference is usually very small, and there is still a significant difference from the low pain condition to the 4th question.

## 14. Key references and their functions

- **van der Linden (1999)**: A statistical framework for empirically initialized latent trait estimation.
- **Matteucci & Veldkamp (2013)**: Let the empirical prior enter the fixed-precision CAT estimate and discuss the efficiency gains.
- **Frans et al. (2023)**: Benefits, bias, and risk of premature discontinuation from continued empirical prior in clinical multilevel scoring CAT.
- **Petersen et al. (2025)**: This study was previously conducted as a pilot in the physical function domain, and the current paper is extended to all 14 CAT domains.
- **Petersen et al. (2018; 2020)**: Development and international validation data sources for the EORTC CAT Core.
- **Liegl et al. (2019)**: European Norms and T-score scaling basis for the EORTC CAT Core.
- **Kim & Feldt (2010)**: Basis for IRT reliability calculations.
- **Muraki (1993)**: The information function basis of the generalized partial credit model.

## 15. Read the conclusion carefully

This paper provides the most direct support for the tutor’s proposal of “only changing the first question”, and also gives the upper limit of its effect:

\[
\text{individual information}
\rightarrow
\text{The first question that is more suitable}
\rightarrow
\text{Improved accuracy on the first 1 to 3 questions}.
\]

But standard CAT will quickly absorb the response evidence after the first question:

\[
\text{The number of questions reaches 4 to 5}
\rightarrow
\text{Most of the differences in the first questions disappear}.
\]

Therefore, changing only the first question is not ineffective, but a lightweight solution in which the benefits are concentrated in the very short test and the tail of ability, the risks are relatively local, and it is easy to implement. If our main goal is to significantly reduce the average question size of a fixed-precision CAT, the first question alone may not be enough; but it should serve as the most important and interpretable ablation baseline.
