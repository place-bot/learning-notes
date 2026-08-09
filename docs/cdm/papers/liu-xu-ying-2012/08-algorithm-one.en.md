#Algorithm 1: Line-by-line hill-climbing search

## Neighborhood

For the current matrix \(Q'\), define

\[
U_j(Q')
\]

is the \(J\times K\) binary matrix that is identical to \(Q'\) except for row \(j\). Line \(j\) has \(2^K\) patterns.

## Initialization

\[
Q^{(0)}=Q_0,
\]

\(Q_0\) usually comes from experts. The paper expects it to be close enough to the true Q.

## Three steps per round

Given \(Q^{(m-1)}\):

### Step 1: Find your best new line for each question

\[
Q_j
=
\arg\inf_{
Q'\in U_j(Q^{(m-1)})
}
\widehat S(Q').
\tag{19}
\]

This step enumerates \(2^K\) q-vectors for each question.

### Step 2: Choose the question with the largest drop among the J questions.

\[
j_*=\arg\inf_j\widehat S(Q_j).
\]

### Step 3: Only accept this line of updates

\[
Q^{(m)}=Q_{j_*}.
\]

If

\[
Q^{(m)}=Q^{(m-1)},
\]

The algorithm stops.

## Popular process

```text
Current Q
  ├─ Suppose only question 1 is changed: find the best whole line of question 1
  ├─ Suppose only question 2 is changed: find the best whole line of question 2
  ├─ ...
  └─ Suppose only question J is changed: Find the best whole line of question J
             ↓
      Select the global optimal from J local winners
             ↓
         Currently Q only changes this line
```

## Complexity per round

The number of candidate evaluations is approximately

\[
J\times2^K.
\]

Each review also includes:

- DINA EM with one fixed Q;
- Construct the selected T-matrix;
- Calculate \(\widehat S\).

Therefore \(J2^K\) is just the number of candidates, and the actual running time is also multiplied by the EM and moment calculation costs.

##Search properties

Each time a single row update is accepted that brings the target down, so the target path does not increase monotonically. The algorithm stops at a local minimum in a row-by-row neighborhood. It is not guaranteed to find the global minimum from any \(Q_0\).

## All zero lines

(19) and "at most \(2^K\) evaluations" literally contain an all-zero q-vector. The main simulation explicitly excludes all-zero rows when constructing \(Q_0\), but the text does not indicate whether subsequent searches also exclude it. In practice, you should usually decide whether to allow "no attributes required" questions based on the meaning of the content, and document this implementation choice.

## draw

The original text does not specify tie-breaking when multiple candidates have the same \(\widehat S\). Code reproduction needs to fix the candidate order or explicitly adopt the simplest rule so that the result can be repeated.
