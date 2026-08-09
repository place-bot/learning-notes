# Symbol table, conclusion and reading map

## 1. Core symbols

|symbol|meaning|
|---|---|
| \(\mathbf x=(x_1,\ldots,x_{T_x})\) |Source sentence|
| \(\mathbf y=(y_1,\ldots,y_{T_y})\) |target sentence|
| \(\overrightarrow{\mathbf h}_j\) |Forward encoding status|
| \(\overleftarrow{\mathbf h}_j\) |Reverse encoding status|
| \(\mathbf h_j\) |Bidirectional source annotation|
| \(\mathbf s_i\) |Decoding status of target step \(i\)|
| \(e_{ij}\) |Unnormalized alignment score|
| \(\alpha_{ij}\) |Normalized weight of source location \(j\)|
| \(\mathbf c_i\) |current dynamic context|
| \(\mathbf z_i,\mathbf r_i\) | update/reset gate |
| \(\mathbf E_y[y]\) |target word embedding|
| \(\mathbf o_i\) |vocabulary logits|
| \(\mathcal L\) |negative log-likelihood|

## 2. Five core formulas

\[
p(\mathbf y\mid\mathbf x)
=
\prod_i p(y_i\mid y_{<i},\mathbf x)
\]

\[
\mathbf h_j
=
[\overrightarrow{\mathbf h}_j;
\overleftarrow{\mathbf h}_j]
\]

\[
e_{ij}
=
\mathbf v_a^\top
\tanh(\mathbf W_a\mathbf s_{i-1}+\mathbf U_a\mathbf h_j)
\]

\[
\alpha_{ij}
=
\frac{\exp(e_{ij})}{\sum_k\exp(e_{ik})}
\]

\[
\mathbf c_i
=
\sum_j\alpha_{ij}\mathbf h_j
\]

## 3. Algorithm Panorama

1. Bidirectional GRU encodes the source sentence into a list of contextualized annotations;
2. Calculate the additive score between the decoder old state and each annotation;
3. Masked softmax is used to obtain the source location distribution;
4. Weighted sum forms the current context;
5. Previous target word, old status and context update GRU;
6. deep output and maxout produce vocabulary probability;
7. Cross-entropy end-to-end update of reference target words for training;
8. Reasoning uses beam search approximation to find high probability sequences.

## 4. Core evidence of the paper

- Under the same length condition, RNNsearch is about 7–9 BLEU higher than the fixed vector baseline;
- The length grouping curve shows that RNNsearch is more robust to long sentences;
- RNNsearch-30 can exceed RNNencdec-50, indicating that increasing the training length does not eliminate the fixed vector bottleneck;
- Alignment heatmap shows similar word order, rearrangement and many-to-one patterns;
- The gap between No-UNK and the complete test set reveals the limitations of word-level closed vocabulary.

## 5. One sentence conclusion

Bahdanau, Cho, and Bengio advanced neural machine translation from "compressing the entire sentence at once" to "dynamically reading the source sentence for each generated word" and allowing the reading rules to be directly trained by translation loss.

## 6. Interface with the next paper

RNNsearch already has a query, source representation, normalized weights, and weighted reads, but the query comes from a recursive state. Vaswani et al. (2017)’s **Attention Is All You Need** goes further:

- Use self-attention to construct sequence representation;
- Replace additive score with scaled dot-product;
- Use multi-head to learn different relationships in parallel;
- Use positional encoding to compensate for the order;
- Remove RNN time step dependency in training.

Therefore, the next article should focus on observing how "dynamic reading" evolves into a complete sequence modeling skeleton.

## 7. Check back the entrance

- Mathematical mechanism: [Additive Attention](05-additive-attention.md)
- Gradient: [End-to-end training](06-end-to-end-training.md)
- Hand calculation: [Step by step hand calculation](09-worked-example.md)
- Experiment: [Experimental design](10-experiment-design.md) and [BLEU result](11-results-and-length-analysis.md)
-Code: [GroundHog intensive reading](13-groundhog-code-reading.md)
- Parallelization: [Complexity and Parallelization](15-attention-interpretation-and-complexity.md)
- Literature: [Reference](references.md)
