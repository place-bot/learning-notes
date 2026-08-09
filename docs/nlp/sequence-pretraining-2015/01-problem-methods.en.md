# pretraining problem and two unsupervised objectives

## 1. Goal

Supervised document classification data is limited, and long sequence LSTM is difficult to optimize. The paper first uses unlabeled sequences to learn embedding and LSTM weights:

\[
\theta_{\text{pre}}
=
\arg\min_\theta
\mathcal L_{\text{unsup}}(\theta),
\]

Reinitialize the supervised model:

\[
\theta_0^{\text{sup}}=\theta_{\text{pre}}.
\]

## 2. Recurrent language model

\[
\mathcal L_{\text{LM}}
=
-\sum_t\log p(x_{t+1}\mid x_{\le t}).
\]

It trains LSTM to save the state that is beneficial to predicting the next token, and obtains LM-LSTM initialization.

## 3. Sequence autoencoder

The encoder LSTM reads the complete input \(x_1,\ldots,x_T\) to the state, and the decoder reconstructs the original sequence:

\[
\mathcal L_{\text{SA}}
=
-\sum_t\log p(x_t\mid x_{<t},h_{\text{enc}}).
\]

Get SA-LSTM initialized. The authors argue that reorganizing documents forces the final state to capture longer-range information.

## 4. Why is it called semi-supervised

Train the representation and sequence parameters on unlabeled data, train the classifier on labeled data and continue fine-tuning all weights:

\[
\text{unlabeled pretraining}
\rightarrow
\text{labeled fine-tuning}.
\]

## 5. With Word2Vec

Word2Vec initialization only migrates word embedding; LM/SA pretraining migrates embedding and recursive combination functions at the same time. The word2vec initialization error in the paper IMDB is 10.00%, LM-LSTM 7.64%, and SA-LSTM 7.24%.
