# Masked Language Model with 80/10/10

## 1. Sampling

For each sequence, 15% of the WordPiece positions are randomly selected as prediction targets. Losses are only calculated at these locations:

\[
\mathcal L_{\text{MLM}}
=
-\sum_{i\in\mathcal M}
\log p(x_i\mid\widetilde{\mathbf x}).
\]

\(\mathcal M\) is the selected target set, and \(\widetilde{\mathbf x}\) is the destroyed input.

## 2. 80/10/10

For the 15% selected locations:

- 80% replaced with `[MASK]`;
- 10% replaced with random words;
- 10% keep the original word.

The expected proportion of all tokens is approximately:

\[
12\%\ [MASK],\qquad
1.5\%\ \text{random},\qquad
1.5\%\ \text{unchanged and still forecast}.
\]

## 3. Why not replace everything with [MASK]

`[MASK]` usually does not appear in downstream fine-tuning input. The random word and original word branches reduce the pretraining-fine-tuning input difference and force the model to maintain usable representations of ordinary tokens.

Although the target position of the original word can be maintained, it can see itself, but the model does not know which common tokens are selected, and only account for a small amount; the overall task still requires context.

## 4. MLM output header

The selected position representation first passes through dense, GELU, LayerNorm, and then calculates vocabulary logits with the output weight shared with the word embedding matrix:

\[
\mathbf o_i
=
\operatorname{LN}(
\operatorname{GELU}(
\mathbf T_i\mathbf W+\mathbf b))
\mathbf E_{\text{vocab}}^\top
+\mathbf b_{\text{vocab}}.
\]

## 5. The efficiency cost of MLM

Only 15% positions of each sequence provide direct word prediction loss, and the training signal is sparser than left-to-right LM. The paper FAQ also points out that MLM converges slowly; it trades deep bidirectional context for each token.

## 6. Static mask

The original code generates TFRecord offline, `dupe_factor` copies document fragments multiple times and randomly generates different masks. It is not infinite resampling online every training epoch; RoBERTa later emphasized dynamic masking.

## 7. Common confusions

- 15% is the proportion selected as prediction targets;
- 80/10/10 is allocated within this 15% only;
- The loss should also be calculated for the 10% that maintains the position of the original word;
- Special tokens do not participate in mask;
- The original paper is selected independently by WordPiece, not whole-word mask.
