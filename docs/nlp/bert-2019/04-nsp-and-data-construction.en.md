# NSP and pretraining sample construction

## 1. Next Sentence Prediction

Each sample contains segments A and B:

- 50%: B is the fragment that follows A in the corpus, `IsNext`;
- 50%: B randomly sampled from other documents, `NotNext`.

`[CLS]` top-level vector passes the binary classifier:

\[
p(z\mid\mathbf C)
=
\operatorname{softmax}(
\mathbf W_{\text{NSP}}\mathbf C+\mathbf b).
\]

\[
\mathcal L_{\text{NSP}}=-\log p(z^\star\mid\mathbf C).
\]

## 2. Joint goals

\[
\mathcal L
=
\mathcal L_{\text{MLM}}
+
\mathcal L_{\text{NSP}}.
\]

The original code directly adds two average losses without additional adjustable weights.

## 3. The importance of document-level corpus

NSP positive examples require real continuous segments, so the paper emphasizes using BooksCorpus and Wikipedia that preserve the document structure, rather than a completely scrambled sentence set.

## 4. Sample construction

The original script splits the document into a list of sentences, accumulates the fragments until it approaches the target length, and then decides whether B is a true follow-up or a random document fragment. 10% of samples randomly use a target length shorter than the maximum length to help the model adapt to short sequences and reduce the bias of only seeing full-length samples.

## 5. What NSP learned

The task also includes topic consistency, document continuity and random negative example identification. The paper considers it beneficial for QA/NLI, and observes a decrease in removing NSP in its own ablation.

Subsequently, RoBERTa still performed well after removing NSP under a stronger training formula, indicating that the conclusion of BERT Table 5 is bound to its training conditions. The universal necessity of NSP cannot be determined by a single ablation of the original paper.

## 6. NSP and sentence pairing tasks

The input form of pretraining is consistent with the downstream sentence pairs such as premise–hypothesis and question–passage. The downstream does not continue to do NSP directly; it uses the shared encoder and segment representation to train its own supervision objectives.
