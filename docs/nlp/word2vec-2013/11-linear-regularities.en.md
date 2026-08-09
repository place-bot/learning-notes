# The meaning and boundaries of linear rules

## 1. Relationship as displacement vector

If the word pair \((a,b)\) expresses a certain relationship, it can be expressed as a difference:

\[
\mathbf r_{a\rightarrow b}
=\mathbf v_b-\mathbf v_a.
\]

When two word pairs have similar relationships, it is expected that

\[
\mathbf v_b-\mathbf v_a
\approx
\mathbf v_d-\mathbf v_c.
\]

Move the terms to get the analogy query:

\[
\mathbf v_d
\approx
\mathbf v_b-\mathbf v_a+\mathbf v_c.
\]

Geometrically, this requires that the two difference value vectors are roughly parallel and of similar length.

## 2. The relationship between the paper Table 8

Table 8 shows the Skip-gram vector using 300 dimensions and 783M training words:

|Relationship example|corresponding word of launch|
|---|---|
| France → Paris | Italy → Rome；Japan → Tokyo；Florida → Tallahassee |
| big → bigger | small → larger；cold → colder；quick → quicker |
| Miami → Florida | Baltimore → Maryland；Dallas → Texas；Kona → Hawaii |
| Einstein → scientist | Messi → midfielder；Mozart → violinist；Picasso → painter |
| Sarkozy → France | Berlusconi → Italy；Merkel → Germany；Koizumi → Japan |
| copper → Cu | zinc → Zn；gold → Au；uranium → plutonium |
| Berlusconi → Silvio | Sarkozy → Nicolas；Putin → Medvedev；Obama → Barack |
| Microsoft → Windows | Google → Android；IBM → Linux；Apple → iPhone |
| Microsoft → Ballmer | Google → Yahoo；IBM → McNealy；Apple → Jobs |
| Japan → sushi | Germany → bratwurst；France → tapas；USA → pizza |

The table also contains results that clearly correspond, are approximately related, and clearly deviate from the target. The authors note that only about 60% of these presentation examples would have scored using the strict exact match rules of the analogy set.

## 3. Why linear structures may appear

This article does not give a formal theorem for linear laws. Three intuitions can be derived from the training objectives.

### 3.1 Shared output decision surface

In Skip-gram, each input word vector produces a correct score for a large number of output nodes. Words with similar context distribution need to give similar results on many shared decision surfaces, so the vectors tend to be close.

### 3.2 Systemic context changes

If changing from singular to plural systematically changes the context distribution, multiple word pairs may receive gradient changes with similar structures, forming an approximate common direction.

### 3.3 Low-dimensional compression

A large number of co-occurrence patterns are compressed into \(D\)-dimensional space. The most stable and repeated changing factors tend to form reusable directions.

These explanations give mechanistic intuitions and do not guarantee that each type of linguistic relation corresponds to a unique linear direction.

## 4. Average of relationship direction

A single word pair difference contains individual semantics. For example

\[
\mathbf v_{\text{Paris}}-\mathbf v_{\text{France}}
\]

It also includes factors such as capital relations, geographical themes, and news frequency. Average multiple examples:

\[
\overline{\mathbf r}
=\frac{1}{K}\sum_{k=1}^{K}
(\mathbf v_{b_k}-\mathbf v_{a_k}),
\]

It can weaken the noise unique to word pairs and preserve the common relationship. The paper reports an absolute improvement of about 10 percentage points in accuracy when reporting \(K=10\).

## 5. Coordinate axes have no fixed semantics

If the same orthogonal transformation \(R\) is applied to all vectors:

\[
\mathbf v'_w=R\mathbf v_w,
\qquad R^\top R=I,
\]

Then the dot product, cosine and Euclidean distances hold:

\[
(R\mathbf a)^\top(R\mathbf b)
=\mathbf a^\top\mathbf b.
\]

Analog differences are also rotated overall:

\[
R(\mathbf v_b-\mathbf v_a+\mathbf v_c).
\]

Therefore, the model can rotate coordinates without changing geometric relationships. Naming the 17th dimension as "gender dimension" and the 42nd dimension as "country dimension" usually lacks uniqueness; subspace and direction comparisons are more secure.

## 6. Relationships don’t have to be one-way

The same label may contain multiple sub-relationships:

- Irregular past tense and regular past tense;
- National and state capitals;
- Biological sex, social roles and grammatical gender;
- Company founders, CEOs, products and competitors.

A global difference direction may only approximately cover part of it. The outputs such as `uranium → plutonium` and `Google → Yahoo` in Table 8 reflect the bias between correlation and precise relationship.

## 7. Density problem of cosine nearest neighbors

Analogical evaluation relies on fully vocabulary nearest neighbors. High frequency words, vector space anisotropy, and "hubness" can make a few words become close neighbors to many queries. Even if the relationship vector is reasonable, the nearest neighbor search may be affected by local density.

Common follow-up treatments include:

-Mean centralization;
- Remove high-variance principal components;
- Use alternative analog scores such as 3CosMul;
- Local density correction;
- Combine input and output vectors.

None of these methods are part of the original experiments of this article.

## 8. Linear analogy and language understanding

Analogical hits illustrate that certain statistical relationships in the training corpus form stable geometric structures in vector space. It does not directly prove model mastery:

- The truth of the facts;
- Combination semantics;
- Event cause and effect;
- The specific meaning of the word in the context;
- Complete grammar of new sentences.

In Table 7, the Skip-gram single sentence completion accuracy is 48.0%, which is lower than RNNLM's 55.4%, which just shows that strong word relationships and strong sequence models have different capabilities.

## 9. The corpus bias will enter the geometric space

Word vectors learn co-occurring structures in corpus. Social stereotypes, historical inequalities, news coverage bias, and field distribution will all be written into the proximity and relationship direction. Vector arithmetic can amplify these patterns.

Therefore, when deploying word vectors you should evaluate:

- Neighbors of words from different groups;
- Differences in the association of occupational, emotional and ability words;
- Source and time of corpus;
- sensitivity of downstream models to these directions;
- Information loss caused by debiasing methods.

This article was published in 2013 and no system fairness audit was conducted.

## 10. The accurate use of the word "algebra"

The paper demonstrates addition and subtraction operations and nearest neighbor retrieval in vector space. The relations satisfy approximate parallelism rather than establishing a closed algebraic system of word meanings. A more accurate statement is:

> Certain semantic and syntactic relations appear as approximately consistent linear displacements in the learned embedding space.

This is already a very important discovery and preserves the scope of the evidence itself.
