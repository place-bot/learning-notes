# GRU, state initialization and Deep Output

The appendix of the paper gives the gated state update and output layer of RNNsearch. Here is a step-by-step explanation along the path of \(\mathbf c_i\) into the decoder.

## 1. decoder status

\[
\mathbf s_i
=
(1-\mathbf z_i)\odot\mathbf s_{i-1}
+
\mathbf z_i\odot\widetilde{\mathbf s}_i.
\]

\[
\begin{aligned}
\mathbf z_i
&=\sigma(
\mathbf W_z\mathbf E_y[y_{i-1}]
+\mathbf U_z\mathbf s_{i-1}
+\mathbf C_z\mathbf c_i),\\
\mathbf r_i
&=\sigma(
\mathbf W_r\mathbf E_y[y_{i-1}]
+\mathbf U_r\mathbf s_{i-1}
+\mathbf C_r\mathbf c_i),\\
\widetilde{\mathbf s}_i
&=\tanh\!\left(
\mathbf W\mathbf E_y[y_{i-1}]
+\mathbf U[\mathbf r_i\odot\mathbf s_{i-1}]
+\mathbf C\mathbf c_i
\right).
\end{aligned}
\]

|input|information|
|---|---|
| \(\mathbf s_{i-1}\) |Status of generated target prefix|
| \(\mathbf E_y[y_{i-1}]\) |Previous target word embedding|
| \(\mathbf c_i\) |The content currently read dynamically from the source sentence|

The update gate determines the interpolation between the old state and the candidate state, and the reset gate determines how much of the old state enters the candidate calculation. The context affects both gates and candidate states simultaneously.

## 2. Differences from modern GRU API

Papers and frameworks may exchange the interpolation direction of the update gate, change the order of the reset gate before and after linear transformation, or splice the context with the input. When reproducing, check the complete equation and tensor shape. The "GRU" name alone is not enough to ensure item-by-item consistency.

## 3. Bidirectional encoder

Gating units are also used in both directions of the source:

\[
\mathbf h_j
=
\begin{bmatrix}
\overrightarrow{\mathbf h}_j\\
\overleftarrow{\mathbf h}_j
\end{bmatrix}.
\]

The forward state reads the left history, and the reverse state reads the right history. After splicing, each source position has a full sentence context.

## 4. decoder initialization

\[
\mathbf s_0
=
\tanh(
\mathbf W_s\overleftarrow{\mathbf h}_1).
\]

\(\overleftarrow{\mathbf h}_1\) has been recursed from the end of the sentence to the beginning of the sentence and is used as the global starting point; at each subsequent step, the dynamic context is obtained through attention.

## 5. Deep output and maxout

The output layer first fuses three sources:

\[
\widetilde{\mathbf t}_i
=
\mathbf U_o\mathbf s_i
+
\mathbf V_o\mathbf E_y[y_{i-1}]
+
\mathbf C_o\mathbf c_i.
\]

Then do maxout on two adjacent dimensions:

\[
t_{i,k}
=
\max(
\widetilde t_{i,2k-1},
\widetilde t_{i,2k}).
\]

eventually

\[
\mathbf o_i=\mathbf W_o\mathbf t_i,
\qquad
p(y_i=w\mid\cdots)
=
\frac{\exp(o_{i,w})}
{\sum_{v\in\mathcal V_y}\exp(o_{i,v})}.
\]

The context not only enters the GRU, but also directly enters the target word reading through \(\mathbf C_o\mathbf c_i\), providing a shorter information and gradient path.

## 6. Main dimensions

|quantity|Paper configuration|
|---|---:|
|encoder single direction hidden dimension \(n\)| 1000 |
|decoder status dimension| 1000 |
|Bidirectional annotation dimensions| 2000 |
|Word embedding dimension \(m\)| 620 |
|Align hidden dimension \(n'\)| 1000 |
|maxout output dimension \(l\)| 500 |
|Vocabulary at both ends|30,000 each|

If the maxout output is 500 dimensions, then the \(\widetilde{\mathbf t}_i\) before it is 1000 dimensions.

## 7. Status subscript

The probability expression in the main text uses the current state \(\mathbf s_i\), and there is a one-step subscript translation in the appendix and the GroundHog readout code. The stable data flow is:

1. Calculate the current attention from the old state;
2. Attention gets \(\mathbf c_i\);
3. Previous target word, old status and context update status;
4. Output the current target word distribution.

Just use a consistent set of subscripts when implementing it.

## Summary of this page

\[
\boxed{
\text{Target prefix status}
+
\text{previous target word}
+
\text{current source context}
\longrightarrow
\text{New state and target word probability}
}
\]

The context of attention simultaneously controls gating updates and directly participates in vocabulary prediction.
