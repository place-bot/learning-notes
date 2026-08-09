# How to write tasks as context

## 1. Unified interface

GPT-2 does not add separate output headers for summary, translation, and question and answer. Each task is translated into a prefix, which is then continued by the language model:

\[
\hat y
=
\arg\max_y p_\theta(y\mid \text{prefix}).
\]

The content and format of prefix determine the current inference task of the model.

## 2. Reading Comprehension CoQA

The input consists of the document, the conversation history, and finally `A:`:

```text
Document: ...
Q: ...
A: ...
Q: ...
A:
```

The paper uses greedy decoding to generate answers, reaching 55 F1 on the development set. The model does not update parameters using CoQA's 127,000+ training question-answer pairs.

## 3. Summary

The author puts the article at the front and adds at the end:

```text
TL;DR:
```

Then use top-k sampling to generate 100 tokens, \(k=2\), and take the first three generated sentences as the summary. After removing `TL;DR:`, the paper reports a 6.4-point drop in average ROUGE, indicating that short prompts do change conditional generation behavior.

## 4. Translation

Put several pairing formats into the context:

```text
English sentence = French sentence
English sentence = French sentence
New English sentence =
```

Finally, use greedy decoding to get the first generated sentence. According to GPT-3's later terminology, as long as a paired example is placed before it, this is an in-context few-shot, rather than a strict zero-shot.

## 5. Fact Questions and Answers Natural Questions

Also first put some short answer question and answer pairs, let the model infer the output style, and then input new questions. The parameters of the model are not updated, but the examples affect the hidden state and subsequent token probabilities.

## 6. Multiple choice and cloze

If the candidate answer set is \(\mathcal A\), each candidate completion text can be scored:

\[
S(a)
=
\sum_{r=1}^{|a|}
\log p_\theta(a_r\mid c,a_{<r}).
\]

Choose

\[
\hat a=\arg\max_{a\in\mathcal A}S(a).
\]

For CBT, the paper not only calculates the candidate words themselves, but also calculates the probability of the remaining sentences after filling in the candidates, so that the candidates are subject to subsequent consistency constraints.

## 7. Generating strategies is also part of the experimental settings

|strategy|rules|Typical uses|
|---|---|---|
| greedy |Select the highest probability token at each step|Translation, short answer|
| beam search |Keep multiple high-scoring sequences|The formation of a more stable structure|
| top-k |Only sample the \(k\) tokens with the highest probability|abstract, open generation|
| temperature |logits divided by temperature \(\tau\)|Control the sharpness of the distribution|

The same model and the same prompt may obtain significantly different results under different decoding. Therefore, zero-shot performance is determined by the model, prompt, answer scoring and decoding rules.

## 8. Evaluation fairness issue

When comparing GPT-2 to supervised systems, also note:

- GPT-2 does not use the task training set for gradient updates;
- It has been trained on large-scale web corpus;
- The same task or similar text may naturally appear on the web page;
- Some "zero-shot" experiments use contextual examples;
- The supervised baseline may be smaller in size and have a narrower training domain;
- Prompt and output post-processing include manual design.

"No downstream training" cannot be equated to "no use of any task-relevant information".
