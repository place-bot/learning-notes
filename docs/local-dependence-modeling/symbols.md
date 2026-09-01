# 符号与缩写表

## 核心符号

| 符号 | 含义 |
| --- | --- |
| \(Q=\{q_1,\ldots,q_J\}\) | 二分题目/问题领域 |
| \(S=\{s_1,\ldots,s_A\}\) | 属性或技能领域 |
| \(X_i\) | 第\(i\)题观察反应，0错1对 |
| \(K\subseteq Q\) | 一个知识状态/掌握题目集合 |
| \(\mathcal K\) | 允许知识状态的结构 |
| \(2^Q\) | \(Q\)的幂集，全部\(2^J\)种模式 |
| \(K^O\) | 状态\(K\)的外缘，可合法一步添加的项目 |
| \(C\subseteq S\) | 一个能力/属性状态 |
| \(\mathcal C\) | 能力结构 |
| \(\theta\) | 连续潜在特质 |
| \(\Theta\) | 多维潜在特质向量 |
| \(\pi(K\mid\theta)\) | 状态反应函数SRF |
| \(P(X\mid K)\) | \(g\)-过程条件概率 |
| \(\eta_i\) | 未掌握时的lucky guess概率 |
| \(\beta_i\) | 已掌握时的careless error/slip概率 |
| \(a_i,b_i,c_i,d_i\) | 区分度、难度、猜测、失误参数 |
| \(p_{x_1x_2}\) | 二题列联表格概率 |
| \(f(K,\theta)\) | 重新参数化中的kernel |

## 缩写

| 缩写 | 英文 | 中文 |
| --- | --- | --- |
| LI | local independence | 局部独立 |
| LD | local dependence | 局部依赖 |
| SLD | surface local dependence | 表层局部依赖 |
| ULD | underlying local dependence | 潜在/底层局部依赖 |
| RD | response dependence | 反应依赖 |
| OD | order dependence | 顺序依赖 |
| CD | combination dependence | 组合依赖 |
| LND | local non-negative dependence | 局部非负依赖 |
| WLIE | weak local independence in expectation | 期望意义下弱局部独立 |
| IRT | item response theory | 项目反应理论 |
| KST | knowledge space theory | 知识空间理论 |
| CDA | cognitive diagnostic assessment | 认知诊断测评 |
| IRF | item response function | 项目反应函数 |
| SRF | state response function | 状态反应函数 |
| GLI | generalized local independence | 广义局部独立 |
| BLIM | basic local independence model | 基本局部独立模型 |
| \(\Theta\)-BLIM | latent-trait-extended BLIM | 潜在特质扩展BLIM |
| SLM | simple learning model | 简单学习模型 |
| \(\Theta\)-SLM | latent-trait-extended SLM | 潜在特质扩展SLM |
| LKS | logistic knowledge structure | Logistic知识结构 |
| PCM | partial credit model | 部分计分模型 |
| 1PLAG | one-parameter logistic ability-based guessing | 单参数logistic能力型猜测模型 |

## 三个容易混淆的“概率”

| 概率 | 层次 | 问题 |
| --- | --- | --- |
| \(\pi(K\mid\theta)\) | \(p\)-过程 | 能力为\(\theta\)的人处于状态\(K\)的概率？ |
| \(P(X\mid K)\) | \(g\)-过程 | 状态\(K\)的人产生观察反应\(X\)的概率？ |
| \(P(X\mid\theta)\) | 观察模型 | 能力为\(\theta\)的人最终给出反应\(X\)的概率？ |

它们通过边缘化连接：

\[
P(X\mid\theta)
=\sum_{K\in\mathcal K}P(X\mid K)\pi(K\mid\theta).
\]

