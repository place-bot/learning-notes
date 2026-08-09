# Sequential search algorithm

## Core Observation

When the number of real required attributes is fixed, the fewer cells the candidate q-vector differs from the true vector, the smaller the attribute profile misclassification is usually, and the smaller the shrinkage of \(\delta\).

This allows the algorithm to start with single-attribute candidates and add only one attribute each round:

\[
\text{Best single attribute}
\rightarrow
\text{Best dual attributes}
\rightarrow
\cdots
\]

In each round, the attributes already selected in the previous round are retained, and only "which attribute should be added" is compared.

## First step

Calculate \(K\) single-attribute candidates respectively:

\[
100\cdots0,\quad010\cdots0,\quad\ldots,\quad000\cdots1.
\]

Choose

\[
\alpha^{(1)}
=
\underset{k}{\arg\max}\ 
\widehat\delta_j(\boldsymbol e_k).
\]

The \(\delta\) values for attributes 1 and 2 in the hypothetical question are both .30. Original text optional attribute 1 as \(\alpha^{(1)}\).

## Step 2

Fix attribute 1 and combine it with the remaining \(K-1\) attributes one by one:

\[
11000,\ 10100,\ 10010,\ 10001.
\]

The optimal dual-attribute candidate is \(11000\),

\[
\delta^{(2)}=.60>\delta^{(1)}=.30.
\]

Therefore property 2 is accepted.

## The third step

Fixed attributes 1 and 2, and then added attributes 3, 4, and 5 respectively:

\[
11100,\ 11010,\ 11001.
\]

All three

\[
\delta^{(3)}=.51<\delta^{(2)}=.60.
\]

The added attributes did not improve the separation and the algorithm stopped at \(11000\).

## General form

Let the selected attribute set in step \(s-1\) be \(A_{s-1}\). Step \(s\) for each

\[
k\notin A_{s-1}
\]

Calculate the candidate \(A_{s-1}\cup\{k\}\) and take the maximum discrimination among them

\[
\widehat\delta_j^{(s)}
=
\max_{k\notin A_{s-1}}
\widehat\delta_j(A_{s-1}\cup\{k\}).
\]

In the ideal case of no sampling error:

- If \(\delta^{(s)}>\delta^{(s-1)}\), accept the new attribute;
- If \(\delta^{(s)}<\delta^{(s-1)}\), return the previous round vector;
- If it goes all the way to \(s=K\), compare the last two rounds and keep the better one.

The real data version will change the stop condition to increment exceeding \(\varepsilon\).

## Number of candidates

Worst case scenario needs to be checked

\[
K+(K-1)+\cdots+1
=\frac{K(K+1)}{2}
\]

candidate.

If the correct q-vector contains \(K_j\) attributes, the algorithm will also perform a stop check of "trying to add the \(K_j+1\) attribute". The actual number given in the original text is

\[
(K_j+1)K-\frac{K_j^2+K_j}{2}.
\]

In the hypothetical question \(K=5,K_j=2\):

\[
3(5)-\frac{2^2+2}{2}=12.
\]

This is exactly:

\[
5+4+3=12.
\]

## The meaning of computational complexity

| \(K\) |exhaustive candidates|Sequential search upper limit|
| ---: | ---: | ---: |
| 5 | 31 | 15 |
| 10 | 1,023 | 55 |
| 20 | 1,048,575 | 210 |
| 30 | 1,073,741,823 | 465 |

Sequential search significantly reduces the amount of calculation, but it is a greedy algorithm. If there is a local optimum in the \(\delta\) terrain in the data, after selecting the wrong attribute early, subsequent candidates will be limited to the wrong path.

