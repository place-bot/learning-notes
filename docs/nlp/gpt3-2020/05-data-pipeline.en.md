# Training data, filtering and mixed sampling

## 1. Five types of data

GPT-3 uses filtered Common Crawl, WebText2, two books corpora and English Wikipedia.

|Data set|Number of available tokens|Training Mixed Weights|The epochs passed when training 300B tokens|
|---|---:|---:|---:|
|Common Crawl (after filtering)| 410B | 60% | 0.44 |
| WebText2 | 19B | 22% | 2.9 |
| Books1 | 12B | 8% | 1.9 |
| Books2 | 55B | 8% | 0.43 |
| Wikipedia | 3B | 3% | 3.4 |

Weights in the table are rounded to a total of 101%. The core idea is that high-quality small corpus is oversampled, and Common Crawl and Books2 do not traverse a complete round.

## 2. Common Crawl scale changes

Supplementary material gives:

```text
41 Common Crawl monthly shards from 2016–2019
        ↓
~45 TB compressed plain text
        ↓ Quality filtering, blurring and deduplication
Approximately 570 GB
        ↓ byte-level BPE
About 400B token
```

The final training only samples about 180B tokens from the filtered Common Crawl, accounting for 60% of the 300B training tokens.

## 3. Quality classifier

The author uses curated corpora such as WebText, Wikipedia and books as positive examples, unfiltered Common Crawl as negative examples, and uses Spark tokenizer, HashingTF and logistic regression to train the quality classifier.

Each document gets `document_score`, and then a random resampling rule is used to retain high-scoring documents first and a small amount of out-of-distribution text. The Pareto parameters given in the supplementary material are

\[
\alpha=9.
\]

This method does not simply cut the Common Crawl to a fixed score threshold, but forms a probabilistic sampling that is biased toward high quality.

## 4. Fuzzy deduplication

The authors used Spark MinHashLSH, 10 hashes, to remove highly similar documents within each dataset and between datasets, and to obfuscate WebText from Common Crawl. The average data size dropped by approximately 10%.

Deduplication goals include:

- Reduce the training weight of repeated samples;
- Reduce validation leakage;
- Ease model memory;
- Maintain data diversity.

## 5. Mixed sampling is not at original scale

If sampled entirely by token number, Common Crawl will overwhelm the rest of the corpus. The paper artificially increases the weight of WebText2, Books and Wikipedia, which is equivalent to accepting high-quality corpus to be seen repeatedly in exchange for better average training quality.

The training distribution can be written as a mixture model:

\[
p_{\mathrm{train}}(x)
=
\sum_{m=1}^{5}w_m p_m(x),
\qquad
\sum_m w_m\approx1.
\]

\(w_m\) is the sampling weight chosen by the researcher and is not a natural distribution on the Internet.

## 6. Language distribution

The paper estimates that the training data by word count is about 93% English and 7% non-English. The byte-level BPE is designed from the English center, so although multilingual texts can be encoded, token efficiency and model performance are still uneven.

## 7. Data bias

The official model card states that the Internet training data is more representative of the connected population and biased toward developed, young, affluent, male, and U.S.-centric views. The filtering classifier will also regard "similar to existing curated corpora" as a quality criterion, further solidifying the cultural and stylistic preferences of the reference corpus.

## 8. Evidence boundaries for data pipelines

The official repository releases language statistics, samples, and partial overlap records, but does not release the complete training corpus, quality classifier model, and reproducible data list. Therefore, external readers cannot understand the method and cannot accurately reconstruct every training token.
