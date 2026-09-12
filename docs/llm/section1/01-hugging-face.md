# Hugging Face Transformers 总览

[返回 Section 1](index.md)

授课课件：Meng Jiang · CSE 60556 · Fall 2026。来源 `Chapter1-L00 (L02).pdf`，共 **38 页**。

[下载完整原课件 PDF](../../assets/llm/section1/01-hugging-face/slides.pdf)


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

## 全部 Beamer 页面

下面按原 PDF 页序完整呈现，包括目录、公式、图表、代码、例子与参考文献。点击图片可放大；每页下方可展开文字并搜索或复制。文字由 PDF 提取，公式和代码排版以原图及 PDF 为准；这里没有重建原始 LaTeX 源码。

### 001 · Hugging Face Transformers

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-001.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-001.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Hugging Face Transformers
Inference or Training with State-of-the-art Pretrained Models
Meng Jiang 1
1Department of Computer Science and Engineering (CSE)
University of Notre Dame
CSE 60556 LLM</pre>
</details>

### 002 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-002.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-002.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Masked LMs
2 Causal LMs
3 Scaling Laws and ”Large” Language Models
4 Seq2Seq LMs
5 Instruction Fine-Tuning</pre>
</details>

### 003 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-003.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-003.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Masked LMs
2 Causal LMs
3 Scaling Laws and ”Large” Language Models
4 Seq2Seq LMs
5 Instruction Fine-Tuning</pre>
</details>

### 004 · Word Embeddings via Masked Word Prediction

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-004.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-004.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Word Embeddings via Masked Word Prediction
Shallow neural networks can learn vector representations of words,
sentences, and documents using tasks such as masked word prediction.
word2vec: [ Mikolov et al. 2013 : Distributed Representations of
Words and Phrases and their Compositionality]
GloVe: [ Pennington et al. 2014 : GloVe: Global Vectors for Word
Representation]
Paragraph Vector: [ Le and Mikolov 2014 : Distributed
Representations of Sentences and Documents]</pre>
</details>

### 005 · Transformers on Hugging Face

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-005.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-005.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Transformers on Hugging Face
Transformers* are way more complex and expressive than shallow neural
networks. Hugging Face Transformers (”transformers”) offers a
PyTorch-based framework to easily use this specific complex neural
network architecture.
*Transformer: [ Vaswani et al. 2017 : Attention is All You Need]
import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import (
AutoTokenizer, AutoModel, AutoModelForMaskedLM,
AutoModelForCausalLM, AutoModelForSeq2SeqLM, pipeline,
set_seed,
)
set_seed(42)
DEVICE = &quot;cuda&quot; if torch.cuda.is_available() else &quot;cpu&quot;</pre>
</details>

### 006 · Three Types of Transformer-based Language Models

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-006.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-006.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Three Types of Transformer-based Language Models
Get their environments before we introduce them :)
Masked LM: BERT* family (mainly encoder-only), including
DistilRoBERTa
Causal LM: GPT** family (mainly decoder-only), including
DistilGPT2
Seq2Seq LM: T5*** (encoder-decoder)
LOCAL_MASKED_LM = os.getenv( &quot;LOCAL_MASKED_LM&quot;, &quot;distilroberta-
base&quot;)
LOCAL_CAUSAL_LM = os.getenv( &quot;LOCAL_CAUSAL_LM&quot;, &quot;distilgpt2&quot;)
LOCAL_SEQ2SEQ_LM = os.getenv( &quot;LOCAL_SEQ2SEQ_LM&quot;, &quot;t5-small&quot;)
*BERT: Bidirectional Encoder Representations from Transformers
**GPT: Generative Pre-trained Transformers
***T5: Text-to-Text Transfer Transformers</pre>
</details>

### 007 · Three Architectures

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-007.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-007.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Three Architectures
(If Encoder exists, there is representation of sequence .)
Encoder-only (Masked LM):
Encoder-decoder (Seq2Seq LM):
Decoder-only (Causal LM):</pre>
</details>

### 008 · Tokenization

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-008.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-008.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Tokenization
Each model uses a tokenizer to process text.
text = &quot;Transformers in Hugging Face make it easy to reuse
pretrained language models.&quot;
bert_tokenizer = AutoTokenizer.from_pretrained(LOCAL_MASKED_LM)
bert_model = AutoModel.from_pretrained(LOCAL_MASKED_LM).to(DEVICE
)
inputs = bert_tokenizer(text, return_tensors= &quot;pt&quot;).to(DEVICE)
with torch.no_grad():
outputs = bert_model(**inputs)
print(&quot;Input tokens:&quot;, bert_tokenizer.convert_ids_to_tokens(
inputs[&quot;input_ids&quot;][0]))
print(&quot;Last hidden state shape:&quot;, tuple(outputs.last_hidden_state
.shape))
print(&quot;[CLS]-like vector shape:&quot;, tuple(outputs.last_hidden_state
[:, 0, :].shape))</pre>
</details>

### 009 · Hidden State

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-009.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-009.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Hidden State
The model’s last hidden state is a tensor with dimensions corresponding to
the number of tokens and embedding size.
The ‘[CLS]‘ vector is often used as a sequence-level representation for
downstream tasks such as classification or semantic similarity.
Output:
Input tokens: [ &#x27;&lt;s&gt;&#x27;, &#x27;Transform&#x27;, &#x27;ers&#x27;, &#x27;Ġin&#x27;, &#x27;ĠHug&#x27;, &#x27;ging&#x27;,
&#x27;ĠFace&#x27;, &#x27;Ġmake&#x27;, &#x27;Ġit&#x27;, &#x27;Ġeasy&#x27;, &#x27;Ġto&#x27;, &#x27;Ġreuse&#x27;, &#x27;Ġpret&#x27;, &#x27;
rained&#x27;, &#x27;Ġlanguage&#x27;, &#x27;Ġmodels&#x27;, &#x27;.&#x27;, &#x27;&lt;/s&gt;&#x27;]
Last hidden state shape: (1, 18, 768)
[CLS]-like vector shape: (1, 768)</pre>
</details>

### 010 · Masked Token Prediction

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-010.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-010.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Masked Token Prediction
mlm = pipeline( &quot;fill-mask&quot;, model=LOCAL_MASKED_LM, tokenizer=
LOCAL_MASKED_LM, device=0 if DEVICE == &quot;cuda&quot; else -1)
mask = mlm.tokenizer.mask_token
for r in mlm(f&quot;A Transformer model can learn useful {mask}
representations.&quot;)[:5]:
print(f&quot;{r[&#x27;token_str&#x27;]:&gt;12s} score={r[&#x27;score&#x27;]:.3f}&quot;)
Output:
mathematical score=0.066
semantic score=0.053
geometric score=0.043
graphical score=0.029
visual score=0.025</pre>
</details>

### 011 · Masked Token Prediction

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-011.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-011.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Masked Token Prediction
mlm = pipeline( &quot;fill-mask&quot;, model=LOCAL_MASKED_LM, tokenizer=
LOCAL_MASKED_LM, device=0 if DEVICE == &quot;cuda&quot; else -1)
for r in mlm(f&quot;A Transformer model {mask} learn useful
representations.&quot;)[:5]:
print(f&quot;{r[&#x27;token_str&#x27;]:&gt;12s} score={r[&#x27;score&#x27;]:.3f}&quot;)
Output:
can score=0.320
will score=0.226
could score=0.123
helps score=0.108
to score=0.070</pre>
</details>

### 012 · Dive Deep into Masked LMs

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-012.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-012.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Dive Deep into Masked LMs
Learning Goals: (a) Get to know the Transformer architecture; (b) Get to
know models in the BERT family, such as:
BERT: [ Devlin et al. 2018 : BERT: Pre-training of Deep Bidirectional
Transformers for Language Understanding]
BioBERT: [ Lee et al. 2019 : BioBERT: A Pre-trained Biomedical
Language Representation Model for Biomedical Text Mining]
SciBERT: [ Beltagy et al. 2019 : SciBERT: A Pre-trained Language
Model for Scientific Text]
Sentence-BERT: [ Reimers et al. 2019 : Sentence-BERT: Sentence
Embeddings using Siamese BERT-Networks]</pre>
</details>

### 013 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-013.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-013.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Masked LMs
2 Causal LMs
3 Scaling Laws and ”Large” Language Models
4 Seq2Seq LMs
5 Instruction Fine-Tuning</pre>
</details>

### 014 · GPT Completes Sentences

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-014.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-014.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT Completes Sentences
prompts = [ &quot;In one sentence, GPT is&quot;, &quot;In one sentence, BERT is&quot;]
gpt_tokenizer = AutoTokenizer.from_pretrained(LOCAL_CAUSAL_LM)
gpt_model = AutoModelForCausalLM.from_pretrained(LOCAL_CAUSAL_LM)
.to(DEVICE)
gpt_tokenizer.pad_token = gpt_tokenizer.eos_token
def generate_completion(model, tokenizer, prompt, max_new_tokens
=32):
model.eval()
batch = tokenizer(prompt, return_tensors= &quot;pt&quot;).to(DEVICE)
with torch.no_grad():
out = model.generate(**batch, ...)
return tokenizer.decode(out[0], skip_special_tokens=True)
for prompt in prompts:
print(&#x27;==&gt;&#x27;, generate_completion(gpt_model, gpt_tokenizer,
prompt))</pre>
</details>

### 015 · GPT Completes Sentences

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-015.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-015.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT Completes Sentences
Potential output:
&quot;==&gt; In one sentence, GPT is a form of “a state-‑ofthe-art
”system that allows the government to control its own
activities. The new law will also
==&gt; In one sentence, BERT is a man who has been accused of raping
and murdering two women in the past. The victim was found
dead on her way home from work at around 8am&quot;</pre>
</details>

### 016 · Fine-Tuning GPTs

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-016.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-016.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Fine-Tuning GPTs
Can we fine-tune with a small set of examples (p=prompt, c=completion)?
tune_data = [
(&quot;In one sentence, a Transformer is&quot;, &quot; a neural network architecture that
uses self-attention to model relationships among tokens in a sequence.&quot;)
,
(&quot;In one sentence, self-attention is&quot;, &quot; a mechanism that lets each token
weigh other tokens when building its contextual representation.&quot;),
(&quot;In one sentence, a language model is&quot;, &quot; a model trained to predict or
generate text by estimating likely token sequences.&quot;),
(&quot;In one sentence, BERT is&quot;, &quot; an encoder-only Transformer model designed to
produce contextual representations of text.&quot;),
(&quot;In one sentence, GPT is&quot;, &quot; a decoder-only Transformer model trained to
generate text from left to right.&quot;),
(&quot;In one sentence, LoRA is&quot;, &quot; a parameter-efficient fine-tuning method that
learns small low-rank adapter matrices instead of updating all weights.&quot;
),
(&quot;In one sentence, quantization is&quot;, &quot; a compression technique that stores
model weights or activations with fewer bits to reduce memory use.&quot;),
(&quot;In one sentence, instruction tuning is&quot;, &quot; supervised fine-tuning on
instruction-response examples so a model learns to follow user requests.
&quot;),
]</pre>
</details>

### 017 · Fine-Tuning GPTs

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-017.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-017.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Fine-Tuning GPTs
Fine-tuning only the last layer of ‘distilgpt2‘ with a small set of examples
is relatively inexpensive. In contrast, fully supervised fine-tuning (SFT) a
large GPT model on a large dataset can be computationally costly.
tune_texts = [p + c + gpt_tokenizer.eos_token for p, c in
tune_data] * 4
for step in range(TUNE_STEPS):
texts = ... (tune_texts)
batch = gpt_tokenizer(texts, return_tensors= &quot;pt&quot;, padding=
True, truncation=True, max_length=96).to(DEVICE)
outputs = gpt_model(**batch, labels=batch[ &quot;input_ids&quot;])
loss = outputs.loss
loss.backward()
torch.nn.utils.clip_grad_norm_([p for p in gpt_model.
parameters() if p.requires_grad], 1.0)
optimizer.step()
optimizer.zero_grad()</pre>
</details>

### 018 · Fine-Tuning GPTs

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-018.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-018.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Fine-Tuning GPTs
Monitor the optimization process:
# prompts = [&quot;In one sentence, GPT is&quot;,
# &quot;In one sentence, BERT is&quot;]
{for ...:}
if step in {0, 1, 2, TUNE_STEPS - 1} or (step + 1) % 8 == 0:
print(&#x27;=&#x27;*30)
print(f&quot;step {step + 1:03d}/{TUNE_STEPS} | loss = {loss.
item():.4f}&quot;)
for prompt in prompts:
print(&#x27;==&gt;&#x27;, generate_completion(gpt_model,
gpt_tokenizer, prompt))
Possible output:
&quot;step 001/64 | loss = 5.8969
==&gt; In one sentence, GPT is a form of “a state-‑ofthe-art ”system that allows
the government to control its own activities. The first step in this
==&gt; In one sentence, BERT is a man who has been accused of raping and murdering
two women in the past. The victim was found dead on her way home from work
at around 8am&quot;</pre>
</details>

### 019 · Fine-Tuning GPTs

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-019.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-019.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Fine-Tuning GPTs
Possible output (continued):
&quot;step 003/64 | loss = 5.2965
==&gt; In one sentence, GPT is a form of “a state-‑ofthe-art ”system that allows
the government to control its own activities. The first step in this
==&gt; In one sentence, BERT is a man who has been accused of raping and murdering
two women in the past. The victim was found dead on her way home from work
at around 8am
==============================
step 008/64 | loss = 4.7318
==&gt; In one sentence, GPT is a form of &#x27;-
==&gt; In one sentence, BERT is a &#x27;suspect&#x27; and an enemy.
==============================
step 016/64 | loss = 2.9686
==&gt; In one sentence, GPT is a form of &#x27;
==&gt; In one sentence, BERT is a model-model that uses models to generate text.
==============================
step 024/64 | loss = 1.6772
==&gt; In one sentence, GPT is a model-based approach that uses models to generate
text from structured representations.
==&gt; In one sentence, BERT is a model trained to generate text from structured
representations.&quot;</pre>
</details>

### 020 · Fine-Tuning GPTs

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-020.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-020.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Fine-Tuning GPTs
Possible output (continued):
&quot;step 032/64 | loss = 0.6785
==&gt; In one sentence, GPT is a model trained to predict or generate text by
estimating likely token sequences.
==&gt; In one sentence, BERT is a model trained to predict or generate text by
estimating likely token sequences.
==============================
step 040/64 | loss = 0.2208
==&gt; In one sentence, GPT is a decoder-only Transformer model trained to generate
text from left to right.
==&gt; In one sentence, BERT is a decoder-only Transformer model trained to
generate text from left to right.
==============================
step 048/64 | loss = 0.0903
==&gt; In one sentence, GPT is a decoder-only Transformer model trained to generate
text from left to right.
==&gt; In one sentence, BERT is a parameter-efficient fine-tuning method that
learns small low-rank adapter matrices instead of updating all weights.&quot;</pre>
</details>

### 021 · Fine-Tuning GPTs

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-021.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-021.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Fine-Tuning GPTs
Possible output (finally):
&quot;step 056/64 | loss = 0.0813
==&gt; In one sentence, GPT is a decoder-only Transformer model trained to generate
text from left to right.
==&gt; In one sentence, BERT is an encoder-only Transformer model designed to
produce contextual representations of text.
==============================
step 064/64 | loss = 0.0797
==&gt; In one sentence, GPT is a decoder-only Transformer model trained to generate
text from left to right.
==&gt; In one sentence, BERT is an encoder-only Transformer model designed to
produce contextual representations of text.&quot;</pre>
</details>

### 022 · Fine-Tuning GPTs

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-022.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-022.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Fine-Tuning GPTs
Possible output (finally):
&quot;step 056/64 | loss = 0.0813
==&gt; In one sentence, GPT is a decoder-only Transformer model trained to generate
text from left to right.
==&gt; In one sentence, BERT is an encoder-only Transformer model designed to
produce contextual representations of text.
==============================
step 064/64 | loss = 0.0797
==&gt; In one sentence, GPT is a decoder-only Transformer model trained to generate
text from left to right.
==&gt; In one sentence, BERT is an encoder-only Transformer model designed to
produce contextual representations of text.&quot;</pre>
</details>

### 023 · GPT Model Family and Insights on the Architecture

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-023.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-023.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT Model Family and Insights on the Architecture
Learning Goals: (a) Get to know GPT-1 and GPT-2; (b) Get to know
advantages of the architecture design:
GPT-1: [ Radford et al. 2017 : Improving Language Understanding by
Generative Pre-Training]
GPT-2: [ Radford et al. 2019 : Language Models are Unsupervised
Multitask Learners]
Implicit Positional Encoding : [ Haviv et al. 2022 : Transformer
Language Models without Positional Encodings Still Learn Positional
Information]
Zero-shot Generalization : [ Wang et al. 2022 : What Language
Model Architecture and Pre-training Objective Work Best for
Zero-shot Generalization?]</pre>
</details>

### 024 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-024.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-024.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Masked LMs
2 Causal LMs
3 Scaling Laws and ”Large” Language Models
4 Seq2Seq LMs
5 Instruction Fine-Tuning</pre>
</details>

### 025 · Scaling Laws (Model Training)

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-025.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-025.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Scaling Laws (Model Training)
Neural Scaling Law : [ Hestness et al. 2022 : Deep Learning Scaling is
Predictable, Empirically]
Kaplan Scaling Law : [ Kaplan et al. 2020 : Scaling Laws for Neural
Language Models]
Chinchilla Scaling Law : [ Hoffmann et al. 2022 : Training
Compute-Optimal Large Language Models]
Language-Vision Scaling Law : [ Alabdulmohsin et al. 2022 :
Revisiting Neural Scaling Laws in Language and Vision]
Mixed-Modal Scaling Law : [ Hoffmann et al. 2023 : Scaling Laws
for Generative Mixed-Modal Language Models]
Multilingual Scaling Law : [ He et al. 2025 : Scaling Laws for
Multilingual Language Models]
Temporal Scaling Law : [ Xiong et al. 2025 : Temporal Scaling Law
for Large Language Models]
Chen et al. 2025 : Revisiting Scaling Laws for Language Models: The
Role of Data Quality and Training Strategies</pre>
</details>

### 026 · GPT-3: A New Way to Learn

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-026.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-026.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT-3: A New Way to Learn
GPT-3: [ Brown et al. 2020 : Language Models are Few-Shot
Learners]
Wei et al. 2022 : Emergent Abilities of Large Language Models
Liu et al. 2021 : What Makes Good In-Context Examples for
GPT-3?
Xie et al. 2021 : An Explanation of In-Context Learning as Implicit
Bayesian Inference
Dong et al. 2022 : A Survey on In-Context Learning</pre>
</details>

### 027 · Mixture-of-Experts (MoE)

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-027.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-027.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Mixture-of-Experts (MoE)
Fedus et al. 2022 : A Review of Sparse Expert Models in Deep
Learning
Jiang et al. 2024 : Mixtral of Experts (known as Mixtral 8x7B )
Dai et al. 2024 : DeepSeekMoE: Towards Ultimate Expert
Specialization in Mixture-of-Experts Language Models
DeepSeek AI et al. 2024 : DeepSeek-V3 Technical Report
Muennighoff et al. 2024 : OLMoE: Open Mixture-of-Experts
Language Models
Meta 2025 : The Llama 4 herd: The Beginning of a New Era of
Natively Multimodal AI Innovation
Microsoft 2026 : MAI-Thinking-1: Microsoft AI’s Flagship Reasoning
Model</pre>
</details>

### 028 · Introducing Gemma 4 (Google 2026)

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-028.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-028.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Introducing Gemma 4 (Google 2026)
Gemma is a family of generative AI models and you can use them in a
wide variety of generation tasks. Gemma models are provided with open
weights and permit responsible commercial use , allowing you to tune
and deploy them in your own projects and applications.
Gemma 4 models are available in 5 parameter sizes: E2B (gemma4:e2b in
Ollama), E4B, 12B, 31B and 26B A4B.
Small Sizes : 2B and 4B effective parameter models built for
ultra-mobile, edge, and browser deployment (e.g., Pixel, Chrome).
Unified: A 12B parameter encoder free model for multimodal tasks,
replaced vision and audio encoders with linear projections of the input.
Dense: A powerful 31B parameter dense model that bridges the gap
between server-grade performance and local execution.
Mixture-of-Experts: A highly eﬀicient 26B MoE model designed for
high-throughput, advanced reasoning.</pre>
</details>

### 029 · Introducing Gemma 4 (Google 2026)

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-029.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-029.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Introducing Gemma 4 (Google 2026)
Capabilities:
Reasoning: All models in the family are designed as highly capable
reasoners, with configurable thinking modes.
Extended Multimodalities : Processes Text, Image with variable aspect
ratio and resolution support (all models), Video, and Audio (featured
natively on the E2B, E4B and 12B models).
Increased Context Window : Small models feature a 128K context
window, while the medium models support 256K.
Enhanced Coding &amp; Agentic Capabilities : Achieves notable
improvements in coding benchmarks alongside built-in function-calling
support, powering highly capable autonomous agents.
Native System Prompt Support : Gemma 4 introduces built-in support for
the system role, enabling more structured and controllable conversations.
Multi-Token Prediction: All Gemma 4 models (E2B, E4B, 12B, 31B, and
26B A4B) include a dedicated draft model for speculative decoding,
enabling significantly faster inference with no quality loss.</pre>
</details>

### 030 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-030.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-030.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Masked LMs
2 Causal LMs
3 Scaling Laws and ”Large” Language Models
4 Seq2Seq LMs
5 Instruction Fine-Tuning</pre>
</details>

### 031 · Sequence-to-Sequence: Encoder-Decoder

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-031.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-031.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Sequence-to-Sequence: Encoder-Decoder
Seq2Seq: [ Sutskever et al. 2014 : Sequence to Sequence Learning
with Neural Networks]
BART (Meta): [ Lewis et al. 2019 : BART: Denoising
Sequence-to-Sequence Pre-training for Natural Language Generation,
Translation, and Comprehension]
T5 (Google): [ Raffel et al. 2019 : Exploring the Limits of Transfer
Learning with a Unified Text-to-Text Transformer]
Sentence-T5 (Google): [ Ni et al. 2021 : Sentence-T5: Scalable
Sentence Encoders from Pre-trained Text-to-Text Models]
RankT5 (Google): [ Zhuang et al. 2022 : RankT5: Fine-Tuning T5 for
Text Ranking with Ranking Losses]</pre>
</details>

### 032 · Run T5 on Hugging Face

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-032.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-032.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Run T5 on Hugging Face
seq2seq_tokenizer = AutoTokenizer.from_pretrained(
LOCAL_SEQ2SEQ_LM)
seq2seq_model = AutoModelForSeq2SeqLM.from_pretrained(
LOCAL_SEQ2SEQ_LM).to(DEVICE)
task = &quot;translate English to German: The library is open today.&quot;
x = seq2seq_tokenizer(task, return_tensors= &quot;pt&quot;).to(DEVICE)
with torch.no_grad():
y = seq2seq_model.generate(**x, max_new_tokens=20)
print(seq2seq_tokenizer.decode(y[0], skip_special_tokens=True))
Potential output:
&quot;Die Bibliothek ist heute geöffnet.&quot;</pre>
</details>

### 033 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-033.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-033.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 Masked LMs
2 Causal LMs
3 Scaling Laws and ”Large” Language Models
4 Seq2Seq LMs
5 Instruction Fine-Tuning</pre>
</details>

### 034 · Instructed Models on Hugging Face

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-034.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-034.webp)

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

### 035 · Instructed Models on Hugging Face

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-035.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-035.webp)

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

### 036 · IFT Data and Models

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-036.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-036.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IFT Data and Models
Tutorial: [ Zhang et al. 2025 : Advancing Language Models through
Instruction Tuning: Recent Progress and Challenges]
IFT Data:
Natural-Instructions: [ Mishra et al. 2021 : Cross-Task
Generalization via Natural Language Crowdsourcing Instructions]
Super-NaturalInstructions: [ Wang et al. 2022 :
Super-NaturalInstructions: Generalization via Declarative Instructions
on 1600+ NLP Tasks]
IFT Models:
T0: [ Sanh et al. 2021 : Multitask Prompted Training Enables
Zero-Shot Task Generalization]
FLAN: [ Chung et al. 2022 : Scaling Instruction Fine-tuned Language
Models]
Self-Instruct: [ Wang et al. 2022 : Self-Instruct: Aligning Language
Models with Self-Generated Instructions]</pre>
</details>

### 037 · IFT Techniques and Evaluation

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-037.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-037.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">IFT Techniques and Evaluation
IFT Techniques:
Auto-Instruct: [ Zhang et al. 2023 : Auto-Instruct: Automatic
Instruction Generation and Ranking for Black-Box Language Models]
PLUG: [ Zhang et al. 2023 : PLUG: Leveraging Pivot Language in
Cross-Lingual Instruction Tuning]
IFT Evaluation:
IFEval: [ Zhou et al. 2023 : Instruction-Following Evaluation for Large
Language Models]
TOWER: [ Ziems et al. 2024 : TOWER: Tree Organized Weighting
for Evaluating Complex Instructions]
Instruction Hierarchy : [ Wallace et al. 2024 : The Instruction
Hierarchy: Training LLMs to Prioritize Privileged Instructions]
IHEval: [ Zhang et al. 2025 : IHEval: Evaluating Language Models on
Following the Instruction Hierarchy]</pre>
</details>

### 038 · Takeaways

[![Beamer 原页](../../assets/llm/section1/01-hugging-face/page-038.webp){ loading=lazy }](../../assets/llm/section1/01-hugging-face/page-038.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Takeaways
Masked LM learns contextualized representations.
Causal LM completes sentences. (Why decoder-only?)
Scaling Law enables in-context learning.
MoE is a sparse, strong architecture.
Seq2Seq LM generalizes across tasks.
Instruction Tuning generalizes better than supervised fine-tuning.</pre>
</details>
