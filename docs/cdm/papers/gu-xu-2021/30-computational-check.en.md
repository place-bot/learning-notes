# This site can calculate verification and code review

## 1. Independent implementation

This site provides zero third-party dependency scripts:

```bash
python tools/gu_xu_2021_identifiability_check.py
```

It implements:

- A/B/C of Theorem 1;
- Pan-integrity attribute--item matching;
- Two-block universal holon matrix and residual coverage search for Theorem 4;
- \(5\times2\) non-zero row Q-space enumeration;
- \(K=8,J=12\) Thesis structure verification.

## 2. Paper sample output

```text
Q5_generic_DINA     A=1 B=1 C=0 strict=0 generic-complete=1 D+E=0
Q15_strict_DINA     A=1 B=1 C=1 strict=1 generic-complete=1 D+E=1
Q18_strict_DINA     A=1 B=1 C=1 strict=1 generic-complete=1 D+E=1
Q27_generic_GDINA   A=0 B=0 C=1 strict=0 generic-complete=1 D+E=1
Q54_generic_GDINA   A=1 B=0 C=1 strict=0 generic-complete=1 D+E=1
Q81_generic_GDINA   A=0 B=0 C=1 strict=0 generic-complete=1 D+E=1
```

Here D+E is a sufficient condition for universal recognition of general RLCM and cannot be used to replace the judgment of DINA Theorem 2.

## 3. \(K=8,J=12\)

Script verification paper matrix:

```text
A=1 B=1 C=1 strict=1
counts=(3, 3, 3, 4, 4, 4, 4, 5)
```

Therefore, the 12 questions meet the three structural requirements at the same time.

## 4. Independent enumeration \(5\times2\)

Each line can only take

\[
(0,1),(1,0),(1,1),
\]

share

\[
3^5=243
\]

Zhang ordered matrix. By exchanging the entire column to obtain the equivalence class, the Burnside count is

\[
\frac{243+1}{2}=122.
\]

This site enumerates the results:

```text
column-swap classes: 122
Theorem 1 candidates: 45; row/column forms: 2
Theorem 4 candidates: 71; row/column forms: 6
```

This verifies what the paper says are two strictly identified structural shapes, as well as Study V's six D/E structural shapes.

## 5. Verification of official `Q_aa.mat`

Author file path can be appended:

```bash
python tools/gu_xu_2021_identifiability_check.py \
  --author-mat path/to/Identify_Q/simulations/Q_aa.mat
```

The official document actually contains 121 unique column exchange representations. According to the paper text "Exclude all-zero rows and only merge column swaps", the combined count should be 122.

The missing ordered representation can be written as

\[
\begin{pmatrix}
1&1\\
1&1\\
1&1\\
1&1\\
0&1
\end{pmatrix}.
\]

It has the same row multiset as \(Q^{81}\), except for the item row order. Therefore:

- The literal statement "121 covers all ordered candidates" is one less category;
- All six structural shapes of Study V are still represented;
- Candidate-by-candidate likelihood exhaustion for a fixed item order, the candidate set is not a complete 122 category in the combinatorial sense.

## 6. Cross-checking with official checkers

This site implements fixed paper names:

- B = \(Q^\star\) columns are different from each other;
- C = at least three 1's per column.

It also does rectangular and binary checks for the input, and returns the complete result on each path to avoid unassigned output when the official function part exits early.

## 7. Scope of verification of this site

The script reviews discrete structure conditions and candidate space counts without rerunning the main text EM 800,000 times or rerunning the entire G-DINA exhaustive run of \(N=10^5\). The probabilistic equality values ​​in the original article come from the author's MATLAB experiments, and are recorded item by item in the notes of this site according to supplementary materials.
