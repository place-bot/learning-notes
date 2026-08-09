# LM-LSTM, SA-LSTM and training process

## 1. Sequence autoencoder

Add a closing tag at the end of the input. After the encoder finishes reading, the decoder begins to reconstruct the complete document token by token. The paper does not truncate the input window, but backpropagation traces up to 400 time steps from the end of the sequence.

## 2. pretraining configuration

- About 500k updates;
- batch size 128；
- Tokenization handles punctuation independently;
- Remove words that appear only once;
- LSTM uses cell output and gradient clipping.

## 3. Which parameters to migrate

\[
\theta_{\text{transfer}}
=
\{\text{word embeddings},\text{LSTM weights}\}.
\]

In the supervision stage, a classification head is added, fine-tune embedding and LSTM are continued, and early stopping is performed when the verification error increases.

## 4. Classification

The final LSTM state goes into the small hidden layer and softmax:

\[
p(y\mid x)
=
\operatorname{softmax}(
W_c\,g(h_T)+b_c).
\]

The IMDB configuration uses 1024 memory cells, 512 embedding, 30-unit classification hidden layer and dropout.

## 5. Variations

- LM-LSTM: next-token LM initialization;
- SA-LSTM: sequence autoencoder initialization;
- linear gain: weight the reconstructed position;
- joint training: Supervision tasks and autoencoder are trained simultaneously.

In the experiment, simple staged SA-LSTM outperformed linear gain and joint training, indicating that the joint target is not automatically better.

## 6. Why does pretraining improve stability?

Randomly initialized LSTM must learn vocabulary representation, long-range state and classification boundaries at the same time. Pretraining first puts the parameters into an area that can model the sequence structure to make the starting point of supervised optimization better. It is an empirical interpretation and there is no guarantee that any pretraining goal will help any task.
