# References and materials

## Original paper

- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). *Efficient Estimation of Word Representations in Vector Space*. ICLR Workshop Papers. [arXiv:1301.3781](https://arxiv.org/abs/1301.3781)
- [Google Research paper page](https://research.google/pubs/efficient-estimation-of-word-representations-in-vector-space/)
- [ICLR 2013 Workshop Proceedings](https://iclr.cc/archive/2013/workshop-proceedings.html)
- [DBLP record](https://dblp.org/rec/journals/corr/abs-1301-3781)

## Official code and data

- [Google Code Archive: word2vec](https://code.google.com/archive/p/word2vec/)
- `questions-words.txt` in archived source code: Set of semantic-syntactic analogy problems.
- `compute-accuracy.c` in archived source: original top-1 analog evaluation program.

## Directly related work in the same year

- Mikolov, T., Yih, W.-T., & Zweig, G. (2013). Linguistic regularities in continuous space word representations. *NAACL-HLT*, 746–751. [ACL Anthology](https://aclanthology.org/N13-1090/)
- Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words and phrases and their compositionality. *Advances in Neural Information Processing Systems, 26*. [NeurIPS Proceedings](https://papers.nips.cc/paper_files/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html)

## Basic and preorder models

- Bengio, Y., Ducharme, R., Vincent, P., & Jauvin, C. (2003). A neural probabilistic language model. *Journal of Machine Learning Research, 3*, 1137–1155.
- Hinton, G. E., McClelland, J. L., & Rumelhart, D. E. (1986). Distributed representations. In *Parallel Distributed Processing, Volume 1*.
- Morin, F., & Bengio, Y. (2005). Hierarchical probabilistic neural network language model. *AISTATS*.
- Mnih, A., & Hinton, G. (2009). A scalable hierarchical distributed language model. *NeurIPS 21*.
- Mikolov, T., Karafiát, M., Burget, L., Černocký, J., & Khudanpur, S. (2010). Recurrent neural network based language model. *Interspeech*.

## Subsequent static vocabulary display

- Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global vectors for word representation. *EMNLP*, 1532–1543. [ACL Anthology](https://aclanthology.org/D14-1162/)
- Levy, O., & Goldberg, Y. (2014). Neural word embedding as implicit matrix factorization. *NeurIPS 27*.
- Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). Enriching word vectors with subword information. *Transactions of the ACL, 5*, 135–146. [ACL Anthology](https://aclanthology.org/Q17-1010/)

## Contextual representation

- Peters, M. E., et al. (2018). Deep contextualized word representations. *NAACL-HLT*, 2227–2237. [ACL Anthology](https://aclanthology.org/N18-1202/)
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL-HLT*, 4171–4186. [ACL Anthology](https://aclanthology.org/N19-1423/)

## Release Notes

This topic is based on arXiv v3 and ICLR 2013 Workshop records. The numbers and values ​​of Equations (1)–(5) and Tables 1–8 follow the paper. The probabilistic objective, hierarchical-softmax gradient, and minimal realization are derived based on the architecture of the paper. Negative Sampling, frequent word downsampling, and phrase learning are included in subsequent NIPS 2013 work.
