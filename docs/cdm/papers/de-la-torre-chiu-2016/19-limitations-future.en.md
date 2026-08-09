# Limitations, conclusions and future work

## Paper conclusion

GDI generalizes the DINA distinction of de la Torre (2008) to the G-DINA family. The theory shows:

\[
\text{Correct q-vector}
\Longrightarrow
\text{Maximum inter-group success rate variance},
\]

The simplicity rule can exclude parallel vectors that only add irrelevant attributes.

Under thesis conditions:

- The correct Q retention rate is high for the five reduced models;
- Most random misconfigurations can be corrected;
- Unconstrained G-DINA is more difficult;
- Fractional subtraction data emerged with specific modifications available for expert review.

## Limitation 1: Fixed design

Simulation fixed:

\[
N=2000,\quad J=30,\quad K=5.
\]

Need to continue research:

- Large \(K\);
- small \(N\);
- shorter or longer quizzes;
- Different attributes related;
- Rare attribute profile;
- Systematic rather than random Q errors.

## Limitation 2: Q error is only one source of mismatch

Model mismatch can also come from:

- The attribute set is incomplete;
- The attribute itself is continuous;
- local dependencies;
- Group heterogeneity;
- Monotonicity does not hold;
- The reaction process changes with the item situation.

The paper recommends combining GDI with model fit indicators based on observations and expected moments to form a more complete diagnosis.

## Limitation 3: There is no unique optimal value for the threshold

\[
\varepsilon=.95
\]

Perform well in thesis simulations. It does not analyze optimality, nor does it cover the entire design. The authors recommend using a threshold to narrow down the set of candidate Q, and then using a more formal procedure to compare the final candidates.

Further research can be done on:

- Data-driven thresholds;
- Prediction threshold;
- cross-validation;
- bootstrap stability;
- loss-based threshold;
- Adjust the threshold according to item quality.

## Limitation 4: The number of attributes \(K\) is known

The algorithm selects the subset required for each question within the fixed set of attributes. If \(K\) is also unknown, it needs to be processed at the same time:

- Selection of number of attributes;
- New attribute definition;
- Q’s identifiability;
- Label replacement;
- Teaching explainability.

The paper lists identifying the correct \(K\) as an important future direction and reminds that constraints such as actual class length should also enter the decision-making process.

## Limitation 5: The calculation increases exponentially with \(K\)

Exhaustive price:

\[
J(2^K-1).
\]

Large \(K\) can be considered:

- sequential search；
- priority attribute search；
- branch-and-bound；
- Sparse penalty;
- Content a priori narrowing down candidates;
- Parallel candidate calculation.

## Limitation 6: Experience suggestions and expert opinions may conflict

The fraction subtraction example shows that statistical advice can produce difficult-to-explain differences between similar problems. The paper positions the method as supplementary information for Q construction and validation.

Can be extended to multi-evidence decision-making:

\[
\text{response evidence}
+
\text{task-analysis evidence}
+
\text{process data}
+
\text{external validity}.
\]

## Follow-up research route

1. Theory: initial Q condition, estimation consistency, equilibrium point;
2. Methods: iterative GDI, Wald, Hull and model averaging;
3. Computation: high-dimensional search and scalable estimation;
4. Data: process data, text and expert priors;
5. Application: reporting threshold sensitivity and recommendation stability;
6. CAT: Study how Q uncertainty propagates to diagnostic topic selection strategies.

## Interface to CAT

This article does not select topics on a student-by-student basis. It verifies item bank metadata:

\[
\text{item}
\longrightarrow
\text{required attributes}.
\]

In cognitive CAT, Q affects:

- Attribute posterior after each answer;
- Probability of success for candidate questions;
- diagnostic information;
- Attribute override;
- stopping rule.

Therefore, GDI Q validation belongs to the measurement model quality control upstream of adaptive policy.
