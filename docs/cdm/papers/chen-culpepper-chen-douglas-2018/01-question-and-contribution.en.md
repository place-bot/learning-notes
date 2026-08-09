# Research questions, contributions and evidence boundaries

## Research questions

The application of DINA usually begins with a Q sheet assigned by an expert. If question \(j\) requires the \(k\) attribute, let \(q_{jk}=1\). Once Q is misplaced, the ideal response grouping will change, and the error rate, guessing rate, and student attribute classification will all shift accordingly.

The issues dealt with in the paper are:

> Given the binary answer matrix \(\boldsymbol Y\) and the number of attributes \(K\), how to simultaneously estimate Q, item parameters, student attribute profiles and latent class proportions, and ensure that all Q accessed during the estimation process meet the identifiable conditions?

This is an **exploratory DINA** question. Expert Q can participate in the comparison during the interpretation phase, it is not required when the algorithm starts.

## Four substantial contributions

### Contribution 1: Q enters the complete Bayesian model

Thesis is Q designated

\[
p(Q)\propto I(Q\in\mathcal Q),
\]

Put Q with

\[
\boldsymbol s,\quad
\boldsymbol g,\quad
\boldsymbol\alpha,\quad
\boldsymbol\pi
\]

Sample together. \(\mathcal Q\) is a finite set that satisfies the three restrictions of the paper.

### Contribution 2: Constructing a restricted Q proposal

The paper studies three proposed distributions:

- independent proposals;
- Reliance proposal DS1;
- Dependency proposal DS2 for adjustable block size.

DS2 selects \(B\) positions in a column at a time, locking the elements necessary to maintain unit rows, column coverage, and nonzero rows before updating.

### Contribution 3: Prove that the proposal chain can be used for correct MCMC

When \(J-2K\ge2\), Theorem 1 proves that DS2 under \(B=1\) can reach any other state from any \(Q\in\mathcal Q\) in finite steps. Theorem 2 shows that the transfer proposal of DS2 is symmetric, so the MH acceptance probability requires only the posterior ratio.

### Contribution 4: Proposing restricted Gibbs

The paper observes that when \(B=1\), \(q_{jk}\) can be directly updated element by element according to the complete conditional distribution. If flipping would destroy the identifiability, keep the original value; if both 0 and 1 are legal, normalize the sampling according to their conditional likelihood.

## Original evidence

|evidence|content|
| --- | --- |
|theory|DS2 irreducibility; DS2 symmetry|
|Simulation|\(N=500,1000,2000,4000\), \(K=3,4\), \(\rho=0,.05,.15,.25\), 100 times per condition|
|Algorithm comparison|Constrained MH, Constrained Gibbs, Chung (2014) Unconstrained Gibbs|
|Empirical evidence|536 students, 20 fraction subtraction questions; fit \(K=3,4\) respectively|
|code|Essay C++/R; follow-up `edina` R package|

## Evidence Boundary

The theoretical proof of the paper targets the irreducibility and symmetry of the proposed chain and cites the DINA Q identifiability condition of Chen et al. (2015). It does not prove:

- Any chain of finite length is fully mixed;
- The posterior mode will inevitably recover the true Q in small samples;
- The attribute number \(K\) can be automatically identified by the algorithm of this paper;
- The constraints are necessary for DINA Q to be identifiable;
- The algorithm can be directly extended to any general CDM;
- The calculation is still feasible when \(K\) is very large.

The paper also clearly leaves the computational complexity under the growth of \(N,J,K\), the Q posterior aggregation method and extensions other than DINA to subsequent research.

## Significance to the current main line of Q learning

The methods of Liu, Xu and Ying in the first two articles write Q learning as moment matching and discrete optimization; this article instead uses posterior sampling search to identify Q space. Key changes are reflected in the search mechanism and uncertainty expression:

\[
\text{single optimal solution}
\quad\longrightarrow\quad
\text{Posterior samples of Q}.
\]

Posterior samples allow calculation of element-wise inclusion probabilities, whole-matrix modes, and uncertainties in item parameters. The Q-point estimate actually reported in the paper is still the posterior mode of the entire matrix.

[Next page: Relationship with existing Q learning methods](02-relation-to-prior-work.md)
