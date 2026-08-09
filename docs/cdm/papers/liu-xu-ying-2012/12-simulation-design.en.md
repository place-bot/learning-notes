# Simulation experiment co-design and three Qs

## Common settings

|factors|settings|
| --- | --- |
|Generate model| DINA |
|Number of questions| \(J=20\) |
|Number of attributes| \(K=3,4,5\) |
|Attribute distribution|Main experiment uniformity: \(p_{\boldsymbol\alpha}=2^{-K}\)|
|item parameters|All questions \(s_j=g_j=.2\), that is, \(c_j=.8\)|
|sample size| \(N=500,1000,2000,4000\) |
|Repeat|100 data per condition|
| T-matrix |Write up to 4 question combinations in the text|
|Starting error|Randomly select 3 questions from the 20 questions and correct the entire row.|
|Search| Algorithm 1 |
|result indicator|Is the complete Q equal to generating Q, cell by cell?|

## Construction of starting Q

Randomly draw 3 rows from the true Q. Each line starts from

\[
2^K-2
\]

Extract replacement values uniformly from vectors:

- exclude true q-vector;
- Exclude all-zero vectors.

So \(Q_0\) has exactly 3 questions with entire rows of errors. Each row may contain 1 to \(K\) incorrect entries.

## \(Q_1:20\times3\)

According to the original formula (20):

```text
100 010 001 100 010 001 100 010 001
110 101 101 011 101 011 110 011 101 011 111
```

It contains repeated unit vectors, as well as two- and three-attribute questions.

## \(Q_2:20\times4\)

```text
1000 0100 0010 0001
1000 0100 0010 0001
1100 1010 1001 0110 0101 0011
1110 1101 1011 0111 1111 1111
```

## \(Q_3:20\times5\)

```text
10000 01000 00100 00010 00001
10000 01000 00100 00010 00001
11000 10100 10010 10001 01100
01010 01001 00110 00101 00011
```

\(Q_3\) only has single-attribute and dual-attribute questions, but no higher-order combinations.

## The reason why difficulty increases with K

The number of attribute classes is

\[
2^K:
\quad
8,\ 16,\ 32.
\]

Similarly, at \(N=500\), the average number of people in each category dropped from 62.5 to 31.25 and then to 15.625. With more parameters and sparser categories, the sampling error of the joint moments is larger.

## Design the scope of answers

This experiment examines the recovery of true Q from a local starting point of "only 3 wrong rows". It does not manipulate:

- Random starting points or widespread errors;
- \(K\) Unknown;
- The model is incorrectly set;
- Heterogeneity of item parameters;
- Missing answers;
- Real content constraints.
