# symbol table

## People, items and attributes

|symbol|Dimension or range|meaning|
| --- | --- | --- |
| \(I\) |positive integer|Number of students|
| \(J\) |positive integer|number of items|
| \(K\) |positive integer|Number of attributes|
| \(i\) | \(1,\ldots,I\) |student index|
| \(j\) | \(1,\ldots,J\) |item index|
| \(k\) | \(1,\ldots,K\) |Property index|
| \(X_{ij}\) | \(\{0,1\}\) |Student \(i\)’s observation response to question \(j\)|
| \(\boldsymbol X_i\) | \(\{0,1\}^J\) |Complete response vector for student \(i\)|
| \(\alpha_{ik}\) | \(\{0,1\}\) |Does student \(i\) master the attributes \(k\)?|
| \(\boldsymbol\alpha_i\) | \(\{0,1\}^K\) |student attribute profile|

## Q matrix and ideal response

|symbol|Dimension or range|meaning|
| --- | --- | --- |
| \(Q\) | \(J\times K\) |item—attribute requirement matrix|
| \(q_{jk}\) | \(\{0,1\}\) |Question \(j\) Is the attribute \(k\) required?|
| \(\boldsymbol q_j\) | \(\{0,1\}^K\) |Transpose of row \(j\) of Q|
| \(Z_{ij}\) | \(\{0,1\}\) |The original text’s notation of ideal response|
| \(\eta_{ij}\) | \(\{0,1\}\) |Commonly used ideal response symbols in this topic and subsequent CDM|
| \(\eta_{ij}=\prod_k\alpha_{ik}^{q_{jk}}\) |formula|1 when all required attributes are mastery|

## item parameters

|symbol|range|meaning|
| --- | --- | --- |
| \(g_j\) | \([0,1]\) |Probability of correct answer when \(\eta=0\)|
| \(s_j\) | \([0,1]\) |Probability of wrong answer when \(\eta=1\)|
| \(1-s_j\) | \([0,1]\) |Probability of correct answer when \(\eta=1\)|
| \(P_j(\boldsymbol\alpha_l)\) | \([0,1]\) |Probability of correct answer for pattern \(l\) in question \(j\)|
| \(\boldsymbol\beta\) | \(2J\) |All parameter vectors of \(g_j,s_j\)|
| \(\beta_{j0}\) |scalar|Appendix notation, equal to \(g_j\)|
| \(\beta_{j1}\) |scalar|Appendix notation, equal to \(s_j\)|

## Latent classes and EM

|symbol|meaning|
| --- | --- |
| \(L=2^K\) |Number of all binary attribute profiles|
| \(l\) |attribute profile index|
| \(\boldsymbol\alpha_l\) |The \(l\)th possible attribute profile|
|\(\pi_l\) or \(p(\boldsymbol\alpha_l)\)|Prior proportion of pattern \(l\)|
| \(Z_{il}\) |Whether student \(i\) belongs to the category indicator variable of pattern \(l\)|
| \(w_{il}\) |\(P(\boldsymbol\alpha_l\mid\boldsymbol X_i)\), E-step posterior weight|
| \(I_j^{(z)}\) |Question \(j\) The ideal state \(z\) The expected number of people|
| \(R_j^{(z)}\) |The expected number of people who answered the question \(j\) correctly|
| \(\ell(X)\) |Marginal log-likelihood|
| \(\mathcal I(\widehat{\boldsymbol\beta})\) |Observation information matrix|

## HO-DINA

|symbol|meaning|
| --- | --- |
| \(\theta_i\) |Higher-order general abilities of student \(i\)|
| \(\theta_i\sim N(0,1)\) |Distribution of high-order abilities of papers|
| \(\lambda_{0k}\) |Logistic intercept of attribute \(k\)|
| \(\lambda_1\) |Positive slope shared by all attributes|
| \(p_k(\theta_i)\) |Mastery probability of attribute \(k\) given \(\theta_i\)|

## Code object

|mathematical objects|script object|
| --- | --- |
|Table 1 of \(Q\)| `PAPER_Q_MATRIX` |
|attribute profile collection| `all_attribute_patterns()` |
| \(\eta\) | `ideal_response()` |
|Analog \(X\)| `simulate_responses()` |
| \(w_{il}\) | `e_step()` |
|\(g,s\) Update| `m_step()` |
|EM result| `EMResult` |
|A15 standard error| `appendix_standard_errors()` |
