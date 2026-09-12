# EM 完整推导

## 缺失数据

把学生 \(i\) 属于属性模式 \(l\) 的指示变量记为

\[
Z_{il}
=
\mathbf 1(
\boldsymbol\alpha_i=\boldsymbol\alpha_l
).
\]

若 \(Z_{il}\) 已知，guess 和 slip 都是分组 Bernoulli 比例。EM 用

\[
w_{il}
=
E(Z_{il}\mid\boldsymbol X_i)
=
P(\boldsymbol\alpha_l\mid\boldsymbol X_i)
\]

替代未知指示变量。

## E 步

由 Bayes 公式：

\[
w_{il}
=
\frac{
\pi_l
L(\boldsymbol X_i\mid\boldsymbol\alpha_l)
}{
\sum_{h=1}^{L}
\pi_h
L(\boldsymbol X_i\mid\boldsymbol\alpha_h)
}.
\tag{7}
\]

对每个学生：

\[
\sum_{l=1}^{L}w_{il}=1.
\]

## 按理想状态聚合期望人数

对题目 \(j\) 和状态 \(z\in\{0,1\}\)，定义：

\[
I_j^{(z)}
=
\sum_{i=1}^{I}
\sum_{l:\eta_{lj}=z}
w_{il},
\tag{8}
\]

即理想状态为 \(z\) 的期望人数。

答对的期望人数为

\[
R_j^{(z)}
=
\sum_{i=1}^{I}
\sum_{l:\eta_{lj}=z}
w_{il}X_{ij}.
\tag{9}
\]

并且

\[
I_j^{(0)}+I_j^{(1)}=I.
\]

## M 步：更新 guessing

对 \(\eta=0\) 组，答对概率为 \(g_j\)。附录 Equation A10 给出：

\[
\widehat g_j
=
\frac{R_j^{(0)}}{I_j^{(0)}}.
\tag{10}
\]

它是“未掌握全部所需属性者中的期望答对比例”。

## M 步：更新 slipping

对 \(\eta=1\) 组，答错概率为 \(s_j\)。Equation A11 给出：

\[
\widehat s_j
=
\frac{
I_j^{(1)}-R_j^{(1)}
}{
I_j^{(1)}
}.
\tag{11}
\]

它是“掌握全部所需属性者中的期望答错比例”。

## 完整算法

1. 给定初始 \(g_j^{(0)},s_j^{(0)}\) 和固定模式先验 \(\pi_l\)。
2. 用当前参数计算全部 \(w_{il}\)。
3. 计算 \(I_j^{(0)},R_j^{(0)},I_j^{(1)},R_j^{(1)}\)。
4. 用式 (10)--(11) 更新全部题目参数。
5. 计算前后两轮参数的最大绝对差。
6. 未达到阈值则回到步骤 2。

论文模拟使用：

\[
\max_m
|\beta_m^{(t+1)}-\beta_m^{(t)}|
<0.0001
\]

作为收敛标准。

## 为什么 M 步有闭式解

E 步以后，每道题被拆成两个加权 Bernoulli 样本：

- \(\eta=0\) 组估计成功率 \(g_j\)；
- \(\eta=1\) 组估计失败率 \(s_j\)。

Bernoulli 极大似然就是加权成功次数除以加权总次数，因此无需数值优化器。

## 固定先验与经验 Bayes 扩展

论文的基础算法在每轮使用同一组 \(\pi_l\)。讨论部分建议更新：

\[
\widehat\pi_l
=
\frac{1}{I}
\sum_{i=1}^{I}
w_{il}.
\tag{12}
\]

这会把算法扩展为同时估计饱和属性模式比例。

本站脚本默认复现固定均匀先验；加上

```bash
--update-prior
```

才执行式 (12)，并将其标为论文讨论的扩展。

## 计算复杂度

每轮 E 步要对

\[
I\times 2^K\times J
\]

个学生—类别—题目组合计算概率，主要复杂度为

\[
O(IJ2^K).
\]

这解释了论文对较大 \(K\) 的担忧。M 步聚合期望计数也依赖同一后验矩阵，但代价通常低于 E 步的似然计算。

## 完整数据似然如何变成 M 步目标

为避免与题目 Q 矩阵混淆，把 EM 辅助目标写成 \(\mathcal Q\)。完整数据对数似然是

\[
\ell_c(\beta,\pi)=\sum_{i,l}Z_{il}\left[
\log\pi_l+\sum_j
\{X_{ij}\log P_j(l)+(1-X_{ij})\log(1-P_j(l))\}
\right].
\]

第 t 轮先用旧参数计算后验，再取条件期望：

\[
\mathcal Q(\beta,\pi\mid\beta^{(t)},\pi^{(t)})
=E_t[\ell_c\mid X].
\]

由于表达式对 \(Z_{il}\) 线性，只需将它换成 \(w_{il}^{(t)}\)。不是先给每个人选一个 MAP 画像再硬分组。

## 把求和整理成每题四个计数

按理想状态分组，题 j 对辅助目标的贡献为

\[
\begin{aligned}
\mathcal Q_j={}&R_j^{(0)}\log g_j
+(I_j^{(0)}-R_j^{(0)})\log(1-g_j)\\
&+R_j^{(1)}\log(1-s_j)
+(I_j^{(1)}-R_j^{(1)})\log s_j.
\end{aligned}
\]

计数全部来自旧后验，在本轮 M 步内固定。不同题目参数不出现在彼此的项中，故可逐题最大化。

## g 的求导与移项

\[
\frac{\partial\mathcal Q_j}{\partial g_j}
=\frac{R_j^{(0)}}{g_j}
-\frac{I_j^{(0)}-R_j^{(0)}}{1-g_j}=0.
\]

乘 \(g_j(1-g_j)\)：

\[
R_j^{(0)}(1-g_j)
-g_j(I_j^{(0)}-R_j^{(0)})=0.
\]

展开、抵消两个 \(g_jR_j^{(0)}\)，剩下

\[
R_j^{(0)}-g_jI_j^{(0)}=0,\qquad
g_j^{(t+1)}=R_j^{(0)}/I_j^{(0)}.
\]

## s 的负号在哪里

\[
\frac{\partial\mathcal Q_j}{\partial s_j}
=-\frac{R_j^{(1)}}{1-s_j}
+\frac{I_j^{(1)}-R_j^{(1)}}{s_j}=0.
\]

乘 \(s_j(1-s_j)\)，展开：

\[
-s_jR_j^{(1)}
+(1-s_j)(I_j^{(1)}-R_j^{(1)})=0,
\]

\[
I_j^{(1)}-R_j^{(1)}-s_jI_j^{(1)}=0.
\]

因此 slip 是高组的答错比例：

\[
s_j^{(t+1)}=1-R_j^{(1)}/I_j^{(1)}.
\]

例如 g 的二阶导为

\[
-\frac{R_j^{(0)}}{g_j^2}
-\frac{I_j^{(0)}-R_j^{(0)}}{(1-g_j)^2}\le0.
\]

有正组人数时目标凹；全对/全错可产生边界最大值。空组没有定义比例，不可直接除零。

## 为什么这里不再对后验求导

M 步优化的是旧参数后验下的辅助目标，所以 \(w^{(t)}\) 固定。若权重随候选新参数改变，就不是这个 M 步了。

直接求边际似然的得分也会出现后验，但它来自对 log-sum 的链式求导，见[标准误章](06-standard-errors-and-classification.md)。不能把一次比例更新误认为已经找到边际似然的全局最大值。

## 模式比例更新的拉格朗日推导

若选择估计先验，记 \(n_l=\sum_iw_{il}^{(t)}\)。最大化

\[
\sum_ln_l\log\pi_l+\lambda(\sum_l\pi_l-1).
\]

求导得 \(n_l/\pi_l+\lambda=0\)，即 \(\pi_l=-n_l/\lambda\)。因为 \(\sum_ln_l=I\)，归一化给出 \(\lambda=-I\)，故 \(\pi_l^{(t+1)}=n_l/I\)。

这是可选扩展；原文基础算法固定先验，不能暗中加入此步。

## 似然为何不下降，却不保证全局最优

对每名学生应用 Jensen：

\[
\log\sum_l w^t_{il}
\frac{\pi_lL_i(l;\beta)}{w^t_{il}}
\ge\sum_lw^t_{il}\log
\frac{\pi_lL_i(l;\beta)}{w^t_{il}}.
\]

取精确旧后验时，在旧参数处等号成立。M 步增大右侧，新观测对数似然便不小于旧值。这里要求 E/M 步使用一致的目标与约束。

但目标不一定全局凹，不同起点可能得到不同局部解；单调性不等于全局最优。

## 一轮的状态不要串用

\[
(g^t,s^t,\pi^t)\to W^t
\to\text{本轮计数}\to(g^{t+1},s^{t+1},\pi^{t+1})
\to W^{t+1}.
\]

各题共用同一份旧后验完成 M 步。停机后再跑一次 E 步，使输出后验与最终参数对应。

以上展开原文附录 A1；Jensen 说明和实现注意事项是本站教学补充。
