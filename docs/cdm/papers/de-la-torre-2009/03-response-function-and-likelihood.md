# 反应概率与似然

## slip 与 guessing

对题目 \(j\)：

\[
s_j
=
P(X_{ij}=0\mid\eta_{ij}=1),
\]

\[
g_j
=
P(X_{ij}=1\mid\eta_{ij}=0).
\]

于是

\[
P(X_{ij}=1\mid\eta_{ij}=1)=1-s_j,
\]

\[
P(X_{ij}=0\mid\eta_{ij}=0)=1-g_j.
\]

## Equation 2

\[
P_j(\boldsymbol\alpha_i)
=
P(X_{ij}=1\mid\boldsymbol\alpha_i)
=
g_j^{1-\eta_{ij}}
(1-s_j)^{\eta_{ij}}.
\tag{3}
\]

分情况看：

\[
P_j(\boldsymbol\alpha_i)
=
\begin{cases}
g_j,&\eta_{ij}=0,\\
1-s_j,&\eta_{ij}=1.
\end{cases}
\]

无噪声时 \(g_j=s_j=0\)，观测反应等于理想反应。实际模型允许两类偏离。

通常希望

\[
1-s_j>g_j,
\]

这样掌握全部所需属性者更可能答对。本文的附录更新式没有额外推导这个不等式约束；软件实现是否强制单调性需要单独检查。

## 给定属性模式的题目似然

对学生 \(i\) 的反应向量

\[
\boldsymbol X_i=(X_{i1},\ldots,X_{iJ}),
\]

在给定 \(\boldsymbol\alpha_i\) 后假设题目局部独立：

\[
L(\boldsymbol X_i\mid\boldsymbol\alpha_i)
=
\prod_{j=1}^{J}
P_j(\boldsymbol\alpha_i)^{X_{ij}}
\left[
1-P_j(\boldsymbol\alpha_i)
\right]^{1-X_{ij}}.
\tag{4}
\]

局部独立使一名学生的联合反应概率分解成 \(J\) 个 Bernoulli 项。

## 已知属性模式时

若所有 \(\boldsymbol\alpha_i\) 已知，可把每道题的学生分成：

- \(\eta_{ij}=0\) 组；
- \(\eta_{ij}=1\) 组。

此时

\[
\widehat g_j
=
\frac{\eta_{ij}=0\text{ 组的答对人数}}
{\eta_{ij}=0\text{ 组人数}},
\]

\[
\widehat s_j
=
\frac{\eta_{ij}=1\text{ 组的答错人数}}
{\eta_{ij}=1\text{ 组人数}}.
\]

EM 只是把未知组别换成后验期望人数。

## 边际似然

属性模式未知。枚举

\[
\boldsymbol\alpha_1,\ldots,\boldsymbol\alpha_L,
\qquad L=2^K,
\]

并设

\[
\pi_l=P(\boldsymbol\alpha_l).
\]

单名学生的边际似然为

\[
L(\boldsymbol X_i)
=
\sum_{l=1}^{L}
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
\pi_l.
\tag{5}
\]

全样本似然：

\[
L(X)
=
\prod_{i=1}^{I}
\sum_{l=1}^{L}
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
\pi_l.
\tag{6}
\]

这就是一个有 \(2^K\) 类、类条件概率受 DINA 约束的有限混合模型。

## 对数形式

数值实现使用

\[
\ell(X)
=
\sum_{i=1}^{I}
\log
\left[
\sum_{l=1}^{L}
\pi_l
\exp\{
\ell_{il}^{\text{conditional}}
\}
\right].
\]

为防止许多小概率相乘下溢，代码使用 log-sum-exp：

\[
\log\sum_l e^{a_l}
=
m+\log\sum_l e^{a_l-m},
\qquad
m=\max_l a_l.
\]

这属于数值实现细节，原文用乘积公式表达统计模型。

## 必须区分的三个数

沿用[手算例子](11-worked-example.md)，某生反应101：

1. 条件似然 \(L_i(10)=.2025\)：假定画像10，出现101的概率。
2. 联合权重 \(\pi_{10}L_i(10)=.25\times.2025=.050625\)：画像10且出现101的概率。
3. 边际概率 \(m_i=\sum_l\pi_lL_i(l)=.102625\)：不指定画像时出现101的概率。

所以后验为 \(.050625/.102625=.493300853\)。

原例中 .4105 是四个条件似然的和，不是边际概率。均匀先验的 .25 可在后验分子分母约掉，却不能在计算边际对数似然时丢掉：

\[
\log m_i=\log(.25)+\log(.4105).
\]

## 为什么先乘题目、后加画像

给定同一个画像，三个反应一起发生，局部独立使

\[
L_i(l)=P(X_{i1}\mid l)P(X_{i2}\mid l)P(X_{i3}\mid l).
\]

画像事件互斥且完备，所以再按先验求和。不能交换成 \(\prod_j\sum_l\pi_lP(X_{ij}\mid l)\)：那相当于每道题重新抽一个画像，破坏同一学生共享画像的模型。

## log-sum-exp 的逐步改写

令 \(a_l=\log\pi_l+\log L_i(l)\)，\(b=\max_la_l\)。提取共同因子：

\[
\sum_le^{a_l}=e^b\sum_le^{a_l-b}.
\]

因此

\[
\log m_i=b+\log\sum_le^{a_l-b},\qquad
w_{il}=\frac{e^{a_l-b}}{\sum_he^{a_h-b}}.
\]

例如 \(a=(-1000,-1001)\) 直接指数化可能都变成浮点0；减最大值后成为 \(1,e^{-1}\)，后验仍正确地约为 .7311、.2689。这是等价计算，不是近似模型。

先验恰好为0时，对数权重应为 \(-\infty\)。现有教学主脚本的截断会将零先验变成小正数，故不能不加修改地表达严格禁止某画像的约束。
