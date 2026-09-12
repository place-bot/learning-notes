## 1. 语言模型究竟在建模什么？

语言模型（language model，LM）给文本分配概率。给出“今天的天气很”，它可以估计下一个 token 是“好”“冷”或其他内容的概率。它输出的是一个分布，不是一条预先写好的标准答案。

**大语言模型（LLM）**通常指规模较大的语言模型。参数是训练中学到的数值，例如矩阵中的元素；参数多，意味着模型能够表示更复杂的规律，但不等于每个参数储存一个知识点。模型也不是查字典：它根据输入进行计算，生成仍可能出错。

把语言模型类比为你熟悉的统计模型：输入文本是条件变量，接下来出现的 token 是预测对象，训练让观测文本获得更高的条件概率。不过神经网络的中间表示是联合学出来的，并没有天然对应到可解释的心理特质。

## 2. Hugging Face、Transformers 和模型是什么关系？

**Hugging Face** 提供模型与数据的共享平台等工具；**Transformers** 是加载和使用模型的 Python 库；**BERT、GPT、T5** 是模型家族。平台、软件库、模型不能当成同一件东西。

**Checkpoint** 是保存下来的模型状态，通常包括权重及配置。**Pretrained model** 是已经完成预训练的模型。调用 `from_pretrained(...)` 的意思是加载已有的配置或权重，不是在这一行重新训练模型。

**Inference（推理）**是用已有权重计算输出。**Training（训练）**是根据数据和损失更新权重。日常说“问模型一个问题”一般属于 inference；“拿一批训练样本改变模型行为”才涉及 training。

## 3. Token、tokenizer、vocabulary：文本怎么变成数字？

**Token** 是模型处理文本的单位，可以是一个词、词的一部分、标点或其他片段。“Transformers”在课件例子里被拆成 `Transform` 与 `ers`。所以 token 数不等于单词数，也不能直接当作中文字数。

**Tokenizer（分词器）**规定如何切分文本、如何把片段映射到编号。**Vocabulary（词表）**是可用 token 与编号的集合。**Token ID** 只是词表索引：编号 100 和 101 相邻，不意味着它们的意思相近。

例如，一句文本经某个分词器得到 `[37, 218, 9]`，这些数字不能直接拿去比较语义距离。它们下一步会查表得到向量。不同模型的词表和编号规则可能不同，加载模型时要配套加载 tokenizer。

**Special tokens（特殊 token）**承担结构功能。例如 BERT 的 `[CLS]` 常用于取得整句表示，`[SEP]` 用于分隔句段，`[MASK]` 表示被遮住的位置，padding token 用于把一批长短不同的序列补齐。它们的角色取决于模型约定。

## 4. Embedding 与 hidden state：最容易混淆的两个概念

**Embedding（嵌入）**是把离散 token 映射为连续向量。若词表有 \(V\) 个 token，每个向量长 \(d\)，可以想象有一张 \(V\times d\) 的可学习表。Token ID 用来选择其中一行。

**Hidden state（隐藏状态）**是 token 经过网络某一层后形成的表示。它通常已经结合了上下文。同一个 `bank` 在“river bank”和“bank account”中可以得到不同的 hidden states；最初的 token embedding 则可能是同一个查表向量。

**Contextualized representation（上下文化表示）**强调向量会随着句子变化。原始 word embedding 更像一个词的通用表示，hidden state 更像“这个词在这句话中扮演什么角色”的编码。

若一次输入 2 句话，每句话补到 10 个 token，隐藏维度为 768，那么最后一层表示的 shape 可以是：

\[
H\in\mathbb{R}^{2\times10\times768}.
\]

这三个维度分别是 batch size、sequence length、hidden size。**Tensor（张量）**在这里就是多维数组。Hidden state 也不是预测概率；通常还需要输出层把它映射为词表大小的分数。

## 5. Logits、softmax、probability 与 loss

**Logits** 是模型给候选 token 的未归一化分数，可以为正也可以为负。**Softmax** 把分数变为加起来等于 1 的概率：

\[
p_j=\frac{e^{z_j}}{\sum_k e^{z_k}}.
\]

若三个候选的 logits 是 \((0,1,2)\)，概率约为 \((0.090,0.245,0.665)\)。最大的 logit 对应最高概率，但其他候选并没有自动消失。

**Loss（损失）**衡量模型预测与训练目标的差距。语言模型常用真实 token 的负对数概率：\(-\log p_{\text{true}}\)。真实答案概率为 0.8 时，损失约 0.223；只有 0.1 时，损失约 2.303。训练希望减小它。

**Gradient（梯度）**告诉我们参数微小变化如何影响损失；**optimizer（优化器）**利用梯度更新参数。训练损失很小，只说明模型拟合了训练目标，还要看新样本才能判断泛化。

## 6. 三种 Transformer 架构分别做什么？

| 架构 | 一般如何读取信息 | 典型训练或使用方式 | 直观例子 |
| --- | --- | --- | --- |
| Encoder-only | 一个位置通常能读左右两侧输入 | 学习输入的表示、填被遮住的词 | BERT 根据“The [MASK] is barking”预测 dog |
| Decoder-only | 每个位置只能读当前及之前的位置 | 预测下一个 token、连续生成 | GPT 根据“The dog is”预测 barking |
| Encoder-decoder | Encoder 读输入；decoder 读此前输出并关注输入表示 | 给定输入生成另一段序列 | T5 把英文翻译成德文 |

**Encoder（编码器）**把输入转成表示；**decoder（解码器）**逐步产生输出。这里不是把文件压缩和解压的意思。三种架构的差别主要在信息可见范围和模块连接方式，不能简单说 encoder 只会“理解”、decoder 只会“生成”；通过不同的任务设计，应用范围会重叠。

**Masked LM** 和 **causal LM** 是训练目标及信息使用方式的描述；**encoder-only** 和 **decoder-only** 是架构描述。两组概念经常对应，但不是同一种分类标准。

## 7. 课件中的 Hugging Face 代码怎么读？

下面是课件流程的示意，`MODEL_PATH` 表示已经准备好的配套模型；不是一个可以直接下载的模型名：

```python
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModel.from_pretrained(MODEL_PATH)
batch = tokenizer(text, return_tensors="pt")
outputs = model(**batch)
hidden = outputs.last_hidden_state
```

第一行加载文本到 token 的转换规则，第二行加载模型。第三行把文本变成 PyTorch 张量；`pt` 指 PyTorch。`batch` 是包含输入字段的字典，`**batch` 把字典展开成函数参数。最后一行取得上下文表示。

**AutoModel** 通常返回基础网络输出；**AutoModelForCausalLM** 带有语言建模输出头；**AutoModelForSeq2SeqLM** 面向序列到序列生成。**Head（任务头）**是把通用表示映射到具体预测目标的输出模块。

**Pipeline** 把分词、模型计算、结果处理包装起来。例如 `fill-mask` 返回 mask 位置的候选词和分数。**Device** 表示计算放在 CPU 还是 GPU；**CUDA** 是 NVIDIA GPU 常用的计算环境。

`model.train()` 与 `model.eval()` 切换某些层的行为，例如 dropout，并不直接决定参数是否更新；只有执行反向传播并让优化器更新权重，才完成训练步骤。

## 8. 为什么 GPT 会续写，却没有回答问题？

原始 causal LM 训练时学的是“什么文本可能接在后面”。输入“In one sentence, GPT is”，它可能续写成自然的句子，也可能生成无关内容。它不自动理解成“这是用户发出的必须执行的任务”。

课件用少量 prompt-completion 样本微调。**Prompt** 是给模型的输入；**completion** 是接在后面的文本。**Fine-tuning（微调）**在已有参数上继续训练，让模型更适合某种数据或任务。**SFT（监督微调）**强调有目标答案作为监督。

**Freeze（冻结）**参数是让某些权重不被更新。只更新最后一层通常比更新全模型便宜，但也限制了可改变的表示。**Overfitting（过拟合）**是模型记住训练中的狭窄规律，换一句话就不会了。课件里重复相似定义后训练损失降低，并不等于模型全面掌握了这些概念。

## 9. 后半章为什么讨论规模、MoE 和指令？

总览后半段提出三类问题。**Scaling laws** 问更多参数、更多数据和更多计算如何改变性能；**MoE** 问能否让模型拥有很多参数，但每次只使用一部分；**instruction tuning** 问怎样使续写模型更可靠地执行自然语言要求。

课件中的模型名称和功能介绍按该版讲义理解。例如 **open weights（开放权重）**说明能取得权重文件，不自动意味着训练数据、训练过程和全部使用权利都开放。**Multimodal（多模态）**表示输入或输出涉及文本之外的图像、音频等形式；本章主线仍是文本语言模型。

## 10. 用三个小问题检查自己

**Token ID 17 比 18 小，是否意味着语义更弱？** 不。它只是索引；语义关系要看学到的向量与具体模型。

**Hidden size 是 768，是否意味着有 768 个明确的人类概念？** 不。向量维度通常是分布式表示，不能直接逐维命名。

**能在训练句上正确补全，就能回答新问题吗？** 不能据此推出。要区分训练拟合、同分布测试表现和新任务泛化。

下一讲：[从语言建模到 Attention 与 BERT](02-masked-lm.md)。
