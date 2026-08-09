# symbol table

|symbol|Dimension or value|meaning|
| --- | --- | --- |
| \(N\) |positive integer|Number of students|
| \(J\) |positive integer|Number of questions|
| \(K\) |positive integer|Number of known properties|
| \(R_i^j\) | \(\{0,1\}\) |Student \(i\)’s reaction to question \(j\)|
| \(\boldsymbol R_i\) | \(J\times1\) |Response vector of student \(i\)|
| \(\boldsymbol\alpha_i\) | \(\{0,1\}^K\) |Attribute profile of student \(i\)|
| \(p_{\boldsymbol\alpha}\) | \([0,1]\) |Overall proportion of attribute profile|
| \(\boldsymbol p\) | \(2^K\times1\) |All attribute profile ratios|
| \(Q\) | \(J\times K\) |true the Q matrix or the current matrix in the context|
| \(Q'\) | \(J\times K\) |General Candidate Q|
| \(Q_0\) | \(J\times K\) |Initial Expert Q|
| \(\boldsymbol q_j\) | \(1\times K\) |Question \(j\)’s q-vector|
| \(\xi^j(\boldsymbol\alpha,Q)\) | \(\{0,1\}\) |DINA ideal response|
| \(s_j\) | \([0,1]\) |slipping probability|
| \(c_j=1-s_j\) | \([0,1]\) |Ideal mastery group correct answer rate|
| \(g_j\) | \([0,1]\) |Correct answer rate for non-ideal mastery group|
| \(\pi_{j\boldsymbol\alpha}\) | \([0,1]\) |attribute profile \(\boldsymbol\alpha\) Correct answer probability for question \(j\)|
| \(B(j)\) | \(1\times2^K\) |Single question conditional correct answer probability vector|
| \(B(j_1,\ldots,j_\ell)\) | \(1\times2^K\) |Question group jointly answers correctly B-vector|
| \(\mathcal C\) |question group collection|into the set of row indices of T|
| \(L\) |positive integer|Number of rows of T|
| \(T_{\boldsymbol c,\boldsymbol g}(Q)\) | \(L\times2^K\) |Model moment design matrix|
| \(\beta_A\) | \([0,1]\) |Sample joint correct answer rate for question group \(A\)|
| \(\boldsymbol\beta\) | \(L\times1\) |Selected sample moment vector|
| \(S_{c,g,p}(Q)\) |nonnegative real numbers|Euclidean distance when parameters are given|
| \(S(Q)\) |nonnegative real numbers|Distance after sectioning nuisance parameters|
| \(\widehat S(Q)\) |nonnegative real numbers|Distance after inserting MLE|
| \(U_j(Q)\) |matrix collection|Only neighborhoods with changes in row \(j\) are allowed|
| \(Q^{(m)}\) | \(J\times K\) |\(m\) round search result|
| \(j_*\) | \(1,\ldots,J\) |The final updated questions for this round|
| \(I_K\) | \(K\times K\) |unit array|
| \(V_J\) | \(1\times K\) |New questions to be calibrated in some known experiments|
| \(\rho\) | \([0,1]\) |probit latent variables are jointly correlated|
| \(\Phi^{-1}\) |function|standard normal quantile function|
| \(\sim\) |Equivalence relationship|Q only differs by attribute column permutation|

## Three easily confused objects

|object|Data or model|Whether to rely on candidate Q|
| --- | --- | --- |
| \(\boldsymbol\beta\) |data|No|
| \(T_{\boldsymbol c,\boldsymbol g}(Q)\) |model|Yes|
| \(\boldsymbol p\) |underlying population parameters|Reestimate under candidate Q|

## Three Q estimation tokens

|mark|nuisance parameters processing|
| --- | --- |
|\(\widehat Q\) (after formula 14)|\(c,g,p\) known|
|\(\widehat Q\) (Formula 16)|Union sections directly in distance|
|\(\widetilde Q\) (Formula 18)|Find MLE first, then substitute \(\widehat S\)|

The original text reuses \(\widehat Q\) to represent estimators in different contexts. You need to check its corresponding objective function when reading.
