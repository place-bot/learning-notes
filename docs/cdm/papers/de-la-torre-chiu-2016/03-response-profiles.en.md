# Five success probability profiles

The paper first uses two attribute questions to explain how the same G-DINA saturated framework contains five generation processes. Let the success probability of zero attribute group and all attribute group be

\[
p_0=.20,
\qquad
p_1=.80.
\]

The pattern sequence is \(00,10,01,11\).

## DINA

\[
\boldsymbol P=(.20,.20,.20,.80).
\]

identity-link parameters:

\[
(\delta_0,\delta_1,\delta_2,\delta_{12})
=(.20,.00,.00,.60).
\]

Only mastering two attributes at the same time will produce an improvement.

## DINA/A-CDM

The paper takes the average of the success probabilities of DINA and A-CDM:

\[
\boldsymbol P=(.20,.35,.35,.80),
\]

\[
(\delta_0,\delta_1,\delta_2,\delta_{12})
=(.20,.15,.15,.30).
\]

A single attribute has contributed, and there is still a positive interaction when fully mastered.

## A-CDM

\[
\boldsymbol P=(.20,.50,.50,.80),
\]

\[
(\delta_0,\delta_1,\delta_2,\delta_{12})
=(.20,.30,.30,.00).
\]

Each attribute contribution adds up and the interaction is zero.

## DINO/A-CDM

\[
\boldsymbol P=(.20,.65,.65,.80),
\]

\[
(\delta_0,\delta_1,\delta_2,\delta_{12})
=(.20,.45,.45,-.30).
\]

Mastering any one attribute brings a greater improvement, while mastering both at the same time slows down the gains.

## DINO

\[
\boldsymbol P=(.20,.80,.80,.80),
\]

\[
(\delta_0,\delta_1,\delta_2,\delta_{12})
=(.20,.60,.60,-.60).
\]

Any one of the required attributes is sufficient to achieve a high success rate.

## Why can the same verification indicator cover five models?

GDI directly uses the success probability of each group:

\[
P_j(\boldsymbol\alpha).
\]

It does not require that effects be conjunctive, disjunctive, or additive. As long as omitting attributes that really affect the probability of success collapses heterogeneous categories into the same group, the between-group variance will decrease.

This is also the main generalization of the 2016 method relative to the 2008 DINA indicator.
