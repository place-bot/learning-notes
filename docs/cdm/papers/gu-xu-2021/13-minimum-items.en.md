# Minimum number of questions and \(K=8,J=12\) structure

## 1. Composition of the lower bound

The construction of Theorem 1 gives

\[
J\ge
K+\left\lceil\log_2K\right\rceil+1.
\]

The three parts serve respectively:

\[
\underbrace{K}_{I_K}
+
\underbrace{\lceil\log_2K\rceil}_{K\text{different column codes}}
+
\underbrace{1}_{\text{Complete each column with at least three 1's}}.
\]

This is a general structural bound that satisfies the conditions. For specific \(K\), the combined design check can also be done directly.

## 2. Q of \(K=8\)

The paper gives

\[
Q=
\begin{pmatrix}
I_8\\
0&0&1&1&1&0&1&1\\
0&1&0&1&0&1&1&1\\
1&0&0&0&1&1&1&1\\
1&1&1&1&1&1&0&1
\end{pmatrix}.
\]

The total number of questions is

\[
J=8+4=12.
\]

## 3. Check item by item

### A

The first 8 lines are \(I_8\).

### B

The last 4 lines form 8 four-digit column codes:

\[
\begin{aligned}
&(0,0,1,1)^\top,\ (0,1,0,1)^\top,\\
&(1,0,0,1)^\top,\ (1,1,0,1)^\top,\\
&(1,0,1,1)^\top,\ (0,1,1,1)^\top,\\
&(1,1,1,0)^\top,\ (1,1,1,1)^\top.
\end{aligned}
\]

Each of the eight columns is different.

### C

Each column already has a 1 in \(I_8\), and there are at least two more 1s in the next four rows, so the total count is at least 3.

## 4. Comparison with classical conditions

The sufficient conditions for the three-block tensor class are given by

\[
J\ge2K+1=17.
\]

The structure of this article uses 12 questions, reducing 5 questions, and the ratio is

\[
\frac{17-12}{17}\approx29.4\%.
\]

## 5. Design Implications

Additional questions do not need to be set as single-attribute questions. They can measure multiple properties simultaneously just like error correcting codes, as long as:

- The coding of attribute columns is different from each other;
- Accumulate at least three 1's in each column.

## 6. Verification of this website

The script on this website directly inputs the \(12\times8\) matrix and outputs:

```text
A=1 B=1 C=1 strict=1 counts=(3, 3, 3, 4, 4, 4, 4, 5)
```

This also checks the formula of the number of questions, the difference between the column codes and the count of each column.
