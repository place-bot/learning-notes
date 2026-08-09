# Overview of three types of candidate generators

## Why candidate generation is difficult

If the elements of Q are randomly flipped directly, it will be easily destroyed:

- At least two copies of the unit line;
- At least three 1's per column;
- At least one 1 per line.

If candidates are selected from all \(2^{JK}\) matrices each time, the vast majority of candidates will be far away from the current high posterior region, and the MH acceptance rate will be very low.

## Three proposals

|propose|Update scope|Relationship to current Q|Original article preliminary acceptance rate|
| --- | --- | --- | ---: |
| Independence |Reconstruct the entire Q|independent|Less than 0.5%|
| DS1 |Rebuild the entire selected column|Depend on|less than 5%|
| DS2 |Reconstruct \(B\) positions in a column|Dependent, adjustable step size| 18%--25% |

## Independent proposal

Construct first

\[
\begin{bmatrix}
I_K\\
I_K\\
\widetilde Q
\end{bmatrix}
\]

And ensure that each column of \(\widetilde Q\) is non-zero and each row is non-zero, and then randomly scramble the item rows. Each candidate is legal and can cover the entire \(\mathcal Q\).

## DS1

Randomly select a column \(k\), fix the elements required to maintain identifiability, and then select a legal configuration for the remaining positions in the column. It retains the other \(K-1\) columns and is therefore more local than independent proposals.

## DS2

Randomly select a column \(k\), and then select \(B\) item positions from this column. Only update this column block

\[
Q_{k,B}.
\]

It controls the stride via \(B\):

- \(B=1\): single element update;
- \(B=K\): medium block;
- \(B=2K\): MH settings used in the simulation and application of the paper;
- \(B=J\): degenerated into column-type update.

## Design requirements

A valid MH proposal must at least ensure:

1. The proposed \(Q^\star\) is always \(\mathcal Q\);
2. The chain can reach any other legal state from any legal state;
3. Proposal probability ratios can be calculated.

The paper proves irreducibility and symmetry for DS2. The symmetry leaves the proposal ratio equal to 1 and the acceptance rate only to the target posterior ratio.

##Why do we keep two algorithms in the end?

- MH + DS2: moving multiple elements at once, possibly across local stickiness of element-by-element updates;
- Restricted Gibbs: MH mechanism without rejection of whole steps, using exact conditional probabilities element-wise, best performance in simulations.

Both target the same identifiable posterior, the difference comes from the transfer kernel.

[Next page: Independent Proposal vs. DS1](11-independence-and-ds1.md)
