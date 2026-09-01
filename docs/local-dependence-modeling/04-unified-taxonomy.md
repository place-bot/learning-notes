# 统一框架与两张分类表

## Table 1：按\(p\)-过程和\(g\)-过程分类测量模型

第一张表还没有专门区分LD，而是先把KST、CDA与IRT放入同一坐标。

| \(g\)-过程 | 无\(p\)-过程 | 有\(p\)-过程 |
| --- | --- | --- |
| 无\(g\)-过程 | 完整或不完整列联表，状态概率就是格概率 | 传统潜在类/CDA/IRT：能力或属性通过\(p\)-过程产生反应或掌握 |
| 能力独立\(g\)-过程 | 基本概率KST：\(P(X)=\sum_KP(X\mid K)\pi(K)\) | KST-CDA/KST-IRT：同时有掌握过程和固定猜测/失误过程 |
| 能力相关\(g\)-过程 | 无\(p\)-过程的混合模型 | 最一般但很少使用：掌握与误差都可依赖能力/属性 |

模型从上到下、从左到右越来越一般；上层模型通常可通过参数约束嵌套在下层模型中。

## 传统CDA与IRT怎样放入过程框架

CDA以离散能力状态\(C\)为潜变量：

\[
P(X)=\sum_{C\in\mathcal C}P(X\mid C)\nu(C).
\tag{10}
\]

IRT把潜在状态推广成连续\(\theta\)：

\[
P(X)=\int P(X\mid\theta)f(\theta)d\theta.
\tag{11}
\]

基本概率KST则是：

\[
P(X)=\sum_{K\in\mathcal K}P(X\mid K)\pi(K).
\tag{12}
\]

KST-IRT把连续能力与知识状态接起来：

\[
P(X)=\int\sum_{K\in\mathcal K}
P(X\mid K)\pi(K\mid\theta)f(\theta)d\theta.
\tag{14}
\]

条件在\(\theta\)上时，核心方程为：

\[
P(X\mid\theta)
=
\sum_{K\in\mathcal K}P(X\mid K)\pi(K\mid\theta).
\tag{19}
\]

## 为什么SRF是IRF的集合推广

单题IRF给出：

\[
P(X_i=1\mid\theta).
\]

状态反应函数（state response function, SRF）给出整个题目集合状态的概率：

\[
\pi(K\mid\theta),\qquad K\in\mathcal K.
\]

若\(K=\{q_1,q_3\}\)，SRF回答能力为\(\theta\)的人恰好掌握第1、第3题而不掌握其他题的概率。

## 从一般KST-IRT方程推回4PL

单题结构只有\(\varnothing\)与\(\{q_i\}\)：

\[
\begin{aligned}
P(X_i=1\mid\theta)
&=P(X_i=1\mid\varnothing)\pi(\varnothing\mid\theta)\\
&\quad+P(X_i=1\mid\{q_i\})\pi(\{q_i\}\mid\theta)\\
&=c_i\pi(K_i=0\mid\theta)+(1-d_i)\pi(K_i=1\mid\theta)\\
&=c_i+(1-c_i-d_i)\pi(K_i=1\mid\theta).
\end{aligned}
\]

若\(\pi(K_i=1\mid\theta)\)是2PL，就得到4PL。这说明“左侧增广”参数\(c_i,d_i\)来自\(g\)-过程。

## BLIM与\(\Theta\)-BLIM

若给定知识状态后，各题猜测/失误独立：

\[
P(\boldsymbol X\mid K)
=
\prod_{i=1}^{J}
P(X_i=1\mid K)^{X_i}
P(X_i=0\mid K)^{1-X_i},
\tag{20}
\]

并定义：

\[
P(X_i=1\mid K)
=(1-\beta_i)^{K_i}\eta_i^{1-K_i},
\]

就得到BLIM。\(\eta_i\)是lucky guess，\(\beta_i\)是careless error。

把状态概率改为\(\pi(K\mid\theta)\)便得到\(\Theta\)-BLIM。它不预先规定SRF的具体形式，
因此是一个容纳不同状态模型的总框架。

## GLI与外缘\(K^O\)

广义局部独立（generalized local independence, GLI）把SRF写成：

\[
\pi(K\mid\theta)
=
\prod_{q_i\in K}\pi(K_i=1\mid\theta)
\prod_{q_i\in K^O}\pi(K_i=0\mid\theta).
\tag{21}
\]

外缘定义为：

\[
K^O
=
\{q_i\in Q\setminus K:K\cup\{q_i\}\in\mathcal K\}.
\]

它只包括“从当前状态出发，可以合法增加一步”的题。不能添加的题不应作为普通未掌握题进入乘积，否则会给结构禁止的转移分配概率。

若\(\mathcal K=2^Q\)，则：

\[
K^O=Q\setminus K,
\]

GLI退化为传统LI。因而完整幂集是传统逐题局部独立乘积成立的必要结构条件。

式(21)只直接适用于可逐题添加的learning space；更一般结构需要其他因子化。

## \(\Theta\)-SLM与LKS

式(21)作为潜在特质扩展称为\(\Theta\)-Simple Learning Model。它是顺序/步骤模型的模板。

另一条路线是对整个SRF做log-link重新参数化：

\[
\ell[\pi(K\mid\theta)]
=f(K,\theta)
=\sum_{L\subseteq K}\lambda_L(\theta),
\tag{23}
\]

其中单元素\(L\)给主效应，二元素\(L\)给二阶交互，以此类推。

只保留主效应\(\theta-b_i\)并归一化，得到：

\[
\pi(K\mid\theta)
=
\frac{\exp\left[\sum_{q_i\in K}(\theta-b_i)\right]}
{\sum_{L\in\mathcal K}\exp\left[\sum_{q_i\in L}(\theta-b_i)\right]}.
\tag{24}
\]

- 若\(\mathcal K=2^Q\)，它等价于局部独立Rasch题的联合分布；
- 若\(\mathcal K\)是阈值链，它成为PCM；
- 在KST中，这个SRF称为Logistic Knowledge Structure（LKS）。

## Table 2：专门针对局部依赖的分类

第二张表在Table 1基础上再加入“幂集还是任意结构”这一轴。

| 结构/过程 | 无\(p\)-过程 | 非因子化\(p\)-过程 | GLI因子化\(p\)-过程 |
| --- | --- | --- | --- |
| 概率性LD，\(\mathcal K=2^Q\)，无\(g\) | 完整列联表 | ULD、RD、OD、CD、log-linear、LND、Bahadur、copula | 强LI基线；多维IRF与随机效应testlet |
| 确定性LD，\(\mathcal K\subsetneq2^Q\)，无\(g\) | 不完整列联表 | 可把概率性SRF约束用于不完整表 | \(\Theta\)-SLM |
| 确定性LD，固定\(g\) | 基本概率KST | 一般KST-IRT、LKS、left-side-added模型 | 顺序型KST-IRT |
| 确定性LD，能力相关\(g\) | SLD与boundary mixture类混合 | 能力相关误差的LKS/一般KST-IRT | 能力相关误差的顺序KST-IRT |

表中的空白或无文献单元格不是逻辑上不可能，而是作者认为尚未被系统研究的模型家族。

