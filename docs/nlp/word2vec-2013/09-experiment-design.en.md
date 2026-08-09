# Experimental design, data and comparison framework

## 1. Experimental problem map

The experiments in the paper can be divided into six groups:

|research questions|Corresponding evidence|
|---|---|
|How do data volume and dimensionality jointly affect accuracy?| Table 2 |
|Who is stronger, CBOW, Skip-gram, NNLM or RNNLM?| Table 3 |
|Can new models outperform public word vectors?| Table 4 |
|What is the trade-off between looking at more new data and repeating epochs?| Table 5 |
|What level can distributed large-scale training achieve?| Table 6 |
|Can word vectors help with sentence completion tasks?| Table 7 |

Table 8 shows several relationship outputs for qualitative observations.

## 2. Main evaluation set

The Semantic-Syntactic Word Relationship data set contains:

- 5 types of semantic questions, 8,869 questions in total;
- 9 types of syntax questions, a total of 10,675 questions;
- 19,544 questions in total.

Each question uses the vector difference to construct a query, and the accuracy is calculated based on the full vocabulary cosine top-1 exact hit. Table 3 also reports Microsoft Research's syntactic word relatedness test set.

## 3. Google News corpus

The Google News corpus used for main training in this paper contains approximately

\[
6\text{B tokens}.
\]

Maximum vocabulary is limited to the most common

\[
1\text{M words}.
\]

Tables 2, 4, and 5 use different subsets of this corpus; Table 6 uses the full 6B data.

## 4. Table 2: Data volume × dimension

### 4.1 Model

- Architecture: CBOW;
- Vocabulary: 30K high-frequency words;
- Dimensions: 50, 100, 300, 600;
- Training word elements: 24M, 49M, 98M, 196M, 391M, 783M;
- epoch：3；
- Optimization: SGD + backpropagation;
- Initial learning rate: 0.025, linearly decreasing to close to 0.

### 4.2 Scope of evaluation

Only four words are retained, all of which belong to the 30K high-frequency vocabulary analogy problem. This allows you to compare model capabilities while fixing the set of computable items under a small vocabulary.

### 4.3 Experimental design

Here is a grid experiment for \(4\times6\) to observe:

\[
\text{Accuracy}=f(D,T).
\]

The author focuses on the respective marginal benefits of data volume and dimensionality, as well as the effect of simultaneous expansion of both.

## 5. Table 3: Comparison of the same data and same dimension architecture

### 5.1 Training data

The training set consists of several LDC corpora:

\[
T=320\text{M words},
\qquad V=82\text{K}.
\]

### 5.2 Common dimensions

All models use 640-dimensional word vectors to reduce representation capacity differences.

### 5.3 Model

- RNNLM: The previously trained recurrent neural language model, which takes about 8 weeks to train on a single CPU;
- NNLM: 640 hidden units, history length 8, trained by DistBelief;
- CBOW；
- Skip-gram。

### 5.4 Indicators

- Semantic accuracy of the newly created analogy set;
- Syntactic accuracy of newly created analogy sets;
- MSR syntactic relatedness test set。

This comparison is closest to schema ablation since the data and dimensions are fixed. The number of model parameters, optimization method and historical structure are still not exactly the same.

## 6. Table 4: Public vectors and new models

Comparison includes:

- Collobert–Weston NNLM；
- Turian NNLM；
- Mnih NNLM；
- Mikolov RNNLM；
- Huang NNLM；
- NNLM trained by the author;
- CBOW；
- Skip-gram。

The training corpus for these models ranges from 37M to 6B, with dimensions ranging from 20 to 640. Table 4 shows the comprehensive performance of the actual available models, but the model structure, corpus, dimensions and training budget change at the same time and cannot be regarded as a single-factor causal comparison.

Both CBOW and Skip-gram use 300 dimensions, 783M words, and are trained for 3 epochs. The authors report single CPU training times of approximately 1 day and 3 days respectively.

## 7. Table 5: epoch, data and dimensions

Author comparison:

1. 783M words training 3 epoch;
2. 783M words training 1 epoch;
3. 1.6B word training 1 epoch;
4. 783M words, 600 dimensions, training 1 epoch.

The goal is to determine near a fixed time:

- Repeat the same data;
- See more different data;
- Expand the representation dimension;

Which way is more effective.

All 1-epoch experiments also linearly decrease the learning rate to close to 0.

## 8. Table 6: DistBelief distributed training

### 8.1 Settings

- Corpus: Google News 6B;
- CBOW / Skip-gram dimension: 1,000;
- NNLM dimension: 100;
- Training framework: DistBelief;
- Optimization: mini-batch asynchronous gradient descent + AdaGrad;
- Model copies: 50–100;
- Number of CPU cores: about 125–180, usage will fluctuate.

### 8.2 Time Record

The paper reports approximate resources as "number of days × number of CPU cores". Data center machines take on other tasks at the same time, the number of cores is an estimate, and the distribution overhead also reduces the difference in CPU usage between CBOW and Skip-gram.

## 9. Table 7：Microsoft Sentence Completion Challenge

The task consists of 1,040 sentences, each missing a word, and given 5 reasonable candidates. The model needs to choose the candidate that is most coherent with the entire sentence.

Skip-gram settings:

- Dimensions: 640;
- Training corpus: 50M words provided by the task;
- For each candidate, place the candidate in the missing position;
- Use candidates as input to predict surrounding words in the sentence;
- Add the individual prediction scores together as the sentence score.

Final comparison of 4-gram, LSA, log-bilinear, RNNLM, Skip-gram, and weighted combination of Skip-gram and RNNLM.

## 10. Table 8: Relationship example

The author uses the best Skip-gram model with 300 dimensions and 783M words in Table 4 to show:

- country—capital;
- Comparative form of adjectives;
- city-state;
- Character—occupation;
- Politicians - countries;
- element—symbol;
- Company—Product;
- Company—Person;
- Country—Food.

The authors point out that only about 60% of these examples would score as a strict exact match, and the display table contains several outputs that are semantically related but do not meet the unique target.

## 11. Main controls and confounds in experiments

|compare|Better control|Still changing factors|
|---|---|---|
| Table 2 |architecture, vocabulary, epoch|Data volume and dimensions|
| Table 3 |Training data, dimensions|Architecture, Optimization and Parameter Sizing|
| Table 4 |same evaluation set|Almost all training factors|
| Table 5 |Architecture and Evaluation Set|Data volume, dimension, epoch, time|
| Table 6 |Corpus and framework|Architecture, dimensions, resources|

Therefore, the strongest evidence in the paper comes from consistent trends and order-of-magnitude differences, rather than strict randomized control or statistical significance analysis in the modern sense.

## 12. Records that need to be supplemented to reproduce

The original article does not have a complete report:

- All random seeds;
- Variance repeated multiple times;
- Detailed tokenization and cleaning process;
- Exact hardware model for each experiment;
- Complete parameter quantities for all models;
- coverage rate for each category;
- hyperparameter search scope.

Modern reproductions should complete these and report accuracy, OOV coverage, throughput, total computation, and peak memory simultaneously.
