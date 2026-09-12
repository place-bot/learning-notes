# 02 从反应矩阵到 SLAM

## 四个对象

| 对象 | 尺寸 | 含义 |
| --- | --- | --- |
| \(R=(r_{ij})\) | \(N\times J\) | 观测对错反应 |
| \(A=(a_{ik})\) | \(N\times K\) | 二值属性掌握情况 |
| \(Q=(q_{jk})\) | \(J\times K\) | 二值题目属性要求 |
| \(\Theta\) | 依模型而定 | 连续题目参数 |

给定 \(A,Q,\Theta\)，所有反应条件独立：

\[
r_{ij}\sim\mathrm{Bernoulli}(p_{ij}),\qquad
p_{ij}=f(a_i,q_j,\theta_j).
\]

“连续题目参数”不意味着 A 或 Q 是连续的。

## DINA：全部满足才进入高概率组

\[
\xi_{ij}=\prod_{k=1}^K a_{ik}^{q_{jk}},\qquad
p_{ij}=\theta_j^-+(\theta_j^+-\theta_j^-)\xi_{ij}.
\]

约定 \(0^0=1\)：没有要求的属性不影响乘积。通常 \(\theta_j^+>\theta_j^-\)，且

\[
g_j=\theta_j^-,\qquad s_j=1-\theta_j^+.
\]

例：\(q_j=(1,1,0)\)。画像 110、111 进入高概率组；其他六种画像进入低概率组。即使学生掌握第二个属性，若第一个没掌握，仍是低概率组。

注意：\(\xi\) 是理想反应，不是实际反应；高概率组仍可能答错。

## DINO 与对偶

DINO 使用“至少满足一个要求”的 OR 规则：

\[
\xi^{\mathrm{OR}}_j(a)=1-\prod_k(1-a_k)^{q_{jk}}.
\]

它与对补画像应用 AND 有联系。若同时把反应改成 \(1-R\)，DINA 对应端点为 \(1-\theta^-_{\mathrm{OR}}\) 和 \(1-\theta^+_{\mathrm{OR}}\)。不能在保持同一组端点数值不变时，随意把 DINA 概率取补当成 DINO。

## 多参数：允许部分掌握产生不同概率

令 \(S_j=\{k:q_{jk}=1\}\)，可写成

\[
p_{ij}=f\left(\mu_{j,\varnothing}
+\sum_{\varnothing\ne T\subseteq S_j}
\mu_{j,T}\prod_{k\in T}a_{ik}\right).
\]

对于 \(S_j=\{1,2\}\)，线性预测子包含截距、两个主效应和一个交互项。identity link 对应 G-DINA 的表达；logistic link 对应 LCDM 一类表达。

以 identity link 为例：

\[
p_{00}=.2,\quad p_{10}=.4,\quad p_{01}=.5,\quad p_{11}=.8
\]

对应 \(\mu_0=.2,\mu_1=.2,\mu_2=.3,\mu_{12}=.1\)。DINA 则令主效应为零，仅保留截距与最高阶交互。

## 局部类与全局画像

全局有 \(2^K\) 种画像，但单道题只看所需属性：

- DINA 把人分成两个局部类；
- 一般多参数题目最多分成 \(2^{|S_j|}\) 个局部类。

证明里剖面似然的“分组”，指这些**逐题局部类**，不是把所有题都用同一个两类划分。

来源：[§2，v3 pp.5–8](https://arxiv.org/pdf/2009.04096v3#page=5)。
