# Reference and source boundaries

## Main thesis

de la Torre, J. (2008). An empirically based method of Q-matrix validation for the DINA model: Development and applications. *Journal of Educational Measurement, 45*(4), 343--362. [DOI](https://doi.org/10.1111/j.1745-3984.2008.00069.x) · [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/j.1745-3984.2008.00069.x)

The figures on this website about sequential EM-based \(\delta\)-method, Tables 1--9, Figures 1--7, simulation, fraction subtraction, NAEP, conclusions and future work of the original text are all based on the official full text of Wiley.

## DINA and data sources

Junker, B. W., & Sijtsma, K. (2001). Cognitive assessment models with few assumptions, and connections with nonparametric item response theory. *Applied Psychological Measurement, 25*(3), 258--272. [DOI](https://doi.org/10.1177/01466210122032064)

Tatsuoka, K. K. (1990). Toward an integration of item-response theory and cognitive error diagnosis. In N. Frederiksen, R. Glaser, A. Lesgold, & M. G. Shafto (Eds.), *Diagnostic Monitoring of Skill and Knowledge Acquisition* (pp. 453--488). Erlbaum.

Mislevy, R. J. (1996). Test theory reconceived. *Journal of Educational Measurement, 33*(4), 379--416. [DOI](https://doi.org/10.1111/j.1745-3984.1996.tb00498.x)

de la Torre, J., & Douglas, J. A. (2004). Higher-order latent trait models for cognitive diagnosis. *Psychometrika, 69*(3), 333--353. [DOI](https://doi.org/10.1007/BF02295640)

## Follow-up Q verification

de la Torre, J., & Chiu, C.-Y. (2016). A general method of empirical Q-matrix validation. *Psychometrika, 81*(2), 253--273. [DOI](https://doi.org/10.1007/s11336-015-9467-8)

Chiu, C.-Y. (2013). Statistical refinement of the Q-matrix in cognitive diagnosis. *Applied Psychological Measurement, 37*(8), 598--618. [DOI](https://doi.org/10.1177/0146621613488436)

Liu, J., Xu, G., & Ying, Z. (2012). Data-driven learning of Q-matrix. *Applied Psychological Measurement, 36*(7), 548--564. [DOI](https://doi.org/10.1177/0146621612456591)

## Public software implementation

Robitzsch, A., Kiefer, T., George, A. C., & Uenlue, A. `CDM`: Cognitive Diagnosis Modeling. [CRAN](https://cran.r-project.org/package=CDM) · [GitHub](https://github.com/alexanderrobitzsch/CDM)

Key source code:

- [`R/din.validate.qmatrix.R`](https://github.com/alexanderrobitzsch/CDM/blob/master/R/din.validate.qmatrix.R)
- [`src/cdm_rcpp_din_validate.cpp`](https://github.com/alexanderrobitzsch/CDM/blob/master/src/cdm_rcpp_din_validate.cpp)

This implementation uses the EM expected-count and \(1-s-g\) ideas of de la Torre (2008). The current function exhaustively enumerates all non-zero q-vectors; it has different meanings from the path and threshold of the original sequential search.

## Calculation materials on this site

[`tools/de_la_torre_2008_q_validation.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/de_la_torre_2008_q_validation.py)

This script is written by this website and is used to check hypothetical questions, candidate parameters, sequential search, exhaustive search and Table 4 conditions. It does not belong to the author Ox Code.

## Data and recurrence boundaries

This site does not republish fraction subtraction and NAEP individual response data, nor does it claim to recalculate the original real data results. The real data page organizes samples, algorithm settings, tables, graphical values ​​and author explanations of the original report.

