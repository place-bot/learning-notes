# Counterexample that C1 alone is not enough

## Proposition 2

Under the model setting of the paper, there is a Q matrix that satisfies C1, so that

\[
(\Theta,\boldsymbol p)
\]

Unrecognizable.

This means that the two \(I_K\) blocks alone cannot replace C2.

## Structure constructed from the original text

The paper focuses on the first property, allowing Q to be written as

\[
Q=
\begin{pmatrix}
1&\boldsymbol0^\top\\
1&\boldsymbol0^\top\\
\boldsymbol0&I_{K-1}\\
\boldsymbol0&I_{K-1}\\
\boldsymbol0&Q^*
\end{pmatrix}.
\]

The first two chunks taken together satisfy C1, but there are no items in \(Q^*\) that provide the additional distinction of the first attribute. Under DINA, in addition to the first two questions, attribute profile
\(\boldsymbol\alpha\) and
The response pattern of \(\boldsymbol\alpha+\boldsymbol e_1\) is the same.

Therefore, all the information about attribute 1 is compressed in the joint distribution of two two-part questions. A two-component Bernoulli product mixture has only a finite number of observable degrees of freedom, but allows continuous change:

- Low and high probability of success for two questions;
- Proportional distribution of each pair of latent classes.

Thesis formula (4.16) explicitly constructs a family of different parameters, so that four
\((R_1,R_2)\) pattern probabilities all remain unchanged.

## A K = 1 numerical instance

take

\[
Q=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

This contains exactly two \(I_1\), satisfying C1; without \(Q'\), C2 fails.

The first set of parameters:

\[
p_0=0.4,\quad p_1=0.6,
\]

\[
(\theta_{1,0},\theta_{1,1})=(0.2,0.8),
\qquad
(\theta_{2,0},\theta_{2,1})=(0.3,0.9).
\]

The moment of the joint distribution of the three decision questions is

\[
P(R_1=1)=0.56,
\]

\[
P(R_2=1)=0.66,
\]

\[
P(R_1=1,R_2=1)=0.456.
\]

The second set of different parameters:

\[
\bar p_0=0.5,\quad\bar p_1=0.5,
\]

\[
(\bar\theta_{1,0},\bar\theta_{1,1})
=(0.26,0.86),
\]

\[
(\bar\theta_{2,0},\bar\theta_{2,1})
=(0.372,0.948).
\]

it produces

\[
P(R_1=1)=0.5(0.26)+0.5(0.86)=0.56,
\]

\[
P(R_2=1)=0.5(0.372)+0.5(0.948)=0.66,
\]

\[
\begin{aligned}
P(R_1=1,R_2=1)
&=0.5(0.26)(0.372)
+0.5(0.86)(0.948)\\
&=0.456.
\end{aligned}
\]

The remaining three pattern probabilities in question 2 are uniquely determined by these three moments, so the complete observation distributions of the two sets of parameters are exactly the same. Both groups satisfy that the high probability of each question is greater than the low probability.

## C2 How to destroy this equivalent curve

If a third question is added that only measures attribute 1:

\[
Q=
\begin{pmatrix}
1\\1\\1
\end{pmatrix},
\]

The third question is located at \(Q'\), and equation (2.3) guarantees

\[
\theta_{3,1}>\theta_{3,0}.
\]

Now the joint moments of the three questions provide additional constraints, C2 is established, and the main theorem ensures that the entire set of parameters is unique.

## What does the counterexample tell us?

- "At least two questions for each attribute" cannot uniformly guarantee general RLCM recognition;
- The remaining questions of C2 bear the third observation direction;
- Non-identification can be expressed as a continuous parameter family and is not limited to simple label exchange;
- Increasing \(N\) can only estimate the same observation distribution more accurately and cannot distinguish equivalent parameter points;
- The software returning a single solution may result from initialization, bounds, or optimizer selection and cannot be used to determine that the model has been identified.
