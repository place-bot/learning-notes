# Limitations, conclusions and future work

## Original conclusion

The paper proposes sequential EM-based \(\delta\)-method, which incorporates Q verification into DINA model fit check:

- Restore all error q-vectors in simulation and retain all correct lines;
- Find the threshold interval that can completely retain the original Q in the fractional subtraction data;
- Minor parameter improvements in NAEP and generation of alternative specifications that can be reviewed on a topic-by-topic basis;
- Statistical advice needs to be combined with content knowledge and expert judgment.

## Method limitations

### Fixed attribute collection

The algorithm searches among the existing non-zero combinations of \(K\) attributes. If the attributes that are really needed are not included in the system, any candidate q-vector can only use existing attributes as a proxy.

### Depends on initial posteriori

Candidate \(\widehat\delta\) uses the initial Q under

\[
\widehat P(\boldsymbol\alpha_l\mid\boldsymbol X_i).
\]

The error Q will affect the item parameters, which in turn affect the posterior. Multiple errors, weak items, or sparse attribute profiles can weaken candidate ranking.

### Greedy path

Once an attribute is selected early in the sequential search, attributes can only be added to the set later. If there is a local optimum in the candidate discrimination, the result may deviate from the exhaustive maximum value.

### Model restrictions

The method is based on DINA's conjunctive two-group structure. Compensatory, saturated interaction, or multipartite models require redefinition of candidate discriminant indicators.

### Single sample fitting

Minimizing this sample \(\bar g+\bar s\) may absorb random fluctuations. The original article does not use independent validation set or bootstrap stability.

### Statistical equivalence and cognitive implications

Multiple q-vectors can produce approximately the same parameters. The NAEP question 52 and property 5 counterexamples for fraction subtraction show that data separation cannot determine property semantics alone.

## Future work clearly proposed in the original article

The author lists five items:

1. Expand simulation conditions, including Q error degree, test length and sample size;
2. Analyze more real-world areas, such as language tests;
3. Study Q validation statistics other than \(\delta\);
4. Relax the known assumptions of \(K\) and include the selection of attribute numbers into verification;
5. Extend the concept to cognitive diagnosis model beyond DINA.

## How to respond to follow-up research

- de la Torre and Chiu (2016) proposed general empirical Q-matrix validation, extending the idea of item differentiation improvement to more general CDM.
- Chiu (2013) Statistical refinement of Q from the perspective of classification residuals.
- Liu, Xu and Ying (2012, 2013) Study Q learning from data and its theory.
- Bayesian, regularized and exploratory CDMs put the uncertainty in Q into the joint estimate.
- The current software provides interfaces such as `CDM::din.validate.qmatrix()` and `GDINA::Qval()`.

These subsequent methods change the search, statistics, or model scope and should be used to distinguish them from the original 2008 sequential \(\delta\)-method.

## Suggestions for research design

If applying this approach today, it is recommended to report at least:

1. Initial Q development process;
2. DINA basic fitting;
3. Candidate threshold grid;
4. The grid and entire row of each threshold change;
5. Item parameters and full test indicators before and after the update;
6. Multiple starting points, bootstrap or reserved sample stability;
7. Review the content of the modified item;
8. The impact of modifications on attribute classification and external validity criteria;
9. Reasons for final adoption and rejection of each recommendation.

## Interface with CAT

Q verification is located at the reactive model and item bank annotation layer of CAT:

\[
\text{item content}
\rightarrow Q
\rightarrow P(X\mid\boldsymbol\alpha)
\rightarrow \text{student posterior}
\rightarrow \text{Topic selection}.
\]

The wrong Q will deviate from both the posterior ability state and the item selection utility. This article does not study topic-by-item adaptive selection policy, nor does it generate test sequences; it can help improve the reliability of CAT's underlying cognitive model and item bank attribute labels.

