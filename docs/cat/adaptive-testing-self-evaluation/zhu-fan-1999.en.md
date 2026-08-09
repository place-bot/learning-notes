# Zhu and Fan (1999): Use individualized starting questions to disperse item bank exposure

!!! abstract "Key takeaway"
    **What they did:** Zhu and Fan used course experience and grade point average to predict ability position, selected only the first question based on this, and then resumed the same CAT update, content balancing, exposure control, and question selection process. **What is gained:** The individualized starting point disperses the use of first questions from around medium difficulty to a wider range, but does not steadily shorten the test; the auxiliary information is not timely, the exposure peak will shift to both ends of the item bank, and the estimated quality may also decrease. **Conclusion on this topic:** This article mainly demonstrates that individualized first questions can be reallocated for item bank use, but does not prove that prior information will accelerate convergence; first question dispersion and measurement efficiency must be evaluated as two independent results.

## Citation details

> Zhu, D., & Fan, M. (1999, April). *Adjusting computer adaptive test starting points to conserve item pool*. Paper presented at the Annual Meeting of the American Educational Research Association, Montreal, Canada. ERIC ED429997.

- [ERIC full text PDF](https://files.eric.ed.gov/fulltext/ED429997.pdf)
- Research type: Computerized adaptive testing (CAT) simulation based on actual large-scale mathematics test data
- Simulation sample: Randomly select \(N=2{,}000\) from approximately 30,000 examinees
- Core comparison: Common medium difficulty starting point, average grade starting point, combined course and average grade starting point

## 1. What the paper wants to solve is not the cold start accuracy, but the item bank consumption.

When standard CAT does not have any individual information, it usually starts from a common mid-ability position and then selects the most informative item near that position. The authors note that this approach has two potential costs:

1. For examinees whose abilities are at both ends of the item bank, the first one or two questions may be too easy or too difficult, and the information provided is limited;
2. A large number of examinees start from the same position, and a few items near the medium difficulty level will be used repeatedly as the first question.

There is a view that as long as the CAT is long enough, the starting point bias will eventually be corrected by subsequent answers, so the first question is not important. This article does not deny this long-term correction, but changes the question to:

> Even if the final ability estimate is not significantly affected, if everyone starts from the middle, is it still wasting early items and exacerbating the exposure of middle items?

Therefore, the main goal of this article is item bank utilization and exposure control, not to prove that individualized starting points can shorten the test.

## 2. Which step of CAT did the paper modify?

This article only uses auxiliary information to determine the difficulty level of the first question. After examinee answers the first question, the system resumes the same ability update, content balancing, exposure control and subsequent topic selection process.

```text
No-Info: Common Middle Position -> Select the first question -> Standard CAT
GPA: Grade point average mapped to ability position -> Select first question -> Standard CAT
Course&GPA: Courses and grade point averages are mapped to competency positions -> Select the first question -> Standard CAT
```

This is not Self-Adapted Testing: examinee does not choose difficulty on a question-by-question basis. It is also not a complete individualized Bayesian prior: the paper only clearly reports the adjustment of the starting position of the first question, and does not explain how to construct the auxiliary information into an individualized prior distribution that continues to participate in the posterior update.

!!! note "Bayesian provisional estimate does not mean that this article has changed prior"
    The simulation uses the Bayesian method to calculate a temporary ability estimate during the test, and finally uses maximum likelihood estimation (MLE) to report ability. However, the paper does not explain what prior is used for Bayesian estimation, what is the prior mean and variance, nor does it explain that GPA or Course&GPA enters the prior. Therefore, the safest interpretation is still that the auxiliary information only determines the first question, rather than continuing to enter the posterior.

## 3. How to obtain the initial position from the auxiliary information

### Raw data

Data come from the actual administration of a large-scale standardized mathematics test. There are nine test formats, each containing six content areas and 60 independent multiple choice questions. The item was modeled using a three-parameter logistic model (3PL) and calibrated between the nine test papers using BILOG.

When registering, examinee self-report the mathematics courses taken in high school and the corresponding scores. Possible courses include Algebra I, Algebra II, Geometry, Trigonometry, Calculus, and others above Algebra II.

### Two background indicators

The **GPA indicator** is the average of grades in all math courses taken.

**Course&GPA indicators** also utilize:

- Average scores in Algebra I, Algebra II and Geometry;
- Number of mathematics courses taken;
- Regression relationships between these variables and actual math test performance.

The author then maps each person's GPA or Course&GPA position in their respective distributions to the position in the ability distribution to form the initial ability level used to select the starting questions.

In the result, the correlation between GPA and reference ability is about \(0.578\), and the correlation between Course&GPA and reference ability is about \(0.695\). This means that Course&GPA contains a stronger signal of ability, but is still far from an error-free measure.

## 4. How to set up CAT simulation

### test length and stopping rule

The authors simulated two types of CAT:

1. fixed length: 15 questions and 30 questions;
2. Variable length: minimum 10 questions, maximum 45 questions.

variable length CAT uses two inferior variance stopping criteria:

|Accuracy conditions|Stop criteria|Equivalent correlation of paper annotations|
|---|---:|---:|
|High precision| \(PV\leq0.0625\) | \(r\approx0.97\) |
|low precision| \(PV\leq0.1500\) | \(r\approx0.92\) |

Here \(PV\) is the posterior variance, which is the variance of the current posterior distribution. The paper gives equivalent correlations, but does not expand on the specific conversion process.

### Content balance and exposure control

Each examinee receives the same proportion of items in the six content areas as the traditional paper-and-pencil test.

Item exposure was controlled using [Sympson–Hetter (1985) method](sympson-hetter-1985.md). The author simulated two levels of exposure control:

- \(0.90\): The restrictions are very loose;
- \(0.10\): Very restrictive.

### ability estimate

- Temporary ability estimate after each question: Bayesian method;
- Final ability estimate after the test: MLE;
- Reference standard: ability scores obtained from actual mathematics tests;
- Primary accuracy metric: Correlation of reference ability with simulated CAT ability estimate.

The paper does not fully report the priori of the temporary Bayesian estimation, the specific item selection function, the extreme reaction mode processing method, and all the details of the simulation answer generation. Therefore, it is impossible to reproduce the entire CAT engine item by item based on this article alone.

## 5. What happened when the first question was exposed?

The result of the first question given in Table 1 most directly reflects the contribution of this article:

|exposure control|starting point method|The number of items actually used as the first question|First question \(b\) range|The range of times used for a single first question|
|---:|---|---:|---:|---:|
| 0.90 | No-Info | 2 |\(-0.198\) to \(-0.067\)|219 to 1781|
| 0.90 | GPA | 12 |\(-2.038\) to \(1.988\)|1 to 475|
| 0.90 | Course&GPA | 12 |\(-2.038\) to \(1.988\)|14 to 469|
| 0.10 | No-Info | 29 |\(-0.436\) to \(0.429\)|2 to 199|
| 0.10 | GPA | 60 |\(-2.038\) to \(1.988\)|1 to 425|
| 0.10 | Course&GPA | 66 |\(-2.038\) to \(1.988\)|1 to 137|

Under loose exposure control, the No-Info method allowed 1,781 out of 2,000 people to use the same first question. GPA and Course&GPA divide the first question into 12 items of different difficulty.

Strict exposure control itself has forced No-Info to use more first questions, but its 29 first questions are still concentrated around medium difficulty. Course&GPA uses 66 first questions and reduces the maximum number of single questions to 137.

### Why GPA alone creates a spike at the difficult end

Many examinees report a GPA of 4.0, causing the GPA distribution to be stacked at the upper end. After mapping to the ability scale, many people are sent to the same difficult starting point. One parameter is

\[
a=2.3166,\qquad b=1.9879,\qquad c=0.1295
\]

The item is therefore frequently used as the first question.

After Course&GPA is added to the number of courses, the impact of GPA accumulation at the upper end is alleviated. This shows that the auxiliary information can disperse the exposure from the middle of the item bank, or it may just create new concentrated exposure at the end of the item bank.

!!! warning "The text is inconsistent with Table 1 and Figure 2"
    The text states that under \(0.10\) exposure control, No-Info uses 5 first questions, with a maximum of 997 times; Table 1 reports 29 questions, with a maximum of 199 times, and the vertical axis and column of Figure 2 also support a maximum of about 199 times. This site organizes the results according to Table 1 and Figure 2, while retaining this internal inconsistency. Do not mix 5/997 in the text with 29/199 in the table.

## 6. fixed lengthresult: exposure improvement is more stable than accuracy improvement

Next, select the most easily comparable result in Table 2. In parentheses are the correlation between the reference ability and the CAT estimate, and the highest number of single questions used.

|test conditions| No-Info | GPA | Course&GPA |
|---|---:|---:|---:|
|15 questions, exposure 0.90| \(0.944;\ 1781\) | \(0.918;\ 1144\) | \(0.948;\ 1182\) |
|15 questions, exposure 0.10| \(0.934;\ 240\) | \(0.903;\ 445\) | \(0.934;\ 365\) |
|30 questions, exposure 0.90| \(0.972;\ 1814\) | \(0.970;\ 1249\) | \(0.973;\ 1269\) |
|30 questions, exposure 0.10| \(0.963;\ 514\) | \(0.954;\ 468\) | \(0.960;\ 509\) |

You can see:

- Under loose exposure control, Course&GPA significantly reduces the maximum number of single questions used, while maintaining a close correlation with No-Info;
- Strict exposure control has taken on a large number of scattered tasks, and the additional advantages of Course & GPA have been significantly reduced;
- Under the conditions of 15 questions and exposure control 0.10, the highest number of single questions used in Course&GPA is higher than that in No-Info;
- Correlations were generally lowest with GPA alone, indicating that inaccurate auxiliary variables harm short tests.

!!! note "Times in the original text should be understood as the difference in times, not multiples"
    The text states that the average usage of No-Info under the condition of 15 questions is "around 50 times more", and also says that the maximum usage differs by about 600 times. Table 2 actually shows that the average number of uses is about \(303-250=53\) times and the maximum number of uses is about \(1781-1182=599\) times, not 50 times and 600 times. This should read "about 50 times more" and "about 600 times more."

## 7. variable lengthresult: it does not make CAT stable to stop earlier

Table 3 also reports average test length and capability correlation:

|posterior variance threshold|exposure control| No-Info | GPA | Course&GPA |
|---:|---:|---:|---:|---:|
| 0.0625 | 0.90 | \(23.2;\ 0.964\) | \(23.3;\ 0.906\) | \(23.9;\ 0.963\) |
| 0.0625 | 0.10 | \(36.1;\ 0.958\) | \(34.3;\ 0.947\) | \(35.6;\ 0.961\) |
| 0.1500 | 0.90 | \(10.2;\ 0.907\) | \(11.1;\ 0.871\) | \(11.3;\ 0.914\) |
| 0.1500 | 0.10 | \(13.0;\ 0.903\) | \(14.2;\ 0.877\) | \(14.6;\ 0.913\) |

Each cell is "Average number of questions; ability related".

Most notable are the low-precision, short-test conditions:

- When exposure is 0.90, Course&GPA has on average \(1.1\) more questions than No-Info, and the correlation is \(0.914\) versus \(0.907\);
- At exposure 0.10, Course&GPA has on average \(1.6\) more questions than No-Info, and the correlation is \(0.913\) versus \(0.903\).

The authors call these two slightly higher correlations exceptions, since there are few stable differences between No-Info and Course&GPA in most other conditions. However, these two related advantages may only be caused by one or two more questions in Course&GPA, and cannot be explained as higher estimation efficiency under the same number of questions.

High-precision conditions also have no consistent advantage in question volume: Course&GPA has more \(0.7\) questions under loose exposure control, and fewer \(0.5\) questions under strict control. The overall conclusion is:

> What the individualized starting question stably improves is the exposure pressure between the starting point and the item bank, rather than the average test length.

## 8. Why does No-Info look more even under strict exposure control?

Under the strict exposure control of \(0.10\), the most informative items in the middle are constantly rejected for testing, and the algorithm can only turn to more alternative questions. This will spread the usage of No-Info items to a larger difficulty range, so the overall distribution looks more even than with loose control.

But "more uniform" does not mean "not heavier in the middle." The No-Info examinee still starts from the common middle position, so the usage of items in the middle third is still relatively high.

GPA and Course&GPA send people to different difficulty positions, reducing the concentration in the middle area. However, they may form higher single-question peaks at the high or low difficulty end due to the accumulation of self-reported distributions and fewer candidate questions at the tail. This is why, in addition to overall exposure, you should also report:

- Conditional exposure grouped by true ability;
- Conditional exposure rate grouped by self-assessment grade;
- test overlap between different examinees.

This article does not provide indicators of these conditions.

## 9. What conclusions can this paper support?

### Better supported conclusion

1. Everyone starts from a common midpoint, which will cause a small number of moderately difficult questions to be highly concentrated;
2. Effective auxiliary information can disperse the first question into a wider \(b\) range;
3. The individualized starting point can improve some item bank utilization indicators without significantly reducing capacity correlation;
4. The quality of auxiliary information determines the effect, and Course&GPA is significantly more stable than GPA alone;
5. Standard exposure control and individualized starting points can have different but interacting effects.

### Conclusions that cannot be derived from this article

1. The individualized starting point will shorten the CAT;
2. Putting self-reported information into Bayesian prior must be effective;
3. Let examinee actively choose the difficulty, which will produce the same result;
4. Higher correlation must come from a better starting point, not more items;
5. Reduced overall exposure means protection within each ability or self-assessment group.

## 10. Research design and reporting limitations

### The reference capability is not a truly known latent trait

The paper uses proficiency scores from actual math tests as a reference and then calculates how this correlates with simulated CAT estimates. This reference score itself also contains measurement error and is not equivalent to the true \(\theta\) known in the simulation study.

### Self-reported average grades are not equivalent to direct self-assessment of current abilities.

GPA and number of courses are proxy variables for educational background. They are not the same as “Where do I think I am right now?” and do not include what Wise et al. call present-moment anxieties, motivations, and subjective states.

### The individualized information only affects the first question

This article cannot answer: After constructing the same information into prior mean and prior variance, how will the entire posterior path and stopping rule change.

### Starting point quality and test length are confused with each other

Under the low-precision condition, the correlation of Course&GPA is slightly higher, and the question volume is also longer. The paper does not compare methods under the same actual number of questions or the same actual root mean squared error.

### Strong exposure control does not completely eliminate local spikes

Even if the nominal exposure control is set to \(0.10\), the GPA condition will still focus on using difficult questions due to a large number of 4.0 self-reports. Overall Sympson-Hetter controls do not guarantee equal protection within each self-assessment group.

### Key algorithm details are incomplete

Priors for Bayesian tentative estimates, specific topic selection criteria, and several simulation details are not reported, limiting reproducibility.

## 11. Its relationship with the methods of this topic

|Dimensions| Zhu and Fan（1999） |Methods for preparing research for this topic|
|---|---|---|
|individual information|Self-reported courses and grade point average|User-selected difficulty level and its reliability|
|initial position|Map as starting ability point|Construct \(N(\mu_c,\tau_c^2)\) individualized prior|
|Question 1|Select topics corresponding to ability positions|Identify candidate regions using \(b\) matching|
|Processing of \(a\)|No separate management|Decide which \(a\) layer to open based on a priori or a posteriori uncertainty|
|Exposure dispersion|Mainly rely on starting point difference and Sympson-Hetter|Exposure-aware random selection among candidates of approximately equal quality|
|Follow-up CAT|Resume standard CAT after first question|The main analysis also changes only the first question; the extended analysis lasts up to a very small \(k\)|
|main goal|Reduce exposure of middle items|Find a better balance between accuracy, question volume and exposure|

The four most direct reminders this paper gives to this topic are:

1. **individualized is \(b\)**: the auxiliary information first determines which difficulty position of the item bank the examinee should start from;
2. **False signals can shift rather than eliminate exposure**: intermediate pressure may turn into tail spikes;
3. **Only changing the first question may not shorten the test**: The number of questions must be used as an independent result test;
4. **Don’t just look at the overall exposure**: You must also check the maximum exposure, conditional exposure and test overlap of the first question.

## 12. A straightforward follow-up ablation design

Based on this article and \(a\)-stratified CAT, you can compare in turn:

1. Standard prior \(N(0,1)\) + the first question with the largest amount of information;
2. Individualized prior \(N(\mu_c,\tau_c^2)\) + the first question with the largest amount of information;
3. Individualized prior + select the first question among the low \(a\) candidate questions matching \(b\);
4. Individualized prior + determine the low, medium or high \(a\) layer based on \(\tau_c^2\), and then randomly select from several questions that are close to \(b\) and currently have low exposure.

The main analysis only changed the first question to maintain comparability with Zhu and Fan and the instructor's current assumptions. A very small extended analysis can allow the hierarchical rule to continue until the posterior variance is below the threshold, but at most three questions, thus avoiding the need to cross-simulate all \(k=1,2,3,4,\ldots\).

It is necessary to report at the same time: average number of questions, bias, root mean squared error (root mean square error, RMSE), coverage rate, maximum exposure rate of the first question, effective item bank size of the first question, conditional exposure rate according to self-assessment grade, and test overlap. Only if the number of questions is smaller with the same actual accuracy, or the exposure is more balanced with the same accuracy and number of questions, can it be said that the new method has brought about real efficiency gains.

## References

- Green, B. F., Bock, R. D., Humphreys, L. G., Linn, R. L., & Reckase, M. D. (1984). Technical guidelines for assessing computerized adaptive tests. *Journal of Educational Measurement, 21*(4), 347-360.
- Hambleton, R. K., Zaal, N. J., & Pieters, J. P. M. (1991). Computerized adaptive testing: Theory, applications, and standards. In R. K. Hambleton & N. J. Zaal (Eds.), *Advances in educational and psychological testing: Theory and applications* (pp. 341-366). Kluwer Academic Publishers.
- Hulin, C. L., Drasgow, F., & Parsons, C. K. (1983). *Item response theory: Application to psychological measurement*. Dow Jones-Irwin.
- Lord, F. M. (1980). *Applications of item response theory to practical testing problems*. Lawrence Erlbaum Associates.
- Mislevy, R. J., & Bock, R. D. (1983). *BILOG: Item and test scoring with binary logistic models* [Computer program]. Scientific Software.
- Sympson, J. B., & Hetter, R. D. (1985). Controlling item-exposure rates in computerized adaptive testing. In *Proceedings of the 27th Annual Meeting of the Military Testing Association* (pp. 973-977).
- Wainer, H. (1990). *Computerized adaptive testing: A primer*. Lawrence Erlbaum Associates.
- Wainer, H., & Kiely, G. L. (1987). Item clusters and computerized adaptive testing: A case for testlets. *Journal of Educational Measurement, 24*, 185-201.
