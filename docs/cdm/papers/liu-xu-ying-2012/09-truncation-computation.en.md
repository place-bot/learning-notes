# T-matrix truncation and calculation amount

## Saturated T-matrix

If all non-empty item combinations are included, the number of rows is

\[
\sum_{\ell=1}^J\binom J\ell=2^J-1.
\]

At this time, \(\boldsymbol\beta\) retains the complete information of the bipartite reaction distribution.

## Why is it difficult to use?

The original article points out that the saturation matrix requires

\[
N\gg 2^J
\]

Only then can each cell of the \(J\)-dimensional contingency table have enough observations. The saturated T at \(J=20\) has 1,048,575 rows and is expensive to construct, store, and repeatedly recompute.

## Practical Advice for Papers

Join in order from low to high:

1. All single question lines;
2. The question is correct;
3. Combination of three questions;
4. Continue increasing until the number of rows is approximately \(N/10\).

Low-order moment samples are more stable, and high-order moments bring finer structural constraints.

## Actual description of simulation section

The simulation design clearly states "combinations containing up to 4 questions." The same paragraph then generalizes that incorporating at least the \(K+1\) order performs well empirically.

These two sentences for \(K=4,5\) cannot be implemented verbatim as "all combinations" at the same time: \(K+1\) is level 5 and level 6 respectively, while the previous sentence reads level 4. The paper does not further list the final set of rows used for each condition. This lack should be treated as an implementation uncertainty when reproducing the original table.

## Three reproducible strategies

|strategy|rules|Features|
| --- | --- | --- |
|fixed highest order|Include all combinations from 1 to \(r\)|Well defined, the number of rows may explode|
|fixed line budget|Start from low level and stop at \(L=N/10\)|Close to practical suggestions, the order of selection is defined within the same level.|
|Random sampling question group|Low-order retention, high-order sampling|Scalable, requires random seed|

The `item_subsets()` script of this site supports both `max_order` and `max_rows`, and lexicographic truncation is used within the same order.

## Large item bank block

Suggestions in the discussion section: If there are 100 questions, they can be divided into about 20 smaller question groups, estimate the sub-Q respectively, and then merge them. Question groups may overlap appropriately to connect the blocks.

This suggestion reduces the amount of calculation and also brings two new problems:

- Attribute column labels of different blocks need to be aligned;
- Cross-block item dependency moments do not enter the target.

The paper lists fast algorithms as a future research direction and does not give a formal error theory for block merging.
