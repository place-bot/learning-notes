# identifiability, label swapping and counterexamples

## Necessary conditions provided by T equation

The correct parameters should satisfy

\[
T_{\boldsymbol c,\boldsymbol g}(Q)\boldsymbol p
=
\boldsymbol\beta
\]

overall version. Q can only be distinguished by these moments if each error \(Q'\) fails to satisfy the same set of equations under legal parameters.

## Completeness

Q Complete means that each attribute has a question that only requires that attribute. After rearrangement, Q contains a unit matrix \(K\times K\).

Summary of the theoretical properties of the 2012 article: Under guessing known, true Q complete and other technical conditions,

\[
\Pr(\widehat Q\sim Q)\to1,
\]

Among them, \(\sim\) represents only the difference column replacement.

## Why can only column replacement be performed?

Swapping the two columns of Q simultaneously swaps the corresponding components in all attribute profiles without changing the response distribution. Purely reactive data only sees the structure of the underlying dimensions and cannot recognize external semantics such as "attribute 1 is called the common part of the fraction, and attribute 2 is called borrowing".

So the strongest conclusion is to recover the column permutation equivalence class of Q.

## Theoretical source boundary

The above consistent conclusion is established by the theoretical work of Liu, Xu and Ying cited in the paper. The 2012 application paper does not give a complete proof. The complete condition and proof chain need to be checked separately in the 2013 theory topic.

## Counterexample

Given in the original text

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&0
\end{pmatrix}
\]

and

\[
Q'=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix}.
\]

When the \(s_j=g_j=.2\) and attribute profiles of each question are uniform, another group of \(s',g',p'\) can be found, so that the two contain the same reaction distribution. Therefore, completeness alone is not enough to cover loose scenarios where all parameters are unknown.

## Diverse items

The paper empirically points out that item banks with richer q-vectors are usually easier to identify. If many questions repeat the same attribute combination:

- Multiple lines of T may be repeated or highly related;
- Some attribute interactions lack observation constraints;
- Error Q is more easily compensated by nuisance parameters.

## Recognition and calculation

Even if the population distribution uniquely identifies Q, the finite sample target may still be flat and the hill climbing algorithm may stop at a local solution. In turn, the algorithm's recovery of Q in a certain batch of simulations cannot replace the overall identifiability proof.
