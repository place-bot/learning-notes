# From language model to implicit multi-task learning

## 1. Autoregressive language model

Given a token sequence

\[
x=(x_1,x_2,\ldots,x_T),
\]

The joint probability is written according to the chain rule

\[
p_\theta(x)
=
\prod_{t=1}^{T}p_\theta(x_t\mid x_1,\ldots,x_{t-1}).
\]

Maximum likelihood training is equivalent to minimizing token-level cross-entropy:

\[
\mathcal L(\theta)
=
-\sum_{t=1}^{T}\log p_\theta(x_t\mid x_{<t}).
\]

The same goal is to train both ordinary continuation and any task that can be written as text continuation.

## 2. Single task conditional distribution

A supervisory task usually estimates

\[
p(y\mid x),
\]

Where \(x\) is the input and \(y\) is the label or output. If the same input may correspond to different tasks, the model also needs to know the task \(z\):

\[
p(y\mid x,z).
\]

Traditional multi-tasking systems commonly use task IDs, task-specific headers or different encoders/decoders to represent \(z\). The idea of GPT-2 is to make the task itself a language:

\[
z=\text{“translate to French”},
\]

Then string the task, input and output into a token:

\[
[z;x;y].
\]

## 3. Why a LM may learn conditional tasks

On the training sequence \([z;x;y]\), the model must predict the output part:

\[
p_\theta(y\mid z,x).
\]

If similar structures appear repeatedly in the corpus, reducing the overall language model loss requires the model to use task prompts and input to predict the answer. Task behavior can then become a by-product of language modeling.

Two conditions need to be noted:

1. There are indeed identifiable task demonstrations in the training corpus;
2. The model has sufficient capacity and optimization capabilities to extract these structures from complex distributions.

The author emphasizes that this logic is easy to establish on a clear artificially constructed multi-task sequence; crossing from this toy situation to open web text is the empirical issue that the paper really wants to test.

## 4. “The supervision goal is part of the language model goal”

Suppose a sample consists of prompt \(c=[z;x]\) and output \(y=(y_1,\ldots,y_m)\). The task loss can be written as

\[
\mathcal L_{\mathrm{task}}
=
-\sum_{r=1}^{m}\log p_\theta(y_r\mid c,y_{<r}).
\]

The complete language model also predicts prompt tokens:

\[
\mathcal L_{\mathrm{LM}}
=
\mathcal L_{\mathrm{prompt}}
+
\mathcal L_{\mathrm{task}}.
\]

Therefore, in the well-formed training distribution, the output conditional likelihood is already included in the unified LM objective. The real difficulty is: natural web pages do not have unified separators, task descriptions may be omitted, wrong answers may appear, and the model must identify the structure on its own.

## 5. What happens in the inference phase

Given prompt token \(c\), the model is gradually generated:

\[
\hat y_r
\sim
p_\theta(\cdot\mid c,\hat y_{<r}).
\]

Here \(\theta\) remains unchanged throughout the downstream tasks. Task adaptation occurs when:

- prompt changes the conditional distribution;
- self-attention reads task prompts, examples and input from context;
- The hidden state changes with the context;
- The generation strategy determines which token to choose.

## 6. Comparison with fine-tuning

|Dimensions|Task fine-tuning|GPT-2 style contextual calls|
|---|---|---|
|Mission information|There are labels training set and task header|Text prompts and contextual formatting|
|Whether backpropagation|Yes|No|
|Whether the parameters have changed|Yes|No|
|Persistent state for each task|new parameter or adapter|No, it disappears when leaving the context|
|Adaptation cost|Multiple optimization steps|One-shot forward and autoregressive generation|
|Typical risks|overfitting, catastrophic forgetting|prompt is sensitive and output is difficult to control|

## 7. Terminology interface with GPT-3

GPT-2 reports broadly refer to migrations without parameter updates as zero-shot. Some experiments, however, provided question-and-answer pairs or translation pairs in context. GPT-3 later reclassified these cases:

- Only natural language task description: zero-shot;
- An example: one-shot;
- Multiple examples: few-shot.

Therefore, when reading the GPT-2 result, you must also see whether contextual examples are used, and not just the overall tags used in the paper.
