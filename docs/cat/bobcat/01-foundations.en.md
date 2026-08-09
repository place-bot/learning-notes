# BOBCAT basics: CAT, probability, gradient and learning paradigm

## First use a human word to catch BOBCAT

### It learns a set of reusable topic selection strategies

Imagine a long test with hundreds of questions. For a new student, we do not want him to complete all the questions, only allow him to ask
Very few. After asking the question, the system should still be able to predict whether he will probably answer the remaining questions correctly or incorrectly. Traditional CAT
Usually, a question selection principle is stipulated first, such as selecting the question with the current probability of correct answer closest to \(50\%\). BOBCAT asked:

> Is it possible to directly learn a question selector from the complete or relatively intensive answer records of many students in the past so that it can select a small number of questions?
> Best for predicting unasked questions?

A core word appears here for the first time: **topic selector**. Thesis is written as
\(\Pi\). This article uses the capital Greek letters \(\Pi\) to represent an algorithm. It receives a certain student into the current
The response state so far, output the next question that should be selected, or output the probability of each candidate question being selected.

### Why are there two learning tasks?

To determine whether a question selector is good, BOBCAT performs a simulation of known responses from history students. Start with what each student has answered
Take a portion of the questions and allow the question selector to pick a small number of questions; these are the **training candidate questions**. Then hide the other part
Get up; these are **meta questions**. After the question selector selects a question, the system only uses the selected question to adapt to the student, and then
Predict hidden meta questions.

So there are two nested tasks.

1. Given a small number of questions that have been selected, how to get the local parameters of this student? This is an inner task.
1. What kind of question selector can make the inner-layer adapted parameters perform best on meta questions? This is an outer mission.

The second task cannot be evaluated directly, bypassing the first task, because the value of the same question depends on how it changes the student parameters,
The change of student parameters determines the prediction of meta questions. This is bilevel, that is, double-layer optimization, the simplest source.

### BOBCAT’S CAUSAL CHAIN

```text
The question selector gives the next question
        ↓
Read the student's history answer
        ↓
Inner layer adapts to student parameters
        ↓
Calculate loss on meta question
        ↓
Reversely update the global model and topic selector
        └──────────────→ Next round of topic selection
```

"Read the history and answer" in the picture is very important. BOBCAT training uses an existing response data set and queries the offline data
Students' recorded answers to selected items simulate the process of administering the item, waiting, and receiving answers.

!!! tip "You should remember this when reading this"
    BOBCAT learns a strategy from "current response state" to "next question". It uses a small number of selected questions to complete student-specific
    Adapt, and then use the meta questions that have not participated in the adaptation to evaluate the quality of the topic selection. Inner layer adaptation is the precursor step of outer layer evaluation, so it forms
    Two-tier optimization.

## Where does CAT come from?

### The difference between fixed tests and adaptive tests

Fixed quizzes give everyone the same questions. CAT stands for computerized adaptive testing, that is, computerized adaptive testing
Quiz. After each question is answered, it selects the next question based on the responses it has observed. The criterion for "adaptive" is the follow-up
The item changes with the previous answers; the system randomly assigns different test papers in advance and only provides the differences between the test papers.

First consider only one student, and use \(i\) to represent this student's number. Here \(i\) comes from index, the value can be
\(1,2,\ldots,N\). The letters \(N\) represent the total number of students in the historical data. Then use \(j\) to represent the item number,
\(j=1,2,\ldots,Q\), where \(Q\) is the total number of items in the item bank.

Student \(i\)’s binary answer to item \(j\) is recorded as

\[
Y_{i,j}\in\{0,1\}.
\]

The first position of the subscript is the person, and the second position is the question. \(Y_{i,j}=1\) means the answer is correct.
\(Y_{i,j}=0\) indicates an incorrect answer.

!!! example "Small example: why you need both \(i\) and \(j\)"
    If \(Y_{3,8}=1\), it only means that the 3rd student answered question 8 correctly. It does not mean that the third student must have high ability.
    It doesn’t mean that Question 8 is necessarily easy. Only by combining the answers to many people and many questions can we distinguish between people's abilities and questions.
    difficulty.

### The response model is the prediction engine of CAT

CAT requires a model to turn student characteristics and item characteristics into correct answer probabilities. This model is called
**Responsive Model**. BOBCAT represents it with the letters \(g\). Let’s not specify whether \(g\) is an IRT or a neural network.
only written as

\[
g(j;\theta_i).
\]

\(j\) on the left side of the semicolon is the item number to be predicted. \(\theta_i\) on the right side of the semicolon is part of student \(i\)
parameters. The output is a number between \(0\) and \(1\), which is interpreted as the predicted probability that the student correctly answers the question \(j\):

\[
g(j;\theta_i)\approx
\Pr(Y_{i,j}=1\mid \text{Information currently held by the model}).
\]

The letters \(\theta\) are pronounced theta. It can be a number in one-dimensional IRT, representing ability; in multi-dimensional IRT
Can be a vector; in a neural network response model, it can also be a student embedding. BOBCAT’s “model-agnostic”
Mainly means that the framework does not force \(\theta_i\) to adopt a specific form.

### The full meaning of traditional 1PL IRT

The paper starts with the simplest 1PL IRT. item \(j\) has a difficulty \(b_j\), student \(i\) has an ability
\(\theta_i\). The probability of correct answer is

\[
p_{i,j}
=\Pr(Y_{i,j}=1\mid\theta_i,b_j)
=\sigma(\theta_i-b_j),
\]

Among them, \(p_{i,j}\) is a newly defined probability to shorten writing, and \(\sigma\) is a sigmoid function:

\[
\sigma(z)=\frac{1}{1+\exp(-z)}.
\]

Here \(z\) is treated as any real number. If \(z=0\), then \(\sigma(0)=1/2\). put back
1PL answer probability formula, when the student's ability is equal to item difficulty, that is, \(\theta_i=b_j\), the probability of correct answer is
\(50\%\). If the ability is higher than the difficulty, \(\theta_i-b_j>0\), the probability of correct answer is greater than \(50\%\); otherwise it is less than
\(50\%\)。

!!! example "Small example: three correct answer probabilities that can be calculated by hand"
    Fixed student ability \(\theta_i=0.5\).

    \[
    \begin{array}{c|c|c}
    \text{item difficulty} & \theta_i-b_j & \Pr(Y_{i,j}=1)\\ \hline
    b_j=-0.5 & 1.0 & \sigma(1)\approx0.731\\
    b_j=0.5 & 0 & 0.500\\
    b_j=1.5 & -1.0 & \sigma(-1)\approx0.269
    \end{array}
    \]

    The same student has different probabilities of correct answers to different questions, so the response model must know both the student and the question.

### Why does traditional CAT prefer questions with a probability of getting correct answers close to half?

In the 1PL model, the Fisher information of item \(j\) on capability \(\theta_i\) is

\[
\mathcal{I}_j(\theta_i)=p_{i,j}(1-p_{i,j}).
\]

The new \(\mathcal{I}\) here represents information; the influence function after BOBCAT is recorded as
\(I_i(j)\). Function \(p(1-p)\) reaches the maximum value \(0.25\) at \(p=0.5\). So, when the goal is to
When reducing the uncertainty of the ability estimate, it is reasonable to choose the question with the current predicted correct answer probability closest to \(0.5\).

If at the \(t\)th topic selection moment, the set of questions that student \(i\) can still choose is recorded as
\(\Omega_i^{(t)}\), the traditional rule can be written as

\[
j_i^{(t)}
=\operatorname*{arg\,max}_{j\in\Omega_i^{(t)}}
\mathcal{I}_j\!\left(\widehat{\theta}_i^{(t-1)}\right).
\]

Now read this expression one by one.

- The superscript \((t)\) indicates step \(t\); it is the step index.
- \(j_i^{(t)}\) is the question number selected for student \(i\) in step \(t\).
- \(\widehat{\theta}_i^{(t-1)}\) is the ability estimate obtained after reading the previous questions \(t-1\). hat
    represents an estimate.
- \(\operatorname*{arg\,max}\) returns the question number that maximizes the following expression; the maximum information value is the corresponding
    objective value。
- After selecting a question, it is usually removed from \(\Omega_i^{(t)}\).

### What does BOBCAT do to rewrite traditional goals?

Traditional CAT often regards "more accurate ability estimate" as the selection criterion. BOBCAT believes that ability is only an intermediate representation. truly care
The task can be written more directly: Can you predict more of a student's responses on a very long test by looking at just a few questions?
So it trains the question selector using the prediction loss on held-out meta questions.

!!! warning "Easily misunderstood"
    ability estimate still has value. If the response model is IRT, the inner layer continues to estimate student ability. changes occurred in
    **Training guidelines for item selectors**: The value of an item is ultimately determined by the improvement in held-out answer predictions it brings, Fisher
    Information can be used as one of the references.

## Probability, likelihood and cross-entropy

### Why does a probability prediction turn into a loss?

The response model outputs the correct answer probability \(p\), and the real answer is \(y\in\{0,1\}\). Training requires a number to measure predictions
How bad. BOBCAT uses binary cross-entropy

\[
\ell(y,p)=-y\log p-(1-y)\log(1-p).
\]

The letters \(\ell\) are pronounced as lowercase ell and represent the loss of a single observation. It receives two inputs: the real answer \(y\) and
Predicted probability \(p\).

When \(y=1\), the second item disappears and the loss is \(-\log p\). The closer the predicted correct answer probability is to 1, the smaller the loss.
When \(y=0\), the first item disappears and the loss is \(-\log(1-p)\). The closer the predicted correct answer probability is to 0, the smaller the loss.

!!! example "Small example: the same answer is correct, but the penalties of the two models are different"
    The real answer is \(y=1\). Model A gives \(p=0.9\), and the loss is
    \(-\log(0.9)\approx0.105\). Model B gives \(p=0.1\), and the loss is
    \(-\log(0.1)\approx2.303\). Cross-entropy heavily penalizes confident but incorrect predictions.

### cross-entropy is negative log likelihood

The binary answer can be viewed as a Bernoulli random variable. Given the probability \(p\), the probability mass of observing the answer \(y\) is

\[
\Pr(Y=y)=p^y(1-p)^{1-y}.
\]

Take the logarithm and add the negative sign:

\[
-\log\Pr(Y=y)
=-y\log p-(1-y)\log(1-p),
\]

Just get the binary cross-entropy formula. Therefore, minimizing cross-entropy is equivalent to maximizing the likelihood of the observed answer. Papers sometimes say
"maximize likelihood", but the formula says "minimize cross-entropy", there is no contradiction between the two statements.

### Why should the losses of multiple questions be added up?

If we temporarily assume that given the student parameters, the answer conditions for each question are independent, then the joint likelihood of multiple questions is the likelihood of each question.
product. After taking the logarithm, the product becomes a sum. Therefore, the total loss for the problem set \(S\) can be written as

\[
\mathcal{L}(\theta_i,S)
=\sum_{j\in S}
\ell\!\left(Y_{i,j},g(j;\theta_i)\right).
\]

This is the first time that the capital letters \(\mathcal{L}\) are used. Lowercase \(\ell\) is the loss of a question, uppercase
\(\mathcal{L}\) is the loss of a question set. This summation is used for the outer loss of BOBCAT later.

Sometimes implementations will divide by the number of questions \(|S|\) to get the average loss. This changes the scale of the gradient, but does not change the fixed \(S\)
The location of the optimal solution. Thesis formula (3) divides the number of students by \(N\), and uses summation for each student's meta questions.

### A key simplification of cross-entropy gradient under 1PL

Order

\[
p=\sigma(\theta-b),
\qquad
\ell(\theta)=-y\log p-(1-y)\log(1-p).
\]

Derivating the ability \(\theta\), the result is very simple:

\[
\frac{\partial\ell}{\partial\theta}=p-y.
\]

If the student answers correctly, that is \(y=1\), and the current answer is \(p<1\), then \(p-y<0\). gradient descent will subtract from the current ability
A negative number, so the ability increases. If the student answers incorrectly, i.e. \(y=0\), then the gradient is \(p>0\) and the ability decreases.

The second derivative is

\[
\frac{\partial^2\ell}{\partial\theta^2}=p(1-p)\geq0.
\]

When it is one-dimensional, the second-order derivative describes the curvature; when it is multi-dimensional, the corresponding object is called the Hessian matrix. Later in the influence function

\[
(\nabla_{\theta_i}^2\mathcal{L}'_i)^{-1}
\]

Just comes from this curvature.

!!! tip "You should remember this when reading this"
    The cross-entropy of a single question is represented by \(\ell\), and the total loss of the question set is represented by \(\mathcal{L}\). In the 1PL model, the loss is
    The gradient of ability is "predicted probability minus true answer", which is \(p-y\). This result will appear repeatedly in inner updates and hand calculations.
    Example.

## What exactly does gradient descent do?

### Optimization variables and ordinary input must be separated

Consider a function \(f(\theta)\). \(\theta\) is a parameter we can change, \(f\) is obtained after changing the parameters
losses. Optimization tasks

\[
\min_{\theta} f(\theta)
\]

Read as: Find the value that minimizes \(f\) among the allowed \(\theta\).

The gradient is written \(\nabla_\theta f(\theta)\). The subscript \(\theta\) clearly states "to whom the derivative is sought." If
\(\theta\) is a number, and the gradient is the ordinary derivative; if \(\theta\) is a vector, the gradient is the bias of each component
A vector composed of derivatives.

### One step gradient descent

The update of gradient descent is

\[
\theta^{\mathrm{new}}
=\theta^{\mathrm{old}}
-\alpha\nabla_\theta f(\theta^{\mathrm{old}}).
\]

The new symbol \(\alpha>0\) is the learning rate. The gradient points in the direction of the fastest local rise of the function, so the preceding negative sign makes the update
Head towards the descent. The learning rate determines how far you go.

!!! example "Small example: update ability with a correct answer"
    Current capability \(\theta=0\), item difficulty \(b=0\), so \(p=\sigma(0)=0.5\). The student answered correctly,
    \(y=1\). According to the IRT gradient formula, the gradient is \(p-y=-0.5\). Take the learning rate
    \(\alpha=0.4\), updated in one step

    \[
    \theta^{\mathrm{new}}
    =0-0.4(-0.5)=0.2.
    \]

    The same student's ability estimate rises from 0 to 0.2.

### K-step gradient descent to obtain a truncated approximate solution

Starting from the initial value \(\theta^{(0)}\), repeat the gradient descent formula:

\[
\theta^{(k+1)}
=\theta^{(k)}-\alpha\nabla_\theta f(\theta^{(k)}),
\qquad k=0,\ldots,K-1.
\]

Here \(k\) is the optimization step number, and \(K\) is the total number of steps. The obtained \(\theta^{(K)}\) is generally only an approximate solution.
Unless there are strong conditions and the iteration is long enough, it cannot be equated to the real
\(\operatorname*{arg\,min}_\theta f(\theta)\)。

The BOBCAT paper first uses \(\theta_i^*=\operatorname*{arg\,min}_{\theta_i}\cdots\) to describe the ideal inner solution. The algorithm implementation only takes
A small number of \(K\) steps. This approach is called truncated optimization, which can also be called truncated inner optimization.

### What does it mean to find the gradient again?

Suppose one step update is

\[
\theta^{(1)}(\gamma)
=\gamma-\alpha\nabla_\theta f(\theta)\big|_{\theta=\gamma},
\]

Here \(\gamma\) is the initial parameter. If the outer layer loss is \(F(\theta^{(1)}(\gamma))\), update
\(\gamma\) requires the chain rule:

\[
\frac{\mathrm dF}{\mathrm d\gamma}
=\frac{\partial F}{\partial\theta^{(1)}}
\frac{\partial\theta^{(1)}}{\partial\gamma}.
\]

The second factor is

\[
\frac{\partial\theta^{(1)}}{\partial\gamma}
=I-\alpha\nabla_\theta^2 f(\gamma).
\]

Where \(I\) is the identity matrix and \(\nabla_\theta^2 f\) is the Hessian. It comes from "rederivating the inner gradient",
So the exact meta-gradient will have second derivatives.

### What automatic differentiation does and doesn’t do

Frameworks such as PyTorch record calculation graphs and calculate derivatives according to the chain rule. Automatic differentiation avoids handwriting long derivatives, but it doesn't
Automatically deciding which variable should be optimized does not fix non-differentiable discrete sampling. The main difficulty with BOBCAT is occurring
"Select question number" is a discrete action, and ordinary backpropagation cannot directly pass through this action. Therefore, the paper proposes an unbiased
The score-function estimate and the biased straight-through approximation are two routes.

## Active learning preparation

### Active learning is taking the initiative

Ordinary supervised learning receives labeled data. Active learning allows the model to actively select the most worthy candidates from a pool of unlabeled candidates.
Request a sample of the label. A typical loop is:

1. Use existing annotations to train the model;
1. Calculate the value of the samples in the candidate pool;
1. Select a sample and request a label from the annotator;
1. Update the model after adding new annotations, and repeat.

In CAT, "candidate sample" corresponds to item, and "request label" corresponds to asking students to answer. The returned answer \(0/1\) is
label. CAT can thus be viewed as a special type of sequential active learning.

### Uncertainty Sampling

The simplest active learning rule in binary classification is called uncertainty sampling. If the model predicts category 1 for a candidate sample
The probability is \(p\), then the closer \(p\) is to \(0.5\), the more uncertain the model is. available

\[
u(p)=\min\{p,1-p\}
\]

as an uncertainty score. It is maximum at \(p=0.5\).

The item information of 1PL IRT \(p(1-p)\) is also the largest in \(0.5\). Therefore, choosing topics based on Fisher information in 1PL is
The same questions will be selected for the two-category uncertainty question selection. The paper calls this traditional baseline IRT-Active.

### The difference between active learning and BOBCAT

The value function for uncertainty sampling is pre-written. BOBCAT's topic selection value is learned from historical data and is determined by meta
Question prediction performance monitoring. The difference between the two can be understood with a counterexample.

!!! example "Small example: the most uncertain question may not be the most conducive to predicting the entire question domain"
    Suppose the item bank contains both algebra and geometry. The probability of a student's correct answer to a popular geometry question is exactly \(0.5\).
    So uncertainty sampling loves it. But most of the meta questions test algebra, and the probability of answering the other question correctly is \(0.65\)
    of algebra questions can strongly differentiate students' algebra levels. If the ultimate goal is to predict meta questions, the second question may be more valuable.
    BOBCAT allows historical data to learn this cross-topic correlation structure.

### Why can offline training know the answers to unselected questions?

In the actual test, questions that have not been asked will of course not have answers. But BOBCAT’s training data comes from past student response records.
For a simulation episode in the training phase, the \(Y_{i,j}\) simulation that already exists in the available data "If you select the question \(j\),
What answers will you see?" The biased approximation may even use historical answers to questions that were not chosen in the current training candidate pool to reduce the gradient.
variance. This permission only exists for offline training, and the question selector during deployment will not see the answers to unanswered questions by new students.

!!! warning "Easily misunderstood"
    This leads to a data coverage problem. If the historical response matrix is very sparse and students have only done a few and highly selective questions,
    You cannot simulate any candidate actions at will. The paper actually divides each student's training/meta from the questions he has answered.
    collection. The strategies learned by the framework are limited by the historical question generation mechanism and observable coverage.

##reinforcement learning preparation

### First use a CAT process to establish five concepts

Reinforcement learning often uses "state, action, strategy, reward, trajectory" to describe sequential decision-making. The entire set of MDP definitions will not be introduced for the time being.
Map them directly to a fixed length CAT.

- **Status**: When reaching step \(t\), which questions did the student answer before, whether they were correct or incorrect.
- **Action**: Which question to choose in step \(t\).
- **Strategy**: An algorithm that gives selection probabilities for optional questions after a given state.
- **Reward**: After selecting the specified number of questions, how well does the local student model perform on the meta questions.
- **Track**: The status, question selection and answer sequence from the first step to the last step.

BOBCAT uses \(\Pi(\cdot;\phi)\) to represent the strategy. \(\phi\) after the semicolon is pronounced as phi, which is the topic selection neural network.
All trainable parameters. Given the state \(x_i^{(t)}\) at step \(t\), the probability of selecting question \(j\) is written as

\[
\Pi\!\left(j\mid x_i^{(t)};\phi\right).
\]

The vertical bar reads "given".

### The relationship between BOBCAT and reinforcement learning

The precise statement is: BOBCAT is a two-layer optimization framework, in which the unbiased gradient version writes the question selector training as
RL-style policy gradient, and uses PPO in the implementation. The entire framework cannot be simply equated to reinforcement learning for three reasons.

1. Student-specific adaptation of the response model is an explicit inner-level optimization.
1. The outer supervision signal comes from the held-out meta response loss.
1. The best-performing Approx version of the paper uses influence functions and straight-through approximation, using surrogate
    gradient update.

### Sign direction of rewards and losses

Reinforcement learning usually maximizes the reward \(R\), and machine learning usually minimizes the loss \(\mathcal{L}\). can make

\[
R=-\mathcal{L}.
\]

Maximizing reward is then equivalent to minimizing loss. The paper formula (8) directly retains the loss, so the sign of the policy gradient update
It should be explained according to "gradient descent minimizing loss".

### From two-armed bandit to sequential topic selection

If there is only one state, you will be rewarded immediately after selecting the action. This is called multi-armed bandit. CAT is not exactly like this.
Single-step problem because the answer to step \(t\) changes the status of step \(t+1\). However, if all rewards are only given at the end point,
It is much like sequential decision-making with limited time domain and end-point feedback.

Traditional MDP also writes state transfer

\[
s_{t+1}\sim P(\cdot\mid s_t,a_t).
\]

In BOBCAT's offline simulation, the current status and the selected question determine which historical answer will be exposed, and then the answer
Write to the next state. The paper assumes that students' true abilities are static during a test, so the sequence itself does not enter state coding.

### Minimal intuition for policy gradients

The question number obtained by discrete sampling cannot be ordinary differentiated with respect to \(\phi\). The policy gradient bypasses the derivative of the question number and instead adjusts the "generated
The probability of this question number". If a certain topic selection trajectory brings lower than average meta loss, increase the cost of the actions in this trajectory.
Probability; if it brings high losses, reduce the probability.

The core identity behind this is

\[
\nabla_\phi \mathbb{E}_{X\sim p_\phi}[f(X)]
=\mathbb{E}_{X\sim p_\phi}\!\left[
f(X)\nabla_\phi\log p_\phi(X)
\right].
\]

Here \(X\) is the discrete object drawn from the distribution \(p_\phi\), and \(f(X)\) is the result obtained after drawing it.
The left side originally requires the derivation of the "expectation with sampling", while the right side only requires the derivation of the log probability. Chapter 16 will start with the summation form
Derive it line by line.

### baseline Why not introduce bias?

A baseline \(b\) that does not depend on the current action can be subtracted from \(f(X)\):

\[
\mathbb{E}[(f(X)-b)\nabla_\phi\log p_\phi(X)].
\]

because

\[
\mathbb{E}[\nabla_\phi\log p_\phi(X)]
=\sum_x p_\phi(x)\nabla_\phi\log p_\phi(x)
=\sum_x\nabla_\phi p_\phi(x)
=\nabla_\phi 1=0,
\]

Subtracting \(b\) does not change the expectation, it may only reduce the variance. \(b_i\) in BOBCAT formula (8) is student \(i\)
control variables. In the actor-critic implementation, the critic learns to predict the result and serves as a state-dependent baseline.

### What role does PPO play here?

PPO is proximal policy optimization. The direct policy gradient may be too large for one update, making the new policy inconsistent with the collection
The old strategy differs too much when trajectories. PPO uses probability ratio

\[
r_t(\phi)
=\frac{\Pi_\phi(a_t\mid s_t)}
{\Pi_{\phi_{\mathrm{old}}}(a_t\mid s_t)}
\]

Measure the change and clip \(r_t\) near \(1-\epsilon\) and \(1+\epsilon\). BOBCAT official code
The unbiased version includes actor, critic, entropy bonus and clipped surrogate loss. Understand thesis formula (8)
Only the REINFORCE identity is required; PPO is the engineering layer that makes actual updates more stable.

## Meta-Learning Preparation

### General training and "Learn to adapt quickly"

Ordinary supervised learning looks for a set of parameters that allow it to predict well directly on the overall data. Meta-learning is more concerned about: whether it can learn a
Good initialization allows the model to adapt to the task in just a few steps after seeing a small amount of data for a new task.

In BOBCAT, each student can be viewed as a small task. Global response model provides common initialization; a small number of selected
The answer is the student's support data; the meta question is the query data. The inner layer uses support data adaptation, and the outer layer uses
query data evaluation.

### MAML skeleton

Assume that the \(i\)th task has training loss \(L_i^{\mathrm{train}}\) and validation loss
\(L_i^{\mathrm{meta}}\). Starting from the common initialization \(\gamma\), one step adaptation:

\[
\theta_i'=\gamma-\alpha
\nabla_\theta L_i^{\mathrm{train}}(\theta)\big|_{\theta=\gamma}.
\]

Then select \(\gamma\) to make the adapted parameters better on the meta data of each task:

\[
\min_\gamma \sum_i L_i^{\mathrm{meta}}(\theta_i').
\]

This is model-agnostic meta-learning, referred to as MAML, the most basic structure
[Finn et al. (2017)](references.md#finn2017maml)。

BOBCAT adds a key variable on this basis: topic selection strategy
\(\Pi(\cdot;\phi)\) actively selects support data. Therefore, the outer layer simultaneously learns a global picture suitable for rapid adaptation.
The response model \(\gamma\), and the policy parameter \(\phi\) "which observations should be shown to the inner layer".

### Don’t mix the words global, local and meta.

- **global parameter**: Parameters shared by students across history and trained by the outer layer, paper writing \(\gamma\).
- **local parameter**: For student \(i\), parameters obtained from global initialization adaptation, written
    \(\theta_i^*\) or \(\theta_i^{(K)}\) in implementation.
- **meta question**: Questions that are reserved for external evaluation and do not participate in the student's internal adaptation. meta describes the data role.

###Why every student is like a task

Fixed parts of the same response model, such as item parameters, can be shared across students; different students' latent abilities or embedding needs
Updated based on a few personal responses. Meta-learning uses "shared initialization plus few-step adaptation" to unify these two parts. It makes the training process straightforward
How to use when matching deployment: When deploying to face new students, the system has only a few individuals to answer.

!!! tip "You should remember this when reading this"
    Active learning explains "why observations should be chosen", and reinforcement learning provides a route for "how to estimate gradients for discrete strategies".
    Meta-learning explains "how to quickly adapt from a global model to an individual student." BOBCAT puts the three into double-layer optimization, and at the same time
    Keep their respective roles.
