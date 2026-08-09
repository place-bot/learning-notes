# Zero-shot, One-shot, Few-shot and Fine-tuning

## 1. Four settings

Let the task training set be \(\mathcal D_{\mathrm{task}}\) and the pretraining parameter be \(\theta_0\).

### 1.1 Fine-tuning

Update parameters via task data:

\[
\theta_{\mathrm{task}}
=
\theta_0-eta\nabla_\theta
\mathcal L_{\mathrm{task}}(\theta_0).
\]

Use \(\theta_{\mathrm{task}}\) for reasoning. The paper does not use fine-tuning as the main experimental setting of GPT-3.

### 1.2 Few-shot

Put \(K\) examples in context:

\[
c_K=[x_1,y_1;\ldots;x_K,y_K;x_*].
\]

Model prediction

\[
\hat y_*
\sim p_{\theta_0}(y\mid c_K).
\]

The parameters remain \(\theta_0\). Papers usually range from \(K\approx10\) to \(100\), and the upper limit is limited by the 2048-token context window; specific tasks may use 32 or 64 examples.

### 1.3 One-shot

\[
K=1.
\]

An example tells the model both the task mapping and the answer format.

### 1.4 Zero-shot

No input is given - answer example, only natural language description or invocation of the task:

```text
Translate English to French:
cheese =>
```

The model relies on instructions and pretraining knowledge to complete tasks.

## 2. The difference between gradient and activation

|settings|Parameter changes|contextual activation changes|Mission data requirements|
|---|---|---|---|
| Fine-tuning |Yes|Yes|usually more|
| Few-shot |None|Yes|few examples|
| One-shot |None|Yes|1 example|
| Zero-shot |None|Yes|Description without examples|

The "learning" of in-context learning occurs in a single forward state. After closing the context, the model does not permanently retain the previous task example.

## 3. An example of unified translation

### Fine-tuning

Use a large number of English-French parallel sentence pairs to update the model parameters, and then enter new English sentences.

### Few-shot

```text
sea otter => loutre de mer
peppermint => menthe poivrée
cheese =>
```

### One-shot

```text
sea otter => loutre de mer
cheese =>
```

### Zero-shot

```text
Translate English to French:
cheese =>
```

## 4. Why few-shot still uses tags

\(y_i\) in the context example is the task label. The advantages of few-shot are:

- There is no need to use these tags for backpropagation;
- Do not save new parameters for tasks;
- Change prompt to switch tasks.

It still requires manual selection, formatting, or generation of examples. When evaluating its data efficiency, it should be counted by the number of labels actually used in prompt.

## 5. Why order and format matter

The autoregressive model reads token sequences rather than unordered collections:

\[
p(y_*\mid x_1,y_1,x_2,y_2,x_*)
\ne
p(y_*\mid x_2,y_2,x_1,y_1,x_*).
\]

Line breaks, tag words, option order, and example order can all change the output probabilities. The original paper randomly selected conditioning examples, but the prompt variance has not yet been fully quantified.

## 6. Relationship with traditional few-shot learning

Traditional meta-learning also pursues rapid adaptation from a small number of samples. The difference lies in the adaptation mechanism:

- MAML: inner layer performs gradient update;
- matching/prototypical networks: calculate samples and category representations;
- GPT-3: String examples into context and activate them through Transformer to implement adaptation.

The common point is that the outer layer first learns from a wide range of tasks or data distributions, and then uses a small amount of information to quickly change behavior when facing new tasks.
