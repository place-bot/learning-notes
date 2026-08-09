# DINA, Q matrix and ideal response

## Basic objects

|symbol|meaning|
| --- | --- |
| \(i=1,\ldots,N\) |student|
| \(j=1,\ldots,J\) |item|
| \(k=1,\ldots,K\) |Properties|
| \(X_{ij}\in\{0,1\}\) |Student \(i\)’s answer to question \(j\)|
| \(\boldsymbol\alpha_i\in\{0,1\}^K\) |studentattribute mastery profile|
| \(\boldsymbol q_j\in\{0,1\}^K\) |Attribute requirements for question \(j\)|

The paper numbers the attribute profiles \(2^K\) as

\[
\boldsymbol\alpha_l,\qquad l=0,1,\ldots,2^K-1,
\]

Among them \(\boldsymbol\alpha_0=\boldsymbol 0\).

## DINA’s AND gate

When the candidate q-vector is \(\boldsymbol q\), the ideal response of the student mode \(\boldsymbol\alpha_l\) is

\[
\eta_l(\boldsymbol q)
=
\prod_{k=1}^{K}\alpha_{lk}^{q_k}.
\]

Explanation:

- When \(q_k=0\), the \(k\)th attribute does not participate in the judgment;
- When \(q_k=1\), only \(\alpha_{lk}=1\) will not cause the product to become 0;
- When all required attributes are mastered \(\eta=1\);
- \(\eta=0\) when any of the required attributes are missing.

The original form of this article is represented by \(\eta_{ll'}\): the student mode is \(\boldsymbol\alpha_l\), and the candidate q-vector takes the \(l'\)th non-zero attribute profile.

## Two item parameters

\[
g_j=P(X_{ij}=1\mid\eta_{ij}=0),
\]

\[
s_j=P(X_{ij}=0\mid\eta_{ij}=1).
\]

Therefore

\[
P(X_{ij}=1\mid\boldsymbol\alpha_i)
=
g_j^{1-\eta_{ij}}(1-s_j)^{\eta_{ij}}.
\]

It can also be written as

\[
P(X_{ij}=1\mid\boldsymbol\alpha_i)
=g_j+(1-s_j-g_j)\eta_{ij}.
\]

The latter form directly shows the difference in correct answer rates between the two groups:

\[
(1-s_j)-g_j=1-s_j-g_j.
\]

## What will happen if you change the Q line for the same question?

The item response \(X_{ij}\) has not changed. What has changed is:

1. Which attribute profiles enter \(\eta=1\);
2. Which modes to enter \(\eta=0\);
3. Posterior number of people in the two groups;
4. The number of correct answers in the post-test of the two groups;
5. \(g,s,\delta\) calculated accordingly.

So \(\delta\) is the property of "item and current q-vector combination". The paper clearly states that it changes when row Q changes.

## Three wrong parameter directions

Assume that the real item requires attributes 1 and 2.

|candidate error|Wrong direction|Typical parameter changes|
| --- | --- | --- |
|Missing attribute 1|Students missing attribute 1 are mixed in \(\eta^*=1\)|\(s^*\) increase|
|Add more attributes 3|Students who have mastered 1 and 2 but not 3 are mixed into \(\eta^*=0\)|\(g^*\) increase|
|Also omit 1 and add 3|Misclassification occurs on both sides|\(g^*,s^*\) may increase|

The asterisk on the symbol indicates a new grouping based on the candidate q-vector.

## Local independence and posteriori

Given an attribute profile, DINA assumes that the responses to each question are locally independent:

\[
P(\boldsymbol X_i\mid\boldsymbol\alpha_l)
=
\prod_{j=1}^{J}
P(X_{ij}\mid\boldsymbol\alpha_l).
\]

Combined with the attribute profile prior \(\pi_l\), the E-step of EM is obtained

\[
\widehat p(\boldsymbol\alpha_l\mid\boldsymbol X_i).
\]

This set of posterior weights is the calculation basis for quickly verifying all candidate q-vectors later.
