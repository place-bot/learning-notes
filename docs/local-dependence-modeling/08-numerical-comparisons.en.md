# Numerical comparisons

All matrices are ordered as

\[
\begin{pmatrix}p_{00}&p_{01}\\p_{10}&p_{11}\end{pmatrix}.
\]

The examples establish observational similarity, not proof that one generating mechanism is true.

## Prerequisite Table A

An LI model with \(b_1=0,b_2=4,a_1=a_2=1\) gives

\[
\text{LI-3}=\begin{pmatrix}.491&.009\\.481&.019\end{pmatrix}.
\]

RD with \(d=1\) gives

\[
\text{RD-1}=\begin{pmatrix}.497&.003\\.453&.047\end{pmatrix}.
\]

A chain-based Theta-SLM needs only \(b_2=3\):

\[
\Theta\text{-SLM-1}=\begin{pmatrix}.500&0\\.453&.047\end{pmatrix}.
\]

Adding \(\eta_2=.006,\beta_2=.06\) gives

\[
\Theta\text{-SLM-2}=\begin{pmatrix}.497&.003\\.453&.047\end{pmatrix},
\]

matching RD-1 with a less extreme difficulty. The rare \(01\) cell is explicitly assigned to the error
process rather than the mastery structure.

OD with \(b_1=0,b_2=4,b_{12}=-1\) gives

\[
\text{OD-1}=\begin{pmatrix}.653&.013\\.257&.078\end{pmatrix}.
\]

LKS with \(b_1=1,b_2=2\) and no errors gives

\[
\text{LKS-A1}=\begin{pmatrix}.660&0\\.261&.079\end{pmatrix}.
\]

Small guessing/slipping parameters produce

\[
\text{LKS-A2}=\begin{pmatrix}.652&.013\\.257&.079\end{pmatrix},
\]

nearly matching OD-1.

## Equally informative Table B

Without a \(g\)-process, LKS assigns probability only to \(00\) and \(11\):

\[
\pi(11\mid\theta)
=\frac{e^{2(\theta-\bar b_{12})}}{1+e^{2(\theta-\bar b_{12})}},
\qquad
\bar b_{12}=\frac{b_1+b_2}{2}.
\tag{39}
\]

The pair behaves as a virtual item with average difficulty and discrimination 2. Different difficulty
pairs with the same average generate the same latent table.

CD and LKS can also match exactly:

\[
\text{CD-B1}=\text{LKS-B4}
=\begin{pmatrix}.239&.145\\.145&.470\end{pmatrix}.
\]

CD uses a joint interaction; LKS uses restricted support plus guessing and slipping. Distinguishing them
requires substantive design information, larger response patterns, interventions on order or stimulus,
or external validation--not only one \(2\times2\) table.

