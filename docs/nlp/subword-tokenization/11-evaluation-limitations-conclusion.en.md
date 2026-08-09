# Comments, limitations and conclusions

## 1. Tokenizer evaluation index

### Fertility

How many tokens are generated on average for each original word:

\[
\operatorname{fertility}
=
\frac{\text{subword token number}}
{\text{Original word count}}.
\]

Lower usually means shorter sequences, but does not alone represent model quality.

### Character or byte coverage rate

Measure `[UNK]` rate, byte fallback rate, and whether round-trip is stable in different languages.

### Compression ratio

\[
R
=
\frac{\text{Raw number of characters or bytes}}
{\text{number of tokens}}.
\]

It must be stated whether the numerator uses Unicode code points, grapheme clusters, or UTF-8 bytes, otherwise cross-language comparisons will be unfair.

### Downstream quality

Finally, we need to compare language-model loss, task accuracy, generation quality, training speed and service cost. A smaller number of tokens does not guarantee that it is more useful.

## 2. Multilingual fairness

Tokenizers trained with English-dominated corpora tend to assign many long tokens to English, while low-resource languages are chopped into smaller pieces. Consequences include:

- The same meaning takes up more context;
- Higher cost of reasoning per sentence;
- Long-distance dependencies span more tokens;
- Low resource text relies more on character or byte fallback;
- Some languages hit the maximum sequence length earlier.

Fertility, bytes-per-token, UNK, latency, and task quality should be reported separately by language.

## 3. Numbers, codes and whitespace

Tokenizer may split the number into single digits, digit fragments or entire segments. Code is highly sensitive to whitespace, indentation, operators, and case. Choose a tokenizer to cover real domain data:

```text
1,000.25
student_id_0042
θ_i^(t)
Indent code
URL and email
```

Compression rates measured only on News English are not representative of math, programming, or education item bank content.

## 4. Boundary errors and tokenization attack

Invisible Unicode, zero-width characters, homographs, unusual whitespace, and combined accents can cause:

- The same text gets different IDs with the naked eye;
- The moderation rules are inconsistent with the model input;
- Keyword matching is bypassed;
- offset and highlight misalignment;
- prompt suddenly expands in length.

Security systems should check the text after explicit normalization and audit the actual sequence of tokens fed into the model.

## 5. Vocabulary Bigger is not always better

A large vocabulary can shorten the sequence, but it will:

- Add embedding and output projection parameters;
- Reduce the training times for rare long tokens;
- Reduce subword sharing between similar words;
- Increase tokenizer training and softmax costs.

The optimal vocabulary size depends on the corpus size, number of languages, model size, context and task.

## 6. Limitations of BPE and WordPiece

- They are all greedy or local construction methods and do not guarantee the global optimal segmentation;
- Statistical fragments are not guaranteed to comply with morphemes and semantics;
- result strongly relies on training corpus and pre-tokenization;
- Deterministic single slicing may reduce robustness to spelling changes;
- After the tokenizer is solidified, new domain vocabulary can only be split by old units;
- Subword boundaries affect NER, extractive question answering, and character-level evaluation.

Unigram language model, subword regularization, BPE dropout, byte fallback and vocabulary adaptation respectively try to alleviate some of these problems.

## 7. Inspiration for CAT and educational texts

In item generation, open response scoring or educational dialogue systems, additional checks should be made:

- Mathematical formulas and LaTeX token overhead;
- Mixed arrangement of Chinese and English, units, question numbers and option symbols;
- Student spelling errors and colloquial abbreviations;
- Professional terms, variable names and codes;
- Whether the context budgets of students of different languages are similar;
- Can the token offset accurately return to the student's original answer?

Tokenizers change the sequence the model sees, but cannot replace measurement models, scoring rubrics, or content validity analysis.

## 8. Final conclusion

The two routes can be compressed into:

```text
BPE
Training: Merge high-frequency pairs
Encoding: Replay merge by merge rank

WordPiece
Training idea: Choose units that can improve the likelihood of the training corpus
Encoding: Make the longest match on the final vocabulary
```

GPT-2 adds reversible UTF-8 byte mapping before BPE to form byte-level BPE; BERT adds BasicTokenizer before WordPiece and marks the intra-word continuation with `##`.

A truly reproducible tokenizer is never just an algorithm name, but a complete combination of normalization, pre-tokenization, subword model, vocabulary, special tokens and post-processing.

