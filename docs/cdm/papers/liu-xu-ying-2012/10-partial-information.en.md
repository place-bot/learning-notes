# Partially known Q and new question calibration

## Scene

The attribute requirements of the existing question \(J-1\) are credible. You only need to learn the q-vector of the new question \(J\). The search space ranges from the complete

\[
2^{JK}
\]

abbreviated to

\[
2^K.
\]

The estimate is

\[
\widehat Q
=
\arg\inf_{Q'\in U_J(Q)}
S(Q').
\]

Only the last line can be changed.

## Anchor question design for paper simulation

Order

\[
J=2K+1,
\qquad
Q=
\begin{pmatrix}
I_K\\
I_K\\
V_J
\end{pmatrix}.
\]

The first row \(2K\) are two sets of unit arrays:

- Each attribute has two questions that only measure it;
- These known questions constitute the anchor;
- \(V_J\) is a new question q-vector to be learned.

## Why two sets of unit formations are helpful

The unit array question anchors each attribute separately. Two repetitions provide more response information for each attribute and also reduce the dominance of noise on the structure of a certain anchor question.

## One calibration process

1. Fixed the previous \(J-1\) line;
2. Enumerate all q-vectors of the new question;
3. Re-estimate \(c,g,p\) for each candidate;
4. Construct T and calculate \(S\);
5. Take the one with the smallest distance;
6. Incorporate content expert checks.

## Multiple new questions

If \(M\) new questions are calibrated each time with trusted old questions as anchors, the number of candidate evaluations will be approximately

\[
O(M2^K).
\]

When all new questions enter the model at the same time, their errors may affect each other; adding questions one by one and updating parameters in each round is a more controllable method of operation.

## An original symbol error

The Discussion section describes this scene at one point where it is printed

\[
\arg\sup S(Q'),
\]

The text then says "the S-function is minimized", while the previous formal definition uses \(\arg\inf\). The entire method should be read as minimized.

## A priori information that can be added

The paper also recommends:

- Fixed known columns corresponding to "hard attributes";
- Search only the "Soft Attributes" column;
- Add log-linear and other parameter structures to \(\boldsymbol p\);
- Fixed or restricted part \(c_j,g_j\);
- Use data results for verification and calibration, and do not directly replace content judgment.
