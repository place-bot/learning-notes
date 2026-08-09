# Chang and Ying (1999): Why high-discrimination questions do not need to be used from the beginning

!!! abstract "Key takeaway"
    **What they did: **Chang and Ying layered the item bank according to the discrimination parameter \(a\). In the early stage, the low \(a\) layer was matched with the current capability position by \(b\). In the later stage, the high \(a\) questions were gradually opened. **What was gained:** In the fixed length simulation, this method significantly improved the item usage balance and test overlap, while maintaining roughly comparable overall bias and mean squared error, but it cannot guarantee the upper limit of single-question exposure, and there is also a certain accuracy cost in the real item bank. **Conclusion on this topic:** What the paper supports is that "the more uncertain the position, the greater the cost of incorrectly matching high \(a\) questions", not "the beginning of high \(a\) questions will inevitably be wasted"; if the individualized prior is very accurate, early high \(a\) questions may be the most effective.

## Citation details

> Chang, H.-H., & Ying, Z. (1999). *a*-stratified multistage computerized adaptive testing. *Applied Psychological Measurement, 23*(3), 211–222. [DOI](https://doi.org/10.1177/01466219922031338)

- Study type: Methods paper and two Monte Carlo simulations
- Core question: How to avoid repeatedly consuming high-discrimination questions by selecting topics with the maximum amount of information, while maintaining the efficiency of ability estimate
- New method: Layer the item bank according to the itemdiscrimination parameter \(a\). Use the low \(a\) layer in the early stage of the test, and gradually open the high \(a\) layer in the later stage.
- In-layer topic selection: no longer maximizes information across the entire item bank, but matches item difficulty \(b\) with the current ability estimate \(\widehat\theta\) within the current \(a\) layer
- Main comparison: \(a\)-stratified method versus Fisher information content or Bayesian topic selection plus Sympson–Hetter exposure control
- Main conclusion: In fixed length simulation, the hierarchical method greatly improves the overall exposure balance and test overlap, while maintaining roughly comparable overall bias and mean squared error; however, it does not guarantee the upper limit of single question exposure, and a certain accuracy price is paid in the real parameter item bank.

!!! important "The most important revision to this topic"
    "High \(a\) questions will definitely be wasted in the early stage" is not the conclusion of the paper. If the individualized prior is very accurate, the \(b\) of the first question is already close to the real \(\theta\), and the higher \(a\) question may provide a lot of information immediately. This article supports a conditional proposition: **The more uncertain the ability position, the greater the cost of mismatching high \(a\) questions. **This just expands the fixed question order layering into the research question of "when to open high \(a\) determined by individual posterior uncertainty".

## 1. Why does the maximum amount of information prefer questions with high \(a\)

### 1.1 Item information under the two-parameter logistic model

In a two-parameter logistic model (2PLM):

\[
P_i(\theta)
=
\frac{1}{1+\exp[-a_i(\theta-b_i)]}.
\]

The Fisher information of item at capability \(\theta\) is:

\[
I_i(\theta)
=
a_i^2
\frac{\exp[a_i(\theta-b_i)]}
{\{1+\exp[a_i(\theta-b_i)]\}^2}.
\]

If item difficulty is exactly equal to true ability:

\[
b_i=\theta,
\]

Then:

\[
I_i(\theta)=\frac{a_i^2}{4}.
\]

Therefore, in perfect difficulty matching, the larger \(a_i\) is, the more information the item has. The standard maximum information amount rule will naturally repeatedly select the question with the largest \(a\), \(b\) and close to the current \(\widehat\theta\) in the item bank.

### 1.2 The real match in the early stage was \(\widehat\theta\), not the real \(\theta\)

Let the ability estimate after question \(k\) be \(\widehat\theta_k\). If the item bank is rich enough, the maximum information rule will find:

\[
b_i\approx\widehat\theta_k.
\]

From the algorithm’s perspective, the estimated information for this question is approximately:

\[
I_i(\widehat\theta_k)\approx\frac{a_i^2}{4}.
\]

But the real information should be calculated at examinee real capability \(\theta_0\):

\[
I_i(\theta_0)
=
a_i^2
\frac{\exp[a_i(\theta_0-\widehat\theta_k)]}
{\{1+\exp[a_i(\theta_0-\widehat\theta_k)]\}^2}.
\]

if:

\[
\widehat\theta_k\neq\theta_0,
\]

When the error is fixed and nonzero, the actual information approaches 0 as \(a_i\) grows. Intuitively, the information curve of a high-\(a\) item is tall but narrow: it is extremely effective when correctly targeted, but quickly loses information when it is mistargeted.

### 1.3 The precise meaning of “waste”

The waste here is not "the item is answered incorrectly", nor is it "high \(a\) questions cannot estimate ability", but:

\[
\underbrace{I_i(\widehat\theta_k)}_{\text{The information the algorithm thinks it can get}}
\quad\text{very high,}
\qquad
\underbrace{I_i(\theta_0)}_{\text{Information obtained from true capabilities}}
\quad\text{But it's very low.}
\]

High-value items are therefore exposed before they are accurately positioned, without realizing the information they could have provided. This also brings:

- Measurement efficiency loss;
- High \(a\) questions are overexposed;
- Low \(a\) test length period idle;
- The overlap of items between examinees increases.

## 2. How to run the original \(a\)-stratified method

### 2.1 Layer the item bank according to \(a\) from low to high

Divide the item bank into \(K\) levels:

\[
\mathcal A_1,\ldots,\mathcal A_K,
\]

The first level contains the lowest \(a\) questions, and the first level \(K\) contains the highest \(a\) questions.

Then divide the fixed length test into \(K\) stages in the same order:

\[
\text{stage }1
\rightarrow
\text{stage }2
\rightarrow
\cdots
\rightarrow
\text{stage }K.
\]

Stage \(k\) is only allowed to select topics from \(\mathcal A_k\). Therefore, everyone experiences:

\[
\text{low}a
\rightarrow
\text{in}a
\rightarrow
\text{high}a.
\]

### 2.2 Do \(b\)-matching in the current layer

The next question in stage \(k\) is:

\[
j_t
=
\arg\min_{j\in\mathcal A_k}
|b_j-\widehat\theta_{t-1}|.
\]

Because \(a_j\) in the same layer is close, under 2PLM, minimizing \(|b_j-\widehat\theta|\) is basically equivalent to maximizing item information in this layer.

In the three-parameter logistic model (3PLM), guessing parameter \(c_j\) will also affect information; the author believes that simply matching \(b\) after fixing \(a\) is an approximation of the maximum amount of information, but admits that the method in this article intentionally ignores the role of \(c\).

### 2.3 Randomization details in simulations

The actual implementation of the paper is not to always select the only nearest \(b\). The system first finds the two candidate questions with the smallest \(|b_j-\widehat\theta|\) in the current layer, and then randomly tests one of them.

This step has two functions:

1. Keep difficulty matching;
2. Prevent everyone with similar ability estimates from seeing the exact same questions.

It is an intra-layer randomization baseline that this topic can draw directly from.

### 2.4 How many questions are used in each layer?

If the total test length is \(L\), it is generally recommended to use approximately:

\[
n_k\approx\frac{L}{K},
\qquad
\sum_{k=1}^{K}n_k=L.
\]

The capacity of each layer in the item bank should also be proportional to the number of questions planned to be tested in that layer, so that the average exposure in different layers is close. The author specifically points out that the first layer needs to be large enough to ensure that the early ability estimate equation has an appropriate solution.

But the paper does not give the universal optimal \(K\). The number of layers depends on:

- The degree of dispersion of \(a\) in the item bank;
- Whether the \(b\) coverage of each layer is wide enough;
- item bank size;
- test length;
- Content constraints.

## 3. Why can it improve item exposure?

### 3.1 The maximum amount of information concentrates the selection on the high end \(a\)

If you maximize the information across the entire item bank every time, it will be easier to win the high-level \(a\) questions. Even with the addition of Sympson–Hetter control, the algorithm only rejects some popular questions that have already been selected; it does not actively increase the usage of low-\(a\) questions that are almost never selected.

### 3.2 Complete "pressing up" and "raising down" in layers at the same time

The \(a\)-stratified method forces questions to be taken from the low \(a\) layer in the early stage, and only enters the high \(a\) layer later. Therefore:

- High \(a\) questions will not run through the entire competition, and exposure will decrease;
- The low \(a\) question has gained a clear usage stage, and its exposure has increased;
- The item parameters in each layer are more similar. \(b\)-matching plus random selection can further disperse the use.

This is different from the Sympson–Hetter mechanism:

|method|How to deal with hot topics|Can you proactively use unpopular questions?|Is the upper limit for a single question guaranteed?|
|---|---|---|---|
| Sympson–Hetter |After selection, reject according to the probability of acceptance.|No; questions that are never selected will still not be administered|Calibrated to approximate control|
|Original \(a\)-stratified|Limit the \(a\) layers that can be entered in each stage|Capable; low \(a\) layer has dedicated stage|Can't|

## 4. How to measure whether the exposure of a paper is balanced

### 4.1 Single question exposure rate

If there is \(m\) name examinee and item \(j\) is tested \(n_j\) times, then:

\[
er_j=\frac{n_j}{m}.
\]

When the fixed length is \(L\) and the item bank size is \(N\), the average exposure rate of all items is always:

\[
\overline{er}=\frac{L}{N}.
\]

This is a conservation relationship: under the same \(L\) and \(N\), no method can reduce the "average exposure rate across the entire item bank". What the method can change is the dispersion, maximum value, number of low-exposure questions, and overlap between examinee exposure rates.

!!! warning "The wording in the abstract cannot be copied"
    The abstract states that STR achieves a lower average exposure rate, but at fixed \(L,N\), \(\overline{er}=L/N\) is identical for the three methods. What Table 1 really supports is that STR has a more balanced exposure distribution, fewer low-exposure questions, and lower test overlap, rather than a lower overall average exposure rate.

### 4.2 \(\chi^2\) discrepancy with uniform target

Author's definition:

\[
\chi^2
=
\sum_{j=1}^{N}
\frac{(er_j-\overline{er})^2}{\overline{er}}.
\]

The smaller the value, the closer the observed exposure distribution is to an ideal uniform distribution in which all questions are exposed at \(L/N\). It is modeled after Pearson \(\chi^2\), but here is primarily a descriptive discrepancy and should not automatically be taken as a significance test with a standard reference distribution.

Two methods can be compared using ratios:

\[
F_{1,2}
=
\frac{\chi_1^2}{\chi_2^2}.
\]

If \(F_{1,2}<1\), the exposure distribution of method 1 is closer to uniform. The author further states:

\[
1-F_{1,2}
\]

Interpreted as skewness reduction relative to method 2.

### 4.3 Test overlap

Test overlap rate is the expected proportion of the number of items that the two examinees have seen together to the test length when two examinees are randomly selected:

\[
\mathrm{Overlap}
=
\frac{\text{The sum of the number of common items for all examinee pairs}}
{L\,m(m-1)/2}.
\]

The theoretical lower bound of fixed length CAT is:

\[
\frac{L}{N}.
\]

Therefore, the lower bound of the 40-question or 400-question item bank is 10%; STR got 11%, which is very close to the lower bound.

## 5. How to set up two simulations

### 5.1 Three comparison methods

Paper comparison:

- **STR**: \(a\)-stratified selection, enter different \(a\) layers according to stages, match \(b\) within the layer;
- **FSH**: Fisher maximum information selection plus Sympson–Hetter;
- **BSH**: Bayesian item selection plus Sympson–Hetter, select items with minimum posterior variance.

STR and FSH use maximum likelihood estimation (maximum likelihood estimation, MLE); BSH uses expected a posteriori estimation (expected a posteriori, EAP), and the prior is:

\[
\theta\sim N(0,1),
\]

and uses 40 numerical integration points.

Therefore, the three conditions not only change the topic selection: BSH also changes the ability estimate method. This means that the difference in mean squared error of BSH cannot be entirely attributed to topic selection or exposure control.

### 5.2 Common three-question initialization

All three methods first use three "artificially generated" initialization questions. Question 1:

\[
a_0=1,
\qquad
b_1\sim N(0,1),
\qquad
c_0=.2.
\]

If the answer is correct, the difficulty of the next question increases by 2; if the answer is wrong, the difficulty of the next question decreases by 2. An initial MLE was obtained after repeating three questions. The authors note that BSH does not require this step, but still uses the same initialization for comparison purposes.

!!! note "This is not what we usually call a unified medium starting point"
    \(b_1\) in the first question is randomly selected from the standard normal, and the three questions use artificial parameters, not selected from the simulated item bank according to three algorithms. The paper also does not clearly state whether these three questions are included in the nominal test length and item bank exposure statistics. They weaken the differences between the three main algorithms in the first three questions, and the result cannot be directly interpreted as "using STR from the first question".

### 5.3 Study 1: Idealized 2PLM item bank

- examinee: 3,000 simulated ability values;
- Capability distribution: \(N(0,1)\);
- item bank: 400 questions;
- test length: 40 or 60;
- Number of layers: \(K=4\);
- Each level: 100 questions;
- Four layers \(a\): .5, 1.0, 1.5, 2.0;
- Each question \(b\): randomly generated from \(N(0,1)\);
- Formal item bankguessing parameter: \(c=0\);
- Target maximum exposure for FSH and BSH: \(r=.20\).

This setup is particularly neat for STR: \(a\) is identical within the layer, the four layers are equal in size, and \(b\) is identically distributed with \(\theta\). It's suitable for demonstrating mechanics, but is more ideal than a real item bank.

### 5.4 Study 2: Real 3PLM item parameters

- item source: 1992 National Assessment of Educational Progress reading test;
- item bank: 254 questions;
- test length: 20;
- examinee: Use the 3,000 \(N(0,1)\) simulation capability values from Study 1;
- Number of layers: 4;
- Layer size: 65, 63, 63, 63;
- Parameter: \(a,b,c\) calibration value of actual 3PLM.

STR is still only layered by \(a\), matched by \(b\), and \(c\) is not explicitly handled in the selection rules. This makes Study 2 closer to reality and more easily exposes the accuracy cost of simplifying the rules.

## 6. Check the results of Table 1 item by item

|Conditions|method| MSE | Bias | Overlap | \(\chi^2\) |The number of questions with an exposure rate of no more than 2%|
|---|---|---:|---:|---:|---:|---:|
|Study 1, 40 questions| STR | .022 | -.004 | 11% | 6.931 | 1 |
|  | FSH | .017 | -.006 | 19% | 33.923 | 169 |
|  | BSH | .028 | .002 | 20% | 40.011 | 200 |
|Study 1, 60 questions| STR | .014 | -.001 | 17% | 8.286 | 0 |
|  | FSH | .015 | -.001 | 19% | 17.858 | 73 |
|  | BSH | .024 | .002 | 20% | 19.197 | 92 |
|Study 2, 20 questions| STR | .084 | .007 | 10% | 5.910 | 5 |
|  | FSH | .060 | .007 | 18% | 25.635 | 129 |
|  | BSH | .078 | -.004 | 19% | 26.875 | 134 |

### 6.1 Conditions for the 40 questions in Study 1

The overlap of STR is 11%, close to the theoretical lower bound of 10%; FSH and BSH are 19% and 20% respectively. The average questions that two random examinees see together are approximately:

\[
40\times .11=4.4
\]

For STR, and about:

\[
40\times .19=7.6,
\qquad
40\times .20=8.0
\]

for FSH and BSH. The text summarizes them into about 4 ways and about 8 ways.

STR's \(\chi^2\) is only .204 of FSH and .173 of BSH, so the author claims that the relative skewness drops by about 80% and 83% respectively. At the same time, the number of questions with an exposure rate of not more than 2% dropped from 169 for FSH and 200 for BSH to 1 for STR.

In terms of accuracy, STR has an MSE of .022: higher than .017 for FSH, but lower than .028 for BSH. The overall Bias of the three is close to 0.

### 6.2 Conditions for the 60 questions in Study 1

STR has the lowest MSE:

\[
.014\quad\text{vs.}\quad .015\quad\text{vs.}\quad .024.
\]

All questions had more than 2% exposure under STR, while FSH and BSH also had 73 and 92 low-exposure questions respectively. The overlap of STR is 17%, which is lower than 19% of FSH and 20% of BSH. However, compared with the theoretical lower bound of 60/400=15%, the room for improvement is inherently small.

### 6.3 Real parameter conditions for the 20 questions in Study 2

STR continues to significantly improve exposure: overlap is 10%, FSH and BSH are 18% and 19%; \(\chi^2\) is reduced by about 77%–78%; there are only 5 low-exposure questions left, while the other two methods have 129 and 134 questions.

But the accuracy cost cannot be downplayed. The MSE is .084 for STR and .060 for FSH:

\[
\frac{.084-.060}{.060}=40\%.
\]

The author's text states that STR is only "slightly higher MSE", which is not small in terms of relative difference. The absolute difference is .024, and the paper does not have a Monte Carlo standard error, so the uncertainty of the difference cannot be judged; but Study 2 cannot be summarized as "no loss of accuracy at all."

## 7. Which results support the author’s conclusion, and which ones need to be lowered?

### There are directly supported conclusions

- STR significantly increases the use of low \(a\) and originally low-exposure questions;
- STR reduced overall exposure imbalance in all three simulation conditions;
- In all three conditions, STR reduces test overlap;
- Overall Bias is small in all conditions;
- In idealized Study 1, the MSE of STR is roughly of the same order as the comparison method.

### More cautious conclusions are needed

1. **"Lower average exposure" is not true. **The fixed test length and item bank size determine that the average exposure is always \(L/N\).
2. **"Maintaining efficiency" is conditional. **Study 2’s STR MSE is 40% higher than FSH.
3. **Overall unbiased does not mean that each ability point is unbiased. **The paper only reports the average bias, and does not give the conditional bias and RMSE of the \(\theta\) tail.
4. **There is no guarantee of maximum exposure for a single question. **In the figure, individual STR questions can still be significantly higher than .20, and the author also lists this as a problem for improvement.
5. **BSH comparisons mix estimator differences. **BSH uses EAP, while STR and FSH use MLE.
6. **No content balancing. **The content, hostile questions and question group constraints in the real exam have not yet been entered into the method.

## 8. Seven unresolved problems acknowledged by the paper itself

The author clearly lists at the end:

1. STR cannot guarantee that each question will be lower than the specified exposure limit;
2. Combinations of STR and Sympson–Hetter should be studied;
3. In 3PLM, the impact of \(c\) on topic selection is deliberately ignored;
4. The estimation error of item parameters should be studied;
5. The \(a\) layer number should be further studied;
6. Content balance constraints should be added;
7. Existing research only does fixed length CAT and should be extended to variable length CAT based on the accuracy of the ability estimate.

This last point is especially important. The authors have proposed that in variable length tests, the number of questions used in each layer can be dynamically determined based on the estimation accuracy achieved by that layer. This is a direct theoretical entrance to upgrade the fixed question sequence to a posteriori uncertainty rule, but there is no actual simulation in this article.

## 9. What is its relationship with "Self-Assessment for CAT"

This article does not use:

- examinee self-evaluation;
- Background variables;
- individualized prior;
- individualized starting question;
- Dynamic \(a\) layer driven by posterior variance.

It solves the problem of item bank management: how to consume less high \(a\) problems when the true capabilities are not known and early estimates are unstable.

But it provides a very clear division of labor for this topic:

\[
\text{Self-assessment or prior decision "where the person is"}
\quad\Longleftrightarrow\quad
b\text{-matching},
\]

\[
\text{Current uncertainty determines “how sharp the questions should be”}
\quad\Longleftrightarrow\quad
a\text{-stratification}.
\]

In other words, \(b\) is a problem of individualized location, and \(a\) is a problem of how to configure item resources under the current positioning reliability.

## 10. How to verify whether there is any benefit in "not using high \(a\) in the early stage"

### 10.1 Don’t just look at the final RMSE

To directly test the mechanism of the paper, the information on how each question is achieved at its true ability should be recorded:

\[
I_{j_t}(\theta_i).
\]

At the same time, record the information that the algorithm thought you would get when selecting the topic:

\[
I_{j_t}(\widehat\theta_{i,t-1}).
\]

The absolute difference between the two can be defined as the early information mismatch magnitude:

\[
G_{it}
=
\left|
I_{j_t}(\widehat\theta_{i,t-1})
-
I_{j_t}(\theta_i)
\right|.
\]

Information regret can also be calculated relative to an oracle that knows the true capabilities:

\[
R_{it}
=
\max_{j\in\mathcal E_t}I_j(\theta_i)
-
I_{j_t}(\theta_i),
\]

Among them, \(\mathcal E_t\) is the available question set that satisfies the content and exposure constraints at that time.

If high \(a\) questions are indeed wasted in the early stage, it should be observed that: the standard maximum information content condition is higher in the first few questions \(G_{it}\) or \(R_{it}\), while the exposure of high \(a\) questions is more concentrated.

### 10.2 You must look at the item resource result at the same time

Report at least:

- The overall exposure rate of each question is \(P(A_j)\);
- \(P(A_j\mid\theta)\) grouped by real abilities;
- \(P(A_j\mid C)\) grouped by self-assessment level;
- Maximum exposure;
- Low exposure and the number of items that have never been used;
- test overlap；
- Distribution of \(a\) tested at different question order positions;
- Actual \(I_j(\theta_i)\) obtained per high \(a\) exposure.

This is how to distinguish between "just using less high \(a\) questions" and "really improving the measured return per high \(a\) exposure."

## 11. Extension from fixed stage to posterior variance driven \(a\) layer

### 11.1 A natural extension

The user first selects the self-assessment grade \(C=c\) to get the individualized prior:

\[
p_0(\theta\mid C=c)
=
N(\mu_c,\tau_c^2).
\]

Calculate the current posterior variance before question \(t\):

\[
V_{t-1}
=
\operatorname{Var}(\theta\mid\mathcal D_{t-1},C=c).
\]

Then press Uncertainty to select the \(a\) layer:

\[
\ell_t=g(V_{t-1}),
\]

And do \(b\)-matching within this layer:

\[
j_t
=
\arg\min_{j\in\mathcal A_{\ell_t}}
|b_j-\widehat\theta_{t-1}|.
\]

For example:

- \(V_{t-1}>.75\): Low \(a\) layer;
- \(.25<V_{t-1}\le.75\): middle \(a\) layer;
- \(V_{t-1}\le.25\): Open high \(a\) layer.

Compared with the fixed "low \(a\) for the first two questions and high \(a\) after that", this rule allows people with reliable self-assessment and narrow prior to use high \(a\) questions earlier, and also allows people with conflicting evidence and still uncertain positioning to continue exploring.

### 11.2 A new risk that must be guarded against

If the prior is narrow but the mean is wrong, the initial posterior variance may already be small:

\[
\tau_c^2\ll1,
\qquad
|\mu_c-	heta_i|\text{very big}.
\]

Simply relying on \(V_{t-1}\) will incorrectly determine "reliable positioning" and open higher questions \(a\) from the first question. This is more dangerous than the original fixed STR because the model behaves confidently but in the wrong place.

Therefore, it is best to add at least one protection to dynamic rules:

- It is required to complete at least a few formal questions before opening the high \(a\);
- Set a lower limit of variance for self-evaluation prior;
- Use mixture or power prior to reduce the impact of incorrect self-assessments;
- Use posterior predictive conflict to check whether self-assessment and responses continue to conflict;
- Fallback to lower \(a\) layer and relax prior on conflict.

## 12. Step-by-step ablation design

### First level: Reproduce the 1999 mechanism first

1. Standard prior plus maximum information amount;
2. Standard prior plus fixed question order \(a\)-stratified;
3. Add the same exposure control to both.

This step verifies whether the problem of "early mismatching of high \(a\) questions and idle low \(a\) questions" really exists in the item bank.

### Second level: only change prior

4. Individualized prior increases the maximum amount of information;
5. Repeat under correct, high, low prior means and various prior variances.

This step answers: Have accurate self-assessments made high \(a\) questions safe for early use, thereby undermining the need for a fixed STR?

### The third level: combination of priority and fixed STR

6. individualized prior plus fixed question order \(a\)-stratified;
7. Compare with condition 4 to identify whether the fixed "low first and then high" will actually lose information under the accurate prior.

### Level 4: Add a new mechanism for this item

8. Individualized prior plus posterior-variance-adaptive \(a\) layer;
9. Add the minimum number of questions, the lower limit of prior variance and conflict fallback;
10. Combine orthogonally with Sympson–Hetter or other exposure control.

Finally, compare under the same stopping rule:

\[
SE(\widehat\theta)\le\varepsilon,
\]

It also reports question volume, bias, RMSE, coverage rate, error early stopping, item bank exhaustion, exposure and overlap. In this way, the contribution of prior, the contribution of \(a\) layering and the interaction between the two can be separated.

## 13. Which novelty claims cannot be supported by this article?

It has been explicitly done:

- Low in early stage \(a\), high in late stage \(a\);
- In the current layer, \(b\) matches \(\widehat\theta\);
- Randomly select a question from the two closest candidates within the layer;
- Comparison with Fisher/Bayesian topic selection plus Sympson–Hetter;
- Simultaneous evaluation with MSE, Bias, exposure equalization and test overlap.

Therefore, it cannot be claimed that "it is the first time to propose early retention of high-discrimination questions" or "it is the first time to treat \(a\) and \(b\) separately."

Method increments that may still hold are:

> Use examinee's self-generated information to construct an individualized prior with uncertainty, and determine the \(a\) layer based on individual posterior uncertainty rather than a fixed question order; under error self-evaluation and exposure constraints, the system verifies when high \(a\) questions should be used early or postponed.

This is more specific than "put together the self-assessment starting point and \(a\)-stratified" and is easier to verify through ablation experiments.

## 14. Quote-safe Chinese paraphrasing

### Used to explain why high \(a\) questions may be mismatched early

> Chang and Ying (1999) pointed out that high-discrimination questions can fully realize their information advantages only when the item difficulty is close to the examinee's true ability; CAT's early ability estimate is unstable, so high-discrimination questions matched by the current estimate may provide little information at the true ability position.

### is used to introduce the original method

> \(a\)-stratified CAT stratifies the item bank from low to high distinction, and uses the corresponding levels in the test phase in sequence; within each layer, questions are selected based on the proximity of the item difficulty to the current ability estimate.

### Used to describe the exposure result

> In the three fixed length simulation conditions of Chang and Ying (1999), the hierarchical method reduced the imbalance of exposure distribution and the test overlap between examinee, and significantly reduced the items that were hardly used.

### Used to illustrate precision boundaries

> Hierarchical methods are not cost-free in all conditions: in a 20-question simulation using 254 real 3PLM parameter questions, the MSE for STR was .084, and for the Fisher informativeness plus Sympson–Hetter condition it was .060.

### Used to connect to this topic

> This method uses \(b\) for person-specific location matching and \(a\) for resource allocation across stages, but it does not use an individualized prior. A further question is whether the accuracy of an examinee's self-assessment and the posterior variance can determine when high-\(a\) items should become available.

## 15. Key References

- Chang, H.-H., & Ying, Z. (1999). *a*-stratified multistage computerized adaptive testing. *Applied Psychological Measurement, 23*(3), 211–222. [https://doi.org/10.1177/01466219922031338](https://doi.org/10.1177/01466219922031338)
- Chang, H.-H., & Ying, Z. (1996). A global information approach to computerized adaptive testing. *Applied Psychological Measurement, 20*(3), 213–229.
- Sympson, J. B., & Hetter, R. D. (1985). Controlling item-exposure rates in computerized adaptive testing. In *Proceedings of the 27th Annual Meeting of the Military Testing Association* (pp. 973–977).
- Weiss, D. J. (1973). *The stratified adaptive computerized ability test* (Research Report 73-3). University of Minnesota.

## 16. Judgment after reading

This paper provides the most direct theoretical and simulation support for the instructor's idea that high-\(a\) items should not be consumed at the outset, but that support has a clear condition: uncertainty about the early ability estimate makes high-\(a\) items easy to mistarget. It shows that fixed \(a\)-stratification can substantially improve overall exposure balance, but it neither proves that every item is protected nor investigates whether high-\(a\) items should become available earlier when self-assessment is accurate.

Therefore, the most interesting question of this item should not assume that "high \(a\) questions will be wasted early on", but should turn it into a testable interaction:

\[
\text{self-assessment accuracy}
\times
\text{prior variance}
\times
\text{current a posteriori uncertainty}
\longrightarrow
\text{high}a\text{The actual information return and exposure cost of the question}.
\]

If the results show that accurate, narrow, and well-calibrated priors can be safely explored early with high \(a\), while erroneous or ambiguous priors need to be explored first with low \(a\), then the contribution is not to repeat the fixed stratification of 1999, but to give a CAT method in which the timing of discrimination configuration is determined by the quality of individual information.
