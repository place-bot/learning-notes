# 06 Theorem 1：究竟哪一种一致性

## 速率项

定义平均真阳性反应概率

\[
M=\frac1{NJ}\sum_{i,j}P^0_{ij},\qquad
\gamma_J=\frac{(\log J)^{1+\varepsilon}}{\sqrt J}
\sqrt{M\log(2^K)}.
\]

这里 M 不是题目数。由于 \(\log(2^K)=K\log2\)，复杂度通过 K 进入此表达。

主文给出的增长条件包括

\[
\sqrt J=O(\sqrt M\,N^{1-c}),\qquad
K=o(MJ\log J),\quad 0<c<1.
\]

还必须结合上章假设，并使下面误差界右侧趋零。补充材料部分增长条件写法不同，见[核对记录](19-source-audit.md)。

## Part (b)：Q 行与学生画像的错误比例

在一个共同属性置换下：

\[
\frac1J\sum_j1(\widehat q_j\ne q_j^0)
=o_P\left(\frac{\gamma_J}{\beta_Jp_N}\right),
\]

\[
\frac1N\sum_i1(\widehat a_i\ne a_i^0)
=o_P\left(\frac{\gamma_J}{\beta_J\delta_J}\right).
\]

指标是整行是否完全正确。例如 10 属性画像错一位，整行就记一个错误；不是只罚 \(1/10\)。

若右侧趋零，结论是错误行比例趋零。并不直接说明

\[
P(\widehat A=A^0,\widehat Q=Q^0)\to1.
\]

例如每次始终错一名学生，错误比例为 \(1/N\to0\)，但全矩阵精确恢复概率为零。

## Part (a)：必须分清概率对象

主文写出的量是

\[
\frac1{NJ}\sum_{i,j}
\{p_{ij}(Q^0,A^0,\Theta^0)
-p_{ij}(\widehat Q,\widehat A,\Theta^0)\}^2
=o_P(\gamma_J/\beta_J).
\]

它保留 \(\Theta^0\)，并不是任意程序输出 \(\widehat\Theta\) 后的预测风险。

补充证明首先控制的却是：在估计结构分组中，按真概率求组均值得到的 oracle 投影 \(\bar P^{\widehat Z}\)。此对象与上式不应直接画等号。后续章节用明确的 \(\bar P\) 记号展开可以独立验证的证明部分；核对章保留二者衔接的疑点。

## 概率小量符号怎么读

\(X_n=o_P(r_n)\) 意味着：对任意固定 \(\epsilon>0\)，

\[
P(|X_n|>\epsilon r_n)\to0.
\]

不是每次有限样本实验都小于 \(r_n\)，也不自带一个明确可用的置信界常数。

## 定理没有保证什么

- 任意初始化的 ADG-EM 都找到此全局估计量；
- 固定 J、仅 N 增长仍恢复每个学生；
- 全部 G-DINA 参数点均满足分离条件；
- binary-Q 定理直接适用于 continuous-Q；
- 表中的有限样本“完全恢复”比例就是定理陈述。

来源：[Theorem 1、Remarks 3–4，v3 pp.14–16](https://arxiv.org/pdf/2009.04096v3#page=14)。
