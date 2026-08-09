# Summary and follow-up questions

## What did this paper accomplish?

Kruskal (1977) developed a connected language for three-way arrays:

1. Use triad to define the rank of the three-way array;
2. Use slab-space and mode transformation to establish rank lower bound;
3. Use the triple product \([A,B,C]\) to uniformly represent the sum of rank one components;
4. Use Kruskal rank to describe the independence of "any column subset";
5. use

   \[
   k_A+k_B+k_C\ge2R+2
   \]

   Ensure that the \(R\) item decomposition is essentially unique;
6. Connect tensor rank to arithmetic complexity and uniqueness to three-way statistical models.

## The core logic chain

\[
\text{The set of three factor columns is general enough}
\]

\[
\Downarrow
\]

\[
\text{Retain the required independence after projection or slicing}
\]

\[
\Downarrow
\]

\[
\text{The columns decomposed into two groups can only correspond item by item.}
\]

\[
\Downarrow
\]

\[
\text{Common displacement + three-way destructive scaling}.
\]

In the probabilistic model, the column sum is fixed scaling to 1, and only the latent class label permutation remains.

## Five points to remember

1. Tensor rank, ordinary matrix rank and Kruskal rank are three different concepts.
2. \(k\)-rank requires that a subset of columns of any specified size be independent.
3. The Kruskal condition provides sufficient proof of certainty.
4. After the condition fails, uniqueness still needs to be judged by other theorems or explicit counterexamples.
5. The only thing that population decomposition does not automatically guarantee is that finite sample estimates are stable.

## Tasks not covered by the paper

Original text not provided:

- Numerical recovery error bound for noisy tensors;
- Efficient verification algorithm for large-scale \(k\)-rank;
- CP decomposition software;
- Data-driven selection of component \(R\);
- Recovery of Q matrix in CDM;
- Limited sample bias, variance or coverage rate experiments.

The scripts on this site only help to check small precise examples.

## How to advance the subsequent theory

Later research expanded in several directions:

- Shorter and more transparent proof of Kruskal's theorem;
- A weaker uniqueness condition than \(k_A+k_B+k_C\ge2R+2\);
- The uniqueness of \(N\) road tensor;
- Approximate uniqueness and stable recovery with noise;
- Computable algebraic decomposition algorithm;
- Pan-identifiability of latent classes, HMMs, phylogenies and CDMs.

Rhodes (2010) deals with proof readability; Allman et al. (2009) systematically transfer theorems to multi-observation variable latent structure models.

## Position in the CDM route of this site

\[
\text{Kruskal (1977)}
\longrightarrow
\text{Allman et al. (2009)}
\longrightarrow
\text{CDM special recognition theorem}.
\]

- Kruskal gives a three-way decomposition uniqueness tool;
- Allman gives the observation variable blocking and pan-full rank methods;
- The CDM paper adds Q matrix, attribute profile and specific reaction function constraints.

These three layers cannot replace each other, but can form a complete identity proof chain.

## Next article

According to the current production route, the next article will enter the CDM core model:

> de la Torre, J. (2009). DINA model and parameter estimation: A didactic.

[Enter de la Torre (2009) full feature](../de-la-torre-2009/index.md).

It will shift attention from "can the overall distribution be uniquely decomposed" to:

- DINA attributes and item parameters;
- Complete data and marginal likelihood;
- EM update;
- Simulation and example evidence;
- Estimated implementation.

Kruskal (1976) and Lauritzen (1996) in the category of mathematical tools will be completed in subsequent dependency nodes.
