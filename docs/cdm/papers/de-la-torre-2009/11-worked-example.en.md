# Two complete EM iterations, from one student to a class

## Settings

Assume \(K=2\), the Q behavior of three questions:

\[
\boldsymbol q_1=(1,0),
\qquad
\boldsymbol q_2=(0,1),
\qquad
\boldsymbol q_3=(1,1).
\]

The four attribute profiles are:

\[
(0,0),(0,1),(1,0),(1,1).
\]

item parameters：

\[
\boldsymbol g=(0.20,0.10,0.25),
\]

\[
\boldsymbol s=(0.10,0.20,0.15).
\]

Assume that the four patterns are the same a priori:

\[
\pi_l=0.25.
\]

One student's response was

\[
\boldsymbol X_i=(1,0,1).
\]

## Step one: ideal response

| \(\boldsymbol\alpha_l\) | \(\eta_{l1}\) | \(\eta_{l2}\) | \(\eta_{l3}\) |
| --- | ---: | ---: | ---: |
| (0,0) | 0 | 0 | 0 |
| (0,1) | 0 | 1 | 0 |
| (1,0) | 1 | 0 | 0 |
| (1,1) | 1 | 1 | 1 |

The third question requires two attributes, so there is only \(\eta_{l3}=1\) of \((1,1)\).

## Step 2: Response likelihood in each mode

### Pattern (0,0)

All three questions are at \(\eta=0\):

\[
L_i(0,0)
=
g_1(1-g_2)g_3
\]

\[
=
0.20\times0.90\times0.25
=0.045.
\]

### Pattern (0,1)

The second question is at \(\eta=1\), but the student answered it incorrectly:

\[
L_i(0,1)
=
g_1s_2g_3
\]

\[
=
0.20\times0.20\times0.25
=0.010.
\]

### Pattern (1,0)

The first question is at \(\eta=1\), the second and third questions are at \(\eta=0\):

\[
L_i(1,0)
=
(1-s_1)(1-g_2)g_3
\]

\[
=
0.90\times0.90\times0.25
=0.2025.
\]

### Pattern (1,1)

All three questions are at \(\eta=1\):

\[
L_i(1,1)
=
(1-s_1)s_2(1-s_3)
\]

\[
=
0.90\times0.20\times0.85
=0.153.
\]

## Step 3: Posterior pattern probability

The priors are the same, so we only need to normalize the four likelihoods:

\[
0.045+0.010+0.2025+0.153
=0.4105.
\]

|mode|Posterior \(w_{il}\)|
| --- | ---: |
| (0,0) | \(0.045/0.4105=0.1096\) |
| (0,1) | \(0.010/0.4105=0.0244\) |
| (1,0) | \(0.2025/0.4105=0.4933\) |
| (1,1) | \(0.153/0.4105=0.3727\) |

The sum is 1.

The MAP attribute profile is

\[
\widehat{\boldsymbol\alpha}_i^{\text{MAP}}
=(1,0).
\]

## Single attribute posterior mastery probability

Property 1:

\[
P(\alpha_{i1}=1\mid\boldsymbol X_i)
=
0.4933+0.3727
=0.8660.
\]

Property 2:

\[
P(\alpha_{i2}=1\mid\boldsymbol X_i)
=
0.0244+0.3727
=0.3971.
\]

This retains more uncertainty information than just reporting the MAP pattern.

## This student’s contribution to the third question, M-step counting

In the third question, there is only \(\eta=1\) with mode \((1,1)\):

\[
I_{3,i}^{(1)}=0.3727,
\qquad
I_{3,i}^{(0)}=0.6273.
\]

The student answered the third question correctly, so:

\[
R_{3,i}^{(1)}=0.3727,
\qquad
R_{3,i}^{(0)}=0.6273.
\]

Adding these scores for all students gives us the overall update of equations (10)--(11). A single student produces extreme proportions, illustrating the M-step of EM's reliance on full-sample expected counts.

## How to react to change the posterior

The student's correct answer to the first question strongly supports attribute 1; the incorrect answer to the second question reduces support for attribute 2; the correct answer to the third question may come from mastering both attributes or from the correct guess of \(g_3=0.25\).

DINA jointly determines attributes through complete response vectors, rather than directly equating single question responses with a certain attribute mastery.

## Complete the M-step with four students

Keep the original first student and add three responses:

\[
X=\begin{pmatrix}1&0&1\\0&1&0\\1&1&1\\0&0&0\end{pmatrix}.
\]

This is a teaching dataset, not paper data. Use the original g, s and uniform fixed prior. In profile order 00,01,10,11, the class-specific success probabilities are

\[
P=\begin{pmatrix}.2&.1&.25\\.2&.8&.25\\.9&.1&.25\\.9&.8&.85\end{pmatrix}.
\]

For example, student2's likelihood under11 is \(.1\times.8\times.15=.012\). Student4 under00 gives \(.8\times.9\times.75=.54\).

| Response | 00 | 01 | 10 | 11 | Marginal probability |
| --- | ---: | ---: | ---: | ---: | ---: |
| 101 | .045 | .010 | .2025 | .153 | .102625 |
| 010 | .060 | .480 | .0075 | .012 | .139875 |
| 111 | .005 | .040 | .0225 | .612 | .169875 |
| 000 | .540 | .120 | .0675 | .003 | .182625 |

The marginal is the row sum times .25, not the raw row sum. Normalize prior-weighted likelihoods:

| Student | 00 | 01 | 10 | 11 |
| --- | ---: | ---: | ---: | ---: |
| 1 | .109622412 | .024360536 | .493300853 | .372716200 |
| 2 | .107238606 | .857908847 | .013404826 | .021447721 |
| 3 | .007358352 | .058866814 | .033112583 | .900662252 |
| 4 | .739219713 | .164271047 | .092402464 | .004106776 |

## Aggregate profiles into item-specific states

Define \(h_{ij}=P(\eta_{ij}=1\mid X_i)\). For the three items respectively, sum columns10+11, columns01+11, and column11 alone:

| Student | Item1 h | Item2 h | Item3 h |
| --- | ---: | ---: | ---: |
| 1 | .866017052 | .397076736 | .372716200 |
| 2 | .034852547 | .879356568 | .021447721 |
| 3 | .933774834 | .959529065 | .900662252 |
| 4 | .096509240 | .168377823 | .004106776 |

For item3:

\[
I_3^{(1)}=.372716200+.021447721+.900662252+.004106776
=1.298932949.
\]

Only students1 and3 answered correctly, hence

\[
R_3^{(1)}=.372716200+.900662252=1.273378451.
\]

Then \(I_3^{(0)}=4-I_3^{(1)}=2.701067051\) and
\(R_3^{(0)}=2-R_3^{(1)}=.726621549\).
Wrong responses contribute to denominators but not correct-response counts.

| Item | \(I^{(0)}\) | \(R^{(0)}\) | \(I^{(1)}\) | \(R^{(1)}\) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 2.068846326 | .200208113 | 1.931153674 | 1.799791887 |
| 2 | 1.595659807 | .161114366 | 2.404340193 | 1.838885634 |
| 3 | 2.701067051 | .726621549 | 1.298932949 | 1.273378451 |

Each pair of group sizes sums to4; each pair of correct counts sums to2. Fractional counts are posterior expectations, not literal fractional people.

## First M-step

\[
g_3^{(1)}=.726621549/2.701067051=.269012777,
\]

\[
s_3^{(1)}=(1.298932949-1.273378451)/1.298932949=.019673454.
\]

The full update is

\[
g^{(1)}=(.096772830,.100970373,.269012777),\quad
s^{(1)}=(.068022441,.235180762,.019673454).
\]

Individual parameters need not decrease; the optimized objective is the likelihood, not the sum of slips and guesses.

## Recompute the posterior and update again

Keep the prior fixed. Under the new parameters:

| Student | 00 | 01 | 10 | 11 |
| --- | ---: | ---: | ---: | ---: |
| 1 | .049818402 | .013032195 | .479779635 | .457369768 |
| 2 | .115402108 | .874135149 | .008690984 | .001771759 |
| 3 | .003520608 | .026667515 | .033905467 | .935906410 |
| 4 | .747700073 | .195593858 | .056309626 | .000396443 |

Aggregate again to obtain

\[
g^{(2)}=(.045925319,.108030406,.232947155),\quad
s^{(2)}=(.034024512,.266038333,.001553772).
\]

The marginal log likelihood progresses from -7.716692639 to -7.372385749 to -7.218309795. The initial value is the sum of the logs of the four marginal probabilities above.

The first maximum parameter change is .130326546, far above \(10^{-4}\). Two iterations illustrate the mechanics; they do not establish convergence.

## Optional prior update is a different branch

Column means of the initial posterior give

\[
\pi^{(1)}=(.240859770,.276351811,.158055181,.324733237).
\]

Using this prior next would produce a different second iteration. Do not mix it with the fixed-prior numbers above.

## Reproduce every intermediate number

Run tools/de_la_torre_2009_em_trace.py with Python3. It checks direct Bayes against log-sum-exp, count identities, M-step ratios, ten monotone iterations, six score derivatives, and matrix inversion. Internal calculations are unrounded.

Four students cannot yield a full-rank six-parameter OPG matrix, so no six-parameter standard errors are invented for this example.
