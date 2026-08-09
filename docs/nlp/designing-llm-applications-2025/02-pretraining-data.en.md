# pretraining data: from corpus size to data governance

## 1. The model learns the training distribution

Autoregressive language model minimization:

\[
\mathcal L(\theta)
=
-\sum_{x\in\mathcal D}
\sum_{t=1}^{|x|}
\log p_\theta(x_t\mid x_{<t}).
\]

Dataset \(\mathcal D\) determines which languages, domains, genres, and biases the model sees repeatedly. Model size cannot compensate for the complete absence of key knowledge, nor can it automatically identify factual errors in the training corpus.

## 2. Data pipeline

```text
original source
  ↓ extraction
parsable document
  ↓ language / format / quality filtering
Candidate corpus
  ↓ deduplication / PII / safety
Cleaning the corpus
  ↓ decontamination
training corpus pool
  ↓ mixture weighting / curriculum
training batches
```

Each step changes the empirical distribution.

## 3. Quality filtering

Quality scores can be given by rules, classifiers or stronger models:

\[
q(x)=f(
\text{Language},
\text{structure},
\text{Repeat},
\text{readability},
\text{Source},
\text{safe}
).
\]

Hard threshold directly deletes documents; soft sampling uses \(q(x)\) to adjust the selection probability. The quality model itself may favor dominant language, formal style, or content that is similar to the evaluation criteria, thus requiring auditing for erroneous deletions by domain.

## 4. Remove duplicates

### Exact duplication

Detect identical documents using content hashes.

### Near duplication

Find highly overlapping documents via n-gram, MinHash, or locality-sensitive hashing. Removing duplicates can:

- Reduce a small number of documents being memorized repeatedly;
- Let the token budget cover more independent information;
- Reduce train-test contamination;
- Improve the interpretability of data mixtures.

Deduplication that is too strong may also delete legitimate templates, quotes, or important repeated facts.

## 5. Data contamination

If the evaluation sample or its approximate version enters the training set, the measured performance includes a memory component:

\[
\widehat R_{\mathrm{test}}
=
R_{\mathrm{generalization}}
+B_{\mathrm{contamination}}.
\]

Decontamination requires choices between tokenizer, string normalization and matching granularity. Only matching complete documents will miss local item leaks; too wide n-gram matching will accidentally delete common expressions.

## 6. Data mixture

The sampling probability of multiple data sources \(D_k\) is:

\[
p(x)
=
\sum_{k=1}^{K}
\pi_k p_k(x),
\qquad
\sum_k\pi_k=1.
\]

\(\pi_k\) does not have to be equal to the proportion of the original data volume. High-quality books, code, or mathematical corpus can be upsampled; large-scale noisy web pages can be downsampled.

The Mixture selection controls the ability, as well as the bias and number of repetitions. The number of tokens, number of epochs and training phase weight of each source should be recorded.

## 7. Synthetic data

Synthetic data is suitable for:

- Supplement the format of scarce tasks;
- Control difficulty and coverage;
- Generate inference or tool trajectories;
- Construct negative examples and safety boundaries;
- Distill strong model behavior.

Risks include error loop amplification, single style, teacher bias, and benchmark contamination. A reliable process should include generation, filtering, deduplication, fact verification, and manual sampling.

## 8. PII and data governance

Deleting the name regex is not enough. PII may appear in free text, code, tables, and combination fields. Data governance includes at least:

- Source authorizations and licenses;
- PII detection and review;
- Delete requests and data lineage;
- Exclusion of high-risk areas;
- training set access rights;
- Model memory and extraction test.

## 9. Interface with CAT data

Student response data is not ordinary web page corpus. Need to consider:

- FERPA/Privacy and Agency Agreement;
- Segment students, items and time to avoid leakage of the same object;
- Whether low-ability groups and language groups are undervalued;
- item exposure and copyright;
- Whether the answer track retains the real-time order;
- Domain gap between simulated data and real behavior.

The upper limit of generative CAT is limited by both training trajectory coverage and counterfactual missingness.

