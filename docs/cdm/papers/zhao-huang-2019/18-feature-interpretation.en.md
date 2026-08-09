# Keyword result and educational semantic explanation

## 1. High-frequency selected words of unigram

List of papers:

- “a bunch of”；
- “figure”；
- “integers”；
- “sum”。

The original item is in Chinese, and the paper explains the keywords in English. The author points out translation difficulties and therefore does not list the complete key vocabulary of bigram/trigram.

## 2. Author’s explanation

“A bunch of” and “figure” are more commonly used in Mathematical thinking questions that describe a longer situation and require understanding of the situation.

“integers” and “sum” appear more often in Operations of integers questions that directly perform addition and subtraction operations.

can be written as:

\[
\text{Long situational/graphic prompts}
\Rightarrow M,
\]

\[
\text{direct arithmetic terms}
\Rightarrow O.
\]

## 3. The model may learn two types of signals

### 3.1 Target construct signal

Words do point to required cognitive activities such as integers, sums, relations, and graphs.

### 3.2 Question type or writing style signal

Long questions are more likely to be classified as M by experts, and short questions are more likely to be classified as O. A classifier might primarily identify:

- text length;
- Template sentences;
- The wording used by the person who asked the question;
- Source of question type.

This type of signal can improve the random division score of the same item bank, but may not be stable across item banks.

## 4. Keyword explanation cannot automatically establish construct validity

Description of high mutual information:

\[
I(X_r;Y)>0.
\]

It does not demonstrate that there is a causal relationship between the word and the attribute, nor does it prove that students actually use the corresponding skills when solving problems.

## 5. Template leak

If the same template only replaces numbers:

```text
Xiao Ming has 12 books and bought 5 more. How many books are there in total?
Xiaohong has 18 pens and bought 7 more pens. How many pens are there in total?
```

Random splitting by item can place near-duplicate templates in both the training and test sets. The model may memorize phrases such as `bought more / in total`, thereby inflating test performance.

A more rigorous approach would be to group them by template or question family.

## 6. How to check feature validity

It is recommended to do at the same time:

1. List the top positive and negative features of each category;
2. Report word frequency and mutual information;
3. Marked by experts as “concept-related/template-related/potential leakage”;
4. Delete obvious label words and retrain;
5. Control the length of the question stem;
6. Evaluate on the new source item bank.

## 7. Inspiration for today

Modern language models can encode longer semantics and context. Keyword analysis remains valuable because it provides a low-cost audit layer:

```text
language model prediction
      │
      ├── Attribute probability
      └── Interpretable phrases/pieces of evidence
```

Experts can use this to determine whether the model relies on reasonable evidence.
