# Reference and source verification

## Core paper

Liu, J., Xu, G., & Ying, Z. (2013). Theory of self-learning Q-matrix. *Bernoulli, 19*(5A), 1790--1817. [DOI](https://doi.org/10.3150/12-BEJ430) · [PubMed Central  full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4011940/) · [arXiv](https://arxiv.org/abs/1010.6120)

This site has verified the electronic reprint of the published version on page 28:

- Title, author, volume, page number and DOI;
- All models, estimators and theorems in Sections 2--4;
- The conclusions of Section 5 and future work;
- Propositions 6.1--6.6, Lemma 6.7 and three theorems proofs of Section 6;
- Technical proofs of Propositions 6.3--6.4 in Appendix;
- The original text does not have the evidence boundary of experiments, datasets, charts and code entry.

## Directly related papers

Liu, J., Xu, G., & Ying, Z. (2012). Data-driven learning of Q-matrix. *Applied Psychological Measurement, 36*(7), 548--564. [DOI](https://doi.org/10.1177/0146621612456591) · [ Read](../liu-xu-ying-2012/index.md) carefully on this website.

Chiu, C.-Y., Douglas, J. A., & Li, X. (2009). Cluster analysis for cognitive diagnosis: Theory and applications. *Psychometrika, 74*, 633--665. [DOI](https://doi.org/10.1007/s11336-009-9125-0)

de la Torre, J. (2008). An empirically based method of Q-matrix validation for the DINA model: Development and applications. *Journal of Educational Measurement, 45*(4), 343--362. [DOI](https://doi.org/10.1111/j.1745-3984.2008.00069.x) · [ Read](../de-la-torre-2008/index.md) carefully on this website.

Junker, B. W., & Sijtsma, K. (2001). Cognitive assessment models with few assumptions, and connections with nonparametric item response theory. *Applied Psychological Measurement, 25*(3), 258--272. [DOI](https://doi.org/10.1177/01466210122032064)

Rupp, A. A., Templin, J. L., & Henson, R. A. (2010). *Diagnostic Measurement: Theory, Methods, and Applications*. Guilford Press.

Tatsuoka, K. K. (2009). *Cognitive Assessment: An Introduction to the Rule Space Method*. Routledge.

## Realized on this site

Independent teaching script:

[`tools/liu_xu_ying_2013_theory_check.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/liu_xu_ying_2013_theory_check.py)

Realize the use of NumPy and SciPy, covering:

- ideal response and saturated T-matrix;
- Experience joint positive response matrix;
- Optimization of the pure form constraint cross-section;
- Q column replacement equivalent class;
- The explicit exclusion matrix D of Proposition 6.6;
- Small-scale overall separation enumeration;
- C4 failure counterexample;
- Demonstration of a limited sample of fixed seeds.

The script is independently written by this website. The original paper does not publish the source code, and the numerical results on this website are not included in the original evidence of the paper.
