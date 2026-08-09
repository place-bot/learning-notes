# symbol table

|symbol|meaning|
| --- | --- |
| \(J\) |number of items|
| \(K\) |Number of cognitive attributes|
| \(Q\) |\(J\times K\) binary item--attribute matrix|
| \(q_{jk}\) |Question \(j\) Is the attribute \(k\) required?|
| \(\boldsymbol q_j\) |Line Q of question \(j\)|
| \(d_j\) |Original text of question \(j\)|
| \(y_j\) |Expert attribute category for question \(j\)|
| \(O\) | Operations of integers |
| \(M\) | Mathematical thinking |
| \(\boldsymbol x_j\) |TF--IDF eigenvector of question \(j\)|
| \(p\) |Number of candidate text features|
| \(k\) |Number of features retained after information gain filtering|
| \(X_r\) |The \(r\) text feature variable|
| \(Y\) |Cognitive attribute random variable|
| \(H(Y)\) |Category entropy|
| \(H(Y\mid X)\) |Conditional entropy given features|
| \(IG(X;Y)\) |Information gain/mutual information|
| \(df_r\) |Number of training questions containing feature \(r\)|
| \(\operatorname{tf}_{jr}\) |Feature \(r\) word frequency in question \(j\)|
| \(\operatorname{idf}_r\) |Inverse document frequency of feature \(r\)|
| \(\boldsymbol w,b\) |SVM hyperplane parameters|
| \(\xi_j\) |SVM slack variables|
| \(C\) |SVM misclassification penalty strength|
| \(\alpha,\boldsymbol\beta\) |Logistic Regression intercept and coefficient|
| \(\lambda\) |L2 regularization strength|
| \(p(c)\) |NB category prior|
| \(\mu_{cr},\sigma_{cr}^2\) |Mean and variance of category \(c\) and feature \(r\) in Gaussian NB|
| \(\mathcal T\) |training set|
| \(\mathcal V\) |validation set|
| \(\mathcal E\) |test set|
| \(TP_c\) |The true number of examples of category \(c\)|
| \(FP_c\) |Number of false positives for category \(c\)|
| \(FN_c\) |Number of false negative examples for category \(c\)|
| \(t_c\) |Support of real class \(c\)|
| \(p_c\) |The number of questions predicted to be in the category \(c\) in the original article|
| \(F1_c\) |F1 for category \(c\)|
| \(\pi_t(\boldsymbol\alpha)\) |CAT student attribute posterior after step \(t\)|
| \(\Omega_t\) |CAT step \(t\) optional question set|
| \(U_t(j)\) |Measurement utility of multiple choice question \(j\) in step \(t\)|
| \(p_\psi(\boldsymbol q_j\mid d_j)\) |Q row distribution of text model question \(j\)|

## Data constants

\[
J_{\mathrm{raw}}=1069,
\qquad
K_{\mathrm{raw}}=9.
\]

\[
J_{\mathrm{experiment}}=805,
\qquad
K_{\mathrm{experiment}}=2.
\]

\[
n_O=666,
\qquad
n_M=139.
\]

## Experimental Grid

\[
\mathcal K
=
\{5,10,\ldots,300\},
\qquad
|\mathcal K|=60.
\]

\[
\mathcal A
=
\{\mathrm{LR},\mathrm{SVM},\mathrm{NB}\}.
\]

\[
\mathcal G
=
\{(1,1),(1,2),(1,3)\}.
\]
