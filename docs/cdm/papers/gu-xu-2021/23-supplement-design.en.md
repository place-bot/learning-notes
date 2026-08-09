#Experiment: Supplementary material co-design

## 1. Seven groups of Study

| Study |model|purpose|
| --- | --- | --- |
| I | DINA |Verify adequacy of A/B/C|
| II | DINA |Verifying universal recognition when C is violated|
| III | DINA |Display local pan-recognition failure|
| IV | DINA |Construct equivalent distributions that violate integrity|
| V | G-DINA |Verify adequacy of D/E|
| VI | G-DINA |Demonstrates severe non-recognition likelihood performance|
| VII | G-DINA |Constructing an infinite number of substitution arguments that violates C|

## 2. \(5\times2\) candidate set

Studies I--III, V--VI use 121 candidate Qs from author file `Q_aa.mat`. Exclude \((0,0)\) for each row, and treat the entire matrix with two columns swapped as the same attribute label class.

For each true Q:

1. Generate data of participant named \(N=10^5\);
2. Fit models to candidate Q respectively;
3. Compare the log-likelihood after maximization;
4. Check if true Q reaches the maximum value.

In the picture:

- Blue triangle: Candidate Q;
- Red star: true Q of generated data;
- Purple square: candidate Q with the highest likelihood.

## 3. Parameter generation

### DINA

Official code set:

\[
\boldsymbol p\sim\operatorname{Dirichlet}(5,\ldots,5),
\]

\[
c_j\sim U(0.7,0.9),
\qquad
g_j\sim U(0.1,0.3).
\]

Run EM with 5 random initial values for each candidate Q.

### G-DINA

The code sets the latent class ratio to be uniform:

\[
p_{\boldsymbol\alpha}=2^{-K}.
\]

The baseline probability of each question randomly falls from about \(0.15\) to \(0.25\), and the full mastery probability is about \(0.75\) to \(0.85\). Each increment is generated according to the required attribute profile. Each candidate Q also uses 5 random initial values.

## 4. G-DINA filtering

The authors fit all candidates Q, but only show candidates whose estimated parameters satisfy stronger monotonic constraints:

\[
\theta_{j,\boldsymbol\alpha}>
\theta_{j,\boldsymbol\alpha'}
\quad
\text{When}\quad
\boldsymbol\alpha\odot\boldsymbol q_j
\succ
\boldsymbol\alpha'\odot\boldsymbol q_j.
\]

The official code uses a strong check that all non-zero G-DINA increments are positive:

```matlab
is_mono_str = all(delta(delta ~= 0) > 0);
```

It is more stringent than "the probability of ability classes is higher than that of all non-ability classes".

## 5. Evidence boundaries for exhaustive likelihood

The true Q in a single large sample obtains the maximum likelihood, which is consistent with the direction of recognition theory. It is still affected by the following factors:

- Limited sample randomness;
- EM local optimum;
- Whether the candidate set is complete;
- G-DINA candidate filtering;
- Number of datasets displayed per scenario.

So the graph constitutes a numerical explanation, and the identification theorem itself is established by an algebraic proof.

## 6. Studies IV and VII

These two groups do not depend on whether true Q is maximal:

- Study IV directly enumerates all \(2^{20}\) reaction modes and compares the probabilities;
- Study VII directly constructs 70 sets of surrogate parameters and compares the complete response distributions.

They provide a more direct check of machine accuracy for necessary counterexamples.
