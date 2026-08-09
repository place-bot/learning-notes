# symbol table

## Overall identification mark

|symbol|type or dimension|meaning|
| --- | --- | --- |
| \(\Theta\) |parameter space|The set of all allowed parameters of the model|
| \(\theta\) |parameter point|a specific set of model parameters|
| \(\Omega\) |sample space|The value space of observable variables|
| \(\mathcal M_1(\Omega)\) |set of probability measures|All probability distribution on \(\Omega\)|
| \(\Psi(\theta)=P_\theta\) |Parametric mapping|Mapping parameters to observed distributions|
| \(\mathcal V\) |algebraic subclusters|Common zero point set of polynomial equations|

## Limited latent class model

|symbol|type or dimension|meaning|
| --- | --- | --- |
| \(Z\) | \(\{1,\ldots,r\}\) |discrete latent class|
| \(r\) |Positive integer, known|number of latent classes|
| \(\pi_i\) |scalar|\(P(Z=i)\), class \(i\) scale|
| \(\boldsymbol\pi\) |\(r\)-Vector|Category scale vector with positive elements and sum to 1|
| \(p\) |positive integer|Number of observed variables|
| \(X_j\) |finite state variables|The \(j\) observed variable|
| \(\kappa_j\) |positive integer|Status number of \(X_j\)|
| \(p_{ij}(\ell)\) |scalar| \(P(X_j=\ell\mid Z=i)\) |
| \(\boldsymbol p_{ij}\) |\(\kappa_j\)-Vector|Conditional distribution of \(X_j\) under class \(i\)|
| \(M_j\) | \(r\times\kappa_j\) |Class conditional probability matrix of the \(j\) variable|
| \(P_i\) |\(\kappa_1\times\cdots\times\kappa_p\) table|Product joint distribution of class \(i\)|
| \(P\) |joint probability table|Overall mixture distribution \(\sum_i\pi_iP_i\)|
| \(\mathcal M(r;\kappa_1,\ldots,\kappa_p)\) |model family|\(r\) class, \(p\) feature limited latent class model|

## Tensors and ranks

|symbol|type or dimension|meaning|
| --- | --- | --- |
| \(\otimes\) |Operation|Vector outer product or Kronecker product|
| \(\otimes_{\mathrm{row}}\) |Operation|Do tensor product row by row for the same row index|
| \([M_1,M_2,M_3]\) |three-way tensor| \(\sum_i\boldsymbol m_{1i}\otimes\boldsymbol m_{2i}\otimes\boldsymbol m_{3i}\) |
| \(\widetilde M_1\) | \(r\times\kappa_1\) | \(\operatorname{diag}(\pi)M_1\) |
| \(\operatorname{rank}(M)\) |integer|Ordinary matrix rank|
| \(\operatorname{rank}_K(M)\) |integer|The maximum number of independent rows for any of this number|
| \(I_j\) |integer|Kruskal rank of \(M_j\)|

## Block theorem

|symbol|type or dimension|meaning|
| --- | --- | --- |
| \(S_1,S_2,S_3\) |Index collection|Three non-empty, disjoint blocks of observation variables|
| \(X_{S_a}\) |composite variable|A joint variable composed of all variables in the \(a\) block|
| \(K_a\) |positive integer|Block status number \(a\) \(\prod_{j\in S_a}\kappa_j\)|
| \(N_a\) | \(r\times K_a\) |Class conditional probability matrix for block \(a\)|
| \(k\) |positive integer|\(\lceil\log_2r\rceil\) in Corollary 5, or HMM left and right window length|

!!! note "Differences in original text notation"
    Original Theorem 4 uses \(k_j\) to represent the number of single-variable states and \(\kappa_a\) to represent the number of block states. Used uniformly on this site
    \(\kappa_j\) represents the number of single variable states, and \(K_a\) represents the number of block states.

## HMM

|symbol|type or dimension|meaning|
| --- | --- | --- |
| \(Z_t\) |\(r\) status|The hidden state of time \(t\)|
| \(X_t\) |\(\kappa\) status|Observation at time \(t\)|
| \(A\) | \(r\times r\) |Hidden state transition matrix|
| \(B\) | \(r\times\kappa\) |emission probability matrix|
| \(\pi\) |\(r\)-Vector|Stationary hidden state distribution|
| \(A'\) | \(r\times r\) |Inverse time transfer matrix \(\operatorname{diag}(\pi)^{-1}A^\top\operatorname{diag}(\pi)\)|
| \(B_1\) | \(r\times\kappa^k\) |Given the left observation block conditional distribution of \(Z_k\)|
| \(B_2\) | \(r\times\kappa^k\) |Given the right observation block conditional distribution of \(Z_k\)|

## Random graph mixing

|symbol|type or dimension|meaning|
| --- | --- | --- |
| \(Z_i\) |Node category|Potential group for node \(i\)|
| \(X_{ij}\) |dichotomous variable|Is there an edge between nodes \(i,j\)|
| \(p_{ab}\) |scalar| \(P(X_{ij}=1\mid Z_i=a,Z_j=b)\) |
| \(G_1,G_2,G_3\) |subplot|Three sets of composite observation variables that do not share edges with each other|

## Non-parametric mixing

|symbol|type or dimension|meaning|
| --- | --- | --- |
| \(\mu_i\) |probability measure|Mixing component \(i\)|
| \(\mu_i^j\) |probability measure|Edge component of class \(i\), direction \(j\)|
| \(F_i^j\) |function|Cumulative distribution function of \(\mu_i^j\)|
| \(I_j^k\) |interval|The \(k\) interval after binning in the \(j\) direction|
| \(Y_j\) |finite state variables|\(X_j\) binning indicator vector|

## CDM corresponding symbols

|CDM symbol|Corresponds to general latent class objects|meaning|
| --- | --- | --- |
| \(\boldsymbol\alpha\) | \(Z=i\) |attribute mastery profile|
| \(\mathcal A\) |latent class set|Allowed attribute profiles|
| \(\nu_{\boldsymbol\alpha}\) | \(\pi_i\) |attribute profile ratio|
| \(Y_j\) | \(X_j\) |item response|
| \(\theta_{j,\boldsymbol\alpha}\) | \(p_{ij}(1)\) |Probability of correct answer given attribute profile|
| \(Q\) |Does not exist in the general model|item and attribute relationship matrix|
| \(g_j,s_j\) |Constrained reaction parameterization|DINA Guess and Error Parameters|

## Quick check on key conditions

\[
I_1+I_2+I_3\ge2r+2
\qquad
\text{Three-way tensor point state uniqueness}
\]

\[
\sum_{a=1}^{3}\min(r,K_a)\ge2r+2
\qquad
\text{Multi-variable three-block recognition}
\]

\[
p\ge2\lceil\log_2r\rceil+1
\qquad
\text{\(r\) Number of sufficient variables for class Bernoulli mixture}
\]

\[
\binom{k+\kappa-1}{\kappa-1}\ge r
\qquad
\text{Continuous observation window conditions for HMM}
\]

