#Relationship with existing recognition result

## 1. Four confusing questions

|question|\(Q\) status|target|
| --- | --- | --- |
|DINA parameter identification|known and correct|Identify \((\boldsymbol s,\boldsymbol g,\boldsymbol p)\)|
|General RLCM parameter identification|known and correct|Identify \((\Theta,\boldsymbol p)\)|
|Q-Learning Consistency|unknown|Estimated \(Q\), often accompanied by parameter estimates|
|joint identification of this article|unknown|Uniquely recover \(Q\) and model parameters from the overall response distribution|

Another DINA paper by Gu and Xu also shows A/B/C conditions, assuming \(Q\) is known. This paper allows candidate models to use another \(\bar Q\), thus requiring the exclusion of a larger set of observational equivalences.

## 2. Why are early sufficient conditions strong?

Joint identification results such as Chen et al. (2015) and Xu & Shang (2018) often require \(Q\) to contain at least two sets of complete submatrices \(I_K\). This type of structure is convenient for decomposing or grouping arguments using three tensors:

\[
\text{Question set 1}\quad|\quad
\text{Question set 2}\quad|\quad
\text{Question set 3}.
\]

For three conditionally independent question groups, the latent class mixture distribution can be written as a three-way tensor, and then the Kruskal-type unique result can be called. The price is higher item number and design constraints.

This article performs more refined algebraic elimination on the special two-parameter structure of DINA, retaining only one set of \(I_K\), and then supplements the information with the mutual column differences of \(Q^\star\) and three measurements per column.

## 3. Improvement of item number

The classical three-way decomposition condition usually brings

\[
J\ge 2K+1.
\]

The DINA conditions of this article can be met

\[
J\ge K+\left\lceil\log_2 K\right\rceil+1.
\]

The first item \(K\) comes from \(I_K\); about \(\log_2K\) rows are enough to encode distinct columns for \(K\) attributes; the extra row helps each column accumulate at least three 1's.

When \(K=8\):

\[
2K+1=17,\qquad
K+\lceil\log_2K\rceil+1=12.
\]

This explains the design value of the conditions in this article: it gives a test blueprint closer to the minimum requirements under the DINA structure.

## 4. Relationship with Q verification and Q estimation

The identification condition answers "Is there a unique truth under infinite samples?" Q verification and Q estimation algorithms answer "How to find the truth under limited samples".

The logical order is:

\[
\text{identify}
\Longrightarrow
\text{There is a basis for consistent estimates}
\Longrightarrow
\text{Design specific optimization, Bayesian or search algorithms}.
\]

The establishment of identification does not guarantee that a certain numerical algorithm will converge quickly, nor does it guarantee a high recovery rate for small samples. If the recognition fails, multiple structures will appear giving the same overall distribution. Structural ambiguity cannot be eliminated by simply increasing the sample size.

## 5. Interface with previous articles on this site

- Liu, Xu & Ying (2012) focus on data-driven objective function and row-by-row search;
- Liu, Xu & Ying (2013) focus on the consistency condition of self-learning Q;
- Chen et al. (2018) uses a strong identifiable Q set as the Bayesian sampling space;
- This article tightens DINA's joint strict identification conditions into necessary and sufficient conditions, and further develops pan-identification.

Therefore, the “two sets of \(I_K\)” in Chen et al. (2018) are safe sufficient designs, and this paper shows that DINA strict identification can hold under weaker structures.
