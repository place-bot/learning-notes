# BOBCAT’s double-layer optimization

## First understand level and optimization separately.

### level is the decision-making level

bilevel optimization literally translates as double-layer optimization. bi means two, and level means level. A two-level problem consists of
Two optimization tasks, the outer task chooses a decision, and the inner task makes its own optimal response given the outer decision.
The outer layer must anticipate this reaction in order to know whether its decision is a good one.

The most general unconstrained form can be written as

\[
\begin{aligned}
\min_{u}\quad &F(u,v^*(u)), \\
\text{subject to}\quad
&v^*(u)\in\operatorname*{arg\,min}_v f(u,v).
\end{aligned}
\]

Now only four objects are introduced.

- \(u\) is the outer selected variable.
- \(v\) is the inner selected variable.
- \(f(u,v)\) is the inner objective function.
- \(F(u,v)\) is the outer objective function.

The notation \(v^*(u)\) emphasizes that the inner optimal solution depends on \(u\). The asterisk represents "the value obtained after solving the inner layer", and the
\(u\) means it is a function of \(u\). After substituting this function into the outer layer, the outer layer actually optimizes the composite function.

\[
\widetilde F(u)=F(u,v^*(u)).
\]

### Why can’t we add the two losses directly?

A common misconception is to rewrite the two-level problem as

\[
\min_{u,v} F(u,v)+f(u,v).
\]

This addition problem changes the original goal. The additive form allows both outer and inner layers to be compromised simultaneously; the bilayer form requires the inner layer to be
The \(u\) first obeys its own optimality conditions. The outer layer can only be optimized based on how the inner layer will react.

!!! example "Small example: hyperparameter selection is the easiest to understand two-layer problem"
    Let \(u=\lambda\) be the regularization strength and \(v=w\) be the model weights. The inner layer is fit on the training set

    \[
    w^*(\lambda)=\operatorname*{arg\,min}_w
    \left\{L_{\mathrm{train}}(w)+\lambda\|w\|_2^2\right\}.
    \]

    For the outer layer, select \(\lambda\) in the validation set:

    \[
    \min_\lambda L_{\mathrm{valid}}(w^*(\lambda)).
    \]

    The quality of the verification loss must be evaluated on "\(w^*(\lambda)\) trained with this \(\lambda\)". If training
    The simple addition of loss and validation loss changes the roles of training and validation.

### Who in BOBCAT corresponds to u and who corresponds to v

In BOBCAT, outer variables are a set of global variables:

\[
u=(\gamma,\phi).
\]

\(\gamma\) is the global response model parameter, and \(\phi\) is the question selector parameter. Inner variables are local parameters for each student:

\[
v=\{\theta_1,\ldots,\theta_N\}.
\]

Given \(\gamma\) and \(\phi\), the question selector first determines which training questions each student sees, and the inner layer then answers based on these
Get \(\theta_i^*(\gamma,\phi)\). The outer layer uses meta questions to determine whether these local parameters are good or not.

### Why do local optimal parameters rely on both the global response model and the topic selector?

Dependence \(\gamma\) is easy to understand: local parameters start from global initialization, or are pulled to global values by regular terms. Depend on
\(\phi\) Slightly hidden: Which answers to use for inner losses are determined by the question selector. Even if \(\phi\) is not written directly into
The response probability is \(g(j;\theta_i)\), which also changes the inner training data through the selected question number.

The dependency chain can be written as

\[
\phi
\longrightarrow
\{j_i^{(1)},\ldots,j_i^{(n)}\}
\longrightarrow
\mathcal L_i^{\mathrm{inner}}
\longrightarrow
\theta_i^*
\longrightarrow
\mathcal L_i^{\mathrm{meta}}.
\]

The gradient of the outer training \(\phi\) must be returned along this chain.

### leader-follower is a metaphor for understanding nested structures

Bi-level planning is sometimes explained by the leader-follower game: the leader makes decisions first, and the followers respond optimally.
BOBCAT There are no two real actors with independent interests. The "inner layer" here is the student parameter adaptation algorithm, and the "outer layer"
is the global training criterion. leader-follower only helps to understand the nested structure and should not lead to the misunderstanding that students are gaming the system.

## How to find the derivative of a double-layer problem

### The real difficulty is the solution map

return to normal form

\[
\widetilde F(u)=F(u,v^*(u)).
\]

When taking the derivative of \(u\), the chain rule gives

\[
\frac{\mathrm d\widetilde F}{\mathrm du}
=
\frac{\partial F}{\partial u}
+
\frac{\partial F}{\partial v^*}
\frac{\mathrm dv^*}{\mathrm du}.
\]

The first item is the outer target's direct dependency on \(u\). The second process
\(\mathrm dv^*/\mathrm du\), describes how the outer variables change the inner optimal solution and how they affect the outer loss.
The entire derivative is often called hypergradient or meta-gradient.

### Route 1: Expand limited step optimization

If the inner layer uses the \(K\) step truncation optimization starting from \(v^{(0)}(u)\),

\[
v^{(k+1)}
=v^{(k)}-\alpha\nabla_v f(u,v^{(k)}),
\]

You can keep all \(K\) steps in the calculation graph and then backpropagate. This is called unrolling or
differentiating through optimization。

Its advantage is that the concept is straightforward and strictly consistent with the actual \(K\) step adaptation. The disadvantage is that intermediate state needs to be saved and may
Calculate the second derivative. If \(K\) is large, memory and time will become heavy.

### Route 2: Implicit derivation using inner optimality conditions

If \(v^*(u)\) truly satisfies the inner first-order condition

\[
\nabla_v f(u,v^*(u))=0,
\]

Derive \(u\):

\[
\nabla^2_{vv} f\,
\frac{\mathrm dv^*}{\mathrm du}
+
\nabla^2_{vu}f=0.
\]

If Hessian \(\nabla^2_{vv} f\) is reversible,

\[
\frac{\mathrm dv^*}{\mathrm du}
=-
\left(\nabla^2_{vv}f\right)^{-1}
\nabla^2_{vu}f.
\]

This is called implicit differentiation. It can save the need to save long optimization trajectories, and at the same time need to solve a problem involving
Hessian linear system. In practice, it is usually through the Hessian-vector product or linear equation
\(Hz=q\) completes calculation.

### BOBCAT borrows two ideas at the same time

For the global response model parameter \(\gamma\), the paper follows the MAML idea to perform backpropagation on a small number of inner layer GD, and uses
The first-order approximation reduces the amount of calculation. For the Approx question selector gradient, in order to evaluate the impact of all current candidate questions, the paper uses
Inner layer optimality conditions and influence functions, the inverse Hessian appears in Equation (11).

The official PyTorch implementation also uses straight-through to construct the forward propagation of hard-selected topics and the backpropagation of softmax.
Therefore three levels should be distinguished:

1. Exact argmin in mathematical framework;
1. Truncated GD, implicit influence function and gradient approximation in the derivation of the paper;
1. Automatic differentiation implementation in code that runs efficiently.

### first-order approximation What is lost

Let one layer adapt to

\[
v'=u-\alpha\nabla f(u).
\]

The exact Jacobian is

\[
\frac{\partial v'}{\partial u}
=I-\alpha\nabla^2f(u).
\]

first-order MAML approximates this as \(I\). So the outer gradient is approximately

\[
\nabla_u F(v')\approx\nabla_{v'}F(v').
\]

It ignores the curvature information of how changing the initialization will change the inner gradient direction. Approximately cheaper, but not equal to exact
Two-layer gradient.

!!! warning "Easily misunderstood"
    “First-order” does not imply that the response model is first-order IRT, nor does it imply that only one step of GD is taken. It is expressed in meta-gradient
    Some second-order derivative terms are ignored in . The inner layer can still take \(K>1\) steps, and the response model can also be a deep network.

## Why are training set, validation set, and meta set easy to confuse?

### There are two different dimensions of data division

There are at least two categories of BOBCAT experiments, which cannot be mixed into one.

1. **Divided by students**: Students are divided into training students, verification students and test students, which are used to evaluate new students
    generalization. The paper uses five-fold cross-validation, and students are divided according to \(60\%/20\%/20\%\) in each fold.
1. **Divide each student by question**: The questions that the student has answered are divided into training candidate sets and
    meta set. The paper is divided approximately according to \(80\%/20\%\) during training, and is regenerated randomly in each epoch.

The first division answers "Can the strategy be generalized to new students who have not participated in the training?" The second type divides manufacturing into two-tier tasks:
Training candidate questions are used to simulate short tests and inner-level adaptation, and meta questions are used for outer-level evaluation.

### Why meta questions cannot participate in inner adaptation

If the student parameters are updated with answers to meta questions first, and then predictions are evaluated on the same batch of questions, information leakage will occur. Outer layer loss
It may be very low, but it does not mean that a small number of selected questions have predictive power for unseen questions. Let the training and meta sets be disjoint, ensuring
The outer layer asks "whether the student representations learned from the selected training questions can be transferred to another batch of questions."

### meta is not equal to the final test

Meta questions are held-out questions used internally by each training student for outer learning. Ultimately test students are completely independent of
Global parameter learning. The training process can repeatedly use the meta questions of training students to update \(\gamma\) and \(\phi\).
Therefore, these meta questions belong to training supervision data.

```text
All history students
├── Train students
│ ├── Student training candidate questions
│ └── Meta questions within students
├── Verify students
└── Test students
```

### Actual set when sparse response matrix

Theoretically, the item bank has \(Q\) questions, but student \(i\) may only answer a subset, recorded as

\[
\mathcal O_i=\{j:Y_{i,j}\text{being observed}\}.
\]

BOBCAT's initial candidate set \(\Omega_i^{(1)}\) and meta set \(\Gamma_i\) for this student are both from
generated in \(\mathcal O_i\) and requested

\[
\Omega_i^{(1)}\cap\Gamma_i=\varnothing.
\]

Here \(\Gamma\) is pronounced Gamma. It specifically represents a collection of meta questions. Collection superscript \((1)\) Description
\(\Omega_i^{(1)}\) is the initial set of options before choosing any question.

!!! tip "You should remember this when reading this"
    Division by student is used to test generalization to new students; division by question within each student is used to construct two-tier tasks. The meta question is left as
    The outer layer evaluates and participates in outer layer parameter update; the final test set consists of independent test students.
