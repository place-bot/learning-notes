# de la Torre & Chiu (2016) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Jimmy de la Torre & Chia-Yi Chiu. *A General Method of Empirical Q-matrix Validation*. |
|Journal| *Psychometrika*, 81(2), 253--273, June 2016 |
| DOI | [10.1007/s11336-015-9467-8](https://doi.org/10.1007/s11336-015-9467-8) |
|official version| [Cambridge Core](https://www.cambridge.org/core/journals/psychometrika/article/general-method-of-empirical-qmatrix-validation/678D0AF47D7F25FE8C5899AC12554690) |
|Publish online| 6 May 2015 |
|Original text implementation|The paper report uses Ox; the code download address is not given in the text.|
|Subsequent implementation| [`GDINA::Qval()`](https://wenchao-ma.github.io/GDINA/reference/Qval.html) |

## One sentence conclusion

Given the correct answer probability of a question under all attribute profiles, the examinee is divided into several groups according to the candidate q-vector; the greater the weighted variance of the correct answer probability between groups, the more item distinguishing information retained by the candidate. The paper records this variance as

\[
\varsigma_j^2(\boldsymbol q)
=
\sum_{\boldsymbol\alpha_{\boldsymbol q}}
w(\boldsymbol\alpha_{\boldsymbol q})
\left[
p_j(\boldsymbol\alpha_{\boldsymbol q})-\bar p_j
\right]^2,
\]

again

\[
\operatorname{PVAF}_j(\boldsymbol q)
=
\frac{\widehat{\varsigma}_j^2(\boldsymbol q)}
{\widehat{\varsigma}_j^2(\boldsymbol 1)}
\]

Measures how much variance of the saturated grouping the candidate retains. Among the candidates that reach the threshold, the one with the fewest required attributes becomes the proposal q-vector.

## What does the paper advance on the 2008 approach?

| de la Torre (2008) | de la Torre & Chiu (2016) |
| --- | --- |
|DINA two groups: \(\eta=0,1\)|Multiple reduced attribute groups of G-DINA|
|Indicator \(\delta=1-s-g\)|Indicator \(\varsigma^2\): Success probability variance between groups|
|Add one attribute each round|Exhaust \(2^K-1\) non-zero q-vectors|
|\(\varepsilon\) is the increment of \(\delta\) in two adjacent steps|\(\varepsilon\) is the retention ratio of saturated GDI|
|The theory mainly relies on the DINA structure|Covering the G-DINA family with two lemmas and a theorem|

\(\varepsilon\) in the two papers has different meanings, and the values cannot be directly interchanged.

## Recommended reading order

1. [Research questions, contributions and boundaries](01-question-and-contribution.md)
2. [G-DINA basic and reduced attribute profile](02-gdina-foundation.md)
3. [Five success probability profiles](03-response-profiles.md)
4. [Posterior weight, folded grouping and conditional mean](04-weights-and-collapsing.md)
5. [Definition and statistical explanation of GDI](05-gdi-definition.md)
6. [Table 1 Complete hand calculation and original text formatting error](06-table1-worked-example.md)
7. [appropriate and correct q-vector](07-appropriate-correct-q.md)
8. [Two lemmas, main theorem and proof](08-lemmas-and-theorem.md)
9. [PVAF exhaustive search and threshold](09-pvaf-search.md)
10. [Complete estimation and verification algorithm](10-complete-algorithm.md)
11. [Co-design of simulation experiments](11-simulation-design.md)
12. [Study 1: Five reduction models](12-study1-results.md)
13. [Study 2: Unconstrained G-DINA](13-study2-results.md)
14. [Fraction subtraction real data](14-fraction-data.md)
15. [Real data results and question-by-question explanations](15-fraction-results.md)
16. [Original text Ox and `GDINA::Qval()` code intensive reading](16-code-implementation.md)
17. [This site can calculate and reproduce](17-computational-reproduction.md)
18. [Consistency comments, responses and method positioning](18-consistency-debate.md)
19. [Limitations, conclusions and future work](19-limitations-future.md)
20. [Symbol table](20-symbol-table.md)
21. [Summary and follow-up reading](21-summary.md)
22. [Reference and source boundaries](references.md)

## You should be able to answer after reading

- \(\varsigma^2\) Why is the variance of conditional expectations?
- Why does missing a required attribute only reduce or maintain GDI?
- How can adding extraneous properties be exactly the same as GDI for a correct q-vector?
- How do PVAF threshold and parsimony rules work together to select a row Q?
- How to estimate the posterior weight \(w\) and the complete attribute profile success rate \(p_j(\boldsymbol\alpha)\) from the initial Q?
- What did the two sets of simulations in the paper test?
- Fixed \(\varepsilon=.95\) What is the tension between finite sample performance and asymptotic consistency?
- Where does the current `GDINA` package extend the original algorithm?
