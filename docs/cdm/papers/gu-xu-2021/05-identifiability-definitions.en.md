# Strict identification, general identification and column label exchange

## 1. Observation Equivalence

Two sets of objects are observed to be equivalent, meaning

\[
\Pr(\boldsymbol R=\boldsymbol r\mid Q,\Theta,\boldsymbol p)
=
\Pr(\boldsymbol R=\boldsymbol r\mid
\bar Q,\bar\Theta,\bar{\boldsymbol p})
\]

to all

\[
\boldsymbol r\in\{0,1\}^{J}
\]

Established at the same time.

## 2. Column label exchange

If the 1st and 2nd columns of \(Q\) are interchanged and the attribute profile is relabeled simultaneously, the observation distribution remains unchanged. For papers

\[
\bar Q\sim Q
\]

Indicates that the difference between the two Qs is only one column permutation.

The identification conclusion can reach at most "unique in the sense of column substitution". This belongs to the inherent label symmetry of latent variable models.

## 3. Joint strict identification

If the observations are equivalent, it follows that

\[
(\bar Q,\bar\Theta,\bar{\boldsymbol p})
\sim
(Q,\Theta,\boldsymbol p),
\]

It is said that the combination of the three is strictly identifiable.

"Strict" means that every legal point in the parameter space satisfies uniqueness. The loss of uniqueness of a special point is enough to destroy strict identification.

## 4. Joint pan-recognition

Let the free parameter space \(\vartheta_Q\subset\mathbb R^m\) of \(Q\) be given. Define unrecognizable collections

\[
\vartheta_{\mathrm{non}}
=
\left\{
(\Theta,\boldsymbol p):
\begin{array}{l}
\exists(\bar Q,\bar\Theta,\bar{\boldsymbol p})
\nsim(Q,\Theta,\boldsymbol p),\\
\Pr(\boldsymbol R\mid Q,\Theta,\boldsymbol p)
=
\Pr(\boldsymbol R\mid\bar Q,\bar\Theta,\bar{\boldsymbol p})
\end{array}
\right\}.
\]

If the Lebesgue measure of \(\vartheta_{\mathrm{non}}\) in \(\mathbb R^m\) is 0, it is said to be jointly universally identifiable.

## 5. Local and global

- Local identification: There is no other set of equivalent parameters in a certain neighborhood of the true parameters;
- Global identification: There is no other set of equivalent parameters in the entire parameter space;
- Local universal recognition: Except for the zero test set, the true parameters are unique in the local neighborhood;
- Global universal recognition: Except for the zero test set, the true parameters are unique in the entire space.

The strong and weak relationship can be written as

\[
\text{Strict global identification}
\Longrightarrow
\text{global recognition}
\Longrightarrow
\text{Local pan-recognition}.
\]

The backward derivation usually does not hold.

## 6. Intuition about limited samples

Universal recognition allows for a zero-test algebraic set. Even if the true parameters do not fall on this set, as long as they are very close to it, the limited sample likelihood surface will flatten, and the estimation variance and optimization difficulty may increase.

Therefore:

\[
\text{Pan-recognition}
\]

gives a theoretical basis for estimates that are almost everywhere consistent;

\[
\text{Distance from unrecognizable set}
\]

Continue to control the limited sample difficulty.
