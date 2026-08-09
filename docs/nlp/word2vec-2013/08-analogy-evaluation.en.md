# Analogy evaluation and vector operations

## 1. From neighbor display to relationship testing

Early word vector papers often showed several nearest neighbors of a word. This kind of display makes it easy to select favorable examples and makes it difficult to compare models. This article establishes a batch analogy test to convert relationship preservation capabilities into repeatable top-1 accuracy.

Given two word pairs

\[
(a,b),\qquad(c,d),
\]

Assume that both express the same relationship:

\[
a:b::c:d.
\]

Model construction query vector

\[
\mathbf q
=\mathbf v_b-\mathbf v_a+\mathbf v_c,
\]

Then find the word with the largest cosine similarity:

\[
\widehat d
=\arg\max_{w\in\mathcal V\setminus\{a,b,c\}}
\operatorname{cos}(\mathbf v_w,\mathbf q).
\]

If \(\widehat d=d\), the question is recorded as a hit.

## 2. Example

### 2.1 Superlative

\[
\mathbf q
=\mathbf v_{\text{biggest}}
-\mathbf v_{\text{big}}
+\mathbf v_{\text{small}}.
\]

If the nearest word is `smallest`, explain

\[
\mathbf v_{\text{biggest}}-\mathbf v_{\text{big}}
\approx
\mathbf v_{\text{smallest}}-\mathbf v_{\text{small}}.
\]

### 2.2 Country—Capital

\[
\mathbf q
=\mathbf v_{\text{Paris}}
-\mathbf v_{\text{France}}
+\mathbf v_{\text{Italy}},
\]

If the nearest word is `Rome`, then the difference from country to capital is approximately parallel on these two word pairs.

## 3. Why exclude three input words?

The query vector is usually highly similar to \(a\), \(b\), \(c\) itself. Without excluding them, nearest neighbor may directly return an input word, making it impossible to measure relationship transfer. Therefore, the first three words are removed from the candidate set.

## 4. 14 types of relationships

Table 1 of the paper contains 5 types of semantic relations and 9 types of syntactic relations:

|Group|relationship category|Word pair example 1|Word pair example 2|
|---|---|---|---|
|Semantics| common capital city | Athens–Greece | Oslo–Norway |
|Semantics| all capital cities | Astana–Kazakhstan | Harare–Zimbabwe |
|Semantics| currency | Angola–kwanza | Iran–rial |
|Semantics| city-in-state | Chicago–Illinois | Stockton–California |
|Semantics| man–woman | brother–sister | grandson–granddaughter |
|syntax| adjective to adverb | apparent–apparently | rapid–rapidly |
|syntax| opposite | possibly–impossibly | ethical–unethical |
|syntax| comparative | great–greater | tough–tougher |
|syntax| superlative | easy–easiest | lucky–luckiest |
|syntax| present participle | think–thinking | read–reading |
|syntax| nationality adjective | Switzerland–Swiss | Cambodia–Cambodian |
|syntax| past tense | walking–walked | swimming–swam |
|syntax| plural nouns | mouse–mice | dollar–dollars |
|syntax| plural verbs | work–works | speak–speaks |

"Semantics" and "Syntax" in the category tags are groupings of papers. Some categories involve simultaneously world knowledge, named entities, and morphological changes, and the boundaries are not purely linguistic.

## 5. How to generate questions

For each category, a list of word pairs with consistent relationships is first manually established, and then two different word pairs are combined to form a question.

If a category has \(m\) directed word pairs, theoretically it can form an approximate

\[
m(m-1)
\]

A directed combination. The paper takes 68 American cities and their states as an example, which generates approximately 2.5K questions after combination.

Public `questions-words.txt` There are:

\[
8{,}869\ \text{a semantic question}
+10{,}675\ \text{syntax question}
=19{,}544\ \text{questions}.
\]

## 6. Strict top-1 accuracy

The overall accuracy is

\[
\operatorname{Accuracy}
=\frac{1}{M}
\sum_{m=1}^{M}
\mathbb I(\widehat d_m=d_m).
\]

The paper uses strict string matching:

- Only the nearest word that is exactly the same as the target word is counted as a hit;
- Synonyms will also be counted as errors;
- Multi-word entities are not included because the test set only retains single tokens;
- The current model has no explicit word structure, so reaching 100% is difficult.

## 7. OOV and denominator

If any word \(a,b,c,d\) is not in the model vocabulary, the problem cannot be calculated. Public `compute-accuracy.c` skips these questions and also reports:

```text
Questions seen / total
```

Therefore, when reproducing the experiment, you should also record:

\[
\text{coverage}
=\frac{\text{Countable number of questions}}{\text{Total number of questions}},
\]

and accuracy on computable problems. Reporting only accuracy may mask the coverage loss caused by small vocabulary.

Table 2 clearly uses only four words in the 30K high-frequency vocabulary problem; subsequent tables use the full model vocabulary.

## 8. Normalization and retrieval

The public evaluation code first normalizes each word vector:

\[
\widetilde{\mathbf v}_w
=\frac{\mathbf v_w}{\lVert\mathbf v_w\rVert_2}.
\]

The query vector is

\[
\mathbf q
=\widetilde{\mathbf v}_b
-\widetilde{\mathbf v}_a
+\widetilde{\mathbf v}_c.
\]

Then calculate \(\mathbf q^\top\widetilde{\mathbf v}_w\). Whether the query vector is renormalized does not change the candidate ranking, because it only provides the same proportional factor for all candidates.

## 9. A hand calculation example

Let the normalized two-dimensional vector be

\[
\mathbf v_a=(0.8,0.6),\quad
\mathbf v_b=(0.6,0.8),\quad
\mathbf v_c=(1,0).
\]

The query vector is

\[
\mathbf q
=(0.6,0.8)-(0.8,0.6)+(1,0)
=(0.8,0.2).
\]

The two candidates are

\[
\mathbf v_d=(0.97,0.24),
\qquad
\mathbf v_e=(0.3,0.95).
\]

The number of points is

\[
\mathbf q^\top\mathbf v_d
=0.824,
\qquad
\mathbf q^\top\mathbf v_e
=0.430.
\]

Model selection \(d\). This calculation only compares the directional similarity and does not require that \(\mathbf q\) itself is exactly equal to a certain word vector.

## 10. Multi-instance relationship vector

Differences between individual word pairs can be noisy. Given \(K\) example relationships, average:

\[
\mathbf r
=\frac{1}{K}
\sum_{k=1}^{K}
(\mathbf v_{b_k}-\mathbf v_{a_k}).
\]

The new query is

\[
\mathbf q=\mathbf v_c+\mathbf r.
\]

The paper reports that after using 10 examples to form the relationship vector, the best model's accuracy on the semantic-syntactic test increased by about 10 percentage points in absolute terms. This suggests that averaging of relationship directions can reduce single-word pair noise.

## 11. What can evaluation indicate?

This task directly measures the following properties:

- Whether the word vector difference can be consistent across multiple word pairs;
- Whether the target word can become the top-1 nearest neighbor in the entire vocabulary;
- Ability to transfer relationships between semantic and syntactic categories.

It cannot be proven alone:

- Vectors are suitable for all downstream tasks;
- The model understands the complete meaning of the word;
- Linear relationships cover all linguistic phenomena;
- High accuracy equivalent to human language understanding.

The paper uses it as a quantifiable proxy for representation quality and supplements task-level evidence on the Microsoft Sentence Completion Challenge.
