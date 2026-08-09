# Three-stage migration process and AWD-LSTM

## 1. Three stages

### General language modelpretraining

Training left-to-right LM on WikiText-103:

\[
\mathcal L_{\text{LM}}
=
-\sum_t\log p(w_t\mid w_{<t}).
\]

### Target task LM fine-tuning

Use all the texts of the target task and still do language modeling to adapt the general LM to the domain distribution.

### Target classifier fine-tuning

Add a classification head to the LM, train with annotations, and unfreeze layer by layer.

## 2. Why is there a target domain LM in the middle?

Generic Wikipedia is not the same distribution as IMDb comments, news headlines, or questions. For unlabeled target text, first adjust the language model to reduce the domain shift, and then learn the label boundaries.

## 3. AWD-LSTM

Thesis uses:

- 3-layer LSTM;
- embedding 400；
- 1150 hidden per level;
- BPTT 70；
- Embedding, input, inter-layer, cycle weight and other types of dropout;
- weight-dropped LSTM。

The approach emphasizes replaceable general-purpose LMs, and the authors anticipate that better LMs will further improve downstream performance.

## 4. With Dai & Le

Dai & Le proved that LM/autoencoder pretraining can be used as LSTM initialization. ULMFiT extends it into a large general corpus → target domain LM → classifier, and specifically solves forgetting and overfitting in fine-tuning.
