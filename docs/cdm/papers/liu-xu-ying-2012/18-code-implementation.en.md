# Disclosure of code status and implementation intensive reading

## Original implementation status

Official article description:

- MLE can be calculated by EM;
- Q search uses Algorithm 1;
- Simulations were performed with 100 repetitions.

The main text, PMC open version and author paper page are not given:

- Source code warehouse;
- Programming language;
- Software version;
- EM initial value and tolerance;
- Complete list of T lines;
- Random seed;
- Tie handling.

A line-by-line audit of the original implementation is therefore not possible.

## Current common software relationships

R packages such as `CDM` and `GDINA` can fit DINA/G-DINA for a given Q and also provide several Q verification tools. Their public main interface does not expose the "low-order T moment + Equation (17) + Algorithm 1" of this article as a recurrence of the same name. After completing EM with these packages, you still need to construct T, \(\boldsymbol\beta\) and discrete search yourself.

## This site is independently implemented

[`tools/liu_xu_ying_2012_q_learning.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/liu_xu_ying_2012_q_learning.py) provides a transparent teaching chain.

|Python object|Thesis object|
| --- | --- |
| `attribute_profiles()` |\(2^K\) \(\boldsymbol\alpha\)|
| `ideal_response()` |\(\xi^j\) of Equation (1)|
| `response_probabilities()` |\(g+(c-g)\xi\) of Equation (2)|
| `item_subsets()` |The set of question groups and rows of T|
| `t_matrix()` |B-vector stack|
| `empirical_beta()` |Sample joint answer rate|
| `s_objective()` |Formula (14)|
| `fit_dina_em()` |nuisance MLE with fixed Q|
| `profiled_objective()` |Formula (17)|
| `hill_climb_q()` | Algorithm 1 |
| `simulate_dina()` |simulated reaction|

## The core of `t_matrix()`

```python
item_prob = response_probabilities(q, c, g, profiles)
return np.vstack([
    np.prod(item_prob[list(s), :], axis=0)
    for s in subsets
])
```

Each question group takes the column-by-column product of the corresponding single question probability rows, which directly corresponds to the B-vector definition.

## The core of `empirical_beta()`

```python
np.mean(np.prod(y[:, list(s)], axis=1))
```

For each student, first multiply the question group responses and then average across the students.

## Numerical processing of EM

Implementation uses:

- log-sum-exp posterior;
- Probabilistic truncation avoidance \(\log0\);
- consistent initialization;
- Marginal log-likelihood difference as convergence criterion.

These are project choices for this site and are not given values in the original text.

## Search boundaries

The library supports the inclusion of all-zero rows to match the \(2^K\) neighborhood definition. The demo run uses `include_zero=False` because each of the six tutorial questions should require at least one attribute. The difference is clearly documented in the command output and documentation.

## Recurrence level

- Formulas (9), (10), (13): deterministic and accurate verification;
- Tables 1--3: Enter formal table values and do range checks;
- Small simulation: independent teaching reproduction;
- Original 100 times table: missing original code and some settings, no claim to reproduce it frame by frame.
