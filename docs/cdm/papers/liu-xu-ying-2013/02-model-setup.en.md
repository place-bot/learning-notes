#Basic models, samples and all objects

## Three dimensions

Thesis uses:

- \(N\): Number of students;
- \(m\): item number;
- \(k\): Number of attributes.

The author assumes that \(m\) and \(k\) are known. Q is

\[
Q=(Q_{ij})_{m\times k}\in\{0,1\}^{m\times k}.
\]

Each row describes a question, and each column describes an attribute.

## Potential attributes of students

For any student,

\[
\boldsymbol A=(A^1,\ldots,A^k)^\top
\in\{0,1\}^k.
\]

\(A^j=1\) means that the student has mastered the attribute \(j\), and \(A^j=0\) means that he has not mastered it.

Attribute writing of student \(r\)

\[
\boldsymbol A_r=(A_r^1,\ldots,A_r^k)^\top.
\]

Properties are not directly observable. The probability of a certain pattern \(\boldsymbol A\) in the population is recorded as

\[
p_{\boldsymbol A}^*
=
\Pr(\boldsymbol A_r=\boldsymbol A).
\]

The sum of all \(2^k\) probabilities is 1.

##Students’ observation responses

For any student,

\[
\boldsymbol R=(R^1,\ldots,R^m)^\top
\in\{0,1\}^m,
\]

Among them, \(R^i=1\) means that question \(i\) is answered correctly.

Response writing from student \(r\)

\[
\boldsymbol R_r=(R_r^1,\ldots,R_r^m)^\top.
\]

The data set consists of

\[
\boldsymbol R_1,\ldots,\boldsymbol R_N
\]

composition. It is estimated that \(\boldsymbol A_1,\ldots,\boldsymbol A_N\) cannot be seen during Q.

## Element-by-element explanation of Q

\[
Q_{ij}=
\begin{cases}
1,&\text{item \(i\) requires attributes \(j\)},\\
0,&\text{item \(i\) does not require attributes \(j\)}.
\end{cases}
\]

The paper assumes that true Q does not have all-zero rows. This means that each question measures at least one attribute.

For example

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix}
\]

Can be interpreted as:

- Question 1 only requires attribute 1;
- Question 2 only requires attribute 2;
- Question 3 requires both attributes.

## Conjunction rules

The ability indicator for question \(i\) is

\[
\xi^i
=
\prod_{j=1}^k (A^j)^{Q_{ij}}
=
\mathbf 1(A^j\ge Q_{ij},\ j=1,\ldots,k).
\tag{2.1}
\]

The two ways of writing are completely equivalent.

If \(Q_{ij}=0\), then

\[
(A^j)^0=1,
\]

This property does not affect the product. If \(Q_{ij}=1\), \(A^j\) remains in the product; whenever a required attribute is missing, the product is 0.

Therefore:

\[
\xi^i=1
\quad\Longleftrightarrow\quad
\boldsymbol A\ge \boldsymbol q_i
\]

Established element by element.

## Noiseless model from Section 2

Study the article first

\[
R^i=\xi^i,
\qquad i=1,\ldots,m.
\tag{2.2}
\]

At this time:

- If the ability indicator is 1, the student must answer correctly;
- If the ability indicator is 0, the student will definitely answer the question incorrectly.

This layer separately exposes the combinatorial structure in the recognition problem. Section 3 adds mistakes and guesswork.

## Sample attribute ratio

If the latent attribute is conceptually visible, the proportion of pattern \(\boldsymbol A\) in the sample is

\[
\widehat p_{\boldsymbol A}
=
\frac1N
\sum_{r=1}^N
\mathbf 1(\boldsymbol A_r=\boldsymbol A).
\tag{2.4}
\]

These proportions are not actually directly calculable. They serve as a bridge between the observation moment and the overall distribution in theory:

\[
\widehat p_{\boldsymbol A}
\overset{\text{a.s.}}{\longrightarrow}
p_{\boldsymbol A}^*.
\]

## Object relations on this page

\[
\boldsymbol A_r
\xrightarrow[\text{Conjunctive rules}]{Q}
\boldsymbol\xi_r
\xrightarrow[\text{Noiseless or DINA}]{c,g}
\boldsymbol R_r.
\]

Statistical inference proceeds in the opposite direction: Q is inferred from the joint information of all \(\boldsymbol R_r\), while simultaneously profiling the attribute distribution.

[Next page: ideal response, B-vector and T-matrix](03-ideal-response-and-tmatrix.md)
