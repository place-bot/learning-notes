# Condition B: The columns of \(Q^\star\) are different from each other

## 1. Definition

Write the complete Q as

\[
Q=
\begin{pmatrix}
I_K\\
Q^\star
\end{pmatrix}.
\]

Condition B requirements

\[
Q^\star_{\cdot k}\ne Q^\star_{\cdot\ell}
\qquad
\text{to all}k\ne\ell.
\]

What is compared is the column after deleting a set of unit matrices.

## 2. Why only compare \(Q^\star\)

The columns of \(I_K\) are naturally different from each other, but this difference comes from the attribute tag itself. If the remaining questions use attributes \(k\) and \(\ell\) in exactly the same way, the continuous parameters may absorb the structural differences between the two columns.

The mutuality of \(Q^\star\) adds an independent structural encoding to each attribute:

\[
k
\longmapsto
Q^\star_{\cdot k}.
\]

After restoring these codes, the attribute columns can only be replaced as a whole and cannot form more complex replacement structures.

## 3. Binary coding intuition

If \(Q^\star\) has \(m\) rows, it can provide up to

\[
2^m
\]

different column codes. To encode \(K\) attributes, you need at least

\[
m\ge\lceil\log_2K\rceil.
\]

This is where the logarithmic term in the minimum number of questions formula comes from.

## 4. Failure structure of \(K=2\)

When completeness and three measurements per column are established, if Condition B fails, Q of \(K=2\) can only have the following shape, allowing row replacement:

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&1\\
\vdots&\vdots\\
1&1
\end{pmatrix}.
\]

After deleting \(I_2\), both columns are all 1's. Results have proven that for any legal DINA parameter, there are infinitely many sets of alternative parameters that give the same response distribution, so this structure does not even hold universal recognition.

## 5. Difference from "column duplication"

Condition B does not require the columns of Q to be distinct from each other. After the entire Q contains \(I_K\), each column is of course different. It requires that measurement structures other than anchor items also distinguish attributes.

The checking steps are:

1. Select a row of unit vectors for each attribute;
2. Delete these lines;
3. Read the remaining matrix by column;
4. Count the number of different column vectors;
5. Passed when the quantity is equal to \(K\).

## 6. Multiple sets of unit arrays

If Q contains two sets of \(I_K\), after deleting one of them, the other set remains at \(Q^\star\), so B is automatically established.

This explains why the early "double complete" condition is safe, and also shows that it contains redundant structures: B only needs \(K\) mutually different column codes, and does not limit the column codes to form another set of unit arrays.
