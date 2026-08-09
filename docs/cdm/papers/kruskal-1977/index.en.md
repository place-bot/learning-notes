# Kruskal (1977) Reading Guide

## Original information

|item|content|
| --- | --- |
|Paper| Joseph B. Kruskal. *Three-way Arrays: Rank and Uniqueness of Trilinear Decompositions, with Application to Arithmetic Complexity and Statistics*. |
|Journal| *Linear Algebra and its Applications*, 18(2), 95--138, 1977 |
| DOI | [10.1016/0024-3795(77)90069-6](https://doi.org/10.1016/0024-3795(77)90069-6) |
|Publisher page| [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0024379577900696) |
|open index|[CORE Record and Full Text Index](https://core.ac.uk/outputs/82529515)|
|Paper type|Multilinear algebra and uniqueness theory; no data sets, simulation experiments, or empirical comparisons|
|official code|Not provided|

This paper simultaneously studies three interrelated things that need to be strictly distinguished:

1. How to define the rank of a three-way array;
2. How to establish a lower bound for the rank of a three-way array;
3. When does a trilinear decomposition only have two types of ambiguity: displacement and scaling?

The CDM literature most often refers to Part 3, later written as

\[
k_A+k_B+k_C\ge 2R+2
\]

Kruskal's uniqueness condition. The original article is broader in scope and also discusses slab-space, tensor rank lower bounds, arithmetic complexity, and statistical models.

## One sentence main line

\[
\underbrace{\mathcal X
=\sum_{r=1}^{R}
\boldsymbol a_r\otimes\boldsymbol b_r\otimes\boldsymbol c_r}
_{\text{an observable three-way array}}
\quad+\quad
\underbrace{k_A+k_B+k_C\ge2R+2}
_{\text{All three directions are difficult enough to confuse}}
\]

\[
\Longrightarrow
\quad
\underbrace{A,B,C\text{can be}\mathcal X\text{restore}}
_{\text{Allows co-displacement and mutually canceling scaling}}.
\]

For latent class models, the common permutation corresponds to class label exchange; the normalization constraints of the probability vector can be fixedly scaled. Therefore, this algebraic theorem becomes the underlying tool for Allman et al. and a large number of CDM identifiability proofs.

## Recommended reading order

1. [Question and historical location](01-question-and-history.md): Why is it easy to have multiple solutions to matrix decomposition, and what constraints are added to the three-way array.
2. [Three-way array, triad and rank](02-array-rank-and-slabs.md): Letter-by-letter explanation of \(X,I,J,K\), slab, \(\dim_\ell\) and tensor rank.
3. [Triple products and inherent ambiguity](03-triple-product.md): Write clear \([A,B,C]\), CP/PARAFAC representation, permutation and scaling.
4. [Kruskal rank](04-kruskal-rank.md): Explain the difference and calculation method between \(k\)-rank and ordinary matrix rank.
5. [Core uniqueness theorem](05-uniqueness-theorem.md): Theorem 4a, reading of conditions, conclusion and boundary.
6. [Proof idea](06-proof-roadmap.md): The main line of the substitution lemma of the original text, and Rhodes’ modern slice-projection proof.
7. [Theoretical results and applications](07-results-and-applications.md): rank lower bound, arithmetic complexity, statistical model and evidence boundary.
8. [Complete hand calculation example](08-worked-examples.md): a satisfying decomposition of \(R=3\) and a multi-solution counterexample.
9. [Computable check](09-computational-check.md): Run the script on this site to accurately calculate the equivalence between \(k\)-rank and tensor.
10. [Interface with CDM](10-cdm-connection.md): three-piece item response, potential attribute profile, label replacement and Q matrix.
11. [Symbol table](11-symbols.md): unified query of original symbols, modern symbols, dimensions and meanings.
12. [Summary and follow-up questions](12-summary.md): Conclusions, limitations and their development in subsequent papers.
13. [Reference](references.md): The original text and this topic are used to explain the direct source of the proof.

## How to deal with the original text and subsequent proofs in this topic

Kruskal's original proof is long, and Theorem 4 also contains 4a, 4b, 4c and other versions from simple to complex. This site is organized into two levels:

- The abstract, definitions, rank lower bounds, Theorem 4a, application scope and historical conclusions of the original article are as per the 1977 thesis statement;
- The proof page uses the open version of Rhodes (2010) to explain the same theorem, since it writes the key slicing, projection, and induction steps more compactly.

Subsequent certifications will clearly indicate the source. Theorem 4b and 4c have more detailed conditions than 4a. This topic explains their status, but the CDM main line first fully masters the most commonly used 4a.

!!! warning "Evidence form of theoretical conclusion"
    The proof of this paper consists of definitions, lemmas, theorems, and proofs. The paper does not have a training set, test set, accuracy table or software warehouse. The scripts on this site only reproduce algebraic checks and do not mean that the original author provided numerical algorithms.
