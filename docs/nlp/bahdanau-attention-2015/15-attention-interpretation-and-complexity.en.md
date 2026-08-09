# Attention explanation, complexity and parallelization

This page focuses on answering a common but easily confused question:

> Attention-based RNN can read the entire sentence context when generating translations. Why is its sequential nature still not conducive to training parallelization?

## 1. Calibrate one sentence first

The key to limiting parallelization comes from RNN's recursive state dependencies. The fact that text is sequential does not automatically lead to serial calculations; the Transformer also handles sequences, but can calculate many positions simultaneously during training.

For the example of generating "Ik hou van lama's", attention can record which source words each Dutch target word mainly reads information from. It improves source-side representation and dynamic context, but retains the circular dependency of encoder and decoder.

## 2. Why does the encoder wait by position?

Forward RNN:

\[
\overrightarrow{\mathbf h}_j
=
f(\mathbf x_j,\overrightarrow{\mathbf h}_{j-1}).
\]

\(\overrightarrow{\mathbf h}_4\) must be obtained before calculating \(\overrightarrow{\mathbf h}_5\), and \(\overrightarrow{\mathbf h}_4\) waits for \(\overrightarrow{\mathbf h}_3\):

\[
\overrightarrow{\mathbf h}_1
\rightarrow
\overrightarrow{\mathbf h}_2
\rightarrow\cdots\rightarrow
\overrightarrow{\mathbf h}_{T_x}.
\]

The reverse RNN forms an identical chain from the other end:

\[
\overleftarrow{\mathbf h}_{T_x}
\rightarrow\cdots\rightarrow
\overleftarrow{\mathbf h}_1.
\]

Both directions can run simultaneously with each other; positions within each direction still need to be advanced sequentially. The encoder critical path has approximately \(T_x\) recursive steps.

## 3. Why does the decoder have to wait?

Bahdanau decoder step \(i\) first uses the old state to calculate attention:

\[
e_{ij}=a(\mathbf s_{i-1},\mathbf h_j),
\qquad
\mathbf c_i=\sum_j\alpha_{ij}\mathbf h_j,
\]

Update again

\[
\mathbf s_i
=
f(\mathbf s_{i-1},y_{i-1},\mathbf c_i).
\]

The query at step \(i+1\) requires \(\mathbf s_i\), so the target position is formed

\[
\mathbf s_0
\rightarrow
\mathbf c_1,\mathbf s_1
\rightarrow
\mathbf c_2,\mathbf s_2
\rightarrow\cdots.
\]

Even if teacher forcing has given all the real target words at once, all \(\mathbf s_i\) still cannot be calculated at the same time. The target word is known to have no eliminated state dependence.

## 4. Which parts of Attention can be parallelized?

After fixing a target step \(i\),

\[
e_{i1},e_{i2},\ldots,e_{iT_x}
\]

It can be calculated simultaneously as a matrix operation; softmax, weighted sum, different sentences in the batch, and within the linear layer can also be parallelized.

Therefore, the model is in a state of "local high degree of parallelism and time step global serialization". The GPU can accelerate large matrix multiplication at each step, but it has to wait for the previous step state to complete before starting the next time step.

## 5. Differences from Word2Vec

Word2Vec converts the corpus into a large number of center word-context word training samples. Given the sampling result, the losses of different word pairs are roughly independent:

\[
\mathcal L
=
\sum_{(w,c)\in\mathcal D}\mathcal L(w,c).
\]

Multiple word pairs can form a large batch, and embeddings can be checked, inner products calculated and updated in parallel. It does not have the dependency chain "the 8th word pair must wait for the hidden state of the 7th word pair".

Word2Vec learns static word vectors through local co-occurrence and cannot generate contextualized representations for the same word in different sentences and different positions. RNNsearch obtains sentence-by-sentence, position-by-position dynamic representation, one of the costs is the recursive critical path.

## 6. Differences from Transformer

During Transformer training, all positions are piled into a matrix and calculated uniformly.

\[
\mathbf Q=\mathbf X\mathbf W_Q,\qquad
\mathbf K=\mathbf X\mathbf W_K,\qquad
\mathbf V=\mathbf X\mathbf W_V,
\]

\[
\operatorname{Attention}(\mathbf Q,\mathbf K,\mathbf V)
=
\operatorname{softmax}\!\left(
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}
\right)\mathbf V.
\]

The target training uses a causal mask to prevent the location from reading future tokens, but the mask just sets the corresponding score to \(-\infty\). The matrix of all target positions can still be obtained in the same forward calculation.

### Training and generation must be separated

Transformer training can be parallelized across locations. When generating autoregression, the \(i+1\) token still has to wait for the \(i\) token to be selected:

\[
\widehat y_1
\rightarrow
\widehat y_2
\rightarrow\cdots.
\]

KV cache reduces repeated calculations without eliminating causal waits between output tokens.

## 7. Comparison of four calculations

|model/stage|Can the positions of the same sentence be parallel?|Where does order dependency come from?|
|---|---|---|
|Word2Vec word pair training|A large number of word pairs can be parallelized|Sampling and shared parameter updates, no per-position hidden state chain|
|Bahdanau RNN encoder|One-way internal serial|\(\mathbf h_j\) depends on \(\mathbf h_{j-1}\)|
|Bahdanau RNN decoder training|target step serial|\(\mathbf s_i,\mathbf c_i\) depends on \(\mathbf s_{i-1}\)|
|Transformer training|Each position is matrixed in parallel|causal mask limits visibility and does not form recursive state chains|
|autoregressive reasoning|Both RNN and Transformer are token-based|The next input token has not been generated yet|

## 8. Why GPUs especially care about critical paths

GPUs are good at processing large regular matrices at once. RNN splits the entire sentence work into smaller calculations that are started sequentially \(T\):

\[
\text{total delay}
\approx
\sum_{t=1}^{T}
\text{No.}t\text{step delay}.
\]

Synchronization is required between time steps, and long sequences increase kernel startup, memory access, and non-overlapping waits. Transformer incorporates the position dimension into the matrix, making the critical path of a single layer independent of sequence length, at the cost of self-attention's fractional matrix requiring \(O(T^2)\) computation and memory.

## 9. Complexity of Bahdanau attention

|part|Main scale|
|---|---|
|Bidirectional RNN encoding|\(O(T_x)\) serial recursive steps|
|RNN decoding|\(O(T_y)\) serial recursive steps|
|All cross-attention scores| \(O(T_xT_y n')\) |
|attention weight storage| \(O(T_xT_y)\) |

Precomputing \(\mathbf U_a\mathbf h_j\) reduces the constant term; the recursive critical path is still approximately \(T_x+T_y\).

## 10. Interpretation scope of attention weight

\(\alpha_{ij}\) is the true coefficient in the context weighted sum, suitable for observing the read pattern at each step of the model. It is not a proof of complete causal contribution because:

- \(\mathbf h_j\) has mixed left and right contexts;
- Information also flows through the decoder old state;
- Changing weights may send inputs outside the training distribution;
- There are non-linear interactions between parameters.

Robust analysis can combine attention heatmaps, gradients, input perturbations, masking experiments, manual alignment and translation evaluation.

## 11. The most accurate conclusion

"This sequential nature is not conducive to parallelization" can be more precisely stated as:

> The Bahdanau model uses recursive states to represent sequences. Each RNN position depends on the previous position, and all hidden states of the same sequence cannot be calculated at the same time during training; source position attention, batch and matrix operations within a single time step can still be parallelized.

This distinction is also the core clue from RNN attention to Transformer.
