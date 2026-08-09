# BOBCAT Framework: Formula (3) to Formula (11) and Algorithm 1

## First create a simulated short test

### fixed length n

Thesis research fixed length CAT. For student \(i\), the question selector selects \(n\) questions in total:

\[
\{j_i^{(1)},j_i^{(2)},\ldots,j_i^{(n)}\}.
\]

Here \(n\) is the short measurement length, which satisfies

\[
n\leq |\Omega_i^{(1)}|.
\]

The vertical bar \(|S|\) represents the number of elements in the set \(S\). Therefore, the right side is the number of candidate questions available to student \(i\) at the beginning.

After each question is selected, it is deleted from the candidate set:

\[
\Omega_i^{(t+1)}
=\Omega_i^{(t)}\setminus\{j_i^{(t)}\}.
\]

Backslash indicates set difference. This update ensures that the same student will not receive the same question twice.

### The first official appearance of the state vector

Before selecting the topic in step \(t\), BOBCAT codes the students’ answers so far into

\[
x_i^{(t)}\in\{-1,0,1\}^{Q}.
\]

It's not written in bold, but it is a vector of length \(Q\). The \(j\) component is defined as

\[
x_{i,j}^{(t)}
=
\begin{cases}
1, & \text{Question \(j\) has been selected previously and the student answered correctly},\\
-1, & \text{Question \(j\) has been selected previously and the student answered it incorrectly},\\
0, & \text{Question \(j\) has not been selected yet}.
\end{cases}
\]

!!! example "Small example: status in item bank for five questions"
    The item bank has \(Q=5\) questions. If the student first answers question 2 correctly and then answers question 5 incorrectly, the next step is

    \[
    x_i^{(3)}=(0,1,0,0,-1).
    \]

    The superscript is 3 because we are now making the third selection. The vector not only stores the answer, but also stores which questions have not been asked through zero elements.

### Why is the status not explicitly recorded in chronological order?

The paper assumes that students' true abilities are static during a short test. If you answer question 2 first and then answer question 5, then answer question 5 first and then answer
Question 2: The currently known information is the same. Therefore, the status only records the "question number and answer" and does not record the time when the answer occurred.
The topic selection network is designed to be insensitive to historical item order.

This static assumption will fail if there is significant learning, fatigue, speed changes, or cueing effects during testing. At that point the status should be added
Time, response duration, or sequence encoding, response models may also require dynamic capabilities. This extension goes beyond the original paper.

### From logits to available action distribution

The question selection network reads \(x_i^{(t)}\) and outputs a logit for each question in the item bank. logit is the unnormalized real fraction.
Add a mask of approximately negative infinity to selected questions or questions without historical answers, and then use softmax:

\[
\Pi(j\mid x_i^{(t)},\Omega_i^{(t)};\phi)
=
\frac{\exp(z_{i,j}^{(t)})}
{\sum_{r\in\Omega_i^{(t)}}\exp(z_{i,r}^{(t)})},
\qquad j\in\Omega_i^{(t)}.
\]

Here \(z_{i,j}^{(t)}\) is the logit of the question \(j\) given by the Internet, and the letters \(r\) are just the denominator for traversing the candidate questions
Temporary index. After softmax, the probabilities of all optional questions are non-negative and sum to 1.

### Sampling and greedy selection

Probabilistic strategies can sample:

\[
j_i^{(t)}
\sim
\Pi(x_i^{(t)},\Omega_i^{(t)};\phi).
\]

The notation \(\sim\) means "draw from the right-hand distribution". You can also take the maximum probability question during deployment:

\[
j_i^{(t)}
=\operatorname*{arg\,max}_{j\in\Omega_i^{(t)}}
\Pi(j\mid x_i^{(t)};\phi).
\]

Preserving randomness during training is helpful for exploration and policy gradient; the Approx code uses hard argmax in the forward direction and approximates it in the reverse direction.
into softmax.

## global and local in response model

### First treat the global response parameters as a parameter container

The paper uses \(\gamma\) to represent global response model parameters. It can hold a set of parameters, dimensions
Can also be different from \(\theta_i\). To avoid abstract confusion, we split it into

\[
\gamma=(\psi,\mu).
\]

\(\psi\) represents the part that is shared across students and fixed within the inner layer, such as all item difficulties or neural network weights;
\(\mu\) represents a global initialization or a priori center for student-specific parameters. What is suitable for students \(i\) is
\(\theta_i\), the initial value is set to

\[
\theta_i^{(0)}=\mu.
\]

When the outer layer learns \(\psi\) and \(\mu\) at the same time, both belong to \(\gamma\).

### IRT Example

In 1PL IRT, one can write

\[
g(j;\theta_i,\psi)
=\sigma(\theta_i-b_j),
\qquad
\psi=(b_1,\ldots,b_Q).
\]

item difficulty \(b_j\) Shared across students. The inner layer only updates the student's ability \(\theta_i\) based on a small number of answers and does not update the item.
Difficulty. The global student ability mean \(\mu\) is used as the initial ability of each new student.

The paper writes \(g(j;\theta_i)\) to simplify the notation, and implicitly fixes the global item parameters in \(g\). cannot while reading
Therefore, it is mistakenly believed that the response model has no item parameters at all.

### Neural network example

The neural response model can accept student embedding \(h_i\), and generate logits for all questions through the shared network:

\[
o_i=W_2\,\rho(W_1 h_i+c_1)+c_2.
\]

Here \(h_i\) corresponds to the local parameters, and \(W_1,W_2,c_1,c_2\) is the global shared weight and bias.
\(\rho\) is a nonlinear function such as ReLU. The \(j\)th output is given after sigmoid

\[
g(j;h_i)=\sigma(o_{i,j}).
\]

The inner layer can only update \(h_i\), and the shared network is fixed. BiNN in official experiments uses 256-dimensional student-specific vectors,
The response network has a 256-node hidden layer, ReLU, dropout and sigmoid output.

### Regular terms between global and local parameters

A small number of answers is not enough to stably estimate high-dimensional local parameters, so the ideal inner target is added

\[
R(\gamma,\theta_i).
\]

For example, one-dimensional IRT is available

\[
R(\gamma,\theta_i)
=\frac{\lambda}{2}(\theta_i-\mu)^2,
\]

Among them, \(\lambda\geq0\) controls the penalty for local capabilities deviating from the global center \(\mu\). From a probability perspective, this corresponds to
Negative log part of the Gaussian prior for \(\theta_i\sim N(\mu,\lambda^{-1})\).

The actual \(K\)-step GD version of the paper omits explicit regularization terms, starting from global initialization and taking only a small number of steps.
Early stopping is considered an implicit regularity. Ideal equation (4) gives the target definition, and equation (6) gives the truncated realization.

### What exactly does model-agnostic guarantee?

BOBCAT only requires that the response model can output probabilities based on item and local student parameters, and that the inner layer adaptation and outer layer loss can
Find the gradient. It does not guarantee that any black box model can be used without modification. Discrete, non-differentiable, or extremely computationally heavy response models still require
Extra estimator. The more precise meaning of model-agnostic is that the framework is not bound to a certain IRT equation.

## Original paper formula (3): What exactly is minimized in the outer layer?

### Let’s look at a student first

Student \(i\) has a meta question set \(\Gamma_i\). After completing the short test selection and completing the inner layer adaptation, the student-specific
Parameter \(\theta_i^*\). The meta loss of this student is defined as

\[
\mathcal L(\theta_i^*,\Gamma_i)
=
\sum_{j\in\Gamma_i}
\ell\!\left(Y_{i,j},g(j;\theta_i^*)\right).
\]

The \(j\) here just traverses the questions in the meta set. It is the same as the one selected in step \(t\)
\(j_i^{(t)}\) The roles are different.

If \(\mathcal L\) is small, it means that \(\theta_i^*\) adapted to only a small number of selected questions can predict that the student has more unused
Respond appropriately.

### Then average across all students

The outer goal of BOBCAT is

\[
\min_{\gamma,\phi}
\frac{1}{N}\sum_{i=1}^{N}
\sum_{j\in\Gamma_i}
\ell\!\left(Y_{i,j},g(j;\theta_i^*)\right)
\equiv
\min_{\gamma,\phi}
\frac{1}{N}\sum_{i=1}^{N}
\mathcal L(\theta_i^*,\Gamma_i).
\tag{3}
\]

The colon equivalent \(\equiv\) here means that the right side just abbreviates the inner sum of the left side as
\(\mathcal L(\theta_i^*,\Gamma_i)\). The paper uses \(:=\) to define this abbreviation.

### Why can’t I see the training loss of the selected topic in the target?

The loss of selected questions is used for inner layer adaptation and does not directly serve as outer layer results. If the outer layer only rewards the questions selected by model fit, the question selector
It may select repeated questions that are most likely to be fit by the current model, but it cannot help predict the remaining questions. The meta loss is caused by the selected topic.
Student representations have extrapolation value.

### How to enter formula (3) for the global response model and topic selector

Equation (3) only says \(\theta_i^*\) on the surface, but it should be expanded in the mind as

\[
\theta_i^*=\theta_i^*(\gamma,\phi).
\]

\(\gamma\) determines global initialization, shared response model and regular center; \(\phi\) determines which training questions are selected.
So to write more completely:

\[
\mathcal J(\gamma,\phi)
=\frac1N\sum_i
\mathcal L\!\left(\theta_i^*(\gamma,\phi),\Gamma_i;\gamma\right).
\]

Here \(\mathcal J\) is our new name for the entire set of outer targets. The final semicolon \(\gamma\) reminds readers:
Shared item parameters may also be directly involved in meta prediction.

### Does equation (3) optimize expectation or one-time sampling?

If the topic selector is a random strategy, the strict outer goal should set expectations for possible topic selection trajectories:

\[
\mathcal J(\gamma,\phi)
=\frac1N\sum_i
\mathbb{E}_{j_i^{(1:n)}\sim\Pi_\phi}
\left[
\mathcal L\!\left(
\theta_i^*(\gamma,j_i^{(1:n)}),\Gamma_i
\right)
\right].
\]

The paper only explicitly states this expectation in equation (7). Equation (3) can be regarded as a compact two-level objective, the expectation of the random strategy
Dependencies are left to be unwrapped during gradient derivation.

## Original paper formula (4) and formula (5): inner layer and topic selection

### Ideal inner layer problem

For student \(i\), the short test will select \(n\) questions. The ideal local parameters are given by

\[
\theta_i^*
=
\operatorname*{arg\,min}_{\theta_i}
\left[
\sum_{t=1}^{n}
\ell\!\left(
Y_{i,j_i^{(t)}},
g(j_i^{(t)};\theta_i)
\right)
+
R(\gamma,\theta_i)
\right]
\equiv
\operatorname*{arg\,min}_{\theta_i}\mathcal L_i'(\theta_i).
\tag{4}
\]

The newly defined \(\mathcal L_i'(\theta_i)\) at the end of the formula is the inner target of student \(i\). Apostrophe is used with meta loss
\(\mathcal L(\theta_i^*,\Gamma_i)\) distinction.

### Read and sum layer by layer

The sum subscript \(t=1,\ldots,n\) traverses the **topic selection moment**. At the \(t\) moment, the actual question number is
\(j_i^{(t)}\), the answer read from the data is \(Y_{i,j_i^{(t)}}\). The response model's prediction for this question is
\(g(j_i^{(t)};\theta_i)\). Each selected topic generates a cross-entropy, and finally adds a regular term.

\(t\) cannot be interchanged with \(j\). \(t\) is the position in the short test, and \(j\) is the item bank number. For example step 2 might
Select item bank question 137, at this time \(t=2\), \(j_i^{(2)}=137\).

### Formula (5) specifies where these questions come from

Question \(t\) is selected by the question selector based on previous responses:

\[
j_i^{(t)}
\sim
\Pi\!\left(
Y_{i,j_i^{(1)}},\ldots,Y_{i,j_i^{(t-1)}};\phi
\right),
\qquad
j_i^{(t)}\in\Omega_i^{(t)}.
\tag{5}
\]

The paper then uses the state vector \(x_i^{(t)}\) to implement the same information, so it can also be written as

\[
j_i^{(t)}
\sim
\Pi(x_i^{(t)},\Omega_i^{(t)};\phi).
\]

### How the three collections change with the process

For student \(i\), there are three item roles in the entire episode.

- \(\Gamma_i\): meta question, the entire inner process does not allow selection.
- \(\Omega_i^{(t)}\): Training candidate questions that can still be selected at step \(t\).
- \(S_i^{(t)}=\{j_i^{(1)},\ldots,j_i^{(t)}\}\): The topic has been selected as of step \(t\).

they satisfy

\[
S_i^{(t)}\subseteq\Omega_i^{(1)},\qquad
S_i^{(t)}\cap\Omega_i^{(t+1)}=\varnothing,\qquad
\Gamma_i\cap\Omega_i^{(1)}=\varnothing.
\]

### The two-tier dependency is now complete

Formula (5) uses \(\phi\) to generate the question number; the question number enters formula (4) to determine \(\theta_i^*\); \(\theta_i^*\) enters
Equation (3) produces meta loss. written as a combination of functions

\[
\phi
\xrightarrow{\Pi}
j_i^{(1:n)}
\xrightarrow{\text{inner argmin}}
\theta_i^*
\xrightarrow{\text{meta prediction}}
\mathcal L_i.
\]

!!! warning "Easily misunderstood"
    In the training data, \(Y_{i,j}\) already exists; the question selector selects "reveal which existing historical answer to the inner layer".
    When deployed, \(Y_{i,j_i^{(t)}}\) will not be obtained until the student actually answers. The computing interfaces for training and deployment are the same,
    But the answers come from different sources.

## Original paper formula (6): How to calculate the inner layer

### Change from ideal optimal solution to K-step update

The algorithm does not exactly optimize equation (4) to convergence for each student. It initializes the adaptable local parameters as
global value, and then take \(K\) steps of gradient descent. An update is written as

\[
\theta_i
\leftarrow
\theta_i
-\alpha
\left.
\nabla_{\theta}
\sum_{\tau=1}^{t}
\ell\!\left(
Y_{i,j_i^{(\tau)}},
g(j_i^{(\tau)};\theta)
\right)
\right|_{\theta=\theta_i}.
\tag{6}
\]

In order to be consistent with the sequential process of the algorithm in the paper, the upper limit is written here as the currently observed \(t\). Paper text presentation (6)
\(n\) is used to indicate the total number of topic selections that have been used for adaptation; Line 7 of Algorithm 1 explicitly uses
\(\{Y_{i,j_i^{(1:t)}}\}\). The two writing methods respectively correspond to the adaptation and gradual training implementation after the entire short test.

### The right side of the vertical line indicates where to calculate the gradient

\[
\left.\nabla_\theta f(\theta)\right|_{\theta=\theta_i}
\]

Read as: First treat \(f\) as a function of the temporary variable \(\theta\) and find the gradient, and then
Take the value at \(\theta_i\). It does not represent conditional probability.

### Initialization and steps

At the beginning of each student's adjustment,

\[
\theta_i^{(0)}=\mu,
\]

Among them, \(\mu\) belongs to the global parameter \(\gamma\). Take \(K\) steps continuously:

\[
\theta_i^{(k+1)}
=U\!\left(\theta_i^{(k)};S_i^{(t)},\alpha\right),
\qquad k=0,\ldots,K-1,
\]

Among them, \(U\) is just the function name we give a GD update. eventually

\[
\theta_i^{(K)}
=U_K(\mu;S_i^{(t)},\alpha).
\]

In actual implementation, this \(\theta_i^{(K)}\) plays the role of the ideal symbol \(\theta_i^*\).

### Why taking fewer steps is like regularization

If there is only one correct answer to the question, optimizing the 1PL capability without any constraints will continuously push \(\theta_i\) to positive infinity, making the question
The probability of correct answer approaches 1. A small number of GD stepping parameters still stay around global initialization. The fewer steps \(K\), the learning rate
The smaller \(\alpha\) is, the harder it is for local parameters to stay away from the global value. So early stopping produces something like shrinkage
effect.

Early stopping and explicit quadratic regularization have different mathematical forms in general nonlinear models. Paper citations
The implicit gradient meta-learning perspective of Rajeswaran et al. considers few-step adaptation as a practical choice for computation and regularization.
[Rajeswaran et al. (2019)](references.md#rajeswaran2019meta).

### Should we adapt again after each new question or continue to adapt?

Mathematically there are two implementations.

1. At each step \(t\), start from the same global initialization \(\mu\) and proceed \(K\) for the first \(t\) observations.
    step. In this way, each adaptation mapping is clear and consistent with MAML task adaptation.
1. Keep the local parameters of the previous step and update incrementally with new questions. This is cheaper to test, but requires computational graphs and implicit regularization
    Different.

The paper description emphasizes taking \(K\) steps from \(\gamma\), and the official training code maintains adaptable meta parameters for each batch.
Then update the training loss of the selected mask. When reproducing, you should refer to the specific code path and make it clear whether to reset.

### Two-step demonstration of one-dimensional IRT

Take \(\mu=0\), question difficulty \(b=0\), student’s correct answer \(y=1\), learning rate \(\alpha=0.4\).
The first step has been calculated:

\[
\theta^{(1)}=0.2.
\]

The second step is to calculate the new probability

\[
p^{(1)}=\sigma(0.2)\approx0.5498,
\]

The gradient is \(p^{(1)}-1=-0.4502\), so

\[
\theta^{(2)}
=0.2-0.4(-0.4502)
\approx0.3801.
\]

Each step recalculates the probability and gradient at the current parameters, and the gradient of the first step cannot be reused twice.

## How to update the global response model

### The outer layer hopes that initialization is suitable for fast individualized

For a mini-batch student set \(\mathcal B\), the outer response model is updated as

\[
\gamma
\leftarrow
\gamma
-\frac{\eta_1}{|\mathcal B|}
\sum_{i\in\mathcal B}
\nabla_\gamma
\mathcal L\!\left(
\theta_i^{(K)}(\gamma,\phi),\Gamma_i
\right).
\]

\(\mathcal B\) is the current small batch of students, \(|\mathcal B|\) is the number of students in the batch,
\(\eta_1\) is the outer response model learning rate.

This update allows "Adapted local parameters starting from \(\gamma\)" to achieve a lower loss on the meta question; select the training question
This goal is indirectly affected through inner layer adaptation.

### Exact meta-gradient across K steps

Let’s just look at the adaptation initialization \(\mu\). The inner Hessian at step \(k\) is recorded as

\[
H_i^{(k)}
=\nabla_\theta^2
\mathcal L_i^{\mathrm{inner}}(\theta_i^{(k)}).
\]

The Jacobian recursion for initialization is

\[
\frac{\partial\theta_i^{(k+1)}}{\partial\mu}
=
\left(I-\alpha H_i^{(k)}\right)
\frac{\partial\theta_i^{(k)}}{\partial\mu}.
\]

The initial Jacobian is \(I\), so

\[
\frac{\partial\theta_i^{(K)}}{\partial\mu}
=
\prod_{k=0}^{K-1}
\left(I-\alpha H_i^{(k)}\right),
\]

The order of products is understood from back to front in the calculation diagram. meta-gradient is

\[
\nabla_\mu\mathcal L_i^{\mathrm{meta}}
=
\left(
\frac{\partial\theta_i^{(K)}}{\partial\mu}
\right)^{\mathsf{T}}
\nabla_{\theta_i^{(K)}}\mathcal L_i^{\mathrm{meta}}.
\]

### First order approximation

If each \(I-\alpha H_i^{(k)}\) is approximated as \(I\), we get

\[
\nabla_\mu\mathcal L_i^{\mathrm{meta}}
\approx
\nabla_{\theta_i^{(K)}}\mathcal L_i^{\mathrm{meta}}.
\]

Intuitively, it updates the global initialization in the direction in which the parameters should move after adaptation, but ignores the impact of initialization changes on inner layers.
Second-order effects of gradient paths.

### Direct and indirect gradients of shared item parameters

If \(\gamma\) also contains shared parameters \(\psi\), such as item difficulty and neural network weight, meta prediction
\(g(j;\theta_i,\psi)\) directly depends on \(\psi\). Inner layer adaptation gradients may also depend on \(\psi\). Therefore

\[
\frac{\mathrm d\mathcal L_i}{\mathrm d\psi}
=
\underbrace{\frac{\partial\mathcal L_i}{\partial\psi}}_{\text{Directly change meta predictions}}
+
\underbrace{
\frac{\partial\mathcal L_i}{\partial\theta_i^{(K)}}
\frac{\partial\theta_i^{(K)}}{\partial\psi}
}_{\text{Change the inner layer to adapt to the result}}.
\]

The actual implementation's choice of which parameters are allowed to be updated in the inner layer and which are only updated in the outer layer is part of the model design.

## Original paper formula (7): Why is the gradient of the topic selector difficult?

### Treat the entire question sequence as a random variable

abbreviation

\[
j_i^{(1:n)}
=\left(j_i^{(1)},\ldots,j_i^{(n)}\right),
\]

Represents the entire topic sequence of student \(i\). Since each step samples from the policy, this sequence is a discrete random variable.
Given it, the inner layer adaptation result can be written as

\[
\theta_i^*(\gamma,j_i^{(1:n)}).
\]

For a student, the target gradient of the policy parameters is

\[
\nabla_\phi
\mathcal L\!\left(\theta_i^*(\gamma,\phi),\Gamma_i\right)
=
\nabla_\phi
\mathbb{E}_{j_i^{(1:n)}\sim\Pi(\cdot;\phi)}
\left[
\mathcal L\!\left(
\theta_i^*(\gamma,j_i^{(1:n)}),\Gamma_i
\right)
\right].
\tag{7}
\]

### Why can’t we find the ordinary derivative of the question number?

If the strategy outputs the probability vector \((0.2,0.5,0.3)\), the sampling result may be question number 2. Slightly change the weight of a certain network,
The probability will continuously change to \((0.21,0.49,0.30)\), but the discrete question number drawn will not continuously change in the manner of "2.01".
The question number has no local derivative in the ordinary sense with respect to the parameters.

Therefore the chain

\[
\phi\to\text{Probability}\to\text{Discrete question number}\to\theta_i^*\to\mathcal L_i
\]

Disconnect at "Probability to Discrete Question Number". The follow-up work of equation (7) is to construct a gradient estimate for this breakpoint.

### Overview of both routes

**Table: Gradient of two question selectors of BOBCAT**

|comparison item|Unbiased estimate, equation (8)|Approximate estimation, equation (9) to equation (11)|
| --- | --- | --- |
|core tools| score-function / REINFORCE |Continuous weight relaxation, implicit differentiation, influence function, straight-through|
|Which candidates to use|The signal is mainly provided by the actual selected trajectory.|Allows all currently available training questions to provide gradient signals|
|Statistical properties|The expectation is equal to the target gradient, but the variance can be very large|Biased, not guaranteed to be equal to the exact gradient, and the empirical variance is low|
|Official implementation|actor-critic and PPO|hard sample forward, softmax gradient reverse|

!!! warning "Easily misunderstood"
    "Unbiased" only means that under correct sampling and expectation, the average of the gradient estimates is equal to the target gradient. It does not account for single estimates
    Being close to the true gradient does not mean that training must be faster. High-variance unbiased estimators may be more biased than stable under limited training budgets.
    Expected to perform even worse.

## Original paper formula (8): unbiased policy gradient

### Let’s start with the expectation of limited actions

Just choose one question for now. Let the probability of \(j\) being selected be \(\Pi_\phi(j)\), and the meta loss after selection is
\(L(j)\). The expected loss is

\[
\mathbb{E}[L]
=\sum_j \Pi_\phi(j)L(j).
\]

Assuming that \(L(j)\) does not directly contain \(\phi\) after a given discrete action, take the derivative:

\[
\nabla_\phi\mathbb{E}[L]
=\sum_j \nabla_\phi\Pi_\phi(j)L(j).
\]

take advantage of

\[
\nabla_\phi\Pi_\phi(j)
=\Pi_\phi(j)\nabla_\phi\log\Pi_\phi(j),
\]

get

\[
\nabla_\phi\mathbb{E}[L]
=
\sum_j\Pi_\phi(j)L(j)\nabla_\phi\log\Pi_\phi(j)
=
\mathbb{E}\!\left[L(j)\nabla_\phi\log\Pi_\phi(j)\right].
\]

### Why is the probability of multi-step trajectories a continuous multiplication?

The action probability condition of step \(t\) is based on the current state. The strategy probability of the entire trajectory is

\[
p_\phi(j_i^{(1:n)})
=
\prod_{t=1}^{n}
\Pi\!\left(
j_i^{(t)}\mid x_i^{(t)};\phi
\right).
\]

Take the logarithm and sum the multiplied changes:

\[
\log p_\phi(j_i^{(1:n)})
=
\sum_{t=1}^{n}
\log
\Pi\!\left(
j_i^{(t)}\mid x_i^{(t)};\phi
\right).
\]

Find the gradient again:

\[
\nabla_\phi\log p_\phi(j_i^{(1:n)})
=
\sum_{t=1}^{n}
\nabla_\phi
\log\Pi\!\left(
j_i^{(t)}\mid x_i^{(t)};\phi
\right).
\]

### Add baseline

So equation (8) is

\[
\begin{aligned}
&\nabla_\phi
\mathbb{E}_{j_i^{(1:n)}\sim\Pi_\phi}
\left[
\mathcal L(\theta_i^*,\Gamma_i)
\right]
\\
&\quad=
\mathbb{E}\left[
\left(\mathcal L(\theta_i^*,\Gamma_i)-b_i\right)
\nabla_\phi
\log\prod_{t=1}^{n}
\Pi\!\left(j_i^{(t)}\mid x_i^{(t)};\phi\right)
\right]
\\
&\quad=
\mathbb{E}\left[
\left(\mathcal L(\theta_i^*,\Gamma_i)-b_i\right)
\sum_{t=1}^{n}
\nabla_\phi
\log
\Pi\!\left(j_i^{(t)}\mid x_i^{(t)};\phi\right)
\right].
\end{aligned}
\tag{8}
\]

### Why increase the probability when the loss is lower than the baseline?

Assume that the loss of a certain trajectory is less than the baseline, so
\(\mathcal L-b_i<0\). Training minimizes the loss, and the parameters are updated as

\[
\phi\leftarrow\phi-\eta_2\widehat{\nabla_\phi\mathcal J}.
\]

The estimated gradient contains a negative coefficient times \(\nabla_\phi\log\Pi\). Subtracting this gradient equals along
\(+\nabla_\phi\log\Pi\) moves, thus increasing the log probability of actions in this trajectory. If the loss is higher than the baseline,
In the opposite direction.

### Why is the variance large?

A sampling only tells the algorithm "what is the result of this sampled trajectory". There are no drawn questions for this REINFORCE gradient
No direct contribution. What's more troublesome is that the end-point meta loss is attributed to \(n\) actions at the same time, making it difficult to tell which step
Really useful. When the action space \(Q\) is large and the trajectory length \(n\) increases, the number of possible trajectories expands rapidly.

### What does critic estimate?

Actor is a policy network that outputs action probabilities. critic reads the state and predicts what is likely to result from continuing the selection from that state
loss or reward. This prediction can be used as a \(b_i\) or finer state-dependent baseline. The advantage can be written as

\[
A_t=R-V(x_i^{(t)}),
\]

where \(V\) is the value estimated by critic. The official code of the paper copies the same end result to multiple action moments.
Then use the critic value to form advantage, and use PPO to truncate the update.

## Original paper equation (9) to equation (11): approximate gradient

### The first step is the ordinary chain rule

The impact of meta loss on \(\phi\) is passed through local parameters:

\[
\nabla_\phi
\mathcal L(\theta_i^*(\gamma,\phi),\Gamma_i)
=
\nabla_{\theta_i^*}
\mathcal L(\theta_i^*,\Gamma_i)
\,
\nabla_\phi\theta_i^*(\gamma,\phi).
\tag{9}
\]

The first factor answers "If the local parameters change a little, how will the meta loss change?"; the second factor answers "If the strategy changes a little, how will the local
How do the parameters change?" The difficulty centers on the second factor.

### Write a discrete selection as one-hot weight

In step \(t\), define \(j\in\Omega_i^{(t)}\) for each currently available question

\[
w_j=
\begin{cases}
1,&j=j_i^{(t)},\\
0,&j\neq j_i^{(t)}.
\end{cases}
\]

So in this step, only the selected topics enter the inner loss. Separate the previous \(t-1\) question from the current selection:

\[
\begin{aligned}
\theta_i^*
=\operatorname*{arg\,min}_{\theta_i}\Bigg[
&\sum_{\tau=1}^{t-1}
\ell\!\left(
Y_{i,j_i^{(\tau)}},
g(j_i^{(\tau)};\theta_i)
\right)
+R(\gamma,\theta_i)
\\
&+
\sum_{j\in\Omega_i^{(t)}}
w_j(\phi)\,
\ell\!\left(Y_{i,j},g(j;\theta_i)\right)
\Bigg].
\end{aligned}
\tag{10}
\]

Although the second line sums all candidate questions, one-hot \(w_j\) keeps only one question in the forward value. The value of this way of writing
We can ask: If the weight of a certain question is slightly increased from 0, how will the inner optimal solution and meta loss change?

### Implicitly find the derivative of the local optimal parameter with respect to the item weight

Let the whole in the brackets of equation (10) be written as \(\mathcal L_i'(\theta_i,w)\). optimal point satisfies

\[
\nabla_{\theta_i}\mathcal L_i'(\theta_i^*,w)=0.
\]

Derive \(w_j\):

\[
\nabla_{\theta_i}^2\mathcal L_i'
\frac{\mathrm d\theta_i^*}{\mathrm dw_j}
+
\nabla_{\theta_i}
\ell\!\left(Y_{i,j},g(j;\theta_i^*)\right)
=0.
\]

If the Hessian is invertible,

\[
\frac{\mathrm d\theta_i^*}{\mathrm dw_j}
=-
\left(\nabla_{\theta_i}^2\mathcal L_i'\right)^{-1}
\nabla_{\theta_i}
\ell\!\left(Y_{i,j},g(j;\theta_i)\right)
\Big|_{\theta_i=\theta_i^*}.
\]

### How to multiply three vectors

Let \(\theta_i\) be the \(d\) dimension column vector.

- The meta gradient \(\nabla_{\theta_i}\mathcal L(\theta_i,\Gamma_i)\) can be regarded as the \(d\) dimensional column vector;
- Hessian is the \(d\times d\) matrix;
- The candidate question gradient \(\nabla_{\theta_i}\ell_{i,j}\) is the \(d\) dimensional column vector.

To get the scalar impact score, one should write

\[
-\nabla_{\theta_i}\mathcal L(\theta_i,\Gamma_i)^{\mathsf{T}}
\left(\nabla_{\theta_i}^2\mathcal L_i'\right)^{-1}
\nabla_{\theta_i}\ell_{i,j}.
\]

The paper omits the transpose symbol and understands it in row gradient notation.

### Influence function score

Substituting the derivative of the local optimal parameter with respect to the item weight into the chain rule, we get

\[
\mathcal I_i(j)
:=
-
\nabla_{\theta_i}\mathcal L(\theta_i,\Gamma_i)^{\mathsf{T}}
\left(\nabla_{\theta_i}^2\mathcal L_i'\right)^{-1}
\nabla_{\theta_i}
\ell\!\left(Y_{i,j},g(j;\theta_i)\right)
\Big|_{\theta_i=\theta_i^*}.
\tag{11}
\]

The new symbol \(\mathcal I_i(j)\) is the influence score of question \(j\) on student \(i\). It approximately represents the problem
How will the meta loss change if \(j\) slightly increases the weight in the inner layer:

\[
\mathcal I_i(j)
\approx
\frac{\partial
\mathcal L(\theta_i^*,\Gamma_i)}
{\partial w_j}.
\]

If \(\mathcal I_i(j)<0\), slightly increasing the inner weight of this question will reduce the meta loss, which is usually a good sign.
If positive, it will increase the meta loss.

### Why is "gradient similarity" separated by the inverse Hessian?

If curvature is ignored, the inner product of two gradients is negative or positive to indicate whether the directions are consistent. But the scale sum in different directions of the parameter space
The curvature is different. The inverse Hessian preconditions the gradient of the candidate question and approximates "where the gradient will actually push the optimal parameters."
Therefore, the influence function contains two parts of information: gradient alignment and local curvature.

It is most intuitive in one dimension:

\[
\mathcal I_i(j)
=-
\frac{
g_{\mathrm{meta}}\,
g_{j}
}{H},
\]

Among them, \(g_{\mathrm{meta}}\) is the derivative of meta loss to ability, \(g_j\) is the candidate question loss gradient,
\(H>0\) is the curvature of the inner layer. If the two gradients have the same sign, increasing the weight of question \(j\) will move the parameters in the direction of the negative gradient, thus
Reduce meta loss, so impact score is negative.

### Approximation from one-hot to probability

\(w_j\) is still a discrete one-hot. For papers

\[
w_j(\phi)
\approx
\Pi(j\mid x_i^{(t)};\phi)
\]

replace it. So the approximate policy gradient is

\[
\nabla_\phi\mathcal L_i
\approx
\sum_{j\in\Omega_i^{(t)}}
\mathcal I_i(j)
\nabla_\phi
\Pi(j\mid x_i^{(t)};\phi).
\]

Now all available questions can contribute gradients, not just the drawn questions.

### straight-through How to make forward hard and reverse soft

The official code first calculates the softmax probability \(y_{\mathrm{soft}}\), and then takes the maximum term to generate one-hot
\(y_{\mathrm{hard}}\), then construct

\[
y
=y_{\mathrm{hard}}
-\operatorname{stopgrad}(y_{\mathrm{soft}})
+y_{\mathrm{soft}}.
\]

During forward calculation, the last two values cancel out, so \(y=y_{\mathrm{hard}}\). When derivation in reverse,
The derivative of \(\operatorname{stopgrad}\) is 0, and the last term retains the softmax derivative, so

\[
\frac{\partial y}{\partial\phi}
\approx
\frac{\partial y_{\mathrm{soft}}}{\partial\phi}.
\]

This is a typical implementation of straight-through estimator
[Bengio et al. (2013)](references.md#bengio2013estimating)。

### Why is it biased?

The true forward function is almost invariant to the parameters outside the argmax boundary, and the true local derivative is usually 0; the reverse function is deliberately
Use non-zero derivatives of softmax. The estimate is therefore not equal to the derivative of the real discrete operator. What it optimizes is a human-designed
Surrogate gradient. Empirically, low variance and dense signals across all candidates may offset the problems caused by bias.

!!! warning "Easily misunderstood"
    Equation (11) strictly uses the inner optimal point and the influence function of the reversible Hessian to derive, and the code uses finite-step inner layer adaptation.
    and straight-through automatic differentiation. The two are ideologically connected, but the code gradient cannot be called the exact formula (11)
    Numerical implementation. When reproducing a paper, "theoretical approximation" and "engineering approximation" should be recorded separately.

## Complete calculation sequence of Algorithm 1

### First list the three learning rates

The algorithm initializes three learning rates.

- \(\alpha\): The inner learning rate of the student’s local parameters, which appears in equation (6).
- \(\eta_1\): The outer learning rate of the global response model parameter \(\gamma\).
- \(\eta_2\): The outer learning rate of the question selector parameter \(\phi\).

The three control different variables, and the values do not have to be the same. In the search range given by the official warehouse, the inner learning rate is approximately
In \(0.05,0.1,0.2\), meta response learning rate is \(10^{-4}\), policy learning
rate is near \(2\times10^{-4}\) or \(2\times10^{-3}\). These values are the search range implemented by the paper,
It is necessary to readjust the parameters when changing the data set.

### An outer iteration

Next, an outer training iteration is broken down into executable actions. Let mini-batch be \(\mathcal B\).

#### Step 1: Create two question sets for each student

For each \(i\in\mathcal B\), divide it from the student's observed questions

\[
\Omega_i^{(1)}\quad\text{and}\quad\Gamma_i,
\]

The former is the training candidate set, and the latter is the meta set. The two do not intersect.

#### Step 2: Clear short test status

Order

\[
x_i^{(1)}=\bm 0,\qquad S_i^{(0)}=\varnothing.
\]

Local adaptation parameters are initialized as global adaptation blocks:

\[
\theta_i^{(0)}=\mu.
\]

#### Step 3: Enter the tth topic selection moment

For \(t=1,\ldots,n\), for each student do:

1. Input the current status \(x_i^{(t)}\) into the question selector;
1. For the mask of unavailable questions, obtain the probability of available questions;
1. Sampling or hard selection \(j_i^{(t)}\);
1. Read \(Y_{i,j_i^{(t)}}\) from the history matrix;
1. Update the selected set, candidate set and state vector;
1. Use the current selection to answer, and walk the inner GD of \(K\) for \(\theta_i\);
1. Use \(\theta_i^{(K)}\) to calculate the meta loss on \(\Gamma_i\).

#### Step 4: Update the topic selector

Choose one of the following gradients:

\[
\widehat g_{\phi,i}^{\mathrm{unbiased}}
=
\left(\mathcal L_i-b_i\right)
\sum_{\tau=1}^{t}
\nabla_\phi\log
\Pi(j_i^{(\tau)}\mid x_i^{(\tau)};\phi),
\]

or

\[
\widehat g_{\phi,i}^{\mathrm{approx}}
\approx
\sum_{j\in\Omega_i^{(t)}}
\mathcal I_i(j)\nabla_\phi
\Pi(j\mid x_i^{(t)};\phi).
\]

Then average the batches:

\[
\phi
\leftarrow
\phi-\frac{\eta_2}{|\mathcal B|}
\sum_{i\in\mathcal B}\widehat g_{\phi,i}.
\]

Paper Algorithm 1 puts the \(\phi\) update inside each topic selection step. This allows the policy to gradually learn what to choose at each stage.
If the implementation is to be updated uniformly after the complete \(n\) step, the calculation graph or trajectory of each step must also be correctly saved.

#### Step 5: Update global response model

After completing \(n\) question selection steps, calculate

\[
\gamma
\leftarrow
\gamma
-\frac{\eta_1}{|\mathcal B|}
\sum_{i\in\mathcal B}
\nabla_\gamma
\mathcal L(\theta_i^{(K)}(\gamma,\phi),\Gamma_i).
\]

Then move on to the next batch of students until the validation metrics no longer improve or the training budget is reached.

### Pseudocode

**Code: Conceptual pseudocode consistent with the notation of the paper**

```python
initialize global response parameters gamma
initialize policy parameters phi

while not converged:
    B = sample_student_minibatch()

    for each student i in B:
        Omega[i], Gamma[i] = split_observed_items(i)
        state[i] = zeros(Q)
        selected[i] = empty_set()

    for t in 1,...,n:
        for each student i in B:
            probs = policy(state[i], available=Omega[i], phi=phi)
            item = sample_or_hard_select(probs)
            answer = historical_response[i, item]
            selected[i].add(item)
            Omega[i].remove(item)
            state[i][item] = +1 if answer == 1 else -1

            theta_i = initialize_from(gamma)
            theta_i = K_gradient_steps(
                selected_responses=selected[i],
                learning_rate=alpha
            )
            meta_loss_i = loss(theta_i, Gamma[i])

        policy_gradient = unbiased_or_approximate_gradient()
        phi = phi - eta2 * average(policy_gradient)

    response_meta_gradient = differentiate_meta_loss_through_adaptation()
    gamma = gamma - eta1 * average(response_meta_gradient)
```

### Tensor-level data flow

If the batch size is \(B=|\mathcal B|\), the number of questions is \(Q\), the local parameter dimension is \(d\), the common tensor shape is

\[
\begin{array}{c|c}
\text{object} & \text{shape}\\ \hline
\text{state matrix}X^{(t)} & B\times Q\\
\text{Available questions mask} & B\times Q\\
\text{Strategy logits and probabilities} & B\times Q\\
\text{Each person's action question number} & B\\
\text{local parameter matrix}\Theta & B\times d\\
\text{The logits of the response model for all questions} & B\times Q\\
\text{meta mask} & B\times Q
\end{array}
\]

The official code uses mask to press the training/meta questions owned by different students into a unified \(B\times Q\) matrix, and then uses
Element-wise binary cross-entropy and mask summation.

### Calculation difference between training and deployment

**Table: Inputs and calculations for training and deployment**

|comparison item|training phase|New student deployment phase|
| --- | --- | --- |
|Answer source|Historical response matrix, read after simulating topic selection|Students will receive real-time information after they actually answer the questions|
|Is there a meta answer?|Yes, for outer layer loss|Usually no and no need|
|Whether to update \(\gamma,\phi\)|Yes|usually fixed|
|Do I need to update \(\theta_i\) to choose the next question?|The paper states that after learning \(\Pi\), you can directly select topics from the status|If a final capability report is still required, local parameters can be updated separately.|
|main cost|Double-layer backpropagation, policy learning|One-pass policy network forward propagation|

### Why does the paper say it is faster during testing?

Traditional IRT-Active updates the current ability estimate every time a question is answered, and then calculates information for a large number of candidate questions. BOBCAT
When deploying the topic selection, only input the state vector into the trained \(\Pi\), and the next question can be obtained by one forward propagation. The training cost is
Pay in advance. If the system still has to report IRT capabilities, a local estimation step may still be required, but it will no longer be the topic selector every time
Required input for decision-making.

!!! tip "You should remember this when reading this"
    There are three parameter movements for one training iteration: \(\theta_i\) is adapted for each student by \(\alpha\) in the inner layer;
    \(\phi\) Press \(\eta_2\) to learn how to choose a topic; \(\gamma\) Press \(\eta_1\) to learn how to quickly adapt and predict
    Global response model for meta-questions.
