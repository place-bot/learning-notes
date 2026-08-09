# Complete hand calculation of three questions and two attributes

## attribute profile order

Paper press

\[
(0,0),(1,0),(0,1),(1,1)
\]

Arrange \(\boldsymbol p=(p_{00},p_{10},p_{01},p_{11})^\top\).

## True Q

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix}.
\tag{8}
\]

Question 1 only requires attribute 1, question 2 only requires attribute 2, and question 3 requires both attributes. Shilling \(c_j=1,g_j=0\), response without noise.

## Three single questions B-vector

\[
B(1)=(0,1,0,1),
\]

\[
B(2)=(0,0,1,1),
\]

\[
B(3)=(0,0,0,1).
\]

So

\[
T(Q)=
\begin{pmatrix}
0&1&0&1\\
0&0&1&1\\
0&0&0&1
\end{pmatrix}.
\tag{9}
\]

Multiply by \(\boldsymbol p\):

\[
T(Q)\boldsymbol p
=
\begin{pmatrix}
p_{10}+p_{11}\\
p_{01}+p_{11}\\
p_{11}
\end{pmatrix}
=
\begin{pmatrix}
N_1/N\\
N_2/N\\
N_3/N
\end{pmatrix}
=
\boldsymbol\beta.
\]

\(N_j\) is the number of correct answers to question \(j\).

## An error candidate

\[
Q'=
\begin{pmatrix}
1&0\\
0&1\\
1&0
\end{pmatrix}
\]

Change question 3 to only require attribute 1. Correspond

\[
T(Q')=
\begin{pmatrix}
0&1&0&1\\
0&0&1&1\\
0&1&0&1
\end{pmatrix}.
\tag{10}
\]

The first row is the same as the third row, and the candidate model forces the same overall correct answer rate for questions 1 and 3. If \(N_1/N\) and \(N_3/N\) in the data are obviously different, this candidate cannot match \(\boldsymbol\beta\) well.

## Add question pair constraints

Order

\[
N_{1\wedge2}
=
\sum_{i=1}^N
\mathbf 1(R_i^1=1,R_i^2=1).
\tag{12}
\]

When there is true Q and no noise, answering questions 1 and 2 correctly at the same time is equivalent to mastering two attributes, so

\[
B(1,2)=B(1)\odot B(2)=(0,0,0,1)=B(3).
\]

The expanded matrix is

\[
T(Q)=
\begin{pmatrix}
0&1&0&1\\
0&0&1&1\\
0&0&0&1\\
0&0&0&1
\end{pmatrix},
\qquad
\boldsymbol\beta=
\begin{pmatrix}
N_1/N\\
N_2/N\\
N_3/N\\
N_{1\wedge2}/N
\end{pmatrix}.
\tag{13}
\]

Noise-free logic requires \(N_3=N_{1\wedge2}\). Actual data generally deviates, and \(s_j,g_j\) is used to absorb response noise.

## What this example really illustrates

Q enters the observable distribution through a set of cross-topic joint constraints. Adding more question group rows is equivalent to proposing more moment conditions from the data that must be satisfied at the same time; the error Q is more difficult to fully compensate with \(\boldsymbol p,\boldsymbol c,\boldsymbol g\).
