# Local Dependence Modeling

这一部分完整精读 Noventa、Spoto、Heller 与 Kelava（2026）的理论论文
*On the Modeling of Local Dependence*。论文的目标不是再发明一个单独的局部依赖指标，
而是建立一套统一语言，把 IRT、知识空间理论（knowledge space theory, KST）和认知诊断测评
（cognitive diagnostic assessment, CDA）中的局部依赖模型放在同一张地图上。

## 原文信息

| 项目 | 内容 |
| --- | --- |
| 论文 | Stefano Noventa, Andrea Spoto, Jurgen Heller, & Augustin Kelava. *On the Modeling of Local Dependence*. |
| 期刊 | *Psychometrika*, 91, 1020--1047, 2026 |
| DOI | [10.1017/psy.2026.10099](https://doi.org/10.1017/psy.2026.10099) |
| 文章类型 | Theory and Methods |
| 许可 | CC BY 4.0 |
| 研究范围 | 分类反应变量下的 IRT、KST 与 CDA；不直接处理连续反应因子分析 |

## 一句话总框架

文章把所有测量模型拆成三层：

\[
P(\boldsymbol X=\boldsymbol x\mid\Theta)
=
\sum_{K\in\mathcal K}
\underbrace{P(\boldsymbol X=\boldsymbol x\mid K,\Theta)}_{g\text{-过程}}
\underbrace{\pi(K\mid\Theta)}_{p\text{-过程 / SRF}}.
\]

| 层 | 回答的问题 |
| --- | --- |
| 结构 \(\mathcal K\) | 哪些潜在状态原则上可能存在？ |
| \(p\)-过程 / SRF | 给定能力或属性，个体进入每个潜在状态的概率是多少？ |
| \(g\)-过程 | 给定潜在状态，猜测、失误等机制怎样产生实际作答？ |

局部依赖由两个不同但可以并存的机制产生：

\[
\boxed{\mathcal K=2^Q:\ \text{概率性 LD}}
\qquad
\boxed{\mathcal K\subsetneq2^Q:\ \text{确定性 LD}}.
\]

前者允许全部反应模式，依赖只改变模式概率；后者先在潜在层排除某些模式，再用
\(g\)-过程解释观测数据中的结构违反。

## 推荐阅读顺序

1. [研究问题、术语与贡献](01-question-terms-contribution.md)
2. [局部独立、列联表与两种典型依赖](02-local-independence-tables.md)
3. [结构、状态与过程](03-structures-and-processes.md)
4. [统一框架与两张分类表](04-unified-taxonomy.md)
5. [概率性LD（一）：ULD、testlet与RD](05-probabilistic-uld-rd.md)
6. [概率性LD（二）：OD、CD、Bahadur与copula](06-probabilistic-joint-models.md)
7. [确定性LD：boundary mixture、SLD与KST-IRT](07-deterministic-models.md)
8. [数值比较：LI、RD、OD、\(\Theta\)-SLM与LKS](08-numerical-comparisons.md)
9. [参数解释与可识别性](09-interpretation-identifiability.md)
10. [多类别题、testlet与知识结构](10-polytomous-testlets.md)
11. [新模型方向与全文结论](11-new-models-conclusions.md)
12. [附录：SLD、Huynh扩展与阈值失序](12-appendices.md)
13. [符号与缩写表](symbols.md)
14. [参考文献](references.md)

## 阅读时始终分清的四组概念

| 不应混同的概念 | 区别 |
| --- | --- |
| 单维性 vs. 局部独立 | 给定多个潜在特质也可能局部独立；单维模型中也可能存在题间直接依赖 |
| ULD vs. SLD | ULD来自遗漏潜在特质；SLD来自题面、位置、共享刺激或近似复制等表层机制 |
| 概率性 vs. 确定性LD | 区别在潜在支持集是否有结构零，不是最终模型有没有随机性 |
| factorization vs. reparameterization | 前者把联合概率分成条件概率乘积，后者更换同一概率模型的函数坐标 |

## 文章做了什么、没有做什么

文章完成的是模型本体和分类学：说明怎样用结构、过程、因子化与重新参数化描述已有模型，
并指出分类表中尚未开发的模型家族。文章没有给出完整的结构学习算法，也没有通过大规模模拟证明
某一类模型普遍优于另一类。可识别性、估计、模型比较和真实数据应用被明确留作未来工作。

