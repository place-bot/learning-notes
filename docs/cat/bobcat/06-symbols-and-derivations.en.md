# BOBCAT symbol table and necessary derivation

## Symbol lookup table

This chapter is only for reference after reading the main text. The same letters may have different meanings in different documents. Please strictly follow this handout below.
and contextualization of the original BOBCAT paper.

### Data and Index

|symbol|Type|meaning|
| --- | --- | --- |
| \(N\) |positive integer|Number of students in historical training response data|
| \(Q\) |positive integer|total number of item bankitem|
| \(i\) |student index| \(i=1,\ldots,N\) |
| \(j,r\) |item index|The question number in the item bank; \(r\) is often used as a temporary index for summation|
| \(t,\tau\) |Index of topic selection steps|\(t=1,\ldots,n\); superscript \((t)\) indicates steps|
| \(k\) |Inner GD step index| \(k=0,\ldots,K-1\) |
| \(n\) |positive integer|The number of questions each student chooses in the short test|
| \(K\) |positive integer|Number of gradient descent steps for each student-specific adaptation|
| \(Y_{i,j}\) | \(0/1\) |Historical or real-time answers to student \(i\) question \(j\)|
| \(\mathcal O_i\) |item collection|Data middle school student \(i\) questions with observed answers|
| \(\Omega_i^{(t)}\) |item collection|Step \(t\) student \(i\) training candidate questions still available|
| \(\Gamma_i\) |item collection|The held-out meta question of student \(i\)|
| \(S_i^{(t)}\) |item collection|The set of selected topics as of step \(t\)|
| \(j_i^{(t)}\) |question number|Step \(t\) is the question selected by student \(i\)|
| \(j_i^{(1:n)}\) |question number sequence|The entire length of student \(i\)’s topic selection track \(n\)|
| \(\mathcal B\) |student collection|Current mini-batch|

### Model and state

|symbol|Type|meaning|
| --- | --- | --- |
| \(x_i^{(t)}\) |\(Q\) dimensional vector|The response state before the topic selection step \(t\), the component is \(-1,0,1\)|
| \(g(j;\theta_i)\) |probability function|Response model’s prediction of student \(i\)’s correct answer to question \(j\)|
| \(\theta_i\) |scalar or vector|Local response parameters of student \(i\)|
| \(\theta_i^*\) |scalar or vector|Ideal inner optimal solution; approximated by \(\theta_i^{(K)}\) in implementation|
| \(\theta_i^{(k)}\) |scalar or vector|Local parameters after step \(k\) of the inner layer|
| \(\gamma\) |parameter set|Global response model parameters|
| \(\psi\) |parameter set|The shared response parameters that this handout unpacks, such as item difficulty or network weight|
| \(\mu\) |scalar or vector|This handout unpacks the local parameter global initialization or a priori center|
| \(\Pi(\cdot;\phi)\) |strategy|item selection algorithm|
| \(\phi\) |parameter vector|Question selector neural network parameters|
| \(z_{i,j}^{(t)}\) |real numbers|The topic selection network gives the logit of the candidate question \(j\)|
| \(b_j\) |real numbers|Difficulty of 1PL IRT mid-term question \(j\)|
| \(p_{i,j}\) |\(0\) to \(1\)|Predict probability of correct answer|

### Loss, optimization and gradient

|symbol|Type|meaning|
| --- | --- | --- |
| \(\ell(y,p)\) |scalar function|Binary cross-entropy of a question|
| \(\mathcal L(\theta_i,\Gamma_i)\) |scalar|Total loss of meta questions for student \(i\)|
| \(\mathcal L_i'(\theta_i)\) |scalar|The inner training target of student \(i\)|
| \(\mathcal J(\gamma,\phi)\) |scalar|Average outer level goals for all students|
| \(R(\gamma,\theta_i)\) |scalar|Regular terms that constrain local parameters near global values|
| \(\alpha\) |positive real numbers|Inner layer local parameter learning rate|
| \(\eta_1\) |positive real numbers|Global response parameter outer learning rate|
| \(\eta_2\) |positive real numbers|Topic selector parameter outer learning rate|
| \(\nabla_\theta f\) |vector|Gradient of \(f\) versus \(\theta\)|
| \(\nabla_\theta^2f\) |matrix|Hessian of \(f\) vs. \(\theta\)|
| \(H\) |matrix|Abbreviation for Hessian|
| \(b_i\) |scalar|Baseline/control variate that reduces variance in equation (8)|
| \(w_j\) |\(0/1\) or slack weight|Step \(t\) Question \(j\) Whether to enter the inner layer loss|
| \(\mathcal I_i(j)\) |scalar|The influence function score of question \(j\) on students \(i\)|
| \(\lambda,\delta\) |nonnegative real numbers|Regular strength or Hessian damping|

### Operator

|symbol|meaning|
| --- | --- |
| \(\operatorname*{arg\,min}_x f(x)\) |Return \(x\) that minimizes \(f(x)\); the minimum function value is recorded as \(\min_x f(x)\)|
| \(\mathbb{E}[\cdot]\) |Taking the expectation of a random variable|
| \(\Pr(\cdot)\) |Probability|
| \(\sim\) |sample from a distribution|
| \(\lvert S\rvert\) |The number of set elements; when used as a scalar, it can also represent an absolute value, depending on the context|
| \(\setminus\) |set difference|
| \(\mathbb{I}(A)\) |It is 1 when the event \(A\) is established, otherwise it is 0|
| \(\operatorname{stopgrad}\) |The forward value is retained and the reverse gradient is set to 0.|
| \((\cdot)^\mathsf{T}\) |Vector or matrix transpose|
|\(\equiv\) or \(:=\)|Define an abbreviation or identity representation|

## Necessary calculus derivation

### sigmoid derivative

\[
\sigma(z)=\frac{1}{1+e^{-z}}.
\]

Find the derivative:

\[
\begin{aligned}
\sigma'(z)
&=-(1+e^{-z})^{-2}(-e^{-z})\\
&=\frac{e^{-z}}{(1+e^{-z})^2}\\
&=\frac{1}{1+e^{-z}}
\left(1-\frac{1}{1+e^{-z}}\right)\\
&=\sigma(z)(1-\sigma(z)).
\end{aligned}
\]

### Derivative of binary cross-entropy with respect to logit

Let \(p=\sigma(z)\),

\[
\ell(y,p)=-y\log p-(1-y)\log(1-p).
\]

First derive the derivative of \(p\):

\[
\frac{\partial\ell}{\partial p}
=-\frac{y}{p}+\frac{1-y}{1-p}.
\]

Take another ride

\[
\frac{\partial p}{\partial z}=p(1-p).
\]

get

\[
\begin{aligned}
\frac{\partial\ell}{\partial z}
&=
\left(-\frac{y}{p}+\frac{1-y}{1-p}\right)p(1-p)\\
&=-y(1-p)+(1-y)p\\
&=p-y.
\end{aligned}
\]

\(z=\theta-b\) in 1PL, so \(\partial z/\partial\theta=1\), thus
\(\partial\ell/\partial\theta=p-y\)。

### softmax and log-softmax derivatives

Order

\[
\pi_a=\frac{e^{z_a}}{\sum_s e^{z_s}}.
\]

Derive \(z_r\):

\[
\frac{\partial\pi_a}{\partial z_r}
=\pi_a\left(\mathbb{I}(a=r)-\pi_r\right).
\]

Then divide by \(\pi_a\):

\[
\frac{\partial\log\pi_a}{\partial z_r}
=\mathbb{I}(a=r)-\pi_r.
\]

This means that the gradient that increases the log probability of the selected action while depressing the probabilities of other actions.

### score-function identity

For discrete \(X\):

\[
\begin{aligned}
\nabla_\phi\mathbb{E}_{X\sim p_\phi}[f(X)]
&=\nabla_\phi\sum_x p_\phi(x)f(x)\\
&=\sum_x \nabla_\phi p_\phi(x)f(x)\\
&=\sum_x p_\phi(x)
\frac{\nabla_\phi p_\phi(x)}{p_\phi(x)}
f(x)\\
&=\sum_x p_\phi(x)f(x)\nabla_\phi\log p_\phi(x)\\
&=\mathbb{E}[f(X)\nabla_\phi\log p_\phi(X)].
\end{aligned}
\]

If \(f\) also directly depends on \(\phi\), it should be added
\(\mathbb{E}[\nabla_\phi f(X,\phi)]\). BOBCAT mainly uses score-function after fixing the discrete trajectory.
Handle action distribution dependencies.

### baseline does not change expectations

As long as \(b\) does not depend on the current sampling action,

\[
\begin{aligned}
\mathbb{E}[b\nabla_\phi\log p_\phi(X)]
&=b\sum_xp_\phi(x)\nabla_\phi\log p_\phi(x)\\
&=b\sum_x\nabla_\phi p_\phi(x)\\
&=b\nabla_\phi\sum_xp_\phi(x)\\
&=b\nabla_\phi 1=0.
\end{aligned}
\]

### The implicit function theorem obtains the influence function

Define weighted inner goals

\[
F(\theta,w)
=F_0(\theta)+\sum_jw_j\ell_j(\theta).
\]

optimal point satisfies

\[
G(\theta^*(w),w)
:=\nabla_\theta F(\theta^*(w),w)=0.
\]

Derive \(w_j\):

\[
\frac{\partial G}{\partial\theta}
\frac{\mathrm d\theta^*}{\mathrm dw_j}
+
\frac{\partial G}{\partial w_j}
=0.
\]

Among them

\[
\frac{\partial G}{\partial\theta}
=\nabla_\theta^2F=H,
\qquad
\frac{\partial G}{\partial w_j}
=\nabla_\theta\ell_j.
\]

So

\[
\frac{\mathrm d\theta^*}{\mathrm dw_j}
=-H^{-1}\nabla_\theta\ell_j.
\]

If the outer layer loss is \(L(\theta^*)\), continue the chain rule:

\[
\frac{\mathrm dL}{\mathrm dw_j}
=
\nabla_\theta L^\mathsf{T}
\frac{\mathrm d\theta^*}{\mathrm dw_j}
=
-\nabla_\theta L^\mathsf{T}
H^{-1}
\nabla_\theta\ell_j.
\]

### Why you shouldn’t explicitly invert the Hessian

The formula is written as \(H^{-1}g_j\), and numerical implementation usually solves linear equations.

\[
Hv=g_j
\]

Get \(v\), then calculate \(-g_{\mathrm{meta}}^\mathsf{T} v\). Explicit construction of \(H^{-1}\) is slower and more memory intensive,
It's also more unstable. Conjugate gradients, LiSSA, or automatically differentiated Hessian-vector products all avoid the complete inverse matrix.
