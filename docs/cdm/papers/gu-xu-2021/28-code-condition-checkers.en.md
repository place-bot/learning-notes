# Intensive reading of official condition checking code

## 1. Warehouse structure

The official repository [`yuqigu/Identify_Q`](https://github.com/yuqigu/Identify_Q) of `check_conditions/` contains:

|File|function|
| --- | --- |
| `check_conditions_main.m` |6 sample portals|
| `check_Theorem1.m` |DINA strictly identifies A/B/C|
| `check_Theorem2.m` |DINA universal recognition branch of two measurements|
| `check_Theorem3.m` |Necessary conditions for the number of repetitions of general RLCM|
| `check_Theorem4.m` |Search the three-block question set for D/E|
| `check_generic_complete.m` |Checking universal completeness using Hall conditions|
| `check_complete.m` |Search for a set \(I_K\)|
| `check_double_complete.m` |Search two sets of single attribute questions|

The last visible commit of `master` in the warehouse is 2019-05-04, and the code uses MATLAB.

## 2. `check_Theorem1.m`

The calculation chain is:

```text
the number of 1's in each column
   │
   ├── Search for each unit row e_k
   ├── Delete selected I_K
   ├── unique(Qstar', 'rows') counts different columns
   └── Multiply three Boolean quantities
```

The core judgment is equivalent to:

\[
I(A)\,I(B)\,I(C).
\]

### Comment bias

The code annotates "at least three 1's in each column" as Condition B, and annotates "\(Q^\star\) columns are different from each other" as Condition C. The order of names in the paper is B = distinctness, C = repetition.

### Output boundary

If it is found that the count of a certain column does not exceed 2, the function first `return` without completely assigning values to the four output variables. A prompt will be printed only when called as a command; if the caller requests a return value, an unassigned error may be triggered.

## 3. `check_Theorem2.m`

It first branches by column count:

- All at least 3: prompt to check Theorem 1;
- A certain column does not exceed 1: it is judged that the general recognition fails;
- multiple columns exactly 2: only double-complete cases are checked;
- Single column is exactly 2: rearrange and read \(\boldsymbol v\), check (a), (b.1), (c).

Using `NaN` means "only partial conclusions are obtained or the theorem is not covered". This design requires the caller to explicitly distinguish `0` from `NaN`.

### Cover the border

When the single column is exactly 2 and \(\boldsymbol v=0\), the code checks A/B/C of \(Q^\star\) first; there is no separate check of the "double \(I_{K-1}\)" condition of Theorem 2(b.2) in this branch. Some theoretically determinable scenarios will be uncovered or the output will not be assigned a value.

## 4. `check_Theorem4.m`

Algorithm exhaustion:

\[
\binom{J}{K}
\]

first sub-matrices, and then enumerate for each

\[
\binom{J-K}{K}
\]

a second submatrix. After finding two panholistic matrices, check whether each column of the remaining questions is non-zero.

The worst number of combinations is approximately

\[
\binom{J}{K}\binom{J-K}{K},
\]

So the cost rises rapidly when the \(J,K\) is large. The code comments document that a \(18\times7\) submatrix search takes about 96 seconds.

## 5. `check_generic_complete.m`

The code enumerates the \(2^K-1\) non-empty subset of properties and performs the Hall condition. The mathematical logic is accurate, and the complexity increases exponentially with the number of attributes.

A more scalable implementation can treat Q as a bipartite graph and directly find the maximum matching.

## 6. Several biases in information output

- `check_Theorem3.m` actually uses `any(attr_count <= 2)`, but the prompt text says "less than 2";
- When passing, the actual requirement is at least 3 in each column, and the prompt text reads "at least 2";
- `check_Theorem4.m` prompts "Theorem 5 condition failed" when \(J<2K+1\), and the relevant sufficient conditions come from Theorem 4;
- Example 2 of `check_conditions_main.m` writes "scenario (a) and global pan-recognition", and the conclusion of Theorem 2(a) is that local pan-recognition fails;
- Example 5 writes "global universal recognition", Theorem 2(c) only gives local universal recognition.

These issues focus on the annotation and prompting layers. When using the official function, the original Boolean output should be saved and reinterpreted according to the paper's theorem.
