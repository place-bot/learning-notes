# Causal LM、GPT 与 Attention 实践

[返回 Section 1](index.md)

授课课件：Meng Jiang · CSE 60556 · Fall 2026。来源 `Chapter1-L02 (L04).pdf`，共 **22 页**。

[下载完整原课件 PDF](../../assets/llm/section1/03-causal-lm/slides.pdf)


## 1. Causal 的意思是“不能偷看后面”

这里的 **causal language model** 指按顺序预测后续 token 的模型。Causal 描述信息可见性的方向，不表示模型自动能做因果推断，也不等同于统计学里识别因果效应。

给定“The dog is barking”，训练时可同时构造“看到 The，预测 dog”“看到 The dog，预测 is”等任务。但每个位置必须只能读取前缀。如果预测 `dog` 的位置能直接看到后面的 `dog`，训练就变成抄答案。

## 2. Causal mask 如何实现这个限制？

Attention 先计算位置之间的分数。**Mask（掩码）**把不允许读取的位置挡住。对四个位置，可以在 attention 分数上加：

\[
M=\begin{bmatrix}
0&-\infty&-\infty&-\infty\\
0&0&-\infty&-\infty\\
0&0&0&-\infty\\
0&0&0&0
\end{bmatrix}.
\]

然后计算 \(\operatorname{softmax}(QK^\top/\sqrt{d_k}+M)\)。由于 \(e^{-\infty}=0\)，未来位置获得零权重。实际实现也可能用非常小的数。

这里对角线可见：位置 \(t\) 的表示含 \(x_t\)，用于预测 \(x_{t+1}\)。这与说“预测当前目标只能看它之前的 token”一致，只是输入和标签的下标错开一位。

**Padding mask** 的用途不同：遮住为对齐长度补出来的空位置。一个防未来信息泄露，一个防填充位置干扰。

## 3. 为什么训练能并行，生成却一步一步？

训练时整条真实序列已经给出，所以可以一次计算所有位置的预测损失，再用 causal mask 保证每个位置只用允许的信息。这叫 **teacher forcing** 的典型用法：训练条件中给的前文是真实前文。

生成时，下一个 token 还不存在。模型先根据 prompt 产生一个 token，把它接回输入，再产生下一个。生成中的前文包含模型自己的选择，错误也可能沿着后续文本传播。

例子：训练有“I like tea”，模型同时学习 `I→like`、`I like→tea`；使用时只有“I”，先选出 `like` 才能继续。

## 4. GPT-1、GPT-2 与 BERT：差别在哪一层？

**GPT** 是 Generative Pre-trained Transformer。GPT-1 的核心路线是先做语言模型预训练，再针对任务微调。GPT-2 扩大规模和训练数据，强调用文本上下文直接表达任务，观察没有针对该任务微调时的表现。

**Generative（生成式）**表示模型能给序列分配概率并产生文本。**Discriminative（判别式）**通常强调给输入预测类别等目标；不能仅按模型名字把所有使用方式永久划死。

| 问题 | BERT 的典型方式 | GPT 的典型方式 |
| --- | --- | --- |
| 预训练时预测什么 | 被选中、被遮盖的 token | 后续 token |
| 一个位置能读什么 | 两侧输入 | 当前及以前输入 |
| 怎么做分类 | 在表示上加任务头并微调 | 可加任务头，或用文本标签表达任务 |
| 怎么生成长文本 | 标准 MLM 接口不直接提供通常的左到右续写 | 自然按 token 迭代生成 |

“BERT 理解、GPT 生成”只是记忆提示，解释能力时仍要回到目标函数、可见信息和任务接口。

## 5. Zero-shot 与 supervised fine-tuning

**Zero-shot** 在这里指没有给当前任务的示例，也没有为该任务进行专门微调，就让模型完成任务。比如直接给“Translate to German: ...”。这不意味着预训练时从未见过相关语言或类似任务。

**Supervised fine-tuning** 则用输入和正确输出训练参数。把“积极/消极”的目标标签作为监督，使表示更适合情感分类，就是一例。

比较实验时要问：模型有没有在这个任务上训练过？Prompt 中给了几个例子？训练数据是否可能包含测试材料？这些设置会影响结论，不能只比表格最高分。

## 6. 从 hidden states 到 next-token probability

对当前位置的隐藏向量 \(h_t\in\mathbb R^d\)，输出头给词表里每个 token 一个 logit：

\[
z_t=W_{\mathrm{out}}h_t+b,\qquad
p_t=\operatorname{softmax}(z_t).
\]

若词表大小为 \(V\)，\(z_t,p_t\) 长度都是 \(V\)。\(p_{t,j}\) 是下一 token 取第 \(j\) 个词表项目的概率。

训练的平均 **negative log-likelihood（负对数似然）**为：

\[
\mathcal L=-\frac1{T-1}\sum_{t=1}^{T-1}\log P_\theta(x_{t+1}\mid x_{1:t}).
\]

它也常称 token-level cross-entropy。**Perplexity（困惑度）**是平均负对数似然取指数：\(\mathrm{PPL}=e^{\mathcal L}\)。例如损失为 \(\ln4\)，困惑度为 4；可以粗略理解为模型平均仍面对多大程度的选择不确定性。比较困惑度需保持测试数据和分词口径一致。

## 7. Greedy、sampling、temperature 是什么？

有了概率分布，还要决定怎么选 token。**Greedy decoding（贪心解码）**每一步选概率最大的候选；**sampling（采样）**按概率随机选，所以同一输入可能得到不同输出。

**Temperature（温度）**缩放 logits：\(p_j\propto e^{z_j/\tau}\)。\(\tau>0\) 较小时分布更尖，较大时更平。它改变的是选词分布，不会直接给模型增加知识。

**Top-k** 只保留分数最高的 k 个候选；**top-p** 保留累计概率达到指定阈值的一组候选，再从中采样。它们用于限制生成选择范围。这些是帮助理解生成的补充概念，不是本讲所有实验都必须使用的步骤。

## 8. 读懂课件的 attention 张量

课件输出 `torch.Size([1, 12, 16, 16])`，含义是：一条输入、12 个 attention heads、16 个 query 位置、16 个 key 位置。外层还按网络 layer 返回多个这样的张量；课件例子中是 6 层。

`attentions[layer][0, head]` 先选层，再选 batch 中第 0 条输入和某个头，得到 \(16\times16\) 矩阵。**Layer** 是网络深度中的一步；**head** 是同一层内并行的一组注意力投影。两者不是同一个编号。

`transpose` 调换维度以完成点积；`softmax(..., dim=-1)` 沿 key 的方向归一化；乘 `value` 才得到信息汇总。课件展示的 `DistilBertSelfAttention` 名称与 `distilgpt2` 示例不是同一个模型类，读代码时不要据此把它们当成相同实现。

## 9. Attention 热图应该怎么解释？

横轴是被读取的 key，纵轴是提出查询的 query。看一行，就是看这个 query 从哪里取信息。标准 causal self-attention 的右上方对应未来位置，应当被遮住。

某个方块颜色深，表示在该头、该层、该次输入中，归一化权重较大。它不直接告诉你最终答案由哪个词“造成”。其他头、value 内容、残差路径和后续层都会改变最终输出。

课件 token 中出现的 `Ġ` 等字符通常与 tokenizer 的空格编码方式有关，不是文本里真的出现了一个奇怪的自然语言词。

## 10. Positional encoding 与 inductive bias

**Positional encoding（位置编码）**向模型提供顺序信息。**Inductive bias（归纳偏置）**是架构或学习方式倾向于表示的规律，例如 causal mask 强制信息只能向后传播。

课件讨论 causal attention 是否能形成某种隐式位置线索。这是研究问题：可见前缀的结构本身确实引入了顺序上的不对称，但不能据此断言所有 causal 模型都不需要显式位置机制。

## 11. 自测与答案

**训练时把整句送进去，为什么不算作弊？** 因为 causal mask 限制每个位置能读取的内容，而标签向后错开一位。

**模型生成两次不同答案，是参数变了吗？** 不一定。仅采样就可能导致差异；参数可以完全相同。

**12 个头等于 12 层吗？** 不等于。头属于某层内部的并行计算，层表示先后堆叠的深度。

下一讲：[规模、ICL 和专家模型](04-scaling-icl-moe.md)。

## 全部 Beamer 页面

下面按原 PDF 页序完整呈现，包括目录、公式、图表、代码、例子与参考文献。点击图片可放大；每页下方可展开文字并搜索或复制。文字由 PDF 提取，公式和代码排版以原图及 PDF 为准；这里没有重建原始 LaTeX 源码。

### 001 · Causal Language Models

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-001.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-001.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Causal Language Models
Meng Jiang 1
1Department of Computer Science and Engineering (CSE)
University of Notre Dame
CSE 60556 LLM</pre>
</details>

### 002 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-002.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-002.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 GPT-1 &amp; GPT-2
2 Practice with ‘distilgpt2’
3 Insights</pre>
</details>

### 003 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-003.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-003.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 GPT-1 &amp; GPT-2
2 Practice with ‘distilgpt2’
3 Insights</pre>
</details>

### 004 · Timeline

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-004.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-004.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Timeline
06/2017: Transformer
06/2018: GPT-1
10/2018: BERT
02/2019: GPT-2
10/2019: BART, T5
05/2020: GPT-3</pre>
</details>

### 005 · GPT-1

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-005.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-005.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT-1
Pre-trained on predicting next words (in a unidirectional, left-to-right,
way.) – naturally autoregressive language modeling.
Supervised fine-tuning: add linear layers.
from Radford et al. 2017 : Improving Language Understanding by
Generative Pre-Training</pre>
</details>

### 006 · GPT-1: Fine-tuning Tasks

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-006.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-006.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT-1: Fine-tuning Tasks
Text generation:
In the midnight, the moon ⇒ shone brightly, illuminating the
quiet streets.
Text classification:
The weather today is sunny. ⇒ positive, negative, neutral
Text entailment:
Premise: A soccer game with multiple males playing.
Hypothesis: Some men are playing a sport.
⇒ entailment, contradiction, neutral
Text similarity:
A: The car is fast and red.
B: The vehicle is quick and crimson.
⇒ 0.85 ∈ [0, 1]
Multi-choice QA: ...</pre>
</details>

### 007 · GPT-1 vs BERT

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-007.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-007.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT-1 vs BERT
GPT-1 uses a stack of unidirectional decoders for text generation.
BERT uses a stack of bidirectional encoders for text understanding.
GPT-1 BERT-baseBERT-large
Parameters 117 million110 million 340 million
Layers 12 12 24
Context token size512 512 512
Hidden dimensions768 768 1024
Batch size 64 256 256
BERT is good at language understanding tasks. GPT is better suited for
language generation tasks.</pre>
</details>

### 008 · GPT-2

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-008.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-008.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT-2
GPT-2 is a direct scale-up of GPT-1, 10 times larger. It can carry out
multiple tasks due to (a) larger and cleaner training data and (b) larger
number of parameters.
GPT-1 GPT-2
Parameters 117 million 1.5 billion
Decoder layers 12 48
Context token size 512 1024
Hidden dimensions 768 1600
Batch size 64 512
from Radford et al. 2019 : Language Models are Unsupervised Multitask
Learners</pre>
</details>

### 009 · GPT-2: Results

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-009.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-009.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT-2: Results
Zero-shot task performance of WebText LMs as a function of model size
on many NLP tasks:</pre>
</details>

### 010 · GPT-2: Scaling Law started to emerge

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-010.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-010.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">GPT-2: Scaling Law started to emerge</pre>
</details>

### 011 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-011.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-011.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 GPT-1 &amp; GPT-2
2 Practice with ‘distilgpt2’
3 Insights</pre>
</details>

### 012 · Dive into Transformers with Hugging Face

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-012.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-012.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Dive into Transformers with Hugging Face
gpt_tokenizer = AutoTokenizer.from_pretrained(LOCAL_CAUSAL_LM)
gpt_model = AutoModelForCausalLM.from_pretrained(LOCAL_CAUSAL_LM,
output_attentions=True,
output_hidden_states=True).to(DEVICE)
gpt_model.eval()
text = &quot;Transformers in Hugging Face make it easy to reuse
pretrained language models.&quot;
inputs = gpt_tokenizer(text, return_tensors= &quot;pt&quot;)
with torch.no_grad():
outputs = gpt_model(**inputs)
print(outputs.keys())
Output:
odict_keys([&#x27;logits&#x27;, &#x27;past_key_values&#x27;, &#x27;hidden_states&#x27;, &#x27;
attentions&#x27;])</pre>
</details>

### 013 · Architecture Code

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-013.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-013.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Architecture Code
modeling_distilbert.py: ‘distilgpt2‘ as one of Transformer models
class DistilBertSelfAttention(nn.Module):
def __init__(self, config: PreTrainedConfig):
super().__init__()
self.config = config
self.n_heads = config.n_heads
self.dim = config.dim
self.attention_head_size = self.dim // self.n_heads
self.scaling = self.attention_head_size**-0.5
self.q_lin = nn.Linear(in_features=config.dim,
out_features=config.dim)
self.k_lin = ...
self.v_lin = ...
self.out_lin = ...
self.dropout = nn.Dropout(p=config.attention_dropout)</pre>
</details>

### 014 · Architecture Code

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-014.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-014.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Architecture Code
def forward(self, hidden_states, attention_mask ...):
input_shape = hidden_states.shape[:-1]
hidden_shape = (*input_shape, -1, self.attention_head_size)
query_layer = self.q_lin(hidden_states).view(*hidden_shape).
transpose(1, 2)
key_layer = self.k_lin(hidden_states).view(*hidden_shape).
transpose(1, 2)
value_layer = self.v_lin(hidden_states).view(*hidden_shape).
transpose(1, 2)
attention_interface: Callable = ALL_ATTENTION_FUNCTIONS.
get_interface(
self.config._attn_implementation, eager_attention_forward
)
attn_output, attn_weights = attention_interface(
self, query_layer, key_layer, value_layer, attention_mask,
) ...</pre>
</details>

### 015 · Architecture Code

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-015.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-015.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Architecture Code
def eager_attention_forward(module, query, key, value,
attention_mask, scaling, dropout ...):
if scaling is None:
scaling = query.size(-1) ** -0.5
# Take the dot product between &quot;query&quot; and &quot;key&quot; to get the
raw attention scores.
attn_weights = torch.matmul(query, key.transpose(2, 3)) *
scaling
if attention_mask is not None:
attn_weights = attn_weights + attention_mask
attn_weights = nn.functional.softmax(attn_weights, dim=-1)
attn_weights = nn.functional.dropout(attn_weights, p=dropout,
training=module.training)
attn_output = torch.matmul(attn_weights, value)
attn_output = attn_output.transpose(1, 2).contiguous()
return attn_output, attn_weights</pre>
</details>

### 016 · Dive into Transformers with Hugging Face

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-016.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-016.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Dive into Transformers with Hugging Face
attentions = outputs.attentions
print(len(attentions)) # number of layers
print(attentions[0].shape) # [batch, heads, query_tokens,
key_tokens]
layer, head = 0, 0
attn = attentions[layer][0, head] # [seq_len, seq_len]
layer_last, head = -1, 0
attn_last = attentions[layer_last][0, head] # [seq_len, seq_len]
tokens = gpt_tokenizer.convert_ids_to_tokens(inputs[ &quot;input_ids&quot;
][0])
print(tokens)
Output:
6
torch.Size([1, 12, 16, 16])
[&#x27;Transform&#x27;, &#x27;ers&#x27;, &#x27;Ġin&#x27;, &#x27;ĠHug&#x27;, &#x27;ging&#x27;, &#x27;ĠFace&#x27;, &#x27;Ġmake&#x27;, &#x27;
Ġit&#x27;, &#x27;Ġeasy&#x27;, &#x27;Ġto&#x27;, &#x27;Ġreuse&#x27;, &#x27;Ġpret&#x27;, &#x27;rained&#x27;, &#x27;Ġlanguage
&#x27;, &#x27;Ġmodels&#x27;, &#x27;.&#x27;]</pre>
</details>

### 017 · Visualize Attentions

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-017.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-017.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Visualize Attentions
import matplotlib.pyplot as plt
plt.figure(figsize=(7, 6))
plt.imshow(attn)
plt.xticks(range(len(tokens)), tokens, rotation=90)
plt.yticks(range(len(tokens)), tokens)
plt.xlabel(&quot;Keys / values attended to&quot;)
plt.ylabel(&quot;Queries&quot;)
plt.title(f&quot;Layer {layer}, Head {head} attention&quot;)
plt.colorbar()
plt.show()</pre>
</details>

### 018 · Visualize Attentions

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-018.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-018.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Visualize Attentions
Transform
ers
in
Hug
ging
Face
make
it
easy
to
reuse
pret
rained
language
models
Keys / values attended to
Transform
ers
in
Hug
ging
Face
make
it
easy
to
reuse
pret
rained
language
models
Queries
Layer 0, Head 0 attention
0.0
0.2
0.4
0.6
0.8
1.0
Figure: First layer, first head
Transform
ers
in
Hug
ging
Face
make
it
easy
to
reuse
pret
rained
language
models
Keys / values attended to
Transform
ers
in
Hug
ging
Face
make
it
easy
to
reuse
pret
rained
language
models
Queries
Layer -1, Head 0 attention
0.0
0.2
0.4
0.6
0.8
1.0 Figure: Last layer, first head</pre>
</details>

### 019 · Table of Contents

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-019.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-019.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Table of Contents
1 GPT-1 &amp; GPT-2
2 Practice with ‘distilgpt2’
3 Insights</pre>
</details>

### 020 · Causal attention learns implicit positional encodings.

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-020.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-020.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Causal attention learns implicit positional encodings.
Conjecture: Causal attention allows models to predict the number of
attendable tokens at each position. Such a mechanism could effectively
encode the absolute position of each token into its representation.
Observation: GPT does not rely on explicit positional encodings.
Analysis: (1) Some notion of absolute positions exists in the hidden layers
of LMs even when they are trained without explicit positional encoding,
and that this information is acquired throughout the first few layers.
GPTs leverage the causal attention to estimate the number of preceding
tokens for each current token, thereby approximating its absolute position.
(2) Bidirectional transformer encoders do not contain causal attention
masks or any other limitation on the attention mechanism; thus, they
should be unable to learn absolute positions without positional encoding.
from Haviv et al. 2022 : Transformer Language Models without Positional
Encodings Still Learn Positional Information</pre>
</details>

### 021 · Path to zero-shot Generalization?

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-021.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-021.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Path to zero-shot Generalization?
Question: How do causal attention mechanisms and multi-task learning
affect zero-shot capabilities?
Findings: (1) GPT models trained with an autoregressive language
modeling objective perform best in zero-shot generalization after
unsupervised pre-training .
(2) BERT models trained with masked language modeling achieve the best
zero-shot performance after multitask fine-tuning .
from Wang et al. 2022 : What Language Model Architecture and
Pre-training Objective Work Best for Zero-shot Generalization?</pre>
</details>

### 022 · Takeaways

[![Beamer 原页](../../assets/llm/section1/03-causal-lm/page-022.webp){ loading=lazy }](../../assets/llm/section1/03-causal-lm/page-022.webp)

<details><summary>展开本页文字</summary>
<pre style="white-space:pre-wrap;overflow-wrap:anywhere">Takeaways
GPT-1 was pre-trained on predicting next words.
It added linear layers for downstream tasks.
GPT-2 was ten times larger, showing zero-shot task performance.
Causal attention learned implicit positional encodings.
What architecture would enable superior zero-shot generalization?</pre>
</details>
