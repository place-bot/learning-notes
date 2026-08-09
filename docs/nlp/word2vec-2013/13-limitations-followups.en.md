# Limitations, follow-up work and modern location

## 1. Static single vector limit

There is only one vector per word type:

\[
w\mapsto\mathbf v_w.
\]

Polysemy mixes different contexts. For example, the riverbank meaning and financial meaning of `bank` jointly update a representation. High frequency meanings usually dominate and low frequency meanings may be diluted.

Subsequent multi-prototype embedding and contextualized representation allow:

\[
(w,\text{context})\mapsto\mathbf h_{w,\text{context}}.
\]

## 2. Limited word order information

CBOW directly averages the context, and the forward result is consistent when the same bag of words is arranged. Skip-gram predicts each context word separately and does not explicitly encode the left, right and precise distance.

The model can learn syntactic rules indirectly through co-occurrence distribution, but it cannot represent the complete sequence structure. Skip-gram individual sentence completion in Table 7 is weaker than RNNLM, showing this limitation.

## 3. Vocabulary and OOV

The model looks up the table with complete word types:

- Words that did not appear in training have no vectors;
- The estimation of low-frequency words is noisy;
- Missing parameter sharing for spelling changes, inflections and compound words;
- Vocabulary expansion increases memory.

fastText later uses character n-grams to combine word vectors, which can share morphological information and construct representations for some unregistered words.

## 4. Multi-vocabulary

The analogy set in this article excludes a type of multi-word entity `New York`. Word-wise vector addition makes it difficult to express uncombinable phrases, such as proper names or idioms.

A subsequent paper in the same year proposed discovering phrases based on co-occurrence statistics, and then training the phrase as a single token, such as `New_York`.

## 5. Boundary of analogy evaluation

Analogy accuracy is affected by:

- Manual selection of relational word pairs;
- Capitalization, tokenization and vocabulary coverage;
- Strict top-1 exact matching;
- Synonyms and multiple reasonable targets;
- Candidate spatial density;
- High-frequency entities and data aging;
- Category size imbalance;

influence. High analogy accuracy should be used with word similarity, downstream tasks, cross-domain transfer, and human analysis.

## 6. Experimental reproducibility

The paper lacks common features found in modern experimental reports:

- Multiple random seed statistics;
- Complete corpus cleaning details;
- Downloadable Google News 6B training text;
- Accurate hardware and energy consumption;
- Unified training budget for all compared models;
- confidence interval and significance test.

Exposing the code, problem sets, and subsequently released pretraining vectors improves usability, but does not allow full reconstruction of all training conditions.

## 7. Corpus bias and privacy

News corpus encodes social stereotypes and uneven co-occurrences. Static vectors compress these patterns into neighbors and directions, which may then be propagated to recruitment, retrieval, recommendation, or classification systems.

Large-scale corpus crawling also involves:

- Personal information and copyright;
- Domain and language representation;
- time drift;
- harmful content;
- Transparency of data sources.

This article does not cover these issues. Modern applications must add data governance and presentation bias assessment.

## 8. Follow-up NIPS 2013 paper

Mikolov et al.'s **Distributed Representations of Words and Phrases and their Compositionality** extends the Skip-gram.

### 8.1 Negative Sampling

For the true center-context pair \((i,o)\), the target is

\[
\log\sigma(\mathbf u_o^\top\mathbf v_i)
+\sum_{k=1}^{K}
\mathbb E_{w_k\sim P_n}
\log\sigma(-\mathbf u_{w_k}^\top\mathbf v_i).
\]

The model improves the true pair score and reduces the sampled noise word score. Only \(K+1\) output word vectors are accessed at each step.

### 8.2 High-frequency word downsampling

Extremely high frequency function words generate a large number of repeated training pairs. Randomly discarding a portion of tokens according to frequency can:

- Reduce calculations;
- Reduce the dominance of high-frequency words on targets;
- Let word pairs with higher information content receive greater relative weight.

### 8.3 Phrases

Discover phrases based on the co-occurrence intensity of combined words, treat a type of expression like `New_York` as a single word element, and then train the vector.

These three improvements are often seen together with "Word2Vec", but they are follow-up papers and should not overwrite the contributions of this initial model.

## 9. From Word2Vec to subsequent representation learning

### 9.1 GloVe

GloVe explicitly uses global word-context co-occurrence counts to bridge predictive methods and matrix factorization perspectives.

### 9.2 fastText

fastText represents vocabulary as the sum of character n-gram vectors, improving morphologically rich languages, low-frequency words and unregistered words.

### 9.3 ELMo and BERT

The contextual model allows the same token to obtain different vectors in different sentences. The training goal extends from local static word prediction to deep bidirectional sequence representation.

### 9.4 Modern large language model

Modern models still rely on embedded lookup tables, dot product predictions, shared parameters, and large-scale self-supervised data. The "learning representation from scale with a simple prediction task" demonstrated by Word2Vec is still one of the core ideas, but the representation unit, model capacity and context range have been greatly expanded.

## 10. Original paper reproduction and modern baseline

If the research goal is historical recurrence, you should use:

- CBOW or Skip-gram;
- Huffman hierarchical softmax；
- Original text window, dimension, epoch and learning rate;
- Original analogy evaluation rules.

If the research goal is to establish a practical static word vector baseline, you can also report:

- SGNS；
- CBOW + negative sampling；
- fastText；
- GloVe；
- Input vectors, output vectors and their combinations;
- Multiple random seeds and downstream tasks.

The two types of experiments answer different questions, and the results should be presented in separate tables.

## 11. Future research questions

Following the logic of this article, you can continue to ask:

1. How to express polysemy while maintaining efficiency?
2. How to make the window include direction, distance and syntactic structure?
3. How to deal with cross-linguistic, morphological and sub-word information?
4. How to build more reliable evaluations of representations that do not rely on a single set of analogies?
5. How to separate the contributions of corpus size, model structure and computational budget?
6. How to detect and control embedded social bias?
7. What cost advantages do static word vectors still have in retrieval, educational text, and small data tasks?

## 12. Historical location

The importance of this paper comes from the combination of three things:

- Minimalist local prediction target;
- Extensible training mechanism;
- Computable relationship evaluation.

It advances neural vocabulary representations from relatively expensive language model by-products to basic representations that can be independently trained and widely reused.
