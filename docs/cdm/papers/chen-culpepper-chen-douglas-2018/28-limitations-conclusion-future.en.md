# Limitations, conclusions and future work

## Paper conclusion

This article writes the exploratory estimation of DINA Q as a restricted Bayes problem:

\[
p(Q\mid-)
\propto
p(\boldsymbol Y\mid Q,-)I(Q\in\mathcal Q).
\]

Key results include:

- Irreducibility and symmetry of DS2 in legal Q-space;
- Restricted MH with adjustable block size;
- Element-wise restricted Gibbs;
- Higher recovery accuracy of Q and item parameters in simulation;
- Low-dimensional exploratory Q on fractional subtraction data.

## Limitations of paper validation

### Calculation extension

The state space is still huge, and the student attribute updates contain \(2^K\) categories. The author divides the complexity into

\[
N,\quad J,\quad K
\]

The law of growth is listed as an open problem, with special emphasis on \(K\).

### Q Posterior summary

The whole matrix mode may require very long chains to be stable in large spaces. Element-wise mode is worth investigating, but structural constraints and column alignment also need to be considered.

### Model scope

Text Focus DINA. The authors note that the DINA/DINO duality allows for straightforward transformations and suggest that in the future the search for corresponding identifiable limits for more general CDMs should be made.

### Integration of expert knowledge

The authors support comparing statistical Q with expert Q to seek a compromise between fit and interpretability. If the Q of some items are known, you can fix these rows and only calibrate the remaining items, which is especially suitable for adding new questions to the item bank.

## Limitations of this site’s supplements

### Strong recognition conditions may have wrong support sets

If true Q is not at \(\mathcal Q\), the restricted posterior can never recover it. Subsequent weaker conditions are worth combining with partially known Q methods.

### The number of attributes is given externally

The original article fitted \(K=3,4\) respectively, and \(K\) was not selected in the algorithm of the paper. Many \(K\) comparisons of current software are extensions that still require validation criteria, chain length, and interpretation stability.

### Incomplete simulation reproduction materials

The accompanying material lacks the real \(s,g\), complete simulation script, and random seeds, and Table 1 cannot be completely rerun data set by data set.

### Fixed chain length and posterior concentration

CGibbs reduces the recovery rate under several large sample conditions, suggesting that MCMC error needs to be separated from statistical error. Subsequent experiments should determine chain length based on ESS or mode stability.

### Q summary of current software

An element-wise 0.5 threshold may produce unrecognizable Q. The software should retain the entire matrix mode frequency or add restricted projections.

## Suggested follow-up research

### 1. Restricted posterior summary

Solve

\[
\widehat Q
=
\arg\min_{Q\in\mathcal Q}
\sum_{j,k}
w_{jk}|q_{jk}-\overline q_{jk}|,
\]

Project element-wise posterior information into legal space.

### 2. Multi-scale transfer kernel

Mix:

- Single element restricted Gibbs;
- DS2 block movement;
- Column exchange;
- Whole row q-vector update;
- tempering or parallel chaining.

This helps span distant Q patterns.

### 3. Scalable posterior approximation

Stochastic gradients, variational inference, continuous relaxation, and combinatorial optimization can be studied. The follow-up Oka and Okada (2023) is developing along this line.

### 4. Joint inference of attribute number and Q

Use model comparison, reversible jumps, sparse latent classes, or nonparametric priors on \(K\) while handling column labels and identifiable designs.

### 5. Expert-data collaborative prior

Assign stronger priors to elements confirmed by experts, and retain greater uncertainty for controversial elements:

\[
q_{jk}\sim\operatorname{Bernoulli}(\omega_{jk}),
\]

Then truncate the joint prior to the identifiable space. This quantifies the extent to which expert structures are revised by the data.

### 6. Interface with CAT

This article estimates the item-attribute structure, which can provide a calibrated item bank for cognitive diagnostic CAT. It does not study real-time topic selection strategies. If used for CAT, additional construction is required:

- Posterior update of student’s current attributes;
- Effect of next question;
- Content and exposure constraints;
- Online re-planning after each answer.

## Final review

The key value of this article is to advance identifiability from post-hoc inspection to sampling state space. The simulation advantages of restricted Gibbs illustrate that structural theory can directly improve computational estimates; strong conditions, computational extensions, and posterior summaries constitute the main space for subsequent work.

[Next page: References, code and data sources](references.md)
