# Limitations, subsequent corrections and future work

## 1. C1 and C2 are strong

The three sets of \(I_K\) are clear and easy-to-check sufficient designs, but in actual item banks there are often multi-attribute questions, and single-attribute questions may be difficult to compile. The main theorem does not claim that a general RLCM can be identified only if it satisfies this design.

Follow-up work continues to look for:

- Weaker Q structural conditions;
- partial identifiability；
- generic identifiability；
- Necessary and sufficient conditions for a specific model.

## 2. Q is considered known and correct

The paper fixes Q and relies on Q to assign attribute semantics to latent class columns. If Q is set incorrectly:

- The probability of items that are forced to be equal may be wrong;
- The C1/C2 review target may also be wrong;
- The strict identifiability conclusion under the fixed tag is not directly portable.

Xu and Shang (2018) advance the problem to the identification and estimation of latent structure matrices and provide examples of likelihood-based methods, simulations and educational data.

## 3. All attribute classes have positive proportions

original hypothesis

\[
p_{\boldsymbol\alpha}>0
\quad\forall\boldsymbol\alpha.
\]

The attribute hierarchy will make certain combinations impossible, resulting in structural zeros. The original article clearly lists extensions under hierarchical attributes as a future direction in Remark 3.

Subsequent theory requires redefining distinguishable columns and anchor conditions on the reduced latent class space.

## 4. Binary response

Model assumes \(R_j\in\{0,1\}\). Multinomial, nominal, or continuous reactions require different conditional probability tensors and identification conditions, which cannot be derived directly from the bisection theorem.

The papers indexed on this site by Lin and Xu and Liu and Culpepper extend along polynomial and nominal reaction directions.

## 5. C2 contains unknown parameters

In general RLCM, C2 is written as

\[
\left(
\theta_{j,\boldsymbol e_k}:j>2K
\right)
\ne
\left(
\theta_{j,\boldsymbol0}:j>2K
\right).
\]

The real \(\Theta\) is not known during the design stage. Three sets of \(I_K\) provide purely structural sufficient conditions; with only two unit blocks, the paper recommends checking C2 empirically after collecting the data. At this time, estimation error also needs to be considered. It is difficult to distinguish between close equality and strict equality in limited samples.

## 6. Theoretical identification and weak identification

As long as the difference is non-zero, C2 holds mathematically:

\[
\theta_{j,\boldsymbol e_k}
-
\theta_{j,\boldsymbol0}
\ne0.
\]

The difference is very small, but limited samples will still cause high correlation, huge standard error, and multiple starting point instability. The paper does not give separation margin or error bound.

## 7. No limited sample experiments

The original text has not been checked:

- RMSE when the C2 difference gradually approaches 0;
- Estimation when class proportions are sparse;
- Recovery performance of different \(N\) under three-unit block conditions;
- What symptoms the software will show when the conditions are not met.

These issues require specialized simulation studies.

## 8. No adaptive data mechanism

The theorem is for the population distribution of fixed \(J\)-dimensional observation vectors. In CAT:

1. Each student only answers a subset of items that depends on history;
2. The exposure probability of different items is determined by policy;
3. Some Q rows may have few observations;
4. The student-level posterior is updated after each answer.

To apply Xu's identification idea to CAT, it is necessary to connect the item bank structural conditions and dynamic exploration coverage. A possible research question is:

> For which anchor questions and Q structures does the adaptive policy need to maintain positive exposure probabilities to continue to identify response models in the population's cumulative data?

This is directly different from studies that generate an entire set of fixed sequences: the next question in CAT is conditioned on the response just received, and the sequence distribution itself results from closed-loop interactions.

## Division of labor for subsequent reading

|Literature|Direction of advancement relative to Xu (2017)|
| --- | --- |
| Xu & Zhang (2016) |Special identification conditions for DINA|
| Xu & Shang (2018) |Identification and estimation of latent structure / Q-shaped structure|
| Gu & Xu (2020) |General RLCM strict and partial identifiability frameworks|
| Culpepper (2023) |Weaker identification conditions for bipartite RLCM|
| Lin & Xu (2024) |Multiple responses DINA|
| Liu & Culpepper (2024) |Nominal response RLCM|

These subsequent results do not make Xu (2017) lose value: it connects Q-restrictions, marginal matrix elimination and rigorous identification systems for the first time, and provides sufficient conditions that can be directly interpreted as test design.
