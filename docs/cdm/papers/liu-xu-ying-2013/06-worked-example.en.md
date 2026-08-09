# Complete hand calculation of three questions and two attributes

## Q matrix

The original text uses two attributes: "addition" and "multiplication":

\[
Q=
\begin{array}{c|cc}
&\text{addition}&\text{Multiplication}\\\hline
2+3&1&0\\
5\times2&0&1\\
(2+3)\times2&1&1
\end{array}.
\tag{2.8}
\]

Remember three questions as \(I_1,I_2,I_3\), and the non-zero attribute profile column is

\[
10,\ 01,\ 11
\]

Arrange.

## Three single question lines

Question 1 only requires addition:

\[
B_Q(I_1)=(1,0,1).
\]

Question 2 only requires multiplication:

\[
B_Q(I_2)=(0,1,1).
\]

Question 3 requires both:

\[
B_Q(I_3)=(0,0,1).
\]

So when using only single questions

\[
T(Q)=
\begin{pmatrix}
1&0&1\\
0&1&1\\
0&0&1
\end{pmatrix}.
\tag{2.11}
\]

## Attribute ratio

The sample attribute proportions can be arranged as

\[
\widehat{\boldsymbol p}
=
\begin{pmatrix}
\widehat p_{10}\\
\widehat p_{01}\\
\widehat p_{11}
\end{pmatrix}.
\]

The all-zero mode ratio is

\[
\widehat p_{00}
=1-\widehat p_{10}-\widehat p_{01}-\widehat p_{11}.
\]

The observation moment vector is

\[
\boldsymbol\alpha
=
\begin{pmatrix}
N_{I_1}/N\\
N_{I_2}/N\\
N_{I_3}/N
\end{pmatrix}.
\]

After the moment equation is expanded, it is

\[
\begin{aligned}
\widehat p_{10}+\widehat p_{11}
&=\frac{N_{I_1}}N,\\
\widehat p_{01}+\widehat p_{11}
&=\frac{N_{I_2}}N,\\
\widehat p_{11}
&=\frac{N_{I_3}}N.
\end{aligned}
\tag{2.9}
\]

## Solve the attribute ratio

From the third formula:

\[
\widehat p_{11}
=
\frac{N_{I_3}}N.
\]

Substituting back the first two equations:

\[
\widehat p_{10}
=
\frac{N_{I_1}-N_{I_3}}N,
\qquad
\widehat p_{01}
=
\frac{N_{I_2}-N_{I_3}}N.
\]

The matrix \(T(Q)\) is an upper triangle and the diagonals are all 1, so it has full rank and a unique solution.

## Add question pairs

The attribute profile that can complete questions 1 and 2 is only \(11\), so

\[
B_Q(I_1\wedge I_2)
=(0,0,1).
\]

The extended matrix becomes

\[
T(Q)=
\begin{pmatrix}
1&0&1\\
0&1&1\\
0&0&1\\
0&0&1
\end{pmatrix},
\qquad
\boldsymbol\alpha=
\begin{pmatrix}
N_{I_1}/N\\
N_{I_2}/N\\
N_{I_3}/N\\
N_{I_1\wedge I_2}/N
\end{pmatrix}.
\tag{2.12}
\]

Therefore, the noiseless model also requires

\[
\frac{N_{I_3}}N
=
\frac{N_{I_1\wedge I_2}}N
=
\widehat p_{11}.
\]

## A numerical sample

hypothesis

\[
\widehat p_{00}=0.10,\quad
\widehat p_{10}=0.25,\quad
\widehat p_{01}=0.35,\quad
\widehat p_{11}=0.30.
\]

rule

\[
T(Q)\widehat{\boldsymbol p}
=
\begin{pmatrix}
0.55\\
0.65\\
0.30\\
0.30
\end{pmatrix}.
\]

This means:

- The correct rate for question 1 is \(0.25+0.30=0.55\);
- The correct rate for question 2 is \(0.35+0.30=0.65\);
- The correct rate for question 3 is \(0.30\);
- The correct answer rate for questions 1 and 2 is also \(0.30\).

## How noise changes the equation

After adding errors and guesses, actually completing question 3 and answering questions 1 and 2 correctly at the same time are two random events, and their probabilities are generally different. \(T_{c,g}(Q)\) in Section 3 will change each B-vector from a 0/1 ability indication to a specific probability of correct answer, so that moment matching continues to hold.

[Next page: Column permutation equivalence, completeness and saturation](07-equivalence-completeness-saturation.md)
