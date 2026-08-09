# Experiment：DINA Studies III--IV

## Study III: Even local pan-recognition failed

### 1. Three true Qs

\[
Q^{10}=
\begin{pmatrix}
0&1\\
0&1\\
0&1\\
1&0\\
0&1
\end{pmatrix}
\]

The first column appears only 1 time.

\[
Q^{21}=
\begin{pmatrix}
0&1\\
1&1\\
0&1\\
1&1\\
0&1
\end{pmatrix}
\]

Incomplete, missing \((1,0)\) single attribute row.

\[
Q^{55}=
\begin{pmatrix}
0&1\\
0&1\\
0&1\\
0&1\\
1&1
\end{pmatrix}
\]

The information in the first column is highly insufficient, and the relevant structure does not meet the general recognition conditions.

### 2. result

In all three scenarios, true Q does not achieve the maximum log-likelihood, and multiple false candidates have higher likelihoods. Figure 6 clearly separates the red true Q from the purple maximum likelihood candidate.

### 3. Interpretation

The finite sample MLE selection error Q is consistent with the theoretical misidentification direction. The theoretical statement is stronger: the true distribution itself allows for locally continuous equivalent objects.

## Study IV: The Necessity of Integrity

### 1. Scene

Author settings:

\[
(K,J)=(3,20)
\quad\text{with}\quad
(5,20).
\]

Each scene starts from incomplete Q, constructs two substitution matrices \(Q'\) and \(Q''\), and adjusts the latent class ratio.

### 2. Construction logic

Define ideal response matrix

\[
\Gamma_{j,\boldsymbol\alpha}(Q)
=
I(\boldsymbol\alpha\succeq\boldsymbol q_j).
\]

\(\Gamma\), which replaces Q, contains more ideal response columns. For columns that appear newly in the surrogate model and are not in the true model, set the corresponding latent class proportion to 0; then merge these qualities into the latent classes in the same column as the true model.

The item parameters remain unchanged.

### 3. Full distribution verification

Compute all for each model

\[
2^{20}=1,048,576
\]

probability of a reaction pattern.

#### \(K=3\)

\[
\max_{\boldsymbol r}
|\Pr_Q(\boldsymbol R=\boldsymbol r)
-\Pr_{Q'}(\boldsymbol R=\boldsymbol r)|
=2.17\times10^{-19},
\]

\[
\max_{\boldsymbol r}
|\Pr_Q(\boldsymbol R=\boldsymbol r)
-\Pr_{Q''}(\boldsymbol R=\boldsymbol r)|
=4.34\times10^{-19}.
\]

#### \(K=5\)

The corresponding maximum difference is

\[
2.17\times10^{-19}
\quad\text{and}\quad
6.51\times10^{-19}.
\]

### 4. result analysis

These errors are lower than MATLAB's double-precision machine error

\[
2.22\times10^{-16}.
\]

Study IV gives an explicit observational equivalent construction and directly verifies that incomplete Q cannot be jointly identified.

### 5. Relationship with the main text hypothesis

The alternative latent class proportions in the construct contain 0 to demonstrate observational equivalence for different Q. The main text true model assumes all \(p_\alpha>0\); the necessity proof deals with strictly positive parameter spaces via more general parameter constructions. The role of the Numeric Study is to visually demonstrate the \(\Gamma\) column merging mechanism.
