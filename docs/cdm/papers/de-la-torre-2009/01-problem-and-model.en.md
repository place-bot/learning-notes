#Problems, objects and model assumptions

## The problem that the paper hopes to solve

Traditional unidimensional IRT often gives each student a continuous ability score:

\[
\theta_i\in\mathbb R.
\]

This kind of score is suitable for ranking and measurement scales. Teaching intervention also requires more detailed information, such as which skills students have mastered and which skills need remediation.

DINA uses a binary attribute vector:

\[
\boldsymbol\alpha_i
=
(\alpha_{i1},\ldots,\alpha_{iK})^\mathsf T,
\qquad
\alpha_{ik}\in\{0,1\}.
\]

- \(\alpha_{ik}=1\): Student \(i\) masters attribute \(k\);
- \(\alpha_{ik}=0\): Not mastered yet.

The paper refers to skill, knowledge representation and cognitive process as attributes.

## Observation data

Set

\[
X_{ij}\in\{0,1\},
\]

Among them:

- \(i=1,\ldots,I\) means student;
- \(j=1,\ldots,J\) represents item;
- \(X_{ij}=1\) means correct answer;
- \(X_{ij}=0\) indicates an incorrect answer.

The data matrix is

\[
X\in\{0,1\}^{I\times J}.
\]

## Q matrix

\[
Q=(q_{jk})\in\{0,1\}^{J\times K}.
\]

\(q_{jk}=1\) represents item \(j\) and requires attribute \(k\). Line \(j\)

\[
\boldsymbol q_j
=(q_{j1},\ldots,q_{jK})^\mathsf T
\]

It is the cognitive requirement of this question.

The original article takes fractional subtraction as an example. The five attributes are:

1. Subtraction of basic scores;
2. Reduction and simplification;
3. Separate the integer and fractional parts;
4. Borrow from the integer part;
5. Convert integers to fractions.

item \(7\frac35-4\frac45\) requires attributes 1, 3, 4, so

\[
\boldsymbol q_j=(1,0,1,1,0)^\mathsf T.
\]

## attribute profile is also latent class

Binary \(K\) attributes are shared

\[
L=2^K
\]

possible modes:

\[
(0,\ldots,0),\ldots,(1,\ldots,1).
\]

So DINA can be written as a restricted latent class model:

- Each attribute profile is a category;
- Class conditional correct answer probability is constrained by Q matrix, guess and slip;
- If different latent classes have the same ideal state on a certain question, they share the same correct answer probability.

"Restricted" is reflected in the fact that \(2^K\) categories do not have independent \(J\) correct answer probabilities.

## The main assumptions of this article’s model

|hypothesis|function|
| --- | --- |
|Binary item response| \(X_{ij}\in\{0,1\}\) |
|Binary attribute mastery| \(\alpha_{ik}\in\{0,1\}\) |
|Q matrix is known|What attributes does item require to be given in advance?|
|The join rule is conjunction|All attributes required by a question must be mastered|
|Local independence given attribute profile|A student's item response condition likelihood can be multiplied|
|Two noise parameters for each question|\(g_j\) and \(s_j\)|
|Attribute profile distribution needs to be specified separately|Saturated multinomial distribution or HO-DINA higher-order distribution|

## Strong constraints of DINA

For a question that requires multiple attributes, all "at least one required attribute is missing" patterns are pressed to the same ideal state:

\[
\eta_{ij}=0.
\]

Regardless of whether the student is missing one attribute or three attributes, the probability of correct answer is \(g_j\).

When all required attributes are mastered:

\[
\eta_{ij}=1,
\]

The probability of correct answer is \(1-s_j\).

This leads to concise explanations and low number of parameters, and also ignores some mastery levels and different main effects between attributes. G-DINA of de la Torre (2011) continues the generalization exactly along this restriction.
