# EM posterior expectation count

## Why is direct revaluation expensive?

The most direct solution is:

1. Change to a new line q-vector;
2. Refit DINA on the entire set of data;
3. Get new \(g_j,s_j,\delta_j\);
4. Repeat for the next candidate.

Even with sequential search, a complete revaluation of every candidate for every question would still require a large number of EM fits at worst. The key computational simplification of this paper comes from the posterior weights of the E-step.

## One DINA fitting

Under the current Q matrix, E-step calculation

\[
\widehat p_{il}
=
\widehat P(\boldsymbol\alpha_l\mid\boldsymbol X_i),
\]

Among them \(l=0,\ldots,2^K-1\).

For item \(j\) and attribute profile \(l\), define:

\[
N_{jl}
=
\sum_{i=1}^{N}\widehat p_{il},
\]

\[
R_{jl}
=
\sum_{i=1}^{N}X_{ij}\widehat p_{il}.
\]

\(N_{jl}\) is the posterior expected number of people in this mode, and \(R_{jl}\) is the posterior expected number of correct answers. The original text uses \(N_j^{(\eta)}\) and \(R_j^{(\eta)}\) to represent the counts after aggregation into the ideal response group.

## Candidate q-vector only changes the aggregation method

Given candidate \(\boldsymbol q_{jl'}\), compute for each pattern

\[
\eta_{ll'}=\prod_{k=1}^{K}\alpha_{lk}^{q_{jl'k}}.
\]

Then aggregate the schema-level expectation counts as:

\[
N_{jl'}^{(h)}
=
\sum_{l:\eta_{ll'}=h}N_{jl},
\qquad h\in\{0,1\},
\]

\[
R_{jl'}^{(h)}
=
\sum_{l:\eta_{ll'}=h}R_{jl}.
\]

Candidate parameters can be calculated directly:

\[
\widehat g_{jl'}
=
\frac{R_{jl'}^{(0)}}{N_{jl'}^{(0)}},
\]

\[
\widehat s_{jl'}
=
\frac{N_{jl'}^{(1)}-R_{jl'}^{(1)}}{N_{jl'}^{(1)}},
\]

\[
\widehat\delta_{jl'}
=
1-\widehat s_{jl'}-\widehat g_{jl'}.
\]

The entire candidate comparison process simply adds up the already existing expected counts.

## A small example of four modes

Assume \(K=2\), the posterior expectation count of a certain question is:

|mode| \(N_{jl}\) | \(R_{jl}\) |
| :---: | ---: | ---: |
| 00 | 20 | 4 |
| 01 | 30 | 9 |
| 10 | 25 | 10 |
| 11 | 25 | 20 |

When candidate \(q=11\) is entered, only mode 11 enters \(\eta=1\):

\[
\widehat g
=\frac{4+9+10}{20+30+25}
=\frac{23}{75}
=.307,
\]

\[
\widehat s
=\frac{25-20}{25}
=.20,
\]

\[
\widehat\delta=.493.
\]

When candidate \(q=10\) is selected, both 10 and 11 go into \(\eta=1\):

\[
\widehat g
=\frac{4+9}{20+30}
=.26,
\]

\[
\widehat s
=\frac{(25+25)-(10+20)}{50}
=.40,
\]

\[
\widehat\delta=.34.
\]

The second candidate is missing attribute 2, mastery group blend mode 10, slip up.

## Where does the approximation come from?

Candidate calculations follow the current Q fit

\[
\widehat P(\boldsymbol\alpha_l\mid\boldsymbol X_i),
\]

The posterior is not immediately recomputed for each new q-vector. If there are many errors in the initial Q, the item parameters and the posterior itself may be significantly biased, and the candidate \(\widehat\delta\) will also be affected.

The treatment of the paper is:

- First use fast regrouping to generate candidate Q;
- Run a small amount of additional EM loops under candidate Q;
- Compare different \(\varepsilon\) solutions with updated full quiz metrics.

