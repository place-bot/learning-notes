# Seq2Seq 与 Instruction Fine-Tuning

[返回 Section 1](index.md)

授课课件：Meng Jiang · CSE 60556 · Fall 2026。来源 `Chapter1-L04 (L06).pdf`，共 **61 页**。

[下载完整原课件 PDF](../../assets/llm/section1/05-instruction-tuning/slides.pdf)

## 中文复习导读

本讲先介绍 Seq2Seq、BART、T5 和 T0：BART 从受损文本恢复原文，T5 用 text-to-text 形式统一任务，T0 通过多任务 prompted training 研究未见任务泛化。

Instruction fine-tuning 用 instruction-response 数据训练模型遵循要求。课件依次介绍 Natural Instructions、Super Natural Instructions、FLAN 和 Self-Instruct，并讨论数据多样性、任务不平衡与泛化。Self-Instruct 涉及模型生成训练数据，质量筛选仍然关键。

实践部分比较 Qwen 与 `distilgpt2` 的回答，并展示少量数据微调及过拟合。高级部分包括 Auto-Instruct、PLUG、IFEval、指令原子及其权重、Instruction Hierarchy 和 IHEval。要区分“回答内容正确”“满足可验证格式要求”与“遵循指令优先级”这几种评价目标。

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
