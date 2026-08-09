# Limitations, conclusions and future work

## Original conclusion

The paper establishes a set of Q self-learning theory for the conjunctive cognitive diagnosis model:

1. Use the saturated joint positive response moment to construct the \(T\)-matrix mapping;
2. Define the column permutation equivalence class of Q;
3. Provide sufficient conditions for completeness, overall diversity and repeated measurement of attributes;
4. Prove the spatial separation of moment sequences corresponding to different Q equivalence classes;
5. Construct consistent estimators for the three situations of noise-free, known \(c,g\), and unknown \(c\).

It advances "Q can be corrected by the data" into a testable mathematical proposition: the model needs to be specified, the structural conditions made clear, and the false candidates shown to be unable to replicate the true response distribution.

## Limitation 1: Completely diverse overall

C4 requires all attribute profiles to have positive probability. Real learning groups often have prerequisite relationships. For example, people who master advanced skills almost always master basic skills, and some patterns may be structurally missing.

The original article suggested adding structural restrictions compatible with attribute hierarchy to Q at this time. In the addition-multiplication example, if mastering multiplication must be accompanied by mastering addition, we can require that all questions testing multiplication also require addition. Then Q may no longer be complete, and the recognition theory needs to be re-established.

## Limitation 2: Expert information has not yet been systematically integrated

The author recommends using expert Q as a penalty or search center:

\[
S(Q)+\lambda\,\operatorname{penalty}(Q,Q_0).
\]

Reliable prior information can:

- Improve limited sample accuracy;
- Narrow the candidate space;
- Provide semantic labels for attribute columns;
- Reduce the difficulty of attribute column alignment.

How to choose punishment and \(\lambda\) is left for subsequent research.

## Limitation 3: The number of attributes is known

Full text fixed \(k\). The authors suggest using a BIC-like dimensionality penalty while estimating:

\[
(k,Q).
\]

This needs to deal with the problem that the number of latent classes, parameter dimensions and candidate spaces change under different \(k\).

## Limitation 4: Identification of additional parameters

This article treats \(\boldsymbol p,\boldsymbol c\) as a parameter accompanying Q. Given Q, the joint identifiability of \((\boldsymbol p,\boldsymbol c,\boldsymbol g)\) itself remains an important issue.

In particular:

- Unknown strict theory of \(g_i\);
- \((p,c)\) Structural constraints when there are too many dimensions;
- Identification of more general CDM item parameters;
- Analysis of propagation of parameter estimation errors to Q selection.

## Limitation 5: No convergence speed

Theorem gives

\[
\Pr(\widehat Q\sim Q)\to1,
\]

but did not give:

- Exponential error rate;
- Finite sample upper bound;
- Minimum effect of \(c_i-g_i\);
- The role of minimum attribute profile probability;
- Conditions when \(m,k\) grows with \(N\).

The original article lists convergence speed as an important direction in both theory and practice.

## Limitation 6: Combination optimization is expensive

Full space evaluation needs to be faced

\[
2^{mk}
\]

level candidate. The author proposed blocking, low-order moments and expert neighborhoods, but did not give an efficient global algorithm and its consistency.

Further research can be done on:

- Mixed integer optimization;
- branch-and-bound；
- Provable local updates;
- Continuous slack and sparse penalties;
- Variational and Bayesian structure search;
- Candidate generation of neural or energy models, then verified using moment conditions.

## Original article Six Future Work

Discussion clearly stated:

1. Modify the conditions when the overall attribute profile is not completely diverse;
2. Integrate expert Q information;
3. Data-driven estimation of attribute dimensions;
4. In-depth study of the identification and estimation of \(s,g,p\);
5. Study the convergence speed of \(\widehat Q\);
6. Design a more efficient Q search algorithm.

Remark 4.2 also separately proposes a rigorous analysis of unknown guess probabilities.

## The value of reading this paper today

The algorithmic form of this article has become computationally intensive, but the judgment criteria it proposes are still important:

> For a Q-learning method to claim to recover structure, it needs to say when the observation distributions differentiate between different Qs, what inherent symmetries are there in the attribute labels, and whether the nuisance parameters absorb structural differences on behalf of erroneous Qs.

For modern machine learning Q estimation, text-to-Q, RBM or generative models, these three problems still exist. High prediction accuracy does not automatically give structural identity.

[Next page: Symbol table](27-symbol-table.md)
