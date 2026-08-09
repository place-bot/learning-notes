# Bass et al. (2026): Can longitudinal PROMIS CAT use the previous score as prior

!!! abstract "Key takeaway"
    **What was done:** In a two-time-point PROMIS CAT simulation, Bass et al. set the final score of the first CAT to the prior mean of the second measurement and systematically varied the prior standard deviation. **What you get:** When health status changes are small, a moderately shrinking prior may shorten the test slightly and reduce RMSE; when changes are large, a too narrow prior will lock the estimate around the old score, making the test appear to stop faster but missing the real change. **Conclusions for this topic:** The individualized prior variance is as important as the mean, short tests cannot be considered successful alone, error, variation recovery and error early stopping must be checked simultaneously.

## Citation details

> Bass, M., Morris, S., & Lam, T. (2026). Brief reports: Impact of informed starting value on longitudinal computer adaptive tests in PROMIS assessments. *Advances in Patient-Reported Outcomes, 2*, 100322. [DOI](https://doi.org/10.1016/j.apro.2026.100322)

- Study type: Two-time point test-retest CAT simulation
- Application tools: Patient-Reported Outcomes Measurement Information System (PROMIS) adult and pediatric item bank
- Supporting information: Final \(\widehat\theta_1\) for first CAT
- The second CAT: use \(\widehat\theta_1\) as the prior mean and change the prior standard deviation
- Estimation method: expected a posteriori estimation (Expected A Posteriori, EAP)
- stopping rule: at least 4 questions, \(SE<0.3\), at most 8 questions
- Main conclusion: Moderately weighting old scores may slightly shorten the test and reduce RMSE when health status changes are small; too narrow a prior will lock the second estimate near the old score, resulting in a shorter but less accurate test

!!! danger "The easiest place to read this article wrong"
    The title uses informed starting value, but what the authors change is the full prior distribution of the second CAT. It not only determines the starting position, but also continues into the EAP ability estimate, question-by-question selection, final score, and stopping judgement. Therefore it is not a “just change the first question” study like Petersen et al.’s (2026) study.

## 1. Research question: Why doesn’t the retest start directly from the last score?

Longitudinal CAT already has scores from the last measurement of the same patient. The most natural idea is:

\[
\mu_{2,p}
=
\widehat\theta_{1,p}.
\]

If patient status does not change much, this is more personalized than starting from a population mean of 0 each time.

The problem is that the last score is not equal to the true state this time:

\[
\theta_{2,p}
=
\theta_{1,p}
+
\delta_p,
\]

where \(\delta_p\) is the true change between the two evaluations. In addition, \(\widehat\theta_{1,p}\) itself has measurement errors.

If the system only uses the final standard error of the last measurement as the prior uncertainty, it implicitly assumes:

\[
\delta_p=0.
\]

In situations where there is a real need to monitor response, progression, or recovery, this assumption may not hold true. Overconfidence in old scores shrinks the second estimate toward the old state, reducing the ability to detect changes.

## 2. The vertical prior variance should include two types of uncertainty

The author uses a simple approximation to express the uncertainty of the second state relative to the first estimate:

\[
SD(\theta_2\mid\widehat\theta_1)
=
\sqrt{
SE(\widehat\theta_1)^2
+
SD(\delta)^2
}.
\]

Included here:

1. The scoring error of the last CAT is \(SE(\widehat\theta_1)\);
2. Individual differences in true change between two measurements \(SD(\delta)\).

This formula is valuable to us because it illustrates that the variance of individualized priors cannot be determined solely by "how accurate the self-assessment itself appears to be." If there is a time gap, situation change or construct drift between the auxiliary information and the current target state, the uncertainty of the state change must also be added.

### An intuitive numerical example

The final standard error of PROMIS for the first measurement is about \(0.25\), and if there is a small change between the two times the standard deviation is about \(0.30\):

\[
\sqrt{0.25^2+0.30^2}
\approx
0.39.
\]

The closest simulated candidate value is prior \(SD=0.5\).

If the standard deviation of the change is \(0.80\):

\[
\sqrt{0.25^2+0.80^2}
\approx
0.84.
\]

At this time \(SD=0.75\) or \(1.0\) is more reasonable. The paper results also generally show this pattern: \(0.5\) is often the best when there are small changes, and \(0.75\) or \(1.0\) is safer when there are big changes.

The author also proposed that if we have large-sample longitudinal data of the appropriate population, we can directly estimate the change variance; if not, we can set it based on existing research, retest intervals and expert judgment, and then adjust parameters through simulation.

## 3. Prior standard deviation and prior variance must be distinguished

Bass et al manipulated:

\[
SD_{\mathrm{prior}}
\in
\{1.00,0.75,0.50,0.25\}.
\]

The corresponding variance is:

\[
\operatorname{Var}_{\mathrm{prior}}
\in
\{1.00,0.5625,0.25,0.0625\}.
\]

This is consistent with the prior variance manipulated by Frans et al. (2023):

\[
\{1.00,0.50,0.25\}
\]

Not the same set of strengths.

| Bass：prior SD | Bass：prior variance |Approximately corresponding meaning|
|---:|---:|---|
| 1.00 | 1.0000 |Little trust in old scores|
| 0.75 | 0.5625 |light trust|
| 0.50 | 0.2500 |medium trust|
| 0.25 | 0.0625 |Strong trust|

!!! warning "Directly related to our \(\tau^2\) experiment"
    If we say "prior variance from 0.1 to 1", Bass's \(SD=0.25\) is not variance 0.25, but variance 0.0625; \(SD=0.5\) only corresponds to variance 0.25. Comparisons across papers must be unified to variance or precision, and surface numbers cannot be directly compared.

## 4. Which PROMIS item banks are used for simulation

### Seven adult areas

1. Physical Function；
2. Fatigue；
3. Pain Interference；
4. Sleep Disturbance；
5. Depression；
6. Anxiety；
7. Ability to Participate in Social Roles and Activities。

### Six children’s areas

1. Mobility；
2. Fatigue；
3. Pain Interference；
4. Depressive Symptoms；
5. Anxiety；
6. Peer Relationships。

A practical advantage of the paper is to use the official PROMIS item bank and actual running software, instead of just generating a fictitious item bank according to rough parameters. The item bank for adults and children differs in the number of questions, coverage, and ceiling/floor effects. It can be tested whether the prior income is limited by the characteristics of the item bank.

## 5. How to generate data at two time points

### 5.1 The true state of Time 1

The first measured true capability is located at nine grid points:

\[
\theta_{1,p}
\in
\{-2,-1.5,-1,-0.5,0,0.5,1,1.5,2\}.
\]

Each grid point is simulated 100 times, so each PROMIS field has:

\[
900
\]

Group assessment.

### 5.2 Real changes in Time 2

The authors simulate two scales of change:

#### Small changes

\[
\delta_p\sim N(0,0.3),
\]

#### Big changes

\[
\delta_p\sim N(0,0.8).
\]

The text discusses \(0.3\) and \(0.8\) as the standard deviation/effect size scale of variation, although the second parameter of \(N(0,\cdot)\) is not clearly written as variance or standard deviation in the symbol. This page will be recorded as \(SD(\delta)=0.3\) or \(0.8\) according to the author's textual explanation.

So:

\[
\theta_{2,p}
=
\theta_{1,p}
+
\delta_p.
\]

The paper allows for both improvement and deterioration since the change distribution is centered around 0.

## 6. Prior, estimation and stopping rule of two CATs

### Time 1

\[
\theta_{1,p}
\sim
N(0,1).
\]

### Time 2

The prior mean is set to the final EAP of the first CAT:

\[
\mu_{2,p}
=
\widehat\theta_{1,p}.
\]

Then use:

\[
\theta_{2,p}
\sim
N(
\widehat\theta_{1,p},
\sigma_{\mathrm{prior}}^2
),
\]

Among them:

\[
\sigma_{\mathrm{prior}}
\in
\{1.00,0.75,0.50,0.25\}.
\]

Each domain implements CAT separately, item responses are generated by the corresponding IRT model in that domain, and ability estimate uses EAP. prior will continue to participate in the posterior of the second CAT:

\[
p(\theta_{2,p}\mid\mathbf u_{2,p})
\propto
p(\mathbf u_{2,p}\mid\theta_{2,p})
\phi(
\theta_{2,p};
\widehat\theta_{1,p},
\sigma_{\mathrm{prior}}^2
).
\]

Therefore prior affects:

\[
\text{initial position}
\rightarrow
\text{Question 1}
\rightarrow
\text{Follow-up EAP}
\rightarrow
\text{Follow-up topic selection}
\rightarrow
\text{Final estimate and stop}.
\]

The common stopping rules are:

\[
n\geq4,
\qquad
SE(\widehat\theta)<0.3,
\qquad
n\leq8.
\]

The evaluation indicators are:

- Average number of questions;
- Final estimated root mean squared error (root mean squared error, RMSE):

\[
\operatorname{RMSE}
=
\sqrt{
\frac{1}{N}
\sum_{p=1}^{N}
(\widehat\theta_{2,p}-\theta_{2,p})^2
}.
\]

## 7. Why \(SD=0.25\) will turn CAT into a four-question test

The narrowest prior variance is:

\[
0.25^2
=
0.0625.
\]

Its initial standard deviation \(0.25\) is already smaller than the stopping threshold \(0.3\). If there is no minimum number of questions constraint, the system may think that the accuracy is sufficient before administering the test.

Since the paper is mandatory to test at least four questions, the \(SD=0.25\) condition almost all stops immediately at the fourth question. The author makes it clear that this effectively turns the CAT into a fixed length four-question test.

Therefore, the condition "the number of questions dropped significantly to 4" cannot be interpreted as the item evidence that the measurement was completed efficiently. A more accurate explanation is:

\[
\text{Strong prior has met the accuracy requirements}
\quad+\quad
\text{At least four question constraints}
\quad\Rightarrow\quad
n=4.
\]

The author also explains that \(SD=0.25\) is not the default implementation recommended in reality, but is used to show the lower limit of the number of questions that different item banks may achieve under the current stopping rule.

## 8. What is item bank well-targeted and poorly targeted?

PROMIS item banks generally provide higher information in locations with certain symptoms or functional impairment, and lower information in asymptomatic or ceiling/floor areas.

According to the matching degree between the real \(\theta_{2,p}\) at Time 2 and the complete item bank information function, the author divides the simulation evaluation into:

- well-targeted: complete item bank information at the real location \(TI>22\);
- Poorly targeted: The complete item bank information at the real location does not exceed 22.

Because:

\[
SE
\approx
\frac{1}{\sqrt{TI}},
\]

\[
TI=22
\Rightarrow
SE\approx0.21.
\]

The paper chooses 22, rather than just about 11 required for \(SE=0.3\), in order to identify regions that can more stably reach the stopping condition before exhausting the item bank.

### Proportion of well-targeted items in the adult item bank

|field|Proportion|
|---|---:|
| Physical Function | 83% |
| Fatigue | 82% |
| Ability to Participate Social | 74% |
| Sleep Disturbance | 72% |
| Anxiety | 60% |
| Depression | 60% |
| Pain Interference | 60% |

### Proportion of well-targeted items in children’s item bank

|field|Proportion|
|---|---:|
| Peer Relationships | 61% |
| Anxiety | 49% |
| Depressive Symptoms | 49% |
| Fatigue | 49% |
| Pain Interference | 39% |
| Mobility | 18% |

!!! note "This layer cannot be used directly for real testing decisions"
    Well-targeted/poorly targeted are divided post hoc based on the real \(\theta_2\) in the simulation. The real location is not known before the actual CAT starts, so it is an analysis tool to explain the heterogeneity of results, not a routing rule that can be directly deployed.

## 9. Adult CAT under small changes: How much reduction in question volume

When \(SD(\delta)=0.3\), only the Time 2 prior mean is changed to the previous score, but \(SD=1\) is still retained. The number of questions is very close to the standard \(N(0,1)\) prior which does not use old information. The authors reported an average change of less than 0.1 question in the adult domain.

Again this says:

> Moving the prior mean itself does not necessarily shorten the fixed-precision CAT; what really significantly changes the number of questions is to shrink the prior SD and let the old scores contribute more precision.

### well-targeted group

From prior \(SD=1\) to \(0.25\), the average number of questions dropped by about 0.44 questions across fields, ranging from:

- Depression: dropped 0.13 questions;
- Sleep Disturbance: Down 1.00 questions.

The benefits are limited because many well-targeted examinees only do the lowest 4 questions, and there is an obvious floor effect.

What is more practical is \(SD=0.5\):

|field|\(SD=1\) Question volume|\(SD=0.5\) Question volume|
|---|---:|---:|
| Ability to Participate Social | 4.43 | 4.17 |
| Anxiety | 4.16 | 4.01 |
| Depression | 4.13 | 4.02 |
| Fatigue | 4.17 | 4.02 |
| Pain Interference | 4.49 | 4.31 |
| Physical Function | 4.76 | 4.25 |
| Sleep Disturbance | 5.00 | 4.16 |

### poorly targeted group

From \(SD=1\) to \(0.25\), the average reduction in all adult fields is more than 3 questions, but the reason is that CAT is forced to 4 questions.

Under the more reasonable \(SD=0.5\) conditions:

|field|\(SD=1\) Question volume|\(SD=0.5\) Question volume|
|---|---:|---:|
| Ability to Participate Social | 7.72 | 7.34 |
| Anxiety | 7.65 | 7.29 |
| Depression | 7.58 | 7.17 |
| Fatigue | 7.13 | 6.16 |
| Pain Interference | 7.97 | 7.92 |
| Physical Function | 7.97 | 7.27 |
| Sleep Disturbance | 7.34 | 6.05 |

The benefit from the number of questions mainly occurs when the number of questions is close to the maximum of 8 and the item bank provides less information about the true position; however, these people are also most susceptible to the impact of wrong priors, so they cannot just look at the number of questions.

## 10. Adult CAT under small changes: How does RMSE change?

### well-targeted group

The authors report that relative to \(SD=1\), the average RMSE improvement using informed prior is approximately:

\[
0.025,
\]

The different fields are approximately \(0.015\) to \(0.051\). Most fields get the lowest RMSE at \(SD=0.5\).

For example:

|field| \(SD=1\) RMSE | \(SD=0.5\) RMSE | \(SD=0.25\) RMSE |
|---|---:|---:|---:|
| Pain Interference | 0.253 | 0.202 | 0.225 |
| Physical Function | 0.244 | 0.217 | 0.237 |
| Sleep Disturbance | 0.275 | 0.251 | 0.283 |

Although \(SD=0.25\) only takes 4 questions, it is already worse than \(SD=0.5\).

### poorly targeted group

The authors report a cross-domain average RMSE improvement of approximately:

\[
0.059.
\]

Fatigue improves the most at \(SD=0.5\), about \(0.097\):

\[
0.407
\rightarrow
0.310.
\]

But Pain Interference is an obvious counterexample:

| prior SD |Question volume| RMSE |
|---:|---:|---:|
| 1.00 | 7.97 | 0.526 |
| 0.75 | 7.94 | 0.529 |
| 0.50 | 7.92 | 0.573 |
| 0.25 | 4.00 | 0.639 |

The stronger the prior, the shorter the question size or basically the same, but the RMSE continues to get worse. This shows that even if the true change is small overall, individual item banks and locations are still not suitable for reusing old scores.

## 11. Old scores quickly lose value when big changes occur

The difference between the Time 1 score and the Time 2 true state is greater when \(SD(\delta)=0.8\).

### Adult well-targeted

The text states that only Pain Interference and Physical Function are slightly improved at \(SD=0.75\):

- Pain Interference：RMSE \(0.276\rightarrow0.254\)；
- Physical Function：RMSE \(0.239\rightarrow0.233\)。

The lowest RMSE for the rest of the fields generally occurs at \(SD=1\), which adds almost no additional weight to the old score.

### Adult poorly targeted

The text states that there are no domains where accuracy improves due to strengthening the prior. Ability to Participate Social in Table 3 is from:

\[
0.594
\rightarrow
0.587
\]

There is a very small numerical drop at \(SD=0.75\), so "no domain improvement" should be understood as no clear or meaningful improvement, rather than a strictly monotonic worsening of each table value.

The narrowest \(SD=0.25\) reduces all tests to 4 questions and produces serious RMSE:

|field| \(SD=1\) RMSE | \(SD=0.25\) RMSE |
|---|---:|---:|
| Ability to Participate Social | 0.594 | 0.814 |
| Anxiety | 0.516 | 0.775 |
| Depression | 0.518 | 0.761 |
| Fatigue | 0.382 | 0.821 |
| Pain Interference | 0.679 | 0.914 |
| Physical Function | 0.447 | 0.900 |
| Sleep Disturbance | 0.369 | 0.719 |

This is exactly the most dangerous situation in longitudinal measurements:

\[
\text{Quizzes are shorter}
\quad\text{But}\quad
\text{Real changes are pushed back to the old state by prior}.
\]

## 12. Result of children’s item bank

The paper only simulates small changes in the children's field \(SD(\delta)=0.3\).

### well-targeted

The average RMSE improvement is about \(0.013\), which is smaller than the adult field. Most areas are best at \(SD=0.5\), and Mobility is slightly better at \(SD=0.75\).

### poorly targeted

There are only three areas with lower RMSE in \(SD=0.75\):

- Peer Relationships；
- Anxiety；
- Depressive Symptoms。

Fatigue is basically unchanged, while Pain Interference and Mobility are the best at \(SD=1\). Children's item banks are smaller and ceiling/floor effects are more obvious, making prior performance more domain-dependent.

This suggests that the “best prior SD” obtained from one PROMIS domain cannot be directly generalized to other domains or age groups.

## 13. Marking issues that need attention in tables and text

### 13.1 Tables 2 to 4 label prior SD rows SE

The first column of the table is written as:

\[
SE=1,\ 0.75,\ 0.5,\ 0.25.
\]

However, the methods, Figures 1 to 6, and the text all indicate that it is the prior standard deviation that is manipulated. So these lines should be as follows:

\[
SD_{\mathrm{prior}}
=
1,\ 0.75,\ 0.5,\ 0.25
\]

Explanation, they cannot be read as CAT final standard error.

### 13.2 The writing method of the second parameter of \(N(0,0.3)\) is not clear enough

In statistics, some authors use \(N(\mu,\sigma^2)\), and some use \(N(\mu,\sigma)\). This article calls 0.3 the change magnitude/effect size, and uses \(SD(\delta)\) to derive prior, so a more reasonable reading is that the standard deviation of the change is 0.3, rather than the change variance of 0.3.

### 13.3 No Monte Carlo uncertainty or significance tests reported

The question sizes and RMSE in the table are descriptive simulation results, without confidence intervals, Monte Carlo standard errors or model comparison tests. Lower primary index values ​​for "improved" should not automatically be interpreted as stable, significant, or clinically meaningful.

## 14. Relationship with Petersen and Frans

|Research|Sources of supporting information|Whether prior continues to enter the estimate|Do you want to change only the first question?|Main questions|
|---|---|---:|---:|---|
|Petersen et al. (2026)|Another HRQoL area|No|Yes|individualized partial benefits of the first question|
|Frans et al. (2023)|oracle bias or clinical global score|Yes|No|Risk of wrongly strong prior|
|Bass et al. (2026)|Last CAT score in the same field|Yes|No|How to set prior SD under time change|

Bass et al. are not new evidence that "external information only determines the first question", but a longitudinal version of Frans et al.: the old score changes both the initial position and the posterior accuracy and stopping time continuously.

Its unique contribution is to split the prior variance into:

\[
\text{Last scoring error}
+
\text{True state change variance}.
\]

## 15. Evidence boundaries and limitations

### 15.1 This is a simulation, not real longitudinal PROMIS data

Both the first and second responses were generated by the IRT model. The paper did not use repeated measures testing with real patients:

- Whether the change distribution is truly normal;
-Whether the variance is the same for different people;
- Whether prior affects the answering behavior of real patients;
- Whether the savings in question volume are perceptible in actual clinical practice.

### 15.2 prior mean comes from the last CAT, not user self-evaluation

What this article proves is:

> Prior assessment information can be entered into the next CAT.

It does not demonstrate that explicit user self-assessments have the same error structure or stability.

### 15.3 well-targeted layering using real \(\theta_2\)

In real deployment it is not possible to know in advance which group a patient belongs to. The paper does not give an observable rule to determine:

\[
\text{The patient should use}SD=0.5
\quad\text{Still}\quad
SD=1.
\]

### 15.4 There is no independent separation of "first question path" and "continuous prior"

All Time 2 conditions allow prior to persist into EAP. The paper does not compare:

- Select the first question using only the old score;
- Old scores are only used for the initial EAP and are discarded after the first question;
- Old scores persist into the full posterior.

### 15.5 No coverage rate, change detection and exposure indicators

The paper reports question size and RMSE, but does not report directly:

- bias；
- Posterior interval coverage rate;
- Detection rate of minimally important changes;
- False negative change rate;
- item overall and conditional exposure;
- test overlap。

Particularly in longitudinal measurements, looking only at RMSE obscures a key clinical question: whether strong priors systematically shrink true improvement or deterioration toward 0.

### 15.6 At least four questions create an obvious floor

The well-targeted group often only does 4 questions, so the informed prior cannot be shortened even if it is useful. The resulting "marginal benefit is very small" may indicate that the prior is useless, or it may simply be that the existing minimum number of questions rule limits the observable benefit.

## 16. Direct implications for our research design

### 16.1 prior variance should be calibrated jointly from signal error and state change

If the self-assessment occurs at the same time as the CAT, the status change term may be small; if the self-assessment comes from days ago, history, or the last measurement, you should use:

\[
\tau_{\mathrm{current}}^2
=
\tau_{\mathrm{signal}}^2
+
\tau_{\mathrm{change}}^2.
\]

Historical scores cannot be treated as equally precise observations of current conditions.

### 16.2 Use variance to report experimental conditions uniformly

It is recommended that the main experiment write:

\[
\tau^2
\in
\{1.00,0.50,0.25,0.10\},
\]

And also list:

\[
\tau
\in
\{1.00,0.707,0.500,0.316\}.
\]

This can be directly compared with Frans's variance condition, and can also avoid misreading Bass's \(SD=0.5\) as variance 0.5.

### 16.3 Check whether prior has satisfied the stopping rule before testing

For each \(\tau^2\), first compare:

\[
\tau
\quad\text{with}\quad
\varepsilon_{\mathrm{stop}}.
\]

If:

\[
\tau\leq\varepsilon_{\mathrm{stop}},
\]

then it must be stated explicitly:

- Whether to allow 0 questions to stop;
- Whether to enforce a minimum number of questions;
- Whether stopping immediately after the minimum number of questions is considered a success;
- How much of the accuracy comes from the prior, not the formal item.

### 16.4 Make direction-sensitive evaluations of “real changes”

In addition to RMSE, longitudinal simulations should report:

\[
\operatorname{Bias}(
\widehat\Delta
),
\qquad
\widehat\Delta
=
\widehat\theta_2-\widehat\theta_1,
\]

and:

- Proportion of true improvement judged as no change;
- The proportion of true deterioration judged as no change;
- Accuracy of judging direction of change;
- sensitivity and specificity of minimally important changes.

### 16.5 Add prior tempering or dynamic conflict mechanism

If early responses conflict with old scores or self-assessments, the prior variance can be expanded:

\[
\tau_t^2
=
h(
\text{prior-response conflict}
),
\]

Or gradually reduce the prior weight:

\[
p_t(\theta)
\propto
p_0(\theta)^{\lambda_t}
\prod_{s=1}^{t}
p(u_s\mid\theta),
\qquad
0\leq\lambda_t\leq1.
\]

The failure of Bass's \(SD=0.25\) shows that the fixed strong prior lacks a mechanism to "admit that you are wrong".

### 16.6 Complete ablation should include longitudinal conditions

|Conditions|Time 2 first question|Time 2 estimate|purpose|
|---|---|---|---|
|A standard retest|\(0\) nearby| \(N(0,1)\) |baseline|
|B Only change the first question|\(\widehat\theta_1\) nearby|Restore after the first question \(N(0,1)\)|First question path|
|C history prior|Current EAP location| \(N(\widehat\theta_1,\tau^2)\) |continue prior|
|D robust history prior|Current EAP location|Expand on conflict \(\tau^2\)|dynamic protection|

Combined with the current user self-evaluation, you can check:

\[
\text{historical scores}
\quad\text{and}\quad
\text{Current self-evaluation}
\]

Who is more reliable when predicting the current state, and how to deal with conflicts between the two.

## 17. Chinese paraphrases that can be quoted safely

### Support "the variance of the retest prior should include the uncertainty of change"

> Bass et al. (2026) pointed out that longitudinal CAT cannot only use the final standard error of the first measurement as the second prior uncertainty; a reasonable prior variance should also include the individual differences in the true change between the two measurements, otherwise the old score will be given too much weight.

### Support "moderate strength prior may be best for small changes"

> In the test-retest simulation of the official PROMIS item bank, when the standard deviation of the change in health status is 0.3, the prior \(SD=0.5\) usually obtains a lower RMSE with the same or fewer questions; the benefit of just moving the prior mean and keeping \(SD=1\) is small.

### Support "narrow prior can hinder change detection"

> When prior \(SD=0.25\), the minimum four-question rule causes many CATs to stop immediately at the fourth question; when health status changes, the strong contraction of the old scores on the posterior causes the RMSE to rise, resulting in shorter but less accurate retests.

### Support "item bank coverage determines the marginal role of prior"

> For patients located in the high information area of the item bank, the standard PROMIS CAT often stops at at least four questions, and the additional benefit of individualized prior is very small; for patients with insufficient item bank coverage, the prior has a greater impact on the number of questions and final estimates, and the risk is also higher.

### Cannot be quoted like this

- It cannot be written as "Bass et al. only use the last score to select the first question";
- \(SD=0.25\) cannot be written as prior variance \(0.25\);
- Stopping at four questions cannot be interpreted as obtaining enough information from four new questions;
- It cannot be claimed that real patient longitudinal CAT has verified the reduction in question volume;
- cannot be written as informed prior Improves accuracy in all PROMIS areas;
- Results from small changes in conditions cannot be generalized to patients who are likely to experience significant improvement or deterioration.

## 18. Key references and their role

- **van der Linden (1999)**: Empirically initialized CAT ability estimate.
- **Frans et al. (2023)**: Question size benefits and incorrect prior risks of empirical priors in clinical multilevel scoring CAT.
- **Petersen et al (2025)**: Use cross-domain information to select individualized first questions in the EORTC CAT Core physical function domain.
- **Wang, Berger, & Burdick (2013)**: Background on Bayesian modeling of true trajectory variation and measurement error in dynamic IRT.
- **Terwee et al. (2021)**: Conceptual and empirical scope of PROMIS minimally important change.
- **Choi et al. (2010)**: PROMIS static short form and CAT efficiency background.
- **Morris et al. (2017) and Bass et al. (2025)**: PROMIS multivariate CAT and stopping rule efficiency study.

## 19. Read the conclusion carefully

Bass et al. advanced the issue of empirical prior from "whether the auxiliary information is accurate" to "whether the auxiliary information will be outdated":

\[
\text{Uncertainty about old fractions}
\neq
\text{Uncertainty about the current state}.
\]

The appropriate strength of the longitudinal prior depends on:

\[
\underbrace{SE(\widehat\theta_1)^2}_{\text{Last measurement error}}
+
\underbrace{SD(\delta)^2}_{\text{true change difference}}.
\]

The most important caveat for us from this paper is this: a strong prior can easily make shorter CATs, but if it makes the system lose the ability to detect changes in the current, this "efficiency" has no measurable value. ** The method contribution should therefore not simply be to set the prior narrower, but to allow the prior strength to co-vary with signal reliability, time intervals and early response collisions.
