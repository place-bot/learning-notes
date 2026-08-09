# Computable recurrence

## Code boundaries

The original paper does not have an official code repository, nor does it propose a parameter estimation algorithm. Kruskal uniqueness is a theoretical conclusion at the population distribution level, and additional numerical methods are required to recover tensor factors from empirical frequencies.

This site provides

```text
tools/allman_2009_identifiability_demo.py
```

Recurring as a concept. It's done using the Python standard library:

1. Search for the best three-block partition of Theorem 4;
2. Calculate the number of Bernoulli sufficient variables for Corollary 5;
3. Building block conditional probability matrix;
4. Restore the probability of a single question within a block through marginalization;
5. Enumerate the complete observation joint distribution;
6. Verify that common class permutation does not change the observed distribution.

It does not perform latent class estimation, nor does it infer parameters from samples.

## Run

Execute in the warehouse root directory:

```bash
python3 tools/allman_2009_identifiability_demo.py
```

Check the number of additional categories and dichotomous variables:

```bash
python3 tools/allman_2009_identifiability_demo.py \
  --classes 8 \
  --binary-items 7
```

## Theorem 4 conditional search

The script assigns the block label \(0,1,2\) to each variable, retaining allocations where all three blocks are non-empty. Calculate for each partition

\[
K_a=\prod_{j\in S_a}\kappa_j
\]

and

\[
\operatorname{score}
=
\sum_{a=1}^{3}\min(r,K_a).
\]

If

\[
\operatorname{score}\ge2r+2,
\]

This partition passes the dimension-level sufficient condition of Theorem 4.

Core functions:

```python
def tripartition_score(number_of_classes, arities, blocks):
    state_counts = tuple(
        product(arities[index] for index in block)
        for block in blocks
    )
    score = sum(
        min(number_of_classes, count)
        for count in state_counts
    )
    return score, state_counts
```

Here `arities[j]` is the single variable state number \(\kappa_j\).

## Block matrix corresponds to row tensor product

For a dichotomous question block, the script enumerates all \(0/1\) response patterns. Probability of correct answer given a category

\[
(\theta_1,\ldots,\theta_m),
\]

The probability of a certain reaction pattern \(\boldsymbol x\) is

\[
P(\boldsymbol X=\boldsymbol x\mid Z=i)
=
\prod_{j=1}^{m}
\theta_j^{x_j}(1-\theta_j)^{1-x_j}.
\]

Code:

```python
def block_probability_row(item_success_probabilities):
    probabilities = []
    for pattern in itertools.product(
        (0, 1),
        repeat=len(item_success_probabilities),
    ):
        probability = product(
            theta if response else 1.0 - theta
            for response, theta in zip(
                pattern,
                item_success_probabilities,
            )
        )
        probabilities.append(float(probability))
    return probabilities
```

Stacking the block response distributions for each latent class row by row gives us \(N_a\).

## Marginal recurrence Lemma 14

To recover the correct answer probability for question \(q\) in a block from a block row, just

\[
x_q=1
\]

Sum of reaction patterns:

```python
def recover_item_probability(
    block_row,
    block_size,
    item_position,
):
    patterns = itertools.product(
        (0, 1),
        repeat=block_size,
    )
    return sum(
        probability
        for pattern, probability in zip(
            patterns,
            block_row,
        )
        if pattern[item_position] == 1
    )
```

This corresponds to the proof

\[
\sum_{\boldsymbol x_{-q}}
N_a(i;\boldsymbol x)
=
M_q(i,x_q).
\]

## Label replacement check

script enumeration

\[
P(\boldsymbol X=\boldsymbol x)
=
\sum_i\pi_i
\prod_j
\theta_{ij}^{x_j}(1-\theta_{ij})^{1-x_j}.
\]

Then do the same permutation on the rows \(\pi\) and \(\Theta\), and calculate the full pattern probabilities again. The maximum difference between the two results should be of the order of floating point rounding:

```text
max difference after class permutation = 0.000e+00
```

This check shows how label permutations belong to the structural symmetry of the model.

## What can the numerical row rank check show?

The script computes the ordinary row rank of the example block matrix using Gaussian elimination. right

\[
r=4,\quad S_1=\{1,2\},\quad S_2=\{3,4\},\quad S_3=\{5\},
\]

The first two \(4\times4\) block matrices have full row rank under the example parameters, and the third \(4\times2\) matrix has normal rank 2.

For \(4\times4\) full row rank matrix,

\[
\operatorname{rank}_K=\operatorname{rank}=4.
\]

For the \(4\times2\) matrix, a normal rank of 2 does not automatically guarantee that any two rows are independent; each pair of rows also needs to be checked. The probabilities of correct answers to the single questions in the example are different from each other, so any two lines

\[
(1-\theta_i,\theta_i)
\]

Disproportional, Kruskal rank 2.

The script's ordinary rank result can only be used as a check for this numerical example and cannot replace the general Kruskal rank proof.

## Expected default output

The default example should report:

```text
Theorem 4 dimension check
  r = 4
  arities = [2, 2, 2, 2, 2]
  block state counts = (4, 4, 2)
  score = 10; threshold = 10
  sufficient dimension condition = True
  Bernoulli Corollary 5 bound = 5 items
```

The shapes and ranks of the three block matrices, marginalization recovery values, joint probabilities, and label replacement errors are then output.

## To actually do parameter recovery

Estimating parameters from finite sample frequency tables introduces new problems:

- The empirical tensor contains sampling error;
- CP decomposition may have local optima and scaling problems;
- Non-negative and random row constraints need to be handled explicitly;
- The condition number may be poor when approaching low-rank exception sets;
- The number of categories \(r\) needs to be selected;
- The estimated unnamed categories are also aligned to the CDM attribute profile.

These problems belong to tensor estimation, latent class estimation, and CDM structure learning. The identification theorem of Allman et al. provides the basis for uniqueness and does not give this set of calculation procedures.

