# Column replacement equivalence, completeness and saturation

## Column replacement equivalent

Thesis definition

\[
Q\sim Q'
\]

If and only if Q and \(Q'\) have the same set of columns, the sort order can be different. Equivalently, there exists a permutation matrix \(P\) of \(k\times k\) such that

\[
Q'=QP.
\]

If there is no such column permutation, it is written as

\[
Q\not\sim Q'.
\]

## Why attribute tags cannot be identified by answering

take

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix},
\qquad
Q'=
\begin{pmatrix}
0&1\\
1&0\\
1&1
\end{pmatrix}.
\]

\(Q'\) swapped two columns. As long as the probabilities of attribute profiles \(10\) and \(01\) are exchanged at the same time, all response probabilities remain unchanged.

The response data can find that "there are two different attribute dimensions and their item structures", but it cannot independently decide which column should be named "addition" or "multiplication". Naming requires item content or expert information.

## Three properties of equivalence relations

\(\sim\) meets:

1. Reflexivity: \(Q\sim Q\);
2. Symmetry: \(Q\sim Q'\Rightarrow Q'\sim Q\);
3. Transitivity: \(Q\sim Q'\) and \(Q'\sim Q''\Rightarrow Q\sim Q''\).

Therefore all Q are divided into non-overlapping equivalence classes. The main theorem recovers \([Q]\).

## Complete Q

Let \(\boldsymbol e_j\) be the \(j\)th standard basis vector. The paper calls Q **complete** if

\[
\{\boldsymbol e_1^\top,\ldots,\boldsymbol e_k^\top\}
\subseteq\mathcal R_Q,
\]

where \(\mathcal R_Q\) is the set of row vectors of Q.

That is, each attribute has at least one question that only requires itself.

After rearranging item rows and attribute columns, the complete Q can be written as

\[
Q=
\begin{pmatrix}
I_k\\
Q^*
\end{pmatrix}.
\]

Completeness immediately entails

\[
m\ge k.
\]

## The use of completeness in proofs

The unit matrix item allows the author to extract a block upper triangular submatrix of order \(2^k-1\) from \(T(Q)\):

\[
\begin{pmatrix}
I_k&*&*&\cdots\\
0&I_{\binom{k}{2}}&*&\cdots\\
0&0&I_{\binom{k}{3}}&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix}.
\]

Its diagonal blocks are all unit matrices, so \(T(Q)\) has full column rank. Full column rank guarantees that when Q is known, the attribute distribution is uniquely determined by all moments.

## Saturated T-matrix

\(T(Q)\) saturation means that it contains rows corresponding to each non-empty subset of items:

\[
I_{i_1}\wedge\cdots\wedge I_{i_\ell},
\qquad
1\le\ell\le m.
\]

The total number of rows is

\[
2^m-1.
\]

Saturation provides two types of key lines in proofs:

- All combinations of unit array items are used to construct full-rank submatrix;
- "All questions" and "All questions after removing a certain question" are used to compare the row ratio and lock \(c_i\).

## Division of completeness and saturation

|Conditions|Object of action|Proof effect|
| --- | --- | --- |
|Q complete|The design of item attributes|Generate unit matrix anchor points and establish full column rank|
|T saturated|Which joint reaction moments are used?|Provide all required question group rows to establish column space separation|

They are all sufficient conditions for the consistency theorem of this article. The original text Remark 2.7 clearly states that some scenarios may use weaker conditions, but this article does not give a general weakest condition.

## Intuitive meaning in design

Completeness requires a "pure question" for each attribute. C5 will also ask for it to appear again in another question. Together they form a minimal redundancy:

- A pure question about locating the attribute direction;
- At least one other question provides cross-validation;
- The joint reaction moment connects two pieces of information.

[Next page: C1--C5](08-conditions-c1-c5.md)
