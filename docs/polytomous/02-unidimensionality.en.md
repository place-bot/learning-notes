# 2. Concept Supplement 1: Single-dimensional scale and local independence

## 2.1 What is Unidimensional Scale?

Unidimensionality (unidimensionality) means that all items jointly measure the same latent trait (latent trait). For example, all items in the scale try to measure "neuroticism".

In fact, if the subject's response pattern is driven by a single latent variable \(\theta\), the scale can be considered unidimensional.

### 2.1.1 Single dimension vs multi-dimensional

- **Single-dimensional scale**: All items measure the same \(\theta\) (such as "neuroticism").
- **Multidimensional scale**: There are multiple latent variables (such as "neuroticism" \(\theta_1\) and "extroversion" \(\theta_2\) acting together).

## 2.2 Formal representation

One-dimensional model:

\[
P(X_{ij} = 1 \mid \theta_j)
\]

Multidimensional model:

\[
P(X_{ij} = 1 \mid \mathbf{\theta}_j) = P(X_{ij} = 1 \mid \theta_{j1}, \theta_{j2}, \dots)
\]

Among them, \( X_{ij} \) represents the response of individual \( j \) to item \( i \).

## 2.3 Why is unidimensionality important?

- Most standard models of Item Response Theory (IRT) (such as 1PL, 2PL, GRM, PCM) **assume unidimensionality**
- If this assumption is violated (e.g. measuring multiple dimensions simultaneously), it will result in:
- Latent variable estimation bias
- item parameters are not interpretable
- Model fit decreases and test validity is impaired

## 2.4 How to verify unidimensionality

- **exploratory factor analysis (EFA)**: Test whether there is a dominant factor
- **Principal Component Analysis (PCA)**: Whether the contribution rate of the principal component is significantly higher than that of other components
- **Scree plot, parallel analysis** and other visualization methods
- Tests such as **Mokken scaling** and **DIMTEST** (used to diagnose underlying dimensional structure)

## 2.5 What is local independence (Local Independence)

Local independence means: **After controlling the latent variable, the item responses are independent of each other**.

The definition is as follows:

> For any subject \( j \), if its latent ability is \( \theta_j \), then for any two questions \( i \) and \( k \), there are:
>
> \[
> P(X_{ij}, X_{kj} \mid \theta_j) = P(X_{ij} \mid \theta_j) \cdot P(X_{kj} \mid \theta_j)
> \]

That is to say, under the premise that latent trait \( \theta_j \) is known, the subject's answer to item \( i \) will not affect the answer to item \( k \).

## 2.6 The relationship between local independence and unidimensionality

- Unidimensionality is a **necessary condition** for local independence, but it is not a sufficient condition
- If the scale is multi-dimensional, it will definitely destroy local independence
- Even if it is a single-dimensional scale, local independence may be violated if there are inter-item dependencies (such as repeated content, sequential guidance)

## 2.7 Examples

Suppose we design a 5-item neuroticism scale, and each question revolves around "anxiety, irritability, nervousness", etc.

- If each question only measures a single dimension of "neuroticism" and does not prompt or repeat each other, then scale can be regarded as a single dimension and locally independent
- If two of the questions mention "insomnia", the answer to one question may affect the other question, violating local independence.
- If some questions are actually measuring "depression" rather than "neuroticism", there may be an underlying multidimensional structure

## 2.8 Summary

|concept|definition|expression|
| --- | --- | --- |
|unidimensionality|All items jointly measure a latent variable| \( P(X_{ij} = 1 \mid \theta_j) \) |
|local independence|After controlling latent variables, item responses are independent of each other.| \( P(X_{ij}, X_{kj} \mid \theta_j) = P(X_{ij} \mid \theta_j) \cdot P(X_{kj} \mid \theta_j) \) |

Satisfying unidimensionality and local independence is the basic prerequisite for applying the IRT model.
