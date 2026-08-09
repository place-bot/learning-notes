# Chinese tokenization and \(n\)-gram features

## 1. tokenization

The original question stem is a Chinese string. The paper uses `jieba` to cut the string into words:

```text
Xiao Ming has twelve books
        ↓
Xiao Ming / has / twelve / books / books
```

tokenizationresult determines subsequent feature boundaries. The same sentence of text may be segmented differently under different dictionaries and `jieba` versions.

## 2. unigram

Let tokenizationresult be

\[
(w_1,w_2,\ldots,w_L).
\]

The unigram set is

\[
\{w_1,w_2,\ldots,w_L\}.
\]

It can grab:

- Numbers and operational terms;
- Direct prompts such as "sum", "difference" and "integer";
- characters, figures and situation words;
- Indirect signal brought by question stem length.

## 3. bigram

bigram is two adjacent words:

\[
(w_1,w_2),(w_2,w_3),\ldots,(w_{L-1},w_L).
\]

It can distinguish the role of the same word in different collocations, for example:

```text
seek sum
total
According to figure
statement correct
```

## 4. trigram

A trigram is three consecutive words:

\[
(w_1,w_2,w_3),\ldots,(w_{L-2},w_{L-1},w_L).
\]

It preserves more local word order and is easier to sparse.

## 5. Three experimental characterizations

The papers compare in order:

\[
(1,1),\quad(1,2),\quad(1,3)
\]

Three \(n\)-gram ranges:

|Name|Contains features|
| --- | --- |
| unigram |only one word|
| unigram+bigram |One word and two adjacent words|
| unigram+bigram+trigram |One word, two adjacent words and three adjacent words|

## 6. Feature sparsity

The unigram generated a total of 2,943 features, more than 80% of which appeared in less than 5 questions.

After adding bigram/trigram, the paper does not report the total number of vocabulary, but only shows that more than 90% of the features belong to the same low-frequency features.

If "less than 5 times" is recorded as rare, then the unigram has at least

\[
0.8\times2943\approx2355
\]

a low-frequency word.

## 7. Why sparsity affects Gaussian NB

A large number of low-frequency features produce:

- Many dimensions that are almost all 0;
- The within-class mean and variance estimates are unstable;
- Accumulation of a large number of weak features in conditional independent likelihood;
- Noise accumulates when training samples are limited.

This explains that the accuracy of NB under "all unigrams" is only 21.3%, while it rises to 84.0% after information gain filtering.

## 8. Details that need to be fixed for reproduction

At a minimum, it should be recorded:

- `jieba` version;
- Custom dictionary;
- Disable vocabulary;
- Whether the numbers are normalized;
- How to deal with punctuation, units and formulas;
- Minimum document frequency;
- Whether templates of the same question type are divided into groups.

The original text does not give these settings.
