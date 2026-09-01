# 概率性LD（二）：OD、CD、Bahadur与copula

## Divide-by-total联合模型

OD与CD不把联合概率分解成“第一题概率乘第二题条件概率”，而是直接给四种反应模式打分：

\[
P(X_i=x_i,X_{i'}=x_{i'}\mid\theta,\Gamma)
=
\frac{e^{f(\boldsymbol x,\theta,\Gamma)}}
{\sum_{\boldsymbol y\in\{0,1\}^2}e^{f(\boldsymbol y,\theta,\Gamma)}}.
\tag{27}
\]

这就是divide-by-total或softmax：分子是当前模式权重，分母是全部模式权重总和。

## OD：Order Dependence

OD是非对称的顺序依赖。文章使用的kernel可写为：

\[
f_{OD}(\boldsymbol x,\theta)
=x_i(a\theta-b_i)+x_{i'}(a\theta-b_{i'})
-x_i(-1)^{1-x_{i'}}b_{ii'}.
\tag{28a}
\]

交互项对\(10\)与\(11\)的影响不同，因此可压低\(01\)等违背先决顺序的模式。OD与RD都能逼近Table A，但：

- RD是条件概率链；
- OD是联合模式的softmax重新参数化。

相似列联表不代表相同生成过程。

## CD：Combination Dependence

CD采用对称交互：

\[
f_{CD}(\boldsymbol x,\theta)
=x_i(a\theta-b_i)+x_{i'}(a\theta-b_{i'})
-x_ix_{i'}b_{ii'}.
\tag{28b}
\]

\(x_ix_{i'}\)只在\(11\)时等于1，因此\(b_{ii'}\)直接改变共同成功模式的权重，并通过分母连带改变全部格概率。

OD与CD都可以让交互参数依赖能力，例如把\(b_{ii'}\)换成\(b_{ii'}-a\theta\)。这样依赖强度本身随能力变化。

## 对数优势、logit与log-linear

赔率是：

\[
\operatorname{odds}(p)=\frac{p}{1-p}.
\]

logit是赔率的对数：

\[
\operatorname{logit}(p)
=\log\frac{p}{1-p}.
\]

它把\((0,1)\)映射到整个实数轴。对数线性模型则对列联表格概率或频数取log：

\[
\log p_{x_1x_2}
=
\lambda_0+lambda_1x_1+lambda_2x_2+lambda_{12}x_1x_2.
\]

\(\lambda_{12}=0\)对应独立；非零交互刻画联合格超出边缘主效应的程度。

## 一般局部依赖潜在特质模型

Ip（2002）把二题模型推广到任意题数：

\[
\begin{aligned}
\log P(\boldsymbol X=\boldsymbol x\mid\theta,\Gamma)
&=\sum_i x_i\omega_i(\theta)
+\sum_{i<j}x_ix_j\omega_{ij}(\theta)\\
&\quad+\cdots+
\left(\prod_i x_i\right)\omega_{1\cdots J}(\theta)
-k\omega(\theta).
\end{aligned}
\tag{29}
\]

其中：

- \(\omega_i(\theta)\)：单题主效应；
- \(\omega_{ij}(\theta)\)：二阶题间交互；
- 更高阶项：三题及以上不能由低阶交互解释的联合效应；
- \(\omega(\theta)\)：归一化项。

把二阶以上交互全部设为0就回到LI。

## 边缘可再现性

加入依赖后，希望仍保持原单题IRF：

\[
\sum_{\boldsymbol x_{-i}}
P(\boldsymbol X=\boldsymbol x\mid\theta)
=P(X_i=x_i\mid\theta).
\]

若成立，称边缘可再现（reproducible）。

- OD和CD通常不可再现：加入联合交互后，边缘IRF也改变；
- 某些模型半可再现：把主效应保留为LI模型形式，但交互仍影响最终边缘；
- Bahadur和copula的重要目标之一是明确保留边缘。

这决定项目难度和区分度是否还能按普通IRT解释。

## LND：局部非负依赖

若只要求正关联，可以把LI等式放宽为不等式：

\[
P(11\mid\theta)
\ge
P(X_i=1\mid\theta)P(X_{i'}=1\mid\theta),
\]

\[
P(00\mid\theta)
\ge
P(X_i=0\mid\theta)P(X_{i'}=0\mid\theta),
\]

\[
P(10\mid\theta)
\le
P(X_i=1\mid\theta)P(X_{i'}=0\mid\theta).
\tag{30}
\]

这些约束等价于条件协方差非负。LND并不指定唯一模型，只给SRF划定允许区域。

## Bahadur表示怎样得到

令：

\[
p_i(\theta)=P(X_i=1\mid\theta),
\]

并把二分反应标准化：

\[
Z_i(\theta)
=
\frac{X_i-p_i(\theta)}
{\sqrt{p_i(\theta)[1-p_i(\theta)]}}.
\]

则两题联合分布可写为：

\[
P(X_i,X_{i'}\mid\theta)
=
P(X_i\mid\theta)P(X_{i'}\mid\theta)
\left[1+\rho_{ii'}(\theta)Z_i(\theta)Z_{i'}(\theta)\right].
\tag{31}
\]

当\(\rho_{ii'}(\theta)=0\)时回到LI。标准化项的选择保证把其他变量求和后，额外交互项抵消，因而保留原边缘IRF。

高维推广继续加入：

\[
\rho_I(\theta)\prod_{i\in I}Z_i.
\]

把所有阶相关项设为0得到强LI；只把二阶项设为0得到弱LI；若二阶相关在能力分布上的期望为0，则得到WLIE。

## Copula怎样构造联合分布

设潜在连续反应：

\[
X_i^*=\theta-b_i+\varepsilon_i,
\qquad
X_i=1\Longleftrightarrow X_i^*>0.
\]

于是：

\[
P(X_i=0\mid\theta)
=F_{\varepsilon_i}(b_i-\theta).
\]

用copula \(C:[0,1]^2\to[0,1]\)连接两个边缘CDF：

\[
P(00\mid\theta)
=C\left(F_i(b_i-\theta),F_{i'}(b_{i'}-\theta)\right).
\tag{32a}
\]

其他三格由边缘减法得到：

\[
P(10)=F_{i'}-C,
\qquad
P(01)=F_i-C,
\]

\[
P(11)=1-F_i-F_{i'}+C.
\tag{32b}
\]

因为构造从既定边缘出发，边缘IRF自然可再现。

当copula达到Fréchet-Hoeffding正依赖上界：

\[
C(u,v)=\min(u,v),
\]

某些格概率成为0：若难度不同得到Table A，难度相同得到Table B。此时模型碰到概率空间边界，
按照本文分类转化为确定性LD。

