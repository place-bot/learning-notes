# This site can calculate recurrence

## Run all checks

```bash
python3 tools/liu_xu_ying_2012_q_learning.py \
  --mode all \
  --examinees 1200
```

## T-matrix accurate verification

```bash
python3 tools/liu_xu_ying_2012_q_learning.py --mode toy
```

Key output:

```text
T(Q), Equation (9):
[[0 1 0 1]
 [0 0 1 1]
 [0 0 0 1]]

T(Q'), Equation (10):
[[0 1 0 1]
 [0 0 1 1]
 [0 1 0 1]]

T(Q) with item-pair row, Equation (13):
[[0 1 0 1]
 [0 0 1 1]
 [0 0 0 1]
 [0 0 0 1]]
```

The script uses `numpy.testing.assert_array_equal` to check three matrices. If any element does not match, it will fail and exit.

## Formal table value verification

```bash
python3 tools/liu_xu_ying_2012_q_learning.py --mode tables
```

The output lists Tables 1--3 and prompts:

```text
editorial discrepancy: Table 1 reports Q1/N=500 as 94; prose reports 98
```

## Small Q recovery

```bash
python3 tools/liu_xu_ying_2012_q_learning.py \
  --mode simulate \
  --examinees 1200 \
  --seed 20260725
```

With a fixed seed, the demo starts with a line of error:

```text
iteration=1 item=6 S=0.130560->0.029598 drop=77.33% accepted=True
iteration=2 item=- S=0.029598->0.029598 drop=0.00% accepted=False
exact recovery: True
```

Numeric path display:

1. Rerun EM for each candidate;
2. In the first round, question 6 was changed from `10` back to `11`;
3. \(S\) dropped significantly;
4. There is no better single row neighbor in the next round, and the algorithm stops.

## Change sample size

```bash
python3 tools/liu_xu_ying_2012_q_learning.py \
  --mode simulate \
  --examinees 500 \
  --seed 7
```

Different seeds or smaller N may stop at other Q, which is exactly the observable version of the finite sample and local search problem.

## Accurately reproduce boundaries

This site does not claim to regenerate the original 100 frequencies of Tables 1--4 for the following reasons:

- The original seed is missing;
- EM initial value, tolerance and local solution handling missing;
- There is an ambiguity in the description of order 4 and \(K+1\) order T;
- The selection method for question groups at the same level is not listed;
- The all-zero q-vector and tie rules are not explained;
- Early stopping implementation details are not fully given.

The value of the script is to turn each mathematical object of the paper into a function that can be tested independently, and to provide a computing base for subsequent theoretical papers.
