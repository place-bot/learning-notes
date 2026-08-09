# Wise et al. (2005): Can self-selected difficulty improve effort and performance on low-stakes tests?

!!! abstract "Key takeaway"
    **What was done:** Wise et al compared fixed tests, standard CAT, regular self-adapted testing, and point-game self-adapted testing on a low-stakes 40-item mathematics test and measured ability, questionnaire effort, and response time effort. **What you got:** No significant differences were detected among the four groups on these outcomes, indicating that providing question-by-question choice or even a points framework did not automatically improve effort or performance. **Conclusions on this topic: **Low-risk scenarios allow for the exploration of self-evaluation, but "autonomy will improve motivation" cannot be regarded as a mechanism premise; the sessions in this article are distributed hierarchically and there are very few effective sessions, and non-significant results cannot be interpreted as strictly equivalent.

## Citation details

> Wise, S. L., Owens, K. M., Yang, S.-T., Weiss, B., Kissel, H. L., Kong, X., & Horst, S. J. (2005, April). *An investigation of the effects of self-adapted testing on examinee effort and performance in a low-stakes achievement test*. Paper presented at the annual meeting of the National Council on Measurement in Education, Montreal.

- Research type: Four groups of computer test experiments, conference papers
- Sample: 711 introductory psychology course participants; main results table actual use 696 people
- Low-stakes meaning: Credit for research participation is earned, there are no personal consequences for test performance
- Test content: 40 retired ACT math questions
- Four conditions: fixed item test, computerized adaptive testing, ordinary self-adapted testing, integral game self-adapted testing
- Main conclusion: There is no significant difference between the four tests in terms of average ability, questionnaire effort and response time effort.

!!! danger "The easiest place to read this article wrong"
    What the paper got was "no differences in test types were detected", not "the four tests have been shown to be equivalent". The experiment only has 15 valid sessions, the treatments are allocated at the session level, and the table sample size and ANOVA labeling are inconsistent in many places; non-significant results cannot be interpreted as an exact zero effect.

## 1. Why low-stakes testing is a question of validity in the first place

Low-stakes tests have few personal consequences. ExameYou will not lose your grades, qualifications or rewards even if you answer questions quickly and incorrectly. The observed score at this point might be:

\[
\text{Observe performance}
=
f(\text{real ability},\text{answer diligently},\text{test situation}).
\]

If low efforters' scores are systematically lower than their true abilities, effort is not random noise but systematic variation unrelated to the target construct. The author cited Wise and DeMars (2005) to point out that in existing studies, low-motivators were on average more than half a standard deviation lower than high-motivators, but this was only background evidence of research motivation and was not a re-estimated effect in this experiment.

What this article wants to answer is: Can more people answer questions seriously under low-risk conditions simply by changing the format of the computer test?

## 2. Why two sets of theories predict that adaptive forms may be effective

### 2.1 Expectation-value model

Expectancy-value theory suggests that task engagement depends on:

\[
\text{work hard}
\approx
f(\text{Expectation of success},\text{mission value},\text{perceived cost}).
\]

Low-stakes tests have low personal utility and real opportunity costs, so some examinees may reduce investment.

### 2.2 Snow’s aptitude dual path

Snow splits task performance into two paths:

- Performance pathway: whether cognitive resources can complete the task;
- Commitment pathway: Whether will, emotion and motivation resources are willing to continue investing.

Traditional measurement focuses more on the first item; low-risk scenarios make the second item a validity threat.

### 2.3 Why CAT may improve motivation

Computerized adaptive testing (Computerized Adaptive Testing, CAT) brings item difficulty close to current capabilities. Theoretically:

- People with high abilities are less likely to be bored because items are too easy;
- People with low abilities are less likely to be frustrated by items that are too difficult;
- Moderate challenge may increase intrinsic motivation.

But the primary design goal of CAT is to measure efficiency, and motivational benefits are only possible side effects.

### 2.4 Why S-AT may go further

Self-adapted testing (Self-Adapted Testing, S-AT) allows the examinee to choose the difficulty before each question. The authors hypothesized that consistently making choices would increase feelings of control and engagement, thereby increasing effort.

Note: This is not "self-assessment first and then returning to CAT", but the difficulty level of the entire 40 questions is selected by the examinee.

## 3. What are the differences between the four experimental conditions?

|Conditions|full name|How item is generated|Feedback or not|Whether to choose difficulty|
|---|---|---|---|---|
| FIT |Fixed-Item Test, fixed item test|Everyone does the same set of 40 questions|Question-by-question correctness feedback not reported|No|
| CAT |Computerized Adaptive Test, computerized adaptive testing|The first 4 questions are randomly selected from the 20 most informative questions in \(\theta=0\); questions with the largest amount of information are selected from the 5th question onwards.|Question-by-question correctness feedback not reported|No|
| S-AT |Self-Adapted Test, self-adapted testing|Choose one of the six difficulty levels before each question, and then randomly select questions within the level without replacement.|Yes|Yes|
| EISS S-AT |Examinee-Informed, Stratum-Scored S-AT, examinee-informed self-adapted testing|Same as S-AT, but with clear points scored and lost per tier|Yes, and show points changes|Yes|

The four conditions are fixed as:

\[
40\text{question},
\]

Instead of stopping with the same standard error. Therefore, this article cannot answer which form achieves the same accuracy with fewer questions.

## 4. The “bet” mechanism of EISS S-AT

EISS S-AT is designed with six levels of difficulty with different risk-benefit options:

|difficulty level|Bonus points for correct answers|Points deducted for wrong answers|
|---:|---:|---:|
| 1 | +1 | -6 |
| 2 | +2 | -5 |
| 3 | +3 | -4 |
| 4 | +4 | -3 |
| 5 | +5 | -2 |
| 6 | +6 | -1 |

Exame starts with 100 points and after each question you see:

1. True or false;
2. Points will be added or deducted for this question;
3. Updated total points;
4. The difficulty level you just selected.

This makes the choice akin to a bet on whether you can get it right. The author hopes that the sense of play will continue to attract attention.

The author cites Wise (1999a, 1999b) to show that this hierarchical integral is highly correlated with the maximum likelihood estimate in other studies, about:

\[
r=.98\text{to}.99.
\]

However, in order to ensure that the four groups are comparable, this article does not regard the integral as the ability result, but uniformly calculates the bounded maximum likelihood (ML) ability estimate:

\[
-4\le\widehat\theta_{ML}\le4.
\]

## 5. item bank and topic selection algorithm

### 5.1 item bank

The study obtained retired items from four publicly available 60-question ACT math papers. In order to reduce the impact of the original test time limit on the final answers, the last 6 questions of each set are not included in the calibration; another 1 question is eliminated because everyone answered it correctly. The final item bank is:

\[
214\text{question}.
\]

The calibration sample for each set of volumes ranges from 2,748 to 2,921 people, using a three-parameter logistic Item Response Theory (3PL IRT) model. The authors assumed that the four sets of volumes came from random equivalence groups, so no measurement scale linking was performed.

!!! warning "Not linking is a material assumption"
    "Four sets of calibration samples are randomly equivalent" does not mean that it has been verified that the parameters of the four sets of questions are at the same measurement scale. If this assumption does not hold, directly combining four volumes of items into one item bank may introduce scale errors. The paper does not report equating tests or link sensitivity analyses.

### 5.2 Six difficulty levels

Questions 214 are sorted according to difficulty parameter \(b\) and divided into six levels. S-AT and EISS S-AT draws questions randomly without replacement within the selected layer each time.

### 5.3 FIT

FIT uses a fixed set of 40 questions, selected according to the content specifications of the full ACT math paper. The average item parameters of this volume are:

\[
\bar a=1.10,
\qquad
\bar b=0.01,
\qquad
\bar c=.19.
\]

### 5.4 CAT

The first 4 questions of CAT are randomly selected from the 20 questions with the highest information at \(\theta=0\) to form an initial ability estimate; after the fifth question, the maximum amount of information is used to select questions and update the ability one by one.

CAT does not use content balancing or itemexposure control. The S-AT two groups also only selected questions according to difficulty level, and did not report balanced content. Therefore, the content combinations obtained by the four groups may not be equivalent.

## 6. Samples, allocations and experimental levels

### 6.1 Sample

- Total recruitment: 711;
- Gender: 23% male, 77% female;
- Source: Introductory psychology subject pool at a mid-sized southern US university;
- Participation Requirements: Participate in research or complete alternative written assignments for course credit;
- Ability to analyze actual \(N=696\) with response time.

The difference between 711 and 696 is 15 people. In the paper's narrative, one S-AT session was excluded due to network outage, so these 15 people were likely from that session, but the author did not clearly correspond with a sample flow chart.

### 6.2 Not random allocation of individuals

Participants first register for the session by themselves, and then the entire session is assigned to a test format:

\[
\text{participants}
\subset
\text{Number of sessions}
\subset
\text{Quiz type}.
\]

The original plan was for 16 games, four in each format. An S-AT session first encountered a server outage, then encountered a fire alarm when retesting, and finally gave up. Therefore, there are only:

\[
15\text{valid sessions}.
\]

In principle, each of the four invigilators is responsible for one session of each of the four conditions and uses a unified script to control the invigilator effect.

!!! warning "The original power analysis overestimated the amount of design information"
    The study estimates that each group has at least 80 people based on individual level \(d=.50\) and power=.80, and the final number of people in each group exceeds 128. But treatments are allocated at the session level, and a truly independent treatment unit is closer to 15 sessions than 696 individuals. The original power analysis did not specify whether to consider intra-group correlation, so it cannot be claimed to have predetermined testing power based solely on the number of people in each group.

## 7. How to measure the three result variables

### 7.1 Ability Performance

All four groups use 3PL IRT's bounded ML ability estimate to compare performance under different item paths.

### 7.2 Self-reported efforts

The effort scale of the Student Opinion Survey (SOS) contains 5 questions. The author only analyzed SOS-Effort and did not use importance scale or total motivation score.

The SOS is administered after completing 40 questions, so it measures overall feelings afterwards, not changes in effort on a question-by-question basis.

### 7.3 response time effort

Response Time Effort (RTE) divides the response to each question into:

\[
\text{response time}<10\text{seconds}
\Rightarrow
\text{rapid guessing},
\]

\[
\text{response time}\ge10\text{seconds}
\Rightarrow
\text{solution behavior}.
\]

Individual RTE is the proportion of items judged to have solution behavior:

\[
RTE_i
=
\frac{
\#\{\text{response time}\ge10\text{Second question}\}
}{40}.
\]

All questions share a 10-second threshold, and the paper does not set item-specific thresholds based on item length, difficulty, or reading requirements. This simplification may misjudge a quick but serious response as a guess, or may misjudge a low-effort response of more than 10 seconds as a serious response.

## 8. Why use hierarchical ANOVA?

Because processing is distributed at the field level, individual observations are not independent. The author uses hierarchical analysis of variance (hierarchical ANOVA) on the three results. The main structure is:

\[
\text{student}
\text{ nested in session}
\text{ nested in test type}.
\]

and simultaneously analyzed the interaction of gender and test type.

This treatment is in the right direction: 696 people cannot be treated as if they were completely independent and randomly received the four treatments. However, the number of effective fields is very small, so the denominator degrees of freedom of the test type main effect are only about 15 to 17, instead of more than 600.

## 9. Main result: There is no difference in test type among the three endings

### 9.1 Ability Performance

|Conditions|Average \(\widehat\theta\)| SD | \(N\) |
|---|---:|---:|---:|
| FIT | 0.32 | 0.63 | 190 |
| CAT | 0.17 | 1.42 | 185 |
| S-AT | 0.14 | 0.80 | 136 |
| EISS S-AT | 0.18 | 0.90 | 183 |

Test type effect:

\[
F(3,17.02)=1.04,
\qquad
p=.399.
\]

The gender and test type times gender interaction was also not significant.

The mean of FIT is ostensibly the highest, but the difference fails this hierarchical test. What is more noteworthy is that the standard deviations are very different between groups, especially CAT's 1.42 which is more than twice that of FIT's 0.63; the paper only tests the mean and does not account for differences in dispersion, extreme ML estimates, or conditional measurement accuracy.

### 9.2 SOS self-reported efforts

|Conditions|SOS-Effort mean| SD | \(N\) |
|---|---:|---:|---:|
| FIT | 17.28 | 3.56 | 175 |
| CAT | 17.32 | 3.88 | 178 |
| S-AT | 16.71 | 4.01 | 128 |
| EISS S-AT | 16.96 | 3.74 | 169 |

Test type effect:

\[
F(3,16.88)=0.21,
\qquad
p=.885.
\]

There were only 650 SOS copies, 46 fewer than the ability and RTE analyses, and the paper did not explain why the missing questions were missing, nor did it examine whether missing questionnaires were related to test type or effort.

### 9.3 response time effort

|Conditions|RTE mean| SD |Total in the table \(N\)|
|---|---:|---:|---:|
| FIT | .96 | .05 | 190 |
| CAT | .96 | .06 | 185 |
| S-AT | .95 | .07 | 138 |
| EISS S-AT | .95 | .08 | 183 |

Test type effect:

\[
F(3,14.62)=0.92,
\qquad
p=.454.
\]

The overall RTE was approximately .96, meaning approximately 4% of responses were judged as quick guesses. On the one hand, this result shows that most participants have put in considerable efforts even if there are no performance consequences; on the other hand, RTE is close to the upper limit, and there may be a ceiling effect, making small differences between test forms more difficult to detect.

## 10. “Low risk” does not mean that participants will lie or make no effort at all

This topic begins with an important premise: in mental health or low-stakes measurements, examinees may be willing to provide honest self-information. This article cannot directly test whether the self-evaluation is accurate, but it provides a counterexample to "low risk necessarily requires low effort":

\[
\overline{RTE}=.96.
\]

That is, most items do not behave as fast guesses.

However, it still cannot be deduced from this:

- Everyone is always serious;
- Self-reported difficulty must be accurate;
- Mental health self-assessment has the same motivation as college mathematics answers;
- No quick guessing means no other form of low-quality answering.

A more appropriate conclusion is: **Effort in a low-risk environment is heterogeneous. It cannot be assumed a priori that all employees will not work hard, nor can it be assumed that all employees are highly invested. **

## 11. Possible mechanisms for no effect

The authors propose an offset explanation:

\[
\text{Choice increases participation}
\quad+
\text{Repeated choices increase burden and time}
\quad\Rightarrow\quad
\text{The net effect is close to 0}.
\]

Each S-AT question requires making a difficulty decision before answering the item. If the test is therefore longer, the latter part of the effort may be reduced.

But this is just an explanation in the discussion, because the paper:

- The total answering time for the four groups was not reported;
- No direct measurement of engagement;
- No analysis of question-by-question RTE versus question order curves;
- No separation of additional selection time from problem solving time.

So it can’t be written as “Research proves that the benefits of engagement are offset by the cognitive load.” It is simply a mechanistic assumption that is compatible with zero net effect.

## 12. The unexpected invigilator effect

### 12.1 Ability Performance

The average overall ability corresponding to the four invigilators is:

|invigilator|ability mean|
|---|---:|
| A | 0.24 |
| B | 0.15 |
| C | 0.43 |
| D | 0.07 |

Thesis report invigilator main effect:

\[
F=4.80,
\qquad
p=.011,
\]

and proctor multiplied by gender interaction:

\[
F=3.75,
\qquad
p=.011.
\]

Simple effects show that the difference in proctors is significant in the male group but not significant in the female group.

### 12.2 RTE

The overall mean RTE for proctors A to D is approximately:

\[
.97, .96, .95, .94.
\]

The paper reports the invigilator effect \(F=3.739,p=.032\), and the session nested in invigilator effect \(F=1.947,p=.031\). Since the RTE was severely skewed, the author conducted a Kruskal-Wallis test and still obtained significant invigilator differences.

### 12.3 It cannot be directly explained as the causal effect of the invigilator

The composition of invigilators, sessions, and participants was not completely random and orthogonal, and there were only four female graduate students invigilating the exams. Even if conditions are counterbalanced, the observed differences may still be mixed:

- conduct of invigilators;
- Show time and atmosphere;
- Differences in participants caused by self-registration;
- Random fluctuations in a small number of sessions.

Therefore, the invigilator effect is a situational signal that needs to be taken into account, rather than a causal identification of certain types of invigilator characteristics.

## 13. Internal problems in the original table and text

### 13.1 The RTE sample sizes in Table 4 cannot be added up.

The male and female sample sizes of EISS S-AT are 34 and 128 respectively according to Table 4, but the total number in this column is written as 183:

\[
34+128=162\ne183.
\]

The sum of the sample sizes of the four groups of girls is also:

\[
136+140+108+128=512\ne533.
\]

If 128 was originally supposed to be 149, the two places will be consistent; however, there are no errata in the original text, and this page will not replace it without authorization. It will only retain the total number in the table and mark the contradiction.

### 13.2 The interactive degrees of freedom of SOS are inconsistent with effective samples

The gender effect for the SOS analysis is written as \(F(1,631)\), but the test type by gender interaction is written as \(F(3,677)\). The latter denominator degrees of freedom are incompatible with SOS's \(N=650\) and more closely follow the numbers from other analyses.

### 13.3 SS, df and MS in Table 6 are inconsistent

The invigilator's line prints as:

\[
SS=22.88,
\quad
df=3,
\quad
MS=5.09.
\]

But:

\[
22.88/3=7.63,
\]

Not 5.09. At least one value or label is incorrect.

### 13.4 \(\eta^2\) cannot be read according to the ordinary variance interpretation rate

Tables 6 and 8 report the proctor's \(\eta^2\) as .407 and .406, respectively, and call this a large effect. But according to the ordinary total sum of squares ratio:

\[
22.88/687.19\approx.033,
\]

Instead of .407. The paper does not give a formula for calculating the effect size under hierarchical design, so it is not appropriate to write "the invigilator explained about 41% of the total variance." The safest approach is to report \(F\) and \(p\), and explain that the original table effect size is unclear and inconsistent with the ordinary \(\eta^2\).

### 13.5 Reference year is wrong

The text correctly lists Rocklin and O'Donnell's SAT paper as 1987, but the reference list lists it as 1995; volume number 79 and pages 315–319 correspond to the 1987 paper.

These internal issues do not overturn non-significant results for the three main test types, but they reduce confidence in additional proctor analysis and accurate form reuse.

## 14. Why “CAT is not significantly different from FIT” does not equal IRT invariance Proven

In the Discussion, the authors interpret the lack of significant differences between CAT and FIT as the principle of IRT invariance being maintained in the data. This is a strong statement.

Non-significant differences only indicate:

\[
\text{The current design does not reject the same means}.
\]

It is not equal to:

\[
\text{Both tests are equivalent within prespecified tolerances}.
\]

Formal equivalence requires equivalence testing or non-inferiority margins and should be compared simultaneously:

- condition bias;
- condition RMSE;
-Measurement standard error;
- Performance at extreme abilities;
- Score distribution and coverage rate.

The ability SDs of CAT and FIT in this study were 1.42 and 0.63, respectively, which already illustrates that mere comparison of means is not sufficient to establish measurement equivalence.

## 15. Direct inspiration for the experimental design of this topic

### 15.1 Don’t assume that “user choice” automatically increases motivation

At least you need to set:

\[
\text{Standard CAT}
\quad\text{vs.}\quad
\text{Only one self-evaluation}
\quad\text{vs.}\quad
\text{before}k\text{Question selection}
\quad\text{vs.}\quad
\text{Full choice}.
\]

Wise et al.'s results suggest that repeated choices throughout the process may simultaneously create a sense of control and decision-making burden. By only asking users to provide information once at the beginning, it is possible to retain personalized signals and reduce burden.

### 15.2 Efforts must use at least two types of indicators

It is recommended to also record:

- Self-reported efforts afterwards;
- Work hard on the response time of each question;
- Select response time;
- Decreased effort in question order position;
- Response quality indicators such as long lists of the same options and extremely short responses.

The RTE threshold is best calibrated by item or question type, rather than sharing 10 seconds for all questions.

### 15.3 Experimental treatments should be randomized at the individual level

If allocation must be based on sessions, it should be:

- Use field counts and intraclass correlations in power analysis;
- Use mixed models to explicitly add session random effects;
- Balancing proctors, time slots and equipment;
- Define proctor analysis up front instead of just exploring after the fact.

### 15.4 Question volume income and motivation income are two independent paths

Our main goal is to achieve the same accuracy with fewer questions, which can happen with constant effort. In turn, options may enhance subjective experience without shortening the test. Therefore, it is recommended to split the ending:

|Dimensions|Main indicators|
|---|---|
|Measurement efficiency|Average number of questions, number of tail questions, and proportion of reaching stopping rule|
|Accuracy|bias, RMSE, coverage rate, error early stopping|
|item bank security|Overall and conditional exposure, test overlap|
|Answering process|RTE, selection time, question sequence effort curve|
|subjective experience|Anxiety, sense of control, burden, preference|

### 15.5 Accurate self-assessment does not mean high effort in answering.

This article measures the effort in answering math questions and does not verify the consistency between the self-assessment of difficulty and the real \(\theta\). Our research needs to include:

\[
\text{self-assessment quality}
\quad\text{and}\quad
\text{Efforts to answer formally}
\]

Measure separately. A person may be serious but inaccurate in self-assessment, or he may be accurate in self-assessment but put less effort in subsequent long tests.

## 16. Chinese paraphrases that can be quoted safely

### About the main zero result

> Wise et al. (2005) compared FIT, CAT, S-AT and integral game-style S-AT on a fixed 40-item low-stakes mathematics test and did not detect a significant effect of test type on average ability, self-reported effort, or response time effort.

### About low-risk efforts

> The overall RTE of the four groups is about .96, indicating that most answers are not judged as quick guesses by the 10-second rule; low-risk conditions do not mean that all examinees have low effort, but this indicator also has threshold simplification and ceiling effects.

### About the right to choose

> Selecting item-by-item difficulty showed no net motivational benefit; the authors speculated that potential engagement may be offset by the time and effort costs of repeated selection, but the study did not directly measure engagement or total group time.

### About the invigilator

> The study later found that there are invigilator differences in ability performance and RTE, suggesting that low-stakes tests are sensitive to situational factors; since the invigilator and the session are not completely independent and random, this result should be regarded as exploratory evidence.

### About evidence boundaries

> The non-significant test type effect cannot prove that the four forms are equivalent; the processing is allocated according to the number of sessions, the number of valid sessions is small, and the original table has several degrees of freedom, sample size and effect size labeling issues.

## 17. How to divide the work of key references

|Literature|role in this article|
|---|---|
| Eccles（1983）；Wigfield and Eccles（2000） |expectancy-value motivation framework|
| Snow（1989, 1992, 1994） |performance and commitment dual paths|
| Pintrich and Schunk（2002） |Theoretical Background of Moderate Challenges and Intrinsic Motivation|
| Rocklin and O'Donnell（1987） |Proposal of S-AT|
| Pitkin and Vispoel（2001） |Early meta-analysis background of S-AT and CAT results|
| Wise and DeMars（2005） |A review of low-risk motivation and performance issues|
| Sundre and Moore（2002） |SOS self-reporting machine scale|
| Wise and Kong（2005） |Theoretical and measurement basis of RTE indicator|
| Wise（1999a, 1999b） |The relationship between hierarchical integral and ML ability estimate|

## 18. Summary

The most valuable aspect of this paper to this topic is not proving that S-AT works, but rather discouraging an overly optimistic hypothesis:

\[
\boxed{
\text{low risk}
+
\text{option}
\not\Rightarrow
\text{higher effort or higher performance}
}
\]

In this experiment, ordinary S-AT, integral game S-AT and CAT did not outperform the fixed-item test. Most students still showed high RTE, but the different quiz interfaces did not improve it further.

This instead supports our lightweight approach: if the main value of self-assessment information is to improve cold starts, there is no need to assume that the entire self-selected items can also bring additional motivational benefits. A more reasonable design is to reduce the interaction burden, independently verify the incremental value of the self-evaluation signal to the starting point, priority, question volume, and exposure, and treat effort and subjective experience as independent outcomes rather than as an automatically established mechanism.
