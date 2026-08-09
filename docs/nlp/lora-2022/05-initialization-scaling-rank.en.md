# Initialization, scaling and ranking

## 1. Zero initial increment

Thesis uses:

\[
\mathbf A\sim\mathcal N(0,\sigma^2),
\qquad
\mathbf B=\mathbf 0.
\]

So at the beginning

\[
\Delta W=BA=0,
\]

The model output is completely consistent with the pretraining base.

## 2. Who should update first in the first step?

Let the gradient of the loss to \(\Delta W\) be \(G\). Ignore scaling:

\[
\frac{\partial\mathcal L}{\partial B}
=
G A^\top,
\qquad
\frac{\partial\mathcal L}{\partial A}
=
B^\top G.
\]

Initial \(B=0\), so the first step \(A\) gradient is 0, \(B\) gets updated first. After \(B\neq0\), both learn together.

## 3. Zoom

\[
s=\frac{\alpha}{r},
\qquad
\Delta h=sBAx.
\]

The paper sets \(\alpha\) as the rank for the first attempt and does not adjust parameters systematically. Scaling helps control the update amplitude when rank changes; \(\alpha\) still interacts with learning rate.

## 4. How to choose Rank

In Table 6 of the original paper GPT-3, the result of \(r=1,2,4,8,64\) is very close when Q/V is adapted at the same time. WikiSQL is 73.4, 73.3, 73.7, 73.8, 73.5; MultiNLI is 91.3, 91.4, 91.3, 91.6, 91.4.

This shows that low rank is sufficient for these tasks, but does not prove that rank 1 is sufficient for all tasks. Domain differences, data volume, number of modules, and task complexity may change requirements.

## 5. Rank and module coverage

When setting a fixed budget:

\[
\text{More modules}\times\text{smaller rank}
\]

with

\[
\text{Fewer modules}\times\text{Larger rank}
\]

Joint selection is required. The result of the original paper favors the former, but modern models should be determined by validation set and resource constraints.

## 6. LoRA dropout

The official library supports using dropout on low-rank branch inputs. It is an implementation layer regularization option and is not a necessary component of Core Formula No. 3; the behavior during training and deployment must follow PyTorch train/eval semantics.
