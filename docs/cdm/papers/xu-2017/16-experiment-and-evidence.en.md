# Original evidence and Experiment boundaries

## The original text has no empirical experiments

This is a theoretical paper. The full text structure is:

1. Model and application background;
2. identifiability definition and \(T\)-matrix;
3. C1, C2 and the main theorem;
4. Proof of main theorem, proposition and lemma.

The original text does not contain:

- Simulation data set;
- Real education data;
- sample size condition table;
-Number of repetitions;
- Parameter recovery error;
- Empirical comparison with other methods;
- running time;
- Ablation experiments.

Therefore, it is impossible to report "which data set was used, how to divide it, and how many indicators were used." Writing the original proof as an experimental result will confuse the types of evidence.

## Theoretical experimental design of the original article

The paper actually compares three design levels:

|design|identifiable conclusion|original text evidence|
| --- | --- | --- |
|Q is incomplete|There are already attribute classes in Ideal DINA that are indistinguishable|Same ideal response column|
|Only C1|In general, identification cannot be guaranteed|Explicitly Equivalent Parameter Family of Proposition 2|
| C1 + C2 |\((\Theta,\boldsymbol p)\) strictly identifiable|Theorem 1 and five-step proof|

This is equivalent to a structural level comparison:

\[
\text{Missing anchor point}
\;\to\;
\text{Two sets of anchor points}
\;\to\;
\text{Two sets of anchor points + extra distinction}.
\]

## The purpose of this site’s calculation verification

The script on this website does four limited checks against the original algebra:

1. Automatically determine complete, C1 and C2 that can be guaranteed by Q under DINA;
2. Find the margin from the complete reaction mode distribution and compare it with
   \(T(Q,\Theta)\boldsymbol p\) compare;
3. Accurately verify the transformation equation of Proposition 3;
4. Verify the collision of two sets of parameters when C1 is established but C2 fails.

The verification object of Proposition 3 is

\[
T(Q,\Theta-\boldsymbol\theta^*\boldsymbol1^\top)
=
D(\boldsymbol\theta^*)T(Q,\Theta).
\]

## Default result of K = 2

run

```bash
python3 tools/xu_2017_rlcm_identifiability.py
```

Get:

|Check|result|
| --- | --- |
|Two \(I_2\)| complete=True，C1=True，DINA structural C2=False |
|Three \(I_2\)| complete=True，C1=True，DINA structural C2=True |
|\(T\)-matrix size| \(64\times4\) |
|\(T\)-matrix exact rank| 4 |
|\(T\boldsymbol p\) and response distribution margin|exactly equal|
|Proposition 3 Both sides|exactly equal|
|\(D\) diagonal element|all 1|
|Maximum distribution difference of counterexamples between two questions| 0 |

Counterexample

\[
P(R_1=1,R_2=1)
=
\frac{57}{125}
=
0.456.
\]

Two sets of different parameters accurately obtain this value and the remaining three grid probabilities.

## Extended check for K = 3

run

```bash
python3 tools/xu_2017_rlcm_identifiability.py --attributes 3
```

Get:

|Check|result|
| --- | --- |
|\(T\)-matrix size| \(512\times8\) |
|exact rank| 8 |
|marginal equation|exactly equal|
|Proposition 3|exactly equal|

All calculations were performed using Python `Fraction`, and the 0 differences reported are exact rational equivalents.

## These calculations cannot replace anything

\(T\) - The matrix has full column rank at a given \(\Theta\), which only means that it can be identified from the margin when \(\Theta\) is known
\(\boldsymbol p\). The main theorem also requires that when \(\Theta\) is unknown, another set of
It is possible for \(\bar\Theta\) to simultaneously compensate \(\bar{\boldsymbol p}\).

Therefore:

- A single rank check does not prove the complete main theorem;
- Limited enumeration does not cover any \(K,J\);
- Calculate results to check formulas, dimensions and counterexamples;
- The general conclusion still comes from the symbolic proof of the original text.

## To make a real simulation

Reasonable subsequent simulations can manipulate:

- C2 comparison
  \(\min_j|\theta_{j,\boldsymbol e_k}-\theta_{j,\boldsymbol0}|\)；
- Minimum value of class proportion;
- \(N\)；
- Two, three or non-pure question block design;
- Q is wrongly set;
- EM initial value.

Indicators can include parameter RMSE, attribute classification error, information matrix condition number, multi-start solution difference, and coverage rate. Such results belong to follow-up research and cannot be classified as the original experiment of Xu (2017).
