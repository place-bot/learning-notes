# Hypothetical questions and exhaustive search

## Original text settings

Assumptions:

- \(K=5\)；
- 32 attribute profiles with equal probability;
- The item actually requires attributes 1 and 2;
- \(g=s=.20\)；
- The real q-vector is \(11000\).

The true probability of correct answer is

\[
P(X=1\mid\eta=0)=.20,\qquad
P(X=1\mid\eta=1)=.80.
\]

There are 24 patterns missing attribute 1 or 2, with a .20 chance of getting it right; 8 patterns have both attributes 1 and 2, with a .80 chance of getting it right.

## Candidate 10000

If only attribute 1 is required:

- \(\eta^*=0\) contains the first 16 patterns, all with a true correct answer rate of .20;
- \(\eta^*=1\) contains the last 16 patterns, 8 of which have a true answer rate of .20 and 8 of which have a .80 true answer rate.

So

\[
\widehat g^*=.20,
\]

\[
1-\widehat s^*
=\frac{8(.20)+8(.80)}{16}
=.50,
\]

\[
\delta^*=.50-.20=.30.
\]

Omission of attribute 2 allowed the mastery group to mix in 8 true low-response patterns.

## Candidate 11000

This candidate exactly recovers the true grouping:

\[
\widehat g^*=.20,\qquad
\widehat s^*=.20,\qquad
\delta^*=.60.
\]

This is the maximum value among 31 non-zero candidates.

## Candidate 11100

After adding irrelevant attribute 3:

- The modes in \(\eta^*=1\) are still all high answer modes, so \(1-\widehat s^*=.80\);
- Half of the high-response modes that master attributes 1 and 2 but not attribute 3 are put into \(\eta^*=0\);
- Original Table 1 Obtain \(P(X=1\mid\eta^*=0)=.29\).

Therefore

\[
\delta^*=.80-.29=.51.
\]

Adding extra irrelevant attributes mainly increases guessing.

## Original Table 1 Key Candidates

|Candidate q|Candidate \(g^*\)|Candidate \(1-s^*\)| \(\delta^*\) |Error type|
| :---: | ---: | ---: | ---: | --- |
| 10000 | .20 | .50 | .30 |Drain property 2|
| 01000 | .20 | .50 | .30 |Leak property 1|
| 11000 | .20 | .80 | .60 |Correct|
| 11100 | .29 | .80 | .51 |Multiple attributes 3|
| 11110 | .32 | .80 | .48 |Multiple attributes 3, 4|
| 11111 | .34 | .80 | .46 |Multiple attributes 3, 4, 5|
| 10100 | .30 | .50 | .20 |Missing 2, excess 3|
| 00100 | .35 | .35 | .00 |Use only irrelevant attributes|

## Exhaustive algorithm

Check all non-zero candidates for each question:

\[
\mathcal Q_K=\{0,1\}^K\setminus\{\boldsymbol 0\},
\qquad |\mathcal Q_K|=2^K-1.
\]

Pseudo code:

```text
for each item j:
    for each nonzero candidate q:
        regroup all attribute patterns using q
        compute g(q), s(q), delta(q)
    choose the q with largest delta
```

When \(K=5\), 31 candidates per question can still be processed; when \(K=20\), there are 1,048,575 candidates per question. The original article therefore further proposes sequential search.

