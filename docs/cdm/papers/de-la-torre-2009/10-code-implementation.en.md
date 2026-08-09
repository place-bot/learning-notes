# Code implementation intensive reading

## Original code status

The paper states:

- DINA EM is implemented in Ox;
- The console version of Ox was free for academic research and teaching at the time;
- EM code is available from the author upon request;
- HO-DINA MCMC from de la Torre and Douglas (2004).

The paper does not give:

- code list;
- Download link;
- Version control warehouse;
- Software license;
- Run parameter file;
- Fraction subtraction data file.

Therefore, it is currently impossible to audit the original Ox source code line by line.

## Teaching implementation on this site

The warehouse provides:

```text
tools/de_la_torre_2009_dina_em.py
```

It only uses the Python standard library to implement:

1. 30×5 Q matrix of Table 1;
2. Equal probability attribute profile simulation;
3. The ideal response of Equation 1;
4. Marginal likelihood of Equation 5;
5. EM update of Equations A10--A11;
6. Standard error of observation information of Equation A15;
7. Summarize the parameter recovery by the required number of attributes.

## Run quickly

Default to smaller setting:

```bash
python3 tools/de_la_torre_2009_dina_em.py
```

The default parameters are:

```text
500 students
30 items
5 attributes
3 replications
g = s = 0.20
```

## Align paper design

```bash
python3 tools/de_la_torre_2009_dina_em.py \
  --examinees 2000 \
  --replications 100 \
  --seed 2009
```

This is a pure Python instructional implementation, and the runtime is not directly comparable to the paper's Ox/3.0 GHz numbers.

## Reproduce fixed prior

Script default:

\[
\pi_l=\frac{1}{32}
\]

And remain unchanged during the EM process, aligning the equal probability mode and basic appendix algorithm of the paper simulation.

The paper discusses empirical Bayesian extensions available through:

```bash
python3 tools/de_la_torre_2009_dina_em.py \
  --update-prior
```

Enable. The output will clearly show `fixed uniform prior = False`.

## Mapping from formula to function

|Thesis object|code|
| --- | --- |
| \(\eta_{lj}\) | `ideal_response()` |
|All \(2^K\) modes| `all_attribute_patterns()` |
| \(w_{il}=P(\alpha_l\mid X_i)\) | `e_step()` |
| \(I_j^{(z)},R_j^{(z)}\) |Expected count within `m_step()`|
| \(\hat g_j=R_j^{(0)}/I_j^{(0)}\) | `m_step()` |
| \(\hat s_j=(I_j^{(1)}-R_j^{(1)})/I_j^{(1)}\) | `m_step()` |
|A15 information matrix| `appendix_standard_errors()` |
|EM external circulation| `fit_dina_em()` |

## Numerical stability of E-step

The code first calculates the logarithmic weight of each mode:

```python
log_weight = log(prior)
log_weight += log(P) if x else log(1 - P)
```

Then subtract the maximum logarithmic weight and index again. It implements log-sum-exp and avoids 30 consecutive probability underflows.

## Implementation of A15

Generate an expected score vector of length \(2J\) for each student:

```python
score[2 * j] = posterior_eta_zero * (x - g) / (g * (1 - g))
score[2 * j + 1] = (
    posterior_eta_one
    * ((1 - s) - x)
    / ((1 - s) * s)
)
```

The information matrix is:

```python
information += score @ score.T
```

The script uses Gaussian-Jordan elimination to find the inversion and take the square root of the diagonal.

## Single paper size check

run

```bash
python3 tools/de_la_torre_2009_dina_em.py \
  --examinees 2000 \
  --replications 1
```

You should see the same standard error structure as Table 2:

```text
required  mean(SE_g)  mean(SE_s)
       1       ~.016       ~.015
       2       ~.011       ~.021
       3       ~.010       ~.030
```

The random seed will affect the single point estimate, and 100 times of aggregation will be at the same level of evidence as Table 2 of the paper.

## Implement boundaries

The script doesn't have:

- Fit HO-DINA or MCMC;
- Read raw score subtraction data;
- Search or verify Q matrix;
- mandatory \(1-s_j>g_j\);
- Handle missing responses;
- Provide production-level optimization;
- Replicate unknown original Ox internals.

Its purpose is to turn appendix formulas into checkable execution paths.
