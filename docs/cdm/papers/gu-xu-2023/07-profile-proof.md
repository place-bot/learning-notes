# 07 剖面似然证明：把每一个等号写出来

本章是对补充证明的重新组织。为避免混淆，明确区分经验最大值与总体最大值。

## 1. 固定一个候选分组

Z 由候选 A、Q 及模型规则生成。题 j 的组 c 有 \(n_{jc}\) 人。定义

\[
\widehat\theta_{jc}=\frac1{n_{jc}}\sum_{i:z_{ij}=c}r_{ij},\qquad
\bar\theta_{jc}=\frac1{n_{jc}}\sum_{i:z_{ij}=c}P^0_{ij}.
\]

前者随机、可计算；后者由未知真概率构成，只用于证明。空组贡献约定为零。

## 2. 总体最优组参数为什么是均值

把某一组的期望对数似然写成

\[
\sum_{i:z_{ij}=c}
[P^0_{ij}\log\theta+(1-P^0_{ij})\log(1-\theta)].
\]

和第三章求导完全相同，只需把总答对数替换为 \(\sum_iP^0_{ij}\)，故最优值是 \(\bar\theta_{jc}\)。

这里使用自由组参数；如另加跨组顺序约束，闭式结果需要满足该约束，或使用相应松弛上界，不能跳过。

## 3. 定义两种最大值

\[
L(Z)=\sup_\Theta\ell(R;Z,\Theta),\qquad
\bar L(Z)=\sup_\Theta E_0[\ell(R;Z,\Theta)].
\]

一般而言，\(\bar L(Z)\ne E_0[L(Z)]\)：期望与最大化不能交换。原补充材料对此记号略简写，这里不沿用。

## 4. 加减一个中间量

经验组贡献为

\[
n[\widehat\theta\log\widehat\theta+
(1-\widehat\theta)\log(1-\widehat\theta)].
\]

总体组贡献为同样表达，但以 \(\bar\theta\) 替代。加减

\[
n[\widehat\theta\log\bar\theta+
(1-\widehat\theta)\log(1-\bar\theta)]
\]

后，第一块成为

\[
nD(\widehat\theta\|\bar\theta),
\]

第二块成为

\[
n(\widehat\theta-\bar\theta)
\log\frac{\bar\theta}{1-\bar\theta}.
\]

由于 \(n(\widehat\theta-\bar\theta)=\sum_{i:z_{ij}=c}(r_{ij}-P^0_{ij})\)，加总得

\[
\boxed{
L(Z)-\bar L(Z)=
\sum_{j,c}n_{jc}D(\widehat\theta_{jc}\|\bar\theta_{jc})
+\sum_{i,j}(r_{ij}-P^0_{ij})
\log\frac{\bar\theta_{j,z_{ij}}}{1-\bar\theta_{j,z_{ij}}}.
}
\]

## 5. 两项各代表什么

第一项非负，代表用数据估计组参数所获得的额外经验拟合收益。第二项是中心化随机和，可能正也可能负。

这也能看出为何左侧不是 \(L-E[L]\)：固定 Z 时取期望，第二项为零，第一项通常仍为正。

## 6. 总体损失恰好是 KL

若真模型在候选族中，真结构的总体最优概率就是 \(P^0_{ij}\)。因此

\[
\bar L(Z^0)-\bar L(Z)
=\sum_{i,j}D(P^0_{ij}\|\bar\theta_{j,z_{ij}}).
\]

因为 Bernoulli KL

\[
D(p\|q)=p\log(p/q)+(1-p)\log\{(1-p)/(1-q)\},
\]

正好等于两个期望对数似然之差。这里不需要近似或 Taylor 展开。

下一章处理随机误差，之后再解释如何由 KL 推出结构恢复。

来源：[Supplement S.2.1、Lemma 1 的证明，v3 pp.42–46、68–69](https://arxiv.org/pdf/2009.04096v3#page=42)。
