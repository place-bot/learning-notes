# de la Torre (2008) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Jimmy de la Torre. *An Empirically Based Method of Q-Matrix Validation for the DINA Model: Development and Applications*. |
|Journal| *Journal of Educational Measurement*, 45(4), 343--362, 2008 |
| DOI | [10.1111/j.1745-3984.2008.00069.x](https://doi.org/10.1111/j.1745-3984.2008.00069.x) |
|official version| [Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1111/j.1745-3984.2008.00069.x) |
|Original text implementation|The thesis report uses Ox programming, and no code download address is given.|
|Subsequent implementation| [CRAN `CDM::din.validate.qmatrix`](https://cran.r-project.org/package=CDM) |

## One sentence conclusion

First fit DINA under the tentative Q matrix, and then use the same group of student attribute profile posterior weights to re-divide each question into two groups according to the candidate q-vector: "has all the required attributes" and "is missing at least one item"; the candidate vectors

\[
\widehat\delta_j=1-\widehat s_j-\widehat g_j
\]

The larger the number, the wider the gap between the two groups in correct answer rates. The paper turns this idea into a Q matrix verification process using a step-by-step attribute search, a threshold \(\varepsilon\), and a small amount of appended EM loops.

## Specific problems solved by this paper

Many CDM analyzes treat the Q matrix given by experts as known input and only check item parameters or reaction residuals. If Q is written incorrectly in a line:

- DINA absorbs structural errors into guessing and slipping;
- The posteriori of student attribute profile will shift accordingly;
- Subsequent item parameters, attribute classification and model fit judgment may be affected;
- Just looking at the fitted DINA parameters, it is difficult to know whether the problem comes from item parameters, attribute definitions or Q lines.

de la Torre provides a data-driven candidate generator: propose a possible q-vector for each question, and use item discrimination to measure whether the candidate improves the separation of the two groups. The author repeatedly emphasizes that the final judgment still needs to be based on the item content, answering process and the opinions of experts in the field.

## Paper contribution

1. Define the empirical validation target with the DINA discrimination \(\delta\) under the candidate q-vector.
2. From exhausting \(2^K-1\) candidates, derive a sequential search that examines at most \(K(K+1)/2\) candidates.
3. Avoid completely re-estimating the model for each candidate vector with the help of posterior expectation counts produced by one EM fit.
4. Use \(\varepsilon\) to control whether to accept new attributes, and select candidate Q based on the average guessing and slipping of the entire test.
5. Use simulations, fraction subtraction, and 2003 NAEP eighth-grade mathematics data to demonstrate that this method can preserve, question, or replace existing Q lines.

## Recommended reading order

1. [Problem, Contribution and Evidence Boundaries](01-question-and-contribution.md)
2. [DINA, Q matrix and ideal response](02-dina-q-foundation.md)
3. [Discrimination index and verification target](03-delta-index.md)
4. [Hypothetical question and exhaustive search](04-hypothetical-exhaustive.md)
5. [Sequential search algorithm](05-sequential-search.md)
6. [EM posterior expectation count](06-em-expected-counts.md)
7. [Complete verification process](07-complete-algorithm.md)
8. [Threshold and final decision](08-epsilon-and-decision.md)
9. [Simulation Experiment Design](09-simulation-design.md)
10. [Simulation result and explanation](10-simulation-results.md)
11. [Fraction subtraction data and design](11-fraction-data.md)
12. [Fractional subtraction result and counterexample](12-fraction-results.md)
13. [NAEP Data and Design](13-naep-data.md)
14. [NAEP result and item case](14-naep-results.md)
15. [Code library to implement intensive reading](15-code-implementation.md)
16. [Computable recurrence](16-computational-reproduction.md)
17. [Limitations, Conclusions and Future Work](17-limitations-future.md)
18. [Symbol table](18-symbols.md)
19. [Summary and follow-up reading](19-summary.md)
20. [Reference and source boundaries](references.md)

## You should be able to answer after reading

- Why does omitting required attributes mainly increase slip, and adding irrelevant attributes mainly increases guess?
- Why can \(\delta=1-s-g\) be compared to candidate q-vectors?
- How can the sequential search of the original text reduce the number of candidates from exponential to quadratic?
- How does the EM posterior allow candidate parameters to be recalculated without repeated complete fittings?
- \(\varepsilon\) What are the risks of being too small or too large?
- What conclusions do each of the three experiments in the paper support?
- Why does the current `CDM` package belong to the "exhaustive version of subsequent implementation"? What is the difference from the original sequential search?

