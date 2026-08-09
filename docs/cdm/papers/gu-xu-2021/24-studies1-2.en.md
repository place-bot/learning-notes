# Experiment：DINA Studies I--II

## Study I: Strict identification

### 1. Two structures

In the \(5\times2\) scenario, structures satisfying A/B/C can be classified into two categories through row-column replacement. Paper selection:

\[
Q^{18}=
\begin{pmatrix}
0&1\\
1&1\\
1&1\\
1&0\\
0&1
\end{pmatrix},
\]

It contains a set of \(I_2\), and

\[
Q^{15}=
\begin{pmatrix}
0&1\\
1&1\\
1&0\\
1&0\\
0&1
\end{pmatrix},
\]

It contains two sets of \(I_2\).

### 2. Design

Generated using \(Q^{18}\) and \(Q^{15}\) respectively

\[
N=10^5
\]

Data, fit DINA to the candidate Q one by one and take the maximum likelihood.

### 3. result

In both scenarios, true Q achieves the highest log-likelihood.

\(Q^{15}\), which contains two sets of \(I_2\), has a larger likelihood gap from the wrong candidate. The authors make an empirical observation based on this: more unit submatrices may improve the separation of finite sample structures.

This observation goes beyond Theorem 1's binary conclusion. The theorem only determines whether it can be identified, but does not give the likelihood interval.

## Study II: Only tested twice but with broad recognition

### 1. True Q

\[
Q^5=
\begin{pmatrix}
0&1\\
1&0\\
1&0\\
0&1\\
0&1
\end{pmatrix}.
\]

The first column appears 2 times and the second column 3 times, so C fails; Q satisfies the structure of Theorem 2(b.2).

### 2. Design

Randomly generate continuous parameters, use \(Q^5\) to generate \(N=10^5\) data, and perform likelihood comparison in the candidate set.

### 3. result

True \(Q^5\) achieves maximum likelihood, numerically demonstrating the structural recovery of pan-recognition parameter points.

### 4. Explanation

Random continuous parameters fall within

\[
p_{00}p_{11}=p_{01}p_{10}
\]

The probability is 0. This experiment verifies typical points outside the zero test set and does not cover the failure points on the zero test set; the zero test set situation has been shown separately in the main article Scenario (a).

## Comparison of two groups of studies

|item| Study I | Study II |
| --- | --- | --- |
|Identification type|strict|Pan|
|At least 3 1's per column|Yes|No|
|Is true Q the largest?|Yes|Yes|
|Parameter dependency|any legal point|Outside the zero test set|

The same "true Q obtains maximum likelihood" graph has different theoretical guarantee strengths.
