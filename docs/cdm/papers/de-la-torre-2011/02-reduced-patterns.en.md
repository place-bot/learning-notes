# Reduced attribute profile and partial ordering

## Complete attribute profile

Assume that the test has \(K\) attributes in total, and the complete attribute profile is

\[
\boldsymbol\alpha_l
=
(\alpha_{l1},\ldots,\alpha_{lK})^\top,
\qquad
\alpha_{lk}\in\{0,1\}.
\]

The index \(l\) points to one of the \(2^K\) latent classes. The mode here is latent class layer object without student index.

## item only reads the attributes in the Q line

Q matrix elements

\[
q_{jk}=
\begin{cases}
1,&\text{item}j\text{Requires attributes}k,\\
0,&\text{item}j\text{No attributes required}k.
\end{cases}
\]

The number of required attributes for item \(j\) is

\[
K_j^*=\sum_{k=1}^{K}q_{jk}.
\]

Take the components of \(q_{jk}=1\) from the complete pattern to form a reduced attribute profile

\[
\boldsymbol\alpha^*_{lj}.
\]

For example,

\[
\boldsymbol q_j=(1,0,1,0),
\qquad
\boldsymbol\alpha_l=(1,1,0,1)
\]

given

\[
\boldsymbol\alpha^*_{lj}=(1,0).
\]

The second and fourth attributes do not affect the response probability of the item.

## From \(2^K\) class to \(2^{K_j^*}\) group

If \(K=5\), but the item only requires attributes 1 and 4, then the 32 complete categories will only form four groups for the item:

\[
(0,0),(1,0),(0,1),(1,1).
\]

This step is called latent-class-to-latent-group mapping. It explains two computational facts simultaneously:

- Step E still needs to calculate the posterior on the complete attribute space;
- When updating an item in M steps, it only needs to be summarized into the reduced group of the item.

## Partial ordering of attribute profile

Thesis definition

\[
\boldsymbol\alpha^*_{lj}
\preceq
\boldsymbol\alpha^*_{l'j}
\]

If and only if each component satisfies

\[
\alpha_{lk}\leq\alpha_{l'k}.
\]

If at least one component is strictly less than, then write

\[
\boldsymbol\alpha^*_{lj}
\prec
\boldsymbol\alpha^*_{l'j}.
\]

This relationship means that the latter contains all the attributes mastered by the former, and masters at least one more attribute.

## "The number of 1's is more" cannot replace partial ordering

compare

\[
(0,0,1)
\quad\text{and}\quad
(1,1,0).
\]

The second pattern contains two 1's and the first contains one 1, but they are not comparable:

\[
(0,0,1)\npreceq(1,1,0),
\]

Because the third attribute changed from 1 to 0.

Therefore, simply sorting according to the number of attributes mastered will lose the information of "which attributes are mastered".

## Monotonic constraints

Saturated G-DINA in its most general form allows

\[
P(\boldsymbol\alpha^*_{lj})
>
P(\boldsymbol\alpha^*_{l'j})
\quad
\text{Even if}
\boldsymbol\alpha^*_{lj}\prec\boldsymbol\alpha^*_{l'j}.
\]

The paper explains a possible situation: those who have mastered some attributes may stably choose a strong interference item, while those who have not mastered it at all make random guesses, and the latter has a higher success rate.

Many educational applications still impose monotonicity:

\[
P(\boldsymbol\alpha^*_{lj})
\leq
P(\boldsymbol\alpha^*_{l'j})
\quad
\text{whenever }
\boldsymbol\alpha^*_{lj}\prec\boldsymbol\alpha^*_{l'j}.
\]

Monotonicity is an additional substantive assumption that cannot be deduced automatically from the G-DINA form.
