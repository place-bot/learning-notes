# Data, results, limitations and subsequent impacts

## 1. Brown corpus

The best validation setting corresponds to a neural + trigram mixture test perplexity of 252; the best n-gram/category model is about 312, a difference of about 24%. Removing interpolated trigrams is 336, about 33% higher than the best neural mixture.

Increasing context from 2 to 4 words helped the neural model, but did not significantly help n-grams, supporting the claim that distributed representations take advantage of longer context.

## 2. AP News

neural mixture test perplexity 109; best Kneser–Ney 5-gram is 117, approximately 8% improvement. The gap narrows at larger scales, but there are still advantages.

## 3. Evidence

Experimental support:

- Jointly learned representations and probabilities are better than strong n-grams at the time;
- hidden units is helpful;
- neural and trigram mixture further reduce perplexity;
- Distributed representations can generalize from similar contexts.

## 4. Limitations

- Fixed window, unable to handle arbitrarily long dependencies;
- Full vocabulary softmax is expensive;
- embedding is static, a word with multiple meanings shares a vector;
- Huge training resources;
- Two corpora, mainly perplexity, task transfer has not yet been verified;
- OOV and output vocabulary display are still limited.

## 5. Historical influence

It establishes the basic template of "embedding + neural conditional probability + end-to-end maximum likelihood". RNN LM removes the fixed window, Word2Vec simplifies representation training, Transformer models context in parallel, and BERT uses language targets for large-scale transfer learning.

## 6. Conclusion

Language modeling provides pretraining with predictive signals without manual labels. Bengio et al. (2003) showed that word vectors and language probabilities can be learned together and are a key starting point for understanding subsequent neural pretraining.
