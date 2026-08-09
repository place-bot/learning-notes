# Q matrix and ideal response

## Equation 1

The deterministic input layer of DINA is

\[
\eta_{ij}
=
\prod_{k=1}^{K}
\alpha_{ik}^{q_{jk}}.
\tag{1}
\]

The original text uses \(Z_{ij}\), and this topic is also written as \(\eta_{ij}\) in order to unify it with subsequent CDM documents.

## How each factor works

Because \(q_{jk}\in\{0,1\}\):

\[
\alpha_{ik}^{q_{jk}}
=
\begin{cases}
1,&q_{jk}=0,\\
\alpha_{ik},&q_{jk}=1.
\end{cases}
\]

When the attribute \(k\) is not required, it contributes 1 to the product; when the attribute \(k\) is required, it contributes the student's mastery status to the product.

Therefore

\[
\eta_{ij}=1
\]

iff all properties satisfying \(q_{jk}=1\) have \(\alpha_{ik}=1\).

## Equivalent to the dot product condition

The required number of attributes is

\[
\boldsymbol q_j^\mathsf T\boldsymbol q_j
=
\sum_{k=1}^{K}q_{jk}.
\]

The required number of attributes a student has is

\[
\boldsymbol\alpha_i^\mathsf T\boldsymbol q_j.
\]

So

\[
\eta_{ij}=1
\iff
\boldsymbol\alpha_i^\mathsf T\boldsymbol q_j
=
\boldsymbol q_j^\mathsf T\boldsymbol q_j.
\tag{2}
\]

If the left side is smaller than the right side, at least one required attribute is missing, \(\eta_{ij}=0\).

## Fraction subtraction example

item requirements

\[
\boldsymbol q_j=(1,0,1,1,0).
\]

Compare four students:

|attribute profile \(\boldsymbol\alpha_i\)|Property 1|Property 3|Property 4| \(\eta_{ij}\) |
| --- | ---: | ---: | ---: | ---: |
| \((1,0,1,1,0)\) | 1 | 1 | 1 | 1 |
| \((1,1,1,0,1)\) | 1 | 1 | 0 | 0 |
| \((0,1,1,1,1)\) | 0 | 1 | 1 | 0 |
| \((1,0,1,1,1)\) | 1 | 1 | 1 | 1 |

Properties 2 and 5, which are not relevant to this question, do not affect the ideal state.

## Meaning of “AND gate”

Equation (1) is a Boolean AND:

\[
\eta_{ij}
=
\alpha_{i,k_1}
\land
\alpha_{i,k_2}
\land\cdots
\land
\alpha_{i,k_m},
\]

Among them, \(k_1,\ldots,k_m\) is the attribute required by the item.

If any of the required attributes is 0, the product is 0. This corresponds to noncompensation:

\[
\text{A mastered attribute cannot offset the absence of another required attribute}.
\]

## Information flow of paper Figure 1

The original image can be compressed into:

\[
\boldsymbol\alpha_i,\boldsymbol q_j
\longrightarrow
\eta_{ij}
\longrightarrow
\begin{cases}
g_j,&\eta_{ij}=0,\\
1-s_j,&\eta_{ij}=1
\end{cases}
\longrightarrow
X_{ij}.
\]

The first half is a deterministic cognitive gate; the second half adds random noise.

## Q Where will matrix errors flow?

If row Q omits an authentic problem-solving strategy, students who can use that strategy to answer the question correctly but do not master the attributes specified in Q will be placed

\[
\eta_{ij}=0.
\]

Their systematic success is absorbed by the model into \(g_j\). The original article specifically states that guess is a broad concept here, including alternative strategies not expressed by the Q matrix.

So the larger \(g_j\) may come from:

- Random guess;
- item clue;
- partial knowledge;
- alternative strategies;
- Q matrix error;
- Other model mismatches.

Parameter names alone cannot identify psychological processes.
