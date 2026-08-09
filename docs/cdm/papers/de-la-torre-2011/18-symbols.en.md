# symbol table

## Data and dimensions

|symbol|meaning|
| --- | --- |
| \(I\) |Number of students/subjects|
| \(J\) |number of items|
| \(K\) |Total number of attributes tested|
| \(L=2^K\) |The complete number of attribute profiles without structural restrictions|
| \(X_{ij}\) |Student \(i\)’s binary response to item \(j\)|
| \(\boldsymbol X_i\) |Response vector of student \(i\)|

## Q matrix and attributes

|symbol|meaning|
| --- | --- |
| \(Q\) |\(J\times K\) item-attribute matrix|
| \(q_{jk}\) |Does item \(j\) require attributes \(k\)?|
| \(K_j^*=\sum_k q_{jk}\) |item \(j\) Number of required attributes|
| \(\boldsymbol\alpha_l\) |The complete attribute profile \(l\)|
| \(\boldsymbol\alpha^*_{lj}\) |item \(j\) Reduced attribute profile for pattern \(l\)|
| \(\boldsymbol a\preceq\boldsymbol b\) |Each component of \(\boldsymbol a\) is not greater than \(\boldsymbol b\)|
| \(\boldsymbol a\prec\boldsymbol b\) |The above partial order holds and at least one component is strictly smaller than|

## Success probability and link

|symbol|meaning|
| --- | --- |
| \(P(\boldsymbol\alpha^*_{lj})\) |The probability of answering item \(j\) correctly in reduction mode|
| \(\boldsymbol P_j\) |item \(j\) All reduction group success probability vectors|
| \(h(P)\) |identity, logit or log link|
| \(\boldsymbol\delta_j\) |identity-link G-DINA effect|
| \(\boldsymbol\lambda_j\) |logit-link effect|
| \(\boldsymbol\nu_j\) |log-link effect|
| \(g_j,s_j\) |DINA’s guessing and slipping parameters|

## design and constraints

|symbol|meaning|
| --- | --- |
| \(A_j\) |item \(j\) All reduced attribute combination matrices|
| \(M_j^{(S)}\) |saturated design matrix|
| \(M_j^{(r)}\) |The design matrix of the reduced model \(r\)|
| \(M_j^{(r-)}\) |Reduced design matrix with the intercept column removed|
| \(R_{jr}\) |Restriction matrix of item \(j\), model \(r\)|
|\(p\) or \(P\)|Reduced model number of free parameters; needs to be identified based on context|

## EM and posterior counting

|symbol|meaning|
| --- | --- |
| \(p(\boldsymbol\alpha_l)\) |Complete attribute profile prior probability|
| \(\tau_{il}\) |The posterior probability that student \(i\) belongs to the complete pattern \(l\)|
| \(\tau_{ij}(\boldsymbol a)\) |The posterior probability that student \(i\) belongs to item \(j\) reduced group \(\boldsymbol a\)|
| \(I_{\boldsymbol a j}\) |The expected number of people in the reduced group \(\boldsymbol a\)|
| \(R_{\boldsymbol a j}\) |The expected number of correct answers for the reduced group \(\boldsymbol a\)|
| \(W_j\) |The weight matrix with \(I_{\boldsymbol a j}\) as the diagonal element|

## Inference

|symbol|meaning|
| --- | --- |
| \(\mathcal I(\widehat{\boldsymbol P}_j)\) |Observation information matrix of item probability|
| \(\operatorname{Var}(\widehat{\boldsymbol P}_j)\) |item probability covariance matrix|
| \(G_j\) |Parametrically transformed Jacobian|
| \(W\) |Wald statistic; different from weight matrix \(W_j\)|
| \(2^{K_j^*}-p\) |Wald test degrees of freedom|

## Code object mapping

|Thesis object| `GDINA` R package |This site Python|
| --- | --- | --- |
|Complete attribute profile| `attributepattern()` | `attribute_patterns()` |
|reduced group mapping| `LC2LG()` / `reduced.LG` | `item_group_maps()` |
| \(M_j\) | `designmatrix()` | `design_matrix()` |
| \(R_{\boldsymbol a j}\) | `Rg` | `expected_correct` |
| \(I_{\boldsymbol a j}\) | `Ng` | `expected_total` |
| \(\boldsymbol P_j\) | `catprob.parm` | `probabilities` |
| Wald | `modelcomp()` | `wald_acdm()` |
