# Research questions, contributions and evidence boundaries

## 1. Core issues

Suppose \(N\) is a participant who answers \(J\) binary items and measures \(K\) binary attributes. The attribute profile of each participant cannot be directly observed, and the connection matrix \(Q\) between items and attributes may also be mistakenly set by experts or completely unknown.

Overall mapping of thesis investigation

\[
(Q,\Theta,\boldsymbol p)
\longmapsto
\left\{
\Pr(\boldsymbol R=\boldsymbol r):
\boldsymbol r\in\{0,1\}^{J}
\right\}.
\]

The question is: Can an object on the left be uniquely recovered when the complete response distribution on the right is known? Also included here:

- \(Q\): What attributes are required by the item;
- \(\Theta=(\theta_{j,\boldsymbol\alpha})\): The probability of answering each question correctly for each latent class;
- \(\boldsymbol p=(p_{\boldsymbol\alpha})\): The proportion of each attribute profile in the population.

Uniqueness allows the entire attribute column of \(Q\) to be reordered. The names of attribute 1 and attribute 2 are interchangeable, and the observed data cannot determine the artificial labels.

## 2. Contribution 1: Strict joint identification of DINA

Theorem 1 gives three conditions that are completely determined by \(Q\):

|Conditions|structural requirements|function|
| --- | --- | --- |
| A |\(Q\) includes one set of \(I_K\)|Each attribute has a single attribute anchor question|
| B |After deleting this set of \(I_K\), the \(Q^\star\) and \(K\) columns are different.|The remaining questions can distinguish attribute columns|
| C |Each column contains at least three 1's|Each attribute was measured repeatedly by at least three questions|

After the three are combined, the necessary and sufficient conditions for strict joint identification of DINA's \((Q,\boldsymbol s,\boldsymbol g,\boldsymbol p)\) are formed. Each item cannot be deleted as a whole.

## 3. Contribution 2: Pan-recognition beyond strict recognition

Strict identification requires that every point in the parameter space be unique. Pan-recognition allows a Lebesgue zero test set to lose its uniqueness.

The paper makes a structural classification of the situation in DINA where "an attribute is only measured by two questions" and gives:

-Completely lose the structure of local pan-recognition;
- Local universal recognition established under the condition of extra sub-matrix;
- Global universal recognition established under the condition of extra sub-matrix;
- The completeness of \(K=2\) must be fully characterized.

This level explains a common phenomenon: the same \(Q\) is estimable at most latent class scales, but is extremely unstable when the attribute scale approaches a special algebraic surface.

## 4. Contribution 3: General RLCM

For general RLCMs such as G-DINA, LCDM, and GDM, the paper proposes "pan-completeness":

\[
Q_0\in\{0,1\}^{K\times K}
\]

After appropriate permutations of rows and columns, only the diagonal lines are required to be all 1, and the off-diagonal lines can be 0 or 1.

The D/E condition of Theorem 4 requires two non-overlapping pan-complete \(K\times K\) submatrices, and the remaining questions cover each attribute at least once. Theorem 5 proves that pan-completeness itself is a necessary condition for pan-recognition; D/E further becomes a necessary and sufficient condition for \(K=2\).

## 5. Evidence boundaries

Thesis evidence consists of three parts:

1. Main text theorem and finite sample error bound;
2. All proofs in supplementary materials;
3. Main text, 3 sets of illustrations and supplementary materials, 7 sets of simulations.

The main task of the simulation is to demonstrate theoretical phenomena and does not constitute a large-scale algorithm benchmark:

- No real education data analysis;
- No comparison of recovery rates with various Q-learning algorithms;
- \(5\times2\) The exhaustive experiment mainly displays the likelihood surface;
- The setting of \(N=10^5\) emphasizes behavior close to the population distribution.

Therefore, this article is first a recognition theory paper, and algorithm and empirical comparisons provide numerical verification for the theory.
