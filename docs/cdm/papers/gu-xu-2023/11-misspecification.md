# 11 Theorems 2–3：模型简化后为什么还可能恢复结构

## 概率错了，不等于所有结构都错了

真模型可能让 00、10、01、11 有四种概率，但我们先用 DINA 只分高低两组。低组内差异会被压成一个均值，因此一般不能恢复全部真概率。

作者问的是：即使这种概率表达不准确，能否仍正确找出 A，以及部分或全部 Q？

## 最好的两组近似

对候选结构 \(Z=(Q,A)\)，先按 DINA 分组，再在每组对真概率求均值：

\[
P^{2,Z}_{ij}
=\frac{\sum_{m:\xi_{mj}(Z)=\xi_{ij}(Z)}P^0_{mj}}
{\#\{m:\xi_{mj}(Z)=\xi_{ij}(Z)\}}.
\]

定义逐题近似损失

\[
f_j(Z)=\sum_iD(P^0_{ij}\|P^{2,Z}_{ij}).
\]

这不是用观测反应做 BIC，而是理论上衡量两组近似的总体 KL 损失。

## Theorem 2：先保住单属性骨架

记 \(E_0=\{j:q_j^0=e_k\text{ for some }k\}\)。单属性题天然只有两种局部画像，不会因两参数简化而丢掉额外局部组。

Assumption 4 要求这些题有信号 \(\zeta_J\)，并要求真实结构在非单属性题上的近似损失接近可达到的最优值：

\[
\sum_{j\notin E_0}f_j(Z^0)
=\min_Z\sum_{j\notin E_0}f_j(Z)+o(NJ\eta_J).
\]

结论是共同置换下

\[
\frac1J\sum_{j\in E_0}1(\widehat q_j\ne q_j^0)
=o_P\left(\frac{\gamma_J\vee\eta_J}{\zeta_Jp_N}\right),
\]

\[
\frac1N\sum_i1(\widehat a_i\ne a_i^0)
=o_P\left(\frac{\gamma_J\vee\eta_J}{\zeta_J\delta_J}\right).
\]

这里 Q 的和只限于 \(E_0\)，但分母仍是 J。它不保证全部多属性题 Q 正确，这正是后续回归阶段存在的理由。

## 把证明中的关键不等式展开

设 \(G(Z)=\sum_{j\notin E_0}f_j(Z)\)，
\(H(Z)=\sum_{j\in E_0}f_j(Z)\)。真结构有 \(H(Z^0)=0\)。总体两参数似然差为

\[
\bar L_2(Z^0)-\bar L_2(\widehat Z)
=H(\widehat Z)+G(\widehat Z)-G(Z^0).
\]

全局最优性与集中给出左侧上界 \(2U\)。Assumption 4 给出

\[
G(Z^0)-G(\widehat Z)
\le G(Z^0)-\min_ZG(Z)=o(NJ\eta_J).
\]

因此

\[
H(\widehat Z)\le2U+o(NJ\eta_J).
\]

这是**单边上界**，不是说任何候选 Z 的非单属性损失都与真结构相等。然后对单属性题复用结构锚定证明。

## Theorem 3：更强信号可以保住全部 Q

Assumption 5 进一步要求：

- 完全掌握要求与未完全掌握的概率有平方间隔 \(\Delta_J\)；
- 真结构下两参数近似的总偏差足够小：
  \(\sum_{j\notin E_0}f_j(Z^0)=o(NJ\eta'_J)\)。

此时

\[
\sum_j f_j(\widehat Z)
\le 2U+\sum_jf_j(Z^0)
=o_P\{NJ(\gamma_J\vee\eta'_J)\}.
\]

再用分离和覆盖将总 KL 转成全部 Q、A 的错误比例，速率分母分别是 \(\Delta_Jp_N\) 与 \(\Delta_J\delta_J\)。

## 一个直觉例子

若 00、10、01 的概率是 .20、.21、.22，而 11 是 .80，将前三类压成一组损失不大，却仍清楚分出“全部掌握”。若前三类是 .10、.45、.75，而 11 是 .80，分组可能更偏向某一个属性，真实 AND 支持不再当然最佳。

补充材料用“高组与低组的间隔 / 低组内部差异”说明这种机制。它是结构性要求，不是“错设越简单越好”的一般定理；其中玩具例子的所有候选分组论证还需明确限制，见核对章。

来源：[§4.2 Theorems 2–3、Supplement S.2.3–S.2.4](https://arxiv.org/pdf/2009.04096v3#page=19)。
