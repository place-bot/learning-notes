# Why low-rank updates are effective: Subspace analysis of the paper

## 1. Three questions

The paper is researched on GPT-3:

1. Which matrices are adapted;
2. How small a rank is enough;
3. What is the relationship between \(\Delta W\) and pretraining \(W\).

## 2. Subspace similarity

Do SVD on the \(A\) learned in rank 8 and rank 64, take the first \(i,j\) right singular directions, and define

\[
\phi(A_8,A_{64},i,j)
=
\frac{
\|U_{A_8,i}^\top U_{A_{64},j}\|_F^2
}{
\min(i,j)
}
\in[0,1].
\]

1 means the subspace is fully contained, 0 means orthogonal.

## 3. Observation

The strongest singular directions of rank 8 and rank 64 obviously overlap, and the overlap in other directions is weak; different random seeds can also learn some common directions. The authors therefore believe that the intrinsic rank of effective task updates is very low, and additional directions with larger ranks may contain more training noise.

## 4. Relationship with \(W\)

The paper projects pretraining \(W_q\) to the left and right singular subspaces of \(\Delta W_q\) and compares the Frobenius norm. At rank 4:

\[
\|W_q\|_F=61.95,\qquad
\|\Delta W_q\|_F=6.91,
\]

The \(W_q\) norm along the \(\Delta W\) subspace projection is 0.32, while the \(W_q\) norm along its own apex direction is 21.67 and the random direction is 0.02.

The author explains that: \(\Delta W\) is more related to \(W\) than random directions, but does not simply repeat the main singular direction of \(W\); it may amplify the task characteristics that already exist but are not emphasized in pretraining.

## 5. Explain limitations

- The analysis focuses on certain layers and tasks of GPT-3;
- Factor \(A,B\) is not unique;
- The overlap of subspaces is an empirical correlation and has not yet been proven by a causal mechanism;
- "Low intrinsic rank" depends on the accuracy threshold, task, target module and optimization process;
- Good performance at rank 1 does not mean that the complete fine-tuning update itself is strictly rank 1.

## 6. Practical Conclusion

First use a small rank to cover key modules, and then increase the rank or module through the validation set. This is usually more consistent with the paper evidence than using a large rank by default. It is necessary to record the parameter budget and target modules at the same time.
