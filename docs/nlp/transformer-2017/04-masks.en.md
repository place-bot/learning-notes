# Padding Mask and Causal Mask

The mask determines which keys can be read by a query. It operates on the fractional matrix before softmax.

## 1. Padding mask

After completing sentences of different lengths, the padding key should not be read. Let the valid key be 1:

\[
M_{ij}^{\text{pad}}
=
\begin{cases}
0,&\text{key }j\text{valid},\\
-\infty,&\text{key }j\text{is padding}.
\end{cases}
\]

## 2. Causal mask

The position of decoder \(i\) can only read the position \(j\le i\):

\[
M_{ij}^{\text{causal}}
=
\begin{cases}
0,&j\le i,\\
-\infty,&j>i.
\end{cases}
\]

The total score number is

\[
\widetilde{\mathbf S}
=
\frac{\mathbf Q\mathbf K^\top}{\sqrt{d_k}}
+\mathbf M.
\]

The weight of illegal positions is 0 after softmax.

## 3. Move the target to the right

The training goal is

\[
[y_1,y_2,\ldots,y_T].
\]

decoder input is

\[
[\langle BOS\rangle,y_1,\ldots,y_{T-1}].
\]

Output prediction \(y_i\) for location \(i\). The right shift provides the true prefix, and the causal mask prevents the network from peeking at future labels through self-attention.

## 4. Why mask does not hinder training parallelism

The causal mask changes the visible connections and does not create recursive variables:

\[
\mathbf O
=
\operatorname{softmax}(
\mathbf Q\mathbf K^\top/\sqrt{d_k}+\mathbf M)\mathbf V.
\]

All rows can be calculated in one matrix. The result of position \(i\) mathematically only depends on the prefix, but the calculation schedule does not need to wait for the hidden state of position \(i-1\).

## 5. Three attention masks

|sublayer| query | key/value | mask |
|---|---|---|---|
| Encoder self-attention |source location|source location| source padding |
| Decoder self-attention |Target location|Target location| causal + target padding |
| Cross-attention |Target location|encoder output| source padding |

Cross-attention does not use causal source mask; the complete source sentence can be read at each target position.

## 6. Common implementation errors

- The mask direction is reversed;
- Set to zero after softmax but not renormalized;
- Query padding is confused with key padding;
- Not small enough at low precision when using finite negative numbers;
- Mask all in a row, resulting in `NaN`;
- The location offset of the inference cache is inconsistent with the causal mask.
