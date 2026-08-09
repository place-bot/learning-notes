# Reading comprehension, summary, translation and Q&A results

## 1. Winograd Schema Challenge

The model compares two analytic probabilities of ambiguous reference. GPT-2 reports an accuracy of 70.70%, which is 7 percentage points higher than the previous results listed in the paper.

The data set has only 273 samples, and a single sample accounts for approximately

\[
\frac{1}{273}\approx0.366\%
\]

accuracy. A few samples will change the conclusion, so the paper also reminds readers to combine small sample uncertainty and data set analysis to understand the result.

## 2. CoQA Reading Comprehension

Input is document, conversation history and last `A:`. Greedy decoding gets 55 F1 in development set:

- Matches or exceeds 3 of the 4 supervised baselines listed in the paper;
- No parameter update using more than 127,000 CoQA training question-answer pairs;
- Still significantly lower than the BERT supervised system and human level which is close to 89 F1.

Error analysis found that the model often relied on shallow retrieval, for example, when seeing `who`, it retrieved a person's name from the document. F1 improvement does not directly demonstrate the development of robust multi-step reading comprehension.

## 3. CNN/Daily Mail Summary

|method| ROUGE-1 | ROUGE-2 | ROUGE-L |average|
|---|---:|---:|---:|---:|
| Bottom-Up Sum | 41.22 | 18.68 | 38.34 | 32.75 |
| Lede-3 | 40.38 | 17.66 | 36.62 | 31.55 |
| Seq2Seq + Attention | 31.33 | 11.81 | 28.83 | 23.99 |
| GPT-2 + `TL;DR:` | 29.34 | 8.27 | 26.58 | 21.40 |
| Random-3 | 28.78 | 8.63 | 25.52 | 20.98 |
|GPT-2 silent| 21.58 | 4.03 | 19.47 | 15.03 |

The result of GPT-2 is only slightly higher than randomly sampling three sentences, and significantly lower than the classic supervised summarization system. Its value mainly lies in: an LM without summary fine-tuning can be induced to summarize the style by short prompts; the quality and factual consistency are still very limited.

The paper observes that generating summaries can bias information later in the article and can also confuse quantities, objects, or details.

## 4. Translation

The author gives the `English = French` pairing in the context, and then lets the model fill in the new sentence translation.

|direction| GPT-2 BLEU |Comparative explanation in the paper|
|---|---:|---|
| English → French | 5.0 |Slightly lower than simple bilingual dictionary word-by-word replacement|
| French → English | 11.5 |Exceeds some early unsupervised MT baselines, and is well below the best unsupervised methods at the time, which was ~33.5|

Fr→En is stronger and conforms to GPT-2, which is a characteristic of a strong English language model. WebText actively filters non-English pages when cleaning; language detection only finds about 10 MB of French text. Scattered bilingual fragments in web pages may still provide weak supervisory signals.

## 5. Natural Questions closed book fact questions and answers

After GPT-2 uses several question and answer examples to specify the short answer format, the exact match is 4.1%. The smallest model did not exceed the 1.0% baseline of returning high-frequency answers by question type; the largest model corrected approximately 5.3 times as many questions.

The paper also reports that on the 1% of questions for which the model is most confident, the accuracy is 63.1%. However, the overall performance is much lower than that of open-domain QA systems that combine retrieval and extractive reading (about 30%–50%).

This experiment revealed two things:

1. Some factual associations are indeed compressed in the parameters;
2. Parameter memory alone is not a reliable knowledge access mechanism.

## 6. Common patterns of results

|Task|signs of competence|Obvious shortcomings|
|---|---|---|
| CoQA |Ability to generate short answers based on documents and conversations|Rely on retrieval heuristics, much worse than strongly supervised systems|
|Summary|`TL;DR:` switchable output behavior|Low ROUGE, confusing details|
|Translate|Small traces of natural bilingualism can induce translation|BLEU low, direction asymmetry|
|Fact Questions and Answers|Partial knowledge is stored in parameters|Overall EM only 4.1%|

The most influential finding of the paper is not that every benchmark is strong, but that the same next-token model reveals a variety of callable behaviors when there are no parameter updates, and these behaviors usually increase with scale.
