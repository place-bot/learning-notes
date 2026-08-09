# Condition C: At least three times for each attribute

## 1. Definition

\[
\sum_{j=1}^{J}q_{jk}\ge3,
\qquad
k=1,\ldots,K.
\]

Each attribute is required by at least three questions.

## 2. One measurement

If the attribute \(k\) appears in only one question, the information related to it is concentrated in a single Bernoulli indicator. Item parameters, attribute proportions, and Q structures can be continuously compensated, and the model cannot be locally recognized.

Theorem 2 first gives:

\[
\exists k:\sum_jq_{jk}=1
\quad\Longrightarrow\quad
\text{DINA does not have universal recognition}.
\]

## 3. Two measurements

The two-index mixed distribution corresponding to the two questions can sometimes be identified with the help of the dependency structure of other attributes, and sometimes there are still continuous substitution parameters. Therefore:

- Two measurements cannot guarantee strict identification;
- Two measurements can achieve universal recognition under a specific Q structure;
- The closer the parameters are to the null test set with independent attributes, the more unstable the finite sample estimation will be.

The four-question, two-attribute example fully demonstrates this boundary.

## 4. Intuition of three measurements

In a latent class model, a binary latent variable usually requires at least three conditional independence indicators to achieve stable separation:

```text
Attribute k
 ├── Question a
 ├── Question b
 └── Question c
```

The three sets of response probabilities provide sufficient high-order joint moments so that item parameters and mixing proportions cannot be arbitrarily interchanged.

## 5. Differences between DINA and general RLCM

At DINA:

- C is a necessary condition for strict identification;
- C In general recognition, you can press Theorem 2 to relax locally.

In general RLCM:

- Theorem 3 proves that C is a necessary condition for universal recognition;
- When only one or two questions appear for any attribute, infinite number of substitute objects can be constructed for any parameter.

Generally, the item parameters of RLCM are more free, and the special supplementary information brought by the conjunctive structure in DINA is no longer sufficient to ensure recognition.

## 6. Naming bias in official code

The main text of the paper is fixedly used:

- A = completeness；
- B = distinctness；
- C = repetition。

The official `check_Theorem1.m` annotation marks "at least three questions" as Condition B, and "\(Q^\star\) columns are mutually different" as Condition C. The actual Boolean calculation checks both items simultaneously, and the final combined value still corresponds to Theorem 1.

The output should be read based on the A/B/C names of the theorems in the paper.
