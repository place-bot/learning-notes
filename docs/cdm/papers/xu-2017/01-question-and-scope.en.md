# Problem, Contribution and Evidence Boundaries

## Research questions

The student's attribute profile cannot be directly observed. The researcher only saw the answers to the two-point question \(J\). The paper asks:

> When the Q matrix and model constraints are known, can the observed response distribution uniquely determine the success probability of all items and the proportion of all attribute profiles?

Written as mapping is

\[
(\Theta,\boldsymbol p)
\longmapsto
\left\{
P(\boldsymbol R=\boldsymbol r\mid Q,\Theta,\boldsymbol p):
\boldsymbol r\in\{0,1\}^J
\right\}.
\]

If this mapping is one-to-one, the parameters can be identified; if two sets of different parameters produce exactly the same observation distribution, even if the sample size tends to infinity, it is impossible to judge which set is correct from the data.

## Why is the general latent class result not enough?

The identification theory of unconstrained Bernoulli latent class models is usually algebraic geometry or Kruskal's three-way decomposition. Such results often give generic identifiability: apart from an outlier set whose Lebesgue measure is zero, the parameters are generally identifiable.

Many item probabilities of RLCM are forced to be equal by the Q matrix. The constrained parameter space itself may fall into a lower-dimensional set in the unconstrained space. Therefore, the conclusion that "holds almost everywhere" in the unconstrained model cannot automatically cover this entire constrained space.

Xu's goal is to use the restriction structure itself to prove uniqueness in the strict sense.

## Two major contributions

### Sufficient conditions for unity

The paper gives a set of sufficient conditions applicable to various dichotomous reaction diagnostic models:

\[
Q=
\begin{pmatrix}
I_K\\
I_K\\
Q'
\end{pmatrix}
\quad\text{and satisfy C2}.
\]

These conditions transform the abstract problem of parameter identification into test design rules.

### Marginal matrix proof technology

The paper rewrites the complete reaction mode probability as \(T\)-matrix margin:

\[
T(Q,\Theta)\boldsymbol p.
\]

pass again

\[
T(Q,\Theta-\boldsymbol\theta^*\boldsymbol 1^\top)
=
D(\boldsymbol\theta^*)T(Q,\Theta)
\]

Construct a large number of zero elements to isolate the parameters to be identified column by column. This method can directly exploit the equality relationship brought by Q restriction.

## What evidence does the original text provide?

|Evidence type|Is the original text provided?|content|
| --- | :---: | --- |
|strict theorem|Yes|C1, C2 \(\Rightarrow(\Theta,\boldsymbol p)\) can be identified|
|Complete proof|Yes|Main theorem, two propositions, two lemmas|
|non-identifying construct|Yes|DINA parameter family when C1 holds and C2 fails|
|Large sample inference|Yes|Discussion of MLE consistency and asymptotic normality|
|Simulation experiment|No|No sample size, number of repetitions or result table|
|Real data analysis|No|No data set|
|Software implementation|No|No public code address|

## Issues not directly addressed by the paper

- Whether C1 and C2 are necessary in general RLCM;
- generic identifiability on the constrained parameter space when Q is incomplete;
- Attribute hierarchy leads to partial identification of \(p_{\boldsymbol\alpha}=0\);
- Joint identification when the Q matrix is unknown or wrong;
- Numerical stability of parameter estimates under limited samples;
- Identifiability and consistency after item is dynamically selected according to CAT rules.

These boundaries determine that the "Experimental" page at the back of this site will report theoretical evidence and calculation verification, and will not add a set of real data results to the paper that does not exist.
