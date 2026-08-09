# 12. Compare six scoring methods

**Score included:**

- RAW: original scale score
- GRM: Grade Response Model Score
- M-GRM: Modified Grade Response Model Score
- PCM: partial credit model score
- G-PCM: generalized partial credit model score
- RSM: evaluate scale model score

**Instructions on scoring method:**

- Most use maximum likelihood estimation (ML)
- M-GRM uses EAP scoring
- GRM uses MAP score
- The latter two methods differ from ML mainly in the use of priors (see Chapter 7 for details)

## 12.1 Table 5.8: Descriptive statistics

**Important findings:**

- These values differ between IRT models, indicating that different measures are used
- But all latent trait scores are highly correlated (r > 0.97)
- Each is highly correlated with the raw score number
- The lowest correlation is r = 0.97 (between raw score number and G-PCM)

## 12.2 Visualizing results

![Figure 5.12: Scatter plot matrix (SPLOM) of trait level estimation under various multinomial models](../assets/images/ch5_fig5.12.png)

Figure 5.12 shows a scatterplot matrix of trait level estimates under various multinomial models, with each scatterplot showing the relationship between two scoring methods.

**Visual Observation:**

- All scatter plots show strong linear relationships
- Verified the high correlation mentioned earlier (r > 0.97)

## 12.3 Important Notes

Special properties of PCM and RSM

In PCM and RSM, trait level estimates are nonlinear transformations of raw score numbers.

That is: the raw score number is a sufficient statistic at the trait level.
This property does not hold in other models (GRM, G-PCM, M-GRM) that include a slope parameter.

## 12.4 Important warning: do not misunderstand result

Common misunderstandings

**Wrong conclusion:** "Since the results of all methods are highly correlated, IRT modeling is no better than simply calculating the raw scale score"

**Why is this conclusion wrong? **

- For relative ordering of subjects: this conclusion is probably correct
- But IRT offers much more than sorting

## 12.5 Many psychometric advantages of IRT models

**a) Connecting (equalizing) test scales:** Different tests can be compared on the same measurement scale

**b) Explore differential item functioning (DIF):** Discover items that are biased towards different groups

**c) Calculate the Person Fit statistic:** Identify subjects with abnormal response patterns

**d) Computerized adaptive test:** Adjust item difficulty according to the subject's ability

**e) standard error varies with trait level: ** Provides measurements with different accuracies at different ability levels

**f) The substantive meaning of item parameters:** item difficulty, discrimination, etc. have clear psychometric explanations

## 12.6 Conclusion

Although subject rankings were similar across methods on this particular data set, the value of IRT modeling goes far beyond simple ranking. IRT provides rich psychometric information and flexible application possibilities that raw scores cannot provide.
