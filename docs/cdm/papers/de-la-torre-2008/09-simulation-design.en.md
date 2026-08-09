# Simulation experiment design

## Research questions

The authors want to check whether, under ideal conditions, the sequential EM-based \(\delta\)-method can:

1. Keep the original correct q-vector;
2. Find a single error line;
3. Handle missing labels, multiple labels and substitutions;
4. Fix errors in three questions at the same time;
5. Select the correct Q through \(\varepsilon\) and updated item parameters.

## Fixed design

|Conditions|Original text value|
| --- | ---: |
|Number of students \(N\)| 5,000 |
|Number of items \(J\)| 30 |
|Number of attributes \(K\)| 5 |
|attribute profile|32 patterns with equal probability|
| guessing |All questions .20|
| slipping |All questions .20|
|DINA Convergence Criteria| .001 |
|initial estimate| empirical Bayesian EM |
|program| Ox |

## Q matrix

The 30 questions are evenly divided into single, double, and three attribute questions, and each attribute appears the same number of times in Q.

|question number|Q OK|question number|Q OK|question number|Q OK|
| ---: | :---: | ---: | :---: | ---: | :---: |
| 1 | 10000 | 11 | 11000 | 21 | 11100 |
| 2 | 01000 | 12 | 10100 | 22 | 11010 |
| 3 | 00100 | 13 | 10010 | 23 | 11001 |
| 4 | 00010 | 14 | 10001 | 24 | 10110 |
| 5 | 00001 | 15 | 01100 | 25 | 10101 |
| 6 | 10000 | 16 | 01010 | 26 | 10011 |
| 7 | 01000 | 17 | 01001 | 27 | 01110 |
| 8 | 00100 | 18 | 00110 | 28 | 01101 |
| 9 | 00010 | 19 | 00101 | 29 | 01011 |
| 10 | 00001 | 20 | 00011 | 30 | 00111 |

## 12 analysis conditions

Condition 0 uses the correct Q. Conditions 1--10 Only change one line of question 1, 11 or 21 at a time, covering single, double and triple attribute questions. Condition 11 Change three lines at the same time.

|Conditions|question number|Original Q|Q for analysis|Join|Delete|Total number of cells changed|
| ---: | ---: | :---: | :---: | ---: | ---: | ---: |
| 0 | -- | -- |Correct Q| 0 | 0 | 0 |
| 1 | 1 | 10000 | 01000 | 1 | 1 | 2 |
| 2 | 1 | 10000 | 11000 | 1 | 0 | 1 |
| 3 | 11 | 11000 | 01100 | 1 | 1 | 2 |
| 4 | 11 | 11000 | 01000 | 0 | 1 | 1 |
| 5 | 11 | 11000 | 11100 | 1 | 0 | 1 |
| 6 | 21 | 11100 | 01100 | 0 | 1 | 1 |
| 7 | 21 | 11100 | 00100 | 0 | 2 | 2 |
| 8 | 21 | 11100 | 01110 | 1 | 1 | 2 |
| 9 | 21 | 11100 | 00110 | 1 | 2 | 3 |
| 10 | 21 | 11100 | 00111 | 2 | 2 | 4 |
| 11 | 1 | 10000 | 11000 | 1 | 0 | 1 |
| 11 | 11 | 11000 | 10100 | 1 | 1 | 2 |
| 11 | 21 | 11100 | 01110 | 1 | 1 | 2 |

The "Number of Alterations" column of the original table of Condition 9 is ranked as 2, but according to the three listed flips, it should be 3; this site counts the actual flips in the "Total Number of Alterations". The summary column record of the original text is added 1, deleted 2, net change \(-1\).

## Thresholds and Updates

The author uses:

\[
\varepsilon\in\{.00,.01,.05,.10,.20\}.
\]

After each threshold generates candidate Q, run another 5 EM cycles and compare:

- Change the number of q-vector;
- Recommended q-vector of the changed item;
- Full Quiz \(\bar g+\bar s\).

## Design strengths

- Q structure is completely balanced;
- Single, double, and three attribute questions have special error conditions;
- Error types cover addition, deletion and replacement;
- Condition 11 checks for common contamination of the posterior by multiple errors;
- Thresholds range from very loose to very strict.

## Design Limitations

The original article does not form a full factorial experiment on sample size, test length, attribute correlation, parameter quality and Q error ratio; it reports a feasibility check under the conditions of a large sample, high discrimination, and uniform attribute profile.

