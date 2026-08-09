# Proof route for Theorem 1

## 1. Prove the starting point

Assume that both groups of subjects give the same response distribution:

\[
T(Q,\boldsymbol c,\boldsymbol g)\boldsymbol p
=
T(\bar Q,\bar{\boldsymbol c},\bar{\boldsymbol g})
\bar{\boldsymbol p}.
\]

Arrange the first \(K\) rows of true Q according to Condition A into \(I_K\). The goal is to prove step by step that the surrogate model can only be equal to the true model, allowing column permutations.

## 2. Five steps for sufficiency proof

The supplementary material breaks the main proof into five steps.

### Step 1: Limit the first \(K\) rows of the substitution matrix

Use the column mutuality of \(Q^\star\) to construct the attribute order, and prove it by induction:

\[
\bar Q_{1:K,\cdot}
\]

After column permutation, it must be an upper triangle with all 1's on the diagonal.

The key idea is to select \(Q^\star\) rows that distinguish a certain column from previous columns, and then use T-matrix translation to create zero entries. If the candidate row lacks the expected 1, it will conflict with the strictly monotonic relationship \(c_j>g_j\).

### Step 2: Identify non-anchor questions \(c_j\)

Yes

\[
j=K+1,\ldots,J,
\]

Select the response moment containing question \(j\) and a set of auxiliary questions. Condition C ensures that each attribute has enough items to participate in the product. Comparing the translated T-matrix rows gives

\[
\bar c_j=c_j.
\]

### Step 3: Identify the anchor question \(g_k\)

For each unit question \(k\), construct a moment combination to avoid the latent class of ability, and use the triangular structure in Step 1 and the parameter elimination identified in Step 2 to get

\[
\bar g_k=g_k.
\]

### Step 4: Tighten the upper triangle shape to \(I_K\)

If some off-diagonal position of \(\bar Q_{1:K,\cdot}\) is still 1, pick two true unit questions and compare specific T rows. The already identified \(g\) and \(c\) would force a contradiction.

Therefore

\[
\bar Q_{1:K,\cdot}\sim I_K.
\]

### Step 5: Restore the remaining Q, all parameters and proportions

After the first \(K\) rows on both sides are aligned to \(I_K\), continue to compare the ideal response columns of each non-anchor question, and get

\[
\bar Q\sim Q.
\]

The DINA parameter identification result given for Q is then given

\[
\bar{\boldsymbol c}=\boldsymbol c,\qquad
\bar{\boldsymbol g}=\boldsymbol g,\qquad
\bar{\boldsymbol p}=\boldsymbol p.
\]

## 3. Three lines of necessity

### A failed

There are equivalent latent classes, and the proportions can be redistributed; in some scenarios, another \(\bar Q\) can also be constructed.

### B failed

The two attributes have the same column code in \(Q^\star\), and parameter compensation can be constructed to make the structure non-unique.

### C failed

Only one or two questions appear for a certain attribute. It is known that the necessary conditions for DINA parameter identification of Q have shown that strict identification fails; Theorem 2 further characterizes the two problem situations.

## 4. Prove the core of technology

This set of proofs does not directly apply universal three-way tensor uniqueness. It uses DINA's special structure of only two probabilities \(c_j,g_j\) for each question, through:

\[
\text{T-matrix translation}
+\text{zero pattern construction}
+\text{partial order induction}
+\text{parameter-by-parameter elimination}
\]

Convert a set of identity arrays and column codes into model-wide uniqueness.
