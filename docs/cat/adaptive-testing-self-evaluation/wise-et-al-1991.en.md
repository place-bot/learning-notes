# Wise et al. (1991): Direct comparison of Self-Adapted Testing and Computerized Adaptive Testing

!!! abstract "Key takeaway"
    **What was done:** Wise et al. divided 204 students into Self-Adapted Testing and Computerized Adaptive Testing with a fixed 20 questions. Both groups received feedback on a question-by-question basis. The difference was that the examinee or the algorithm determined the difficulty of the next question. **What we got:** The self-selected items group had a higher average ability estimate and lower post-test state anxiety, but it took longer to complete and had a larger ability estimate variance error. **Conclusion on this topic:** Self-selection may change the response state, but it does not prove that the measurement efficiency is improved; due to limitations such as fixed test length, grouping and immediate feedback, this article cannot answer whether self-evaluation can stop standard CAT earlier.

## Citation details

> Wise, S. L., Plake, B. S., Johnson, P. L., & Roos, L. L. (1991, April). *A comparison of self-adapted and computer-adaptive tests*. Paper presented at the Annual Meeting of the American Educational Research Association, Chicago, IL. ERIC ED331888.

- [ERIC full text PDF](https://files.eric.ed.gov/fulltext/ED331888.pdf)
- Study population: Algebra skills remediation screening of students in introductory college statistics courses
- Comparison: Self-Adapted Testing (SA) and Computerized Adaptive Testing (CA)
- sample size: \(N=204\), SA and CA each \(n=102\)

!!! note "Abbreviations"
    The paper refers to Self-Adapted Testing as SA and Computerized Adaptive Testing as CA. This topic uses the more common CAT, Computerized Adaptive Testing, when discussing this area of ​​research. CA and CAT here refer to the same type of computerized adaptive testing, but the abbreviations used in the original paper and this topic are different.

## 1. Why does the paper propose Self-Adapted Testing (SA)?

Item Response Theory (IRT) puts the difficulty of different items and the abilities of different examinees on the same latent scale. As long as the item bank has been calibrated and the model is established, even if different people answer different items, the ability estimates can still be compared on the same scale. Traditional Computerized Adaptive Testing (CA) takes advantage of this, and the algorithm selects the next question based on previous responses.

The author believes that the standard CA algorithm mainly uses the observed item response, but does not directly utilize the examinee's current anxiety, motivation and self-perceived ability. The previous self-adapted testing therefore proposed that allowing the examinee to choose the difficulty of the next question may be able to bring information invisible to these algorithms into the question selection process.

The core differences between the two tests are:

```text
SA: answer the previous item -> get correctness feedback -> self-selected difficulty level -> the system administers the item at this level
CA: answer the previous item -> get correctness feedback -> computer selects questions based on performance -> administer the item
```

SA here is not "evaluate yourself first and then run CAT". It retains the choice of difficulty for a full 20 questions, unlike the brief self-assessment starting point for this topic's preparation study.

## 2. How to create samples and item bank

### examinee

The sample was drawn from five introductory statistical methods classes at a university in the Midwestern United States and included 156 undergraduates and 48 graduate students; 76 males and 128 females. Participation is a course requirement, and test results are used to identify the need for remedial study in Basic Algebra.

The author conducted power analysis before collecting data. The standard deviation of the IRT ability scale is expected to be approximately 1, considering \(0.25\) as the minimum meaningful mean difference; blocking is expected to reduce the error variance, making the standardized effect approximately \(0.35\). With about 100 people in each group and significance level \(0.05\), the paper estimates the statistical power to be \(0.68\). By today's common standards, this statistical power is not generous, especially since the two main \(p\) values ​​are close to \(0.05\).

### item bank development

The item mainly measures the algebraic skills needed to learn introductory statistics, and also includes a small number of probability and logical reasoning questions. item bank went through the following process:

1. Initial preparation of 120 four-choice questions;
2. Two authors and two graduate students respectively evaluate the appropriateness and difficulty of the content;
3. Delete or modify the unqualified items to form three test papers with 35 questions each, similar content and difficulty, for a total of 105 non-duplicate questions;
4. Between January 1988 and July 1989, each test paper was answered by approximately 250 people;
5. Conduct principal axis factor analysis on each test paper and delete 12 questions with single factor loading lower than (0.10);
6. Finally got 93 questions item bank.

The first eigenvalue in each test paper explains 20%--25% of the total variance. The author concludes from this that the item bank is sufficient for single-factor IRT analysis. However, each pre-tester only answered one of the three test papers, so the paper also clearly admitted that it did not directly test the dimensional structure of the complete 93-question item bank.

The final item bank is calibrated using LOGIST. The author uses a modified one-parameter logistic model and fixes the lower asymptote of each item characteristic curve to \(0.20\). Formal tests estimate ability using the maximum likelihood method.

## 3. How to perform testing with Self-Adapted Testing (SA) and Computerized Adaptive Testing (CA)

Both tests use MicroCAT software, have a fixed set of 20 questions, and examinee the correct answer immediately after each question is answered.

### Self-Adapted Testing (SA) conditions

The 93 questions are divided into six levels according to the difficulty parameter, with 15 or 16 questions in each level. The items within each level are randomly sorted first, and then the order is fixed. Therefore, examinees who choose the same level will encounter the same first and second questions in that level in sequence, and so on.

Before each question appears, examinee selects a difficulty level from 1 (easiest) to 6 (hardest). The caption tells them:

- The harder the choice, the greater the weight of the score you get when you answer it correctly;
- It is recommended to choose the most difficult problem that you think you can answer correctly;
- The final score will take into account item difficulty. In theory, which level you choose should not change the final score.

If a certain level of questions has been used up, the system will ask you to choose again.

### Computerized Adaptive Testing (CA) conditions

The examinee was told that the computer would select questions based on performance: give more difficult questions for correct answers, easier questions for incorrect answers, and take item difficulty into account when scoring. The paper does not fully report the initial \(\theta\), precise topic selection criteria, extreme reaction mode processing and exposure control settings like modern CAT research, so it is impossible to reproduce its CA algorithm item by item based on this article alone.

### Decision after the test

After 20 questions, the system calculates the ability estimate. Students with abilities below (0.20) were informed that they would need to attend a one-hour remedial math class the following week. The paper states that this threshold corresponds to the domain score (0.77) on the test characteristic curve of the entire item bank.

## 4. What does the study measure?

The paper has four dependent variables:

1. Item Response Theory (IRT) ability estimate;
2. Post-test state anxiety;
3. Total test time;
4. Error variance of ability estimate.

State anxiety was measured before and after the test using the State Anxiety Scale from the State-Trait Anxiety Inventory.

Ability and post-test anxiety were analyzed using two-factor analysis of variance (ANOVA): when analyzing ability, the number of years since the last algebra class was used as the blocking variable; when analyzing post-test anxiety, pre-test state anxiety was used as the blocking variable. The test time and error variance distributions are significantly skewed, so use the large-sample \(z\) approximation of the Mann-Whitney \(U\) test. All inspections use \(\alpha=.05\).

## 5. Look at the result item by item.

|result| Self-Adapted Testing（SA） | Computerized Adaptive Testing（CA） |Group comparison|
|---|---:|---:|---|
|ability estimate, mean (standard deviation)| \(0.37\;(1.14)\) | \(0.06\;(1.05)\) | \(F=5.19,\ p=.024\) |
|Post-test state anxiety, mean (standard deviation)| \(37.25\;(11.13)\) | \(39.28\;(12.17)\) | \(F(1,198)=4.16,\ p=.043\) |
|Test time, median (minutes)| \(22.15\) | \(18.70\) | \(z=2.18,\ p=.029\) |
|Ability error variance, median| \(0.14\) | \(0.12\) | \(z=3.60,\ p<.001\) |

### ability estimate

The SA group average ability estimate is \(0.31\) logit higher. Time since the last algebra class also has a significant main effect, and the interaction between test type and this blocking variable is not significant.

The original text printed the test type effect as \(F(1,98)=5.19\). However, the total sample is 204, and the adjacent blocking effect is reported as \(F(2,198)\). According to this \(2\times3\) design inference, the denominator degree of freedom should be 198; it is likely that a "1" is missing from the original text. This website retains this errata reminder and does not silently rewrite it as the paper has been correctly reported.

### Post-test anxiety

After controlling for pretest anxiety blocking, the SA group reported lower posttest state anxiety. However, the two groups' unadjusted overall means differed by only about 2 points, and \(p=.043\). The paper does not report effect size or confidence interval.

### Time and precision

Median test time for SA was 3.45 minutes longer than for CA. The reasons at least include that examinee has to make a difficulty decision for each question, and computers can select questions faster.

CA's ability error variance is smaller, which is consistent with CAT's item selection criteria: the algorithm actively selects questions that can best reduce the uncertainty of the ability estimate. The maximum value of SA error variance reaches 22.08, while CA is 3.48, indicating that there are more extreme imprecise cases in SA conditions.

## 6. How to understand "ability estimate does not depend on specific items"

The author writes the result as a challenge to the invariance of the IRT item, but conditions must be added to this sentence.

The invariance of IRT mainly means that if the model is correct, the item parameters have been placed on the same scale, and the answering process remains stable, then people who answer different items can still estimate their abilities on the same scale. It does not guarantee that the two question sets will give exactly the same point estimates under a limited number of questions, nor does it guarantee that Examinee's answering mechanism will remain unchanged after changing the test interface, sense of control, feedback utilization, and anxiety.

Therefore, there are at least three explanations for this study:

1. examinee does make use of the algorithm’s unobserved self-knowledge to make a more appropriate topic selection;
2. Self-selection reduces anxiety or improves motivation, causing actual answering performance to change;
3. The topic selection path and response process of SA cause model mismatch or estimation bias, which improves the ability score but does not necessarily bring it closer to the target ability.

The higher mean SA score alone precludes a choice between the three explanations. The paper does not have an independent standard of true ability, nor does it examine item parameters, measurement invariance, or differential item functioning under the two conditions.

## 7. What are the limitations of causal explanation?

### The grouping instructions are not completely consistent.

At the beginning of the method, it is written that examinee is randomly assigned to two conditions; but in the program part, it is written that students can choose a computer after arriving to enter SA or CA. Midway through the study, the types of tests the computers ran were switched, which reduced fixed-seat bias but was not equivalent to clearly documented random assignment of individuals. This internal inconsistency affects the reliability of causal explanations.

### Instant feedback and self-selection are intertwined

Both groups received feedback after each question, so “feedback or not” was not a between-group difference. However, only the SA group had to use feedback to determine the difficulty of the next question. The effect of SA may come from autonomy, feedback utilization, difficulty selection itself, or the interaction of the three, which this article cannot unpack.

### Test the four endings separately

The paper uses \(\alpha=.05\) for all four dependent variables and does not report multiple comparison corrections. The \(p\) values ​​for Ability and Anxiety were .024 and .043, respectively, and are appropriately considered preliminary evidence for replication rather than very solid conclusions.

### fixed length cannot answer the efficiency assumption

Both groups had to complete 20 questions. The paper compares the ability, anxiety, time and accuracy after completing the same number of questions, rather than how many questions are needed to achieve the same standard error. Therefore, it did not test "whether the use of self-evaluation can allow CAT to trigger the stopping rule earlier."

## 8. How close it is to the idea of this topic

|Dimensions| Wise et al. (1991) |The design this topic focuses on|
|---|---|---|
|self information|Choose a difficulty level for each question|Report your level at the beginning, or select only the first \(k\) questions|
|control duration|All 20 questions|Very short, followed by standard CAT|
|test length|Fixed 20 questions|Determined by the original precision stopping rule|
|Main comparison|Ability, anxiety, time, error variance|Question volume, bias, root mean squared error (root mean square error, RMSE), coverage rate, experience|
|key risks|Self-selection sacrifices estimation accuracy|Can wrong starting points be quickly corrected by CAT?|

Therefore, this paper is an important conceptual precursor, but it has not completed the experiments we really care about. It tells us: self-selection may change performance and anxiety, and may also reduce measurement accuracy; the next step is not to just compare the average scores, but to simultaneously use the question volume and estimated quality under the same stopping rule as the main result.

A direct follow-up experiment can set up three groups:

1. Standard CAT: everyone starts from the same starting position;
2. Self-report initialization: map the self-report level to \(\widehat{\theta}^{(0)}\), and then run the standard CAT immediately;
3. Top \(k\) questions self-selection: only allow a brief selection of difficulty, after which the same CAT as the first set is run.

The three groups must share the item bank, ability estimator, topic selection constraints, and stopping rules to determine whether the efficiency gains truly come from a better starting point.

## References

- Hambleton, R. K., & Swaminathan, H. (1985). *Item response theory: Principles and applications*. Kluwer-Nijhoff.
- Rocklin, T., & O'Donnell, A. M. (1987). Self-adapted testing: A performance-improving variant of computerized adaptive testing. *Journal of Educational Psychology, 79*(3), 315-319. [https://doi.org/10.1037/0022-0663.79.3.315](https://doi.org/10.1037/0022-0663.79.3.315)
- Wise, S. L., Plake, B. S., Johnson, P. L., & Roos, L. L. (1991). *A comparison of self-adapted and computer-adaptive tests*. ERIC ED331888.
