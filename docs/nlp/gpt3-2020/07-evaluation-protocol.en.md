# Prompt construction and evaluation protocol

## 1. Few-shot sample sampling

For each evaluation example, the paper usually randomly selects \(K\) examples from the training set of the task as conditioning, separated by one or two newlines. LAMBADA and StoryCloze do not have a standard supervised training set. Examples are extracted from the development set and finally evaluated in the test set.

## 2. Composition of Prompt

A complete prompt may contain:

\[
c=
[\text{instruction};
\text{demo}_1;\ldots;\text{demo}_K;
\text{query}].
\]

Different tasks will:

- Add natural language task instructions;
-Adjust answer format;
-Write classification as completion;
- Compare using candidate answers;
- Limit generation to newlines or delimiters.

## 3. Test and development

Report test results when the public test server is available. Some private test servers could not accommodate the model, so the paper was changed to development result. The numbers in the comparison table must be checked against split; the GPT-3 SuperGLUE curve in Figure 1.1 of the paper uses dev, and the reference dotted line comes from test. The text clearly reminds that direct equivalent comparisons cannot be made.

## 4. Free generation

Free form completion using beam search:

\[
\text{beam width}=4,
\qquad
\alpha=0.6
\]

length penalty. Other tasks use specific scoring or sampling. The evaluation behavior is therefore not uniformly greedy decoding.

## 5. Multiple token tags and length bias

If the candidate answers are of different lengths, the original joint probability is naturally biased towards shorter sequences, because the probability of each token is less than or equal to 1:

\[
p(y\mid c)=\prod_{r=1}^{|y|}p(y_r\mid c,y_{<r}).
\]

Available average log-probability:

\[
S_{\mathrm{avg}}(y;c)
=
\frac{1}{|y|}
\sum_{r=1}^{|y|}\log p(y_r\mid c,y_{<r}),
\]

But whether to normalize should follow specific benchmark rules. The appendix to the paper gives specific formats for different tasks.

## 6. Example settings for SuperGLUE

few-shot SuperGLUE uses 32 examples per task. Except for WSC and MultiRC, each evaluation problem resamples the conditioning examples randomly; WSC and MultiRC reuse the same set of random examples for all problems.

Therefore the result also reflects:

- model size;
- prompt design;
- Specific sampling of 32 examples;
- Answer scoring with split.

## 7. Prompt choice is also a researcher’s degree of freedom

The same task can be written in multiple natural language templates. The paper report WiC tried a variety of wordings but still had no strong result, which shows that prompt engineering can eliminate some superficial failures, but it also introduces a selection bias: if only the optimal template is reported, the benchmark will absorb additional parameters.

Rigorous reproduction requires saving:

- Complete prompt string;
- Sample ID and order;
- Random seed;
- tokenizer and truncation rules;
- decoding/scoring parameters;
- exact evaluation script。

## 8. “No training” and “no parameter adjustment” should be separated

There are no gradient updates downstream of GPT-3, but research may still make choices on prompt, format, \(K\), delimiter, and decoding. The parameter learning cost is removed, but the task interface design cost still exists.
