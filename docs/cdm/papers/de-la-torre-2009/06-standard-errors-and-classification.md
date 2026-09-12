# 标准误与分类

## 附录的目标

参数点估计为

\[
\widehat{\boldsymbol\beta}
=
(\widehat g_1,\widehat s_1,\ldots,\widehat g_J,\widehat s_J)^\mathsf T.
\]

论文用边际似然得分外积构造信息矩阵近似，再近似协方差；它不是有限样本下严格负 Hessian 的恒等表达：

\[
\widehat{\operatorname{Cov}}
(\widehat{\boldsymbol\beta})
\approx
\mathcal I(\widehat{\boldsymbol\beta})^{-1}.
\tag{13}
\]

标准误是逆矩阵对角元素的平方根。

## 把属性后验压到题目理想状态

定义

\[
p_j(z\mid\boldsymbol X_i)
=
\sum_{l:\eta_{lj}=z}
P(\boldsymbol\alpha_l\mid\boldsymbol X_i).
\tag{14}
\]

它表示给定学生完整反应向量后，该生在题 \(j\) 上处于理想状态 \(z\) 的后验概率。

## 单个学生对参数的期望得分

令

\[
P_j(0)=g_j,
\qquad
P_j(1)=1-s_j.
\]

对于 \(\beta_{j0}=g_j\)：

\[
u_{i,j0}
=
p_j(0\mid\boldsymbol X_i)
\frac{
X_{ij}-g_j
}{
g_j(1-g_j)
}.
\tag{15}
\]

对于 \(\beta_{j1}=s_j\)，因为

\[
\frac{\partial(1-s_j)}{\partial s_j}=-1,
\]

得：

\[
u_{i,j1}
=
p_j(1\mid\boldsymbol X_i)
\frac{
(1-s_j)-X_{ij}
}{
(1-s_j)s_j
}.
\tag{16}
\]

## Equation A15

把所有 \(2J\) 个参数得分排成向量 \(\boldsymbol u_i\)。论文的 A15 可以写成：

\[
\mathcal I(\widehat{\boldsymbol\beta})
\approx
\sum_{i=1}^{I}
\boldsymbol u_i\boldsymbol u_i^\mathsf T
\bigg|_{\boldsymbol\beta=\widehat{\boldsymbol\beta}}.
\tag{17}
\]

这会产生一个

\[
2J\times2J
\]

信息矩阵，包含不同题目参数的交叉信息项；求逆后才得到协方差近似。

## 为什么不能只用两个二项分布公式

若每人的 \(\eta_{ij}\) 已知，可近似写

\[
\operatorname{SE}(\widehat g_j)
\approx
\sqrt{
\frac{g_j(1-g_j)}{I_j^{(0)}}
}.
\]

在 DINA 中，\(\eta_{ij}\) 是后验不确定的，并且同一属性模式同时影响多道题。A15 通过完整后验和交叉乘积保留这部分依赖。

## 模拟中怎样验证标准误

100 次重复中，论文比较：

- 每次拟合得到的模型标准误，再取平均；
- 100 个参数估计的经验标准差。

两者非常接近。论文报告模型标准误平均约比经验标准差保守 2%。

## 边界估计

真实数据 Item 1 的 DINA 结果为

\[
\widehat g_1=0.00,
\qquad
\operatorname{SE}(\widehat g_1)=0.050.
\]

当参数接近 0 或 1 时：

- 正态近似可能不对称；
- 信息矩阵可能病态；
- 不同先验或约束会显著影响结果；
- Wald 区间可能越出 \([0,1]\)。

Table 4 中 HO-DINA 对同一 \(g_1\) 给出标准误 0.004，显示潜变量分布和贝叶斯估计会改变边界附近的不确定性。

## 属性模式分类

EM 已经产生

\[
w_{il}
=
P(\boldsymbol\alpha_l\mid\boldsymbol X_i).
\]

可据此定义：

### MAP 模式分类

\[
\widehat l_i^{\text{MAP}}
=
\arg\max_l w_{il}.
\]

### 单属性 EAP

\[
\widehat P(\alpha_{ik}=1\mid\boldsymbol X_i)
=
\sum_{l:\alpha_{lk}=1}
w_{il}.
\]

本文主要研究项目参数校准。讨论部分明确把模式可识别性、分类方法、测验长度和 Q 矩阵规格列为需要系统研究的后续问题。

## 从边际似然逐步求出学生得分

固定先验，令 \(m_i(\beta)=\sum_l\pi_lL_i(l;\beta)\)。链式求导：

\[
\frac{\partial\log m_i}{\partial\beta_r}
=\frac1{m_i}\sum_l\pi_l\frac{\partial L_i(l)}{\partial\beta_r}
=\sum_l\frac{\pi_lL_i(l)}{m_i}
\frac{\partial\log L_i(l)}{\partial\beta_r}.
\]

系数恰好是 \(w_{il}\)。对 g 只有理想状态0的类贡献；对 s 只有状态1的类贡献，且 \(\log(1-s)\) 产生负号。这分别给出式(15)、(16)。

## 数字示例：一个学生贡献什么

用[完整手算](11-worked-example.md)第一名学生及初始参数：

\[
u_{i,g_1}
=(1-.866017052)\frac{1-.2}{.2(1-.2)}
=.669914738,
\]

\[
u_{i,s_1}
=.866017052\frac{.9-1}{.9(.1)}
=-.962241169.
\]

依次排列 \(g_1,s_1,g_2,s_2,g_3,s_3\)：

\[
u_i\approx(.669915,-.962241,-.669915,
1.985384,2.509135,-.438490).
\]

该生外积的(1,1)项是 \(.669915^2\)，(1,2)项是 \(.669915\times(-.962241)\)。各学生的外积逐项相加；不是先加得分再做一个外积。

此处演示初始参数处的运算；正式标准误须在最终拟合参数和对应后验处计算。

## OPG、负 Hessian 与期望信息不是同一个对象

严格观测信息为

\[
H_{\mathrm{obs}}=-\partial^2\ell/\partial\beta\partial\beta^\mathsf T,
\]

得分外积近似为

\[
I_{\mathrm{OPG}}=\sum_i u_i u_i^\mathsf T.
\]

有限样本下通常不相等。在正确设定和正则条件下，取期望后的信息恒等式连接二者。原文 A12–A15 利用期望关系，再代入观测反应作近似，不是证明每份数据的 Hessian 都等于负得分外积。

## 先求整个矩阵的逆，再取对角线

只用下面矩阵演示线性代数，不作为本文数据结果：

\[
I=\begin{pmatrix}4&1\\1&9\end{pmatrix},\qquad
I^{-1}=\frac1{35}\begin{pmatrix}9&-1\\-1&4\end{pmatrix}.
\]

标准误是 \(\sqrt{9/35}\)、\(\sqrt{4/35}\)，不是 \(1/\sqrt4\)、\(1/\sqrt9\)。非对角项会影响逆矩阵的对角项。

四学生三题例子有6个题目参数，OPG 由4个得分外积组成，秩最多4，必然奇异。因此不为该例编造6个标准误；加 ridge 求出数值也不等于获得可靠推断。

若先验比例也估计，参数向量还含 \(L-1\) 个比例参数，需要相应完整信息矩阵或其他适当方法。现有脚本只对 g、s 做 A15 计算，不能将开启先验更新后的该结果称作已计入所有干扰参数不确定性。

## MAP 与逐属性阈值判定可能不一致

按00、01、10、11排列的后验若为

\[
(.35,.25,.10,.30),
\]

MAP 是00；但边际掌握概率为 .40、.55，逐属性按 .5 阈值判定得到01。

二者对应不同损失：整行是否正确，与逐位是否正确。并列最大值还需明确规则。后验均值处于 [0,1] 也不代表模型把真实属性改成连续变量。
