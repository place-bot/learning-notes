# BOBCAT hand calculation: from topic selection to influence function

## Settings throughout the hand calculation example

### One student, four questions

To make each step hand-countable, 1PL IRT was used. There is only one training student, so \(i=1\). The item bank has four questions,
\(Q=4\), difficulty is

\[
b_1=-1,\qquad b_2=0,\qquad b_3=1,\qquad b_4=1.
\]

The first three questions are used as training candidates:

\[
\Omega_1^{(1)}=\{1,2,3\},
\]

The fourth question is used as a meta question:

\[
\Gamma_1=\{4\}.
\]

The two sets do not intersect.

In historical data, the student’s answer is set to

\[
Y_{1,1}=1,\quad
Y_{1,2}=1,\quad
Y_{1,3}=0,\quad
Y_{1,4}=0.
\]

These answers are known in the offline training data, but when simulating question selection, the inner layer is only allowed to see the answers to the actual selected training questions.

### Global initialization and inner rules

Global capabilities are initialized as

\[
\mu=0.
\]

local capabilities from

\[
\theta_1^{(0)}=0
\]

Start. In order to see the effect of topic selection first, only one step is taken in the inner layer, \(K=1\), learning rate

\[
\alpha=0.5.
\]

The response probability is

\[
g(j;\theta)=\sigma(\theta-b_j).
\]

### Initial strategy

Initial status no answer:

\[
x_1^{(1)}=(0,0,0,0).
\]

Assume that the probability of the topic selection network on the three training candidate topics is

\[
\Pi_\phi(\cdot\mid x_1^{(1)})
=(0.2,0.5,0.3).
\]

This means that questions 1, 2, and 3 have \(20\%\), \(50\%\), and \(30\%\) probabilities respectively. Probability itself does not explain which question
Really best; training will change it based on the meta result.

## If question 2 is drawn, the complete forward process

### Read answers and update status

Suppose you get this time

\[
j_1^{(1)}=2.
\]

The history matrix tells us \(Y_{1,2}=1\). The status becomes

\[
x_1^{(2)}=(0,1,0,0),
\]

Question 2 Remove from available set:

\[
\Omega_1^{(2)}=\{1,3\}.
\]

### Inner layer adapts in one step

Current ability 0, question 2 difficulty 0, initial probability of correct answer

\[
p_{1,2}^{(0)}
=\sigma(0-0)=0.5.
\]

The student answered correctly, so the single-question loss gradient is

\[
\frac{\partial\ell_{1,2}}{\partial\theta}
=p_{1,2}^{(0)}-Y_{1,2}
=0.5-1=-0.5.
\]

One step update:

\[
\theta_1^{(1)}
=0-0.5(-0.5)
=0.25.
\]

### Predict on meta questions

The difficulty of question 4 is 1, and the probability of correct answer after adaptation is

\[
\widehat p_{1,4}
=\sigma(0.25-1)
=\sigma(-0.75)
\approx0.3208.
\]

The real meta answer is \(Y_{1,4}=0\), cross-entropy is

\[
\mathcal L_1^{\mathrm{meta}}
=-\log(1-0.3208)
\approx0.3869.
\]

This number is the outer result of the current sampling trajectory.

### Why good fitting of training questions does not mean good meta

The probability of correct answer to question 2 after the update is

\[
\sigma(0.25)\approx0.5622,
\]

The answer is more consistent with the correct answer than before the update. However, the increase in ability also makes the model more inclined to believe that the student will answer difficult question 4 correctly, and the student
Actually got question 4 wrong. Therefore, this correct answer to the intermediate question may not be the best choice for the current meta goal.

## Compare all three candidate questions counterfactually

### If multiple choice question 1

Question 1 difficulty \(-1\), initial probability

\[
p_{1,1}^{(0)}=\sigma(1)\approx0.7311.
\]

The answer is 1, gradient

\[
g_1=p_{1,1}^{(0)}-1\approx-0.2689.
\]

one step update

\[
\theta_{(j=1)}'
=0-0.5(-0.2689)
\approx0.1345.
\]

meta correct answer probability

\[
\widehat p_{4\mid j=1}
=\sigma(0.1345-1)
\approx0.2962.
\]

Since the true meta answer is 0,

\[
L_{4\mid j=1}
=-\log(1-0.2962)
\approx0.3512.
\]

### If multiple choice question 2

The previous chapter has been obtained

\[
\theta_{(j=2)}'=0.25,\qquad
L_{4\mid j=2}\approx0.3869.
\]

### If multiple choice question 3

Question 3 Difficulty 1, initial probability of correct answer

\[
p_{1,3}^{(0)}=\sigma(-1)\approx0.2689.
\]

The answer is 0, gradient

\[
g_3=p_{1,3}^{(0)}-0\approx0.2689.
\]

One-step update reduces capabilities:

\[
\theta_{(j=3)}'
=0-0.5(0.2689)
\approx-0.1345.
\]

Probability of correct answer to meta question

\[
\widehat p_{4\mid j=3}
=\sigma(-0.1345-1)
\approx0.2433,
\]

The meta loss is

\[
L_{4\mid j=3}
=-\log(1-0.2433)
\approx0.2787.
\]

### Comparison table

**Table: One-step adaptation and meta result after selecting different training questions**

|Multiple choice questions|historical answer|inner gradient|post-adaptation ability|meta loss|
| --- | --- | --- | --- | --- |
| 1 | 1 | \(-0.2689\) | \(0.1345\) | \(0.3512\) |
| 2 | 1 | \(-0.5000\) | \(0.2500\) | \(0.3869\) |
| 3 | 0 | \(0.2689\) | \(-0.1345\) | \(0.2787\) |

For this student and this meta-question, Question 3 is the most useful because its wrong answer pushes down the ability and just improves the ability.
Prediction of the wrong answer to another difficult question. The initial strategy favors question 2 the most. The goal of outer layer training is to gradually correct this mismatch.

### What will the traditional uncertainty rule choose?

When the initial ability is 0, the probability of answering the three questions correctly is

\[
(0.7311,0.5000,0.2689).
\]

The closest to \(0.5\) is question 2, so IRT-Active will select question 2. This example deliberately constructs the question 3 pairs of meta
Predicting more valuable situations is used to demonstrate the differences between BOBCAT goals and traditional local information goals. This construction example
The scope of the conclusion is limited to the comparison of objective functions, and it is impossible to judge the advantages and disadvantages of BOBCAT and Fisher information in all scenarios.

## Unbiased policy gradient in the same example

### Assume baseline is the expected counterfactual loss

To facilitate hand calculation, let baseline equal the weighted average of the losses of the three actions under the current strategy:

\[
\begin{aligned}
b_1
&=0.2(0.3512)+0.5(0.3869)+0.3(0.2787)\\
&\approx0.3473.
\end{aligned}
\]

The actual algorithm cannot observe all counterfactuals on every deployment, but training the critic can approximate this expectation.

### This time I got question 2

The loss of question 2 is higher than baseline:

\[
L_{4\mid j=2}-b_1
\approx0.3869-0.3473
=0.0396.
\]

The single-sample gradient of REINFORCE is

\[
\widehat g_\phi
=0.0396\,
\nabla_\phi
\log\Pi_\phi(j=2\mid x_1^{(1)}).
\]

Gradient descent will reduce the log probability of question 2 because it brings a higher loss than the baseline.

### If you get question 3 this time

\[
L_{4\mid j=3}-b_1
\approx0.2787-0.3473
=-0.0686.
\]

The coefficient is negative. Gradient descent therefore improves the log probability of question 3.

### Specific derivatives of softmax logits

Let the three logits of the strategy be \(z_1,z_2,z_3\), and the probability is
\(\pi_r=\exp(z_r)/\sum_s\exp(z_s)\). If action \(a\) is drawn, there is

\[
\frac{\partial\log\pi_a}{\partial z_r}
=
\mathbb{I}(r=a)-\pi_r.
\]

Among them, \(\mathbb{I}(r=a)\) is 1 when \(r=a\), otherwise it is 0.

Question 2 is drawn, the current probability is \((0.2,0.5,0.3)\), so

\[
\nabla_z\log\pi_2
=(-0.2,0.5,-0.3).
\]

Multiply \(0.0396\):

\[
\widehat g_z
\approx(-0.00792,0.01980,-0.01188).
\]

After doing gradient descent \(z\leftarrow z-\eta_2\widehat g_z\), the logit of question 2 is reduced, and the logit of question 1 and question 3 is reduced.
The logits are relatively increasing.

### I don’t know if question 3 is better than question 1 in a single update.

The sample drawn for question 2 only shows that the performance of question 2 is biased. Questions 1 and 3 both obtain relative results due to softmax normalization.
rise, but this signal cannot sufficiently differentiate between them. One must wait for more sampling, or use a method that utilizes all candidates
Approx gradient. This is exactly a matter of variance and sample efficiency.

## Influence function in the same example

### Add curvature stabilization term

In order to make the one-dimensional Hessian stable and reversible, add

\[
\frac{\lambda}{2}(\theta-\mu)^2,
\qquad \lambda=0.5.
\]

Near the initial \(\theta=0\), the gradient of meta question 4 is

\[
g_{\mathrm{meta}}
=p_4-Y_{1,4}
=\sigma(-1)-0
\approx0.2689.
\]

### Gradient and Hessian of each candidate question

The gradient of the first three questions is

\[
g_1\approx-0.2689,\qquad
g_2=-0.5,\qquad
g_3\approx0.2689.
\]

The second derivative of the single question is \(p_j(1-p_j)\), plus the regular curvature \(\lambda\):

\[
H_j=\lambda+p_j(1-p_j).
\]

So

\[
H_1=H_3\approx0.5+0.1966=0.6966,
\qquad
H_2=0.5+0.25=0.75.
\]

### Calculate the impact score on a question-by-question basis

The one-dimensional influence function is

\[
\mathcal I_1(j)
=-\frac{g_{\mathrm{meta}}g_j}{H_j}.
\]

So

\[
\begin{aligned}
\mathcal I_1(1)
&\approx-\frac{(0.2689)(-0.2689)}{0.6966}
\approx 0.1038,\\
\mathcal I_1(2)
&\approx-\frac{(0.2689)(-0.5)}{0.75}
\approx 0.1793,\\
\mathcal I_1(3)
&\approx-\frac{(0.2689)(0.2689)}{0.6966}
\approx -0.1038.
\end{aligned}
\]

Question 3 has a negative impact score, indicating that increasing its weight in the inner layer is expected to reduce the meta loss. Questions 1 and 2 are correct.
This ranking is consistent with the counterfactual result after taking a complete step in the previous chapter:

\[
\text{Question 3 is the best, Question 1 is the second best, Question 2 is the worst}.
\]

### How does Approx gradient compare all questions at once?

continuous relaxation

\[
\mathcal J_{\mathrm{relaxed}}
\approx
\sum_{j=1}^{3}\pi_j\mathcal I_1(j),
\]

Derive the logits. The softmax derivative gives

\[
\frac{\partial\mathcal J_{\mathrm{relaxed}}}{\partial z_r}
=
\pi_r\left(
\mathcal I_1(r)-\sum_j\pi_j\mathcal I_1(j)
\right).
\]

The current probability is \((0.2,0.5,0.3)\), and the weighted average impact is approximately

\[
\bar{\mathcal I}
=0.2(0.1038)+0.5(0.1793)+0.3(-0.1038)
\approx0.0793.
\]

So the three logit gradients are approximately

\[
\left(
0.2(0.0245),\,
0.5(0.1000),\,
0.3(-0.1831)
\right)
\approx
(0.0049,0.0500,-0.0549).
\]

Gradient descent will significantly reduce the logit of question 2 and improve the logit of question 3. One update has used all three questions
relative information.

### The difference between this hand calculation and the actual training in the paper

The hand calculation uses the candidate's respective Hessian at \(\theta=0\) in order to show the sign direction. Thesis formula (11) is currently
At the inner layer solution \(\theta_i^*\), use the unified Hessian of the existing inner layer target to evaluate the small weight perturbations of each candidate question. complete
The neural implementation approximates gradients through automatic differentiation and straight-through propagation. The three share "How to change the candidate questions"
Local parameters, how to change the core chain of meta loss", but the numerical details are different.

!!! tip "You should remember this when reading this"
    REINFORCE updates the log probability through the drawn trajectory and endpoint loss; the influence function passes
    \(-g_{\mathrm{meta}}^{\mathsf{T}}H^{-1}g_j\) gives each candidate a local counterfactual score. The former is unbiased but
    Sparse and high variance, the latter is biased but signal dense.
