# 局部独立、列联表与两种典型依赖

## 强局部独立

设二分题集合为 \(Q=\{q_1,\ldots,q_J\}\)，反应变量 \(X_i\in\{0,1\}\)。给定潜在特质
\(\theta\) 与项目参数 \(\Gamma\)，强局部独立写成：

\[
P(\boldsymbol X=\boldsymbol x\mid\Gamma,\theta)
=
\prod_{i=1}^{J}P(X_i=x_i\mid\Gamma_i,\theta).
\tag{1}
\]

对二分反应也可写成：

\[
\prod_{i=1}^{J}
P(X_i=1\mid\Gamma_i,\theta)^{x_i}
P(X_i=0\mid\Gamma_i,\theta)^{1-x_i}.
\]

这不是说题目在总体上独立，而是说给定\(\theta\)后独立。总体相关可以完全来自不同能力者混合。

## 4PL及其子模型

文章用四参数logistic模型说明传统IRT：

\[
P(X_i=1\mid\Gamma_i,\theta)
=
c_i+(1-c_i-d_i)
\frac{e^{a_i(\theta-b_i)}}{1+e^{a_i(\theta-b_i)}}.
\tag{2}
\]

| 参数 | 含义 |
| --- | --- |
| \(a_i\) | 区分度/斜率 |
| \(b_i\) | 难度/位置 |
| \(c_i\) | 未掌握时答对的下渐近线，通常解释为猜测 |
| \(d_i\) | 掌握后答错的上渐近损失，通常解释为失误 |

- \(d_i=0\)：3PL；
- \(c_i=d_i=0\)：2PL；
- 再令\(a_i=1\)：Rasch/1PL。

1PLAG把常数猜测改为能力函数：

\[
c_i(\theta)=\frac{1}{1+\exp(\widetilde c_i-\theta)}.
\]

文章后面用同一思想构造能力相关的\(g\)-过程。

## 弱局部独立

实际研究常用更弱的两两条件协方差为零：

\[
\operatorname{cov}(X_i,X_{i'}\mid\theta)
=
P(X_i,X_{i'}\mid\theta)
-P(X_i\mid\theta)P(X_{i'}\mid\theta)
=0.
\tag{3}
\]

强LI蕴含所有高阶联合分解；弱LI只要求两两条件协方差为零，不能保证高阶独立。

## 从条件协方差到观察列联表

对能力分布\(f(\theta)\)积分后，观测格频率和LI模型期望格频率的差为：

\[
p_{x_ix_{i'}}-p^*_{x_ix_{i'}}
=
\int
\left[
P(X_i=x_i,X_{i'}=x_{i'}\mid\theta)
-P(X_i=x_i\mid\theta)P(X_{i'}=x_{i'}\mid\theta)
\right]f(\theta)d\theta.
\tag{4}
\]

所以许多LD诊断量本质上是在比较观察列联表与LI模型所预言的列联表。

## 二乘二列联表怎样读

本文统一使用：

\[
\begin{pmatrix}
p_{00}&p_{01}\\
p_{10}&p_{11}
\end{pmatrix},
\]

其中行对应\(X_1=0,1\)，列对应\(X_2=0,1\)。四格之和为1。

## Table A：单向先决关系

\[
q_1\rightarrow q_2,
\qquad
\begin{pmatrix}
p_{00}&0\\
p_{10}&p_{11}
\end{pmatrix}.
\tag{5A}
\]

这里\(p_{01}=0\)：不可能不会第一项却会第二项。它可以表示基础技能是进阶技能的先决条件。

潜在结构为：

\[
\mathcal K_A
=
\{\varnothing,\{q_1\},\{q_1,q_2\}\}.
\]

## Table B：共同掌握或共同失败

\[
q_1\leftrightarrow q_2,
\qquad
\begin{pmatrix}
p_{00}&0\\
0&p_{11}
\end{pmatrix}.
\tag{5B}
\]

只有\(00\)与\(11\)，两题在潜在层总是一起掌握或一起失败。对应结构：

\[
\mathcal K_B
=
\{\varnothing,\{q_1,q_2\}\}.
\]

KST把这类题称为 equally informative items。这里“同等信息”指它们区分相同知识状态，
不要求题目文字相同，也不要求传统IRT难度参数相等。

## 为什么LI也能逼近Table A或B

在2PL中让斜率\(a_i\to\infty\)，项目反应曲线变成近似阶跃函数。

- 若\(b_2>b_1\)，能力区间依次主要产生\(00\)、\(10\)、\(11\)，逼近Table A；
- 若\(b_2=b_1\)，两题同时由0跳到1，逼近Table B。

但这种逼近通常需要极大斜率或难度差。更麻烦的是，逼近Table A时也可能把\(p_{11}\)压得很小。
这正是作者后来主张结构建模的动机：若某格在理论上就不可能，不必用极端连续参数勉强逼近零。

## 文章给出的LI数值基线

在\(\theta\sim N(0,1)\)、两题猜测和失误均为0时：

| 模型 | 参数 | 列联表 |
| --- | --- | --- |
| LI-1 | \(a_1=a_2=1,b_1=b_2=0\) | \(\begin{pmatrix}.293&.207\\.207&.293\end{pmatrix}\) |
| LI-3 | \(a_1=a_2=1,b_1=0,b_2=4\) | \(\begin{pmatrix}.491&.009\\.481&.019\end{pmatrix}\) |
| LI-4 | \(a_1=a_2=10,b_1=b_2=0\) | \(\begin{pmatrix}.461&.039\\.039&.461\end{pmatrix}\) |
| LI-6 | \(a_1=a_2=10,b_1=0,b_2=4\) | \(\begin{pmatrix}.500&.000\\.500&.000\end{pmatrix}\) |

LI-3靠极端难度差压低\(p_{01}\)；LI-4靠极端斜率压低两个不一致格；LI-6则连\(p_{11}\)也消失。

