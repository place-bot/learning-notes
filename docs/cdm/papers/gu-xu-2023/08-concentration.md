# 08 一致集中与全局最优性的夹逼

## 为什么逐点收敛不够

估计的 \(\widehat Z\) 是看了数据后选出来的。只证明每个预先固定 Z 的误差小，不能自动保证被算法挑中的那个也小。因此需要

\[
U=\sup_{Z\in\mathcal Z}|L(Z)-\bar L(Z)|.
\]

## 第一项：有限取值加 union bound

固定 Z 时，组均值只可能是

\[
0,\frac1n,\ldots,\frac{n-1}{n},1.
\]

独立但概率可不同的 Bernoulli 和，利用矩母函数与 Jensen 不等式，可得相应的 Chernoff KL 尾界。对一个取值组合 \(\vartheta\)，其概率受

\[
\exp\{-\sum_{j,c}n_{jc}D(\vartheta_{jc}\|\bar\theta_{jc})\}
\]

控制。再把所有组合的概率相加。

两组模型中，每题组合数量至多

\[
(n_{j0}+1)(n_{j1}+1)\le(N/2+1)^2.
\]

所以固定结构下，

\[
P\left(\sum_{j,c}n_{jc}D(\widehat\theta_{jc}\|\bar\theta_{jc})>t\right)
\le (N/2+1)^{2J}e^{-t}.
\]

多参数时将两组替换为至多 \(2^{K_0}\) 组。

## 再对全部结构取并集

若候选结构数为 S，再乘 S，即指数多出 \(\log S\)。必须先说清枚举的是什么：

- Q 已固定，只枚举 A：\(S\le2^{NK}\)；
- A、Q 均未知，粗略上界：\(S\le2^{K(N+J)}\)。

有支持约束时可进一步收紧 Q 的计数。底本若将联合未知结构直接计成 \(2^{NK}\)，需要额外论证；本章不把缺少的说明略去后宣称独立证明了原速率。

## 第二项：Bernstein 控制加权中心化和

设

\[
X_{ij}=(r_{ij}-P^0_{ij})
\log\frac{\bar\theta_{j,z_{ij}}}{1-\bar\theta_{j,z_{ij}}}.
\]

固定 Z 时，\(E[X_{ij}]=0\)。概率边界给出权重绝对值 \(O(\log J)\)，且

\[
\sum_{i,j}\mathrm{Var}(X_{ij})
\le C\,MNJ(\log J)^2.
\]

Bernstein 不等式给出“方差项 + 最大单项项”控制的指数尾界，再对 S 个候选结构取 union bound。这是 \(\sqrt{M K/J}\) 与对数因子的来源，而不是从维度数直接猜出的速率。

## 最优性夹逼：最关键的三行

若 \(\widehat Z\) 是全局最大值，则 \(L(\widehat Z)\ge L(Z^0)\)。于是

\[
\begin{aligned}
\bar L(Z^0)-\bar L(\widehat Z)
={}&[\bar L(Z^0)-L(Z^0)]\\
&+[L(Z^0)-L(\widehat Z)]\\
&+[L(\widehat Z)-\bar L(\widehat Z)]\\
\le{}&2U.
\end{aligned}
\]

结合上章 KL 恒等式和 Pinsker 不等式 \(D(p\|q)\ge2(p-q)^2\)，得到

\[
\frac1{NJ}\sum_{i,j}(P^0_{ij}-\bar P^{\widehat Z}_{ij})^2
\le \frac{U}{NJ}.
\]

## 如果只是近似最大化

若 \(L(\widetilde Z)\ge L(Z^0)-r_{NJ}\)，同样推导只多出优化误差：

\[
\bar L(Z^0)-\bar L(\widetilde Z)\le2U+r_{NJ}.
\]

这是本站由相同代数得到的扩展，不是论文为 ADG-EM 给出的收敛保证。若不知道 \(r_{NJ}\) 多大，就不能将全局 MLE 定理直接贴到某次运行结果上。

来源：[Supplement Steps 1–4、Lemmas 1–2、5–7，v3 pp.42–46、69–75](https://arxiv.org/pdf/2009.04096v3#page=42)。
