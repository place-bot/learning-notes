# Evaluate the fit of the IRT model

## 0. Introduction: The importance of model fit

As with any model-based approach to psychological data interpretation, the benefits of an IRT model (e.g., item-independent examinee trait level estimates, test information curves) are achieved in direct proportion to the degree to which the data are consistent with the assumptions underlying their application.

Core content of this chapter

1. **IRT model assumptions**: Assessment methods of unidimensionality and local independence
2. **Goodness of fit evaluation**: Fit test at item, personnel and model levels
3. **Practical Suggestions**: Additional issues to consider when applying IRT models

key challenges

The topic of model fit is an active area of current research, and to date, no clear answers exist in this area.

## 1. Evaluate IRT model assumptions

### 1.1 Two main assumptions

The most commonly used IRT models make relatively simple but powerful assumptions about the relationship between item responses and latent traits:

#### 1.1.1 unidimensionality assumption

"Appropriate" dimensionality. In the vast majority of applications, IRT models assume unidimensionality:

- A single latent trait variable is sufficient to explain the common variance between item responses
- Test scores (i.e., trait level estimates) are clear indicators of a single construct

#### 1.1.2 local independence assumption

Consistent with the first assumption is the concept of **local statistical independence**:

- Test items are uncorrelated (i.e. independent) while controlling for examinee trait levels
- The probability of identifying with an item is strictly determined by the examinee’s trait level
- is not affected by its responses to other test items or common sources of variance that are not taken into account

Relationship with CTT

The local independence assumption is similar to the assumption in CTT regarding the independent error condition based on the examinee's true score.

### 1.2 Relationship between hypotheses

Although conceptually different, unidimensionality and local independence are related:

- By definition, a data set is unidimensional when item responses are locally independent based on a single latent trait.
- See McDonald (1981) for an extended description

## 2. Assess Dimensionality

### 2.1 Method Overview

Although the development of multidimensional IRT modeling continues (e.g., Ackerman, 1994; Reckase, 1997), most commonly used IRT models assume that a single latent trait dimension governs the probability of item responses.

key questions

Even in the application of multidimensional IRT models, the correct number of latent factors must be determined a priori.

Therefore, determining the number of dimensions is a key issue in IRT modeling, regardless of whether a single-dimensional or multidimensional model is considered.

### 2.2 Traditional methods and their problems

Hattie (1984; 1985) reviewed dozens of suggested methods for assessing matrix dimensionality:

#### 2.2.1 Methods based on different principles

- **Answer pattern consistency**: e.g. Guttman scalability
- **Test-Retest Reliability**
- **Principal Component Analysis**: The number of eigenvalues is greater than 1.0 or the ratio of the first to the second eigenvalue
- **Factor Analysis**: Output of linear and non-linear factor analysis
- **model fit statistics**: Residual analysis after fitting a specific model

#### 2.2.2 Problems with traditional methods

Hattie found that most dimensional assessment methods have serious flaws:

1. Unable to reliably distinguish between one- and two-dimensional data sets
2. There is no known sampling distribution
3. Their performance under various test conditions is unknown
4. Few guidelines exist to guide researchers

### 2.3 Active discovery

Although the tone was mostly negative, there were some positive findings revealed in the Hattie study:

- Recommend using **Nonlinear Factor Analysis** as a possible dimensionality assessment tool
- Especially residual variance term analysis (using programs such as NOHARM)
- Hambleton and Rovinelli (1986) also reported that nonlinear factor analysis is promising for assessing dimensionality

## 3. New methods for assessing dimensionality

### 3.1 McDonald and Mok (1995) method

#### 3.1.1 Two model types

McDonald and Mok note that two general types of models may be suitable for item response data:

- **Complete Information Model**
- **Bivariate Information Model**

These provide researchers with methods to assess dimensionality and evaluate the goodness of fit of unidimensional and multidimensional IRT models.

#### 3.1.2 Two forms of local independence

**Strong form**:

\[
P\{\mathbf{X} = \mathbf{x}|\mathbf{\theta}\} = \prod_{i=1}^{I} P_i\{X_i = x_i|\mathbf{\theta}\}
\]

This equation shows that, given the latent trait vector, the probability of a joint response pattern can be decomposed into the product of the conditional probabilities of each item.

**Weak form**:

\[
\text{Cov}\{X_i, X_j|\mathbf{\theta}\} = 0
\]

Represents items that share variance and no longer share variance once the latent trait is taken into account.

The difference between the two forms

The weak form allows higher-order dependencies between items, while the strong form does not.

### 3.2 The concept of basic unidimensionality

The studies of Stout (1987; 1990) and Nandakumar and Stout (1993) represent methods for assessing "basic unidimensionality".

#### 3.2.1 Definition of basic unidimensionality

A test is said to be essentially unidimensional when the average inter-item residual covariance after fitting a one-factor model approaches zero (increasing with test length).

#### 3.2.2 Characteristics of the Stout program

- Used to identify the number of "major" common dimensions in a quiz
- Ignore minor factors
- No need to estimate any IRT model parameters

### 3.3 Software implementation

- **TESTFACT**（Wilson, Wood, & Gibbons, 1991）
- **NOHARM**（Fraser, 1988）
- **LISCOMP**（Muthén, 1987）
- **DIMTEST**（Stout, 1987）

### 3.4 Suggestions

current situation

Researchers currently know more about what not to do than what to do when it comes to test dimensionality.

**Don’ts**:

- Rely only on internal consistency indices (e.g., coefficient alpha). Alpha is affected by the number of items and average correlation, and cannot prove unidimensionality alone.
- Use any index based on compositional analysis

**Promising Directions**:

- Development of statistical fit tests and dimensionality goodness of fit indices
- Use the new technology described previously

Key points to remember

1. All models are strictly wrong and only approximations of reality
2. The impact of small deviations from unidimensionality on parameter estimates remains unproven
3. Some studies show that IRT model parameter estimates are robust to minor violations of unidimensionality

## 4. Evaluate local independence

### 4.1 Definition of local dependency (LD)

Violations of local independence, called local dependence (LD), occur when:

- participantitem responses not only depend on their trait level
- Also depends on their reactions to other quiz items (or combinations of items)
- or other common factors

### 4.2 Consequences of LD

The existence of LD may have serious consequences on the applicability of single-dimensional IRT models:

#### 4.2.1 Impact on likelihood calculation

The key equation for calculating participant answer pattern likelihood:

\[
L(\mathbf{x}_i|\theta_i) =
\prod_{j=1}^{I} P_j(\theta_i)^{x_{ij}}
\left[1-P_j(\theta_i)\right]^{1-x_{ij}}
\]

Among them:

- \(L(\mathbf{x}_i|\theta_i)\) represents the conditional probability of the item reaction mode \(\mathbf{x}_i\) of participant \(i\)
- \(P_j(\theta_i)\) is the model probability that a participant with ability \(\theta_i\) answers correctly or agrees with item \(j\)

key questions

In order for this product form to be valid, the local independence condition must be met. When LD occurs, the product likelihood will underestimate the uncertainty caused by the correlation between items, thereby affecting parameters, information functions and ability estimates.

#### 4.2.2 Empirical research findings

Yen (1993) demonstrated the impact of the presence of LD:

- Quiz information is overrated
- itemdiscrimination parameter is overestimated
- Dimensions of latent traits that may cause IRT computer programs to identify errors (Steinberg & Thissen, 1996)

### 4.3 Test situations leading to LD

#### 4.3.1 Factors in Educational Assessment

- **Reading Comprehension Questions**: Multiple questions embedded in the context of a single segment
- **Accelerated Test**: Time pressure affects the response of subsequent items
- **Material Exposure Difference**: There are differences between students in practice or material exposure
- **item link**: Answering one item affects answers to other items

#### 4.3.2 Factors in Personality Assessment

Steinberg and Thissen (1996) demonstrated that LD can also occur in personality assessment situations:

- **Approximately copy item**: scale contains similar items
- **Response Consistency Change**: participant responses become more consistent as the test progresses
- People clarify their self-concept during testing (Knowles, 1988)

### 4.4 Statistical methods for identifying LD

#### 4.4.1 Q3 Statistics (Yen, 1984)

The Q3 index represents the correlation between item pairs after excluding latent trait variables.

**Calculation steps**:

1. Estimate item parameters and participant trait levels
2. Calculate each participant’s expected response to each test item
3. Calculate residuals: observed response - expected response
4. Residual score of associated item pairs

**Explanation**:

- Since the residuals use the same ability estimate, the average value of Q3 usually has a slight negative skew. The commonly used empirical baseline is about \(-1/(I-1)\), where \(I\) is the number of items.
- In practice, it is more common to compare the difference between the item pair Q3 and the average value of all item pairs Q3
- Significantly larger positive values indicate possible LD

#### 4.4.2 G² Statistics (Chen & Thissen, 1997)

\(G^2\) statistic developed to identify local dependencies:

- Provide methods for formal analysis of residuals
- Evaluate item pairs
- Find unexpected covariance of other item covariance in a given quiz

### 4.5 Suggestions

Strategies for handling local dependencies

1. **Prevention First**: Yen (1993) provides suggestions on how to arrange testing situations to minimize the chance of LD occurrence.
2. **Use quizzes**: Merge items showing LD into "quizzes" (Wainer & Kiely, 1987)
3. **Note on limitations**: It is difficult to form quizzes when items are not binary.

## 5. Evaluate model-data fit

### 5.1 Determine item fitting

#### 5.1.1 Graphical method

Compare estimated IRC to "empirical" IRC:

**Steps to Create an Experience IRC**:

1. Estimating the parameters of the IRT model
2. Estimating participant trait levels based on item parameters
3. Sort and group by trait level (for example, 10 groups)
4. Calculate the actual percentage of item recognition in each group
5. Plot using the within-group mean trait level as a coordinate

**Identify possible causes of the problem**:

- multidimensionality is not considered
- Failure to estimate sufficient item parameters
- Non-monotonicity of item-trait relationship
- participant samples come from different groups
- poorly constructed item

#### 5.1.2 Statistical methods

**Bock (1972) Chi-Square Index**:

\[
\text{BCHI} = \sum_{g=1}^{G} \frac{N_g(O_{ig} - E_{ig})^2}{E_{ig}(1-E_{ig})}
\]

Among them:

- \(O_{ig}\) is the observed correct proportion of item \(i\) in the interval \(g\)
- \(E_{ig}\) is the expected correct proportion based on the interval median trait level
- \(N_g\) is the number of participants in the interval \(g\)

Degrees of freedom: \(G - m\) (\(m\) is the estimated number of item parameters)

**Table 5.1 Residuals and fitting statistics of five stress response items**

|midpoint of θ interval| ST1 | ST2 | ST3 | ST4 | ST5 |
| --- | --- | --- | --- | --- | --- |
| -2.0 | 0.00 | 0.03 | 0.00 | 0.00 | 0.00 |
| -1.5 | 0.02 | -0.04 | -0.04 | 0.00 | 0.00 |
| -1.0 | -0.01 | 0.01 | 0.02 | 0.00 | 0.00 |
| -0.70 | -0.02 | 0.01 | 0.01 | 0.02 | 0.00 |
| -0.40 | 0.01 | -0.04 | -0.03 | -0.02 | -0.01 |
| -0.10 | -0.01 | 0.04 | 0.02 | 0.01 | -0.05 |
| 0.10 | 0.02 | 0.04 | 0.00 | 0.00 | 0.05 |
| 0.40 | 0.02 | 0.04 | 0.06 | -0.06 | 0.05 |
| 0.70 | 0.02 | -0.02 | 0.02 | 0.02 | 0.04 |
| 1.10 | 0.01 | -0.02 | 0.00 | 0.00 | -0.04 |
| 1.80 | -0.01 | 0.01 | -0.02 | 0.00 | 0.00 |

Things to note

Like many chi-square statistics, these fit tests are very sensitive to sample size and probably should not be considered reliable decision-making tools.

**BILOG Likelihood Ratio Chi-Square**:

\[
\chi^2 = 2\sum\left[R_g \log\frac{R_g}{N_g P(\theta_M)} + (N_g - R_g)\log\frac{N_g - R_g}{N_g(1-P(\theta_M))}\right]
\]

- Degrees of freedom equal to the number of θ groups
- Theta groups are collapsed to avoid expectation less than 2

#### 5.1.3 Standardized residuals

For Rasch models, standardized residuals can be calculated:

**Expected reaction**:

\[
E[x_{si}] = \sum_{k=0}^{K-1} kP_i(\theta_s)
\]

**variance**:

\[
V[x_{si}] = \sum_{k=0}^{K-1}(k-E[x_{si}])^2 P_i(\theta_s)
\]

**Standardized Residuals**:

\[
z_{si} = \frac{x_{si} - E[x_{si}]}{\sqrt{V[x_{si}]}}
\]

**Fit Statistics**:

- item fitting: \(\text{Item fit} = \sum \frac{z_{si}^2}{N}\)
- Personnel fitting: \(\text{Person fit} = \sum \frac{z_{si}^2}{I}\)

### 5.2 Personnel fitting

#### 5.2.1 Purpose of Personnel Fit Index

- Evaluate IRTmodel fit at the individual level
- Evaluate effectiveness of participant
- Evaluate the validity and meaningfulness of test scores

#### 5.2.2 Types of Personnel Fit Index

- **Appropriateness Measure** (Levine & Rubin, 1979)
- **caution index** (Tatsuoka, 1984; 1996)
- **Scalability Index** (Reise & Waller, 1993)

#### 5.2.3 ZL Statistics (Drasgow, Levine & Williams, 1985)

**Log-likelihood**:

\[
\text{LogL}|\theta_s = [x_{si} \times \log(P_i|\theta_s)] + [(1-x_{si}) \times \log(1-P_i|\theta_s)]
\]

**expectation**:

\[
E[\text{LogL}|\theta_s] = \sum\{P_i|\theta_s \times \log(P_i|\theta_s) + Q_i|\theta_s \times \log(Q_i|\theta_s)\}
\]

**variance**:

\[
V(\text{LogL}|\theta_s) = \sum\{P_i|\theta_s)(Q_i|\theta_s)[\log(P_i|\theta_s)/Q_i|\theta_s)]^2
\]

**Normalized \(Z_L\) Index**:

\[
Z_L|\theta_s = \frac{\sum[\text{LogL}|\theta_s - \sum E(\text{LogL}|\theta_s)]}{(\sum V(\text{LogL}|\theta_s))^{1/2}}
\]

**Table 5.2 Example of person fitting for six tests**

|participant|reaction mode| θ | \(T\text{-INFO}(\theta)\) | \(SEM(\theta)\) | \(Z_L\) |
| --- | --- | --- | --- | --- | --- |
| 1 | 000011 | -0.96 | 0.99 | 1.006 | -4.10 |
| 2 | 000101 | -0.96 | 0.99 | 1.006 | -3.68 |
| 3 | 001001 | -0.96 | 0.99 | 1.006 | -2.83 |
| ... | ... | ... | ... | ... | ... |
| 13 | 011000 | -0.96 | 0.99 | 1.006 | -0.31 |
| 14 | 101000 | -0.96 | 0.99 | 1.006 | 0.53 |
| 15 | 110000 | -0.96 | 0.99 | 1.006 | 0.95 |

explain

- The conditional null distribution of \(Z_L\) is standard normal
- Large negative \(Z_L\) values (for example, < -2.0) indicate a poor fit
- Large positive \(Z_L\) values indicate a more likely response pattern than predicted by the model

#### 5.2.4 Application of Personnel Fitting

- **Identify Abnormal Test Behavior**: Cheating, groping, careless or inconsistent responses
- **Data Cleaning**: Identify abnormal participants
- **Personality Assessment**: Identify structural differences in individual personality traits
- **Diagnostic Use**: Identify specific skill deficits or cognitive errors

#### 5.2.5 Issues in Personnel Fitting Research

1. **Explanation Difficulties**: Unable to explain the reasons for non-fitting
2. **Sampling distribution**: The actual null distribution may not be as good as theoretical expectations
3. **statistical power**: limited ability to identify response bias

Improve conditions for statistical power

- Longer quizzes (e.g., more than 30 items)
- Extensive range of itemdifficulty parameters
- Highly differentiated test items

### 5.3 Model comparison method

#### 5.3.1 Nested model comparison (Thissen, 1986)

By comparing the log-likelihoods of different models:

**Example**: Comparing 2PL and 1PL models

1. Estimate the 2PL model and calculate the log likelihood
2. Apply constraints (all slopes are equal) and estimate the 1PL model
3. Compare the difference in log-likelihood of two models
4. The difference distribution is chi-square, degrees of freedom = number of parameter differences

Limit

- Under sparse contingency table conditions, the distribution of changes in \(G^2\) may not be chi-squared
- More research is needed to confirm

#### 5.3.2 Ideal Observer Method (Maydeu-Olivares, Drasgow & Mead, 1994)

- Can compare non-nested models
- Based on the likelihood of observing item response patterns under various models
- When the likelihood is approximately equal across models, there is no difference in which model is ultimately chosen

## 6. Future directions and conclusions

### 6.1 General recommendations

#### 6.1.1 The Importance of Conceptual Model

First assess the measured construct and the conceptual model underlying the construct:

**Manifest variables vs latent variables**:

- **Manifest variable**: defined by its indicators (e.g. economic strength, health)
- **Latent variables**: Cause indicators to be related (such as intelligence, extraversion)

Key differences

IRT models are "latent" variable models, assuming causal relationships from latent traits to indicators.
If you simply apply the IRT model to manifest variables, it will inevitably lead to problems.

#### 6.1.2 Good exploration of model fit

Good model fit exploration should include:

1. **Dimensionality Assessment**: Use DIMTEST or nonlinear factor analysis
2. **local independence test**: Q3 or G² statistics
3. **Residual analysis**: Check the residual covariance term
4. **item fitting**: graphical and statistical methods
5. **Personnel Fitting**: Identifying Abnormal Response Patterns

### 6.2 Perspectives on model selection

Prudence

We take a more cautious approach to model selection for the following reasons:

**Model choice is usually obvious**:

- Two-category item + guess → 3PL model
- Personality assessment data → 2PL model

**Actual impact may be limited**:

- For research applications, as long as the data has strong one-dimensionality and the sample size is large enough
- It may not make much difference which specific IRT model is actually adopted

need attention

Goldstein (1980) noted that different models can have significant effects on the relative scales at which individuals are mapped onto the latent trait continuum.

### 6.3 Summary

This chapter introduces methods for evaluating IRTmodel fit:

1. Evaluation of **Model Assumptions** is the basis
2. **Multi-level** fit assessment is necessary
3. **New methods** are constantly evolving
4. **Practical application** requires comprehensive judgment

Remember: all models are wrong, but some are useful. The key is to ensure that violations of the model's assumptions do not significantly affect the study's conclusions.

The content of this chapter is based on Chapter 9 of Embretson & Reise (2000)
