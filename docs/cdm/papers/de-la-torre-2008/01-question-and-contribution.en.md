# Problem, Contribution and Evidence Boundaries

## Why does the Q matrix need to be verified separately?

Suppose the test has \(J\) questions and \(K\) binary attributes. Row \(j\) of Q matrix

\[
\boldsymbol q_j=(q_{j1},\ldots,q_{jK})
\]

Explain which attributes are required to correctly answer question \(j\). Experts will use task analysis, cognitive interviews, content standards and item texts when constructing Qs, but this information may still produce:

- Missing mark: The item actually requires a certain attribute, and the Q line is written as 0;
- Multi-standard: item does not require a certain attribute, the Q line is written as 1;
- Replacement: omit one attribute and add another attribute at the same time;
- Attribute system bias: There are already \(K\) attributes which are not enough to explain the answer.

The first three categories can adjust Q rows within a fixed set of attributes; the last category requires redefining the attribute space. The method in this article mainly deals with the first three categories.

## How errors get into DINA parameters

DINA divides students into two groups:

- \(\eta_{ij}=1\): Student \(i\) masters all the attributes required by question \(j\);
- \(\eta_{ij}=0\): At least one required property is missing.

If row Q misses the attributes that are really needed, some students with insufficient abilities will be put into the \(\eta=1\) group, and the error rate in the group will increase, and it is estimated that slip will tend to increase.

If irrelevant attributes are added to row Q, some students who could have answered correctly will be put into the \(\eta=0\) group. The correct answer rate in the group will increase, and it is estimated that the guess will tend to increase.

Therefore, Q line errors can be disguised as poor item parameters. The validator regroups and checks which q-vector produces a clearer separation in answer rates.

## The statistical interface proposed by the author

For any candidate q-vector of the same question, calculate

\[
\widehat\delta_{j}(\boldsymbol q)
=
P(X_j=1\mid\eta_j(\boldsymbol q)=1)
-
P(X_j=1\mid\eta_j(\boldsymbol q)=0).
\]

Under DINA parameterization,

\[
\widehat\delta_j(\boldsymbol q)
=1-\widehat s_j(\boldsymbol q)-\widehat g_j(\boldsymbol q).
\]

The verification can be expressed as: look for the larger \(\widehat\delta\) in the candidate q-vector and check whether the improvement reaches the threshold.

## Three-tier contribution

|level|Contribute|Actual effect|
| --- | --- | --- |
|statistical criteria|\(\delta\) for candidate q-vector|Convert Q row comparison into two groups of correct answer rate separation|
|search algorithm| sequential \(\delta\)-method |Attributes are added one by one to reduce the number of candidates|
|Calculation algorithm| EM posterior expected counts |Quickly recalculate candidates after one fitting \(g,s,\delta\)|

These three levels need to be read separately. A larger \(\delta\) indicates that candidate groupings are better able to differentiate answering performance; it does not by itself guarantee that the attribute labels have correct cognitive meaning.

## Evidence provided by the original text

|evidence|Data size|Main purpose|
| --- | ---: | --- |
|hypothetical question|5 attributes, 32 equal probability patterns|Accurately demonstrate how to compress missing labels and multiple labels \(\delta\)|
|Simulation| \(N=5000,J=30,K=5\) |Testing resilience under author-specified 11 types of Q-errors|
|Fraction subtraction|2144 people, 15 questions, 5 attributes|Check if existing Qs will be retained and demonstrate the importance of content knowledge|
| NAEP |3823 people, 90 questions, 9 attributes|Demonstrate applications under missing, multi-weighted, large item bank and obvious mismatch conditions|

## Evidence Boundary

- The simulation only fixes \(N=5000,J=30,K=5,g=s=.20\), and does not systematically change the sample size, test length, low-differentiation item or attribute-related structure.
- Each attribute profile in the simulation has equal probability, which is an ideal posterior recovery condition.
- Fractional subtraction analysis supports the relative stability of the original Q under this data and DINA and cannot prove that the attribute system is correct for all student groups.
- NAEP's original model fit is very poor; recommending Q only brings small parameter improvements.
- The original article does not use Q-adjusted student classification accuracy, teaching validity or external validation standards as results.
- The method assumes that the attribute number \(K\) and the attribute meaning are already given.

These boundaries determine that this article belongs to the Q matrix **empirical verification**: it presents evidence of modification within the framework of existing properties.

