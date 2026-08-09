# Proof idea

## Demonstrate what to exclude

from

\[
[M_1,M_2,M_3]=[N_1,N_2,N_3]
\tag{7}
\]

To start, it is necessary to prove that two sets of three factor matrices correspond column-by-column, allowing common permutation and scaling.

The main thread of Kruskal's original article relies on **Permutation Lemma**: if two sets of columns maintain the same sparse linear combination structure under enough projections, they must match column-by-column. The original proof is longer in technical details.

Rhodes (2010) gives a compact proof of the same Theorem 4a. This page uses it to demonstrate the algebraic mechanism and to distinguish subsequent proofs from the original 1977 text.

## The first step: first process the two factors to fill the column rank

Set

\[
M_1,M_2\in\mathbb F^{s\times R}
\]

The column ranks are all full, and \(M_3\) has no zero columns.

Take a vector \(\boldsymbol c\) such that

\[
\boldsymbol c^\mathsf T M_3
\]

Every element of is non-zero. Shrink the tensor in the third direction:

\[
A_{\boldsymbol c}
=
\boldsymbol c^\mathsf T*_{3}
[M_1,M_2,M_3].
\]

Using the triple product,

\[
A_{\boldsymbol c}
=
M_1
\operatorname{diag}(\boldsymbol c^\mathsf T M_3)
M_2^\mathsf T.
\tag{8}
\]

The middle diagonal matrix is invertible, so

\[
\operatorname{rank}(A_{\boldsymbol c})=R.
\]

Equation (7) also gives

\[
A_{\boldsymbol c}
=
N_1
\operatorname{diag}(\boldsymbol c^\mathsf T N_3)
N_2^\mathsf T.
\]

Therefore, \(N_1,N_2\) must also have rank \(R\), and be spread into the same column space as \(M_1,M_2\).

## Step 2: Look at tensor slices after changing the base

To change the basis in the common column space, we can put

\[
M_1=M_2=I_R
\]

as a normalized situation.

Fix the third coordinate \(i\) to get the matrix slice

\[
S_i
=
\operatorname{diag}(\bar{\boldsymbol m}^{\,3}_i),
\]

where \(\bar{\boldsymbol m}^{\,3}_i\) is row \(i\) of \(M_3\).

Another set of decompositions gives

\[
S_i
=
N_1
\operatorname{diag}(\bar{\boldsymbol n}^{\,3}_i)
N_2^\mathsf T.
\]

Then multiply by \(A_{\boldsymbol c}^{-1}\) to get a family of matrices that can be diagonalized at the same time:

\[
S_iA_{\boldsymbol c}^{-1}.
\tag{9}
\]

## Step 3: Common feature subspace recovery column grouping

In the \(M\) representation, the \(r\)th eigenvalue of equation (9) is

\[
\frac{m^3_{ir}}
{\boldsymbol c^\mathsf T\boldsymbol m^3_r}.
\]

The two numbers \(r,s\) produce the same set of eigenvalues for all \(i\), if and only if

\[
\boldsymbol m^3_r
\quad\text{with}\quad
\boldsymbol m^3_s
\]

proportional.

So the common feature subspace groups the columns of \(M_3\) "proportionally to each other". Since the same family of matrices also comes from the \(N\) representation, the two sets of decompositions must give the same grouping of eigensubspaces, resulting in a common permutation.

## Step 4: \(k_{M_3}\ge2\) shrink the group into a single column

If

\[
k_{M_3}\ge2,
\]

Any two columns are independent and cannot be proportional. Each common feature subspace corresponds to only one column number.

So:

- The columns of \(M_1\) correspond to \(N_1\) one by one;
- \(M_2\) and \(N_2\) use the same corresponding relationship;
- After comparing eigenvalue, \(M_3\) and \(N_3\) also use the same substitution;
- Only column-by-column scaling remains in the three directions.

This proves the special case of "two factors have full column rank, and the third factor \(k\)-rank is at least 2".

## Step 5: Rewrite the general situation into defect quantity

Order

\[
a_i=R-k_{M_i},
\qquad i=1,2,3.
\]

Kruskal condition becomes

\[
a_1+a_2+a_3\le R-2.
\]

Rhodes called the triple a type

\[
(R;a_1,a_2,a_3).
\]

The smaller the amount of defects, the closer the factor is to full column rank.

## Step 6: Projection, deletion and induction

The core operations of the general proof are as follows:

1. Select a column subset;
2. Construct the projection \(\Pi_i\) so that its zero space exactly contains the space spanned by these columns;
3. Apply \(\Pi_i\) to the \(i\) direction of the tensor;
4. The eliminated column corresponds to zero triad and can be deleted from the triple product;
5. Use special cases or inductive hypotheses on the remaining fewer columns;
6. Restore the same space formed by a subset in \(M_i\) and \(N_i\);
7. Change the projected subset and gradually refine "subspace matching" into "single column matching".

Kruskal rank comes into play here: no matter which set of columns is deleted or retained, the independence of the remaining columns is guaranteed as long as the number does not exceed the threshold.

## Step 7: Why the three scalings must cancel

Finally got

\[
\boldsymbol n^1_r
=\lambda_r\boldsymbol m^1_{\sigma(r)},
\]

\[
\boldsymbol n^2_r
=\mu_r\boldsymbol m^2_{\sigma(r)},
\qquad
\boldsymbol n^3_r
=\nu_r\boldsymbol m^3_{\sigma(r)}.
\]

The \(r\) triad becomes

\[
\lambda_r\mu_r\nu_r
\left(
\boldsymbol m^1_{\sigma(r)}
\otimes
\boldsymbol m^2_{\sigma(r)}
\otimes
\boldsymbol m^3_{\sigma(r)}
\right).
\]

The tensors on both sides are the same and the columns have been aligned item by item, so

\[
\lambda_r\mu_r\nu_r=1.
\]

This results in co-permutations and mutually canceling scaling.

## Prove the shortest memory version of the main line

\[
\text{Tensors are equal}
\rightarrow
\text{shrink into matrix}
\rightarrow
\text{co-diagonalization}
\rightarrow
\text{Restore grouping of proportional columns}
\]

\[
\rightarrow
\text{\(k\)-rank eliminates confusion within the group}
\rightarrow
\text{Projection and induction to deal with non-full rank situations}
\rightarrow
\text{Co-displacement and scaling}.
\]
