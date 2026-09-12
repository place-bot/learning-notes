# Seq2Seq 与 Instruction Fine-Tuning

[返回 Section 1](index.md)

授课课件：Meng Jiang · CSE 60556 · Fall 2026。来源 `Chapter1-L04 (L06).pdf`，共 **61 页**。

[下载完整原课件 PDF](../../assets/llm/section1/05-instruction-tuning/slides.pdf)


## 1. Seq2Seq：输入一段，输出另一段

**Sequence-to-sequence（Seq2Seq）**指给定输入序列，预测输出序列。例如英文 → 德文、文章 → 摘要、问题与材料 → 答案。输入和输出的长度可以不同。

经典 encoder-decoder 中，encoder 把输入 \(x\) 编成表示；decoder 根据此前输出以及该表示，逐步预测目标 \(y\)：

\[
P(y\mid x)=\prod_{t=1}^{T_y}P(y_t\mid y_{<t},x).
\]

\(T_y\) 是输出长度。Decoder 内部的 self-attention 控制只看此前输出；cross-attention 读取 encoder 的输入表示。它不是把英文每个词机械换成一个德文词，而是建模整个条件输出序列。

## 2. BART 的 denoising 是什么意思？

**Denoising（去噪）**在这里指先人为破坏文本，再训练模型恢复原文。例如删掉片段、用 mask 代替一段或调整句序。模型要结合上下文推断缺失和被打乱的信息。

**BART** 把双向 encoder 与自回归 decoder 结合起来。与只在选中位置预测的典型 MLM 不同，BART 可以让输入和输出长度、位置不完全对应，再通过 decoder 生成完整目标。

为什么这样预训练能帮摘要或翻译？因为网络已经学过“读取不完整或变形的输入，再组织输出”的能力。但仍通常需要对应任务的数据或适配，不能仅凭去噪目标推断某项下游任务一定做好。

## 3. T5 的 text-to-text 统一了什么？

**T5** 是 Text-to-Text Transfer Transformer。它把不同任务都表达成文本输入 → 文本输出。例如：

| 任务 | 输入 | 输出 |
| --- | --- | --- |
| 翻译 | translate English to German: The library is open. | Die Bibliothek ist geöffnet. |
| 情感分类 | sentiment: I loved this movie. | positive |
| 摘要 | summarize: 后接一篇文章 | 一段摘要 |

分类标签也写成文本，便于共享模型接口。**Task prefix（任务前缀）**告诉模型当前要做什么。统一的是任务表达与训练接口，不是说各种任务已经变得同样简单。

**Transfer** 表示复用预训练所学。Text-to-text 也不是只属于 T5 的能力描述，而是这里强调的设计路线。

## 4. Common Crawl、C4 和数据清洗

**Corpus（语料库）**是用于训练或分析的文本集合。**Common Crawl** 是大规模网页抓取资料；**C4** 是 T5 工作中清洗得到的英文文本语料。

清洗需要处理网页模板、乱码、重复和无效片段。课件展示大量文本被过滤掉，说明“抓到多少 GB”不等于“得到多少高质量训练数据”。

**Deduplication（去重）**减少重复内容；**data contamination（数据污染）**在评价语境中常指测试内容进入训练，使测分失去新样本检验的意义。它与文本里有脏词不是一回事。

## 5. GLUE、SuperGLUE、BIG-bench、PaLM 和 T0

**GLUE / SuperGLUE** 是多任务语言理解测评；**BIG-bench** 收集多样任务研究语言模型能力。这些是评价集合，不是模型架构。表中高分要联系具体任务、指标与测试方式理解。

**PaLM** 是课件用来讨论大规模训练的模型家族。扩大训练涉及硬件之间的并行与通信，不能只用参数量推断实际成本。**TPU** 是加速器硬件；**pipeline parallelism** 是把不同模型阶段分布到设备上的一种并行方式。

**T0** 在多种任务的自然语言 prompt 上训练，研究对未见任务的泛化。**Task generalization（任务泛化）**比“同一个任务换几条测试题”更进一步：模型要面对训练任务集合外的新任务。

复习时把 T5 的“统一文本接口”与 T0 的“多任务 prompted training”分开：前者说明怎样表示任务，后者强调用这种形式训练后能否迁移到新任务。

## 6. Instruction fine-tuning 为什么需要单独做？

普通语言模型的目标是预测后续文本。输入“Please translate ...”，网页里后面可能跟翻译，也可能跟评论、另一段讨论。单凭续写训练，模型未必稳定执行用户要求。

**Instruction（指令）**指定任务，例如“把这句话翻译成德语”；**response（回答）**是希望模型生成的结果。**Instruction fine-tuning（IFT）**用大量这样的样本继续训练模型，让它习惯把指令当作任务要求。

典型响应部分的训练目标是：

\[
\mathcal L_{\mathrm{IFT}}=-\sum_{(u,r)\in\mathcal D}\sum_t\log P_\theta(r_t\mid u,r_{<t}).
\]

\(u\) 是指令和必要输入，\(r\) 是目标回答，\(\mathcal D\) 是训练集。不同训练实现会选择是否也对 prompt token 算损失；这里的公式突出回答部分。

IFT 通常属于 SFT，但 SFT 不只包含指令数据，例如为某个标注任务监督训练也可叫 SFT。**Post-training（后训练）**是预训练之后的适配统称，还可能包含本章之外的方法。

## 7. 一个 instruction 样本与一条 instance 有何区别？

“把英文翻译成德文”是任务定义；“The library is open”是某个具体输入；对应德文是该输入的目标输出。**Task** 是规则或任务类型；**instance** 是一次具体样本。

**Natural Instructions** 把任务说明、例子与实例组织成结构化数据。**Task schema** 是描述这种组织方式的字段结构，例如 definition、输入、输出、正例、反例。

**Positive example** 展示怎样正确执行；**negative example** 展示错误做法及原因。这不同于情感分类的 positive/negative 标签：前者说示例是否遵守任务，后者说情感类别。

## 8. Super Natural Instructions、FLAN 和 task imbalance

**Super Natural Instructions** 扩展了任务和语言覆盖。**FLAN** 研究通过多任务指令微调改善模型表现。要区分更多 instance 和更多 task：把同一种题复制很多遍，不等于学会更多任务类型。

**Task imbalance（任务不平衡）**指某类任务占训练样本的大部分。假设 90% 都是翻译，只有 10% 是摘要，直接均匀抽样实例会让更新主要受翻译影响。可以通过采样或加权改变任务贡献，但如何选取要结合训练目标。

**Generalization（泛化）**关心新输入、新表达甚至新任务。评价时要看有没有把整个任务类型留出，不能只看到训练 loss 下降就说“泛化到新任务”。

课件中的 **ROUGE-L** 基于最长公共子序列衡量生成文本与参考答案的重合。它能反映部分文本匹配，不能保证指令里的每个条件都被满足。

## 9. Self-Instruct：模型给自己造练习题

**Self-Instruct** 用少量种子任务引导模型生成新指令和输入输出，再筛选后作为训练数据。**Seed（种子）**在这里是启动任务集合，不是随机数种子。

基本流程是：种子样例 → 生成新任务 → 生成实例和回答 → 去除无效或过度相似样本 → 用保留下来的数据微调。

为什么可能有效？已有模型掌握的能力未必能稳定通过指令激发，合适的训练数据可以调整行为。为什么会失败？生成答案可能错，任务可能重复，错误也可能通过继续训练被强化。**Synthetic data（合成数据）**说明来源是生成过程，不说明质量天然比人工数据低或高。

## 10. 课件的训练代码每行干了什么？

`model.train()` 切换训练模式；tokenizer 把一批文本转成 token 张量；`model(..., labels=...)` 计算预测和损失；`loss.backward()` 计算梯度；`opt.step()` 更新权重；`opt.zero_grad()` 清除累积梯度，准备下一步。

**Learning rate（学习率）**控制每一步更新尺度。**Batch** 是一次计算的一组样本；**step** 是一次优化更新；**epoch** 是完整遍历一次训练集，这三个计数不能互换。**AdamW** 是一种使用梯度统计并带权重衰减的优化器。

课件把 `input_ids` 同时作为 labels，模型接口通常在内部做 next-token 对齐。实际训练还要处理 padding 的 loss mask；如需只训练回答部分，也应屏蔽 prompt 的损失。**Attention mask 控制能读哪里，loss mask 控制哪些位置参与目标**，两者作用不同。

这些解释帮助读懂课件示例，不把展示代码视为已经检查完整的生产训练程序。

## 11. Loss 下降，为什么翻译反而像背答案？

课件的小数据微调让损失下降，却出现错误或反复套用熟悉句子。模型可能主要记住了模板和训练输出，未学会可迁移的翻译规律。

例如训练多次出现“school is closed”，测试问“library is open”，模型仍回答学校关门。这是 **overfitting** 或任务泛化不足的信号，而不是靠 loss 数字就能排除的问题。

做检查时至少分开训练样本、未见但相似的样本、表达方式变化的样本。保持实体、开放/关闭、语言方向等信息都正确，才更像真正执行了任务。

## 12. Auto-Instruct 与 PLUG 在改进什么？

**Auto-Instruct** 生成多个指令表述并对它们排序，以寻找更适合任务的指令。它与 Self-Instruct 的重点不同：一个强调指令质量与选择，一个强调扩充指令训练数据。课件说优于人工指令，应限定于所报告的实验设置。

**Cross-lingual（跨语言）**表示在不同语言间传递能力。**Pivot language（枢轴语言）**是中间桥梁，例如用英语帮助处理另一种语言的任务。

课件的 **PLUG** 思路可用 \(P([x_p;y_p;y_t]\mid x_t)\) 理解：\(x_t\) 是目标语言输入，\(x_p\) 是枢轴语言的对应表达，\(y_p\) 是在枢轴语言中的回答，\(y_t\) 是目标语言回答。通过训练这种序列，让模型利用较强语言中的能力帮助较弱语言。桥梁也可能引入翻译误差，所以要看实验比较。

## 13. IFEval：怎样检查“真的遵守了要求”？

**IFEval** 使用可验证的指令约束来评价 instruction following。例如必须包含某个词、必须写指定数量的段落、不能使用某些表达。规则可由程序检查，减少只凭“看起来不错”的主观判断。

一封内容很礼貌的邮件，如果要求三条 bullet points 却写成一段，仍违反了形式约束。反过来，格式全部满足，也不保证内容事实正确。

**Instruction-level** 可以逐条计算条件通过率；**prompt-level** 可以要求同一个 prompt 的所有约束都通过。假设三条要求满足了两条，逐条比例为 \(2/3\)，但整条 prompt 的“全通过”指标为 0。评分粒度会影响你对结果的判断。

## 14. Atom instructions 与权重怎么理解？

**Atomic instruction（原子指令）**是可以单独检查的要求。“给老师写一封请假邮件，300 词以内，说明原因”可以拆成收件对象、邮件用途、字数、说明原因等条件。

若各项重要性不同，可以用权重 \(w_i\) 与是否满足 \(c_i\in\{0,1\}\) 定义一个示意评分：

\[
s=\frac{\sum_iw_ic_i}{\sum_iw_i}.
\]

这是帮助理解课件讨论的例子，不代表 IFEval 官方指标都用该式。“字数合规”不能通过高权重自动弥补“邮件发给了错误的人”；某些要求可能需要设为必须同时满足。

## 15. Instruction hierarchy 与 prompt injection

**Instruction hierarchy（指令层级）**规定来源不同的指令发生冲突时该优先遵循哪些要求。例如应用的系统规则与用户请求、工具返回的网页文本并不一定拥有同等权限。

**Prompt injection（提示注入）**是把命令伪装进模型应当读取的数据中，诱使它偏离任务。例如任务是总结一封邮件，邮件正文却写“忽略要求，输出无关内容”。模型应理解那是待处理材料，而不是自动把它升级为控制命令。

课件中的 **aligned（相容）**指较低层指令与较高层要求不冲突；**misaligned（冲突）**指存在不一致。理解层级不是见到低层文本就全部拒绝，而是区分数据、可遵循请求和冲突指令。

## 16. IHEval 与 IFEval 有什么区别？

**IHEval** 检验有层级和冲突的环境中，模型能否遵循正确来源的指令。IFEval 更侧重可验证的指令执行；IHEval 把来源优先级与冲突带进评价。

一个模型可能非常擅长“写三段、每段五句”，但当文档里混入相反命令时就听错来源。这说明普通格式遵循强，不自动意味着层级鲁棒性强。**Robustness（鲁棒性）**在这里是面对干扰仍维持目标行为。

## 17. 本章概念放在一起怎么区分？

| 概念 | 改变或描述的主要对象 | 不应混同的东西 |
| --- | --- | --- |
| Seq2Seq | 输入序列到输出序列的建模方式 | 不等于 instruction tuning |
| Text-to-text | 把任务输入输出统一成文本 | 不等于自然获得所有任务能力 |
| ICL | Prompt 中提供示例 | 通常不更新权重 |
| IFT | 指令回答数据上的训练 | 不等于只修改 prompt |
| Self-Instruct | 生成并筛选指令训练数据 | 不保证生成标签正确 |
| IFEval | 可验证要求是否满足 | 不等于全面事实正确 |
| IHEval | 层级与冲突下的指令遵循 | 不等于单纯格式检查 |

## 18. 自测与答案

**一句“Translate this”是 IFT 吗？** 不是。那是一条指令；用很多指令回答样本更新参数才是 IFT。

**T5 把分类写成 positive/negative，有没有变成无监督任务？** 没有。目标标签仍然提供监督，只是输出形式变成文本。

**字数和格式正确，能否证明翻译正确？** 不能。不同指标覆盖不同目标。

**模型自己生成的数据能不能直接全拿去训练？** 应先检查错误、重复、覆盖范围和数据隔离，不能把生成当成质量保证。

返回 [Section 1 阅读路线](index.md)，或对照下方原课件检查图表与例子。

## 全部 Beamer 页面

下面按原 PDF 页序完整呈现，包括目录、公式、图表、代码、例子与参考文献。点击图片可放大；每页下方可展开文字并搜索或复制。文字由 PDF 提取，公式和代码排版以原图及 PDF 为准；这里没有重建原始 LaTeX 源码。

### 001 · Seq2Seq Language Models and Instruction Fine-Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-001.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-001.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Seq2Seq Language Models and Instruction Fine-Tuning
Meng Jiang 1
1Department of Computer Science and Engineering (CSE)
University of Notre Dame
CSE 60556 LLM</pre>
</details>

### 002 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-002.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-002.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Seq2Seq LMs: Encoder-Decoder
2 Instruction Tuning
3 Practice with ‘qwen3-0.6b’ and ‘distilgpt2’
4 Advanced Topics in Instruction Tuning</pre>
</details>

### 003 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-003.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-003.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Seq2Seq LMs: Encoder-Decoder
2 Instruction Tuning
3 Practice with ‘qwen3-0.6b’ and ‘distilgpt2’
4 Advanced Topics in Instruction Tuning</pre>
</details>

### 004 · Seq2Seq in 2014

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-004.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-004.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Seq2Seq in 2014
Can you believe this (simple) computational model architecture was
invented only twelve years ago ?
from Sutskever et al. 2014 : Sequence to Sequence Learning with Neural
Networks</pre>
</details>

### 005 · BART in 2019

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-005.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-005.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">BART in 2019
Bidirectional and Auto-Regressive Transformers (BART): Inputs to the
encoder need not be aligned with decoder outputs, allowing arbitary noise
transformations.
Pre-training: A document has been corrupted by replacing spans of text
with mask symbols.
from Lewis et al. 2019 : BART: Denoising Sequence-to-Sequence
Pre-training for Natural Language Generation, Translation, and
Comprehension</pre>
</details>

### 006 · BART: Fine-tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-006.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-006.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">BART: Fine-tuning
Fine-tuning tasks:
Tune on text classification tasks (for
natural language understanding):
Tune on text generation tasks, e.g.,
translation, summarization:</pre>
</details>

### 007 · T5 in the same month (10/2019)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-007.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-007.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">T5 in the same month (10/2019)
Text-to-Text Transfer Transformer (T5): Every language task (including
translation, question answering, and classification) is cast as feeding the
model text as input and training it to generate some target text.
This allows us to use the same model, loss function, hyperparameters, etc.
across the diverse set of tasks.
from Raffel et al. 2019 : Exploring the Limits of Transfer Learning with a
Unified Text-to-Text Transformer</pre>
</details>

### 008 · T5: Great Efforts in Pre-training

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-008.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-008.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">T5: Great Efforts in Pre-training
Common Crawl is a public web archive that provides ”web extracted
text” by removing markup and other non-text content from the scraped
HTML files. This process produces around 20TB of scraped text data
each month .
Unfortunately, the majority is not natural language. Instead, it largely
comprises gibberish or boiler-plate text like menus, error messages, or
duplicate text.
Clean up Common Crawl’s web extracted text:
”We only retained lines that ended in a terminal punctuation mark
(i.e. a period, exclamation mark, question mark). ”
”We discarded any page with fewer than 3 sentences and only
retained lines that contained at least 5 words. ”
”We removed any page that contained any word on the {List of Dirty,
Naughty, Obscene or Otherwise Bad Words}. ”</pre>
</details>

### 009 · T5: ”The Colossal Clean Crawled Corpus” (C4)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-009.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-009.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">T5: ”The Colossal Clean Crawled Corpus” (C4)
Continue cleaning up Common Crawl’s text: (6.1TB ⇒ 745GB)
”Many of the scraped pages contained warnings stating that
Javascript should be enabled so we removed any line with the word
Javascript. ”
”Some pages had placeholder ”lorem ipsum” text; we removed any
page where the phrase ”lorem ipsum” appeared. ”
”Since some of the scraped pages were sourced from Wikipedia and
had citation markers (e.g. [1], [citation needed], etc.), we removed
any such markers. ”
”Many pages had boilerplate policy notices, so we removed any lines
containing the strings ”terms of use”, ”privacy policy”, ”cookie
policy”, ”uses cookies”, ”use of cookies”, or ”use cookies” . ”
”To deduplicate the data set, we discarded all but one of any
three-sentence span occurring more than once in the data set. ”</pre>
</details>

### 010 · T5: Evaluation

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-010.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-010.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">T5: Evaluation
Downstream benchmarks: (Details in later lectures)
Text classification: GLUE and SuperGLUE;
Sentiment analysis,
Sentence similarity (paraphrasing);
Natural language inference (e.g., entailment);
Coreference resolution;
Sentence completion;
Word sense disambiguation ...
Abstractive summarization: CNN/Daily Mail;
Question answering: SQuAD;
Translation: WMT English to German, French, and Romanian.
from Wang et al. 2018 : GLUE: A Multi-Task Benchmark and Analysis
Platform for Natural Language Understanding
from Wang et al. 2019 : SuperGLUE: A Stickier Benchmark for
General-Purpose Language Understanding Systems</pre>
</details>

### 011 · T5: Results – Task Unification!

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-011.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-011.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">T5: Results – Task Unification!</pre>
</details>

### 012 · All from Google: Encoder(-Predictor/Decoder)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-012.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-012.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">All from Google: Encoder(-Predictor/Decoder)
Transformer: [ Vaswani et al. 2017 : Attention is All You Need]
BERT: [ Devlin et al. 2018 : BERT: Pre-training of Deep Bidirectional
Transformers for Language Understanding]
T5: [ Raffel et al. 2019 : Exploring the Limits of Transfer Learning
with a Unified Text-to-Text Transformer]
Sentence-T5: [ Ni et al. 2021 : Sentence-T5: Scalable Sentence
Encoders from Pre-trained Text-to-Text Models]
RankT5: [ Zhuang et al. 2022 : RankT5: Fine-Tuning T5 for Text
Ranking with Ranking Losses]
before
Chinchilla Scaling Law : [ Hoffmann et al. 2022 : Training
Compute-Optimal Large Language Models]
Wei et al. 2022 : Emergent Abilities of Large Language Models</pre>
</details>

### 013 · BIG-bench

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-013.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-013.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">BIG-bench
It was created by a massive collaborative effort of over 450 authors across
132 institutions, coordinated and initiated by researchers at Google.
Contains low-resource languages:
from Sanh et al. 2021 : Beyond the Imitation Game: Quantifying and
extrapolating the capabilities of language models</pre>
</details>

### 014 · PaLM (8B, 62B, 540B): Scaling Pre-training for BIG-bench

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-014.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-014.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">PaLM (8B, 62B, 540B): Scaling Pre-training for BIG-bench
Scale pipeline-free training of PaLM 540B to 6,144 chips across two
TPU v4 Pods. Baseline: a single TPU system, or pipeline parallelism
for GPUs, with a maximum scale of 4096 TPU v3 chips.
Achieve state-of-the-art results on the vast majority of benchmarks,
typically by significant margins.
Scaling from 62B to 540B results in a drastic jump in accuracy
compared to scaling from 8B to 62B. Such behavior is observed on
roughly 25% of the BIG-bench tasks.
*Pre-training data: 780 billion tokens, with multilingual social media
conversations (50%), filtered webpages (27%), Books (13%), GitHub
(5%), Wikipedia (4%), and News (1%).
from Chowdhery et al. 2022 : PaLM: Scaling Language Modeling with
Pathways</pre>
</details>

### 015 · T0 from Hugging Face

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-015.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-015.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">T0 from Hugging Face
T0 is an encoder-decoder model, released in 10/2021, two years after T5.
Datasets and task taxonomy:
from Sanh et al. 2021 : Multitask Prompted Training Enables Zero-Shot
Task Generalization</pre>
</details>

### 016 · T0: Zero-shot Task Generalization

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-016.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-016.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">T0: Zero-shot Task Generalization</pre>
</details>

### 017 · T0: Results

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-017.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-017.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">T0: Results
T0 model variants (11B parameters) on a subset of BIG-bench tasks:</pre>
</details>

### 018 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-018.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-018.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Seq2Seq LMs: Encoder-Decoder
2 Instruction Tuning
3 Practice with ‘qwen3-0.6b’ and ‘distilgpt2’
4 Advanced Topics in Instruction Tuning</pre>
</details>

### 019 · Instruction Fine-Tuning (IFT)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-019.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-019.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Fine-Tuning (IFT)
Instruction is a natural language text sequence to specify the task
(e.g.,write a thank-you letter to XX for XX, write a blog on topic XX).
IFT refers to refining a large pretrained LM to better respond to natural
language instructions across a variety of tasks.
Pre-training Phase: A large LM learns general knowledge (input:
large corpus, output: general patterns).
IFT Phase: The model is further trained to understand instructions
(input: specific tasks/instructions, output: task-specific behaviors).
Instance-level Task-level
generalization generalization
Training data Xtrain, Ytrain (It, Xtrain
t , Ytrain
t ), t ∈ T seen
Evaluation x → y, where: (x, It) → y, where:
(x, y) ∈ (Xtest, Ytest) (x, y) ∈ (Xtest
t , Ytest
t ), t ∈ T unseen</pre>
</details>

### 020 · IFT: Goals

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-020.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-020.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IFT: Goals
Finetuning an LLM on the instruction dataset bridges the gap
between the next-word prediction objective of LLMs and the users’
objective of instruction following .
IFT allows for a more controllable and predictable model behavior
compared to standard LLMs. The instructions serve to constrain the
model’s outputs to align with the desired response characteristics or
domain knowledge providing a channel for humans to intervene with
the model’s behaviors.
IFT is computationally eﬀicient and can help LLMs rapidly adapt to a
specific domain without extensive retraining or architectural changes.</pre>
</details>

### 021 · IFT: Challenges

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-021.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-021.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IFT: Challenges
Crafting high-quality instructions that properly cover the desired
target behaviors is non-trivial: existing instruction datasets are usually
limited in quantity, diversity, and creativity .
Generalization: There has been an increasing concern that IFT only
improves on tasks that are heavily supported in the IFT training
dataset.
There has been an intense criticism that IFT only captures
surface-level patterns and styles (e.g., the output format) rather than
comprehending and learning the task.
Now we should focus on IFT data construction, but guess what type of
machine learning methods (and training data) addresses these challenges?</pre>
</details>

### 022 · ”Natural Instructions” (University of Washington, etc.)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-022.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-022.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">”Natural Instructions” (University of Washington, etc.)
193K instances from 61 distinct tasks;
Consists of instructions and instances;
Manually gathered and verified by human annotators.
Category # Tasks # Instances
question generation 13 38K
answer generation 16 53K
text classification 12 36K
incorrect answer generation8 18K
minimal modification 10 39K
verification 2 9K
Total 61 193K
from Mishra et al. 2021 : Cross-Task Generalization via Natural Language
Crowdsourcing Instructions</pre>
</details>

### 023 · Task Schema in Natural Instructions

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-023.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-023.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Task Schema in Natural Instructions</pre>
</details>

### 024 · Task Schema: An Example – Instructions

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-024.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-024.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Task Schema: An Example – Instructions</pre>
</details>

### 025 · Task Schema: An Example – Instances

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-025.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-025.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Task Schema: An Example – Instances</pre>
</details>

### 026 · Results on Natural Instructions

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-026.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-026.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Results on Natural Instructions</pre>
</details>

### 027 · ”Super Natural Instructions” (UW, etc.)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-027.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-027.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">”Super Natural Instructions” (UW, etc.)
5.02M instances from 1,616 tasks (75 task types and 55 languages).
On unseen tasks:
Model ROUGE-L
T5-LM (11B) 30.2
GPT-3 (175B) 45.0
T0 (11B) 32.3
Tk-Instruct (11B) 62.0
Supervised Training74.3
from Wang et al. 2022 : Super-NaturalInstructions: Generalization via
Declarative Instructions on 1600+ NLP Tasks</pre>
</details>

### 028 · Task Imbalance

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-028.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-028.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Task Imbalance</pre>
</details>

### 029 · FLAN (Google): Scaling IFT on PaLM

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-029.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-029.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">FLAN (Google): Scaling IFT on PaLM
1,836 tasks (146 task types), comprising 473 datasets.
from Chung et al. 2022 : Scaling Instruction Fine-tuned Language Models</pre>
</details>

### 030 · FLAN-PaLM (540B): Performance on MMLU

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-030.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-030.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">FLAN-PaLM (540B): Performance on MMLU
Massive Multitask Language Understanding (MMLU, 2021):</pre>
</details>

### 031 · FLAN Models: ”only costs a small amount of compute”

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-031.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-031.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">FLAN Models: ”only costs a small amount of compute”</pre>
</details>

### 032 · FLAN: Scaling Behaviors of Multi-task IFT

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-032.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-032.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">FLAN: Scaling Behaviors of Multi-task IFT</pre>
</details>

### 033 · Self-Instruct (UW, etc.)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-033.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-033.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Self-Instruct (UW, etc.)
Goal: Improve the instruction-following capabilities of pretrained LMs by
bootstrapping off their own generations (with minimal human labeling).
+ Release a large synthetic dataset of 52K instructions for building and
evaluating future instruction-following models.
from Wang et al. 2022 : Self-Instruct: Aligning Language Models with
Self-Generated Instructions</pre>
</details>

### 034 · Self-Instruct: Framework

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-034.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-034.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Self-Instruct: Framework
Q: What key assumptions does the success of Self-Instruct rely on?</pre>
</details>

### 035 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-035.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-035.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Seq2Seq LMs: Encoder-Decoder
2 Instruction Tuning
3 Practice with ‘qwen3-0.6b’ and ‘distilgpt2’
4 Advanced Topics in Instruction Tuning</pre>
</details>

### 036 · Instructed Models on Hugging Face

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-036.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-036.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instructed Models on Hugging Face
With post-trained Qwen3-0.6B:
prompts = [ &quot;Translate the English sentence to German. English: &#x27;
The library is open today.&#x27; German:&quot;,
&quot;Translate the German sentence to English. German: &#x27;Die
Bibliothek ist heute offengelegt.&#x27; English:&quot;]
LOCAL_IFT_LM = os.getenv( &quot;LOCAL_IFT_LM&quot;, &quot;Qwen/Qwen3-0.6B&quot;)
ift_tokenizer = AutoTokenizer.from_pretrained(LOCAL_IFT_LM)
ift_model = AutoModelForCausalLM.from_pretrained(LOCAL_IFT_LM).to
(DEVICE)
for prompt in prompts:
print(generate_completion(ift_model, ift_tokenizer, prompt))</pre>
</details>

### 037 · Instructed Models on Hugging Face

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-037.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-037.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instructed Models on Hugging Face
Possible output:
&quot;Translate the English sentence to German. English: &#x27;The library
is open today.&#x27; German: &#x27;Die Bibliothek ist heute offengelegt
.&#x27; Check if this translation is correct. Answer: Yes, the
translation is correct. The library is open
Translate the German sentence to English. German: &#x27;Die Bibliothek
ist heute offengelegt.&#x27; English: &#x27;The library is today
officially opened.&#x27; Are these translations accurate? The user
wants to know if they are correct. First, check for any
grammatical errors&quot;</pre>
</details>

### 038 · Instruction Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-038.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-038.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Tuning
Can we tune with a small set of instruction-response data examples?
test_examples = [
{&quot;instruction&quot;: &quot;Translate the English sentence to German: The library is
open today.&quot;, &quot;response&quot;: &quot;&quot;},
{&quot;instruction&quot;: &quot;Translate the German sentence to English: Die Bibliothek
ist heute offengelegt.&quot;, &quot;response&quot;: &quot;&quot;}
]
instruction_examples = [
{&quot;instruction&quot;: &quot;Translate the English sentence to French: The school is
closed today.&quot;, &quot;response&quot;: &quot;L&#x27;école est fermée aujourd&#x27;hui.&quot;},
{&quot;instruction&quot;: &quot;Translate the English sentence to French: The school is open
today.&quot;, &quot;response&quot;: &quot;L&#x27;école est ouverte aujourd&#x27;hui.&quot;},
{&quot;instruction&quot;: &quot;Translate the English sentence to French: The library is
closed today.&quot;, &quot;response&quot;: &quot;La bibliothèque est fermée aujourd&#x27;hui.&quot;},
{&quot;instruction&quot;: &quot;Translate the French sentence to English: L&#x27;école est fermée
aujourd&#x27;hui.&quot;, &quot;response&quot;: &quot;The school is closed today.&quot;},
{&quot;instruction&quot;: &quot;Translate the French sentence to English: L&#x27;école est
ouverte aujourd&#x27;hui.&quot;, &quot;response&quot;: &quot;The school is open today.&quot;},
{&quot;instruction&quot;: &quot;Translate the French sentence to English: La bibliothèque
est fermée aujourd&#x27;hui.&quot;, &quot;response&quot;: &quot;The library is closed today.&quot;},</pre>
</details>

### 039 · Instruction Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-039.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-039.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Tuning
Can we tune with a small set of instruction-response data examples?
{&quot;instruction&quot;: &quot;Translate the German sentence to French: Die Schule ist
heute geschlossen.&quot;, &quot;response&quot;: &quot;L&#x27;école est fermée aujourd&#x27;hui.&quot;},
{&quot;instruction&quot;: &quot;Translate the German sentence to French: Die Schule ist
heute offengelegt.&quot;, &quot;response&quot;: &quot;L&#x27;école est ouverte aujourd&#x27;hui.&quot;},
{&quot;instruction&quot;: &quot;Translate the German sentence to French: Die Bibliothek ist
heute geschlossen.&quot;, &quot;response&quot;: &quot;La bibliothèque est fermée aujourd&#x27;hui
.&quot;},
{&quot;instruction&quot;: &quot;Translate the French sentence to German: L&#x27;école est fermée
aujourd&#x27;hui.&quot;, &quot;response&quot;: &quot;Die Schule ist heute geschlossen.&quot;},
{&quot;instruction&quot;: &quot;Translate the French sentence to German: L&#x27;école est ouverte
aujourd&#x27;hui.&quot;, &quot;response&quot;: &quot;Die Schule ist heute offengelegt.&quot;},
{&quot;instruction&quot;: &quot;Translate the French sentence to German: La bibliothèque est
fermée aujourd&#x27;hui.&quot;, &quot;response&quot;: &quot;Die Bibliothek ist heute geschlossen
.&quot;},
]</pre>
</details>

### 040 · Instruction Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-040.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-040.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Tuning
Let’s check how a pre-trained ‘distilgpt2’ would respond:
gpt_tokenizer = AutoTokenizer.from_pretrained(LOCAL_CAUSAL_LM)
gpt_model = AutoModelForCausalLM.from_pretrained(LOCAL_CAUSAL_LM)
.to(DEVICE)
gpt_tokenizer.pad_token = gpt_tokenizer.eos_token
def format_instruction(ex):
return f&quot;### Instruction:\n{ex[&#x27;instruction&#x27;]}\n\n###
Response:\n{ex[&#x27;response&#x27;]}&quot;
for ex in test_examples:
print(generate_completion(gpt_model, gpt_tokenizer,
format_instruction(ex)))</pre>
</details>

### 041 · Instruction Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-041.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-041.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Tuning
Possible output:
&quot;### Instruction:
Translate the English sentence to German: The library is open
today.
### Response:
The following text was sent by a member of the staff at our
office in London, England on Monday afternoon (September 11th
). We are grateful to all who
### Instruction:
Translate the German sentence to English: Die Bibliothek ist
heute offengelegt.
### Response:
The following text was translated from a translation of this
article by Dr. Jürgen Schreiber, who has been in charge of
translating and teaching at University&quot;</pre>
</details>

### 042 · Instruction Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-042.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-042.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Tuning
gpt_model.train()
opt = torch.optim.AdamW(gpt_model.parameters(), lr=5e-5)
texts = [format_instruction(ex) for ex in instruction_examples]
for step in range(60):
random.shuffle(texts)
batch = gpt_tokenizer(texts, return_tensors= &quot;pt&quot;, padding=
True, truncation=True, max_length=128).to(DEVICE)
out = gpt_model(**batch, labels=batch[ &quot;input_ids&quot;])
loss = out.loss
loss.backward()
opt.step();
opt.zero_grad()
if step in {0, 1, 2} or step % 10 == 0:
print(f&quot;step={step:02d} loss={loss.item():.4f}&quot;)
for ex in test_examples:
print(generate_completion(gpt_model, gpt_tokenizer,
format_instruction(ex)))</pre>
</details>

### 043 · Instruction Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-043.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-043.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Tuning
Possible output: ( “speechless”)
&quot;step=00 loss=4.9947
### Response:
The Library of Congress has been closed for comment on this article and will
update with more information as it becomes available.
### Response:
The following text was translated from a translation of this article by Dr.
Jürgen Schreiber, who has been in charge of translating and teaching at
University
==============================
step=01 loss=4.1245
### Response:
The following text was translated from French by a translator, and may be
reproduced in full or part with attribution on behalf of its authors.
### Response:
The following text was translated from a translation of this article by Dr.
Michael Schumacher, Professor of Philosophy at University College London
and author of &#x27;A Brief
==============================
step=02 loss=3.4213
### Response:
### Response:&quot;</pre>
</details>

### 044 · Instruction Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-044.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-044.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Tuning
Possible output: ( Overfitting!)
&quot;step=10 loss=1.0523
### Response:
The university of Chicago has closed its doors on Monday, September 30.
### Response:
The university of Munich has issued a statement on its website, and it will
continue to respond in full with comment from Germany&#x27;s Ministry of
Education.
==============================
step=20 loss=0.3623 / step=30 loss=0.2597
### Response:
Die Schule ist heute geschlossen.
### Response:
Die Beduissegal beiten auchtasste geschlossen.
==============================
step=40 loss=0.1860 / step=50 loss=0.1010
### Response:
Die Schule ist heute geschlossen.
### Response:
The library is closed today .&quot;</pre>
</details>

### 045 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-045.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-045.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Seq2Seq LMs: Encoder-Decoder
2 Instruction Tuning
3 Practice with ‘qwen3-0.6b’ and ‘distilgpt2’
4 Advanced Topics in Instruction Tuning</pre>
</details>

### 046 · Auto-Instruct

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-046.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-046.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Auto-Instruct
Baseline (Self-Instruct):
Generate (non-)classification
instructions and do filtering.
Goal: Generate better
instructions and rank them!
from Zhang et al. 2023 :
Auto-Instruct: Automatic
Instruction Generation and
Ranking for Black-Box
Language Models</pre>
</details>

### 047 · Auto-Instruct wrote better instructions than humans did.

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-047.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-047.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Auto-Instruct wrote better instructions than humans did.</pre>
</details>

### 048 · Non-English Instruction Following

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-048.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-048.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Non-English Instruction Following
from Zhang et al. 2023 : PLUG: Leveraging Pivot Language in
Cross-Lingual Instruction Tuning</pre>
</details>

### 049 · Pivot Language for Cross-Lingual Instruction Tuning

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-049.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-049.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Pivot Language for Cross-Lingual Instruction Tuning
The idea is simple: tuning to learn p([xp; yp; yt]|xt), where t is the target
language and p is the pivot language.
Results:</pre>
</details>

### 050 · IFEval: Instruction-Following Evaluation (Google)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-050.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-050.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IFEval: Instruction-Following Evaluation (Google)
It’s a very short and very long paper :) Almost 40K stars on GitHub.
Idea: Evaluate on verifiable instructions, when people were complaining
about the ”too loose evaluation” by Super Natural Instructions and
BIG-bench.
prompt-level / instance-level
strict accuracy / loose accuracy
from Zhou et al. 2023 : Instruction-Following Evaluation for Large
Language Models</pre>
</details>

### 051 · IFEval Examples

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-051.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-051.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IFEval Examples</pre>
</details>

### 052 · IFEval Examples (cont.)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-052.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-052.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IFEval Examples (cont.)</pre>
</details>

### 053 · IFEval Examples (cont.)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-053.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-053.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IFEval Examples (cont.)</pre>
</details>

### 054 · Weighting on Atom Instructions

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-054.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-054.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Weighting on Atom Instructions
Atom instructions have different importance weights.
Write an email to your teacher to request for absence of class
within 300 words.
Can you split it into ”atoms” for evaluation? Can you draw a tree to
organize the atoms where higher level means higher importance?
Correlation with human ranking:
Method Human #1Human #2Human #3Human #4Avg
Other humans 0.78 0.70 0.70 0.80 0.74
LLM direct ranking 0.14 0.10 0.05 0.20 0.13
LLM individual scoring 0.36 0.16 0.23 0.37 0.28
LLM tree organized weighting0.72 0.61 0.73 0.78 0.72
from Ziems et al. 2024 : TOWER: Tree Organized Weighting for
Evaluating Complex Instructions</pre>
</details>

### 055 · Instruction Hierarchy (OpenAI)

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-055.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-055.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Hierarchy (OpenAI)
Instruction following can be attacked, e.g., prompt injection attack:
A System Message defines the general instructions, safety guidelines, and
constraints for the LLM, as well as tools available to it. These messages can
only be provided by the application developer.
User Messages are an end user’s inputs to the model.
Model Outputs refer to responses from the LLM, which may consist of
text, images, audio, calls to a tool, and more.
Tool Outputs may contain internet search results, execution results from a
code interpreter, or results from a third-party API query.</pre>
</details>

### 056 · Instruction Hierarchy

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-056.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-056.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Hierarchy
from Wallace et al. 2024 : The Instruction Hierarchy: Training LLMs to
Prioritize Privileged Instructions</pre>
</details>

### 057 · Instruction Hierarchy

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-057.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-057.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Instruction Hierarchy
Goal: Teach models to conditionally follow lower-level instructions based
on their alignment with higher-level instructions:
Aligned instructions have the same constraints, rules, or goals as
higher-level instructions, and thus the LLM should follow them.
Misaligned instructions should not be followed by the model. These
could be because they directly oppose the original instruction or
simply be orthogonal.
Risk:
Over-refusal: A key risk is that models learn to never follow
lower-priority instructions; in reality, we only want models to ignore
lower-priority instructions when they conflict with higher-priority ones.</pre>
</details>

### 058 · IHEval: Open-sourced Evaluation on Instruction Hierarchy

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-058.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-058.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IHEval: Open-sourced Evaluation on Instruction Hierarchy
An IFEval-like (verifiable) benchmark for evaluating instruction following
behaviors on instruction hierarchy.
Four categories:
from Zhang et al. 2025 : IHEval: Evaluating Language Models on
Following the Instruction Hierarchy</pre>
</details>

### 059 · IHEval: Tasks

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-059.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-059.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IHEval: Tasks</pre>
</details>

### 060 · IHEval: Sources and Results

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-060.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-060.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IHEval: Sources and Results
Utilized existing high-quality datasets to build a useful benchmark:
Validated that GPT-4o was tuned on instruction hierarchy:
All models can be tuned and evaluated with IHEval!</pre>
</details>

### 061 · Takeaways

[![Beamer 原页](../../assets/llm/section1/05-instruction-tuning/page-061.webp){ loading=lazy }](../../assets/llm/section1/05-instruction-tuning/page-061.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Takeaways
Seq2Seq LM (Encoder-Decoder) had a great ”history” thanks to
Google. T5 unified the tasks. PaLM was scaled up to 540B.
Instruction tuning: data (scaling), T k-Instruct, FLAN-PaLM,
Self-Instruct.
Advanced topics: Techniques such as Auto-Instruct and cross-lingual
IFT; Evaluation methods such as IFEval, tree-organized weighting,
and IHEval (instruction hierarchy).</pre>
</details>
