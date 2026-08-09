# Calculate the E step of an EM by hand

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

### Pattern \((0,0)\)

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

### Pattern \((0,1)\)

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

### Pattern \((1,0)\)

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

### Pattern \((1,1)\)

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
