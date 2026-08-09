#Limitations and future work

## Accurate conditions for parameters and standard error

The paper points out that it was still unclear at the time which conditions would guarantee:

- Item probability estimation is accurate;
- delta-method standard error is accurate;
- covariance matrix is stable;
- The two-step reduction estimate has good asymptotic properties.

Particularly critical factors include sample size, attribute distribution, and the number of attributes required for each question.

## Pattern sparsity and exponential growth

The complete attribute space size is

\[
2^K,
\]

The probability of success for a single question is

\[
2^{K_j^*}.
\]

When \(K\geq20\), the paper believes that the saturated attribute joint distribution may not be feasible under the memory and sample size conditions at that time.

Proposed mitigation routes include:

- higher-order latent trait；
- attribute hierarchy;
- Only keep feasible attribute profiles;
- Apply structure to the attribute joint distribution.

## Wald asymptotic approximation

Still needs research:

- How large a sample is to make \(\chi^2\) approximately reliable;
- \(K_j^*\) whether to change the approximate quality;
- Whether different reduction models have different test performances;
- How rare latent groups affect power;
- How boundary probabilities affect covariance and statistics.

The paper simulation only covers \(I=2000\), \(K_j^*\leq3\) and stronger model differences.

## Multiple comparisons

Comparing multiple models on a question-by-question basis yields a large number of tests. The paper proposes research:

- Bonferroni type correction;
- Joint control between item layer and test layer;
- Methods such as AIC that take into account both fitting and complexity.

Subsequent software added a variety of \(p\) value corrections, but specific decisions still need to be combined with the research purpose.

## Cross-item constraints

Item-by-item two-step estimation cannot directly handle cross-item shared parameters, for example:

- Items in the same Q row share the main effect;
- Shared guessing/slipping for multiple questions;
- Attribute effects are equal across topics;
- Longitudinal or multi-set parameter invariance.

These problems require a joint estimation framework.

## Q matrix is treated as known

Wald model comparison assumes that the attributes have been identified and the Q matrix is correct. If row Q is missing or has extra attributes:

- The saturation probabilities themselves may be incorrectly grouped;
- Item interaction may absorb Q errors;
- Reduced models may be incorrectly rejected;
- The attribute meaning of the classification result will deviate.

The paper proposed extending the 2008 DINA Q verification method to G-DINA; this later became an important research direction.

## Interpretation Risks of Data-Driven Model Selection

You can fit the saturated model first, and then select DINA, DINO, A-CDM, etc. by item. This increases flexibility and also results in:

- Unstable selection;
- Sample specificity;
- Post hoc theoretical explanation;
- Multiple comparisons;
- Inference after selection.

A more robust process should combine item cognitive analysis, pre-registered candidate models, statistical testing, and external sample validation.

## Psychometric models are only part of

The paper concludes by emphasizing that the G-DINA framework only constitutes the psychometric part of cognitive diagnosis. Effective diagnosis also requires:

- Clearly define attributes;
- Design tasks that can distinguish attribute profiles;
- Validation of Q matrix by domain experts;
- Interpret scores and develop appropriate interventions;
- Test the validity of the consequences of the diagnostic conclusion.

Model flexibility cannot compensate for weaknesses in test design and attribute theory.

## Recommended connection to CAT/Sequence

This paper estimates the static response model and item layer model structure, and does not study real-time topic selection. It can become the response model of CD-CAT:

\[
P(X_{ij}=1\mid\boldsymbol\alpha_i,Q_j),
\]

But adaptive selection requires additional definition:

- How to update the current posterior;
- Effect of next question;
- Content constraints;
- stopping rule;
- exposure control;
- Replan after each answer.

G-DINA provides richer response probability, and sequence adaptability still belongs to the upper-level decision-making algorithm.
