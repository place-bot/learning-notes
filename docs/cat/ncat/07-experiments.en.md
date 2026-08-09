# Experimental design, complete results and result analysis

This page organizes the experiments according to the four research questions of the paper:

- RQ1: Does the measurement efficiency of NCAT exceed existing topic selection algorithms?
- RQ2: What kind of questions will NCAT choose, and how will the coverage of knowledge points change?
- RQ3: Can dual-channel networks capture complex response relationships and guess/error perturbations?
- RQ4: What are the roles of Performance Learning, Contradiction Learning and temperature randomization?

## 1. Data set

The paper uses three real education data sets:

|Data set|Source and content|
|---|---|
| ASSIST |Mathematics practice logs and item knowledge points in the ASSISTments online tutoring system|
| EXAM |Junior high school mathematics answering in online homework, examination and evaluation system|
| NIPS-EDU |Student question answering data from the Eedi platform in NeurIPS 2020 Education Challenge|

The main text of the paper does not report the number of students, items, and interactions of the three preprocessed data sets, so these numbers cannot be inferred from the result table of the main text. The ASSIST preprocessing metadata included with the public repository records a code snapshot:

|Statistics|Warehouse `assist1213/info_filtered.yml`|
|---|---:|
|Number of students| 20,785 |
|number of items| 15,069 |
|knowledge points| 163 |
|Number of answers after removing duplicates| 1,915,861 |
|Average number of questions per student| 92.18 |

This set of values is used to understand the scale of warehouse data; it does not constitute a complete statistical table of the three data sets of the paper.

## 2. Data division and evaluation process

The paper conducts 5-fold cross-validation. Per discount:

1. Students are divided into training, verification and testing according to 60%/20%/20%;
2. Each student’s answer is divided into support/query according to 70%/30%;
3. Randomly re-divide support/query within the training epoch;
4. The topic selection algorithm only selects topics one by one from the support candidates;
5. The response model updates student parameters with the selected questions and corresponding answers;
6. Predict responses on query questions;
7. Report ACC and AUC in steps 5, 10, and 20.

Response models include:

- IRT；
- NCDM。

MFI and KLI rely on IRT, so there is no result in the NCDM column.

## 3. Comparison method

|method|core criterion|Dependence on response model|
|---|---|---|
| RAND |Randomly select topics|model independent|
| MFI |Max Fisher Information| IRT |
| KLI |KL information of neighbor ability posterior| IRT |
| MAAT |Anticipate model changes and diversity|model independent|
| BOBCAT |Double-layer optimization learning topic selection strategy|model independent|
| NCAT |Q-learning and dual-channel attention|model independent|

## 4. Hyperparameter and operating conditions

Thesis report:

|item|settings|
|---|---:|
|Maximum test length| \(T=20\) |
|embedding dimension| \(d=128\) |
| RL learning rate | 0.001 |
|Test temperature| \(\nu_t=2^{-0.1t}\) |
|replay buffer capacity| 10,000 |
|training exploration|\(\varepsilon\) decays from 1 to 0|
|Equipment| Tesla K20m GPU |
|hyperparameter selection|Subject to the optimal validation set|

The item parameters are first estimated on the training set and then used as global item parameters in the CAT simulation.

## 5. RQ1: ACC complete result

### ASSIST

|response model|method|Step 5|Step 10|Step 20|
|---|---|---:|---:|---:|
| IRT | RAND | 0.720 | 0.717 | 0.724 |
| IRT | MFI | 0.722 | 0.730 | 0.741 |
| IRT | KLI | 0.723 | 0.730 | 0.742 |
| IRT | MAAT | 0.723 | 0.729 | 0.742 |
| IRT | BOBCAT | 0.726 | 0.733 | 0.749 |
| IRT | **NCAT** | **0.733** | **0.748** | **0.756** |
| NCDM | RAND | 0.704 | 0.710 | 0.721 |
| NCDM | MAAT | 0.727 | 0.731 | 0.749 |
| NCDM | BOBCAT | 0.730 | 0.741 | 0.749 |
| NCDM | **NCAT** | **0.735** | **0.754** | **0.756** |

### NIPS-EDU

|response model|method|Step 5|Step 10|Step 20|
|---|---|---:|---:|---:|
| IRT | RAND | 0.629 | 0.658 | 0.687 |
| IRT | MFI | 0.646 | 0.676 | 0.706 |
| IRT | KLI | 0.646 | 0.672 | 0.702 |
| IRT | MAAT | 0.648 | 0.674 | 0.713 |
| IRT | BOBCAT | 0.656 | 0.681 | 0.723 |
| IRT | **NCAT** | **0.661** | **0.703** | **0.732** |
| NCDM | RAND | 0.621 | 0.663 | 0.692 |
| NCDM | MAAT | 0.643 | 0.681 | 0.718 |
| NCDM | BOBCAT | 0.663 | 0.695 | 0.724 |
| NCDM | **NCAT** | **0.674** | **0.716** | **0.733** |

### EXAM

|response model|method|Step 5|Step 10|Step 20|
|---|---|---:|---:|---:|
| IRT | RAND | 0.721 | 0.754 | 0.810 |
| IRT | MFI | 0.750 | 0.775 | 0.838 |
| IRT | KLI | 0.756 | 0.784 | 0.843 |
| IRT | MAAT | 0.759 | 0.797 | 0.845 |
| IRT | BOBCAT | 0.766 | 0.799 | 0.844 |
| IRT | **NCAT** | **0.781** | **0.817** | **0.852** |
| NCDM | RAND | 0.723 | 0.762 | 0.814 |
| NCDM | MAAT | 0.762 | 0.800 | 0.846 |
| NCDM | BOBCAT | 0.771 | 0.810 | 0.844 |
| NCDM | **NCAT** | **0.784** | **0.824** | **0.855** |

## 6. RQ1: AUC complete result

### ASSIST

|response model|method|Step 5|Step 10|Step 20|
|---|---|---:|---:|---:|
| IRT | RAND | 0.688 | 0.698 | 0.710 |
| IRT | MFI | 0.699 | 0.710 | 0.730 |
| IRT | KLI | 0.700 | 0.710 | 0.732 |
| IRT | MAAT | 0.711 | 0.712 | 0.735 |
| IRT | BOBCAT | 0.716 | 0.720 | 0.742 |
| IRT | **NCAT** | **0.719** | **0.732** | **0.755** |
| NCDM | RAND | 0.689 | 0.697 | 0.719 |
| NCDM | MAAT | 0.714 | 0.721 | 0.744 |
| NCDM | BOBCAT | 0.718 | 0.736 | 0.746 |
| NCDM | **NCAT** | **0.721** | **0.739** | **0.752** |

### NIPS-EDU

|response model|method|Step 5|Step 10|Step 20|
|---|---|---:|---:|---:|
| IRT | RAND | 0.655 | 0.687 | 0.723 |
| IRT | MFI | 0.673 | 0.707 | 0.746 |
| IRT | KLI | 0.671 | 0.703 | 0.739 |
| IRT | MAAT | 0.673 | 0.703 | 0.748 |
| IRT | BOBCAT | 0.684 | 0.710 | 0.757 |
| IRT | **NCAT** | **0.689** | **0.731** | **0.760** |
| NCDM | RAND | 0.659 | 0.699 | 0.726 |
| NCDM | MAAT | 0.671 | 0.714 | 0.747 |
| NCDM | BOBCAT | 0.691 | 0.720 | 0.762 |
| NCDM | **NCAT** | **0.704** | **0.739** | **0.766** |

### EXAM

|response model|method|Step 5|Step 10|Step 20|
|---|---|---:|---:|---:|
| IRT | RAND | 0.671 | 0.692 | 0.768 |
| IRT | MFI | 0.695 | 0.719 | 0.783 |
| IRT | KLI | 0.706 | 0.729 | 0.787 |
| IRT | MAAT | 0.701 | 0.735 | 0.791 |
| IRT | BOBCAT | 0.707 | 0.737 | 0.791 |
| IRT | **NCAT** | **0.712** | **0.749** | **0.802** |
| NCDM | RAND | 0.679 | 0.702 | 0.779 |
| NCDM | MAAT | 0.702 | 0.738 | 0.798 |
| NCDM | BOBCAT | 0.711 | 0.742 | 0.792 |
| NCDM | **NCAT** | **0.713** | **0.759** | **0.815** |

Notes in the paper table: The improvement of the bold result relative to the best baseline passes the two-sided \(t\) test, and the condition is \(p<0.01\). The main text of the paper does not also provide the standard deviation, confidence interval, or value of each fold, so the test cannot be independently recalculated from Table 1.

### How to read RQ1 result

1. NCAT achieves the highest ACC/AUC in the table across three data sets, two response models, and three test lengths.
2. Step 5 has been improved, indicating that the advantage does not only come from longer trajectories.
3. BOBCAT is usually better than manual criterion and supports the direction of "learning topic selection from historical data".
4. The gap between NCAT and BOBCAT is widespread, but the absolute magnitude ranges from thousandths to hundredths; the actual significance needs to be combined with question number savings, error costs and repeated experimental judgments.
5. ACC/AUC measures query response prediction and is a proxy of ability estimate. They do not directly give parameter recovery error, classification consistency, or decision risk.

## 7. RQ2: Knowledge point coverage

Let all knowledge points be

\[
\mathcal K=\{k_1,\ldots,k_{|\mathcal K|}\},
\]

The set of selected questions in the previous \(t\) step is \(\mathcal J_t\). Thesis definition:

\[
\operatorname{Cov}_t(\pi)
=
\frac{1}{|\mathcal K|}
\sum_{k\in\mathcal K}
\mathbb I
\left(
k\text{Be}\mathcal J_t\text{Cover at least one question in}
\right).
\tag{1}
\]

Figure 3 of the paper shows that on ASSIST, the concept coverage curve of NCAT grows faster and approaches 1 in both IRT and NCDM environments. The paper analyzes this: RL exploration and item combination diversity help to form a more comprehensive measurement.

This result is an empirically emergent phenomenon. NCAT's reward does not directly include the content blueprint, and formula (1) only counts "at least one occurrence", without guaranteeing the proportion, lower limit, upper limit, or measurement accuracy of each content.

## 8. RQ3: Response contradiction and noise robustness

### contradiction score visualization

The paper displays the contradiction score matrix of a student's first 7 responses in EXAM, and lists the item difficulty and knowledge points at the same time.

One pair of "more difficult questions answered correctly and related easier questions answered incorrectly" received a higher score, while a question pair with a similar difficulty relationship but low correlation between knowledge points received a smaller score. The authors explain this as the network simultaneously leveraging difficulty relationships and semantic/knowledge point connections to identify potential guesses/slips.

This visualization shows the internal attention structure in a case and cannot prove that the attention score alone is the identifiable guess probability.

### Simulate guess/slip

The paper conducts capability recovery simulation in EXAM's IRT environment:

- Use the ability parameter estimated from the full data as ground truth;
- Generate reaction;
- The original incorrect response will be converted into correct with 25% probability, simulating guess;
- The originally correct response will be turned into an error with a 5% probability, simulating slip;
- use

\[
\operatorname{MSE}
=
\mathbb E
\left[
\left\|
\widehat\theta-\theta^0
\right\|^2
\right]
\tag{2}
\]

Compare the ability errors of different topic selection algorithms as the test steps change.

Figure 4(b) of the paper reports that NCAT’s MSE curve performs well under these perturbations, thereby supporting its noise robustness. The main text does not give the point-by-point values ​​and intervals of the curve.

## 9. RQ4: Ablation experiment

Ablation compares ACC under IRT, \(T=20\):

|structure| ASSIST | NIPS-EDU | EXAM |
|---|---:|---:|---:|
| Default NCAT | 0.7562 | 0.7321 | 0.8516 |
|NCAT-C: Contradiction Learning only| 0.7415 | 0.7059 | 0.8351 |
|NCAT-P: Performance Learning only| 0.7508 | 0.7235 | 0.8417 |
|\(\nu\to0\): deterministic argmax| 0.7586 | 0.7329 | 0.8530 |

Both modules reduce ACC when used alone, and the complete dual-channel structure performs better. The ACC of the deterministic strategy is slightly higher than that of the default temperature strategy, indicating that randomization comes at a small cost in prediction accuracy.

## 10. Exposure result

The paper reports the average item exposure rate in the ASSIST simulation:

|method|average exposure|
|---|---:|
| MFI | 14.4% |
| MAAT | 13.9% |
| BOBCAT | 16.3% |
| **NCAT，\(\nu_t=2^{-0.1t}\)** | **5.2%** |
| NCAT，\(\nu\to0\) | 15.1% |

Default temperature sampling significantly reduces the average exposure in the table, while deterministic argmax is close to other methods. An empirical trade-off between accuracy and exposure can be seen in combination with ablated ACC.

Average exposure is still not enough to describe item bank security. The formal evaluation should also report:

- Maximum item exposure rate;
- Quantile or Gini coefficient of the exposure distribution;
- Exposure stratified by groups and content categories;
- Risk of item leakage during repeated testing;
- Accuracy after forcing maximum exposure constraint.

## 11. The conclusion boundaries supported by the paper’s experiments

The paper provides three types of evidence:

1. In the support/query simulation of historical logs, NCAT improves query ACC/AUC;
2. Concept coverage and average exposure results show that its trajectories have higher diversity;
3. Synthetic guess/slip perturbation and module ablation support the role of dual-channel structures.

Evidence that remains to be added includes:

- The new strategy changes the online effect of item presentation distribution;
- Cold start for items outside the bank or new questions;
- Content blueprint, problem, time and maximum exposure hard constraints;
- Calibration, fairness and uncertainty of ability parameters and classification decisions;
- Ablation of multiple random seeds, full error bars and modern DQN stabilization;
- OPE related to old logging policy bias.

How to implement these formulas in the code, see [Official Code Intensive Reading and Minimum Implementation](08-implementation.md).
