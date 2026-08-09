# DINA, G-DINA and general RLCM

## 1. DINA’s ideal response

DINA uses conjunctive rules:

\[
\Gamma_{j,\boldsymbol\alpha}(Q)
=
I(\boldsymbol\alpha\succeq\boldsymbol q_j).
\]

Only if all attributes required by the item are mastered, the ideal response will be 1.

Order

\[
c_j=1-s_j
\]

is the correct answer probability of the ability latent class, \(g_j\) is the correct guessing probability of the non-ability latent class, then

\[
\theta_{j,\boldsymbol\alpha}
=
c_j^{\Gamma_{j,\boldsymbol\alpha}}
g_j^{1-\Gamma_{j,\boldsymbol\alpha}},
\qquad c_j>g_j.
\]

So there are only two response probabilities for each question. The main text of the paper mainly uses \(\boldsymbol s\) and \(\boldsymbol g\), and the official simulation code uses \(\boldsymbol c\) and \(\boldsymbol g\) extensively.

## 2. DINA’s structural compression

Generally, \(\Theta\) has \(J2^K\) positions. DINA compresses each line into:

\[
\theta_{j,\boldsymbol\alpha}
=
\begin{cases}
c_j,&\boldsymbol\alpha\succeq\boldsymbol q_j,\\
g_j,&\boldsymbol\alpha\nsucceq\boldsymbol q_j.
\end{cases}
\]

This strong structure enables Theorem 1 to reduce the strict identification conditions to A/B/C.

## 3. G-DINA

Corresponding to the question \(j\), G-DINA includes all the main effect and interaction effect of the required attributes:

\[
\theta_{j,\boldsymbol\alpha}
=
\sum_{S\subseteq\{1,\ldots,K\}}
\beta_{j,S}
\prod_{k\in S}q_{jk}\alpha_k.
\]

Only when each attribute in \(S\) is required by question \(j\), the corresponding \(\beta_{j,S}\) enters the model.

For example, when \(\boldsymbol q_j=(1,1,0)\),

\[
\theta_{j,\boldsymbol\alpha}
=
\beta_{j,\varnothing}
+\beta_{j,\{1\}}\alpha_1
+\beta_{j,\{2\}}\alpha_2
+\beta_{j,\{1,2\}}\alpha_1\alpha_2.
\]

## 4. General RLCM

The paper classifies G-DINA, LCDM, GDM, etc. into general RLCM. They allow the same question to give multiple probabilities for different reduced attribute profiles, and the parameter freedom is higher than DINA.

Recognition requirements vary by model family:

|model|strict joint identification|Pan joint recognition|
| --- | --- | --- |
| DINA |A+B+C necessary and sufficient|Theorem 2 gives important boundaries; \(K=2\) fully characterizes|
| DINO |Transferable by DINA duality|The corresponding conclusions can be transferred|
|General RLCM|A+B+C is still a necessary condition|C necessary; D+E sufficient; pan-completely necessary|

## 5. Additional difficulties brought by unknown Q

When \(Q\) is known, just compare

\[
(\Theta,\boldsymbol p)
\quad\text{with}\quad
(\bar\Theta,\bar{\boldsymbol p}).
\]

Also compare when unknown \(Q\)

\[
(Q,\Theta,\boldsymbol p)
\quad\text{with}\quad
(\bar Q,\bar\Theta,\bar{\boldsymbol p}).
\]

Candidate models can vary both structural and continuous parameters so that the response distributions of the two models completely overlap. All the main theorems of this article revolve around the elimination of this joint substitution.
