# Pitkin and Vispoel (2001): A meta-analysis of Self-Adapted Testing and CAT

!!! abstract "Key takeaway"
    **What was done:** Pitkin and Vispoel compiled 19 ability comparisons and 8 posttest anxiety comparisons from earlier studies of Self-Adapted Testing and CAT. **What we got:** Self-selected items on average corresponded to slightly higher ability estimates (about \(0.11SD\)) and slightly lower posttest anxiety (about \(0.18SD\)), but the effects were small, the study design was heterogeneous, and selection, feedback, and scoring were confounded. **Conclusion on this topic:** It supports "the right to choose may change emotions and the answering process", but it does not comprehensively examine the number of questions, standard error or time taken, so it cannot prove that self-selected items improve CAT efficiency or that reduced anxiety leads to an increase in scores.

## Citation details

> Pitkin, A. K., & Vispoel, W. P. (2001). Differences between self-adapted and computerized adaptive tests: A meta-analysis. *Journal of Educational Measurement, 38*(3), 235–247. [DOI](https://doi.org/10.1111/j.1745-3984.2001.tb01125.x)

- Research type: Early stage quantitative research synthesis
- Scope included: 19 ability comparisons and 8 posttest anxiety comparisons from 15 studies
- Main comparison: Self-Adapted Tests (SATs) vs. Computerized Adaptive Tests (CATs)
- Main result: SAT ability estimate is on average \(0.11\) standard deviations higher, and post-test anxiety is on average \(0.18\) standard deviations lower
- After correction for measurement errors: ability difference \(d=0.12\), anxiety difference \(d=0.19\)
- Key boundary: The paper does not integrate test length, time, standard error or item exposure, nor does it prove that the decrease in anxiety causes the increase in ability estimate

!!! important "The most direct judgment on this topic"
    The most supportive aspect of this article is not the amount of questions, but the fact that the test format may change the mood and answering process of the test taker. If only the first question or the first \(k\) self-evaluation is allowed to affect, it may be possible to retain a sense of control while avoiding the accuracy and time costs of the entire self-selected items; however, this inference requires new randomized experiments, and the meta-analysis itself did not test this mixed design.

## 1. What is the difference between SAT and CAT?

### 1.1 The control of CAT lies in the algorithm

Standard CAT updates the ability estimate and measurement error after each question, and then selects the question from the item bank that can best reduce the current error until the fixed test length or accuracy stopping criterion is reached.

### 1.2 The control of SAT lies with examinee

A typical SAT divides items into six or eight levels according to difficulty parameter \(b\). The process for each question is:

1. examinee to select the difficulty level;
2. The system presents a question from this level;
3. examinee to answer;
4. Usually get correctness feedback;
5. Select the difficulty level of the next question.

Therefore, what the SAT changes is not just the first question, but the control over the selection of the entire test.

### 1.3 Why SAT may affect scores

In the standard Item Response Theory (IRT) framework, if the model is established, the item parameters are on a common measurement scale, and the comparison groups are randomly equivalent, then different item sets should not cause systematic differences in average ability.

There are still mean differences between SAT and CAT, and there are at least three possible explanations:

- SAT allows examinee to choose a more appropriate or advantageous level of difficulty;
- Options and feedback change anxiety, attention or motivation, causing the response state to change;
- Question selection, stopping or scoring methods cause ability estimate bias.

The task of a meta-analysis is to estimate how large the difference is on average, not to identify which of the three mechanisms holds true.

## 2. Why meta-analysis is needed

Results from earlier studies were inconsistent:

- Some studies have found that SAT ability estimate is higher and post-test anxiety is lower;
- Some studies show no significant differences;
- A few comparisons even favor CAT.

A single study is easily affected by sample size, test content, item bank, feedback, difficulty level and stopping rule. Pitkin and Vispoel therefore converted existing comparisons into a unified standardized mean difference \(d\) and then calculated a weighted average across studies.

## 3. How to find and include documents

Author search:

- ERIC；
- Psychology Journal；
- Dissertation Abstracts。

Keyword combinations include anxiety, test anxiety, computer-assisted testing, and computerized adaptive testing. At that time, the database did not have the subject heading self-adapted testing, so some information was provided directly by the study authors.

Finally, 15 studies with the information needed to calculate effect size were found, forming:

\[
k_{\theta}=19
\]

Ability estimate comparison, and:

\[
k_{A}=8
\]

Comparison of post-test anxiety.

!!! warning "This is not a complete system review in the modern sense"
    The paper did not report clear search start and end dates, reasons for stepwise exclusion, repeat screener agreement, risk of bias assessment, or publication bias analysis. Requesting materials directly from the authors may include some gray literature, but there is no way to prove that the direction of the omitted studies was random.

## 4. How representative are the samples and tests?

The examinee in the 19 experimental comparisons is composed of:

- 1 is a senior elementary school student and a junior high school student;
- 1 is a junior high school student;
- 1 is a high school student;
- 2 mixed high school seniors and college undergraduates;
- 2 include undergraduate students only;
- 1 includes graduate students only;
- 11 mixed undergraduate and graduate students.

So results are most generalizable to college students, rather than to children, clinical populations, or large high-stakes examinations.

IRT models are also not uniform:

|model|Number of experiments|
|---|---:|
|three-parameter model| 3 |
|Two-parameter model, fixed \(c\)| 8 |
|two-parameter model| 1 |
|One parameter model, fixed \(c\)| 6 |
|one parameter model| 1 |

Additionally, only 4 of all comparisons were conducted by researchers other than those at the University of Iowa or the University of Nebraska. Research teams, software, item banks, and operational traditions are highly centralized, limiting external validity.

## 5. How is effect size defined?

### 5.1 ability estimateeffect size

Ability estimates for SAT and CAT, the author defines:

\[
d_{\theta}
=
\frac{
\overline\theta_{\mathrm{SAT}}
-
\overline\theta_{\mathrm{CAT}}
}{S_w},
\]

where \(S_w\) is the combined within-group standard deviation. Therefore:

\[
d_{\theta}>0
\]

Indicates that the average ability estimate of SAT is higher than that of CAT.

### 5.2 Post-test anxiety effect size

The direction of the anxiety indicator is defined inversely:

\[
d_A
=
\frac{
\overline X_{\mathrm{CAT}}
-
\overline X_{\mathrm{SAT}}
}{S_w}.
\]

So:

\[
d_A>0
\]

Indicated lower post-test anxiety on the SAT.

Both effects specify positive values as “SAT may have an advantage,” an artificial direction that must be kept in mind when reading Table 1 .

### 5.3 It is Cohen's formula \(d\), not small sample corrected Hedges \(g\)

The authors directly standardized by the pooled within-group standard deviation and did not report small sample bias correction. Most samples are not small, but the minimum experimental sample size is only 24. The uncorrected \(d\) may be slightly positively biased in small samples.

## 6. How to merge across studies

The author uses the Hunter and Schmidt (1990) procedure to construct a weighted average using \(d\) from each study, first calculates the uncorrected result, and then corrects the effect size based on the measured reliability.

The paper does not itemize the final weights in the text or in Table 1, so it is not possible to reconstruct the contribution of each comparison to the combined value from that page alone.

### 6.1 What reliability is used for measurement error correction?

The anxiety scale mainly uses alpha reliability. ability estimatereliability is usually measured by:

\[
\rho_{\theta}
=
1-\overline{\sigma_e^2}
\]

way, obtained from the average ability estimateerror variance; this way of writing relies on the ability measurement scalevariance being normalized to 1.

But not all reliability in Table 1 is reported directly:

- One study derived reliability from the median average standard error of SAT and CAT, which the authors acknowledged may overestimate reliability;
- Several studies lack standard error or error variance, directly borrowing .87 from previous studies with the same test length, the same population, and the same item bank.

Therefore, the "corrected effect" is not entirely derived from each study's own direct reliability evidence. Fortunately, the original measurement reliability is generally high and the correction range is very small.

### 6.2 How to calculate confidence interval

The author uses:

\[
SE_{\overline d}
=
\frac{SD_d}{\sqrt{k}},
\]

Among them, \(SD_d\) is the standard deviation of the observed effect size, and \(k\) is the number of effect sizes.

This formula compresses the dispersion between effect sizes into the mean standard error, but does not deal with it explicitly:

- The same research contributes to the dependence of multiple effect sizes;
- The effect size sampling variance caused by different sample sizes;
- True heterogeneity between studies;
- Small sample effect size correction;
- Research team clustering.

By modern meta-analytic standards, these confidence intervals may be overly optimistic.

## 7. What is the pattern of the single effects in Table 1?

### 7.1 ability estimate comparison

The 19 capabilities \(d\) range approximately:

\[
-.145\text{to}.437.
\]

Of these, 13 were positive and 6 were negative. The largest positive effect is .437, but there are studies favoring CAT. The result is not that "every study finds that SAT is higher", but that the majority of positive effects are positive and the average is small.

### 7.2 Anxiety comparison

All 8 anxiety effects were positive and ranged from approximately:

\[
.040\text{to}.373.
\]

The direction is relatively consistent, but the number is only 8, and most of them come from similar research teams. Selective reporting or common method factors cannot be ruled out simply by being “all positive”.

## 8. What is the merged result?

|result|Uncorrected \(d\)|After measurement error correction \(d\)|Uncorrected 95% CI|
|---|---:|---:|---:|
|SAT ability estimate is higher than CAT| .11 | .12 | [.05, .17] |
|SAT post-test anxiety was lower than CAT| .18 | .19 | [.10, .26] |

### 8.1 Differences in abilities

\[
d_{\theta}=.11
\]

The ability estimate representing the SAT is on average about 0.11 standard deviations higher. Corrected for measured reliability is .12.

### 8.2 Anxiety differences

\[
d_A=.18
\]

Posttest anxiety for the SAT was on average about 0.18 standard deviations lower. Corrected to .19.

If the standard deviation of the resultscale is 10, this roughly corresponds to a 1.1 point difference in ability and a 1.8 point difference in anxiety. The authors therefore call the average effect modest.

### 8.3 The original text’s representation of a number is inconsistent

The author clearly states that the confidence intervals are for uncorrected effects, so they should correspond to .11 and .18 respectively. Then write these intervals to show that the overall \(d=.12\) and \(.18\) are not just sampling errors: the former uses corrected values, and the latter uses uncorrected values.

A safer way to write it is:

> The uncorrected effects are .11 and .18 respectively, corresponding to the 95% intervals [.05, .17] and [.10, .26]; the reliability-corrected point estimates are .12 and .19, but the paper does not report additional corrected intervals.

## 9. "Higher ability estimate" does not equal "higher real ability"

There are at least two competing sets of explanations for the higher SAT ability estimate than the CAT.

### 9.1 Explanation 1: SAT estimates are positively biased

When examinee controls the difficulty, it may continue to select questions that seriously do not match the actual ability. Different estimators will have biases in different directions:

- Maximum likelihood estimation may diverge or shift under extreme or mismatched response patterns;
- Bayesian estimation will pull the result towards the prior mean;
- When the item bank lacks information questions at the end of the ability, the bias will be more obvious.

For example, if there are 20 fixed questions and the examinee always chooses the easiest questions and answers them all correctly, the maximum likelihood estimate may tend to be positive infinity.

The simulation cited by the author shows that in order for the SAT to reduce bias, it must ultimately select enough questions that truly match ability. Available protections include fixed accuracy stopping, forcing a difficulty level change after consecutive correct or incorrect answers, and ensuring that the item bank has information in each ability area.

### 9.2 Explanation 2: SAT reduces anxiety and brings performance closer to attainable levels

The SAT may improve performance through the following mechanisms:

- Examine and select the appropriate difficulty level based on your current abilities, emotions and motivations;
- Choices and feedback keep attention on task;
- Sense of control reduces anxiety and feelings of helplessness.

Some studies have also found a weak relationship between SAT scores and pretest anxiety. However, this meta-analysis only combined the effect of "form on ability" and the effect of "form on anxiety" respectively, without testing:

\[
\text{SAT}
\rightarrow
\text{Anxiety decreases}
\rightarrow
\text{Improved performance}.
\]

Therefore, the anxiety mediator is only a plausible explanation and not an established causal mechanism. Post-test anxiety may also be reduced by feeling like one performed better, and the cause and effect may be in the opposite direction.

### 9.3 Why can’t IRT invariance be used for direct adjudication?

The item invariance of IRT requires that the response model and parameters remain applicable between testing situations. If the sense of control, feedback, or strategies of the SAT alters the answering process, then the response function for the same question may be different in the SAT versus CAT context.

On the other hand, average capability differences may also result from estimation bias or implementation differences. Therefore, this result prompts that situation dependence and measurement invariance need to be tested, but it cannot alone prove that "SAT measures more real abilities."

## 10. Why the full SAT is usually less accurate than the CAT

Under a fixed test length, the CAT algorithm directly selects the questions that can best reduce measurement errors; the SAT examinee can usually only choose from a few rough difficulty levels, and may not be able to find the most statistically matching questions.

The authors concluded that the fixed test lengthreliability of the SAT was generally lower than that of the CAT in earlier studies. Possible improvements include:

1. Provide correctness feedback for each question;
2. Add optional difficulty levels;
3. After the user selects a difficulty level, the algorithm selects the most informative questions within the level for the current \(\widehat\theta\);
4. When you get consecutive correct or incorrect answers, you will be forced to move to the adjacent difficulty level.

The third item is especially like the hybrid design of this topic: the user provides a rough location, and the algorithm is responsible for finely selecting topics in that area.

!!! warning "Accuracy is not a combined outcome of meta-analysis"
    Paper discussion SAT is generally less reliable under fixed test length, but there is no meta-analysis of poor reliability, standard error, or the number of questions required to achieve the same accuracy. The qualitative summary of the discussion paragraph cannot be written as the third pooled effect obtained by this meta-analysis.

## 11. Why the full SAT is usually slower

The SAT requires longer instructions, and the examinee has to select and confirm the difficulty before each question, so it may take more time even if the number of questions is the same.

At the fixed precision stop, the SAT may also require more questions because each question has less information. The authors quote Vispoel et al. (1994): SAT takes 43% longer than CAT at the same accuracy stop.

This 43% is the result of one study, not the pooled estimate of this article's meta-analysis. There is no comprehensive average time or number of questions for papers.

## 12. Conflict between freedom of choice and measurement protection

The author points out that restricting topic selection can avoid extreme mismatches and infinite estimates, and can also help with content balance and exposure control; however, restrictions may weaken the sense of control and anxiety benefits of the SAT.

Roos et al. (1998) provided an example: posttest anxiety for the restricted SAT was not significantly different from the CAT, but was higher than the unrestricted SAT. That is to say:

\[
\text{More freedom of control}
\longrightarrow
\text{May be less anxious},
\]

But at the same time:

\[
\text{More freedom of control}
\longrightarrow
\text{Higher risk of mismatch, exposure and manipulation}.
\]

This is not simply "more freedom is better" but a design trade-off between psychological benefits and measurement constraints.

## 13. How does the author evaluate practical applications?

### High risk scenario

The authors believe that if the full SAT is used for high-stakes decision-making, it needs to:

- Larger item bank;
- Algorithm to prevent overexposure;
- Content balance;
- Prevent the ability estimate from being raised through topic selection strategies;
- Maintain stopping rules with sufficient accuracy.

Given that the average benefit was only about .1–.2 standard deviations, in 2001 the authors considered widespread implementation unrealistic.

### Low risk scenario

The authors argue that the SAT is more likely to be used for formative assessment, teaching placement, and diagnosis of learning difficulties, but caution: Low risk does not mean no consequences. If the examinee obtains falsely high scores through test writing or strategies, he or she may still be placed in an inappropriate teaching environment.

This judgment directly refutes an overly strong assumption: just because a mental health or learning situation is not a high-stakes exam, it does not mean that the examinee information must be accurate, honest, and unstrategic.

## 14. Main limitations of meta-analysis methods

### 14.1 Small number of studies and strong dependence

- Ability only has 19 effects;
- Anxiety has only 8 effects;
- Multiple effects come from the same research report;
- All but 4 experiments were from two similar research centers.

The paper does not use multilevel meta-analysis or cluster-robust variance to deal with dependencies.

### 14.2 No heterogeneity statistics

The paper does not report \(Q\), \(\tau^2\) or \(I^2\), nor does it have a random effects model. Effects merged across age, content, IRT model, feedback format, difficulty level, and stopping rule, but these differences were not entered into the moderator analysis.

### 14.3 No publication bias or small sample bias analysis

There are no funnel plots, choice models, Egger's tests or trim-and-fill, and no Hedges \(g\) correction. Although some conference papers and degree materials reduce the risk of including only significant results from journals, selective availability cannot be ruled out.

### 14.4 "SAT" is not a unified treatment

Different experiments may change simultaneously:

- Whether to provide feedback for each question;
- Several levels of difficulty;
- Whether to limit extreme choices;
- Use fixed test length or fixed precision;
- MLE or Bayesian scoring;
- item bank parameters and content;
- Designed within participant room or participant.

The merger effect is therefore an average difference across "early SAT implementation packages" and not a pure "option effect".

### 14.5 Three limitations of the paper itself

The author explicitly acknowledges:

1. Only compares SAT and CAT, without comprehensive SAT and fixed-question tests;
2. The effect size is small, the research team is concentrated, and the content area is not broad enough;
3. None of the topic selection algorithms studied at that time controlled item exposure and content balance at the same time.

## 15. Direct implications for our research design

### 15.1 Don’t treat the full SAT as the only experimental group

The most critical design considerations should be to separate control durations:

1. Standard CAT: Topics selected entirely by algorithm;
2. self-informed first item: The user only affects the first item;
3. self-informed first \(k\) items: User-informed first \(k\) items;
4. Personalized prior CAT: Self-evaluation enters the complete prior;
5. Full SAT: Each question has a user-selected difficulty level.

This could examine whether the psychological benefits require only a small amount of early control without the accuracy costs of a full SAT.

### 15.2 Separating psychological mechanisms from measurement efficiency

Measure at least simultaneously:

- State anxiety before and after the test;
- perceived control；
- Set reliability and self-efficacy;
- response time effort or quick guess;
- Question volume, time and selection time for each question;
- Bias, RMSE, coverage rate and stop errors.

If we only find that the number of questions has been shortened, we cannot say that it is a sense of control or anxiety mechanism; if we only find that anxiety has decreased, we cannot say that the measurement is more efficient.

### 15.3 Really check the intermediary

After randomly assigning quiz formats, you can explicitly establish:

\[
\text{Test format}
\rightarrow
\text{Changes in sense of control or anxiety}
\rightarrow
\text{answer and ability estimateresult}.
\]

There is a need to measure pre- and post-changes and perform mediation analyses, rather than inferring mechanisms from two independent average effects as in this meta-analysis.

### 15.4 Signal quality still needs to be reported in low-risk scenarios

Should be estimated directly:

\[
\operatorname{Cor}(s_i,\theta_i),
\]

Self-assessment error distributions, overconfidence proportions, and calibration curves by ability level. Low risk only reduces certain incentives to cheat and does not automatically eliminate misjudgments, reaction styles, social desirability, or strategic behavior.

### 15.5 Potential advantages of hybrid designs

This meta-analysis exposed a gap: the early literature mainly compared two endpoints - CAT fully controlled by the algorithm and SAT fully controlled by the examinee.

This topic studies the middle area:

\[
\text{Few user controls}
+
\text{prior with uncertainty}
+
\text{Subsequent algorithms take over}.
\]

The potential contribution is not to once again prove that the SAT is different from the CAT, but to determine the minimum amount of user control required to retain useful subjective information or psychological benefits while maintaining the accuracy, question volume, and item bank security of the CAT.

## 16. Quote-safe Chinese paraphrasing

### Used to summarize ability differences

> Pitkin and Vispoel (2001) synthesized 19 early comparisons and found that the ability estimate of SAT was on average 0.11 standard deviations higher than that of CAT; it was 0.12 after correction for measured reliability, but the authors evaluated this difference as small.

### Used to summarize anxiety differences

The pooled effect of > 8 post-test anxiety comparisons is 0.18 standard deviations, and the directions are all in favor of SAT; the reliability correction is 0.19, but the number of studies is small and most of them come from similar research teams.

### Used to qualify causal explanations

> The meta-analysis simultaneously observed higher ability estimates and lower post-test anxiety on the SAT, but did not test the mediating role of anxiety. Therefore, it cannot be concluded that a decrease in anxiety leads to an increase in performance.

### Used to illustrate the efficiency boundary

> Early SAT is generally not as accurate as CAT under fixed test length, and examinee question-by-question selection will increase the test time; however, this meta-analysis did not combine question volume, standard error or time, and the relevant conclusions mainly come from the single study cited in the discussion.

### Used to connect to this item

> Early evidence focuses on comparing the full process of self-selected items with the full process of algorithmic question selection. It has not been answered yet whether it only allows the examinee to affect the first question or the previous \(k\) questions. Can the sense of control and auxiliary information gains be retained while avoiding the accuracy cost of the full SAT.

## 17. Key References

- Pitkin, A. K., & Vispoel, W. P. (2001). Differences between self-adapted and computerized adaptive tests: A meta-analysis. *Journal of Educational Measurement, 38*(3), 235–247. [https://doi.org/10.1111/j.1745-3984.2001.tb01125.x](https://doi.org/10.1111/j.1745-3984.2001.tb01125.x)
- Hunter, J. E., & Schmidt, F. L. (1990). *Methods of meta-analysis: Correcting error and bias in research findings*. Sage.
- Rocklin, T. R., O'Donnell, A. M., & Holst, P. M. (1995). Effects and underlying mechanisms of self-adapted testing. *Journal of Educational Psychology, 87*(1), 103–116.
- Wise, S. L., Plake, B. S., Johnson, P. L., & Roos, L. L. (1992). A comparison of self-adapted and computerized adaptive tests. *Journal of Educational Measurement, 29*(4), 329–339.

## 18. Judgment after reading

This meta-analysis confirms that the SAT and CAT do produce small but stable average differences across self-selected items: slightly higher ability estimates and slightly lower post-test anxiety. But it also demonstrates that the advantages of the SAT are not so great that issues of accuracy, time, exposure, content balance, and strategic manipulation can be ignored.

For this topic, this is not evidence that "our idea has been completed", but it helps to narrow the problem: early studies compared two extremes, and there has not yet been a systematic study of self-evaluation that only affects the beginning, and then the intermediate design that is taken over by individualized prior and standard CAT. What really needs to be verified is whether this intermediate design can shorten the number of questions with the same stopping accuracy, while avoiding false self-evaluation, false certainty and concentrated exposure at the tail of the item bank, and whether the psychological benefits still exist.
