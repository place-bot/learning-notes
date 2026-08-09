# Soft alignment heat map and long sentence case

## 1. What is a heat map?

For each target position \(i\) and source position \(j\), the model produces \(\alpha_{ij}\). All weights are composed of

\[
\mathbf A=[\alpha_{ij}]
\in\mathbb R^{T_y\times T_x}.
\]

The sum of each row is 1, which represents the distribution of the position of the source sentence when generating a target word. Figure 3 of the paper uses light and shade to represent weights, with white close to 1 and black close to 0.

## 2. Diagonal and reordering

Fragments with similar English and French word orders will form a roughly diagonal line. When internal rearrangement of phrases is encountered, the bright area will deviate from the diagonal. For example, the paper shows the correspondence between "European Economic Area" and the French phrase "zone économique européenne", and the weight trajectory reflects the order changes of adjectives and nouns.

## 3. One-to-many and many-to-one

The paper also shows that “the man” corresponds to a situation like “l’homme”. A target word can read information from multiple source locations at the same time; the same source location can also be repeatedly accessed in multiple target steps. Soft alignment naturally allows this allocation.

## 4. Long sentence case

The appendix of the paper compares multiple long sentence translations. The fixed vector baseline often misses or distorts details after about 30 words, and RNNsearch is better at maintaining entities, modification relationships, and the content of the second half of the sentence. This corroborates with the BLEU curves grouped by length.

Cases are qualitative evidence. It helps understand model behavior, cannot replace complete test set statistics, and may also be affected by the author's selection of examples.

## 5. What judgments can heat maps support?

Heatmaps can be used to observe:

- The actual normalized weight used in the current forecast;
- Whether the weights are concentrated, dispersed or in a rearrangement pattern;
- Whether different target steps read different source locations;
- Whether padding is correctly blocked;
- Models may appear to be duplicated or skipped.

## 6. Explain boundaries

A high weight means that the model forward calculation gives a larger coefficient to that annotation. It is not necessarily equal to:

- Manually annotated unique word alignment;
- The complete causal contribution of this input to the final prediction;
- Performance changes after removing the word;
- Cognitive attention in human translation.

The reason is that the annotation itself already contains context, there are other information paths to the state, and there is interaction between the parameters and the representation. Heatmaps are valuable internal computational records that need to be combined with ablations, gradients, counterfactual perturbations, and human evaluation.

## 7. Commonly used diagnostic quantities

Attention entropy at each goal step:

\[
H(\boldsymbol\alpha_i)
=
-\sum_j\alpha_{ij}\log\alpha_{ij}.
\]

Low entropy means the distribution is concentrated, and high entropy means it is scattered. The amount of coverage can be written as

\[
\operatorname{coverage}_j
=
\sum_i\alpha_{ij}.
\]

The original paper did not use an explicit coverage mechanism to constrain it; subsequent work will use accumulated attention to reduce missed translations and repeated translations.

## Summary of this page

Aligned heatmaps turn the internal weights of dynamic contexts into an observable matrix. It provides direct mechanistic evidence that the model reads different source regions at each step, while requiring caution in handling its scope of interpretation.
