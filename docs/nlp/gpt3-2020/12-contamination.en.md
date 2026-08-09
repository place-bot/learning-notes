# Benchmark pollution and clean subset

## 1. Why the problem is more serious than GPT-2

The data and model scale of GPT-3 is approximately two orders of magnitude larger than that of GPT-2. Common Crawl may contain public benchmarks, item source web pages, or near-duplicate texts. Models do not need to see formal labels and may benefit from seeing background paragraphs.

## 2. Filter before training

The author tries to search for 13-gram overlap between benchmark development/test and training data, and delete the collision fragment and the 200 characters before and after. Fragments that are too short are discarded; a document that is cut into more than 10 segments is deleted entirely.

A bug was later discovered that made filtering of long documents incomplete. Since the cost of 175B retraining is too high, the author did not retrain, but performed post-hoc clean subset analysis.

## 3. Clean example definition

Select the length \(N\) for each benchmark, roughly taking the 5th percentile of the number of sample words and limiting it to between 8 and 13; smaller n-grams can be used for short synthetic tasks. If any \(N\)-gram of the sample collides with the full training corpus, it is marked as dirty, otherwise it is marked as clean.

Simplified and written as:

\[
\operatorname{dirty}(x)
=
\mathbb I
\left[
\exists g\in\operatorname{NGram}_N(x):
g\in\mathcal C_{\mathrm{train}}
\right].
\]

Then compare:

\[
\Delta
=
\operatorname{Score}(\mathcal D_{\mathrm{clean}})
-
\operatorname{Score}(\mathcal D_{\mathrm{all}}).
\]

## 4. Overall result

Most benchmarks show little change on the clean subset, and the pollution ratio is not significantly related to the performance difference. The author proposes two explanations:

- Conservative detection produces a large number of false positives;
- Text overlap exists, but provides limited help with task answers.

## 5. Key cases

### 5.1 Reading Comprehension

More than 90% of the samples of QuAC, SQuAD2, and DROP were marked by the initial screening, but manual inspection found that the training corpus mainly contained source passage, without formal questions and answers. For these tasks, a distinction needs to be made between seeing background documentation and remembering the answers.

### 5.2 PIQA

About 29% of the samples are labeled, and the absolute drop in clean subset accuracy is about 3 percentage points. Since there is a similar drop in the smaller model, the author suspects a difference in clean/dirty difficulty distribution, but cannot strictly rule out contamination, thus giving the result an asterisk.

### 5.3 Winograd

About 45% were tagged; manual inspection confirmed that 132 schemas were present in the training set, with varying formats. The clean subset dropped by 2.6%, and the paper added pollution marks to the results.

### 5.4 LAMBADA

There is substantial real overlap, but the clean subset and full set scores differ within about 0.5%. The fill-in-the-blank format also prevents the most direct rewrite of an entire segment of memory, but that doesn't eliminate all effects.

### 5.5 Language modeling data set

Almost all of the four Wikipedia LM benchmarks and CBT used by GPT-2 appear in the GPT-3 training data, and a credible clean subset cannot be constructed, so the paper does not report these results. PTB has become the main LM benchmark due to its earlier age and less pollution.

## 6. Clean subset will also generate selection bias

If the questions reproduced on the Internet happen to be easier, deleting dirty examples will leave a more difficult distribution:

\[
p(x\mid\mathrm{clean})
\ne
p(x\mid\mathrm{all}).
\]

The drop in score at this time may come from difficulty changes and cannot be entirely attributed to memory. The opposite direction is equally possible.

## 7. The value of this analysis

The paper openly admits to filtering bugs, marking suspicious results, and deleting data sets that cannot be trusted to be evaluated. This establishes important specifications for large model evaluation:

- Remove weight before training;
- Contamination detection after training;
- Distinguish between source overlap and label leakage;
- Report clean and all at the same time;
- Explicitly raise unadjustable results.

It is still a hindsight approximation. At the scale of the open web, semantic rewriting, translation, answer leakage, and non-disclosure of training corpus all limit audit integrity.
