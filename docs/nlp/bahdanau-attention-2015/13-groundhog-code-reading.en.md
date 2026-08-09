# GroundHog Original code intensive reading

[GroundHog](https://github.com/lisa-groundhog/GroundHog/tree/master/experiments/nmt) disclosed by the author is a Theano/Python 2 era implementation. It is suitable for checking the paper mechanism and historical configuration, but is not suitable as a direct dependence on the modern environment.

## 1. File map

|File|Responsibilities|
|---|---|
| `experiments/nmt/state.py` |Model, data, optimizer and length configuration|
| `experiments/nmt/encdec.py` |encoder, RNNsearch decoding layer, cost map|
| `experiments/nmt/sample.py` |Sampling and beam search|
| `groundhog/trainer/SGD_adadelta.py` |Adadelta and gradient cropping|
|data iterator|padding, mask, OOV mapping and length sorting|

The README clearly states that this directory contains the implementation used in the paper, and the default search prototype corresponds to RNNsearch-50.

## 2. How to configure how to distinguish between two models

Key switches for fixed vector configuration include

```python
search = False
last_forward = True
forward = False
backward = False
```

RNNsearch configuration uses

```python
search = True
last_forward = False
forward = True
backward = True
dec_rec_layer = "RecurrentLayerWithSearch"
seqlen = 50
sort_k_batches = 20
```

These switches replace single end vectors with bidirectional annotation sequences and enable stepwise search/attention.

## 3. Forward path of `RecurrentLayerWithSearch`

The code first precomputes projections for all source annotations:

\[
\mathbf U_a\mathbf h_j.
\]

The state projection is calculated again at each target step, broadcast to all source positions, added to the precomputed items, and energy is obtained through \(\tanh\) and vector projection. Then:

1. Apply source mask;
2. Normalize the source position;
3. Calculate the weighted sum of the annotations;
4. Add the context to the candidate state, reset gate and update gate;
5. Optional return to the entire alignment.

This corresponds one-to-one with the thesis formula.

## 4. Bidirectional comments

The code constructs a forward layer and a reverse layer that runs on the reverse sequence, and then splices the components at the corresponding positions. The source mask is used for both recursion and attention, ensuring that padding neither pollutes the hidden state nor gains attention.

## 5. Numerical stability

The historical code directly takes `exp` for energy and divides it by the sum. Modern implementations typically use the numerically stable `softmax`:

\[
\operatorname{softmax}(\mathbf e)
=
\frac{\exp(\mathbf e-\max\mathbf e)}
{\sum_j\exp(e_j-\max\mathbf e)}.
\]

Subtracting the maximum value does not change the probability, but it can avoid exponential overflow of large positive numbers.

## 6. Optimizer

`SGD_adadelta.py` first summarizes all gradient norms, scales them by the upper limit of 1, and then performs Adadelta cumulative update. \(\rho=0.95,\epsilon=10^{-6}\) in the configuration is consistent with the appendix.

## 7. Data batch

Iterators are responsible for:

- Map words to integer ids;
- OOV mapping is \([UNK]\);
- Padding on the source and target ends;
- Generate effective position mask;
- Divide buckets by length to reduce empty calculations;
- Provide reverse sequence for reverse encoder.

These data layer details are necessary to reproduce the attention mask and training speed.

## 8. Beam search

`sample.py` Also maintained:

- active hypothesis token;
- Cumulative negative log probability;
- The hidden state of each hypothesis;
- Assumptions completed;
- Optional \([UNK]\) masking and length normalization.

The script's maximum loop length is relative to the source sentence length and includes minimum length logic. The paper does not report beam width, so the code default cannot automatically be considered the only setting for all results of the paper.

## 9. When migrating from an old implementation

Need to be handled explicitly:

- Python 2 and old Theano API;
- Modern GRU equation convention;
- Stable masked softmax;
- batch-first/time-first dimensions;
- EOS, BOS and \([UNK]\) id;
- Beam parent path status rearrangement;
- The status subscripts of papers and codes are shifted.

## Summary of this page

The GroundHog code verifies the key engineering ideas of the paper: source projection precomputation, step-by-step status query, source mask, context entry into the three GRU channels, and independent maintenance of the status of each beam. Modern reproductions should preserve these information paths while updating numerical stability and software stacks.
