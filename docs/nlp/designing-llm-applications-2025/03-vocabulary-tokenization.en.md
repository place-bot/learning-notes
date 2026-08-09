# Vocabulary and Tokenization

## 1. This is the chapter pointed to by the recommended statement

Chapter 3 of the book is dedicated to Vocabulary and Tokenization, and the table of contents covers:

```text
Vocabulary
→ Tokenizer
→ Normalization
→ Pre-tokenization
→ BPE / WordPiece
→ Special Tokens
```

Its value lies in putting BPE and WordPiece back into the complete input pipeline, rather than just talking about a pair-merge algorithm.

## 2. Vocabulary is part of the model parameters

If the vocabulary size is \(V\), the hidden size is \(d\), and the embedding parameter scale is:

\[
P_{\mathrm{embed}}=Vd.
\]

A large vocabulary can shorten the sequence, but increase embedding and output layers; a small vocabulary can reduce parameters, but increase the number of tokens and attention cost.

## 3. Tokenizer is a combination of functions

\[
T=P_{\mathrm{post}}
\circ L_{\mathrm{id}}
\circ S_{\mathrm{subword}}
\circ P_{\mathrm{pre}}
\circ N.
\]

Among them, normalization, pre-tokenization, subword model, ID lookup and special-token post-processing all affect the final input.

## 4. BPE and WordPiece’s place in the book

BPE training usually selects the highest frequency adjacent pairs:

\[
(a^*,b^*)=\arg\max_{a,b}F(a,b).
\]

The original idea of WordPiece is to select new units that can maximize the likelihood of improving the corpus; BERT runtime does longest-match-first on the final vocabulary.

Detailed derivation, GPT-2 byte mapping, `Ġ`, BERT `##` and complete hand calculations have been placed in [Subword tokenization special topic](../subword-tokenization/index.md).

## 5. Special token connects model targets and application protocols

Special tokens may mean:

- Document start and end;
- padding；
- BERT classification and sentence separation;
- masked prediction；
- system/user/assistant role;
- tool call and observation boundaries.

They are not ordinary string decorations. The model must learn the behavior corresponding to the ID during training, and the inference template must be accurately reproduced.

## 6. Tokenizer’s impact on application behavior

|behavior|Tokenizer impact|
|---|---|
|context capacity|How many tokens are generated for the same original text?|
|Delays and fees|prefill length and API token billing|
|Multilingual fairness|Is there an imbalance in fertility in different languages?|
|Numbers and codes|How to divide digits, indentation, and symbols|
|span task|Can token offset accurately return to the original text?|
|safe|Whether Unicode and whitespace variants bypass checks|
|continue training|Is new domain terminology overly fragmented?|

## 7. Why can’t I just change the tokenizer to an existing model?

The embedding line \(i\) is bound to the token ID \(i\) during training:

\[
e_i=E[i,:].
\]

The new tokenizer redefines ID semantics even if the vocabulary size is the same. Direct substitution is equivalent to sending the input to the wrong embedding line.

Safe practices include keeping the original tokenizer, adding new tokens in a controlled manner and initializing embedding, or retraining/continuing pretraining the model.

## 8. CAT scene check

Educational texts are individually tested for formulas, option numbers, codes, units, Chinese and English mixing, spelling errors, and student speaking. Tokenizer efficiency may affect the valid contexts available to students of different languages ​​and is therefore part of system fairness.

