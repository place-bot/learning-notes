#Clinical Data & Errata

## Data source

The second real data example in the paper comes from the Dutch version of MCMI-III:

|item|numerical value|
| --- | ---: |
|Subject|1,210 Belgian subjects|
|Female ratio| 39% |
|clinical patients| 68% |
|remaining subjects|inmates|
|Analyze items| 44 |
|properties/scale| 4 |

The four properties are:

1. Anxiety；
2. Somatoform；
3. Thought Disorder；
4. Major Depression。

Here, clinical scale status is used as a binary attribute to illustrate that CDM can be used as a diagnostic statistical tool outside the education field.

## Q matrix structure summary

|Specify method| Anxiety | Somatoform | Thought Disorder | Major Depression |
| --- | ---: | ---: | ---: | ---: |
|Appear alone| 9 | 2 | 11 | 6 |
|Appears in conjunction with other attributes| 5 | 10 | 6 | 12 |
|total| 14 | 12 | 17 | 18 |

Among 44 items:

- 28 items are single attribute items;
- 15 items are dual attribute items;
- 1 is a three-attribute item.

It is estimated to take less than 20 seconds using the same Ox program, computer, and 0.001 convergence criterion as the fraction subtraction example.

## Probability result of dual attribute item

The paper uses a human symptom item to illustrate the combined impact of Somatoform and Major Depression. According to the corrigendum of the same year, this website does not reproduce the copyrighted title.

The endorsement probabilities of the four modes are

\[
\begin{aligned}
P(00)&=0.05,\\
P(10)&=0.49,\\
P(01)&=0.32,\\
P(11)&=0.74.
\end{aligned}
\]

The improvement associated with Somatoform alone is greater than the improvement associated with Major Depression alone.

## Judgment of DINO and additive models

DINO requirements

\[
P(10)=P(01)=P(11).
\]

Current estimates clearly do not satisfy this structure.

identity-link A-CDM prediction

\[
\begin{aligned}
P(11)
&=
P(10)+P(01)-P(00)\\
&=
0.49+0.32-0.05\\
&=
0.76.
\end{aligned}
\]

The saturation estimate is 0.74, which is very close, so this item has an approximately additive relationship on the probability scale.

The corresponding G-DINA effect is

\[
\delta_0=0.05,
\quad
\delta_1=0.44,
\quad
\delta_2=0.27,
\quad
\delta_{12}=-0.02.
\]

The interaction terms are small, supporting additive approximations.

## 2011 Errata

The errata DOI is

[10.1007/s11336-011-9214-8](https://doi.org/10.1007/s11336-011-9214-8)。

Errata description:

- The original article published a question from MCMI-III;
- The content is copyrighted quiz material;
- The author failed to obtain appropriate permission before publication;
- The journal regrets this.

The correction is for the reprint permission of the question stem, and does not correct the above sample size, Q matrix summary or four probability results.

## Why notes must deal with errata

Intensive technical reading requires checking the main text and subsequent errata at the same time. The processing taken here is:

- Preserve statistical structure and numerical results;
- Delete the original text of the question subject that is protected by copyright;
- Clearly state the roles of the four attributes;
- Document copyright issues separately from model conclusions.

This avoids repeating in secondary dissemination authorization errors already acknowledged by the original text.
