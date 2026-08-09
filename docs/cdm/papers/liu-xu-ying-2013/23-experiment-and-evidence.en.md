#Experiment: A complete inventory of the original evidence

## First explain the evidence type

This *Bernoulli* paper is 28 pages long and has the following structure:

1. Introduction；
2. Model specifications and basic results；
3. DINA model with known slipping and guessing parameters；
4. Extension to unknown slipping probabilities；
5. Discussion；
6. Proofs of the theorems；
7. Appendix: Technical proofs。

The original text does not have Simulation, Experiment, Application or Real Data chapters, nor does it have experimental tables, result graphs, data sets and numerical comparisons.

Therefore, this topic cannot report the original text:

- sample size condition;
-Number of repetitions;
- Dataset name;
- Recovery rate table;
- Baseline method;
- running time;
- Real data conclusions.

None of these items appear in the paper.

## How to provide evidence in the original text

The evidence chain of the paper consists of four parts.

### 1. Constructive example

Section 2.3 Use three questions and two attributes of addition-multiplication Q to demonstrate:

\[
T(Q)\widehat{\boldsymbol p}
=
\boldsymbol\alpha.
\]

This example explains how the estimator is formed, but does not use random data to evaluate performance.

### 2. Three main theorems

|situation|result|
| --- | --- |
|No mistakes, no guesswork|Theorem 2.4: Q equivalence classes consistent with attribute distributions|
|\(c,g\) known|Theorem 3.1: Q equivalence classes consistent with attribute distributions|
|\(g\) known, \(c\) unknown|Theorem 4.2: Q equivalence class is consistent; \(p\) is consistent and \(c\) is estimated to be consistent.|

### 3. Six propositions and one lemma

- Propositions 6.1--6.2: Full column rank;
- Propositions 6.3--6.4: Guess-free column space separation;
- Corollary 6.5: Aggregate candidate Q;
- Proposition 6.6: Augmented column space separation with guessing;
- Lemma 6.7: Linear row transformation preserves column space inclusion relationships.

### 4. Counterexamples and dimensionality arguments

The original text uses the following examples to mark the boundaries of the conclusion:

- Q cannot be recognized when everyone is in full mastery mode;
- When two attributes are always synchronized, the related columns cannot be distinguished;
- When \(Q=I_k\), the parameter dimension of \((p,c)\) exceeds the observation degrees of freedom;
- Unknown \(g_i\) requires additional conditions and analysis.

## How should the original result be expressed?

It can be accurately said:

> Under the conditions of fixing \(m,k\), C1--C5, DINA and corresponding item parameters, the global moment distance minimization estimator constructed in this paper is consistent with the column permutation equivalence class of Q.

It cannot be claimed based on this:

- Small sample recovery rate is very high;
- Low-order cutoffs are equally effective as saturation moments;
- Local search can stably find the global solution;
- Unknown \(c,g\) can be reliably estimated;
- The method has been verified on real tests;
- Computation is scalable to large scale Q.

## How should the "Experimental Design" column of the original text be recorded?

|item|Verify result|
| --- | --- |
|Data generation model|Theorem level stipulates the noiseless conjunctive model and DINA|
|simulated data|None|
|real data|None|
|Data set|None|
|Experimental conditions|None|
|comparison method|None|
|Evaluation indicators|None|
|Tables and Figures|None|
|main evidence|Consistency theorem, column space proposition, counterexample|

##Why does this site do additional numerical verification?

Matrix objects in theoretical derivation can be directly computed on a small scale. Script check on this site:

1. The saturated \(T(Q)\) full column rank of the complete Q;
2. D transformation transforms the augmented \(T_{c,g}\) into \((0,T_{c-g})\);
3. Column permutation produces the same overall moment;
4. In the small examples of enumeration, only the true equivalence class achieves zero overall loss;
5. When C4 fails, all candidates can match the full master population;
6. Under a fixed teaching setting, the recovery rate increases with \(N\).

These checks help understand the formula and troubleshoot implementation errors. They are new additions to this site and cannot replace general proofs, nor can they be included in the original results.

## Complementary to the experiments of the 2012 paper

If you need to observe limited sample performance, you should read the 2012 paper by the same author. That article gives:

- Three Q design;
- Multiple sample sizes;
- Early stopping rules;
- Relevant and uneven attributes;
- Partially known Q;
- Recovery rate table and curve.

The 2013 paper complements the identification and consistency basis of this research direction. The two articles together form a relatively complete chain of "practical algorithm + simulation evidence + theoretical guarantee", but there are still differences between the specific algorithm and the theoretical global estimator.

[Next page: Code status and implementation intensive reading](24-code-implementation.md)
