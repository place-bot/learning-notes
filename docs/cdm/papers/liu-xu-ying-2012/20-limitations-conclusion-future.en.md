# Limitations, conclusions and future work

## Paper conclusion

The paper establishes a unified route for learning Q from response data:

\[
Q
\longrightarrow
T_{\boldsymbol c,\boldsymbol g}(Q)
\longrightarrow
T_{\boldsymbol c,\boldsymbol g}(Q)\boldsymbol p
\longleftrightarrow
\boldsymbol\beta.
\]

In DINA simulation, as long as the sample size is large enough relative to \(2^K\) and the starting Q only has a small number of wrong questions, line-by-line search can restore the true Q with a high frequency. Partially known Q scenarios can efficiently calibrate new questions.

## Main limitations

### 1. Starting point dependency

The main simulation is fixed at 3 wrong lines out of 20 questions. Distant origin and multiple origin strategies were not evaluated.

### 2. Local minimum

Algorithm 1, which only changes one line at a time, may not be able to overcome the target obstacle that requires two lines to change at the same time.

### 3. Limited sample overfitting

Figures 1--2 show that continuing to lower \(S\) may cross true Q. 4.5% Early stopping lacks independent parameter adjustment evidence.

### 4. Computational burden

Each round of \(J2^K\) candidate evaluations requires EM and T construction each time. Both K and J are growing rapidly.

### 5. Model dependency

The main algorithms and experiments use DINA, local independence and bipartite reactions. The DINO extension is discussed only to illustrate the principles.

### 6. Identification conditions

When all parameters are unknown, Q is incomplete, and question types are not diverse enough, observational equivalent structures may occur.

### 7. Empirical gaps

Full text has no real item bank, content expert review, runtime or downstream classification effects.

### 8. Insufficient implementation information

The original code, random seeds, and key engineering settings are not publicly available.

## Future directions proposed in the original article

- Develop faster optimization algorithms for Big Q;
- Use chunking to reduce calculations;
- Expanded to DINO and other DCMs that meet conditional independence;
- Formal research on hypothesis testing and model selection;
- Add constraints to the known Q entry, item parameters and attribute distribution structure;
- Validate existing Q and model assumptions using the S-framework.

## This site believes that it is worth pursuing further.

These questions are an extension of the limitations of the paper:

1. Use multiple starting points, beam search or reversible jump strategy to measure local solution uncertainty;
2. Provide stability frequencies for \(\Delta S\) and structural modifications through bootstrap;
3. Use item text and response data jointly to solve the semantic anchoring of attribute columns;
4. Use cross-validation to select the highest order, row budget and early stopping threshold of T;
5. Embed Q learning for online new question calibration and continuously monitor the drift of old anchor questions;
6. Split the complete Q recovery rate into entry, row, attribute-level and downstream classification indicators.

## Apply bottom line

Data recommendations should be made in parallel with content analysis. Multiple near-optimal Qs, rare attribute classes, and model misspecifications can all make a single optimal matrix appear overdetermined. The paper itself also recommends examining multiple candidates when the target value is close and selecting a reasonable structure from a substantive perspective.
