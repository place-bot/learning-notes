# Word2Vec Original paper: CBOW, Skip-gram and efficient vocabulary representation

This topic focuses on the paper **Efficient Estimation of Word Representations in Vector Space** by Tomas Mikolov, Kai Chen, Greg Corrado and Jeffrey Dean.

The scale of the paper is billions of words, millions of vocabulary, and vectors of hundreds to thousands of dimensions. The research question can be condensed into one sentence:

> How to learn high-quality word vectors from extremely large corpus under limited computing budget?

## Read the paper with a picture

```text
Large-scale text corpus
      │ Sliding context window
      ▼
Center words and context words in training samples
      │
      ├── CBOW: Aggregation of multiple context vectors ──► Predict the center word
      │
      └── Skip-gram: Center word vector ─────► Predict multiple nearby words
                              │
                              ▼
                 Huffman hierarchical softmax
                              │
                              ▼
                    Continuous vector for each word
                              │
             ┌────────────────┴───────────────┐
             ▼                                ▼
       Cosine Neighbors and Analogy Downstream NLP Tasks
```

## Citation details

|item|information|
|---|---|
|Author| Tomas Mikolov、Kai Chen、Greg Corrado、Jeffrey Dean |
|meeting| ICLR 2013 Workshop Poster |
| arXiv | [1301.3781](https://arxiv.org/abs/1301.3781) |
|Initial submission|January 16, 2013|
|Current version|v3, September 7, 2013|
|Official paper page| [Google Research](https://research.google/pubs/efficient-estimation-of-word-representations-in-vector-space/) |

## The real main line of the paper

This article is often summarized as "two word vector models", but the main line of argument in the full article consists of four steps:

1. Traditional NNLM and RNNLM can learn word vectors, but the hidden layer and large vocabulary output layer cause high computational costs.
2. After removing the nonlinear hidden layer, the calculation of each training sample drops significantly.
3. The saved budget can be exchanged for more training tokens, higher vector dimensions, and larger vocabulary.
4. The scaled-up simple model outperforms the more complex baseline on the semantic-syntactic analogy task.

Therefore, the value of CBOW and Skip-gram comes from the combination of "target design + structural simplification + data scale".

## Original text scope

The paper explicitly discusses:

- Training complexity \(O=E\times T\times Q\);
- Complexity of feedforward NNLM, RNNLM, CBOW and Skip-gram;
- Huffman hierarchical softmax；
- Distributed DistBelief training;
- Semantic-syntactic analogy data set;
- 8 experimental tables and their results;
- Microsoft Sentence Completion Challenge；
- Several examples of word vector relationships.

The paper does not fully describe the probability objectives and gradients of CBOW and Skip-gram. The topic will complete the derivation based on the model description and hierarchical softmax mechanism in the article, and clearly mark these expansions.

## Recommended reading route

### First time: first establish model intuition

1. [Problems, Citation details and innovation](01-paper-question-and-contributions.md)
2. [Distributed vocabulary display base](02-distributed-representations.md)
3. [CBOW: Predict the center word](05-cbow.md) from context
4. [Skip-gram: Predict context](06-skip-gram.md) from center words
5. [Analog evaluation and vector operation](08-analogy-evaluation.md)

### The second time: thorough calculation and training

1. [Computational complexity and neural language model baseline](03-complexity-and-baselines.md)
2. [Huffman Hierarchical Softmax](04-hierarchical-softmax.md)
3. [SGD, backpropagation and complete algorithm](07-training-algorithm.md)
4. [Public code and minimum implementation](12-code-and-implementation.md)

### The third time: judging the strength of evidence

1. [Experimental design and data](09-experiment-design.md)
2. [Experimental results and analysis](10-results-and-analysis.md)
3. [The meaning and boundaries of linear laws](11-linear-regularities.md)
4. [Limitations, follow-up work and modern location](13-limitations-followups.md)
5. [Symbol table, conclusion and reading map](14-symbols-conclusion.md)

## You should be able to explain after reading

- The difference between one-hot numbering and distributed representation;
- Why removing hidden layers brings orders of magnitude computational savings;
- What conditional probabilities do CBOW and Skip-gram construct respectively?
- How does Huffman tree decompose a \(V\) problem into several binary categories;
- Why are the input word vector and the output node vector two sets of parameters;
- How the dynamic window changes the sampling frequency of far and near contexts;
- How to construct analogy questions and how to determine hits;
- Table 2–6 shows what conclusions are supported respectively;
- Why negative sampling should not be included in the original goal of this paper;
- What are the limitations of static word vectors in terms of polysemy, word order, morphology and social bias.
