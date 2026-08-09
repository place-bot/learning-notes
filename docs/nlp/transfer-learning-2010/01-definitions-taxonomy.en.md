# Domain, Task and migration definitions

## 1. Domain

\[
\mathcal D=\{\mathcal X,P(X)\}.
\]

\(\mathcal X\) is the feature space, and \(P(X)\) is the marginal distribution. Even if the two corpora use the same vocabulary, there may be differences due to different topics and expression frequencies.

\[
P_S(X)\ne P_T(X).
\]

## 2. Task

\[
\mathcal T=\{\mathcal Y,P(Y\mid X)\}.
\]

\(\mathcal Y\) is the label space, and \(P(Y\mid X)\) is the target prediction relationship. Emotion classification and NLI have different label spaces and conditional rules, and they belong to different tasks.

## 3. Transfer learning

Using source knowledge to improve target learning:

\[
(\mathcal D_S,\mathcal T_S)
\longrightarrow
f_T\text{ on }\mathcal D_T.
\]

If both domain and task are exactly the same, it is conventional identically distributed learning; migration involves at least changes in domain or task.

## 4. Why does pretraining model belong to migration?

language modelpretraining:

\[
\mathcal T_S=\text{token prediction}.
\]

Downstream classification:

\[
\mathcal T_T=\text{label prediction}.
\]

The task changes, and the pretraining general corpus is very different from the \(P(X)\) in the downstream field. The pretraining parameters serve as transferable knowledge to initialize the target model.

## 5. Historical role of Survey

The paper systematically organizes the examples, features, parameters and relationship knowledge transfer up to 2009. The modern foundation model is much larger than its examples, but the basic notation still clearly distinguishes "what is different, what is transferred, and when it is harmful."
