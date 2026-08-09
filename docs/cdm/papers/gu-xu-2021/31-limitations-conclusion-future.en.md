# Limitations, conclusions and future work

## 1. Conclusion

This paper establishes a joint identification framework under unknown Q scenarios.

### DINA

\[
A+B+C
\]

It is a necessary and sufficient condition for strict joint identification:

- A: Contains \(I_K\);
- B: \(Q^\star\) columns are different from each other;
- C: At least three questions for each attribute.

### DINA pan-identification

When attributes are measured by only two questions, the local structure and latent class dependence of Q determine whether it can be broadly recognized. \(K=2\) is completely necessary and fully characterized.

### General RLCM

- C is a necessary condition for general recognition;
- Pan-completeness is a necessary condition;
- D/E is a sufficient condition;
- D/E is necessary and sufficient for \(K=2\).

## 2. Theoretical limitations

### High-dimensional pan-recognition is still not fully characterized

When \(K>2\), whether the D/E of the general RLCM can be further relaxed, this article does not give a complete conclusion. DINA's Theorem 2 also does not cover all high-dimensional Q structures.

### Full positive latent class ratio

Main result hypothesis

\[
p_{\boldsymbol\alpha}>0
\]

True for all \(2^K\) latent classes. Real education data may only support a small number of attribute profiles, and attribute hierarchy will also force the probability of some patterns to be 0.

### Binary attributes and binary reactions

The main framework focuses on binary attributes and binary items. Multi-level attributes, multi-part items and continuous latent abilities require new parameter spaces and equivalence relationships.

## 3. Experimental limitations

- No real data;
- The main exhaustive scenario is \(K=2,J=5\);
- The sample size is permanently set to \(10^5\), which weakens the problem of small samples;
- The likelihood map is mostly a single simulated data set;
- No system reporting Q recovery rates, running times or algorithm comparisons;
- The G-DINA graph filters out candidates that fail strong monotonic checks.

## 4. Code limitations

- MATLAB driver script relies on the current directory and precomputed `.mat`;
- Part of the precalculated results are not stored in the warehouse;
- Several annotations, Theorem numbers and output text are inconsistent with the final paper;
- Conditional search and Hall enumeration grow rapidly with the number of \(K\) or combinations;
- Some function signatures or early exit paths need to be corrected before they can be reused robustly.

## 5. Original article Future work

The paper proposes:

1. Extend the theory to ordered multi-level attributes;
2. Study models containing both discrete and continuous latent variables;
3. Develop likelihood or Bayesian estimates on the set of Q that satisfy the identification conditions;
4. Research on incomplete Q \(p\)-partial identifiability;
5. Handle forbidden modes caused by attribute hierarchy.

## 6. Interface to the current CAT/generative topic selection direction

This paper does not study adaptive topic selection sequences. It provides the prerequisite constraints for item bank measurement design:

\[
\text{item selection strategy}
\]

Whether given by information volume, reinforcement learning, or generative models, long-term deficiencies in actual administration should be avoided:

- attribute anchor;
- Attribute column distinction;
- Enough to repeat measurements.

For CAT, it is not enough for the complete item bank to satisfy the identification conditions. The adaptive path actually traveled by each student also needs to retain sufficient local identification information. Converting A/B/C or D/E into online sequence constraints is a research problem that can continue to be developed.

## 7. A direction worth extending

Online topic selection can be written as a strategy with structural safety constraints:

\[
j_{t+1}
\sim
\pi_\phi\!\left(
j\mid
\boldsymbol R_{1:t},
Q_{\mathrm{remain}},
\mathcal I_t
\right),
\]

And it is required that the reachable future question set at each time point can still complete some recognition coverage. In this way, generative strategies are responsible for long-term utility, and identifying constraints are responsible for measuring effectiveness.

This extension belongs to the research derivation of this site and was not implemented in Gu and Xu (2021).
