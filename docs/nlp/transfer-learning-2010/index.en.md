# transfer learning: Pan & Yang (2010)

**A Survey on Transfer Learning** is a classic review of transfer learning. The idea of ​​transfer is earlier than this article; it is chosen here because the paper provides a unified domain/task definition and classification framework, which is suitable for answering "Why does BERT belong to transfer learning?"

## Core definition

a domain:

\[
\mathcal D=\{\mathcal X,P(X)\}.
\]

A learning task:

\[
\mathcal T=\{\mathcal Y,P(Y\mid X)\}.
\]

transfer learning utilizes the knowledge of the source \((\mathcal D_S,\mathcal T_S)\) to improve the target prediction \(f_T\), provided that

\[
\mathcal D_S\ne\mathcal D_T
\quad\text{or}\quad
\mathcal T_S\ne\mathcal T_T.
\]

## Reading route

1. [Domain, Task and Migration Definition](01-definitions-taxonomy.md)
2. [Three settings and four types of migration methods](02-settings-methods.md)
3. [Negative migration with a heavily weighted hand calculation](03-negative-transfer-worked-example.md)
4. [Relationship with BERT pretraining—fine-tuning](04-bert-connection-conclusion.md)
5. [Reference](references.md)
