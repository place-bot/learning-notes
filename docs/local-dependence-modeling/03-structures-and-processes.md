# 结构、状态与过程

## 先把4PL拆成两个过程

作者先把4PL重写为：

\[
P(X_i=1\mid\theta)
=
c_i\pi(K_i=0\mid\theta)
+(1-d_i)\pi(K_i=1\mid\theta).
\tag{6}
\]

其中潜在变量\(K_i\)表示题目是否被掌握，并令：

\[
\operatorname{logit}\pi(K_i=1\mid\theta)
=a_i(\theta-b_i).
\tag{7}
\]

于是4PL不再是一条不可拆的曲线，而是：

1. \(p\)-过程：\(\theta\to K_i\)，能力怎样产生掌握；
2. \(g\)-过程：\(K_i\to X_i\)，掌握怎样通过猜测或失误产生作答。

具体地：

\[
c_i=P(X_i=1\mid K_i=0),
\qquad
d_i=P(X_i=0\mid K_i=1).
\]

## 结构的正式定义

令\(D\)是一个非空元素集合。结构是二元组：

\[
(D,\mathcal Y),
\]

其中：

\[
\{\varnothing,D\}
\subseteq
\mathcal Y
\subseteq
2^D.
\]

\(\mathcal Y\)中的每个子集\(Y\)称为一个状态。结构不是相关矩阵，而是“哪些元素组合允许存在”的支持集。

## 三种典型结构

设\(D=\{d_1,d_2,d_3\}\)。

### 链

\[
\mathcal Y_{	ext{chain}}
=
\{\varnothing,\{d_1\},\{d_1,d_2\},D\}.
\]

只允许逐层累积；\(d_2\)以\(d_1\)为先决，\(d_3\)又在更高层。

### 幂集

\[
\mathcal Y_{	ext{power}}=2^D.
\]

三个元素的全部\(2^3=8\)种组合都允许。

### 任意结构

可以保留某些分支、排除另一些组合，不必是链，也不必是完整幂集。

## 结构与列联表一一对应

令随机向量\(\boldsymbol Y=(Y_1,\ldots,Y_m)\)满足：

\[
Y_i=1
\quad\Longleftrightarrow\quad
d_i\in Y.
\]

例如状态\(Y=\{d_1,d_3\}\)对应：

\[
\boldsymbol y=(1,0,1).
\]

若给每个状态一个概率\(P(Y)\)，就得到概率结构\((D,\mathcal Y,P)\)。

- \(\mathcal Y=2^D\)：完整列联表；
- \(\mathcal Y\subsetneq2^D\)：不完整列联表；
- \(2^D\setminus\mathcal Y\)中的模式是结构零。

## 三种解释

### 知识结构

领域元素是题目或可掌握的问题：

\[
(Q,\mathcal K,\pi).
\]

状态\(K\subseteq Q\)表示一个人能够掌握的题目集合。

### 能力结构

领域元素是二分属性或技能：

\[
(S,\mathcal C,\nu).
\]

例如\(s_1=\)加法，\(s_2=\)分数。幂集表示二者可任意组合；链表示掌握\(s_2\)必须先掌握\(s_1\)。

### 多类别题与连续特质

四类别Likert题可以由四个链状态表示：

\[
\varnothing
\subset
\{d_1\}
\subset
\{d_1,d_2\}
\subset
\{d_1,d_2,d_3\}.
\]

元素\(d_i\)可解释为跨越类别所需的阈值。把有限链推广为不可数链，就得到连续潜在特质；
\(\theta\in\mathbb R\)可理解为定义在连续能力结构上的随机变量。

## 过程的正式定义

给定两个概率结构，离散过程满足全概率公式：

\[
P(X)=\sum_{Y\in\mathcal Y}P(X\mid Y)P(Y).
\tag{8}
\]

连续潜变量时：

\[
P(X)=\int P(X\mid\theta)f(\theta)d\theta.
\tag{9}
\]

这两式分别是潜在类模型和潜在特质模型的共同骨架。

## \(p\)-过程与\(g\)-过程

作者沿用Hutchinson的命名：

- \(p\)-process：能力/属性结构到知识结构，描述掌握；
- \(g\)-process：知识状态到观察反应结构，描述猜测、失误和其他二级机制。

典型路径为：

\[
\Theta
\xrightarrow{p}
K
\xrightarrow{g}
\boldsymbol X.
\]

## 因子化

因子化把联合概率写成乘积。例如局部独立：

\[
P(\boldsymbol X\mid\theta)
=
\prod_iP(X_i\mid\theta).
\]

或顺序模型：

\[
P(X_1,X_2\mid\theta)
=P(X_1\mid\theta)P(X_2\mid X_1,\theta).
\]

因子化不只是代数技巧；选择哪种因子化，等于声明怎样的条件顺序或独立关系。

## 重新参数化

重新参数化用链接函数改变概率的坐标：

\[
\ell_r[P(X\mid Y)]=f_r(X,Y).
\tag{22}
\]

常见链接有identity、logit、probit和log；\(f_r\)称为kernel。它可以包含难度、能力、主效应和交互效应。

重要区别是：

- 因子化回答“联合概率拆成哪些条件块”；
- 重新参数化回答“每一块或整个联合概率用什么函数形式表示”。

一个模型可以同时使用二者。

