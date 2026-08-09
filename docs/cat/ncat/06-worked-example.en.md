# Complete hand calculation example

The following uses four questions and two-dimensional embedding to complete an NCAT forward calculation and a TD update. In order to make each step calculable by hand, the attention projection matrix is ​​the unit matrix, and FFN is temporarily processed by identity mapping. These matrices in real networks are learned by training.

## 1. Current status

item bank is

\[
\mathcal J=\{q_1,q_2,q_3,q_4\},
\qquad d=2.
\]

Students have:

- Correct answer \(q_1,q_3\);
- Wrong answer \(q_2\);
- \(q_4\) has not been answered yet.

Correct answer embedding is set to

\[
\mathbf e_{q_1}^1=[1,0],
\qquad
\mathbf e_{q_3}^1=[0,1],
\]

Wrong answer embedding is set to

\[
\mathbf e_{q_2}^0=[0.8,0.2].
\]

## 2. Correct answer channel self-attention

The correct answer matrix is

\[
\mathbf E_t^1
=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}.
\]

Scale points score:

\[
\frac{\mathbf E_t^1(\mathbf E_t^1)^\top}{\sqrt2}
=
\begin{bmatrix}
0.707&0\\
0&0.707
\end{bmatrix}.
\]

Line-by-line softmax:

\[
W_{\mathrm{att}}^1
\approx
\begin{bmatrix}
0.67&0.33\\
0.33&0.67
\end{bmatrix}.
\]

After multiplying by value:

\[
\mathbf F_t^1
\approx
\begin{bmatrix}
0.67&0.33\\
0.33&0.67
\end{bmatrix}.
\]

The first line indicates that the representation of \(q_1\) still mainly comes from itself, while absorbing the information of \(q_3\); the same applies to the second line.

## 3. Wrong answer channel self-attention

The wrong answer channel is only \(q_2\), and its attention weight can only be 1:

\[
\mathbf F_t^0=[0.8,0.2].
\]

## 4. Summarize from the correct answer channel to the wrong answer position

The scaled dot product of \(q_2\) and the two correct answers is

\[
A
=
\begin{bmatrix}
\dfrac{[0.8,0.2][1,0]^\top}{\sqrt2}
&
\dfrac{[0.8,0.2][0,1]^\top}{\sqrt2}
\end{bmatrix}
\approx
\begin{bmatrix}
0.566&0.141
\end{bmatrix}.
\]

Softmax by row:

\[
\widetilde A^0
\approx
[0.605,0.395].
\]

Therefore, the cross-channel features obtained from the correct answer channel for the wrong answer question \(q_2\) are

\[
\mathbf F_t^{1\rightarrow0}
=
[0.605,0.395]
\begin{bmatrix}
0.67&0.33\\
0.33&0.67
\end{bmatrix}
\approx
[0.536,0.464].
\]

The result is more in the direction of \(q_1\) because the dot product of \(q_2\) and \(q_1\) is larger.

## 5. Summarize from the wrong answer channel to the correct answer position

There is only one question in the wrong answer channel. After normalizing each correct question by another dimension, the weight of the only incorrect question is 1:

\[
\mathbf F_t^{0\rightarrow1}
=
\begin{bmatrix}
0.8&0.2\\
0.8&0.2
\end{bmatrix}.
\]

Average pooling results in

\[
\overline{\mathbf f}_t^{0\rightarrow1}
=[0.8,0.2].
\]

## 6. Four-way pooling and splicing

The four fixed-dimensional vectors are

\[
\overline{\mathbf f}_t^0=[0.8,0.2],
\]

\[
\overline{\mathbf f}_t^1
=
\frac12
\left(
[0.67,0.33]+[0.33,0.67]
\right)
=[0.5,0.5],
\]

\[
\overline{\mathbf f}_t^{1\rightarrow0}
=[0.536,0.464],
\]

\[
\overline{\mathbf f}_t^{0\rightarrow1}
=[0.8,0.2].
\]

Splicing according to the four-way sequence of the paper:

\[
\mathbf u_t
=
[0.8,0.2,\,
0.5,0.5,\,
0.536,0.464,\,
0.8,0.2]
\in\mathbb R^8.
\]

The specific implementation only needs to keep the same order of training and inference.

## 7. Policy layer and action mask

Assume that the first layer maps the eight-dimensional vector into

\[
\mathbf h=[0.9,0.4],
\]

Last layer output

\[
Q_\phi(s_t,\cdot)
=
[0.30,0.10,0.45,0.70].
\]

Question \(q_1,q_2,q_3\) has been answered, after masking:

\[
\widetilde Q_\phi(s_t,\cdot)
=
[-\infty,-\infty,-\infty,0.70].
\]

Therefore, this step chooses

\[
q_t=q_4.
\]

The output of this forward process is the long-term question value of each discrete question. Student parameters are estimated from cumulative responses by the adjacent response model.

## 8. Read answers and update students

The offline log shows that the student answered 0 for \(q_4\). status updated to

\[
s_{t+1}
=
\{
(q_1,1),(q_2,0),(q_3,1),(q_4,0)
\}.
\]

The response model uses these four responses to re-estimate the student parameters. Assume that the BCE of the updated parameters on the query set is

\[
\mathcal L_M
\left(
\mathcal D_i^u,\widehat\theta_i^{\,t}
\right)
=0.25.
\]

So

\[
r_t=-0.25.
\]

## 9. Terminate transition’s TD update

If \(q_4\) is the last step, then \(d_t=1\):

\[
y_t=r_t=-0.25.
\]

The network previously gave

\[
Q_\phi(s_t,q_4)=0.70.
\]

The one-sample TD MSE is

\[
\mathcal L_{\mathrm{TD}}
=
\left(
0.70-(-0.25)
\right)^2
=
0.9025.
\]

Gradient descent will adjust the prediction of \(q_4\) in this state to \(-0.25\).

## 10. TD update for non-terminating transition

If there are still legal questions and the maximum target Q value of the next state is

\[
\max_{q'}Q_{\bar\phi}(s_{t+1},q')=-0.10,
\qquad
\gamma=0.8,
\]

rule

\[
y_t
=
-0.25+0.8(-0.10)
=
-0.33.
\]

The goal includes both the current query loss and the expected loss of future topic selections. Q-learning only needs to compare values:

\[
-0.20>-0.70,
\]

Therefore, actions with smaller cumulative losses will have larger Q values that are closer to 0.

## 11. Differences in goals between the two rewards

Original paper used

\[
r_t=-L_t.
\]

An alternative design that could be investigated is loss improvement:

\[
r_t^\Delta=L_{t-1}-L_t.
\]

It's undiscounted and telescoping happens:

\[
\sum_{t=1}^{T}
\left(
L_{t-1}-L_t
\right)
=
L_0-L_T,
\]

The primary emphasis is on ultimate improvement. original definition

\[
\sum_{t=1}^{T}-L_t
\]

Continuous rewards keep the query loss low at each intermediate step, and therefore fit more closely with the outer goal of "the test may stop at any step".

The next page uses all the numerical values of the original paper to check the effect of the method: [Experimental design, complete results and result analysis](07-experiments.md).
