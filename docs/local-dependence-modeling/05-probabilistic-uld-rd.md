# 概率性LD（一）：ULD、testlet与RD

概率性LD使用完整幂集：

\[
\mathcal K=2^Q.
\]

所有反应模式原则上都允许，局部依赖完全由SRF的函数形式产生。大多数传统IRT局部依赖模型位于Table 2的这一行，通常只有\(p\)-过程而没有\(g\)-过程：

\[
P(\boldsymbol X\mid\theta)=\pi(K\mid\theta).
\]

## ULD与trait dependence

ULD来自遗漏共同构念。作者把潜在变量从单个\(\theta\)扩展为多维向量：

\[
\Theta=(\theta,u_1,u_2,\ldots).
\]

于是：

\[
P(\boldsymbol X\mid\Theta)=\pi(K\mid\Theta).
\]

如果给定完整\(\Theta\)后施加LI，题目仍然条件独立；依赖是因为分析者只控制了\(\theta\)，没有控制额外维度。

## 随机效应testlet模型

若题目\(i\)属于testlet \(t\)，一个Rasch式模型为：

\[
P(X_i=1\mid\theta,u_t)
=
\frac{e^{\theta-b_i-u_t}}
{1+e^{\theta-b_i-u_t}}.
\tag{25}
\]

这里：

- \(\theta\)：总体能力；
- \(u_t\)：该testlet共享的局部因子或随机效应；
- \(b_i\)：项目难度。

同一testlet内的题共同包含\(u_t\)，所以只给定\(\theta\)时相关；若再给定\(u_t\)，模型恢复LI。

不同testlet的\(u_t\)通常被设为来自某个总体分布，例如\(N(0,\sigma_u^2)\)。这不是逻辑真理，而是层级模型的交换性假设：
在缺少每个testlet大量观测时，用共同分布实现部分池化。是否合理必须由设计和数据检验。

## 与bifactor模型的关系

bifactor模型给每道题一个一般因子载荷，并让题组内项目再加载在特定因子上：

\[
\text{item response}
\leftarrow
\text{general factor}
+
\text{group-specific factor}.
\]

随机效应testlet模型可视为bifactor家族的一种限制形式。一般因子解释全测验共同变化，特定因子解释题组内部剩余相关。

## ULD不是结构限制

只要斜率和载荷有限，ULD通常仍给每个模式正概率：

\[
P(00),P(01),P(10),P(11)>0.
\]

它改变模式的相对可能性，却不声明某个模式逻辑上不存在。这正是它被归为概率性LD的原因。

## RD：Response Dependence

RD描述后一道题的成功概率依赖前一道题的实际反应。它使用概率链式法则：

\[
P(X_i,X_{i'}\mid\theta)
=
P(X_i\mid\theta)
P(X_{i'}\mid X_i,\theta).
\]

第一题使用普通Rasch形式：

\[
P(X_i=x_i\mid\theta)
=
\frac{e^{x_i(\theta-b_i)}}{1+e^{\theta-b_i}}.
\]

第二题的条件模型为：

\[
P(X_{i'}=x_{i'}\mid X_i=x_i,\theta)
=
\frac{
e^{x_{i'}[\theta-b_{i'}-(1-2x_i)d]}
}
{1+e^{\theta-b_{i'}-(1-2x_i)d}}.
\tag{26}
\]

若\(d>0\)：

- 当\(x_i=0\)，第二题的有效难度是\(b_{i'}+d\)，更难；
- 当\(x_i=1\)，有效难度是\(b_{i'}-d\)，更易。

所以第一题答对后，第二题答对概率上升；第一题答错后，第二题答对概率下降。

## RD的实质含义

RD不是简单说“两题相关”，而是明确写出方向：

\[
X_i\longrightarrow X_{i'}.
\]

这可能表示：

- 后题使用前题答案；
- 前题产生练习或提示；
- 前题失败改变后题策略；
- 题目按学习阶段顺序出现。

因此若题目顺序被调换，模型含义可能改变。RD适合真实的序列机制，不宜仅因相关显著就使用。

## RD与ULD的区别

| ULD | RD |
| --- | --- |
| 依赖来自共同遗漏潜变量 | 依赖来自题间条件路径 |
| 给定完整潜变量后可恢复LI | 即使给定能力，\(X_{i'}\)仍依赖\(X_i\) |
| 通常对题间关系较对称 | 天然有方向 |
| 用多维SRF表达 | 用链式因子化表达 |

