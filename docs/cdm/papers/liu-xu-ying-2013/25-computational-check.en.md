# This site can calculate and verify

## Fixed teaching settings

Script usage

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&1\\
1&1
\end{pmatrix}.
\]

This Q satisfies:

- Complete: the first two lines are \(I_2\);
- Each attribute is required by at least three questions;
- Saturated T contains \(2^4-1=15\) question group rows.

attribute profile press

\[
00,\ 01,\ 10,\ 11
\]

Arrange, take

\[
\boldsymbol p^*
=(0.10,0.20,0.30,0.40)^\top,
\]

\[
\boldsymbol c
=(0.85,0.82,0.90,0.88)^\top,
\]

\[
\boldsymbol g
=(0.15,0.18,0.10,0.12)^\top.
\]

## Run method

```bash
python3 tools/liu_xu_ying_2013_theory_check.py --mode all
```

It can also be run separately:

```bash
python3 tools/liu_xu_ying_2013_theory_check.py --mode structural
python3 tools/liu_xu_ying_2013_theory_check.py --mode separation
python3 tools/liu_xu_ying_2013_theory_check.py --mode counterexample
python3 tools/liu_xu_ying_2013_theory_check.py --mode finite --replicates 20
```

## Verification 1: Full column rank

Noiseless \(T(Q)\) excludes all zero attribute columns, the shape is

\[
15\times3.
\]

Script result:

```text
saturated deterministic T shape: (15, 3)
rank(T): 3 (target 3)
```

It is the same as Proposition 6.1

\[
\operatorname{rank}(T)=2^k-1=3
\]

consistent.

Augmenting T with guessing retains all four attribute profiles, and the script gets

```text
rank(augmented noisy T): 4
```

It is consistent with the full column rank conclusion of Proposition 6.6.

## Verification 2: Guess elimination transformation

The script explicitly constructs D and compares

\[
D\widetilde T_{c,g}(Q)
\]

with

\[
(0,T_{c-g}(Q)).
\]

The maximum element-wise error is

```text
1.110e-16
```

This is the double-precision floating-point rounding magnitude, which verifies Equation (6.3) and the corresponding matrix identity of the inductive construction.

## Verification 3: Column replacement

Swap the two columns of Q and swap the attribute profile columns according to the same rules. The maximum difference is

```text
0.000e+00
```

This directly demonstrates the observational invariance corresponding to the \(\sim\) equivalence relation.

## Verification 4: Overall column space separation

Each non-zero q-vector has three choices, and there are a total of four questions

\[
3^4=81
\]

Candidate Q that does not have all-zero rows.

For each candidate, the script profiles \(\boldsymbol p\) on the probability simplex. The result is:

```text
candidate matrices: 81
matrices in the true column-permutation class: 2
candidates with numerical zero loss: 2
best inequivalent loss: 0.105301
```

Only true Q and Q after swapping two columns achieve numerical zero loss. The closest false equivalence class is still about \(0.1053\) away from the true total moment.

This enumeration only verifies the current small example. The general conclusion is proved by the original proposition.

## Verification 5: C4 failed

Put all probability mass in full mastery mode:

\[
\boldsymbol p=(0,0,0,1)^\top,
\]

and adopt a noiseless model. Script result:

```text
candidate matrices reproducing the moments: 81/81
every nonempty item-set moment equals 1
```

All candidates are able to replicate the reaction moments, accurately reproducing the counterexample of Remark 2.4.

## Verification 6: Limited sample demonstration

Using the fixed seed `20260726`, each sample size is repeated 20 times. \(c,g\) is known, and a global enumeration is performed among 81 candidates each time:

| \(N\) |Restore True Column Permutation Equivalence Class|average win loss|
| ---: | ---: | ---: |
| 100 | 16/20（80.0%） | 0.07807 |
| 500 | 20/20（100.0%） | 0.03290 |
| 2000 | 20/20（100.0%） | 0.01691 |

As \(N\) increases, the win loss decreases and the recovery rate increases in this simple setting.

## Interpretation boundaries of numerical results

These 60 pieces of data belong to the teaching demonstration of this website, and the original text does not have these numbers. The number of repetitions is small, Q is small, and \(\boldsymbol p,c,g\) is in good condition. The result can verify the code flow and theorem intuition, but cannot give general sample size suggestions.

More rigorous follow-up experiments should systematically change:

- \(m,k\)；
- Minimum attribute profile probability;
- Signal strength of \(c_i-g_i\);
- the truncation order of T;
- redundancy of Q;
- The extent to which \(c,g\) is known;
- Global search and local search.

[Next page: Limitations, conclusions and future work](26-limitations-conclusion-future.md)
