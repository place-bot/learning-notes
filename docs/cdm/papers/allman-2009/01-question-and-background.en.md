# Problem and theoretical background

## What exactly is the paper asking?

Suppose a model generates the observable data distribution \(P_\theta\) with parameters \(\theta\). identifiability research parametric mapping

\[
\Psi:\Theta\longrightarrow\mathcal M_1(\Omega),
\qquad
\Psi(\theta)=P_\theta
\]

Can it be solved in reverse? Here:

- \(\Theta\) is the parameter space;
- \(\Omega\) is the observation sample space;
- \(\mathcal M_1(\Omega)\) is the set of all probability measures on \(\Omega\);
- \(P_\theta\) is the overall distribution determined by parameter \(\theta\).

Identifiability assumes that the population distribution is known accurately, and then asks whether the parameters are unique. It precedes the finite sample estimation problem:

\[
\text{identifiable}
\quad\Longrightarrow\quad
\text{Parameters are likely to be consistently estimated};
\]

\[
\text{Unrecognizable}
\quad\Longrightarrow\quad
\text{Even if the sample size tends to infinity, some parameter values cannot be distinguished}.
\]

The accuracy of estimation under limited samples also depends on the amount of information, algorithm, sample size and model settings. Identifiable only deals with "whether there is a unique answer at the overall level".

## Four common identification concepts

### Strictly identifiable

Strict identifiable requirements

\[
P_\theta=P_{\theta'}
\quad\Longrightarrow\quad
\theta=\theta'.
\]

That is, \(\Psi\) is a one-to-one mapping.

### Differential label replacement can be identified

Models with discrete latent classes suffer from inevitable label renaming. If

\[
Z\in\{1,\ldots,r\},
\]

Replacing all class proportions and class conditional distributions simultaneously does not change the observed distribution. For example, swap categories 1 and 2:

\[
(\pi_1,M_1(1,\cdot),\ldots)
\longleftrightarrow
(\pi_2,M_1(2,\cdot),\ldots).
\]

The paper considers "unique except for common label permutations" as strict identification enough. If there is a \(r\) class, pure label exchange corresponds to \(r!\) equivalent parameter representations.

### Partially identifiable

Local identifiability only requires that there is no second equivalent parameter point within a neighborhood of \(\theta\). There may still be another set of parameters further away that produces the same distribution. Under common regular conditions, local identification is related to the non-singularity of the Fisher information matrix, but local conclusions cannot automatically give global uniqueness.

### Universally identifiable

Generic identifiability allows a set of exceptions defined by polynomial equations. Set

\[
\mathcal V
=
\{\theta:f_1(\theta)=\cdots=f_m(\theta)=0\}
\]

is a proper algebraic subvariety in parameter space. if all
\(\theta\in\Theta\setminus\mathcal V\) can be recognized, and the model can be recognized universally.

In a finite-dimensional parameter space, the Lebesgue measure of a true algebraic subvariety is 0. Therefore, the universally identifiable expression is:

> Parameters at general locations can be recovered; some degenerate, symmetric or boundary parameter points may still fail.

This conclusion does not guarantee that the numerical estimates near the exception set are stable. Although the parameter point is not on the exception set, if it is very close to it, the finite sample problem may still be seriously ill-posed.

## Why algebraic language is suitable

The observation probability of a finite latent class model is a polynomial in the parameters. Taking two dichotomous observation variables as an example,

\[
P(X_1=x_1,X_2=x_2)
=
\sum_{i=1}^{r}
\pi_i
P(X_1=x_1\mid Z=i)
P(X_2=x_2\mid Z=i).
\]

Each joint probability is the sum of the products of \(\pi_i\) and the conditional probabilities. The decrease in matrix rank is equivalent to some subexpressions being 0, so failure situations such as "insufficient rank" and "two reaction contours coincide" can be written as polynomial equations.

The logic used in the paper is:

1. Write the full rank condition required for identification as certain determinants are non-zero;
2. Find at least one parameter point such that these determinants are non-zero;
3. Explain that the relevant polynomial is not always equal to 0;
4. Their zero point sets are true algebraic subvarieties;
5. Therefore, the full rank condition holds at general parameter points.

## Four types of models covered by the paper

|model|latent structure|conditional independence structure|Main result|
| --- | --- | --- | --- |
|Finite State Multiplicative Distribution Mixing|Single finite latent class \(Z\)|Given \(Z\), each observed variable is independent|Universal identifiability of multivariable finite latent class models|
|Discrete HMM|Potential Markov chain \(Z_t\)|Given the intermediate state, the left and right observation blocks and the current observation can be separated|Identifying HMM parameters from finite length marginal distributions|
|random graph mixture|Each node has a latent class|Each edge is independent given all node categories|Two-node category model identifies with enough nodes|
|Non-parametric multiplicative distribution mixture|Finite mixture class, component distribution non-parametric|At least three observation blocks are independent after a given category|Strict identification under linear independence conditions|

The unified action of the paper is to find three observation blocks that are independent under appropriate latent variable conditions.

## The paper clearly fixes what

### latent class number \(r\) known

When Kruskal decomposition is used throughout the text, it is assumed that the latent class number \(r\) is known. Identifying the number of classes is another model selection problem in itself. If the wrong \(r\) is used during fitting, the theorem in this article cannot guarantee parameter interpretation.

### Category ratio is positive

Finite potential class results usually require

\[
\pi_i>0,\qquad i=1,\ldots,r.
\]

When \(\pi_i=0\), the \(i\) class completely disappears from the overall distribution, and its conditional reaction parameters naturally cannot be recovered.

### Local independence or constructible conditional independence

The basic model directly requires

\[
X_1,\ldots,X_p\ \perp\!\!\!\perp\ \text{given } Z.
\]

The observed variables of HMM and random graphs are generally dependent on each other, but the paper makes the three merged observation blocks conditionally independent by retaining appropriate composite latent variables.

## Why this paper is relevant to CDM

Standard bisection CDM is often written as

\[
P(\boldsymbol Y=\boldsymbol y)
=
\sum_{\boldsymbol\alpha\in\mathcal A}
\nu_{\boldsymbol\alpha}
\prod_{j=1}^{J}
\theta_{j,\boldsymbol\alpha}^{y_j}
(1-\theta_{j,\boldsymbol\alpha})^{1-y_j},
\]

Among them:

- \(\boldsymbol\alpha\) is attribute mastery profile;
- \(\mathcal A\) is the set of allowed attribute profiles;
- \(\nu_{\boldsymbol\alpha}\) is the attribute profile ratio;
- \(\theta_{j,\boldsymbol\alpha}=P(Y_j=1\mid\boldsymbol\alpha)\)。

Temporarily treating each \(\boldsymbol\alpha\) as an unnamed latent class, this formula is a finite mixture of Bernoulli product distributions. The result of Allman et al. can therefore support the first level of recovery:

\[
P(\boldsymbol Y)
\longrightarrow
\{\nu_{\boldsymbol\alpha},\theta_{j,\boldsymbol\alpha}\}
\quad\text{up to class labels}.
\]

CDM will also continue to explain why these classes correspond to a certain set of attributes, which items measure which attributes, and why the response probability obeys DINA or G-DINA constraints. This information is not included in the parameter naming of general latent class models.

## The most important method contribution of this article

The value of a paper is not just a set of sample size upper bounds. What's more important is a transferable proof route:

\[
\text{conditional independence graph structure}
\rightarrow
\text{three composite observed variables}
\rightarrow
\text{class conditional probability matrix}
\rightarrow
\text{Kruskal rank condition}
\rightarrow
\text{Parameter identification}.
\]

Subsequent RLCM and CDM identifiability papers often borrow the idea of "three blocks + full rank", and then use Q matrix constraints to eliminate label and structural ambiguities still retained by general latent class models.

