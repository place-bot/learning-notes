# Three settings and four types of migration methods

## 1. Inductive transfer

\[
\mathcal T_S\ne\mathcal T_T.
\]

The target domain has a small amount of annotations, which are used to learn the objective function. Pretraining language models to sentiment classification, QA or NLI fall into this broad category.

## 2. Transductive transfer

\[
\mathcal T_S=\mathcal T_T,
\qquad
\mathcal D_S\ne\mathcal D_T.
\]

The source domain is labeled, but the target domain is usually unlabeled. Typical cases are domain adaptation or covariate shift.

## 3. Unsupervised transfer

The source and target tasks are related but different. The target task is an unsupervised task such as clustering, dimensionality reduction or density estimation. There are no labels when training both parties.

## 4. Four categories of “what to transfer”

|Category|transfer object|Typical mechanism|
|---|---|---|
| Instance-based |source sample|Reweighting/selecting useful source samples|
| Feature-representation |express|Learn shared features across domains|
| Parameter-transfer |Parameters/prior|Share or initialize model parameters|
| Relational-knowledge |entity relationship|Migrate relationship structure|

BERT embodies both representation migration and parameter migration: the pretraining encoder generates a universal representation, and the downstream model is initialized by the pretraining parameters and continues to be updated.

## 5. Three core questions

- What to transfer: What knowledge can be shared;
- How to transfer: how to code and optimize;
- When to transfer: When will it improve or hurt the target mission.

What LoRA changes is how: it uses low-rank parameters to carry target updates; BERT pretraining mainly provides what: contextualized language representation and parameters.
