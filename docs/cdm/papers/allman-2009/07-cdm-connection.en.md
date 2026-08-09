# Interface with CDM identifiability

## Translate general latent classes into CDM

Suppose the test measures \(K\) binary attributes. attribute profile is

\[
\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_K)
\in\{0,1\}^K.
\]

The set of allowed attribute profiles is denoted by

\[
\mathcal A\subseteq\{0,1\}^K,
\]

Its size is

\[
r=|\mathcal A|.
\]

For item \(j\), define

\[
\theta_{j,\boldsymbol\alpha}
=
P(Y_j=1\mid\boldsymbol\alpha).
\]

Under the assumption of local independence,

\[
P(\boldsymbol Y=\boldsymbol y)
=
\sum_{\boldsymbol\alpha\in\mathcal A}
\nu_{\boldsymbol\alpha}
\prod_{j=1}^{J}
\theta_{j,\boldsymbol\alpha}^{y_j}
(1-\theta_{j,\boldsymbol\alpha})^{1-y_j}.
\tag{CDM-LCM}
\]

After treating each attribute profile as a latent class:

|Allman Papers| CDM |
| --- | --- |
| \(Z=i\) |attribute profile \(\boldsymbol\alpha\)|
| \(r\) |Number of allowed attribute profiles \(|\mathcal A|\) |
| \(\pi_i\) | \(\nu_{\boldsymbol\alpha}\) |
| \(X_j\) |item response \(Y_j\)|
| \(M_j(i,\cdot)\) | \((1-\theta_{j,\boldsymbol\alpha},\theta_{j,\boldsymbol\alpha})\) |
|conditionally independent|CDM items are partially independent|

## First level: restore unconstrained conditional response

If there are three suitable items and satisfy the rank condition, the Allman route can be obtained

\[
P(\boldsymbol Y)
\longrightarrow
\left\{
\nu_{\boldsymbol\alpha},
\theta_{j,\boldsymbol\alpha}
\right\}
\quad
\text{up to an unknown common row permutation}.
\tag{Stage 1}
\]

What is restored at this time is an unnamed potential class response probability table. For example, when \(K=2\), theoretically four lines are obtained, but it is not known which line corresponds to it.

\[
(0,0),(0,1),(1,0),(1,1).
\]

## Second level: interpret these lines using CDM structure

CDM identification also needs to be proven

\[
\left\{
\nu_{\boldsymbol\alpha},
\theta_{j,\boldsymbol\alpha}
\right\}
\longrightarrow
\left\{
Q,\ \boldsymbol\alpha,\ \text{item parameters}
\right\}.
\tag{Stage 2}
\]

This step depends on the specific model.

### DINA

The Q vector of item \(j\) is

\[
\boldsymbol q_j=(q_{j1},\ldots,q_{jK}).
\]

ideal response indicator

\[
\eta_{j,\boldsymbol\alpha}
=
\prod_{k=1}^{K}\alpha_k^{q_{jk}}
\]

It is 1 when all the attributes required by the item are mastered. DINA response probability is

\[
\theta_{j,\boldsymbol\alpha}
=
(1-s_j)^{\eta_{j,\boldsymbol\alpha}}
g_j^{1-\eta_{j,\boldsymbol\alpha}},
\]

Equivalently,

\[
\theta_{j,\boldsymbol\alpha}
=
\begin{cases}
1-s_j,&\eta_{j,\boldsymbol\alpha}=1,\\
g_j,&\eta_{j,\boldsymbol\alpha}=0.
\end{cases}
\]

Allman's theorem can help recover the \(\theta\) table, but recovering \(\boldsymbol q_j,g_j,s_j\) from this table requires:

- attribute profile rows can be named structurally;
- The high and low response probability groups in the item can correspond to \(\eta\);
- The Q matrix has sufficient completeness and repeated measurements;
- Parameters satisfy constraints that distinguish mastered from unmastered, such as \(1-s_j>g_j\).

### G-DINA

G-DINA models the main effect and interaction of the required attributes of the item:

\[
P(Y_j=1\mid\boldsymbol\alpha)
=
\delta_{j0}
+
\sum_k\delta_{jk}\alpha_kq_{jk}
+
\sum_{k<\ell}
\delta_{jk\ell}
\alpha_k\alpha_\ell q_{jk}q_{j\ell}
+\cdots.
\]

Generally, the latent class layer recovers the response probability under each attribute profile. G-DINA also identifies which effects are present, which attributes the Q row contains, and whether the parameterization is unique.

## Why the generic conclusion of the general space cannot be directly restricted to CDM

Assume that the general latent class parameter space is \(\Theta_{\mathrm{LCM}}\), and the DINA parameter space is embedded in it through constraint mapping:

\[
\Theta_{\mathrm{DINA}}
\subset
\Theta_{\mathrm{LCM}}.
\]

Allman result says bad set

\[
\mathcal V\subset\Theta_{\mathrm{LCM}}
\]

The measure is 0 in general space. may still occur

\[
\Theta_{\mathrm{DINA}}\subseteq\mathcal V.
\]

A low-dimensional structured subspace may fall exactly within the set of exceptions to the general space. It is therefore necessary to re-prove full rank in the CDM's own parameter space or to exploit additional structures to establish identification.

This is also an important task for subsequent RLCM identification papers.

## Q matrix manufacturing row duplication

If two attribute profiles \(\boldsymbol\alpha\) and \(\boldsymbol\alpha'\) have the same ideal response for all items,

\[
\eta_{j,\boldsymbol\alpha}
=
\eta_{j,\boldsymbol\alpha'},
\qquad
j=1,\ldots,J,
\]

Under DINA they satisfy

\[
\theta_{j,\boldsymbol\alpha}
=
\theta_{j,\boldsymbol\alpha'}
\quad\forall j.
\]

The complete reaction profiles of the two classes are then the same and only the sum of the proportions can be identified

\[
\nu_{\boldsymbol\alpha}
+
\nu_{\boldsymbol\alpha'}.
\]

This problem will ultimately be solved by the Q matrix's ability to distinguish attribute profiles.

## Structural zero ratio

If the attribute hierarchy makes certain patterns impossible, then

\[
\nu_{\boldsymbol\alpha}=0
\]

holds for these patterns. Allman's hypothesis of positive class proportions does not allow treating zero-proportion classes as identifiable existing classes.

A more reasonable approach would be to

\[
\mathcal A
=
\{\boldsymbol\alpha:\nu_{\boldsymbol\alpha}>0\}
\]

Treat it as an actual set of potential classes and then study:

1. Is \(\mathcal A\) known?
2. Can it be recovered from the data;
3. Whether the hierarchical relationship can be inferred from \(\mathcal A\);
4. Whether Q is still identifiable on a restricted set of categories.

This connects to attribute profile learning, attribute hierarchy and sparse latent class models.

## Tag replacement is more complex in CDM

Ordinary latent class models only care about the names of class 1 and class 2. CDM labels contain multiple meanings:

- Which \(\boldsymbol\alpha\) does the potential class row correspond to;
- The order of attribute coordinates;
- Which skill does the Q matrix column correspond to?
- How a certain skill tag corresponds to content expert interpretation.

Even if the latent class table is restored, there may still be attribute column permutations:

\[
(Q,\boldsymbol\alpha)
\mapsto
(QP,P^\top\boldsymbol\alpha),
\]

Where \(P\) is the attribute dimension permutation matrix. Statistical distributions may remain unchanged, but attribute names such as “algebra” and “geometry” in educational explanations require external content anchoring.

## Impact on continuous-Q and partial mastery

### continuous-Q

If the Q elements are relaxed from \(\{0,1\}\) to continuous weights, the structural constraints of the itemresponse probability change. As long as the latent attribute profile remains discrete, the model can still be written as a limited latent class mixture first, but the second-stage mapping after general latent class recovery may be more difficult to unique.

### partial mastery

If each attribute mastery degree is continuous,

\[
\boldsymbol a\in[0,1]^K,
\]

Latent variables are no longer finite categories. Corollary 5 cannot be used directly. Identification tools that require continuous latent variables, nonparametric mixtures, integral transformations, or specific response functions.

Theorem 8's non-parametric mixing result still assumes a finite number of mixing components, but the component distribution in each observation direction is non-parametric; it is not equivalent to a continuous attribute distribution.

## The appropriate place for this paper in the CDM proof

The identification argument can be organized into three steps:

\[
\boxed{
P(\boldsymbol Y)
\overset{\text{Three pieces of full rank}}{\longrightarrow}
\text{Unnamed latent class response table}
}
\]

\[
\boxed{
\text{response table}
\overset{\text{Q and model constraints}}{\longrightarrow}
\text{attribute profile, item structure and parameters}
}
\]

\[
\boxed{
\text{statistical structure}
\overset{\text{Content anchoring}}{\longrightarrow}
\text{Interpretable attribute names}
}
\]

Mainly supporting the first step, Allman et al. CDM specialized papers complete the second step, and expert review and test content design support the third step.

## Follow-up intensive reading chain

|Follow-up paper|Issues to be corrected|
| --- | --- |
| Kruskal (1977) |How to prove the three-way decomposition uniqueness theorem itself and how to understand the conditions|
| Xu (2017) |How does bipartite RLCM use three conditions to establish identifiability?|
|Gu & Xu: DINA identification|Sufficient and necessary conditions for DINA parameters|
| Gu & Xu (2021) |When is the Q matrix itself identifiable?|
| Xu & Shang (2018) |How latent structures and restricted latent classes are jointly recovered|
| Chen et al. (2015/2017) |Estimation, regularization, and finite sample behavior of Q structures and latent classes|

