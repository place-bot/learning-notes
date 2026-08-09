# Discrimination index and verification target

## Correctness guidelines for the original text

For item \(j\), let \(\boldsymbol\alpha_{l'}\) act as a candidate q-vector, and calculate \(\eta_{ll'}\) according to this vector. The author writes the best candidate as

\[
\boldsymbol q_j
=
\underset{\boldsymbol\alpha_{l'}}{\arg\max}
\left[
P(X_j=1\mid\eta_{ll'}=1)
-
P(X_j=1\mid\eta_{ll'}=0)
\right].
\]

Note the difference in parentheses as

\[
\delta_{jl'}
=
P(X_j=1\mid\eta_{ll'}=1)
-
P(X_j=1\mid\eta_{ll'}=0).
\]

Under DINA,

\[
\delta_{jl'}=1-s_{jl'}-g_{jl'}.
\]

So maximizing \(\delta\) is equivalent to minimizing \(s+g\).

## Why it can be used as a candidate comparison quantity

If q-vector is reasonable:

- The \(\eta=1\) group should have a higher correct answer rate \(1-s\);
- The \(\eta=0\) group should have a lower correct answer rate \(g\);
- There is a big gap between the two groups.

If q-vector misclassifies many attribute profiles, the correct answer rates of the two groups will shrink toward the middle and \(\delta\) will decrease.

## Numerical explanation

| \(g\) | \(s\) | \(1-s\) | \(\delta\) |meaning|
| ---: | ---: | ---: | ---: | --- |
| .20 | .20 | .80 | .60 |The difference between the two groups is .60|
| .20 | .50 | .50 | .30 |The mastery group is contaminated|
| .50 | .20 | .80 | .30 |nonmastery group is tainted|
| .48 | .49 | .51 | .03 |The two groups are nearly indistinguishable|

## The difference between it and IRT discrimination

Here \(\delta\) is the difference between the correct answer rates of the two types of conditions:

\[
\delta=P(X=1\mid\eta=1)-P(X=1\mid\eta=0).
\]

It depends on:

- conjunctive grouping of DINA;
- Current candidate q-vector;
- Current posterior and posterior attribute profile distribution;
- Reaction data for the current sample.

Therefore, if you change the q-vector for the same question, \(\delta\) will change. It does not define a slope on a continuous ability axis.

## Small parameters are sufficient but do not constitute necessary conditions

The author specifically reminds:

- Small \(g\) and small \(s\) can support good separation of the current q-vector;
- A certain question may always have a higher \(g\) or \(s\) under the existing attribute set;
- When replacing existing attributes cannot improve, the problem may come from missing attributes, item quality, or DINA structure.

Therefore, low \(\delta\) will trigger diagnosis, and it is impossible to determine which Q box to change alone.

## Item-level and test-level goals

item level search comparison

\[
\widehat\delta_j(\boldsymbol q).
\]

When multiple \(\varepsilon\) generate multiple sets of candidate Q, the paper uses test-level indicators

\[
\overline{\widehat g}+\overline{\widehat s}
=
\frac{1}{J}\sum_{j=1}^{J}\widehat g_j
+
\frac{1}{J}\sum_{j=1}^{J}\widehat s_j
\]

Compare the entire set of solutions and append a small number of EM loops updating parameters and posteriors under candidate Q.

The relationship between the two levels is:

\[
\text{Propose candidates topic by topic}
\longrightarrow
\text{Composition candidate Q}
\longrightarrow
\text{Full test re-comparison}.
\]

