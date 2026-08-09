# WebText: How the data is structured

## 1. Why not just use Common Crawl

The author needs a corpus with diverse fields, large scale, and relatively complete natural text. Common Crawl is large enough, but the original web page has navigation, templates, ads, garbled text, SEO text, and low-quality pages. If the data is completely filtered around a certain downstream task, task preferences will be revealed in advance.

WebText employs human crowd-filtered proxy signals: A link to a web page gets at least 3 karma on Reddit, indicating that at least some users think it's worth sharing or reading.

## 2. Build process

The process described in the paper can be written as:

```text
Reddit external link
   ↓ At least 3 karmas
~45 million links
   ↓ Download the external link page and do not use Reddit comments as the main text
HTML response
   ↓ Dragnet + Newspaper extracts text
text document
   ↓ Deduplication, heuristic cleaning, time truncation
WebText experimental version
```

The first version of the data used in the experiment meets:

- Excludes links created after December 2017;
- Slightly more than 8 million documents after deduplication and cleaning;
- Approximately 40 GB of text in total;
- In order to reduce overlap with common benchmarks, Wikipedia documentation has been actively removed.

## 3. Why does the data support the multi-tasking hypothesis?

A single news domain primarily teaches model news writing distribution. Cross-site corpora may also include:

- Tutorials and operating steps;
- Forum-style Q&A;
- bilingual citations;
- Article with TL;DR abstract;
- Dialogues and interviews;
- Tables, lists and semi-structured pages.

Different document formats mix multiple \(p(\text{output}\mid\text{input},\text{task})\) examples into the same training distribution.

## 4. Manually filter the signal bias

karma is not an objective label of text quality. It is affected by community demographics, interests, time of day, language, and platform rules. So WebText inherits:

- Selection bias between Reddit users and external link publishers;
- English Internet and American Center content bias;
- Popular topics are over-represented;
- Editorial and commercial biases of the linked website;
- Factual errors, stereotypes, and harmful text in the original page.

The official model card further explains that the source of WebText is the text of the external link page posted by Reddit users, which does not mean directly using the text on the Reddit site.

## 5. Verification difficulties caused by not making the data set public

GPT-2 officially released the model, code, output sample data set and WebText high-frequency domain name list, but did not release the complete WebText training set. It is difficult for researchers to completely reproduce:

- Specific crawl list;
- Extracted version of the page;
- Cleaning and deduplication rules;
- Each training sample;
- Complete audit of benchmark pollution.

Therefore, "the official code can run reasoning" and "the paper training process can be fully reproduced" are two different levels of judgment.

## 6. The relationship between WebText and model capabilities

The paper's causal claims require caution: the experiments simultaneously increase data size, diversity, number of model parameters, context length, and training computation. The existing design can show that the entire system improves with scale, but it is difficult to accurately break down the benefits into:

\[
\text{income}
=
\text{Data quality}
+
\text{Data diversity}
+
\text{Parameter scale}
+
\text{Optimization changes}
+
\text{Assessment format effect}.
\]

This also explains why subsequent scaling law, data ablation and pollution research have become independent directions.
