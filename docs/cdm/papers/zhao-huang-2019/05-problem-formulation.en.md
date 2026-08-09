# Mathematical representation of supervised learning tasks

## 1. Input and tags

For question \(j\), note:

- Original question stem: \(d_j\);
- Expert category: \(y_j\in\{O,M\}\);
- Feature vector: \(\boldsymbol x_j\in\mathbb R^p\).

The training sample is

\[
\mathcal D
=
\{(\boldsymbol x_j,y_j)\}_{j=1}^{n}.
\]

## 2. Text to line Q

The classifier gives

\[
\widehat y_j=f_{\widehat\theta}(\boldsymbol x_j).
\]

The mapping of categories to Q rows is

\[
\widehat{\boldsymbol q}_j
=
\begin{cases}
(1,0),&\widehat y_j=O,\\
(0,1),&\widehat y_j=M.
\end{cases}
\]

## 3. Training objectives

Three types of models use different losses:

### Logistic Regression

\[
\widehat\theta_{\mathrm{LR}}
=
\arg\min_\theta
\left\{
-\sum_{j\in\mathcal T}
\log p_\theta(y_j\mid\boldsymbol x_j)
+\lambda\|\theta\|_2^2
\right\}.
\]

### SVM

\[
(\widehat{\boldsymbol w},\widehat b)
=
\arg\min_{\boldsymbol w,b}
\left\{
\frac12\|\boldsymbol w\|_2^2
+C\sum_{j\in\mathcal T}\ell_{\mathrm{hinge},j}
\right\}.
\]

The paper prints the squared relaxation variable form, see the SVM chapter for details.

### Gaussian NB

\[
\widehat y_j
=
\arg\max_{c\in\{O,M\}}
\widehat p(c)
\prod_{r=1}^{p}
\widehat p(x_{jr}\mid c).
\]

## 4. The number of features is also a hyperparameter

Information gain first sorts all text features. Yes

\[
k\in\{5,10,\ldots,300\},
\]

Only the first \(k\) features are retained. So each model also contains a hyperparameter selected by the validation set:

\[
\widehat k
=
\arg\max_{k}
\operatorname{Score}_{\mathcal V}
\left(f_{\widehat\theta(k)}\right).
\]

## 5. Final test

After fixing \(\widehat k\), calculate on test set \(\mathcal E\):

\[
\operatorname{Accuracy}_{\mathcal E},
\qquad
\operatorname{WeightedF1}_{\mathcal E}.
\]

If training, validation and testing are strictly separated, the test set should only be used once at the end.

## 6. Core assumptions of the thesis task

This method depends on:

\[
p(y\mid d)
\]

Remain relatively stable between training questions and new questions.

When course terminology, question templates, language styles, or attribute definitions change, the text-to-attribute mapping will undergo a domain shift. The paper's random division of a single item bank cannot measure this change.
