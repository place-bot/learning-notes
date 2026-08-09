# From complete reaction distribution to observable moments

## Response distribution given by candidate model

Let \(Q'\) represent any candidate matrix. For reaction mode \(\boldsymbol r\in\{0,1\}^J\),

\[
\Pr(\boldsymbol R=\boldsymbol r\mid Q',\boldsymbol p,\boldsymbol c,\boldsymbol g)
=
\sum_{\boldsymbol\alpha}
p_{\boldsymbol\alpha}
\prod_{j=1}^J
\pi_{j\boldsymbol\alpha}^{r_j}
(1-\pi_{j\boldsymbol\alpha})^{1-r_j}.
\tag{3}
\]

This is a mixture of Bernoulli product distributions with \(2^K\) latent classes.

## Empirical response distribution

\[
\widehat P(\boldsymbol r)
=
\frac1N\sum_{i=1}^N
\mathbf 1(\boldsymbol R_i=\boldsymbol r).
\tag{4}
\]

If Q and parameters are correct, the empirical distribution will approach the model distribution as \(N\) increases.

Using the complete reaction table directly requires processing \(2^J\) reaction patterns. There are 1,048,576 cells at the time of \(J=20\), and many cells are empty in the general sample. The paper instead uses low-order joint answer moments drawn from response distributions.

## Single question moment

For item \(j\),

\[
\beta_{\{j\}}
=
\frac1N\sum_{i=1}^N R_i^j.
\]

It is the sample correct answer rate.

## Question correct moment

\[
\beta_{\{j_1,j_2\}}
=
\frac1N\sum_{i=1}^N
R_i^{j_1}R_i^{j_2}.
\]

The product is equal to 1 only if both questions are answered correctly, so this is the combined correct answer rate for both questions.

## General question set

For non-empty item set \(A\subseteq\{1,\ldots,J\}\),

\[
\beta_A
=
\frac1N\sum_{i=1}^N
\prod_{j\in A}R_i^j.
\]

Stack all selected \(\beta_A\) into vector \(\boldsymbol\beta\) in a fixed order.

## Key distinction

\(\boldsymbol\beta\) is completely calculated by the response matrix and does not need to estimate the student's attribute profile. On the other hand, the model's predictions for the same batch of moments rely on \(Q'\), \(\boldsymbol c\), \(\boldsymbol g\) and \(\boldsymbol p\). Q-learning is driven by the gap between "sample moments" and "model moments".

## Why does the joint moment have additional information?

When looking only at the correct answer rate for a single question, attribute proportion, slipping, guessing and q-vector can compensate for each other. The structure of "which questions will be answered correctly by the same group of students" is added to the question pairs and higher-order moments, which can eliminate more errors Q. Increasing the order will bring stronger constraints and produce sparser and more unstable sample proportions.
