# 确定性LD：boundary mixture、SLD与KST-IRT

## 确定性LD的真正含义

确定性LD从真子结构开始：

\[
\mathcal K\subsetneq2^Q.
\]

某些潜在反应或掌握模式因此被排除。最终模型仍然是概率模型；“确定性”只描述随机过程之前已经存在结构约束。

## 为什么需要\(g\)-过程

若\(01\notin\mathcal K\)，潜在层有：

\[
\pi(01\mid\theta)=0.
\]

但现实中可能因为：

- 第一题粗心答错；
- 第二题猜对；
- 评分错误；
- 临时策略变化；

观察到\(X=01\)。因此\(g\)-过程把潜在结构映射到完整观察反应空间：

\[
(\mathcal K,2^Q).
\]

## Boundary mixture copula的结构解释

文章把总体看成两个潜在成分的混合：

\[
P_t(X\mid\theta)
=(1-\delta_t)P_{2^Q}(X\mid\theta)
+\delta_tP_{\mathcal K}(X\mid\theta).
\tag{33}
\]

其中：

- 以概率\(1-\delta_t\)，个体属于完整幂集成分；
- 以概率\(\delta_t\)，个体属于受限结构成分。

一般mixture copula写成：

\[
P_t(X_i,X_{i'}\mid\theta)
=(1-\delta_t)P(X_i\mid\theta)P(X_{i'}\mid\theta)
+\delta_tP_{\mathcal K}(X_i,X_{i'}\mid\theta).
\tag{34}
\]

当第二成分位于Fréchet-Hoeffding上边界时，它只允许Table A或Table B式模式，因此属于确定性LD。

## SLD的复制机制

SLD可以表述为：

- 以概率\(1-\pi_{LD}\)，第二题按自己的IRF作答；
- 以概率\(\pi_{LD}\)，第二题直接复制第一题。

\[
P^*(X_{i'}=1\mid\theta)
=(1-\pi_{LD})P(X_{i'}=1\mid\theta)
+\pi_{LD}P^*(X_i=1\mid\theta).
\tag{36}
\]

复制成分中：

\[
X_{i'}=X_i,
\]

所以只有\(00\)和\(11\)，不一致格\(01,10\)在该成分中结构上不可能。

## 对称答对率为.5时的手算

若两题独立分支中的答对率均为\(.5\)：

\[
P_{LI}(00)=P_{LI}(01)=P_{LI}(10)=P_{LI}(11)=\frac14.
\]

复制分支中：

\[
P_{copy}(00)=P_{copy}(11)=\frac12,
\qquad
P_{copy}(01)=P_{copy}(10)=0.
\]

混合后：

\[
P_{11}=P_{00}
=\pi_{LD}\frac12+(1-\pi_{LD})\frac14
=\frac{1+\pi_{LD}}4,
\]

\[
P_{10}=P_{01}
=(1-\pi_{LD})\frac14.
\]

因此中等\(\pi_{LD}\)就能明显压低不一致格。这解释了为什么用连续ULD因子模仿SLD时可能需要极大载荷。

## SLD与Ackerman-Spray模型

Ackerman与Spray允许两个转移方向有不同缩放系数：

\[
\alpha^*_{ii'}
=\alpha P(X_{i'}=1\mid\theta),
\qquad
\beta^*_{ii'}
=\beta P(X_{i'}=0\mid\theta).
\]

当\(\alpha=\beta=1\)时恢复LI；当\(\alpha=\beta=0\)时第二题完全跟随第一题。令：

\[
\pi_{LD}=1-\alpha=1-\beta
\]

就得到对称SLD。完整代数见[附录页](12-appendices.md)。

## 两过程KST-IRT

一般形式是：

\[
P(\boldsymbol X=\boldsymbol x\mid\theta)
=
\sum_{K\in\mathcal K}
P(\boldsymbol X=\boldsymbol x\mid K)
\pi(K\mid\theta).
\]

右边两部分分别是：

- SRF \(\pi(K\mid\theta)\)：能力产生知识状态；
- \(g\)-矩阵\(P(\boldsymbol X\mid K)\)：知识状态产生观察反应。

## Table A的\(g\)-矩阵

对链：

\[
\mathcal K_A=\{00,10,11\},
\]

观察概率向量由一个\(4\times3\)矩阵乘状态概率向量：

\[
\begin{pmatrix}
P(00\mid\theta)\\P(01\mid\theta)\\P(10\mid\theta)\\P(11\mid\theta)
\end{pmatrix}
=G_A
\begin{pmatrix}
\pi(00\mid\theta)\\\pi(10\mid\theta)\\\pi(11\mid\theta)
\end{pmatrix}.
\tag{37}
\]

矩阵的每一列对应一个潜在知识状态，每一行对应一个观察模式。列内概率和为1。

例如潜在状态\(10\)生成观察\(01\)要求第一题失误、第二题猜对，因此对应概率包含：

\[
\beta_1\eta_2.
\]

潜在状态\(11\)生成观察\(01\)要求第一题失误、第二题不失误，因此包含：

\[
\beta_1(1-\beta_2).
\]

这样潜在结构仍禁止\(01\)，但观察层允许它以小概率出现。

## Table B的\(g\)-矩阵

对：

\[
\mathcal K_B=\{00,11\},
\]

\[
\begin{pmatrix}
P(00\mid\theta)\\P(01\mid\theta)\\P(10\mid\theta)\\P(11\mid\theta)
\end{pmatrix}
=G_B
\begin{pmatrix}
\pi(00\mid\theta)\\\pi(11\mid\theta)
\end{pmatrix}.
\tag{38}
\]

不一致反应只能由猜测或失误产生。没有\(g\)-过程时，\(p_{01}=p_{10}=0\)精确成立。

## 为什么概率性模型里通常没有\(g\)-过程

这不是因为从\(2^Q\)到\(2^Q\)不能定义\(g\)-过程。完全可以定义：

\[
(2^Q,2^Q).
\]

只是多数传统IRT-LD模型直接把潜在反应与观察反应视为同一层：

\[
P(X\mid\theta)=\pi(K\mid\theta).
\]

此时\(g\)-过程等于恒等映射，写出来没有新增内容。4PL等带猜测和失误模型则可以重新解释为非平凡\(g\)-过程。

