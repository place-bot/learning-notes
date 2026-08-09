# Complete estimation and verification algorithm

## Input

- \(N\times J\) bisection response matrix \(Y\);
- \(J\times K\) initial Q matrix \(Q_0\);
- G-DINA model;
- PVAF threshold \(\varepsilon\).

## Stage 1: Fit the model at initial Q

Estimated using empirical Bayes EM:

- item parameters;
- overall probability of attribute profile;
- Complete attribute profile posterior for each student.

\[
\tau_{il}
=
P(\boldsymbol\alpha_i=\boldsymbol\alpha_l
\mid\boldsymbol Y_i,Q_0,\widehat\Theta).
\]

## Phase 2: Constructing full pattern statistics

Mode weight:

\[
\widehat w_l
=
\frac{1}{N}\sum_i\tau_{il}.
\tag{13}
\]

The success probability of item \(j\) in full mode \(l\):

\[
\widehat p_{jl}
=
\frac{\sum_i\tau_{il}Y_{ij}}
{\sum_i\tau_{il}}.
\tag{14}
\]

The main text of the paper only summarizes the two-stage process; Liu (2017) clearly gives equation (14) based on communication with the author.

## Stage 3: Exhausting candidates question by question

For each \(\boldsymbol q\ne\boldsymbol0\):

1. Group \(2^K\) complete patterns according to the attributes required by the candidate;
2. Find \(\widehat w\) for each group;
3. Use \(\widehat w\) to weight \(\widehat p_{jl}\) to find the composition power;
4. Calculate \(\widehat{\varsigma}_j^2(\boldsymbol q)\);
5. Divide by the full attribute vector GDI to get PVAF.

## Phase 4: Proposal generation Q

Execute each question:

\[
\operatorname{PVAF}\ge\varepsilon
\rightarrow
\text{Minimum attributes}
\rightarrow
\text{The largest GDI of its kind}.
\]

Group all suggested lines into

\[
\widehat Q.
\]

## Phase 5: Content Review

The real data analysis of the paper shows that statistical suggestions may produce unexplained differences in content between similar items. A complete application requires:

1. Check whether the proposed attributes to be added or deleted comply with the problem-solving steps;
2. Refit suggestion Q;
3. Compare item fitting, overall fitting and classification stability;
4. Preserve uncertainty for multiple candidates close to the threshold;
5. Final Q confirmed by subject experts.

## Three "probabilities" in the algorithm

|object|formula|role|
| --- | --- | --- |
|student posterior| \(\tau_{il}\) |Softly assign everyone to the complete attribute profile|
|Pattern weight| \(\widehat w_l=N^{-1}\sum_i\tau_{il}\) |Weighted distribution of GDI|
|Probability of success| \(\widehat p_{jl}\) |Describe the response structure of item in complete mode|

## Original text implementation boundary

The paper states that the two-step analysis was performed by the Ox program and invites readers to contact the first author to obtain the code. The article, supplementary material, and references do not have public repository links, so it is currently impossible to check the original Ox implementation line by line.
