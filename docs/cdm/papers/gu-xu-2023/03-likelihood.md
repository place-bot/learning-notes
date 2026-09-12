# 03 联合似然、边际似然与闭式题目更新

## 从一个 Bernoulli 反应开始

\[
P(r_{ij}\mid A,Q,\Theta)
=p_{ij}^{r_{ij}}(1-p_{ij})^{1-r_{ij}}.
\]

条件独立允许相乘，取对数后相加：

\[
\ell(A,Q,\Theta)
=\sum_i\sum_j\{r_{ij}\log p_{ij}+(1-r_{ij})\log(1-p_{ij})\}.
\]

joint MLE 同时对 A、Q、\(\Theta\) 最大化此式。数学定义中的最大化是全局的，不是“跑一次某个程序”。

## 与边际似然比较

设总体画像比例为 \(\pi_\alpha\)。边际似然是

\[
\ell_{\mathrm{marg}}(Q,\Theta,\pi)
=\sum_i\log\left[
\sum_{\alpha\in\{0,1\}^K}\pi_\alpha
\prod_j p_j(\alpha)^{r_{ij}}\{1-p_j(\alpha)\}^{1-r_{ij}}
\right].
\]

两者最关键的差别是：一个优化每人的画像，一个对画像求和。**最大值与加权求和不相同**。边际估计后仍可做 MAP/EAP 分类，但不能把它的目标函数称为 joint MLE。

## 固定 A、Q 后，DINA 参数怎么求

令 \(G_{jc}=\{i:\xi_{ij}=c\}\)，\(n_{jc}=|G_{jc}|\)，\(s_{jc}=\sum_{i\in G_{jc}}r_{ij}\)。某一组贡献为

\[
\ell_{jc}(\theta)=s_{jc}\log\theta+(n_{jc}-s_{jc})\log(1-\theta).
\]

求导：

\[
\ell'_{jc}(\theta)=\frac{s_{jc}}{\theta}
-\frac{n_{jc}-s_{jc}}{1-\theta}.
\]

令其为零：

\[
s_{jc}(1-\theta)=(n_{jc}-s_{jc})\theta
\quad\Longrightarrow\quad
\widehat\theta_{jc}=s_{jc}/n_{jc}.
\]

二阶导非正，故为最大值；全对/全错时最大值位于端点。若规定参数必须离开 0、1，则需按规定截断。空组 \(n_{jc}=0\) 不提供信息，不能做除以零。

若另强制 \(\theta_j^+\ge\theta_j^-\)，而两个组均值违反顺序，无约束公式不能直接作为约束最优解；两组有样本时需在共同边界池化。严格大于还涉及边界是否允许及数值约定。

## 剖面似然的两种 profile

先给定结构 Z，再最大化连续题目参数：

\[
L(Z)=\sup_\Theta\ell(Z,\Theta).
\]

这里 profile likelihood 指“剖掉其他参数后的似然”，与 attribute profile（学生属性画像）是两个意思。

## 缺失反应

若可忽略缺失机制，记观测位置为 \(\Omega\)，似然改为

\[
\ell_\Omega=\sum_{(i,j)\in\Omega}
\{r_{ij}\log p_{ij}+(1-r_{ij})\log(1-p_{ij})\}.
\]

组均值的分母也必须只数观测反应。缺失不能填成答错；观测数据算法也不自动继承完整数据定理。

来源：[§3、Supplement S.2，v3 pp.9–12、41–44](https://arxiv.org/pdf/2009.04096v3#page=9)。
