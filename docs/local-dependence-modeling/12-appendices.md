# 附录：SLD、Huynh扩展与阈值失序

## Appendix A：SLD与Ackerman-Spray方法

令\(P^*(X_i=x_i\mid\theta)\)表示存在LD时的概率，\(P(X_i=x_i\mid\theta)\)表示LI概率。
定义两种转移：

\[
\alpha^*_{ii'}
=P^*(X_{i'}=1\mid X_i=0,\theta),
\]

\[
\beta^*_{ii'}
=P^*(X_{i'}=0\mid X_i=1,\theta).
\]

Ackerman与Spray设：

\[
\alpha^*_{ii'}=\alpha P(X_{i'}=1\mid\theta),
\qquad
\beta^*_{ii'}=\beta P(X_{i'}=0\mid\theta).
\]

由全概率公式：

\[
\begin{aligned}
P^*(X_{i'}=1\mid\theta)
&=\alpha^*_{ii'}P^*(X_i=0\mid\theta)\\
&\quad+(1-\beta^*_{ii'})P^*(X_i=1\mid\theta).
\end{aligned}
\tag{A.1}
\]

- \(\alpha=\beta=1\)：第二题使用自己的LI概率；
- \(\alpha=\beta=0\)：第二题完全等于第一题。

对称地令：

\[
\pi_{LD}=1-\alpha=1-\beta,
\]

整理得：

\[
P^*(X_{i'}=1\mid\theta)
=(1-\pi_{LD})P(X_{i'}=1\mid\theta)
+\pi_{LD}P^*(X_i=1\mid\theta),
\]

正是正文SLD复制模型。

## Appendix B：Huynh结果的扩展

设有\(J\)个局部独立Rasch二元题，总分：

\[
R=\sum_{i=1}^{J}X_i.
\]

给定能力的总分概率为：

\[
P(R=r\mid\theta)
=
\frac{e^{r\theta}S_r}
{\sum_{r'=0}^{J}e^{r'\theta}S_{r'}},
\tag{B.1}
\]

其中第\(r\)个基本对称函数：

\[
S_r
=
\sum_{\substack{\boldsymbol x\in\{0,1\}^J\\|\boldsymbol x|=r}}
e^{-\sum_i x_ib_i},
\qquad S_0=1.
\tag{B.2}
\]

若它能写成PCM，需要：

\[
S_r=e^{-\sum_{k=1}^{r}\delta_k},
\]

所以步难度：

\[
\delta_r=\log\frac{S_{r-1}}{S_r}.
\]

相邻步难度差为：

\[
\Delta\delta_{r+1}
=\delta_{r+1}-\delta_r
=\log\frac{S_r^2}{S_{r-1}S_{r+1}}.
\]

对两题：

\[
S_1=e^{-b_1}+e^{-b_2},
\qquad
S_2=e^{-b_1-b_2}.
\]

因此：

\[
\Delta\delta_2
=
\log\frac{(e^{-b_1}+e^{-b_2})^2}{e^{-b_1-b_2}}
\ge\log4,
\tag{B.3}
\]

不等式来自算术平均不小于几何平均，等号在\(b_1=b_2\)时成立。

### Huynh原结论的正确范围

若：

\[
\Delta\delta_2<\log4,
\]

则不可能由两道局部独立Rasch题产生，因而提示正局部依赖。

但：

\[
\Delta\delta_2\ge\log4
\]

只说明与某个LI分解相容，不证明数据生成机制为LI。

### 推广到LD

作者用\(u=p,d\)分别表示概率性与确定性LD，定义广义状态和：

\[
S_r^u
=
\sum_{\substack{K\in\mathcal K\\|K|=r}}
e^{f(K,\theta,\Gamma)-r\theta}.
\tag{B.5}
\]

依赖参数或受限结构会改变\(S_r^u\)。因此LD模型也可以产生“分得足够开”的步难度。

结论是：

\[
\text{步难度过近或反转}\Rightarrow\text{LD信号},
\]

但：

\[
\text{步难度足够分离}\not\Rightarrow\text{LI证据}.
\]

## Appendix C：disordered threshold controversy

争议来自PCM中估计步难度没有按照类别顺序递增，例如：

\[
\delta_2<\delta_1.
\]

### 幂集中的情况

若多个二元Rasch题独立且难度充分分离，PCM步难度近似按项目难度排序：

\[
\delta_1\approx\min_i b_i,
\qquad
\delta_J\approx\max_i b_i.
\]

### 链中的情况

链只规定先决顺序：

\[
q_1\prec q_2.
\]

它不要求：

\[
b_1<b_2.
\]

如果第一步很难，但掌握第一步后第二步很容易，完全可能：

\[
b_2<b_1
\quad\Longrightarrow\quad
\delta_2<\delta_1.
\]

这意味着中间类别人数可能很少：一旦跨过第一阈值，很快也跨过第二阈值。

### 作者的立场

阈值失序可能提示：

- 中间类别定义不清；
- 类别利用不足；
- 评分规则或样本构成需要检查。

但它不是PCM形式上无法定义的证据。逻辑次序与难度数值是两个不同对象；仅凭阈值反转不能宣布模型数学非法。

