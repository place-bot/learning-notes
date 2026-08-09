# Experimental cropping: 805 questions and two mutually exclusive categories

## 1. Binary classification data

definition

\[
y_j=
\begin{cases}
0,&\text{question}j\text{Belongs to Operations of integers},\\
1,&\text{question}j\text{Belongs to Mathematical thinking}.
\end{cases}
\]

The corresponding two columns of \(Q\) rows are only

\[
(1,0)
\quad\text{or}\quad
(0,1).
\]

Predicting \(y_j\) restores one of the two possible Q rows.

## 2. Category ratio

\[
\Pr(O)=\frac{666}{805}=0.8273,
\]

\[
\Pr(M)=\frac{139}{805}=0.1727.
\]

The majority class is about the minority class

\[
\frac{666}{139}=4.79
\]

times.

## 3. Simplification brought by one-hot hypothesis

Generally Q line has

\[
2^K
\]

A binary pattern; after removing all zero rows, there is still

\[
2^K-1
\]

a legal combination.

The one-hot constraint reduces the number of candidates to \(K\):

\[
\{\boldsymbol e_1,\ldots,\boldsymbol e_K\}.
\]

After further retaining two attributes, there are only two candidates left.

## 4. What does this simplification exclude?

The experiment did not encounter the following situations:

- One question requires both integer operations and mathematical reasoning;
- There is a prerequisite or hierarchical relationship between attributes;
- item cannot distinguish multiple solutions based on text alone;
- Multiple reasonable Q lines for the same question;
- An attribute exists but is not marked by experts.

## 5. Generalize from binary classification to multi-label

If each question can correspond to multiple attributes, a probability can be established for each column:

\[
\widehat{\boldsymbol p}_j
=
\left(
p_{j1},\ldots,p_{jK}
\right),
\qquad
p_{jk}
=
\Pr(q_{jk}=1\mid d_j).
\]

Then select the threshold:

\[
\widehat q_{jk}
=
\mathbb I(p_{jk}\ge \tau_k).
\]

Reporting is required at this time:

- micro-F1 and macro-F1;
- precision/recall for each attribute;
- row exact match；
- Hamming loss；
- The fitting and classification results after the Q matrix enters CDM.

The paper does not make this generalization.

## 6. More appropriate actual positioning

This method can be used as a candidate Q row generator:

1. Output attribute probabilities for new questions;
2. Send high-level reliability questions to quick review;
3. Send low-level reliability or multi-attribute conflict issues to complete expert discussion;
4. Perform CDM calibration after collecting student responses.

This positioning both leverages textual automation and preserves measurement evidence chains.
