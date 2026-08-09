# Frosini et al. (1998): Launching automated exams with self-adaptive pretests

!!! abstract "Key takeaway"
    **What was done:** Frosini et al. designed a two-stage automatic examination: the examinee first repeatedly selects the difficulty level in the self-adaptive pre-examination and obtains feedback. The system determines the starting level of the formal examination based on this, and then increases, decreases, or maintains the difficulty level based on the performance of the last two questions. **What we learned:** The system completed over 300 administrations and compared manual versus automated exams on 100 students, demonstrating that this architecture can work. **Conclusion for this topic:** It is an early precedent of "self-selected difficulty startup + rule-based adaptation", but there is no IRT latent variable prior, informative topic selection or accuracy stop, and there is no proof that this kind of start can shorten the test or improve the estimation accuracy.

## Citation details

> Frosini, G., Lazzerini, B., & Marcelloni, F. (1998). Performing automatic exams. *Computers & Education, 31*(3), 281–300. [DOI](https://doi.org/10.1016/S0360-1315(98)00042-6)

- Research type: Examination system design paper, with item rating, running examples and preliminary validity comparison
- Application scenario: Oral and practical examinations in technical or scientific courses at Italian universities
- Implementation object: Six-question automatic examination of Pascal programming course
- Start method: Examinee first completes a self-adaptive pre-test, chooses the difficulty of each question and gets correctness feedback
- Formal stage: Increase, decrease or maintain the difficulty according to the rules based on the scores of the last two questions.
- Core evidence: The system has completed more than 300 exams; another 100 students have taken manual and automated exams respectively

!!! danger "Don't be misled by the author's use of the word CAT"
    The author calls the formal stage Computerized Adaptive Testing (CAT), but the "adaptive" here means changing the difficulty level according to the scores of the first two questions. The system does not have a \(\theta\) estimate, item information function, Bayesian posterior, or maximum likelihood scoring. Therefore, it is more accurately called **self-adaptive pre-test plus rule-based automatic test** and cannot be directly regarded as an effect study of modern IRT-CAT.

## 1. What problem is the author trying to solve?

The starting point for the essay is not a large standardized test, but a short oral or practical examination common in Italian universities. Such exams typically ask only four to six questions, with teachers choosing the first question based on their knowledge of the student and adjusting subsequent difficulty based on on-site performance.

If the computer starts with the same medium question for everyone, there's a special problem with short tests: the test is over before the system can get to the right level of difficulty for the student. The scoring in this article makes difficult questions worth higher than easy questions, so a starting point that is too low not only reduces efficiency, but may also limit the maximum score that high-level students can achieve.

The author therefore combines two ideas:

1. Use Self-Adapted Testing (SAT) pre-test to allow students to choose item difficulty;
2. Use a CAT-style formal stage to allow the system to adjust subsequent difficulty levels based on answering performance.

The common structure between this and this topic is:

\[
\text{Startup information provided by examinee}
\longrightarrow
\text{Determine the starting point for the formal test}
\longrightarrow
\text{The system takes over subsequent topic selection}.
\]

The difference is that the "starting information" in this article is not a self-report, nor is it a question choice, but a pre-test that includes **choices, answers and feedback**.

## 2. What parts does the entire system consist of?

The system is divided into three layers:

- The database saves items, answers and exam results;
- The calculation engine is responsible for item grading, formal examinations and post-event item analysis;
- The user interface serves teachers and students respectively.

Item includes four categories:

1. Unstructured multiple choice questions;
2. Unstructured multiple choice questions;
3. Structured questions composed of multiple sub-questions;
4. Application questions requiring writing, compiling and running programs.

The paper discusses the automatic scoring of program answers at considerable length, including correctness, coding style, efficiency, cyclomatic complexity and programming proficiency. These illustrate that the system is oriented towards automated course examinations, but are not the statistical contribution of this paper that is most relevant to the CAT cold start problem.

## 3. The first stage: How to determine the starting point for SAT-style pre-test

### 3.1 The process of each pre-examination question

The number of questions in the pre-test is fixed in advance by the teacher. Each round:

1. Students choose a difficulty level;
2. The system randomly selects a question at this level;
3. Students answer;
4. The system feedbacks whether the answer is correct or incorrect;
5. Students then choose the difficulty level of the next question.

If the difficulty level is:

\[
D_t\in\{1,\ldots,K\},
\]

The answer result is:

\[
U_t\in\{0,1\},
\]

Then what is observed in the pre-test is not a single self-evaluation, but a piece of process data:

\[
\mathcal H_m
=
\{(D_1,U_1),\ldots,(D_m,U_m)\}.
\]

### 3.2 Rules for determining starting difficulty

If at least one question is answered correctly in the pre-test, the starting point for the official test will be the highest difficulty among all correctly answered items:

\[
L_0
=
\max\{D_t:U_t=1\}.
\]

If all answers are wrong, the lowest difficulty level chosen by the student will be lowered by one level, but not lower than the lowest level:

\[
L_0
=
\max\left\{1,\min_t(D_t)-1\right\}.
\]

Therefore, the system does not simply believe in "which level am I suitable for?" It requires that the chosen difficulty level be supported by actual correct answers; once there is evidence of success, the highest level of success is used.

!!! important "This is not individualized prior"
    This rule only outputs the discrete starting point \(L_0\) and does not form

    \[
    p_0(\theta\mid\mathcal H_m).
    \]

    It neither expresses uncertainty within the same level nor allows self-assessment evidence to decay with formal responses. Two students who get the same \(L_0\) will be considered identical, even if one barely gets one question right and the other gets it right on multiple high difficulty levels.

### 3.3 Why does it do one more thing than "students choose the first question directly"

If we only record the first choice \(D_1\), we can only know where the student is willing to start. This article also observed:

- Whether the selected difficulty questions can be answered correctly;
-Whether to change the choice after receiving feedback;
- Where is the highest difficulty level for success.

Therefore, the starting point is mixed simultaneously:

\[
\text{self-evaluation}
+
\text{short test performance}
+
\text{Strategy adjustments after feedback}.
\]

It is more likely to obtain a reliable starting point, but also means that any efficiency gains cannot be attributed to "self-assessment per se". Pre-test questions are also part of the test burden and must be included when comparing the total number of questions.

## 4. The second stage: How to adapt to the formal examination

### 4.1 Fixed six formal questions

The teacher pre-specifies the number of main question rounds for the official exam \(Q\). The actual system takes:

\[
Q=6.
\]

In each round, the system first draws a main question from the current difficulty level and current subject. If the student chooses "I don't know", the system can give alternate questions of the same subject and the same difficulty; the alternate questions can only get up to half of the full score for that level. If the student expresses he does not know for the second time, he will remember it incorrectly. Therefore, \(Q=6\) refers to the six main question rounds, and the actual number of items seen may exceed six due to backup questions.

### 4.2 Original rules for upgrade, downgrade and retention

Record the score and full score of the previous question:

\[
m_{t-1},\quad s_{t-1},
\]

The current question score and full score are:

\[
m_t,\quad s_t.
\]

The next question will keep the current level by default. Only the following two types of combinations will be upgraded by one level:

\[
\left(m_{t-1}=s_{t-1}\ \text{and}\ m_t\ge\frac{s_t}{2}\right)
\]

or

\[
\left(m_{t-1}\ge\frac{s_{t-1}}{2}\ \text{and}\ m_t=s_t\right).
\]

In other words, you need at least a full score on one of the two questions and at least half a score on the other to move up.

The following two types of combinations will be downgraded by one level:

\[
\left(m_{t-1}=0\ \text{and}\ m_t<\frac{s_t}{2}\right)
\]

or

\[
\left(m_{t-1}<\frac{s_{t-1}}{2}\ \text{and}\ m_t=0\right).
\]

That is, if at least one of the two questions has a zero point, and the other question has less than half a point, it will be moved downwards. In other cases, the original level is maintained and is always limited to \(1\) to \(K\).

!!! note "Why does it use two questions instead of one"
    A single question may be correct or incorrect by accident. The author uses the joint performance of two adjacent questions to reduce the chance of an accidental answer immediately changing the difficulty. However, this is only an artificial rule; the paper does not compare it with "one question rises or falls," Bayesian updating, or optimal decision rules.

### 4.3 Early termination is not precision stopping

After each question, the system assumes that all remaining items are answered correctly, and calculates the theoretical maximum score \(v\) that can be obtained according to the highest upgradeable path. If:

\[
v<\frac{3}{5}V,
\]

Among them, \(V\) is a full score, and the exam will end immediately. The full score for the Italian exam is 30, so the passing line is:

\[
\frac{3}{5}\times30=18.
\]

This stopping rule asks "whether it is impossible to pass", not:

\[
SE(\widehat\theta)\le\varepsilon.
\]

Therefore, early closure in the paper cannot be taken as evidence of the required number of questions in CAT to achieve the same measurement accuracy.

## 5. Higher puzzle scores: Scoring and routing are bound to each other

The full score for the most difficult single question is the total full score divided by the number of official questions:

\[
\text{max\_sc}=\frac{V}{Q}.
\]

The single question score of level \(j\) is set by the system as:

\[
sc_j
=
\text{max\_sc}\frac{j}{K}.
\]

In the actual \(V=30,Q=6,K=3\) setting, the full marks for each question at the three levels are:

\[
\frac{5}{3},\quad\frac{10}{3},\quad5.
\]

This is different from IRT's "different items all serve the same ability scale". In this article, item difficulty not only changes the probability of answering, but also directly changes how many points can be obtained. Therefore, a wrong starting point may lower the total score, and a wrong starting point may cause continuous points loss.

!!! warning "Cannot apply IRT's item immutability"
    If two people enter different difficulty paths due to pre-test results, the final total score they receive may not only reflect the same latent ability; it is also affected by the path and difficulty weighting rules. The paper has no equating, linking, or proof of conditional unbiasedness.

## 6. How to automatically calibrate the item difficulty level

### 6.1 The teacher first provides sample questions

The teacher first labels some sample questions as level \(1,\ldots,K\) based on experience. For each level, administer the sample questions to the same sample of students and record the percentage of correct answers:

\[
X_j=\text{No.}j\text{The percentage of correct answers for layer items}.
\]

The author assumes:

\[
X_j\sim N(\mu_j,\sigma_j^2).
\]

As new sample questions are added, the system continuously updates the sample mean and variance until the variance of these estimators themselves is small enough.

### 6.2 Use normal density intersection points to divide levels

The intersection of two normal densities at adjacent levels constitutes the correct answer rate boundary. For a new question, first let the sample students answer, get the correct answer rate \(\widehat x\), and then select the level with the highest density:

\[
\widehat j
=
\arg\max_{j\in\{1,\ldots,K\}}
f_j(\widehat x).
\]

This is equivalent to doing Gaussian classification based on the group's correct answer rate. For example, the paper assumes that the correct answer rate for a certain question is 80%. Among the three levels of density, the first level has the highest density, so it is classified as the easiest level 1.

### 6.3 Why is it not IRT calibration?

This method only uses the total correct answer rate of a question in the sample, without estimation:

- Continuous positions of item difficulty \(b_i\);
- item discrimination \(a_i\);
- guessing parameter;
- Differences in student abilities;
- Parameter estimation error.

The same total correct answer rate can come from different discrimination levels and composition of the answering group. Treating percentages as a normal variable may also be inappropriate in small samples or close to 0, 1, since the number of correct answers is inherently closer to a binomial distribution.

## 7. How to implement the actual system

### 7.1 How to extract calibration samples

The authors stratified students by their average scores on previous exams: they divided the possible score range into six bands and selected one student from each band for each sample group. Each sample group therefore consisted of six students. This was done in an attempt to avoid a sample consisting solely of high- or low-scoring students.

The author sets the variance threshold of the sample mean sequence to .002 and the variance threshold of the sample variance sequence to .0002; and only checks whether the threshold is reached after completing at least four sample questions. However, the paper does not explain whether the different sample groups are composed of the same group of students, the sensitivity of the normal approximation in a small sample of six people, and whether each new question is always administered to the exact same six people.

### 7.2 Experience distribution of three difficulty levels

Implementation uses:

\[
K=3.
\]

The number of sample questions required to estimate the mean and variance are 8, 6 and 6 respectively. The mean and variance of the correct answer rates at the three levels are:

|difficulty level|average correct answer rate|variance|
|---:|---:|---:|
| 1 | .85 | .017 |
| 2 | .51 | .012 |
| 3 | .23 | .012 |

The obtained correct answer rate is divided into:

\[
B_0=0\%,\quad
B_1=37\%,\quad
B_2=67\%,\quad
B_3=100\%.
\]

Therefore:

- 67%–100% correct answers are classified as level 1;
- 37%–67% classified as level 2;
- 0%–37% classified as level 3.

### 7.3 System scale

The formal exam consists of six fixed questions, the system is used in several university courses, and more than 300 automated exams were completed before the paper was published. The authors did not provide average scores, item paths, starting tier distributions, completion times, early termination rates, or overall correlation with manual exams for these 300+ exams.

## 8. Item analysis: ease and selectivity

### 8.1 Ease of Index

For \(n_s\) students who have done a certain question, if the sum of the scores for the question is \(t\) and the full score for a single question is \(\mathrm{max}\), then:

\[
I_e
=
\frac{t}{n_s\,\mathrm{max}}.
\]

The author’s experience is explained as follows:

- \(.75\le I_e\le1\): easy;
- \(.25\le I_e<.75\): medium;
- \(I_e<.25\): Hard.

### 8.2 Best-worst group selectivity index

First, sort the students who have done the question according to the total score of the final exam, and take the highest group \(B\) and the lowest group \(W\) with equal numbers. Suppose there are \(s\) people in each of the two groups, and the item score sum is \(b,w\) respectively, then:

\[
I_{bw}
=
\frac{b-w}{s\,\mathrm{max}}.
\]

The author considers .4–1 as good, .2–.4 as acceptable, 0–.2 as insufficient, and negative values may indicate misplaced items, ambiguous expressions, or scoring problems.

### 8.3 Examples of single questions in the paper

A Level 3 structured question was administered 20 times to obtain:

\[
I_e
=
\frac{35}{20\times5}
=.35,
\]

and:

\[
I_{bw}
=
\frac{25-10}{10\times5}
=.30.
\]

According to the author's threshold, this is a moderately difficult question with acceptable selectivity.

!!! warning "There is a loop definition here"
    The best group and the worst group are defined by the final total score of the same exam, and the score of the analyzed item enters the total score. Therefore \(I_{bw}\) is not an independent distinction relative to an external standard and may be inflated by part-whole overlap. It also does not replace the \(a_i\) parameter of the IRT.

## 9. What does the automatic scoring of program questions do?

Application question scoring sums up several characteristics according to teacher weights, including:

- Whether the program compiles and passes the test data;
- Coding style;
- Operational efficiency;
- McCabe Cyclomatic Complexity;
- Programming operation process.

Some features use fuzzy sets to map continuous indicators into partial scores. For example, the closer the running time is to the teacher's demonstration program, the higher the efficiency affiliation; if the program is too long or too short, the style score may be reduced. Program operation proficiency refers to the number of compilations and compilation intervals.

These rules demonstrate the engineering scope of the 1998 automated testing system, but their conceptual validity has not been systematically verified. For example, the number of compilations may simultaneously reflect exploration strategy, interface familiarity, or caution, and does not necessarily equal programming ability.

## 10. What evidence of effects does the paper actually report?

### 10.1 Comparison between manual examination and automatic examination

The author asked 100 students to take manual examinations and automatic examinations respectively, and reported:

- In 70% of cases, the difference between the two results is 1 point;
- In 90% of cases, the difference is less than 3 points;
- In 3% of cases, the difference is more than 3 points;
- Both grades are awarded out of 30 points.

If the first sentence is understood as "exactly 1 point difference", there are still situations where the difference between these categories is exactly 3 points; the original text does not provide a complete contingency table and cannot be completed by oneself.

### 10.2 What can this set of numbers support?

It would be prudent to say that for the majority of these 100 students, there were no large absolute differences between manual and automated test scores.

However, it cannot be claimed that the two exams are equivalent or that the automatic exam has obtained sufficient validity evidence, because the paper does not report:

- The order and interval between the two exams;
- Whether to use parallel content;
- Human rater agreement;
- Correlation, mean difference, standard deviation and confidence interval of two scores;
- Whether there is systematic overestimation or underestimation;
- Differences stratified by ability level;
- Test-retest or equivalence limits.

In their conclusion, the authors called the reliability and validity "very satisfactory," with strength exceeding what can be safely supported by the reported statistics.

## 11. Separate author’s interpretation from original data

Citing early SAT research, the paper suggests that allowing students to choose difficulty may reduce anxiety, increase feelings of control and confidence, and avoid frustration. But this article did not measure it:

- Anxiety before or after the test;
- Sense of autonomy;
- Self-efficacy;
- Test motivation;
- Differences between SAT prep and no prep conditions.

Therefore, these are architectural motivations and previous research explanations, not the results of this study.

Similarly, the system's random selection of questions within a layer may distract the use of certain items, but the author did not report item exposure rate, conditional exposure rate, or test overlap between examinees, and cannot claim that the pre-examination has improved item bank security.

## 12. Boundary of evidence: This article proves nothing

This article cannot be used to prove:

1. Self-selection can shorten the number of CAT questions required to achieve the same accuracy;
2. The level students choose is an unbiased ability estimate;
3. The multi-question pre-test is better than direct self-report, personalized first question or standard mid-level starting point;
4. Regular lifting is better than maximum information amount or Bayesian topic selection;
5. Automatic examinations and manual examinations are statistically equivalent;
6. Allowing choice will reduce anxiety or increase motivation;
7. The difficulty-weighted total score satisfies the item invariance of IRT;
8. Random topic selection within a layer can effectively control overall or conditional exposure.

The most critical lack is that the author did not set a control condition that starts from a common starting point and has exactly the same rules. Therefore, the independent contribution of self-adapted pretests to question volume, grades, pathways, or experiences cannot be identified.

## 13. Exact comparison with the methods of this topic

|design dimensions|Frosini et al. (1998)|The method to be studied in this topic|
|---|---|---|
|user signal|Multiple self-selected difficulty levels plus pre-test corrections|A self-assessment, first question selection or first \(k\) question selection|
|Signal output|discrete starting level|Initial point or individualized prior with variance|
|formal ability estimate|difficulty weighted total score|EAP, MAP or ML for IRT|
|Follow-up topic selection|Score-driven improvement rules for the last two questions|Information volume, posterior variance or stratification rules|
|stopping rule|Fixed six questions; if it is impossible to pass, it will end early|Reach a common accuracy threshold and set a minimum/maximum number of questions|
|item bank use|Randomly selected questions within the layer, no exposure reported|Explicit reporting of overall and conditional exposure and test overlap|
|main evidence|System examples and rough manual-automatic differences|bias, RMSE, coverage rate, question volume, exposure and robustness|

The closest thing in structure is:

\[
\text{Let people participate in the startup first}
\quad\Longrightarrow\quad
\text{Algorithms take over}.
\]

The core difference in methods is: this article uses **hard hierarchical routing**, and we consider using **probabilistic information with uncertainty**. The former does not express how reliable the judgment is once a person is sent to a certain level; the latter can use prior variance to control how strong the impact of self-evaluation is, and let opposite formal responses gradually correct it.

## 14. How this article changes our experimental design

### 14.1 Incorporate the pre-test cost into the total number of questions

If the first \(k\) questions are chosen by the student, and then CAT takes fewer \(r\) questions, the net benefit should be calculated as:

\[
\Delta L
=
L_{\mathrm{standard}}
-
\left(k+L_{\text{CAT after self-selection}}\right).
\]

Simply reporting how many questions are missing from the official CAT hides startup costs.

### 14.2 Separate "selection signal" and "actual answer signal"

Frosini's starting point uses both \(D_t\) and \(U_t\). To know whether user self-reviews really have incremental value, you should at least compare:

1. Common standard prior;
2. Only use the first \(k\) questions to actually answer;
3. Only user selection;
4. Use choices and answers at the same time;
5. Select and answer before entering the complete individualized prior.

In this way, we can ask: How much additional information does the difficulty selection provide after we have already seen the previous \(k\) questions correctly?

### 14.3 Comparing hard routing and probabilistic routing

The rules in this article can be used as a historical baseline:

\[
\mathcal H_k\longrightarrow L_0.
\]

Our probabilistic version is:

\[
\mathcal H_k
\longrightarrow
p_0(\theta\mid\mathcal H_k)
=
N(\mu_i,\tau_i^2).
\]

The error of \(\mu\) should be manipulated simultaneously with \(\tau^2\) to examine whether hard routing produces unrecoverable path loss due to erroneous self-evaluation, and whether a wide prior can improve robustness.

### 14.4 Add item exposure ablation

Random sampling within a layer can be the simplest way to spread exposure, but should be compared to a clear baseline:

- Maximum amount of information without exposure control;
- Sympson–Hetter accepts probabilistic control;
- \(a\)-stratified early low \(a\) topic selection;
- User signal determines random or probability questions in \(b\) area, layer;
- User signal plus standard exposure control.

Report at least:

\[
P(A_i),
\qquad
P(A_i\mid\theta\text{Group}),
\qquad
P(A_i\mid\text{self-rating group}),
\]

And the item ratio is not used in test overlap and item bank.

## 15. Quote-safe Chinese paraphrasing

### Used to illustrate historical architectural precedents

> Frosini et al. (1998) proposed a two-stage automatic examination: the examinee first selects the difficulty of each question in the pre-examination and obtains correctness feedback. The system determines the starting point of the formal examination with the highest successful difficulty, and then adjusts the item level according to recent scoring rules.

### is used to indicate that it is not a modern IRT-CAT

> Although the authors refer to the formal stage as CAT, the system uses discrete difficulty levels, a difficulty-weighted total score, and two-adjacent question-driven ascending and descending rules, and does not use IRT ability estimate, informative question selection, or accuracy stopping.

### Used to describe the boundaries of existing evidence

> The paper reports more than 300 system runs and roughly compares manual and automated test scores among 100 students. However, there is no common starting point comparison, question accuracy comparison, or item exposure statistics, so it cannot be judged based on whether self-adaptive pretests can improve the efficiency of modern CAT.

### Used to illustrate the incremental issues of this topic

> This early work proves that the architecture of "user participation in startup and algorithm subsequent takeover" is not new; what remains to be tested is whether short-term self-assessment can be modeled as an IRT prior with uncertainty and simultaneously improve question volume, estimation robustness and item bank usage under unified stopping accuracy.

## 16. Key References

- Frosini, G., Lazzerini, B., & Marcelloni, F. (1998). Performing automatic exams. *Computers & Education, 31*(3), 281–300. [https://doi.org/10.1016/S0360-1315(98)00042-6](https://doi.org/10.1016/S0360-1315(98)00042-6)
- Rocklin, T. R., & O'Donnell, A. M. (1987). Self-adapted testing: A performance-improving variant of computerized adaptive testing. *Journal of Educational Psychology, 79*(3), 315–319.
- Vispoel, W. P., Rocklin, T. R., & Wang, T. (1994). Individual differences and test administration procedures: A comparison of fixed-item, computerized-adaptive, and self-adapted testing. *Applied Measurement in Education, 7*(1), 53–79.

## 17. Judgment after reading

The value of Frosini et al. (1998) to this topic is primarily to identify historical boundaries. It has placed the difficulty selection of Examinee before the formal adaptive exam, and constrained this choice with actual answers, so the "self-selected first, automatic later" architecture cannot be our first initiative.

But it does not solve the really difficult parts of modern CAT: how to calibrate self-evaluation to mean and variance, how to allow error signals to be corrected a posteriori, how to check the net question volume under the same accuracy stopping rule, and how to protect the item bank at the same time. Our potential contribution should be on these estimable, ablation, and verifiable mechanisms, rather than just putting users into the first question selection process.
