## 1. 从概率分解理解 language modeling

设一句话的 token 是 \(x_1,\ldots,x_T\)。联合概率可以按概率链式法则写成：

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t}).
\]

\(T\) 是句子长度，\(x_{<t}\) 是第 \(t\) 个位置之前的全部 token。这一步是概率恒等式，还没有假定相邻词独立。真正的建模选择是：如何估计右边每个条件概率？

例如“I like tea”的概率可以写成 \(P(I)P(like\mid I)P(tea\mid I,like)\)。**Autoregressive（自回归）**表示用序列已有部分预测后续部分；这里不是只能用线性 AR 模型。

## 2. Unigram 与 n-gram：先看简单模型为什么不够

**Unigram** 只看一个 token 的总体频率，用 \(P(x_t)\) 近似条件概率。这样“I love dogs”与“dogs love I”若由相同 token 构成，就可能得到相同乘积，语序信息丢失了。

**Bigram** 只看前一个 token；**trigram** 看前两个；一般的 n-gram 看前 \(n-1\) 个：

\[
\widehat P(w\mid u)=\frac{c(u,w)}{c(u)}.
\]

\(c(u,w)\) 表示上下文 \(u\) 后接 \(w\) 的计数。如果“I like”出现 10 次，其中 6 次接 tea，那么经验条件概率是 0.6。优点是简单；缺点是没见过的组合可能被赋予零概率，并且固定窗口遗漏远处信息。平滑可缓解零概率，却不能消除窗口限制。

**Data sparsity（数据稀疏）**在这里指可能的词组合非常多，而观察到的组合很少，不是指你的数值矩阵一定存成稀疏格式。

## 3. Neural LM：为什么把词变成向量？

前馈神经语言模型先把上下文 token 查成 embedding，拼接后经过可学习变换，再输出下一个词的分布。若“cat”和“dog”在训练中学到某些相似特征，模型能在它们之间共享统计信息，而不必分别记住所有 n-gram。

**Feed-forward（前馈）**表示计算沿层向前，不在时间上循环传递状态。**Nonlinearity（非线性）**让多层组合能表达超出线性模型的关系。简单前馈 LM 仍可能使用固定长度上下文，因此长距离依赖还没有解决。

**Long-distance dependency（长距离依赖）**例如“The key to the old cabinets is missing”。决定 `is` 的是较远的 `key`，不是更近的 `cabinets`。只看最近几个词容易判断错。

## 4. RNN 与 vanishing gradient 是什么？

**RNN（循环神经网络）**把过去压进一个随时间更新的状态：

\[
h_t=f(W_hh_{t-1}+W_xe_t+b).
\]

\(e_t\) 是当前 token embedding，\(h_{t-1}\) 是此前状态，\(W_h,W_x,b\) 是参数，\(f\) 是非线性函数。每一步都能间接依赖更早输入，所以不再只限固定窗口。

但训练信号往回经过很多步时，要连乘许多导数。若这些导数通常较小，早期参数收到的梯度就会非常弱，这叫 **vanishing gradient（梯度消失）**。它不等于模型在前向计算时突然失忆，而是长期关系很难通过训练学好。

**LSTM** 使用门控机制控制信息保留、输入和输出，改善长距离信息传播。**Convolution（卷积）**通过局部窗口提取模式，堆叠层扩展覆盖范围。课件将它们与 attention 对比，是在比较信息如何在位置之间传播。

## 5. Attention：一个位置怎样挑选有用信息？

Attention 让一个 token 根据当前需要，从其他位置汇总信息。它的核心是“计算相关程度，再做加权求和”。不是先写好“主语看谓语”的规则，而是训练这些权重的计算方式。

**Query（查询向量）**可理解为当前位置在找什么；**key（键向量）**表示每个候选位置能提供什么线索；**value（值向量）**是最后实际被汇总的内容。这是辅助理解的比喻，三者都是向量，不是人类可读的问答。

对输入表示矩阵 \(X\in\mathbb R^{n\times d}\)：

\[
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V.
\]

\(n\) 是 token 数；\(d\) 是输入隐藏维度；\(W_Q,W_K,W_V\) 是训练得到的投影矩阵。若 query/key 维度为 \(d_k\)，则 \(Q,K\) 是 \(n\times d_k\)。Value 可有另一个维度 \(d_v\)。

\[
A=\operatorname{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right),\qquad H=AV.
\]

\(QK^\top\) 是 \(n\times n\) 的相关分数矩阵。Softmax 沿每行计算，因此 \(A_{ij}\) 表示位置 \(i\) 汇总位置 \(j\) 信息的权重。\(H\) 的大小是 \(n\times d_v\)。除以 \(\sqrt{d_k}\) 是为了控制分数尺度，避免维度变大时点积过大，让 softmax 过度尖锐。

## 6. 手算一次 attention

假设一个 query 对两个 key 的缩放后分数为 \((0,\ln3)\)。则 softmax 权重是：

\[
(a_1,a_2)=\left(\frac{1}{1+3},\frac{3}{1+3}\right)=(0.25,0.75).
\]

若两个 value 为 \(v_1=(2,0)\)、\(v_2=(0,4)\)，输出是：

\[
h=0.25(2,0)+0.75(0,4)=(0.5,3).
\]

分数决定取多少，value 决定取什么。若只计算 query-key 相似度，没有乘 value，还没有完成 attention 输出。

## 7. Self-attention、cross-attention、multi-head

**Self-attention** 的 Q、K、V 都来自同一段序列的表示，句子内部各位置互相交换信息。**Cross-attention** 的 query 来自一侧，key/value 来自另一侧，例如翻译时 decoder 用自己当前状态去读取 encoder 的输入表示。

**Multi-head attention（多头注意力）**并行学习多组投影，各自在不同表示空间汇总信息，再拼接并投影。有的头可能对局部关系更敏感，有的关注远处；但不能事先保证“第一头管语法、第二头管语义”。

每一层的输入不是原始词义表，而是上一层已经加工的表示。因此深层 attention 即使指向某个位置，也可能在读该位置先前聚合的信息。

## 8. Transformer 不只有 attention

**Position information（位置信息）**帮助模型区分语序。单纯把同样 token 调换顺序，模型必须能感知位置变化；不同 Transformer 使用不同位置编码方式。

**FFN（前馈网络）**通常对每个位置的向量分别做非线性变换；attention 负责跨位置汇总，FFN 进一步处理表示。**Residual connection（残差连接）**把模块输入加回输出，帮助信息和梯度传播。**Layer normalization** 对单个表示的特征做归一化，帮助训练稳定。

理解 Transformer 时，应把它看作多层“汇总信息 + 加工表示”的网络。Attention 不是整台机器。

## 9. BERT 为什么能双向读，又不会直接看到答案？

**BERT** 全称 Bidirectional Encoder Representations from Transformers。它的 encoder 通常允许一个位置看到左右两侧输入。预训练时把部分词替换或遮住，要求预测原词，这叫 **MLM（masked language modeling）**。

例如“The [MASK] is barking”，左右线索都可用于猜 `dog`。因为目标位置输入不是直接给出原词，模型需要利用上下文。

原版 BERT 选出约 15% 的 token 作为预测目标。对这些被选中的 token，约 80% 换成 `[MASK]`、10% 换成随机 token、10% 保持不变。**80/10/10 的分母是被选中的位置，不是全句。** 这种设计也用于缓解预训练有 `[MASK]`、下游输入通常没有它的不一致。

MLM 损失可以理解为：

\[
\mathcal L_{\mathrm{MLM}}=-\sum_{t\in M}\log P_\theta(x_t\mid\widetilde x),
\]

\(M\) 是选中的位置，\(\widetilde x\) 是经过替换的输入，\(\theta\) 是全部模型参数。监督目标是原始 token。

## 10. NSP、输入 embedding 与下游任务

原版 BERT 的 **NSP（next sentence prediction）**判断两个句段是否在原文中相邻。它是句对二分类，不是“生成下一句话”。后续 BERT 变体未必保留 NSP。

BERT 输入表示包含 token、segment 和 position embedding。Segment 标记 token 属于句段 A 还是 B；position 标记位置；token embedding 表示词表项目。相加后共同进入网络。

**Pretraining（预训练）**用大量文本学习通用表示；**downstream task（下游任务）**是在此基础上做分类、问答等具体工作；**transfer learning（迁移学习）**是在新任务中复用已学到的参数或表示。

**Token-level** 任务逐位置预测，例如 **NER** 为姓名、机构等标实体标签；**sentence-level** 任务对整句分类。**MNLI** 判断两个句子的蕴含、矛盾或中立关系；**SQuAD** 的经典任务是在段落中定位问题答案的起止位置。它们不是三个网络模块，而是任务或数据集。

## 11. SciBERT、BioBERT 与 Sentence-BERT 各改了什么？

**SciBERT** 使用科学文献训练，使模型更熟悉科学领域语言，并研究领域词表。**BioBERT** 在生物医学语料上继续预训练 BERT；重点是领域语言适应，不是换一种“生物版 attention”。

**Sentence-BERT（SBERT）**针对句向量学习。普通 BERT 可以输出 token 表示，但直接平均或取 `[CLS]` 不一定得到适合语义检索的距离空间。SBERT 用成对句子等监督，使相似句子在向量空间里更容易比较。

**Siamese（孪生）网络**在这里指两段输入经过共享权重的编码器；它们不是两套完全独立训练的模型。**Pooling（池化）**把多个 token 向量汇成一个句向量。**Cosine similarity（余弦相似度）**比较两个向量的方向：\(u^\top v/(\|u\|\|v\|)\)。

课件还列出 **PICO** 信息抽取（患者/人群、干预、比较、结果）、关系分类和依存句法分析。它们用来检验表示能否支持具体科学文本任务，而不是只看预训练损失。

## 12. 读实验表时怎么看？

先找任务、指标、基线和数据划分。**Baseline** 是比较对象；**fine-tuning** 表示模型在该任务上训练过。NER 常用 precision、recall、F1：分别关注预测中有多少正确、真实实体找回多少，以及二者的调和平均。不同任务的 F1、accuracy 或其他指标不能直接混成“模型总智力”。

**自测：BERT 的双向性与 causal LM 的概率链式分解冲突吗？** 不冲突。链式法则始终成立；BERT MLM 使用的是被遮盖输入条件下的预测目标，不是在以同样方式拟合逐词自回归分解。

**自测：attention 权重大就是这个词导致了答案吗？** 不能直接作因果解释。权重只是一次信息汇总的部分计算，还受到 value、其他头、后续层等影响。

下一讲：[Causal LM 与 GPT](03-causal-lm.md)。
