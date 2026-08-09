# Independent Proposal and DS1

## Independent proposal: Generate a legal Q from scratch

Construct first

\[
Q_A=
\begin{bmatrix}
I_K\\
I_K\\
\widetilde Q
\end{bmatrix}.
\]

The first \(K-1\) columns are generated sequentially. For the column \(k\), start with

\[
\{1,\ldots,J-2K\}
\]

Uniformly extract the columns and \(c_k\), and then uniformly extract from all column vectors containing \(c_k\) 1's.

## The last column is filled with zero rows

After the first \(K-1\) columns are generated, there are \(l\) rows of all zeros. The last column must fix these positions to 1 to ensure that each question requires at least one attribute.

Then extract

\[
c_K\in
\{\max(1,l),\ldots,J-2K\},
\]

And fill in the remaining positions with \(c_K-l\) 1s.

## Random item row replacement

Draw a random permutation matrix \(P\) and set

\[
Q^\star=P^{\mathsf T}Q_A.
\]

Unit matrix anchor points can appear at any item position. This step also illustrates that the recognizability condition only requires the existence of an appropriate row permutation.

## Advantages and disadvantages of independent proposals

Advantages:

- Every candidate is legal;
- Any \(Q\in\mathcal Q\) has a chance to be proposed;
- Irreducibility is established directly.

Disadvantages:

- Candidates almost reconstruct the entire matrix;
- Often far away from the current high posterior state;
- The acceptance rate in the original paper's pilot experiment was less than 0.5%.

## DS1: Update only one column

DS1 randomly selects column \(k\). To protect legality, it first identifies two types of locations.

### must be fixed to 1 position

If only the \(k\) column in a row is 1, once this 1 is deleted, an all-zero row will be generated. Suppose there are \(k_1\) such positions, and they are all fixed to 1.

### must be fixed to 0 position

For each other attribute \(i\ne k\), examine the form

\[
\boldsymbol e_i
\]

pure question. Updating column \(k\) might turn \(\boldsymbol e_i\) into a row that also requires \(i,k\). In order to ensure that the attribute \(i\) still retains two pure questions, two \(\boldsymbol e_i\) questions are randomly selected, and the \(k\) column is fixed to 0.

### Extract legal columns from the remaining positions

Except for the above fixed elements, the remaining positions can be freely taken as 0/1, but the column sum of the last \(k\) column must be at least 3.

## Limitations of DS1

DS1 may still change the entire column at once. The acceptance rate in the original paper pilot experiment was less than 5%. This result prompted the author to propose DS2: under the same set of protection rules, only a resizable subset of a column is moved.

## Relationship to supplementary code

Exposed C++'s main MH function implementation DS2. The independent generation logic is retained in `random_Q()` and is mainly used to generate legal initial values; DS1 is not used as a separate public entry.

[Next page: DS2 chunked dependency proposal step-by-step teardown](12-ds2.md)
