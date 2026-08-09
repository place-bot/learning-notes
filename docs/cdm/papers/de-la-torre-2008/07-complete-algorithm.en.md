# Complete verification process

## Input and output

Input:

- Bipartite response matrix \(\boldsymbol X\);
- Initial Q matrix \(Q^{(0)}\);
- Fixed \(K\) attributes and their meanings;
- a set of thresholds \(\mathcal E\);
- DINA estimation settings.

Output:

- Candidate Q under each \(\varepsilon\);
- modified q-vector;
- Updated \(g,s,\delta\);
- Test level \(\bar g+\bar s\);
- List of items to be reviewed by content experts.

## Phase 1: Fitting the current model

Fitting DINA under \(Q^{(0)}\), we get:

\[
\widehat{\boldsymbol g}^{(0)},\quad
\widehat{\boldsymbol s}^{(0)},\quad
\widehat P(\boldsymbol\alpha_l\mid\boldsymbol X_i).
\]

Also recording raw test-level metrics:

\[
C(Q^{(0)})
=
\overline{\widehat g}^{(0)}
+
\overline{\widehat s}^{(0)}.
\]

## Phase 2: Establish posterior expectation count

Calculate for all \(j,l\):

\[
N_{jl}=\sum_i\widehat p_{il},
\qquad
R_{jl}=\sum_iX_{ij}\widehat p_{il}.
\]

Do this step only once.

## Stage 3: Search sequentially question by question

For each question \(j\) and each \(\varepsilon\):

```text
selected = empty
previous_delta = undefined

for s = 1,...,K:
    candidates = selected plus each remaining attribute
    compute g, s, delta for every candidate
    best = candidate with largest delta

    if this is the first step:
        accept best
    else if best.delta - previous_delta > epsilon:
        accept best
    else:
        stop and retain the previous candidate
```

Get the suggested rows for this question under the threshold \(\varepsilon\)

\[
\widehat{\boldsymbol q}_j(\varepsilon).
\]

## Stage 4: Putting together candidate Q

\[
\widehat Q(\varepsilon)
=
\begin{bmatrix}
\widehat{\boldsymbol q}_1(\varepsilon)\\
\vdots\\
\widehat{\boldsymbol q}_J(\varepsilon)
\end{bmatrix}.
\]

The smaller \(\varepsilon\) is more likely to accept new attributes, and the candidate Q is often denser; the larger \(\varepsilon\) requires each new addition to bring a more obvious improvement in discrimination, and the candidate Q is often rarer.

## Stage 5: Adding EM

The paper adds several EM cycles under each set of candidate Q, and updates:

\[
\widehat{\boldsymbol g}(\varepsilon),\quad
\widehat{\boldsymbol s}(\varepsilon),\quad
\widehat p_{il}(\varepsilon).
\]

5 additional EM cycles were added to the simulation; 100 were added to the fractional subtraction; and 10 were added to the NAEP.

## Stage 6: Full test comparison

Calculate

\[
C\{\widehat Q(\varepsilon)\}
=
\overline{\widehat g}(\varepsilon)
+
\overline{\widehat s}(\varepsilon).
\]

And compare both:

- The same grid proportions as the original Q;
- The same whole row proportions as the original Q;
- Which questions are the changes focused on;
- Improvement or deterioration of each question \(\delta\);
- Whether the modified attribute interpretation can be established.

## Stage 7: Substantive review

It is recommended to organize each changed question into:

|content|question|
| --- | --- |
|Original q-vector|Why do experts request these properties in the first place?|
|Recommend q-vector|What attributes have been added or removed?|
|Parameter changes|\(g,s,\delta\) How much improved?|
|item text|What are alternative strategies, cues, and language loading?|
|response evidence|Which explanation is supported by spoken reports or process data?|
|final decision|Keep, modify, delete item or reconstruct attributes?|

The algorithm generates statistical recommendations, and ultimately Q should record joint justification of statistical and content evidence.

