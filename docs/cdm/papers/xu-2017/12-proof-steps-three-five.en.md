# Proof steps 3--5

## Step 3: Complete the zero-order and first-order attribute columns

Step 3 To prove

\[
\theta_{j,\boldsymbol0}
=
\bar\theta_{j,\boldsymbol0},
\qquad
\theta_{j,\boldsymbol e_k}
=
\bar\theta_{j,\boldsymbol e_k},
\qquad j\le2K,
\]

and

\[
p_{\boldsymbol0}
=
\bar p_{\boldsymbol0},
\qquad
p_{\boldsymbol e_k}
=
\bar p_{\boldsymbol e_k}.
\]

### C2 generates contrast vectors

From steps 1--2, the remaining questions are between \(\boldsymbol0\) and
The parameters of column \(\boldsymbol e_k\) have been equalized across both sets of models. C2 Guarantee

\[
\left(
1,\theta_{2K+1,\boldsymbol e_k},\ldots,
\theta_{J,\boldsymbol e_k}
\right)^\top
\]

and

\[
\left(
1,\theta_{2K+1,\boldsymbol0},\ldots,
\theta_{J,\boldsymbol0}
\right)^\top
\]

Disproportionate. Then \(\boldsymbol u_k\) exists so that the previous vector remains as
\(b_k\ne0\), the latter vector is eliminated to 0.

Applying \(\boldsymbol u_k\) to a matrix composed of constant rows and remaining question rows is equivalent to constructing a
A linear combination that retains information in the \(\boldsymbol e_k\) column and disappears in the \(\boldsymbol0\) column.

### Combined with anchor question selection line

The paper multiplies this linear combination element-wise with the transformed rows of the first \(2K\) anchor questions. Comparing the two rows of equations "without adding the \(k\) anchor question" and "after adding it", we get

\[
\theta_{k,\boldsymbol e_k}
=
\bar\theta_{k,\boldsymbol e_k}.
\tag{4.11}
\]

The same goes for the second unit block:

\[
\theta_{K+k,\boldsymbol e_k}
=
\bar\theta_{K+k,\boldsymbol e_k}.
\]

Swapping the roles of retention and elimination, the zero attribute probability of the previous \(2K\) problem can be identified.

### Isolation class ratio

When the anchor question parameters are equal, the selection is only in
\(\boldsymbol0\) transformed rows with non-zero columns, equation (3.5) directly gives

\[
p_{\boldsymbol0}
=
\bar p_{\boldsymbol0}.
\]

Then for each \(\boldsymbol e_h\), construct only rows that are non-zero in this column, and get

\[
p_{\boldsymbol e_h}
=
\bar p_{\boldsymbol e_h}.
\tag{4.13}
\]

Finally, add any of the previous questions \(2K\) to the corresponding selection row, and pass the identified
\(p_{\boldsymbol e_h}>0\) obtains its single attribute column item with equal probability.

## Step 4: Two attribute columns

Fixed \(1\le h_1<h_2\le K\). The goal is

\[
p_{\boldsymbol e_{h_1}+\boldsymbol e_{h_2}}
=
\bar p_{\boldsymbol e_{h_1}+\boldsymbol e_{h_2}},
\]

\[
\theta_{j,\boldsymbol e_{h_1}+\boldsymbol e_{h_2}}
=
\bar\theta_{j,\boldsymbol e_{h_1}+\boldsymbol e_{h_2}}
\quad\forall j.
\]

The paper chooses the new \(\boldsymbol\theta^*\) so that the product of the first \(K\) anchor rows is non-zero on at most two columns:

\[
\boldsymbol e_{h_2},
\qquad
\boldsymbol e_{h_1}+\boldsymbol e_{h_2}.
\]

The item parameters and class scale of the previous column have been identified by step 3. After subtracting the marginal equations of the two sets of models, the known columns cancel out, leaving only two attribute columns, so we identify

\[
p_{\boldsymbol e_{h_1}+\boldsymbol e_{h_2}}.
\]

Add question \(j\) to the item subset and isolate it
\(\theta_{j,\boldsymbol e_{h_1}+\boldsymbol e_{h_2}}\)。

Use the first unit block construction for \(j>K\); use the second unit block symmetrically for \(j\le K\) to eventually cover all questions.

## Step 5: Summarize by number of attributes

Assume that all patterns containing less than \(k\) attributes have been identified, that is, for \(l<k\):

\[
p_{\sum_{i=1}^l\boldsymbol e_{h_i}}
=
\bar p_{\sum_{i=1}^l\boldsymbol e_{h_i}},
\]

\[
\theta_{j,\sum_{i=1}^l\boldsymbol e_{h_i}}
=
\bar\theta_{j,\sum_{i=1}^l\boldsymbol e_{h_i}}.
\]

For a target schema with \(k\) attributes

\[
\boldsymbol\alpha^*
=
\sum_{i=1}^k\boldsymbol e_{h_i},
\]

take

\[
\theta_i^*
=
\begin{cases}
\theta_{i,\boldsymbol0},
&i\in\{h_1,\ldots,h_k\},\\
\theta_{i,\boldsymbol1},
&i\in\{1,\ldots,K\}
\setminus\{h_1,\ldots,h_k\},\\
0,&\text{Other questions}.
\end{cases}
\]

The resulting selection row's non-zero columns will only come from a subset of the target attribute set. All proper subset terms have been identified by the inductive hypothesis, so the only new unknown class proportion in the marginal equation is

\[
p_{\boldsymbol\alpha^*}.
\]

First identify the ratio, and then add the identification of question \(j\)
\(\theta_{j,\boldsymbol\alpha^*}\). Make a symmetrical structure for the second unit block and cover the remaining questions.

Advancing from \(k=3\) to \(K\), all potential class columns are identified.

## Five steps together

|steps|newly recognized object|
| --- | --- |
| 1 |\(\boldsymbol0\) column for \(Q'\) question|
| 2 |All \(\boldsymbol e_k\) columns for \(Q'\) questions|
| 3 |Zero/single attribute columns of two \(I_K\) blocks and corresponding \(p\)|
| 4 |All two attribute columns and corresponding \(p\)|
| 5 |Three attributes to full attribute column and corresponding \(p\)|

eventually

\[
\Theta=\bar\Theta,
\qquad
\boldsymbol p=\bar{\boldsymbol p},
\]

Complete Theorem 1.

## Abstract form of proof strategy

\[
\text{Anchor block zero suppression}
\longrightarrow
\text{The low-level attribute profile is identified first}
\longrightarrow
\text{Known true subset terms cancel}
\longrightarrow
\text{Inductively identify higher-order patterns}.
\]

This explains why the author arranged the columns of \(\Theta\) by the Hamming weight of the attribute profile.
