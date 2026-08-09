# Condition A: Completeness

## 1. Definition

\(Q\) under DINA is complete, which means it contains

\[
I_K=
\begin{pmatrix}
1&0&\cdots&0\\
0&1&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&1
\end{pmatrix}.
\]

Each attribute has at least one question that requires only that attribute.

## 2. Why can single-attribute questions separate latent classes?

For the unit line \(\boldsymbol e_k\), the DINA ideal response is

\[
\Gamma_{j,\boldsymbol\alpha}
=I(\alpha_k=1).
\]

Therefore, this question directly divides the latent class into two groups according to the \(k\) attribute. \(K\) The unit rows of the channels are combined so that any two different attribute profiles are different in at least one question's ideal response.

Formally, the integrity guarantee

\[
\boldsymbol\alpha\ne\boldsymbol\alpha'
\quad\Longrightarrow\quad
\Gamma_{\cdot,\boldsymbol\alpha}(Q)
\ne
\Gamma_{\cdot,\boldsymbol\alpha'}(Q).
\]

## 3. Consequences of Lack of Integrity

If there are no single-attribute questions with attribute \(k\), some latent classes may have the same ability status on all questions. Their proportions can only enter the observed distribution as sums.

Assume that the two patterns \(\boldsymbol\alpha,\boldsymbol\alpha'\) satisfy all questions

\[
\Gamma_{j,\boldsymbol\alpha}
=
\Gamma_{j,\boldsymbol\alpha'}.
\]

Then the observation distribution only depends on

\[
p_{\boldsymbol\alpha}
+p_{\boldsymbol\alpha'},
\]

The two proportions cannot be restored independently.

## 4. Structure of Study IV

The supplementary materials are taken as \(J=20\) and constructed respectively:

- Incomplete \(Q_1\) for \(K=3\);
- Incomplete \(Q_2\) for \(K=5\).

The author gives two more substitution matrices \(Q_i'\) and \(Q_i''\), keeping the item parameters the same, and re-merges or distributes the proportion of latent classes that cannot be distinguished.

Three sets of models for all

\[
2^{20}=1,048,576
\]

two reaction modes give the same probability, the maximum numerical difference is

\[
2.17\times10^{-19}
\quad\text{Arrive}\quad
6.51\times10^{-19}
\]

between.

## 5. Strict identification and general identification

For DINA, Condition A cannot be relaxed overall in pan-recognition. Once the latent class ideal response columns overlap structurally, the phenomenon of inseparable proportions covers the entire parameter area and has a positive dimension.

## 6. Test design explained

Completeness provides a semantic anchor for each attribute. When there are no single-attribute questions, even if there are many multi-attribute questions, it is possible that only attribute combinations can be identified, and each column cannot be stably named and separated.

This requirement relies on DINA's conjunctive rules. Generally, the general identification of RLCM can be relaxed into general completeness, allowing the anchor question to require other attributes at the same time.
