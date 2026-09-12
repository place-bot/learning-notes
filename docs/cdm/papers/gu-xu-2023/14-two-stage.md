# 14 两阶段估计：先画像，再逐题回归

## 为什么第一阶段不直接拟合最复杂模型

一般多参数模型既要找支持，又要估计主效应与许多交互项。作者利用 Theorem 2 的思想：先用较简单的两参数模型学习 A，再把估计画像作为协变量，逐题拟合更丰富的模型。

流程为

\[
R\ \longrightarrow\ \widehat A^{(1)}
\ \longrightarrow\ \text{逐题筛选与回归}
\ \longrightarrow\ \widehat Q^{(2)}.
\]

第二阶段主要修正多属性题的 Q，不应说成论文给出了与第一阶段完全同样的联合全局最大化。

## 固定 A 后，问题像普通回归

构造主效应 \(a_{ik}\) 与交互特征

\[
x_{i,T}=\prod_{k\in T}\widehat a_{ik}.
\]

以 logistic working model 为例：

\[
p_{ij}=\sigma\left(\mu_{j,0}
+\sum_{\varnothing\ne T}\mu_{j,T}x_{i,T}\right).
\]

若含属性 k 的某个保留项系数非零，便认为题 j 与属性 k 有联系。

## 为什么还要边际筛选

所有非空子集有 \(2^K-1\) 个，直接展开仍贵。作者先对每个属性做单变量 logistic 回归，按边际系数绝对值排序，用相邻差距定位候选属性集合，再在该集合内生成交互项。

下一步用 L1 正则化 logistic 回归，惩罚强度通过五折交叉验证选择。应区分筛选阈值、模型惩罚和全局理论约束 \(B_j\)。

## 目标函数的方向

最大化

\[
\sum_i[r_{ij}x_i^\top\mu-\log(1+e^{x_i^\top\mu})]
-\lambda\sum_{T\ne\varnothing}|\mu_T|
\]

等价于最小化负对数似然加惩罚。底本边际回归显示式将 log-likelihood 与 arg min 搭配，按公式含义应更正方向；不要在代码里最小化对数似然本身。

## 这种方法不是没有条件的筛选保证

边际相关小，不代表属性在交互中无用。例如均衡独立二值属性下，XOR 型响应可以与每一个单属性边际不相关，但联合关系很强。

这不是说作者教育模型就是 XOR，而是说明“先边际筛选”需要信号结构支持，不能凭复杂度优势就保证所有模型都筛选正确。

同样，\(\widehat A\) 是估计协变量，不是真实无误的设计矩阵；第一阶段分类质量会影响第二阶段。

## 与 conditional BIC 的区别

本文此处是“边际筛选 + 正则化回归”的两阶段法，不是 Continuous-Q DINA 项目中的 itemwise conditional BIC support refit。本文 TIMSS 的 BIC 用来比较两参数与多参数拟合，不能据此把两个项目的 Stage 2 当成同一个实现。

来源：[§4.2，v3 pp.19–24](https://arxiv.org/pdf/2009.04096v3#page=19)。
