# Theorem 2: Three structures when only measured twice

## 1. Standard form

Suppose attribute 1 is required by exactly two questions. After row-column replacement,

\[
Q=
\begin{pmatrix}
1&\boldsymbol0^\top\\
1&\boldsymbol v^\top\\
\boldsymbol0&Q^\star
\end{pmatrix},
\]

Among them

\[
\boldsymbol v\in\{0,1\}^{K-1},
\qquad
Q^\star\in\{0,1\}^{(J-2)\times(K-1)}.
\]

The first question only measures attribute 1; the second question measures both attribute 1 and other attributes specified by \(\boldsymbol v\); the remaining questions do not measure attribute 1.

## 2. The attribute only appears once

\[
\exists k:\sum_jq_{jk}=1
\]

DINA does not have universal recognition. This attribute is continuously interchangeable with the parameters of the unique item.

## 3. Case (a)：\(\boldsymbol v=\boldsymbol1\)

The second question requires attribute 1 and all other attributes:

\[
\boldsymbol q_2=(1,1,\ldots,1).
\]

The conclusion is that the model does not even support local general recognition. There are infinitely many sets of equivalent parameters in any small neighborhood of true parameters.

Intuitively, the second question only enters the ability state in the full mastery latent class, and it is difficult to separate the independent contribution of attribute 1 from the proportion of the full mastery class.

## 4. Case (b)：\(\boldsymbol v=\boldsymbol0\)

The first two questions are single-attribute questions for attribute 1. Any of the following conditions can guarantee global pan-recognition:

### (b.1)

\(Q^\star\) satisfies A/B/C of Theorem 1 for the remaining \(K-1\) properties.

### (b.2)

\(Q^\star\) includes two sets

\[
I_{K-1}.
\]

This conclusion covers four questions and two attribute examples. At this time, \(Q^\star\) contains two unit questions for a single remaining attribute.

## 5. Case (c)：\(\boldsymbol v\ne\boldsymbol0,\boldsymbol1\)

The second question only connects a proper subset of the remaining attributes. If \(Q^\star\) satisfies A/B/C, the model is locally identifiable.

The paper only gives local conclusions because the proof requires excluding extra branches in the true parameter neighborhood, and the global uniqueness of the entire parameter space has not yet been established.

## 6. Zero test set condition

The identifiable parameters of Case (b) require the existence of two remaining sets of attribute configurations such that

\[
p_{\boldsymbol\alpha^1}
p_{\boldsymbol\alpha^2+\boldsymbol e_1}
\ne
p_{\boldsymbol\alpha^2}
p_{\boldsymbol\alpha^1+\boldsymbol e_1}.
\]

The equal sign defines an unrecognizable algebraic set. \(K=2\) degrades to

\[
p_{00}p_{11}=p_{01}p_{10}.
\]

## 7. How to use Theorem 2

```text
Count 1 for each column
   │
   ├── Column ≤ 1: General recognition failed
   ├── All columns ≥ 3: Go to Theorem 1
   └── A certain column = 2
          │
          ├── Rearrange into standard form and read v
          ├── v=1: Local general recognition failed
          ├── v=0: Check (b.1)/(b.2)
          └── Others v: Check A/B/C of Q* and get local conclusions
```
