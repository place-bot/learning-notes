# Sympson–Hetter (1985): CAT itemexposure control method

!!! abstract "Key takeaway"
    **What was done:** The Sympson–Hetter method first lets CAT recommend the optimal questions according to the original rules, then determines whether to actually administer the test based on the item-specific acceptance probability, and uses offline Monte Carlo simulation to calibrate these probabilities. **What is gained:** It can limit the marginal exposure of popular questions in the overall examinee, but rejecting the best questions will cause loss of information, and the overall exposure security does not mean the internal security of a certain ability group. **Conclusion on this topic:** This method solves the problem of item bank confidentiality and overall exposure, not measurement accuracy; if the study population is low-risk psychometrics, the exposure can be reduced to a descriptive indicator, but it cannot automatically interpret "the first questions are more scattered" as CAT is more effective.

## Method identity

> Sympson, J. B., & Hetter, R. D. (1985, October). *Controlling item-exposure rates in computerized adaptive testing*. In *Proceedings of the 27th Annual Meeting of the Military Testing Association* (pp. 973–977). San Diego, CA: Navy Personnel Research and Development Center.

- Method type: probabilistic maximum exposure control of Computerized Adaptive Testing (CAT)
- Control object: The proportion of each question that is actually tested in the overall examinee
- Core tools: item-specific acceptance probability and offline Monte Carlo simulation
- Clear open full text description: [Stocking (1993), *Controlling Item Exposure Rates in a Realistic Adaptive Testing Paradigm*](https://files.eric.ed.gov/fulltext/ED384663.pdf)

## 1. Why does CAT need exposure control?

If CAT selects the question with the most information at each step:

\[
j_t
=
\arg\max_{j\in\mathcal R_t}
I_j(\widehat\theta_{t-1}),
\]

Examinees with similar abilities and similar answer paths will encounter the same items repeatedly. The first question is particularly dangerous: if everyone's initial ability is set to \(0\), a large number of examinees will start from the same batch of medium-difficulty, high-discrimination questions.

The item exposure rate can be written as:

\[
\widehat P_i(A)
=
\frac{\text{item}i\text{Number of people actually tested}}
{\text{examinee total number of people}}.
\]

\(A_i\) here means item \(i\) was administered, that is, item \(i\) was actually presented to the examinee. Excessive exposure will bring:

1. The risk of the item being memorized, disseminated or leaked;
2. A small number of high-quality questions are consumed quickly, and item bank maintenance costs increase;
3. Different examinees obtain highly overlapping tests;
4. A large number of items that have been developed and calibrated are almost never used.

The Sympson–Hetter method mainly solves the first type of problem: **limiting the maximum overall exposure of any single question. **

## 2. The most critical distinction: being selected does not mean being tested.

This method distinguishes between two events:

- \(S_i\): item \(i\) is selected by the CAT topic selection algorithm;
- \(A_i\): item \(i\) was finally tested.

An item can only be tested if it is selected first, therefore:

\[
A_i\subseteq S_i.
\]

The actual exposure rate of item \(i\) can be broken down into:

\[
P_i(A)
=
P_i(A\mid S)P_i(S).
\]

Order

\[
K_i=P_i(A\mid S),
\]

Among them, \(K_i\in[0,1]\) is the **exposure control parameter** of item \(i\), that is, the exposure control parameter. So:

\[
P_i(A)=K_iP_i(S).
\]

These three probabilities are answered respectively:

|symbol|meaning|What determines|
|---|---|---|
| \(P_i(S)\) |The probability of item being selected by the question algorithm|item bank, ability distribution, initial value, topic selection rules, content constraints and stopping rule|
| \(K_i=P_i(A\mid S)\) |The probability of being allowed to take the test after being selected|Item parameters obtained by Sympson–Hetter calibration|
| \(P_i(A)\) |final actual exposure|The first two decide together|

!!! note "It does not control the probability of topic selection"
    Popular questions may still be frequently selected by the maximum information content rule. The Sympson–Hetter method does not change why it becomes the optimal question, but adds an acceptance or rejection level after it is selected.

## 3. How to run the actual test

Assume that the current CAT selects item \(i\) based on ability estimate, content constraints and other conditions:

1. Generate random number \(U\sim\operatorname{Uniform}(0,1)\) from uniform distribution;
2. If \(U\le K_i\), actually test item \(i\);
3. If \(U>K_i\), do not display item \(i\) to the examinee, and temporarily remove it from the items available to the examinee this time;
4. Select the next best question from the remaining items and make another acceptance or rejection judgment;
5. Until you find a question that you can actually take the test.

> CAT selects the current best question \(i\) → extracts \(U\sim\operatorname{Uniform}(0,1)\) → if \(U\le K_i\), perform the test; otherwise, skip item \(i\) this time and move to the next best question.

Rejected questions will not be displayed to the examinee and will not be recorded as an answer question. The algorithm simply falls back and selects candidates with less information or less suitable constraints.

!!! note "How to ensure that there will be questions available at the end"
    For a test with a fixed length of \(n\), the classic implementation will ensure that there are at least \(n\) questions in the item bank and \(K_i=1\); otherwise, in extreme cases, all remaining candidate questions may be continuously rejected and the test cannot be completed. CAT with content blocks should also retain enough \(K_i=1\) questions in each block where questions must be drawn. Modern implementations can also set explicit fallback question selection rules.

## 4. A specific numerical example

Assume that the target maximum exposure is:

\[
r_{\max}=0.20.
\]

The simulation found that if the level is not accepted or rejected, item \(i\) will be selected by the examinee of \(50\%\):

\[
P_i(S)=0.50.
\]

If its acceptance probability is set to:

\[
K_i
=
\frac{r_{\max}}{P_i(S)}
=
\frac{0.20}{0.50}
=
0.40,
\]

Then its expected actual exposure is:

\[
P_i(A)
=
K_iP_i(S)
=
0.40\times0.50
=
0.20.
\]

In other words, although this question often becomes the first choice of the algorithm, on average only \(40\%\) will be selected into the actual test.

If another question only has:

\[
P_j(S)=0.08<r_{\max},
\]

Then you can set \(K_j=1\). It can be tested every time it is selected because even if fully accepted, the expected exposure will not exceed \(0.20\).

## 5. Why can’t \(K_i\) be counted directly?

It looks like it can be used directly:

\[
K_i
=
\min\left(1,\frac{r_{\max}}{P_i(S)}\right).
\]

The problem is that \(P_i(S)\) is not a pre-fixed item property. It is affected by the entire CAT system:

- Parameters of other items in the item bank;
- examinee ability distribution;
- Initial ability estimate or prior;
- Topic selection criteria;
- Content balance and hostile problem constraints;
- fixed length or variable lengthstopping rule;
- \(K_j\) for other items.

When the popular question \(i\) is rejected, the next candidate question \(j\) will be selected more frequently; so \(P_j(S)\) rises, and its original \(K_j\) may no longer be enough. Rejection has a chain reaction, so all \(K_i\) must be jointly calibrated.

## 6. Offline Monte Carlo calibration

The classic implementation uses repeated simulation to obtain \(K_i\) for each question:

1. Fix the complete CAT design, including item bank, ability estimate, topic selection, content constraints, exposure target and stopping rule;
2. Generate a large number of simulated examinees from the predicted real capability distribution;
3. Initialize all items \(K_i^{(0)}=1\), that is, there will be no exposure limit in the first round;
4. Simulate the complete CAT and record the selection rate \(\widehat P_i(S)\) and actual exposure rate \(\widehat P_i(A)\) for each question;
5. Update exposure parameters:

\[
K_i^{\text{new}}
=
\begin{cases}
r_{\max}/\widehat P_i(S),&
\widehat P_i(S)>r_{\max},\\[4pt]
1,&
\widehat P_i(S)\le r_{\max};
\end{cases}
\]

6. Re-simulate with the new \(K_i\);
7. Repeat updates until the highest observed exposure stabilizes near the target value;
8. Use last round \(K_i\) for official CAT.

!!! warning "The target value is not a hard upper limit in each batch of data"
    \(r_{\max}\) controls expected exposure under model and simulated conditions. Random fluctuations of limited samples, inconsistencies between real ability distribution and simulated distribution, item parameter errors or changes in system rules may cause the observation exposure rate in formal testing to exceed the target.

Stocking's (1993) example starts with all \(K_i=1\) and takes many rounds of simulations before the maximum exposure stabilizes. This also shows that \(K_i\) is not a permanent attribute of the item, but a system parameter of "how many times this question should be accepted in the current entire CAT system."

## 7. Why does it lose information?

Without exposure control, the algorithm can test the optimal question \(i^*\):

\[
i^*
=
\arg\max_i I_i(\widehat\theta).
\]

If \(i^*\) is rejected by the exposure level, the system can only use the second-best question \(j\) instead, which usually includes:

\[
I_j(\widehat\theta)
<
I_{i^*}(\widehat\theta).
\]

Therefore, there is a direct trade-off between exposure control and single-question measurement efficiency:

\[
\text{Stronger item bank protection}
\quad\Longleftrightarrow\quad
\text{Reject the best question more times}
\quad\Longleftrightarrow\quad
\text{Lower cumulative information}.
\]

In a fixed length CAT, this may manifest as a larger standard error or root mean squared error; in a variable length CAT where accuracy is the stopping criterion, this may manifest as more questions being required to reach the same stopping threshold.

van der Linden (1999) paraphrased the result of Thomasson (1995) and said that the Sympson–Hetter method loses about \(15\%\) information in the middle area of the \(\theta\) distribution, and the more rigorous method can lose up to \(40\%\) in the entire \(\theta\) range. This set of numbers should be understood as the results under specific research conditions, not the fixed loss rate of the method in all item banks; and this is a second-hand reference by van der Linden to a conference paper, not the conclusion of the original text of Sympson and Hetter (1985).

## 8. Why people with intermediate abilities may lose more

If the real ability is most densely distributed near \(0\), the number of medium ability examinees is the largest. Medium-difficulty, high-information questions suitable for this group are most likely to be selected frequently and therefore tend to result in smaller \(K_i\).

There are fewer extreme ability examinee. Even if the questions suitable for both ends of the item bank are very popular for this group, the selection rate may not be high in the overall population. Therefore, its \(K_i\) is often close to \(1\).

The result may be:

|competence area|Number of people|Overall selection rate of the best question|Common \(K_i\)|information loss|
|---|---:|---:|---:|---:|
|middle|Much|high|smaller|more obvious|
|both ends|less|low|Close to \(1\)|smaller|

This explains why Stocking (1993) observed that conditional standard error increases more in the middle fractional region than in the tail under Sympson–Hetter control.

## 9. Biggest limitation: overall exposure security is not equal to internal security of the group

The classic Sympson–Hetter controls the overall marginal exposure:

\[
P_i(A).
\]

It does not automatically control conditional exposure on specific ability positions:

\[
P_i(A\mid\theta),
\]

It also does not automatically control the exposure within a specific self-assessment grade:

\[
P_i(A\mid C=c).
\]

For example, highly capable people account for only \(5\%\) of the population. A certain extremely difficult problem is seen by almost all high-powered people but completely invisible to others. Then:

\[
P_i(A)\approx0.05,
\]

Below \(r_{\max}=0.10\), the overall indicator looks safe; however:

\[
P_i(A\mid\theta\text{very high})\approx1.
\]

This question is almost completely exposed to high-ability groups. Stocking (1993) clearly stated that the overall exposure of an item may be low, but it may still be seen by almost all examinees of a certain ability level.

The conditional version of Sympson–Hetter can calibrate \(K_i(\theta)\) separately within several \(\theta\) intervals, but it requires larger simulation samples and more complex parameter calibration, and will also face the problem of early \(\widehat\theta\) instability.

## 10. What can’t it solve automatically?

### There is no guarantee that the item bank will be utilized evenly

The classic method mainly suppresses the highest exposure rate and does not actively increase the usage rate of low-quality or mismatched items that are never selected. So it may happen at the same time:

- A few questions are still close to \(r_{\max}\);
- The exposure rate of a large number of questions is close to \(0\).

Later methods such as the two-stage Sympson–Hetter further attempted to simultaneously control the minimum and maximum exposure rates.

### Cannot directly control test overlap

Decreasing the maximum exposure of a single question usually reduces the item overlap between the two examinees, but the two are not the same constraint. When the fixed length is \(L\), the average pairwise overlap rate can be written as:

\[
\overline O
=
\frac{\sum_i n_i(n_i-1)}
{N(N-1)L},
\]

Among them, \(n_i\) is the number of examinees for item \(i\), and \(N\) is the total number of examinees. Studies should still report test overlap directly instead of just reporting \(\max_i\widehat P_i(A)\).

### The same set of parameters cannot be used permanently

The selection rate \(P_i(S)\) may change simply by changing any of the following:

- Add or delete items;
- Change ability distribution;
- change the starting value or prior;
- Change the topic selection rules;
- Change content constraints;
- Change test length or stopping rule.

Therefore it is usually necessary to recalibrate \(K_i\). van der Linden also later pointed out that classic offline iteration is time-consuming and does not always smoothly obtain parameters that meet the goal; this has promoted online alternative methods such as on-the-fly and item-eligibility.

## 11. What is the difference between randomly selecting the top few questions?

|method|How to introduce randomness|directly control what|Main questions|
|---|---|---|---|
| Randomesque |Randomly select a question from the first few questions with the highest amount of information|Scattered choices within the candidate set|It is difficult to know in advance the ultimate maximum exposure|
| Sympson–Hetter |Select the best question first, then click on the question \(K_i\) to accept or reject|Expected overall exposure per question|Requires repeated simulation calibration|
| Hard cap / restricted |Disable the item directly after reaching the upper limit|Observe Hard Caps on Exposure|Topic selection behavior may suddenly change near the upper limit|
| \(a\)-stratified |Use the low \(a\) layer in the early stage, and open the high \(a\) layer in the later stage.|When to use high-discrimination questions|Do not directly give each question an exposure limit|

These methods can be combined. For example, first form a candidate set according to the \(a\) layer and content constraints, and then use Sympson–Hetter to control the actual test probability of the candidate questions.

## 12. How is it related to the self-assessment starting point method?

Two types of methods act on different parts of probability decomposition:

\[
\underbrace{P_i(A)}_{\text{final exposure}}
=
\underbrace{P_i(A\mid S)}_{\text{Sympson–Hetter control}}
\times
\underbrace{P_i(S)}_{\text{Starting point of self-evaluation and influence of topic selection rules}}.
\]

The self-evaluation starting point sends different examinees to different \(b\) areas. The main change \(P_i(S)\) is to reduce the concentration of choices caused by everyone starting from a common midpoint.

Sympson–Hetter controls \(P_i(A\mid S)\): even if a certain question is still often the top candidate, only some of the choices are allowed to be actually administered.

Therefore, the two are not in competition, but can complement each other:

> Self-evaluation or background information → individualized prior or initial position → forming a candidate area matching \(b\) → selecting candidate questions according to the amount of information, \(a\) layer and content constraints → Sympson–Hetter acceptance or rejection → actual test

However, it must be noted that the self-evaluation starting point has changed to \(P_i(S)\), so the \(K_i\) calibrated under the standard starting point conditions cannot be directly used. Exposure parameters should be recalibrated individually for each starting point method, otherwise the comparison will not be fair.

## 13. The most direct experimental design for this topic

You can first do a clear \(2\times2\) ablation:

|starting point|exposure control|Answered questions|
|---|---|---|
|common starting point|None|Accuracy and Exposure Baseline for Standard Maximum Information Capacity CAT|
|common starting point| Sympson–Hetter |What can direct exposure control alone do?|
|Starting point for self-evaluation|None|What can dispersion \(P_i(S)\) do on its own?|
|Starting point for self-evaluation| Sympson–Hetter |Are the two mechanisms complementary when combined?|

The four groups use the same item bank, ability estimator, content constraints and stopping rule. For both conditions using Sympson–Hetter, the respective \(K_i\) should be calibrated separately.

Report at least simultaneously:

1. bias, root mean squared error (root mean square error, RMSE) and coverage rate;
2. The average number of questions and the number of tail questions required to achieve the same accuracy;
3. Maximum overall exposure rate \(\max_i\widehat P_i(A)\);
4. Item bank exposure distribution and number of effective questions;
5. Conditional exposure rate grouped by real \(\theta\);
6. Conditional exposure rate grouped by self-assessment grade \(C\);
7. The exposure rate of the first question and the effective item bank size of the first question;
8. test overlap。

!!! tip "The real contribution your approach may present"
    If the self-assessment starting point makes \(P_i(S)\) itself more spread out, it is possible that fewer rejections will be needed to achieve the same maximum exposure goal, thus retaining more quiz information. The most meaningful result is not to prove "lower exposure" alone, but to prove that at the same exposure safety level, the question size is shorter or the estimation is more accurate.

## 14. How to understand \(0.90\) and \(0.10\) when reading Zhu and Fan (1999)

Zhu and Fan set the Sympson–Hetter target exposure level to \(0.90\) or \(0.10\):

- \(r_{\max}=0.90\): The control is very loose, and most of the popular questions can still be tested;
- \(r_{\max}=0.10\): The control is very strict, popular questions will be rejected frequently, and more alternative questions will enter the test.

So \(0.10\) is not "each selected question has only a probability of \(10\%\) being tested". Each question has its own \(K_i\):

- \(K_i\) for popular questions may be small;
- Questions that are not popular in the first place may include \(K_i=1\);
- The ultimate goal is \(P_i(A)\le0.10\), not all \(K_i=0.10\) are required.

This also explains the result of Zhu and Fan: strict control makes the No-Info method have to use more medium-difficulty alternative questions, and the overall item usage looks more scattered; but it does not eliminate the selection pressure caused by a common intermediate starting point.

## References

- Chao, H.-Y., & Chen, J.-H. (2023). Controlling the minimum item exposure rate in computerized adaptive testing: A two-stage Sympson–Hetter procedure. *Applied Psychological Measurement, 47*(7–8), 460–477. [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10664747/) · [DOI](https://doi.org/10.1177/01466216231209756)
- Stocking, M. L. (1993). *Controlling item exposure rates in a realistic adaptive testing paradigm* (ETS Research Report RR-93-02). Educational Testing Service. [ERIC Full text PDF](https://files.eric.ed.gov/fulltext/ED384663.pdf) · [DOI](https://doi.org/10.1002/j.2333-8504.1993.tb01513.x)
- Sympson, J. B., & Hetter, R. D. (1985). Controlling item-exposure rates in computerized adaptive testing. In *Proceedings of the 27th Annual Meeting of the Military Testing Association* (pp. 973–977).
- van der Linden, W. J. (1999). Empirical initialization of the trait estimator in adaptive testing. *Applied Psychological Measurement, 23*(1), 21–29. [DOI](https://doi.org/10.1177/01466219922031149)
- van der Linden, W. J. (2006). *A formal characterization of and some alternatives to Sympson–Hetter item-exposure control in computerized adaptive testing* (LSAC Computerized Testing Report 02-05). Law School Admission Council. [Publication Information and Full Text Portal](https://research.utwente.nl/en/publications/a-formal-characterization-of-and-some-alternatives-to-sympson-het/)
