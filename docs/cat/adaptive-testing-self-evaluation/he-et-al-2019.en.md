# He et al. (2019): How self-narrative becomes an individualized prior for PTSD measurement

!!! abstract "Key takeaway"
    **What they did:**He et al. converted the trauma self-narrative into a continuous text score, then constructed an individualized normal prior through latent regression, and combined it with the 2PL IRT likelihood of 21 PTSD items. **What was obtained:** In the 99-person sample, the classification accuracy of 21 questions increased from .94 to .97 after adding text; based on the average posterior standard error comparison, 17 questions with text and 21 questions without text are close to each other. **Conclusion on this topic:** It directly proves that the examinee text can enter psychometrics prior, but the items are always sorted by the information amount of the common diagnostic cut-off point, and everyone has the same order. Therefore, there is no proof that the text prior can improve individualized CAT topic selection or real early stopping.

## Citation details

> He, Q., Veldkamp, B. P., Glas, C. A. W., & van den Berg, S. M. (2019). Combining text mining of long constructed responses and item-based measures: A hybrid test design to screen for posttraumatic stress disorder (PTSD). *Frontiers in Psychology, 10*, 2358. [DOI](https://doi.org/10.3389/fpsyg.2019.02358)

- Research type: Real data method research
- Measurement objectives: Potential severity and screening classification of posttraumatic stress disorder (PTSD)
- Supporting information: Examinee’s own narrative of traumatic experiences and symptoms
- Core model: text classification score \(\rightarrow\) individualized normal prior \(\rightarrow\) two-parameter Logistic IRT posterior
- Key result: The classification accuracy of 21 questions increased from 0.94 to 0.97; the average posterior standard error curve shows that 17 questions plus text prior is close to 21 questions without prior

!!! warning "The most likely place to misread"
    The author calls adding item information item by item adaptive, but the amount of information here is always calculated at the common diagnostic cut-off point \(\theta_c=-0.15\), rather than each person's current posterior position. All examinees accept the same item order. What is truly individualized is the ability prior and posterior estimation, not item selection.

## 1. Research what problem you want to solve

The researchers wanted to put two types of information into the same PTSD screening process:

1. **Unstructured information: **examinee’s freely written traumatic experiences and related symptoms;
2. **Structured information:** 21 dichotomous questions on PTSD symptoms.

They asked two questions:

- Can the combination of text and item responses be more accurate in distinguishing PTSD from non-PTSD than using questionnaire alone?
- Can text serve as a kind of routing information, allowing shorter item sequences to achieve estimation accuracy similar to that of a complete questionnaire?

Therefore, this is not a self-evaluation in the traditional sense of “asking how anxious you are first”, but rather:

\[
\text{examineeself-narrative}
\longrightarrow
\text{machine learning text score}
\longrightarrow
p(\theta\mid\text{text})
\longrightarrow
\text{IRT posterior}.
\]

## 2. Sample, reference diagnosis and two types of answers

105 trauma survivors were initially recruited from an online forum for people with mental health problems. After excluding 2 persons who did not experience the listed traumatic events and 4 persons with missing narratives, the final sample was:

\[
N=99,
\]

Among them:

- PTSD: 34 people;
- Non-PTSD: 65 people;
- Age range: 19 to 63 years, mean 30.06 years, standard deviation 11.30;
- 78.4% female;
- More than 90% have college or higher education background.

The examinee first reported whether they had been diagnosed with PTSD by a psychiatrist through a structured interview, and the paper then used this label as the true standard for classification comparisons. Note: This study did not re-conduct an independent clinical diagnosis on 99 people; the reference label comes from Examinee's report of previous professional diagnosis.

### self-narrative

The examinee is asked to describe the traumatic event and its symptoms, the recommended length is over 150 words.

### 21 structured items

The item comes from the PTSD screening part of the National Comorbidity Survey Replication (NCS-R) and corresponds to the symptom standards of the Diagnostic and Statistical Manual of Mental Disorders, Fourth Edition (DSM-IV). It adopts a "yes/no" dichotomous response.

The item parameters are not recalibrated on the current 99 people, but are taken from the previous NCS-R sample:

\[
N_{\mathrm{calibration}}=880.
\]

This is an advantage of the design: the current hybrid model uses fixed item parameters that are externally calibrated, and the items are not recalibrated simultaneously with the same small sample.

## 3. Approach 1: Only IRT questionnaire

The authors have previously compared Rasch models, single-dimensional two-parameter logistic models (2PLM), and three-dimensional models. The likelihood ratio test is more biased towards the three-dimensional model, but the item-oriented Lagrange multiplier test shows that there is no significant item mismatch between the single-dimensional 2PLM and the multi-dimensional model, and the effect sizes are similar. For parsimony, a single-dimensional 2PLM was ultimately adopted.

For item \(i\) and examinee \(n\):

\[
P(X_{ni}=1\mid\theta_n)
=
\frac{
\exp\{\alpha_i(\theta_n-\beta_i)\}
}{
1+\exp\{\alpha_i(\theta_n-\beta_i)\}
}.
\]

Where \(\theta_n\) represents the potential severity of PTSD, \(\alpha_i\) is the discrimination, and \(\beta_i\) is the symptom severity position.

The external calibration parameter range for 21 questions is:

- \(\alpha_i\in[0.78,1.86]\), average about 1.32;
- \(\beta_i\in[-4.45,1.22]\), average about \(-0.99\).

The IRT-only condition uses expected a posteriori estimation (expected a posteriori, EAP) and assumes a standard normal ability distribution.

## 4. Approach 2: Only text classification

### The text model is not trained from scratch on the current 99 people

This paper follows the product score model (PSM) established by He et al.’s early research. The original training materials include 300 self-narratives, including 150 for PTSD and 150 for non-PTSD. The current study uses 1,000 previously screened unigram features and an established text processing pipeline.

Preprocessing includes:

- Remove numbers, punctuation, stop words and common abbreviations;
- Use Porter stemming to normalize word forms;
- Compute unigram features in the input narrative.

### Product score model How to score

Let \(C_1\) be the PTSD text corpus, and \(C_2\) be the non-PTSD corpus. For keywords appearing in the input text, PSM calculates respectively:

\[
S_1
=
P(C_1)
\prod_{w=1}^{k}
\frac{u_w+a}{\operatorname{len}(C_1)},
\]

\[
S_2
=
P(C_2)
\prod_{w=1}^{k}
\frac{v_w+a}{\operatorname{len}(C_2)},
\]

Among them, \(u_w\) and \(v_w\) are the frequencies of the keyword \(w\) in the two corpora, and the smoothing constant is set to \(a=0.5\).

Personal text score is defined as:

\[
y_n
=
\log\frac{S_1}{S_2}.
\]

When \(y_n>0\), the text model is classified as PTSD; otherwise, it is classified as non-PTSD. In order to connect with the standard normal scale of IRT, the text score of the current sample is then standardized.

!!! note "In what sense is this 'self-information'"
    The information is indeed generated by the examinee himself, but what ultimately enters the model is not its explicit self-evaluation, but the risk score extracted from the narrative words by the supervised learning algorithm. Therefore, what it proves is that "self-generated data can form a prior" rather than "examinee can accurately choose his own ability or symptom level."

## 5. Approach 3: text score becomes individualized prior

The author establishes latent regression:

\[
\theta_n
=
b_0+b_1y_n+\varepsilon_n,
\qquad
\varepsilon_n\sim N(0,\sigma^2).
\]

So:

\[
\theta_n\mid y_n
\sim
N(b_0+b_1y_n,\sigma^2).
\]

It serves as an individualized prior to IRT:

\[
p(\theta_n\mid\mathbf x_n,y_n)
\propto
p(\mathbf x_n\mid\theta_n,\alpha,\beta)
g(\theta_n\mid y_n).
\]

In the current data of 99 people, it is estimated that:

\[
\widehat b_0=-0.41,
\qquad
\widehat b_1=1.44,
\qquad
\widehat\sigma^2=3.57.
\]

Therefore:

\[
\theta_n\mid y_n
\sim
N(-0.41+1.44y_n,3.57).
\]

The a priori standard deviation is approximately:

\[
\sqrt{3.57}\approx1.89,
\]

So it's not a particularly narrow strong prior. The text primarily moves the personal a priori center while retaining considerable uncertainty.

Posteriors were estimated via WinBUGS, each running 5,000 Markov chain Monte Carlo (MCMC) iterations, with the first 1,000 as burn-in. The paper does not report multi-chain convergence diagnosis, \(\widehat R\) or effective sample size.

## 6. What is the so-called adaptive item administration?

The authors used the diagnostic cut-off points previously determined on the NCS-R sample of \(N=880\):

\[
\theta_c=-0.15.
\]

Then calculate the amount of information at the common tangent point for each question:

\[
I_i(\theta_c)
=
\alpha_i^2
P_i(\theta_c)
\{1-P_i(\theta_c)\},
\]

Then arrange the 21 questions into a fixed sequence from high to low according to \(I_i(\theta_c)\). The first question is C6, followed by B5, C4, B3, etc., up to all 21 questions.

Research comparison:

\[
\text{before}k\text{Fixed sorting question},
\qquad
k=1,\ldots,21,
\]

The average posterior standard error under the two estimation methods "with text prior" and "without text prior".

### Why this is not a personalized CAT

|Truly personalized CAT|He et al. (2019)|
|---|---|
|Calculate the selection target on the individual's current \(\widehat\theta_{n,k}\) or posterior|Always calculate the amount of information at the common tangent point \(-0.15\)|
|Different people's early reactions may lead to different next questions.|Everyone uses the same presort|
|prior can change the actual item sequence|The prior only changes the posterior estimate and does not change the item order.|
|Re-select the remaining optimal questions at each step|Just gradually increase the prefix length over a fixed sequence|

Its more accurate name is: Fixed short list sequence optimized by diagnostic cut points + individualized text prior.

## 7. Classification results of three methods

Paper comparison:

1. IRT-only: 21 questions;
2. Text-only: PSM text classification;
3. Hybrid: text prior + IRT posterior of 21 questions.

### Correlation between three types of scores

|two kinds of fractions|Related|
|---|---:|
|IRT and Text| 0.56 |
|IRT and Hybrid| 0.99 |
|Text and Hybrid| 0.62 |

The correlation between Hybrid and IRT is as high as 0.99, indicating that when using the complete 21 questions, the hybrid score is still mainly determined by the structured items; the text provides a small but potentially useful correction.

### Classification performance

|method| Accuracy | Sensitivity | Specificity | PPV | NPV |
|---|---:|---:|---:|---:|---:|
| IRT-only | 0.94 | 1.00 | 0.92 | 0.87 | 1.00 |
| Text-only | 0.84 | 1.00 | 0.77 | 0.69 | 1.00 |
| Hybrid | 0.97 | 1.00 | 0.95 | 0.92 | 1.00 |

Among them, PPV and NPV are positive predictive value (positive predictive value) and negative predictive value (negative predictive value) respectively.

In the sample:

- IRT-only misclassified 6 people;
- Hybrid misclassified 3 people.

Therefore, the author interprets the decrease in the number of misclassifications as a 50% reduction. This relative percentage sounds large, but the absolute difference is only 3 people, and the total sample is only 99 people. It cannot be regarded as a stable external validity conclusion.

## 8. How to obtain the evidence of “4 less questions”

As the fixed sequence increases topic by topic, the paper reports the average posterior standard error:

- No text prior: approximately dropped from 1.6 for question 1 to 0.68 for question 21;
- With text prior: approximately dropped from 1.4 for question 1 to 0.65 for question 21.

The difference between the two curves shrinks from about 0.20 to about 0.03, which is consistent with the rule of "the more items there are, the weaker the relative impact of priority."

The author plots the average standard error level for the no-prior, 21-question condition, and finds that it intersects with the "with prior" curve at approximately 17 questions. Therefore it is proposed:

\[
17\text{question + text prior}
\approx
21\text{question + no text prior}
\]

Can use 4 fewer questions while maintaining similar accuracy.

!!! warning "The 'same accuracy' here is just that the average posterior standard error is similar"
    The paper does not report the accuracy, sensitivity, specificity, PPV or NPV of the 17-question Hybrid, nor does it compare bias, RMSE, interval coverage rate or individual-level stopping results. Therefore, "4 fewer questions without loss of accuracy" is stronger than the original evidence; a more rigorous statement is that "the average posterior standard error of 17 questions Hybrid is close to 21 questions IRT-only".

## 9. Which evidence is solid and which needs to be retained?

### The more solid part

- item parameters come from independent \(N=880\) sample;
- The keyword system of the text classifier comes from earlier independent corpus, rather than training from scratch on the current 99 people;
- The same group of 99 people provided both narrative and item responses, allowing the two data to be combined at the individual level;
- The paper clearly provides prior regression, classification indicators and question-by-question average standard error curves.

### Parts that need to be retained

1. **The sample is small and unrepresentative. **Only 99 people, mostly female and highly educated, from mental health online forums.
2. **The reference label is not a clinical diagnosis reimplemented in this study. **Examinee reports his or her previous psychiatric diagnosis, which is then used as the true standard in the paper.
3. **Hybrid mapping uses the same 99 people as the effect evaluation. **The text classifier comes from external research, but \(b_0,b_1,\sigma^2\) is estimated in the current sample, and the classification and standard errors are also reported in the same sample, without cross-validation or independent validation set.
4. **After adding prior, the posterior standard error decreases and has an internal component in the model. **Additional information will inevitably increase the accuracy of the model; the real key is whether the prior is calibrated correctly in new samples, and the paper does not report coverage rate.
5. **No errors in prior experiments. **The consequences of textual misjudgment, language style differences, educational differences, or deliberate concealment have not been examined.
6. **Provincial questions do not equal the total provincial burden. **Examinee also needs to write a sensitive narrative of at least about 150 words; the author himself admits that writing time needs to be factored into cost-effectiveness.
7. **No item exposure analysis. **If everyone uses the same sorting, it may make the first few questions highly exposed.

## 10. What does the paper really prove?

It directly supports:

1. Exame’s self-generated long text can be converted into personal scores through the supervised text model;
2. The score can be constructed into an individualized experience prior of IRT ability through latent regression;
3. In the current sample of 99 people, after combining the text prior with the complete questionnaire, the number of misclassified people was reduced from 6 to 3;
4. The impact of text prior on the average posterior standard error is more obvious when there are fewer items;
5. The average posterior standard error of the 17-question Hybrid is close to that of the 21-question IRT-only.

It does not directly prove:

- Self-reporting a symptom level can achieve the same effect;
- Text prior can drive personalized CAT topic selection;
- The classification accuracy of the 17-question Hybrid is the same as that of the complete 21 questions;
- The same benefits remain among new examinee or other language, education and gender groups;
- Wrong or overly strong text prior will not cause missed diagnosis;
- This method reduces the total completion time or total mental load;
- This method has solved the item exposure problem.

## 11. Impact on the novelty of our research

This paper invalidates the following novelty claims:

> For the first time, the information generated by examinee itself is converted into individualized prior in psychometrics.

Because it's done:

\[
\text{self-narrative}
\longrightarrow
y_n
\longrightarrow
N(b_0+b_1y_n,\sigma^2)
\longrightarrow
p(\theta_n\mid\mathbf x_n,y_n).
\]

But it doesn't finish:

\[
p(\theta_n\mid\mathbf x_{n,1:k},y_n)
\longrightarrow
\text{Personalized choice for next question}.
\]

Therefore it is still possible to study:

- Explicit user self-assessment or difficulty selection instead of NLP risk scores;
- prior simultaneously drives real question-by-question;
- Returns and risks under different prior variances;
- How to combine prior with low \(a\) starting, \(b\)-matching and first question randomization;
- The real question volume distribution under the same precision stopping rule;
- Error prior, risk of missed diagnosis, coverage rate and condition exposure.

!!! important "The most accurate expression of novelty"
    The possible contribution is no longer "putting self-generated information into the prior", but "putting the examinee's self-evaluation signal, calibrable prior strength, truly personalized early topic selection and exposure protection into a CAT framework that can ablate and test error priors".

## 12. Direct implications for experimental design

### Training mapping must be separated from effect evaluation

If we use the self-evaluation \(s_i\) construct:

\[
\theta_i\mid s_i
\sim
N(\mu(s_i),\tau^2(s_i)),
\]

You cannot fit \(\mu(\cdot),\tau^2(\cdot)\) on the same group of people and treat CAT returns as external performance. At a minimum it should be:

- Independent training set and test set; or
- cross-fitting / nested cross-validation; or
- Fix prior mapping on independent samples before performing CAT simulation.

### "Problem saving" must use the real stopping rule

You cannot just compare the intersection points of the average posterior standard error curves. Should be run person by person:

\[
\operatorname{Var}(\theta_i\mid\mathcal D_{i,t})
\leq
\varepsilon,
\]

It also reports the average question size, 95th percentile question size, error early stopping rate, bias, RMSE and coverage rate.

### Personalized topic selection must be certified separately

The comparison should be made explicitly:

1. All people are sorted according to the same diagnostic cut-off point;
2. Select topics with the maximum amount of information at the individual’s current posterior position;
3. Randomly select within the \(b\) region that matches the individual posterior;
4. Add \(a\)-stratified or posterior variance gate control.

Only in this way can we distinguish whether the income comes from the prior itself, the fixed short list sorting, or the truly personalized item path.

### The total burden should not only count items

If the self-assessment or narrative requires additional time, the total burden should be written as:

\[
T_{\mathrm{total}}
=
T_{\mathrm{self\ info}}
+
T_{\mathrm{items}}.
\]

Having 4 fewer questions doesn’t automatically mean it’s faster or easier overall.

## 13. Chinese paraphrasing that can be safely included in the paper

### examinee self-produced information enter prior

> He et al. (2019) converted the examinee's trauma self-narrative into text score, then constructed the individualized normal prior of the PTSD latent trait through latent regression, and combined it with the IRT questionnaire likelihood.

### Classification performance

> Among the 99 people sampled in this study, the classification accuracy of the complete 21-question questionnaire was 0.94, and after adding the text prior, it was 0.97; due to the difference, 6 people and 3 people were misclassified, which still needs to be verified in an independent large sample.

### Question size result

> The average posterior standard error of the text prior plus 17 pre-sorted questions is approximately equal to the average posterior standard error of the complete 21 questions without the text prior; the paper does not report the classification accuracy or coverage rate under the condition of 17 questions (He et al., 2019).

### Topic Boundary

> This study predetermines the same item order for everyone based on the amount of information at the common diagnosis cut-off point. The text prior does not participate in individualized real-time topic selection, so it does not belong to prior-driven CAT item selection (He et al., 2019).

## 14. Conclusion after intensive reading

He et al. (2019) is a direct precedent for "examinee self-generated information \(\rightarrow\) individualized prior" and is also an adjacent work that must be recognized in this topic. But it limits personalization to the estimation level: items are still uniformly sorted according to diagnostic cut-off points shared by all.

The most important inspiration for us is: **External signals enter prior, prior improves short test accuracy, and prior drives personalized topic selection. These are three different levels of propositions, and ablation conditions must be set separately for verification. **

---

**Topic navigation:**[Return to reading list](index.md) · [Previous article: Matteucci and Veldkamp (2009)](matteucci-veldkamp-2009.md)
