# NLP

Natural language processing studies how to convert text into computable representations, and complete prediction, generation, retrieval, reasoning and decision-making on these representations. The NLP section of this site is organized by "Representation Levels" and "Modeling Problems" rather than by software tools.

## Learn the main line

```text
discrete symbols
   │
   ├── tokenization and input encoding: BPE, Byte-level BPE, WordPiece
   │
   ├── Word and subvocabulary representation: Word2Vec, GloVe, fastText
   │
   ├── Contextual representation: ELMo, BERT and pretraining language model
   │
   ├── Sequence modeling: RNN, CNN, Transformer
   │
   ├── Task learning: classification, annotation, retrieval, generation
   │
   └── Evaluation and interpretation: similarity, transferability, bias and robustness
```

The learning route starts with understanding "how discrete words obtain vectors" from static word vectors, and then adds the subword tokenization layer from string to token ID; then enters the sequence-to-sequence model with attention, and connects to the Transformer which is completely based on attention. This allows us to see in turn how the input units are formed, how the model reads the source sentence in the generation step, and how the RNN's serial state chain is removed.

## Vocabulary representation with Word2Vec

### Mikolov et al. (2013)

[Efficient Estimation of Word Representations in Vector Space](word2vec-2013/index.md) proposes two efficient architectures: Continuous Bag-of-Words (CBOW) and Continuous Skip-gram. The core contributions of the paper include:

- Delete the computationally expensive nonlinear hidden layers in traditional neural language models;
- Use CBOW to predict the center word from context;
- Use Skip-gram to predict nearby words from the center word;
- Combined with hierarchical softmax on the Huffman tree, the output calculation is reduced from vocabulary scale to path length;
- Use semantic-syntactic analogy questions to systematically evaluate linear patterns in vectors;
- Prove that simple models, more corpus and higher-dimensional vectors can form strong vocabulary representations.

This paper is suitable as a starting point for NLP representation learning because it simultaneously connects language model, representation learning, comparative prediction goals, approximate normalization, scale training and representation evaluation.

## Subword tokenization

### BPE, Byte-level BPE and WordPiece

[Subword tokenization topic](subword-tokenization/index.md) explains how text is transformed from strings into token IDs that can be processed by the model, and distinguishes three routes that are often mixed:

- How the original BPE evolved from data compression to subword learning based on high-frequency pairs;
- GPT-2 How to construct byte-level BPE with reversible UTF-8 byte mapping;
- How BERT connects BasicTokenizer and WordPiece longest-match-first.

The topic completely explains the training algorithm, merge rank, WordPiece likelihood ideas, `Ġ` and `##`, hand calculation process, official code, offset mapping, multi-language efficiency and tokenizer evaluation. It also clearly states that BERT did not disclose the WordPiece vocabulary trainer that year, so the pair score reconstructed by the community will not be regarded as a public internal implementation.

## Neural Machine Translation and Attention

### Bahdanau, Cho & Bengio (2015)

[Neural Machine Translation by Jointly Learning to Align and Translate](bahdanau-attention-2015/index.md) For the long sentence bottleneck of fixed vector Encoder–Decoder, source position weights are recalculated for each target step:

\[
e_{ij}=a(\mathbf s_{i-1},\mathbf h_j),\qquad
\alpha_{ij}=\operatorname{softmax}_j(e_{ij}),\qquad
\mathbf c_i=\sum_j\alpha_{ij}\mathbf h_j.
\]

The topic fully explains bidirectional GRU, additive attention, end-to-end gradient, deep output, beam search, WMT14 experiments and GroundHog code, and has a special section to explain why the recursive dependence of RNN limits training parallelization.

## Transformer, pretraining and parameter efficient adaptation

|Topics|core issues|
|---|---|
| [Attention Is All You Need](transformer-2017/index.md) |How to use self-attention to remove positional recursion in RNN training|
| [LoRA](lora-2022/index.md) |How to efficiently adapt Transformer using low-rank increments|
| [BERT](bert-2019/index.md) |How to use MLM pretraining deep bidirectional Transformer encoder|

## Four representative documents corresponding to BERT terms

"First perform language modeling pretraining, and then fine-tuning for the task" involves different levels of abstraction. This site is expanded separately after BERT in the order specified by the user:

1. [transfer learning: Pan & Yang (2010)](transfer-learning-2010/index.md)
2. [Language modeling: Bengio et al. (2003)](neural-language-model-2003/index.md)
3. [pretraining: Dai & Le (2015)](sequence-pretraining-2015/index.md)
4. [fine-tuning: ULMFiT (2018)](ulmfit-2018/index.md)

## Autoregressive language model and dialogue alignment

From GPT-2 to GPT-3 and then to Llama 2, we can see three consecutive shifts in focus: first testing whether large-scale language models can be migrated with zero samples, then systematically studying in-context learning, and then advancing the focus to SFT, preference modeling and RLHF of open weight basic models.

1. [GPT-2：Language Models are Unsupervised Multitask Learners](gpt2-2019/index.md)
2. [GPT-3：Language Models are Few-Shot Learners](gpt3-2020/index.md)
3. [Llama 2：Open Foundation and Fine-Tuned Chat Models](llama2-2023/index.md)

## Model family and LLM software stack

In addition to the thesis route, two topics are responsible for establishing a horizontal map of modern model selection and system implementation:

|Topics|core issues|
|---|---|
|[Command R, Mistral, Phi and Llama](open-weight-model-families/index.md)|How to compare the architecture, positioning, deployment and open weight licenses of model families|
|[Transformers, llama.cpp and LangChain](llm-software-stack/index.md)|Which layer is responsible for the model library, inference runtime and application orchestration framework respectively?|

"Code is public", "weights are downloadable", "commercial use is allowed" and "complete training is reproducible" need to be judged separately. When introducing models on this site, we will implement precise checkpoints and licenses, and will not uniformly label "open source" by brand.

## LLM application panorama and book introduction

### Pai (2025)

["Designing Large Language Model Applications" special topic introduction](designing-llm-applications-2025/index.md) expands the route of a single paper into an end-to-end system map. The topic follows the three-layer structure of "where does the model come from - how to adapt and run - how to form an application", explaining pretraining data, vocabulary and tokenizer, architecture and learning goals, model selection, fine-tuning, alignment, inference optimization, tool calling, embedding, RAG and system architecture.

The discussion about tokenizer in the book is here as the entrance to the whole system: tokenization will simultaneously affect context budget, cross-language efficiency, latency, embedding and downstream data pipelines; the algorithm derivation and official code of BPE, Byte-level BPE and WordPiece are undertaken by [sub-word tokenization topic](subword-tokenization/index.md)]. The introduction also provides a separate mapping of the CAT scenario, explaining which layer of the system the real-time topic selection, status update, constraint checking and generation model are located at.

## Follow-up special interface

Subsequent papers can be accessed along the following relationships:

|direction|problem to be solved|representative method|
|---|---|---|
|Training target improvements|Full vocabulary normalization is still expensive| Negative Sampling、NCE |
|Intra-word substring features|Static word vectors lack morphological information| fastText |
|global co-occurrence|The relationship between local prediction and matrix factorization|GloVe, SGNS-PMI analysis|
|polysemy|There is only one static vector for each word|Multi-prototype word vector, context representation|
|context pretraining|The same word changes expression depending on the sentence| ELMo、BERT |
|modern sequence model|Long-distance dependencies and parallel computing| Transformer |

## Reading Convention

The topic will distinguish three types of evidence:

1. **Models and experiments clearly written in the paper**;
2. **Derivation directly developed from the formulas in the paper**;
3. **Follow-up work or public implementation details**.

This distinction is important. Taking Word2Vec as an example, the paper in January 2013 mainly used hierarchical softmax; the negative sampling, frequent word downsampling and phrase learning that are often bound to Word2Vec come from subsequent work in the same year.
