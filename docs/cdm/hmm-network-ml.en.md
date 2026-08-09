# HMM, network and machine learning background

This page does not serve as the main line of CDM, but retains relevant background literature. They help understand hidden-state models, stochastic block models, clustering, and EM-like semi-supervised learning.

## hidden Markov model and probabilistic automata

|reading level|Literature|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|main reading| Cappé, Moulines & Rydén (2005). Inference in Hidden Markov Models. | `cdm/papers/cappe-moulines-ryden-2005-hmm.md` |Systems background for HMM inference, EM and state estimation.|
|main reading| Ephraim & Merhav (2002). Hidden Markov processes. | `cdm/papers/ephraim-merhav-2002-hidden-markov-processes.md` |A theoretical review of hidden Markov processes.|
|background| Gilbert (1959). On the identifiability problem for functions of finite Markov chains. | `cdm/papers/gilbert-1959-markov-identifiability.md` |Early HMM/Markov function recognition problems.|
|background| Petrie (1969). Probabilistic functions of finite state Markov chains. | `cdm/papers/petrie-1969-probabilistic-functions.md` |Complementary to Gilbert, read the relevant sections on identifiability.|
|background| Paz (1971). Introduction to Probabilistic Automata. | `cdm/papers/paz-1971-probabilistic-automata.md` |Basic background of probabilistic automata.|
|background| Finesso (1991). Consistent estimation of the order for Markov and hidden Markov chains. | `cdm/papers/finesso-1991-markov-order.md` |Model order estimation background.|
|background| Leroux (1992). Maximum-likelihood estimation for hidden Markov models. | `cdm/papers/leroux-1992-hmm-mle.md` |HMM maximum likelihood estimation (maximum likelihood estimation) background.|
|background| Chambaz & Matias (2009). Number of hidden states and memory: A joint order estimation problem for Markov chains with Markov regime. | `cdm/papers/chambaz-matias-2009-hidden-states-memory.md` |Joint estimation of number of hidden states and memory order.|

## Networks, block models and classification

|reading level|Literature|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|main reading| Nowicki & Snijders (2001). Estimation and prediction for stochastic blockstructures. | `cdm/papers/nowicki-snijders-2001-stochastic-blockstructures.md` |Estimation and prediction of stochastic blockstructures.|
|main reading| Daudin, Picard & Robin (2008). A mixture model for random graphs. | `cdm/papers/daudin-picard-robin-2008-random-graphs.md` |Random graph mixture model, which overlaps with latent class/block model.|
|background| Zanghi, Ambroise & Miele (2008). Fast online graph clustering via Erdős-Rényi mixture. | `cdm/papers/zanghi-ambroise-miele-2008-graph-clustering.md` |Graph clustering and online estimation of background.|
|background| Frank & Harary (1982). Cluster inference by using transitivity indices in empirical graphs. | `cdm/papers/frank-harary-1982-cluster-inference.md` |An early background on graph clustering and transitivity indices.|
|background| Glick (1973). Sample-based multinomial classification. | `cdm/papers/glick-1973-multinomial-classification.md` |Classic background for multinomial classification.|
|background| Tallberg (2005). A Bayesian approach to modeling stochastic blockstructures with covariates. | `cdm/papers/tallberg-2005-bayesian-blockstructures.md` |Bayesian block models with covariates.|

## machine learning background

|reading level|Literature|The position of subsequent single notes|pronunciation|
| --- | --- | --- | --- |
|main reading| Nigam, McCallum, Thrun & Mitchell (2000). Text classification from labeled and unlabeled documents using EM. | `cdm/papers/nigam-mccallum-thrun-mitchell-2000-text-em.md` |Semi-supervised text classification and EM learning, suitable for comparison with Q-matrix text classification methods.|

## Relationship with CDM

The literature on this page is mainly used for the background of the complementary method and does not directly determine the main line of the CDM chapter. You can quote as needed when writing later:

- HMM literature: for understanding hidden state identification and dynamic CDM.
- Network literature: for understanding latent block structure and clustering.
- Machine learning literature: for understanding text-assisted Q matrix learning and AI-assisted Q matrix development.
