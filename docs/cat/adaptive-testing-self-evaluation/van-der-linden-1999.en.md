# van der Linden (1999): individualized empirical initialization complete intensive reading notes

!!! abstract "Key takeaway"
    **What was done:** van der Linden proposed latent regression and empirical Bayes methods to directly estimate \(p(\theta\mid X)\) from the pre-test auxiliary variables and the item-by-item responses of the calibrated item, avoiding the ability point estimation with measurement error as an error-free regression dependent variable. **What was gained:**A practical example shows that the individualized initial mean and conditional uncertainty can be generated during the pre-test response time, and can be used only for the first question routing, or as a complete Bayesian prior. **Conclusion for this topic:** The empirical initialization of auxiliary information construction is not a new idea, but this article does not run a comparative CAT to prove the provincial questions; it provides a statistical calibration framework that must be completed before the text or self-assessment enters the CAT.

## Citation details

> van der Linden, W. J. (1999). Empirical initialization of the trait (θ) estimator in adaptive testing. *Applied Psychological Measurement, 23*(1), 21–29. [https://doi.org/10.1177/01466219922031149](https://doi.org/10.1177/01466219922031149)

- Research type: Statistical methods paper with an example of real data
- Core question: How to transform the background information already mastered before the test into the individualized initial point or empirical prior of CAT
- Core model: latent regression (latent regression) plus empirical Bayesian initialization
- Supporting information in the example: the total answering time of the previous test, not the examinee self-assessment

!!! important "The most critical point of the whole article: the point estimate can be ignored, which does not mean that the error can be ignored"
    Mislevy and Wu (1988) distinguish two issues. For a completed CAT, if you only care about the maximum likelihood (ML) ability point estimate actually obtained by the examinee, when the ignorability condition is met, you do not need to multiply the probability of "why the system chose these questions" by the likelihood:

    \[
    \widehat\theta_{\mathrm{ML}}
    =
    \arg\max_\theta
    \prod_{t=1}^{T}
    P(U_t=u_t\mid\theta,J_t).
    \]

    The actual tested item \(J_t\) and its item parameters cannot be ignored here; what can be ignored is the probability of the topic selection mechanism itself, such as \(P(J_t\mid J_{1:t-1},U_{1:t-1})\). Selecting a difficult problem is often just the algorithm result of the previous correct answer, and is not a second evidence of ability independent of the previous answer.

    However, if you care about the sampling distribution of \(\widehat\theta\) in repeated tests—including standard error, bias, variance, root mean squared error, and confidence intervalcoverage rate—you cannot ignore the topic selection and stopping mechanisms. Because different early answers will produce different item paths, information amounts and test lengths.

    **Direct implications for this topic:** If the self-assessment only determines the first question and ML scoring is used in the end, the self-assessment does not have to be entered into the final score as an additional bonus item; if the self-assessment is structured as \(p(\theta\mid X)\) and used for Bayesian update, it has officially entered the ability inference, and this ML conclusion can no longer be cited to say "self-assessment is ignored".

## 1. First distinguish: which are the contributions of this article and which are the previous evidence

### van der Linden (1999) own main contribution

The paper assumes that the background variable vector is \(X=(X_1,\ldots,X_P)\), and establishes a latent regression model:

\[
\theta
=
\beta_0+\beta_1X_1+\cdots+\beta_PX_P+\varepsilon,
\qquad
\varepsilon\sim N(0,\sigma^2).
\]

Therefore, for the examinee whose background information is \(X=x\):

\[
\theta\mid X=x
\sim
N(x^\top\beta,\sigma^2).
\]

This distinction directly corresponds to the two CAT initialization methods:

1. **When only the initial point is needed**, let \(\widehat\theta^{(0)}=x^\top\widehat\beta\), and select the first question accordingly;
2. **When using Bayesian CAT**, use the complete \(N(x^\top\widehat\beta,\widehat\sigma^2)\) as an individualizedempirical prior. The background information will continue to affect subsequent estimation and topic selection through posterior updates.

The paper further rewrites the EM idea of Rigdon and Tsutakawa (1983) into the calibrated two-parameter logistic model (2PLM) and sparse CAT response data to directly estimate \(\beta\) and \(\sigma^2\). This avoids the need to first estimate each person's \(\widehat\theta\) and then perform ordinary regression on \(\widehat\theta\) with measurement errors.

### This is not a conclusion directly tested in this article.

This article does not set standard CAT comparison conditions, nor does it simulate or measure the number of questions, root mean squared error, coverage rate and exposure rate. Therefore it is **not directly proven**:

- Individualized initialization will inevitably shorten CAT;
- Self-reported information can accurately predict \(\theta\);
- The individualized prior must be better than the standard normal prior;
- The exposure problem caused by the same starting point has been solved by the examples in this article;
- Use background information to be fair in all quiz situations.

These are the theoretical reasons, statistical methods or research hypotheses that need to be tested in the paper, and cannot be written into the effect conclusions that have been obtained in this paper.

## 2. One-page citation evidence map

|The perspective used by van der Linden (1999)|main citation|The actual role of citations|subsequent citation strength|
|---|---|---|---|
|Traditional linear testing optimizes test information within expected ability ranges| Birnbaum（1968） |Item Response Theory (IRT) Information Function and Test Formulation Basics|background theory|
|CAT matches items one by one based on the current ability estimate.| Wainer（1990）；Thissen and Mislevy（1990） |The maximum amount of information in CAT and the Bayesian topic selection framework|background theory|
|Maximum likelihood and Bayesian estimates can converge to true capabilities under certain conditions| Chang and Ying（1996）；Gelman et al.（1995） |Support asymptotic convergence rather than guarantee fast or monotonic convergence in short tests|Conditional theoretical support|
|In actual CAT, there may be a large number of content and item dependency constraints.| van der Linden and Reese（1998） |Illustrating the realistic scale of constrained CAT; its LSAT example contains a large number of constraints|Direct methods and instance support|
|Short adaptive subtests can borrow information from earlier subtests to improve subsequent initialization| Brown and Weiss（1977）；Gialluca and Weiss（1979） |The closest early application to “predicting subsequent starting points using existing individual information”|direct precursor evidence|
|Starting from a common initial value will subject items near the starting point to concentrated exposure.|Theoretical argument by van der Linden (1999); control method provided by Sympson and Hetter (1985)|This article gives mechanistic inferences, but does not directly compare exposures in examples; empirical testing can be referred to Zhu and Fan (1999)|This article can be cited as a theoretical motivation, and it is not appropriate to write it as an empirical result.|
|Direct exposure control may sacrifice statistical information|Thomasson (1995), cited in van der Linden (1999)|Reports about 15% and up to about 40% information loss in certain simulations|Secondary, context-dependent evidence|
|Auxiliary information can be entered into IRT parameter and population distribution estimates| Mislevy（1988）；Mislevy and Sheehan（1989）；Sheehan and Mislevy（1990）；Mislevy et al.（1992） |Demonstrate that collateral information has a statistical tradition in IRT|Methodological Basis for Adjacency Problems|
|The adaptive topic selection mechanism can be ignored under specific goals.| Little and Rubin（1987）；Mislevy and Wu（1988） |Distinguish between value realized of point estimate and sampling distribution and standard error|Technical, borderline support|
|Use manifest variables to predict latent ability| Zwinderman（1991, 1997） |manifest predictors latent regression model; when \(a_i=1\) corresponds to the generalized Rasch model|The direct statistical basis of this article’s model|
|Use EM to estimate parameters directly from latent trait models| Rigdon and Tsutakawa（1983） |The source of the algorithm derived by EM in this article|direct calculation basis|
|Transforming variables and nonlinear terms can still maintain parameter linearity| Neter et al.（1990） |Regression modeling and variable transformation basis|General statistics background|
|Numerical integration can be performed using the Gauss–Hermite quadrature| Ralston and Rabinowitz（1983） |The source of the method for calculating points in this article|Numerical Computing Background|
|Response time in the previous test may predict language ability in the later test| Schoonman（1989） |Provide example data and naive regression comparison of \(N=306\) in this article|Data sources for the examples in this article|
|Bayesian CAT can use different selection items| van der Linden（1998） |Compare the maximum posterior information, minimum expected posterior variance and other topic selection criteria|direct method extension|

## 3. CAT topic selection and convergence: what do these quotations say?

### Birnbaum (1968): Why items can match ability positions

Birnbaum's chapter is a classic source of item information function. The basic idea it supports is: different items have different information peaks on the \(\theta\) scale. Traditional linear tests can select a set of questions so that the test information is higher within the expected ability range of the target population.

Can be used for demonstration: **After the item parameters are separated, the item can be selected based on the ability area where the examinee is expected to be. **

It does not directly discuss individualized priors, nor does it test the predictive ability of background variables.

### Wainer (1990) and Thissen and Mislevy (1990): How the CAT works question by question

*Computerized Adaptive Testing: A Primer*, edited by Wainer, provides a general framework for CAT; the "Testing Algorithms" chapter by Thissen and Mislevy discusses maximum likelihood and Bayesian testing algorithms. van der Linden uses them to support two standard paths:

- Use the current \(\widehat\theta\) to select the question with the largest amount of information;
- Use the current posterior distribution to select questions that can optimize the posterior.

This set of citations is suitable for defining a "traditional CAT baseline" but cannot be used to prove that individualized starting points are more effective.

### Chang and Ying (1996) and Gelman et al. (1995): Convergence arguments require qualifiers

van der Linden cited these two works to illustrate that, under general regular conditions, maximum likelihood estimation or Bayesian posterior estimation can approach the true \(\theta\) as information accumulates. From this, the paper further proposes that the further the initial point or initial distribution is from the true capability, the slower the algorithm usually enters the appropriate area.

The safe way to write it is:

> Under appropriate regular conditions, the ability estimate in CAT can converge with the accumulation of answer information; initialization mainly affects the path and efficiency in the early stage of the limited test (van der Linden, 1999; see Chang & Ying, 1996).

Don't write it as "There is a proven monotonic functional relationship between the starting point distance and the convergence speed under a limited number of questions." The “generally” in the original article refers to the motivation of the method, not the finite sample theorem provided in this article.

!!! note "Chang and Ying (1996) version"
    van der Linden's reference list is a paper from the 1996 Psychometric Society Annual Meeting *Building a Statistical Foundation for Computerized Adaptive Testing*. Related journal articles published in the same year [*A Global Information Approach to Computerized Adaptive Testing*](https://doi.org/10.1177/014662169602000303) are not the same bibliographic entry and should not be directly interchanged when cited.

## 4. Short test, content constraints and starting point of experience

### van der Linden and Reese (1998): Real CAT does not only pursue information maximization

[A Model for Optimal Constrained Adaptive Testing](https://doi.org/10.1177/01466216980223006) explains that the actual topic selection must also meet constraints such as content, cognitive level, question attributes, hostile questions, and question groups. van der Linden (1999) emphasizes that when there are many constraints, CAT may not always be able to select statistically optimal questions in the early stages, so more accurate initialization may be more valuable.

There is a need to be precise here: van der Linden and Reese (1998) directly support that "constraints can be many and need to be modeled uniformly", but it is not equivalent to "any content constraints necessarily reduce the final measurement efficiency". The latter still depends on the item bank, test length and constraint strength.

### Brown and Weiss (1977): Short Adaptive Subtests

[An Adaptive Testing Strategy for Achievement Test Batteries](https://files.eric.ed.gov/fulltext/ED150165.pdf) Study of adaptive test batteries consisting of multiple subtests. Its importance is not only that "CAT can shorten the test", but also that the information obtained from the previous subtest can help the subsequent subtests start more reasonably.

### Gialluca and Weiss (1979): Across subtest strands

*Efficiency of an Adaptive Inter-Subtest Branching Strategy in the Measurement of Classroom Achievement* Further research on using early subtest performance to schedule subsequent subtest starting points. van der Linden (1999) refers to Brown and Weiss (1977) and Gialluca and Weiss (1979) as early examples of empirical starting values: they regressed ability estimates of subsequent subtests onto estimates of earlier subtests.

These two articles are best suited to support:

> In a test battery consisting of multiple short subtests, performance on previous subtests can be used as auxiliary information for initialization of subsequent subtests.

They do not directly support the idea that a single self-report can form an accurate prior, because the auxiliary information comes from previous actual responses.

## 5. Exposure control: How should 15% and 40% be quoted?

### Sympson and Hetter (1985): Control the actual test probability of the item

The Sympson–Hetter method determines whether to actually administer the test based on the item-specific acceptance probability after the CAT selects the item. There is another page on this site [Complete Method Notes](sympson-hetter-1985.md).

The logic of van der Linden (1999) is:

1. Everyone starts from the same ability value, and items near the starting point are easy to be selected repeatedly;
2. Direct exposure control will reject some of the current optimal questions, so information may be lost;
3. If the individualized initialization itself disperses the examinee to different \(b\) areas, it may reduce the dependence on the forced rejection mechanism.

Points 1 and 3 are mechanism arguments in this article, not the results of exposure simulation. If empirical data are needed, they should also cite [Zhu and Fan (1999)](zhu-fan-1999.md): they directly compared the item usage distribution of common starting points and individualized starting questions.

### Thomasson (1995): This is a second-hand and context-dependent number

van der Linden paraphrases Thomasson's (1995) conference paper: Sympson–Hetter control causes an information loss of about 15% near the center of the capability distribution, with more conservative methods up to about 40% across the capability range.

It is best to quote as:

> Under the simulation conditions of Thomasson (1995), exposure control is accompanied by significant information loss; van der Linden (1999) reports that the Sympson–Hetter method loses about 15% of information near the center of the ability distribution, while the more conservative method reaches about 40% under some conditions.

Don't write "15% fixed loss for the Sympson–Hetter method and 40% fixed loss for the other methods." There are three reasons:

- Figures come from unpublished conference papers;
- What is currently available is a second-hand account from van der Linden;
- Information loss will vary with item bank, ability distribution, maximum exposure rate and topic selection constraints.

## 6. Collateral information, ignorability and fairness

### Mislevy Series: Auxiliary information entering IRT is not a new idea

van der Linden illustrates with four sets of work that IRT already uses auxiliary information in other statistical objectives:

|Literature|For what purpose is auxiliary information used?|Relationship to this article|
|---|---|---|
| [Mislevy（1988）](https://doi.org/10.1177/014662168801200306) |Estimating Rasch item difficulty using item auxiliary information|Prove that auxiliary information can enter item parameters estimation|
| [Mislevy and Sheehan（1989）](https://doi.org/10.1007/BF02296402) |Improving item parameter estimation using examinee auxiliary information|More direct connection examinee collateral information with IRT|
| Sheehan and Mislevy（1990） |Integrating cognitive and psychometric models to measure literature literacy|Show how structured external information enters the measurement model|
| [Mislevy et al.（1992）](https://doi.org/10.1111/j.1745-3984.1992.tb00371.x) |Estimating population characteristics from responses to sparse matrix sampling|Connecting auxiliary variables, sparse data and population inference|

These literatures provide precedents for methodological ideas, but the research goals are mainly item parameters or population distributions, not initializing CAT for a single examinee. Therefore, initialization at the individual level is still a step that van der Linden (1999) needs to make up.

### Little and Rubin (1987): Why the authors discuss missingness

In CAT, each person only answers a small part of the item bank, and the remaining items are not tested according to adaptive rules. Little and Rubin's missing data framework provides a formal language for whether selection mechanisms can ignore it.

### Mislevy and Wu (1988): Negligibility does not mean that any inference will not be affected

[Inferring Examinee Ability When Some Items Are Missing](https://doi.org/10.1002/j.2330-8516.1988.tb00304.x) is the most critical technical source in van der Linden's fairness argument. The limitation given in the original article is: if you focus on the achieved value of the maximum likelihood estimate rather than its sampling distribution or standard error, then the adaptive topic selection mechanism can be ignored.

This means that using background information to select questions does not automatically require background variables to be added directly to the final score formula; the answer is still provided by IRT likelihood. But it doesn't mean:

- Background information has no impact on item path, measurement accuracy and stop time;
- Conditional standard error can unconditionally ignore the topic selection mechanism;
- There are no fairness or policy issues with the use of sensitive background variables.

van der Linden's conclusion is that "whether to use a priori information to select a topic is a policy choice, and there is no general technical prohibition", rather than "fairness has been proven."

## 7. The real method difference: score first and then return, or score for latent ability

!!! important "One sentence summary"
    Schoonman treats \(\widehat\theta_j\) as the observed regression dependent variable; van der Linden retains \(\theta_j\) as a latent variable and integrates its uncertainty using complete item-by-item responses. The difference between the two is not "whether to do regression", but the difference between **plug-in point estimate** and **integrating over latent-trait uncertainty**.

### Two estimated paths

Schoonman's two-step method is:

\[
\mathbf u_j
\longrightarrow
\widehat\theta_j
\longrightarrow
\widehat\theta_j\sim x_j.
\]

It first compresses each person's Vocabulary item-by-item responses \(\mathbf u_j\) into a capability point estimate \(\widehat\theta_j\), and then uses ordinary least squares regression:

\[
\widehat\theta_j
=
\beta_0+\beta_1x_j+e_j.
\]

van der Linden established a joint generation model in the following direction:

\[
x_j
\longrightarrow
\theta_j
\longrightarrow
\mathbf u_j,
\]

\[
\theta_j\mid x_j
\sim
N(\beta_0+\beta_1x_j,\sigma^2),
\qquad
U_{ij}\mid\theta_j
\sim
\operatorname{Bernoulli}\{P_i(\theta_j)\}.
\]

This model asks: Which set of \(\beta_0,\beta_1,\sigma^2\) is most likely to generate all currently observed item-by-item responses?

### Why does two-step regression contaminate prior variance?

Assume that the real latent regression is:

\[
\theta_j
=
\beta_0+\beta_1x_j+\varepsilon_j,
\qquad
\operatorname{Var}(\varepsilon_j)=\sigma^2.
\]

However, ability point estimation itself has errors:

\[
\widehat\theta_j
=
\theta_j+\delta_j.
\]

Therefore, what the two-step regression actually fits is:

\[
\widehat\theta_j
=
\beta_0+\beta_1x_j
+
\underbrace{\varepsilon_j}_{\text{true prediction residuals}}
+
\underbrace{\delta_j}_{\text{ability estimate error}}.
\]

If the two errors are independent, the residual variance seen by ordinary regression is approximately:

\[
\operatorname{Var}(e_j)
=
\sigma^2+\operatorname{Var}(\delta_j).
\]

But individualized prior requires real conditional heterogeneity:

\[
\sigma^2
=
\operatorname{Var}(\theta_j\mid x_j),
\]

Instead, the part of the short test itself that is inaccurate in scoring \(\theta_j\) should not be stuffed into the prior variance.

!!! example "A hypothetical numerical example"
    If the true \(\sigma^2=0.8\) is \(\widehat\theta\) and the mean estimated error variance is \(0.3\), then the two-step regression may see a residual variance of \(0.8+0.3=1.1\). The thus constructed \(N(\widehat\beta_0+\widehat\beta_1x,1.1)\) is wider than the real \(N(\beta_0+\beta_1x,0.8)\), thus underestimating the predictive value of the auxiliary information. These numbers are only hypothetical examples of the explanation mechanism and are not estimated results of the paper.

### A statistical qualification that must be added

If the ability estimate error satisfies \(E(\delta_j\mid x_j)=0\) and is independent of \(x_j\), then "the dependent variable contains classical measurement error" does not necessarily attenuate the OLS slope \(\widehat\beta_1\):

\[
\frac{\operatorname{Cov}(x,\widehat\theta)}{\operatorname{Var}(x)}
=
\frac{\operatorname{Cov}(x,\theta+\delta)}{\operatorname{Var}(x)}
=
\frac{\operatorname{Cov}(x,\theta)}{\operatorname{Var}(x)}.
\]

So van der Linden's original article just says: The two-step method may still give a satisfactory estimate of \(\beta\), but it cannot give a good estimate of the prior variance \(\sigma^2\). What will be more clearly affected is the residual variance, regression uncertainty and correlation coefficient. Under classical independent errors, the associated attenuation can be expressed as:

\[
\operatorname{Cor}(\widehat\theta,x)
=
\operatorname{Cor}(\theta,x)
\sqrt{
\frac{\operatorname{Var}(\theta)}
{\operatorname{Var}(\theta)+\operatorname{Var}(\delta)}
}.
\]

### van der Linden How to retain uncertainty about everyone’s capabilities

Calibrated 2PLM gives:

\[
P(U_{ij}=1\mid\theta_j)
=
\frac{\exp[a_i(\theta_j-b_i)]}
{1+\exp[a_i(\theta_j-b_i)]}.
\]

Without first generating a fixed \(\widehat\theta_j\), the marginal likelihood of the regression parameters can be written as:

\[
L(\beta_0,\beta_1,\sigma^2)
=
\prod_{j=1}^{N}
\int
\left[
\prod_{i=1}^{I}
P_i(\theta)^{u_{ij}}
\{1-P_i(\theta)\}^{1-u_{ij}}
\right]
\phi\left(
\theta;
\beta_0+\beta_1x_j,
\sigma^2
\right)
\,d\theta.
\]

For each person, this formula does not assume that ability is a certain error-free point, but traverses all possible \(\theta\), judges how reasonable each position is based on item-by-item responses, and then integrates them. Therefore, two examinees who also get \(\widehat\theta=0.5\) are no longer considered equally accurate: the \(0.5\) given by 20 high-discrimination questions will be tighter than the \(0.5\) given by 4 low-discrimination questions, providing more information about the regression parameters.

### What the EM algorithm actually does

For each examinee, the unobserved residuals are:

\[
\varepsilon_j
=
\theta_j-(\beta_0+\beta_1x_j).
\]

van der Linden borrowed the idea from Rigdon and Tsutakawa (1983) and treated \(\varepsilon_j\) as missing data:

- **Step E: **Based on the current \(\beta_0,\beta_1,\sigma^2\), combine the personal \(x_j\) and all item-by-item responses \(\mathbf u_j\) to calculate \(p(\varepsilon_j\mid\mathbf u_j,x_j,\beta_0,\beta_1,\sigma)\). The intuitive question is: How much higher or lower is this person's true ability than predicted by the regression?
- **Step M:**Re-update \(\beta_0,\beta_1,\sigma^2\) according to the above-mentioned posterior distribution. The update of the residual variance is essentially

    \[
    \widehat\sigma^2
    =
    \frac{1}{N}
    \sum_{j=1}^{N}
    E\left(
    \varepsilon_j^2
    \mid
    \mathbf u_j,x_j
    \right).
    \]

The two steps are repeated until convergence. The example calculates the integral using the Gauss–Hermite quadrature and updates \(\beta_0\) and \(\beta_1\) using Newton’s method. "Directly estimating the regression of the real \(\theta\)" here does not mean that the author observed the real ability, but that he used \(\theta\) as a latent variable and did not pretend to be the first-stage \(\widehat\theta\) as an error-free observation.

!!! note "Citation sources for methods"
    Zwinderman (1991, 1997) provides the basis for manifest predictors to enter latent trait models; Rigdon and Tsutakawa (1983) provide EM ideas; Neter et al. (1990) supports regression and variable transformation; Ralston and Rabinowitz (1983) is the source of numerical calculations for Gauss–Hermite quadrature. Untested items do not enter the likelihood product of the examinee, so the same idea can also be used for sparse response data of actual CAT.

## 8. Empirical Example: from pretest response time to posttest individualized prior

!!! abstract "The core of this instance"
    van der Linden used the response time of the previous test to establish individualized ability priors for the subsequent vocabulary test; instead of estimating each person's \(\widehat\theta\) first and then doing ordinary regression, he jointly estimated the regression model and the IRT response model to avoid the measurement error of \(\widehat\theta\) being mistaken for a priori uncertainty.

### Relationship between data and prediction

The paper uses data from the Dutch General Aptitude Test Group, and the sample size is:

\[
N=306.
\]

Each person completes two tests in turn:

1. **Name Comparison test:**Record the total response time \(T_j\) to complete the test, and use logarithmic time \(x_j=\log T_j\).
2. **Vocabulary test: **Measuring language usage ability \(\theta_j\), the researcher uses the actual item-by-item responses of each examinee \(u_{ij}\in\{0,1\}\). The item bank has been calibrated with 2PLM, so the item difficulty \(b_i\) and discrimination \(a_i\) are regarded as known.

Both tests involve simple word usage, so the authors expected that those with higher language proficiency would complete the Name Comparison more quickly:

\[
\operatorname{Cor}(\theta,x)<0.
\]

Schoonman (1989) used the aforementioned two-step method to obtain \(\operatorname{Cor}(\widehat\theta,x)=-0.46\). After joint estimation at the latent variable level, van der Linden reports that the estimated correlation between the true \(\theta\) and the logarithmic response time is \(-0.59\), and interprets the difference in absolute values ​​as the information loss caused by estimating \(\widehat\theta\) first. This is the associated measurement error attenuation and should not be rephrased as "OLS slope must be corrected from \(-0.46\) to \(-0.59\)".

### The final estimated prior

Multiple sets of starting values converge to:

\[
\widehat\beta_0=5.833,
\qquad
\widehat\beta_1=-1.279,
\qquad
\widehat\sigma^2=0.986.
\]

Therefore, as long as the new examinee provides the logarithm of the Name Comparison and the total response time \(x\), it can get:

\[
\theta\mid x
\sim
N(5.833-1.279x,0.986).
\]

A negative slope indicates that the slower the response, the lower the predicted vocal latent ability.

### Two ways to use it in the new CAT

**Only as an initial point:**

\[
\widehat\theta^{(0)}
=
5.833-1.279x_{\mathrm{new}}.
\]

Then choose the first Vocabulary question with the most information at this location:

\[
j_1
=
\arg\max_j I_j(\widehat\theta^{(0)}).
\]

At this time, the response time of the previous test is only responsible for sending the new CAT to a more appropriate starting point.

**As a complete Bayesian prior:**

\[
p_0(\theta\mid x_{\mathrm{new}})
=
N(5.833-1.279x_{\mathrm{new}},0.986).
\]

Update using Bayes' theorem after each answer:

\[
p_t(\theta)
\propto
p_0(\theta\mid x_{\mathrm{new}})
\prod_{s=1}^{t}
P(U_{i_s}=u_{i_s}\mid\theta).
\]

At this time, the auxiliary information will continue to affect the intermediate ability estimate, subsequent item selection, final estimate and posterior standard error. Later, you can use the maximum amount of information to select topics in the EAP position, or you can use Bayesian criteria such as the minimum expected posterior variance.

### What does this example prove and what does it not prove?

What it proves is that the mean and variance of individualized prior can be directly estimated from "pre-test auxiliary variables + item-by-item responses" and avoid mistaking ability scoring errors as prediction failures of background variables.

It does not rerun a set of individualized prior CAT versus standard CAT, so there is no direct comparison:

- Average test length and stopping time under the same stopping rule;
- bias, root mean squared error and interval coverage rate;
- Actual item path and item exposure;
- Whether the error prior causes bias or error early stopping.

!!! warning "It is an a priori construction example, not a CAT efficiency experiment"
    The upper limit of the evidence in this case is "the joint model can be estimated and obtain an individualized prior", not "the prior has been shown to shorten CAT".

### Direct inspiration for self-assessment CAT

If response time \(x_j\) is replaced by user self-evaluation \(s_j\), the simplest training method is to do ordinary regression on \(\widehat\theta_j\). If the calibration test used to estimate \(\theta_j\) is long and \(\widehat\theta_j\) is sufficiently accurate, this two-step method may be useful.

But if the calibration test is inherently short, it makes more sense to build it directly:

\[
\theta_j\mid s_j
\sim
N(\beta_0+\beta_1s_j,\sigma^2),
\qquad
U_{ij}\mid\theta_j
\sim
\operatorname{Bernoulli}\{P_i(\theta_j)\},
\]

Then jointly estimate \(\beta_0,\beta_1,\sigma^2\) from item-by-item responses. Only in this way can we separate "inaccurate user self-assessment predictions" from "inaccurate ability scoring in short tests".

## 9. You can directly rewrite the quotations into the paper

Below is a safe Chinese paraphrase template, not a word-for-word translation of the original text.

### individualizedempirical prior

> The individual auxiliary variables available before the test can be mapped to the conditional ability distribution \(\theta\mid X=x\sim N(x^\top\beta,\sigma^2)\) through latent regression. Its conditional mean can be used to select starting questions, and the complete conditional distribution can be used as the individualizedempirical prior of Bayesian CAT (van der Linden, 1999).

### The difference between initial point and complete prior

> When only using the conditional mean to initialize the point estimate, the auxiliary information can only determine the first question; if the conditional distribution is used as a prior, the auxiliary information will affect the entire adaptive test process through question-by-question posterior updates (van der Linden, 1999).

### Do not perform naive regression on the ability estimate with error

> Using the ability estimate with measurement error as a common regression dependent variable will mix the ability estimate error with the true prediction residual, making it difficult to correctly estimate the prior variance; a more appropriate approach is to directly estimate the latent regression parameters from the item response data (van der Linden, 1999).

### Early cross-subtest initialization

> In adaptive test batteries, performance on previous subtests is used to predict and initialize ability position on subsequent short subtests (Brown & Weiss, 1977; Gialluca & Weiss, 1979; van der Linden, 1999).

### Common starting point and item bank exposure

> A common initial ability value will cause items near the starting point to bear higher exposure pressure; individualized starting positions may spread the use of first questions to a wider difficulty range (van der Linden, 1999). Direct simulation evidence of this mechanism can be found also in Zhu and Fan (1999).

### Fairness and ignorability

> Under a specific maximum likelihood inference goal, the adaptive topic selection mechanism can have negligible estimates of achieved ability points, but this result does not automatically extend to the sampling distribution, standard error, or fairness judgment of the estimator (Mislevy & Wu, 1988; van der Linden, 1999).

## 10. The six most common places to overquote

|Not recommended way of writing|question|More accurate way of writing|
|---|---|---|
|"van der Linden (1999) demonstrated that individualized prior shortens CAT."|No CAT controlled experiment|"Proposed an estimation and initialization framework for individualizedempirical prior."|
|“This paper demonstrates that self-assessment accurately predicts ability.”|The example uses pre-test response time, not self-assessment.|"In principle, the framework allows the use of pre-test variables related to ability; self-assessment validity needs to be verified separately."|
|"Individualized information only changes the first question."|This is true only when using the conditional mean as the initial point|"Point initialization can only affect the first question; the complete prior will affect subsequent posterior paths."|
|“Sympson–Hetter fixed loss of 15% information.”|Numbers are second-hand, specific analog results|"van der Linden paraphrases Thomasson (1995) who observed a loss of about 15% of central information under certain conditions."|
|“The topic selection mechanism can be ignored, so background variables will not cause fairness issues.”|Confusing statistical negligibility with normative fairness|"Ignorability only holds true under certain inference goals and model conditions; fairness remains a policy and empirical matter."|
|"A prior that is closer to the true value can be stopped immediately."|A single answer is random, and sufficient posterior accuracy is required to stop it.|"A more appropriate prior may improve early pathways, but response evidence must still be used to meet the established stopping criteria."|

## 11. The seven most worthy sources of this topic are worth pursuing.

Sorted by proximity to the “Self-Assessment Information Enters CAT” study:

1. **Zwinderman (1991)**: Understand the latent regression model of \(X\rightarrow\theta\);
2. **Rigdon and Tsutakawa (1983)**: Understand why \(\beta\) and \(\sigma^2\) should be estimated directly from item responses;
3. **Mislevy and Wu (1988)**: Clarify adaptive topic selection, missing mechanisms and final ability inference;
4. **Brown and Weiss (1977) and Gialluca and Weiss (1979)**: Looking for early direct precedents of "initializing subsequent short tests with existing individual information";
5. **van der Linden and Reese (1998)**: Understand how the amount of information and content constraints in real CAT jointly determine topic selection;
6. **van der Linden (1998)**: Compare the maximum amount of information and the minimum expected posterior variance and other Bayesian topic selection criteria;
7. **Thomasson (1995)**: If the original conference paper is available, check the simulation conditions for 15%/40% information loss.

## 12. A bibliographic problem in the references

The text cites Lord (1970), but the reference page of the paper is printed as Lord (1990), and the book title listed is Computer-Assisted Instruction, Testing, and Guidance, edited by W. H. Holtzman. This book and Lord's chapter actually correspond to 1970 publication information. Do not use “Lord, 1970” and “Lord, 1990” in references at the same time in subsequent writing; they should be checked against the original publication first and then unified into the correct year.

## 13. Direct inspiration for the experimental design of this topic

van der Linden (1999) clearly separates the two actions proposed by the tutor:

|design action|mathematical implementation|what does it change|
|---|---|---|
|Only change the first question|Initialize with \(\mu_c=x_c^\top\widehat\beta\) and select the first question|The difficulty position of the first question and the exposure of the first question|
|Change individualized prior|Use \(N(\mu_c,\tau_c^2)\) to update question by question|Initial position, uncertainty, posterior path, subsequent topic selection and stopping time|

Therefore subsequent ablations need to be compared separately at least:

1. Standard prior \(N(0,1)\) and standard first question;
2. Match the first question between standard prior and self-assessment;
3. Individualized priori and conventional Bayesian topic selection;
4. Individualized prior and self-assessment match the first question.

However, what van der Linden (1999) provides is the statistical entrance to the 3rd and 4th categories of methods, not the answer to the effect between these four groups.

## 14. References rearranged by citation role

### CAT, IRT and convergence basics

- Birnbaum, A. (1968). Some latent trait models and their use in inferring an examinee’s ability. In F. M. Lord and M. R. Novick, *Statistical Theories of Mental Test Scores*. Addison-Wesley.
- Chang, H.-H., and Ying, Z. (1996, June). *Building a Statistical Foundation for Computerized Adaptive Testing*. Paper presented at the annual meeting of the Psychometric Society, Banff, Alberta, Canada.
- Gelman, A., Carlin, J. B., Stern, H. S., and Rubin, D. B. (1995). *Bayesian Data Analysis*. Chapman and Hall.
- Thissen, D., and Mislevy, R. J. (1990). Testing algorithms. In H. Wainer (Ed.), *Computerized Adaptive Testing: A Primer*. Erlbaum.
- Wainer, H. (Ed.). (1990). *Computerized Adaptive Testing: A Primer*. Erlbaum.

### Experience initialization, short subtests and constraints

- Brown, J. M., and Weiss, D. J. (1977). *An Adaptive Testing Strategy for Achievement Test Batteries* (Research Report 77-6). University of Minnesota. [ERIC Full text](https://files.eric.ed.gov/fulltext/ED150165.pdf)
- Gialluca, K. A., and Weiss, D. J. (1979). *Efficiency of an Adaptive Inter-Subtest Branching Strategy in the Measurement of Classroom Achievement* (Research Report 79-6). University of Minnesota.
- Lord, F. M. (1970). Some test theory for tailored testing. In W. H. Holtzman (Ed.), *Computer-Assisted Instruction, Testing, and Guidance* (pp. 139–183). Harper and Row. Original reference page misprinted as 1990.
- van der Linden, W. J., and Reese, L. M. (1998). A model for optimal constrained adaptive testing. *Applied Psychological Measurement, 22*, 259–270. [DOI](https://doi.org/10.1177/01466216980223006)

### exposure control

- Sympson, J. B., and Hetter, R. D. (1985, October). *Controlling Exposure Rates in Computerized Adaptive Testing*. Paper presented at the 27th annual meeting of the Military Testing Association, San Diego, California.
- Thomasson, G. L. (1995, June). *New Item Exposure Control Algorithms for Computerized Adaptive Testing*. Paper presented at the annual meeting of the Psychometric Society, Minneapolis, Minnesota.

### Auxiliary information, missing data and ignorability

- Little, R. J. A., and Rubin, D. B. (1987). *Statistical Analysis with Missing Data*. Wiley.
- Mislevy, R. J. (1988). Exploiting auxiliary information about items in the estimation of Rasch item difficulty parameters. *Applied Psychological Measurement, 12*, 281–296. [DOI](https://doi.org/10.1177/014662168801200306)
- Mislevy, R. J., Beaton, A. E., Kaplan, B., and Sheehan, K. M. (1992). Estimating population characteristics from sparse matrix samples of item responses. *Journal of Educational Measurement, 29*, 133–161. [DOI](https://doi.org/10.1111/j.1745-3984.1992.tb00371.x)
- Mislevy, R. J., and Sheehan, K. M. (1989). The role of collateral information about examinees in item parameter estimation. *Psychometrika, 54*, 661–679. [DOI](https://doi.org/10.1007/BF02296402)
- Mislevy, R. J., and Wu, P.-K. (1988). *Inferring Examinee Ability When Some Items Are Missing* (Research Report 88-48). Educational Testing Service. [DOI](https://doi.org/10.1002/j.2330-8516.1988.tb00304.x)
- Sheehan, K. M., and Mislevy, R. J. (1990). Integrating cognitive and psychometric models to measure document literacy. *Journal of Educational Measurement, 27*, 255–272.

### latent regression, EM and numerical calculations

- Neter, J., Wasserman, W., and Kutner, M. H. (1990). *Applied Linear Statistical Models* (3rd ed.). Irwin.
- Ralston, A., and Rabinowitz, P. (1983). *A First Course in Numerical Analysis*. McGraw-Hill.
- Rigdon, S. E., and Tsutakawa, R. K. (1983). Parameter estimation in latent trait models. *Psychometrika, 48*, 567–574. [DOI](https://doi.org/10.1007/BF02293880)
- Zwinderman, A. H. (1991). A generalized Rasch model for manifest predictors. *Psychometrika, 56*, 589–600. [DOI](https://doi.org/10.1007/BF02294492)
- Zwinderman, A. H. (1997). Response models with manifest predictors. In W. J. van der Linden and R. K. Hambleton (Eds.), *Handbook of Modern Item Response Theory* (pp. 245–256). Springer. [DOI](https://doi.org/10.1007/978-1-4757-2691-6_14)

### Examples of this article and Bayesian topic expansion

- Schoonman, W. (1989). *An Applied Study on Computerized Adaptive Testing*. Swets and Zeitlinger.
- van der Linden, W. J. (1998). Bayesian item selection criteria for adaptive testing. *Psychometrika, 63*, 201–216. [DOI](https://doi.org/10.1007/BF02294775)

---

**Topic Navigation:** [Return to reading list](index.md) · [Part 2: Zhu and Fan (1999)](zhu-fan-1999.md) · [Sympson–Hetter method](sympson-hetter-1985.md)
