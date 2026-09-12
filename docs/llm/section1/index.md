# Section 1 · Hugging Face 与语言模型基础

这里的 **Section 1 对应课程 Chapter 1**，现在按中文讲义学习。每讲先解释概念的意思、它解决的问题、公式中的符号，再给例子和自测答案；不要求先看懂原幻灯片才能阅读。五份原 Beamer 共 187 页，放在各讲末尾作对照。

## 五讲中文详解

| 顺序 | 中文讲义 | 原课件页数 | 主要内容 |
| --- | --- | ---: | --- |
| 1 | [Hugging Face Transformers 总览](01-hugging-face.md) | 38 | 三种架构、tokenizer、hidden states、推理与微调 |
| 2 | [Masked LM、Transformer 与 BERT](02-masked-lm.md) | 26 | n-gram、神经语言模型、attention、BERT、领域模型与句向量 |
| 3 | [Causal LM、GPT 与 Attention 实践](03-causal-lm.md) | 22 | GPT-1/2、causal mask、模型代码、attention 可视化 |
| 4 | [Scaling Laws、ICL 与 MoE](04-scaling-icl-moe.md) | 40 | Kaplan、Chinchilla、GPT-3、in-context learning、专家路由 |
| 5 | [Seq2Seq 与 Instruction Fine-Tuning](05-instruction-tuning.md) | 61 | BART、T5、T0、FLAN、Self-Instruct、IFEval、IHEval |

## 复习顺序

先读第一讲，分清 token、embedding、hidden state、logits。第二讲手算 attention，再理解 BERT。第三讲弄懂 GPT 的 causal mask 和生成过程。第四讲把规模与预算、ICL 与微调、MoE 的容量与计算区分开。第五讲理解指令训练的数据、目标和评价。

每个英文术语第一次出现时都配中文解释。手算例子是为理解而构造的示例；涉及课件数值的地方单独注明。原 PDF、图片与提取文字保留在讲义之后。

## 按不懂的概念找讲解

| 想弄懂的问题 | 去哪一讲 |
| --- | --- |
| Token 是词吗？Embedding 与 hidden state 有什么区别？ | [第一讲，2–5 节](01-hugging-face.md) |
| Encoder、decoder、head、pipeline 分别是什么？ | [第一讲，6–8 节](01-hugging-face.md) |
| n-gram、RNN、梯度消失为什么引出 attention？ | [第二讲，1–4 节](02-masked-lm.md) |
| Q/K/V、softmax、多头和 cross-attention 怎么计算？ | [第二讲，5–8 节](02-masked-lm.md) |
| MLM、NSP、SciBERT、BioBERT、SBERT 是什么？ | [第二讲，9–12 节](02-masked-lm.md) |
| Causal mask、teacher forcing、困惑度、温度是什么？ | [第三讲](03-causal-lm.md) |
| Scaling law、FLOPs、Chinchilla 怎么理解？ | [第四讲，1–4 节](04-scaling-icl-moe.md) |
| ICL、zero/few-shot、元学习、涌现是什么意思？ | [第四讲，5–8 节](04-scaling-icl-moe.md) |
| MoE、expert、router、load balancing 是什么？ | [第四讲，9–12 节](04-scaling-icl-moe.md) |
| Seq2Seq、BART、T5、T0 是什么关系？ | [第五讲，1–5 节](05-instruction-tuning.md) |
| IFT、SFT、FLAN、Self-Instruct 到底在训练什么？ | [第五讲，6–12 节](05-instruction-tuning.md) |
| IFEval、原子指令、指令层级、IHEval 怎么区分？ | [第五讲，13–18 节](05-instruction-tuning.md) |

## 应该能回答的问题

1. Encoder-only、decoder-only 和 encoder-decoder 的输入可见性及训练目标有什么区别？
2. Token IDs、embedding、hidden states 和输出概率分别是什么？
3. Query、key、value 如何决定 attention？Causal mask 限制了什么？
4. BERT 的 MLM 与 GPT 的 next-token prediction 如何影响下游使用方式？
5. 给定计算预算，如何理解参数量和训练 token 数的取舍？
6. ICL 与 fine-tuning 分别在哪一步使用示例，是否更新权重？
7. MoE 的总参数量、激活参数量与 routing 有什么关系？
8. T5 的 text-to-text 与 instruction tuning 有什么联系和区别？
9. 为什么训练损失下降不等于泛化能力提高？
10. IFEval 与 IHEval 各自在检验什么？

## 版本与完整性

采用本地带讲次编号的 Chapter1-L00 至 Chapter1-L04 五份 PDF，同内容的旧编号副本不重复列入。页码包括封面、目录和重复展示页，均未省略。各 PDF 的 SHA-256 与页数保存在[来源清单](../../assets/llm/section1/sources.json)。

讲义按课件主题展开，补充概念解释、手算与常见误区；原 Beamer 内容按原版保留。PDF 提取文字可能打乱公式、表格或代码缩进，查原版时请以原图为准。
