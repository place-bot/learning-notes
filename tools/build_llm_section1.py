"""Import the supplied Chapter 1 Beamer PDFs as lossless-in-content study pages.

Run with the Codex PDF runtime. Images preserve layout; extracted text supports
search and copying. This does not claim to recover the original LaTeX source.
"""
from pathlib import Path
import hashlib
import html
import json
import re
import shutil
import subprocess
import tempfile

from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('/Users/jguo9/Desktop/26fall/LLM/Slides')
POPPLER = '/Users/jguo9/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
DECKS = [
    ('01-hugging-face', 'Hugging Face Transformers 总览', 'Chapter1-L00 (L02).pdf', 38,
     '''本讲把整个 Section 1 串起来：先区分 encoder-only、decoder-only 和 encoder-decoder，再用 Hugging Face 加载 tokenizer 和模型，观察 hidden states、mask prediction、文本续写及微调。

复习时沿着“文本 → token IDs → hidden states → 任务输出”读代码。`AutoModel` 提供模型表示，`AutoModelForCausalLM` 面向自回归生成，`AutoModelForSeq2SeqLM` 面向编码器—解码器生成。不要把 token 的编号与它的向量表示混为一谈。

课件后半段介绍 scaling laws、GPT-3、MoE、Seq2Seq 和 instruction fine-tuning，并列出深入阅读材料。微调示例中的训练损失下降，不能单独证明模型能处理未见过的任务。'''),
    ('02-masked-lm', 'Masked LM、Transformer 与 BERT', 'Chapter1-L01 (L03).pdf', 26,
     r'''本讲从 unigram、n-gram 和前馈语言模型出发，解释长距离依赖为什么难学，再引入 RNN、attention、Transformer 和 BERT。

语言建模的概率分解是 \(P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})\)。n-gram 截短历史；神经网络通过向量表示共享统计信息。Attention 用 query 与 key 的相似度决定如何汇总 value：

\[
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V.
\]

BERT 使用双向上下文做 masked language modeling；原版 BERT 还使用 next sentence prediction。复习时要能解释预训练和下游微调的关系，以及 token、segment、position 三种 embedding 的作用。最后比较 SciBERT、BioBERT 的领域适配与 Sentence-BERT 的句向量目标。'''),
    ('03-causal-lm', 'Causal LM、GPT 与 Attention 实践', 'Chapter1-L02 (L04).pdf', 22,
     '''本讲比较 GPT-1、GPT-2 与 BERT，并通过 `distilgpt2` 查看模型内部。重点是左到右的 next-token prediction、decoder 的 causal mask，以及规模和数据如何影响 zero-shot 表现。

代码部分读取 hidden states 和 attention weights。Attention 张量的维度通常对应 batch、head、query token、key token；热图的一行表示某个 query 对各个 key 的权重。复习时联系 causal mask 理解为什么不能读取未来 token。

最后的架构讨论涉及位置编码和模型结构的归纳偏置。原幻灯片中的研究假说按原样保留，不应把假说当成对所有模型都成立的定理。课件架构代码页出现 DistilBERT 命名，阅读时应注意它与前面 `distilgpt2` 实例并非同一个模型类。'''),
    ('04-scaling-icl-moe', 'Scaling Laws、ICL 与 MoE', 'Chapter1-L03 (L05).pdf', 40,
     r'''本讲讨论模型参数量 \(N\)、训练 token 数 \(D\) 和计算预算 \(C\) 的关系。课件以 \(C\approx6ND\) 作为训练 FLOPs 的近似，并比较 Kaplan 与 Chinchilla 对预算分配的建议。该式依赖计算口径与架构近似，不是所有训练过程的精确计费公式。

GPT-3 部分区分 zero-shot、one-shot 和 few-shot。ICL 在 prompt 中加入示例，推理时不更新模型参数。Zero-shot 指没有任务示例，并不意味着不能给任务指令；原课件第 23 页的措辞有冲突，复习时按这个区分理解。

Meta-learning 和 Bayesian inference 是理解 ICL 的研究视角。随后讨论 emergent abilities、MMLU，以及 MoE 如何通过 routing 只激活部分专家。要分清总参数与激活参数，并理解负载均衡、专家专门化、Mixtral 和 DeepSeekMoE 的设计。

原课件第 40 页把 GPT-3 写成 GPT-2 的 10 倍；若比较 175B 与 1.5B 参数，约为 117 倍。这里保留原页，单独注明这个数值区别。'''),
    ('05-instruction-tuning', 'Seq2Seq 与 Instruction Fine-Tuning', 'Chapter1-L04 (L06).pdf', 61,
     '''本讲先介绍 Seq2Seq、BART、T5 和 T0：BART 从受损文本恢复原文，T5 用 text-to-text 形式统一任务，T0 通过多任务 prompted training 研究未见任务泛化。

Instruction fine-tuning 用 instruction-response 数据训练模型遵循要求。课件依次介绍 Natural Instructions、Super Natural Instructions、FLAN 和 Self-Instruct，并讨论数据多样性、任务不平衡与泛化。Self-Instruct 涉及模型生成训练数据，质量筛选仍然关键。

实践部分比较 Qwen 与 `distilgpt2` 的回答，并展示少量数据微调及过拟合。高级部分包括 Auto-Instruct、PLUG、IFEval、指令原子及其权重、Instruction Hierarchy 和 IHEval。要区分“回答内容正确”“满足可验证格式要求”与“遵循指令优先级”这几种评价目标。'''),
]


def clean_text(page):
    lines = []
    for line in (page.extract_text() or '').splitlines():
        if re.fullmatch(r'[.\s]+', line):
            continue
        if line.startswith('CSE 60556 LLM (Notre Dame)'):
            continue
        lines.append(line)
    return '\n'.join(lines).strip()


def main():
    pages = ROOT / 'docs/llm/section1'
    assets = ROOT / 'docs/assets/llm/section1'
    pages.mkdir(parents=True, exist_ok=True)
    assets.mkdir(parents=True, exist_ok=True)
    manifest = []
    for slug, title, filename, count, overview in DECKS:
        source = SOURCE / filename
        reader = PdfReader(source)
        assert len(reader.pages) == count, filename
        target = assets / slug
        target.mkdir(exist_ok=True)
        shutil.copy2(source, target / 'slides.pdf')
        with tempfile.TemporaryDirectory(prefix='llm-slides-') as temp:
            subprocess.run([POPPLER, '-scale-to', '1500', '-png', str(source), str(Path(temp)/'page')], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            images = sorted(Path(temp).glob('page-*.png'))
            assert len(images) == count
            for i, image in enumerate(images, 1):
                with Image.open(image) as frame:
                    frame.convert('RGB').save(target / f'page-{i:03}.webp', quality=90, method=6)
        content = [f'# {title}', '', '[返回 Section 1](index.md)', '',
                   f'授课课件：Meng Jiang · CSE 60556 · Fall 2026。来源 `{filename}`，共 **{count} 页**。', '',
                   f'[下载完整原课件 PDF](../../assets/llm/section1/{slug}/slides.pdf)', '',
                   '## 中文复习导读', '', overview, '',
                   '## 全部 Beamer 页面', '',
                   '下面按原 PDF 页序完整呈现，包括目录、公式、图表、代码、例子与参考文献。点击图片可放大；每页下方可展开文字并搜索或复制。文字由 PDF 提取，公式和代码排版以原图及 PDF 为准；这里没有重建原始 LaTeX 源码。', '']
        for i, page in enumerate(reader.pages, 1):
            text = clean_text(page)
            heading = text.splitlines()[0] if text else '图表'
            heading = heading.replace('#', '').strip()
            content += [f'### {i:03} · {heading}', '',
                        f'[![{title}：第 {i} 页](../../assets/llm/section1/{slug}/page-{i:03}.webp){{ loading=lazy }}](../../assets/llm/section1/{slug}/page-{i:03}.webp)', '',
                        '<details><summary>展开本页文字</summary>', '<pre style="white-space:pre-wrap;overflow-wrap:anywhere">'+html.escape(text)+'</pre>', '</details>', '']
        (pages / f'{slug}.md').write_text('\n'.join(content), encoding='utf-8')
        manifest.append({'source': filename, 'pages': count, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'page': f'{slug}.md'})
        print(f'{slug}: {count} pages', flush=True)
    (assets / 'sources.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
