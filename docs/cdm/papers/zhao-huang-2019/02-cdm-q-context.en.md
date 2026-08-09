# Interface between CDM, Q matrix and text classification

## 1. General definition of Q matrix

There are \(J\) questions and \(K\) attributes. The binary \(Q\) matrix is

\[
Q=(q_{jk})\in\{0,1\}^{J\times K},
\]

Among them

\[
q_{jk}=1
\]

Indicates that question \(j\) requires attribute \(k\).

In general, a line can contain multiple 1's:

\[
\boldsymbol q_j=(1,0,1,0)
\]

Expression question \(j\) requires both attribute 1 and attribute 3.

## 2. The role of Q in CDM

Taking DINA as an example, the mastery vector of student \(i\) is

\[
\boldsymbol\alpha_i=(\alpha_{i1},\ldots,\alpha_{iK}).
\]

The ideal answer index for question \(j\) is

\[
\eta_{ij}
=
\prod_{k=1}^{K}
\alpha_{ik}^{q_{jk}}.
\]

When \(\boldsymbol q_j\) changes, the meaning of \(\eta_{ij}\) also changes, which affects the classification of mistakes, guessing parameters and student attributes.

## 3. Special Q used in the paper

The paper asked experts to specify "the most prominent cognitive attribute" for each question. So each row satisfies

\[
\sum_{k=1}^{9}q_{jk}=1.
\]

Such \(Q\) is a one-hot matrix. Each row is exactly equivalent to a multi-category label:

\[
\boldsymbol q_j=\boldsymbol e_{y_j},
\]

Among them \(y_j\in\{1,\ldots,9\}\).

## 4. Why can one-hot situations be converted into text classification?

The question stem is \(d_j\) and the classifier is \(f_\theta\). Multi-category prediction can be written as

\[
\widehat y_j=f_\theta(d_j),
\qquad
\widehat{\boldsymbol q}_j=\boldsymbol e_{\widehat y_j}.
\]

If multiple 1s are allowed in one line, \(K\) binary judgments need to be output:

\[
\widehat q_{jk}
=
\mathbb I\left\{
p_\theta(q_{jk}=1\mid d_j)>\tau_k
\right\}.
\]

This is already a multi-label classification, and the loss function, threshold, evaluation and data requirements will all change.

## 5. Differences from data-driven Q estimation

Two types of methods use different evidence:

|route|input|learning signal|Typical output|
| --- | --- | --- | --- |
|Text semantic annotation|Question stems and expert tags|Row Q marked|First draft of new question Q line|
|CDM Statistical Calibration|Student item reaction|response likelihood or fit index|Modifications to existing Q|

The text model can handle new questions that have no student response. The response data method can discover the bias between the semantics of the question stem and the actual problem-solving process. A more reasonable combination in practice is:

\[
\text{text prior}
\longrightarrow
\text{Expert review}
\longrightarrow
\text{Reaction data calibration}.
\]

## 6. The relationship between this article and the previous six Q matrix papers

Previous topic studies:

- How to verify or correct Q using reaction data;
- Under what conditions Q and model parameters can be identified;
- How the Bayesian or frequentist algorithm estimates Q.

Zhao and Huang moved the problem to an earlier stage when the item enters the item bank: first using the semantics of the question stem to generate candidate tags. It complements the cold start phase of the statistical calibration route.
