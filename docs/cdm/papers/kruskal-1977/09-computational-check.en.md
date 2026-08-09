# Computable check

## Code boundaries

Kruskal (1977) has no official code. This site provides

```text
tools/kruskal_1977_demo.py
```

Used to reproduce the finite-dimensional algebra checks in this topic:

1. Use Gaussian elimination of rational numbers to calculate the rank of ordinary matrices;
2. Enumerate column subsets and accurately calculate Kruskal rank of small matrices;
3. Construct a triple product;
4. Verify that common permutation and destructive scaling keep the tensor unchanged;
5. Verify non-unique decomposition when the third factor column is repeated.

The script does not implement the general CP decomposition algorithm, nor does it estimate factors from noisy data.

## Run

Execute in the warehouse root directory:

```bash
python3 tools/kruskal_1977_demo.py
```

Expected key outputs include:

```text
Full-rank R=3 example
  ordinary ranks = (3, 3, 3)
  Kruskal ranks = (3, 3, 3)
  condition: 9 >= 8 -> True
  tensor rank certified as R = 3
  max difference after permutation/scaling = 0
```

and:

```text
Non-unique matrix-like example
  Kruskal ranks = (2, 2, 1)
  condition: 5 >= 6 -> False
  equal tensors from a non-monomial Q = True
```

## Ordinary rank function

The script uses `fractions.Fraction` to save rational numbers and obtains the exact rank through Gaussian elimination:

```python
def matrix_rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    ...
```

The zero difference in such examples comes from exact arithmetic and does not rely on floating point tolerance.

## Kruskal rank enumeration

For each \(q\), enumerate all \(q\) column combinations:

```python
def kruskal_rank(matrix):
    column_count = len(matrix[0])
    result = 0
    for size in range(1, column_count + 1):
        if all(
            matrix_rank(select_columns(matrix, indices)) == size
            for indices in itertools.combinations(
                range(column_count),
                size,
            )
        ):
            result = size
        else:
            break
    return result
```

If a certain scale \(q\) already has related column sets, a larger scale cannot satisfy "any subset independence", so it can be stopped.

## Triple product

Directly implemented in code

\[
x_{ijk}
=
\sum_{r=1}^{R}
a_{ir}b_{jr}c_{kr}.
\]

```python
def triple_product(a, b, c):
    return [
        [
            [
                sum(
                    a[i][r] * b[j][r] * c[k][r]
                    for r in range(component_count)
                )
                for k in range(len(c))
            ]
            for j in range(len(b))
        ]
        for i in range(len(a))
    ]
```

## Displacement and scaling checks

The script rearranges the columns of the three matrices according to the same `permutation`, and then multiplies them respectively.

```text
(2, 1/2, 1)
(3, 1, 1/3)
(1/6, 2, 3)
```

The product of the three terms is 1 at every location. All tensor elements are then recalculated and compared.

This inspection display

\[
[AP\Lambda,BPM,CPN]=[A,B,C].
\]

It verifies intrinsic equivalence and does not "discover" a unique decomposition through numerical search.

## Code mapping for non-unique examples

The second example uses

\[
A=B=I_2,\qquad C=(1,1)
\]

and a non-diagonal, non-permutation invertible matrix \(Q\). Script construction

\[
\bar A=AQ,\qquad
\bar B=BQ^{-\mathsf T},
\qquad
\bar C=C.
\]

Since the two third-dimensional vectors are exactly the same, the three-way problem degenerates into matrix factorization, and any \(Q\) will produce the same tensor.

## Where can the code result be supported?

|Check|Can confirm|Unable to confirm|
| --- | --- | --- |
|Enum \(k\)-rank|Exact \(k\)-rank given a small matrix|Efficient general algorithms on large matrices|
|Check for inequalities|Is Kruskal's sufficient condition true?|Uniqueness after condition failure|
|Construct equivalent factors|Displacement/scaling does preserve tensors|Stable recovery factors from unknown tensors|
|explicit counterexample|There are additional solutions for a specific decomposition|All low \(k\)-rank cases have multiple solutions|

If the research goal is finite sample CDM estimation, nonnegative tensor decomposition, latent class likelihood or Bayesian estimation, and analysis of sampling errors are also required.
