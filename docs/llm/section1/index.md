# Section 1 · Hugging Face 与语言模型基础

这里的 **Section 1 对应课程 Chapter 1**。五份课件共 **187 页**，每页都保留原始 Beamer 图像，并提供可展开的英文文字。各讲开头附中文复习导读；原始课件及其引用归原作者所有。

## 全部课件

| 顺序 | 课件与复习页面 | 页数 | 主要内容 |
| --- | --- | ---: | --- |
| 1 | [Hugging Face Transformers 总览](01-hugging-face.md) | 38 | 三种架构、tokenizer、hidden states、推理与微调 |
| 2 | [Masked LM、Transformer 与 BERT](02-masked-lm.md) | 26 | n-gram、神经语言模型、attention、BERT、领域模型与句向量 |
| 3 | [Causal LM、GPT 与 Attention 实践](03-causal-lm.md) | 22 | GPT-1/2、causal mask、模型代码、attention 可视化 |
| 4 | [Scaling Laws、ICL 与 MoE](04-scaling-icl-moe.md) | 40 | Kaplan、Chinchilla、GPT-3、in-context learning、专家路由 |
| 5 | [Seq2Seq 与 Instruction Fine-Tuning](05-instruction-tuning.md) | 61 | BART、T5、T0、FLAN、Self-Instruct、IFEval、IHEval |

## 复习顺序

先用总览建立全章框架，再按 Masked LM → Causal LM → Scaling / ICL / MoE → Instruction Tuning 阅读。每讲均可通过右侧目录定位具体幻灯片；原 PDF 可以直接下载，原图可以点击放大。

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

课件内容按原版保留；中文导读单独标明明显的措辞或数值问题。PDF 提取文字可能打乱公式、表格或代码缩进，请以逐页原图为准。
