# Universal completeness and bipartite graph matching

## 1. Definition

A \(J\times K\) Q is universally complete, which means that it contains a certain \(K\times K\) submatrix, and the diagonals are all 1 after row and column replacement:

\[
\begin{pmatrix}
1&*&\cdots&*\\
*&1&\cdots&*\\
\vdots&\vdots&\ddots&\vdots\\
*&*&\cdots&1
\end{pmatrix}.
\]

The asterisk can be 0 or 1.

## 2. Relationship with integrity

Integrity requires that the submatrix be exactly \(I_K\). Universal completeness only requires that each attribute can match a related question for different people.

\[
\text{complete}
\Longrightarrow
\text{Pan-complete}.
\]

The inverse relationship does not hold. For example

\[
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
\]

It is comprehensive and complete, and there are no single attribute questions.

## 3. Bipartite graph representation

Construct a bipartite graph:

- Left node: \(K\) attributes;
- Node on the right: \(J\) question;
- \(q_{jk}=1\) connects the property \(k\) with the question \(j\).

Q is universally complete if and only if there is a match covering all attributes, and each attribute matches a different question.

```text
Attribute 1 ───── Question a
Attribute 2 ───── Question c
Attribute 3 ───── Question b
```

## 4. Hall conditions

For any attribute subset \(S\), let \(N(S)\) be the set of items that measure at least one attribute in \(S\). Hall's matching theorem gives:

\[
|N(S)|\ge|S|
\quad
\text{to all}S\subseteq\{1,\ldots,K\}
\]

If and only if there is a match covering all attributes.

## 5. Official implementation

`check_generic_complete.m` enumerate all

\[
2^K-1
\]

non-empty attribute subsets, calculate the number of neighbor questions for each subset and check the Hall condition.

The time complexity increases with at least \(2^K\). For the larger \(K\), you can directly run the maximum matching of the bipartite graph to determine whether there is a match of size \(K\) in polynomial time.

The script on this site uses direct match search to maintain zero dependencies and readability; production implementation can be replaced by the Hopcroft--Karp algorithm.

## 6. Statistical meaning

Universal completeness allows each anchor question to depend on other properties simultaneously. Generally, the multi-parameter response surface of RLCM can use these cross-questions to separate attribute directions, so there is no need to force single-attribute anchor questions for general recognition.

This relaxation only corresponds to general recognition. Strict joint recognition still requires stronger structures.
