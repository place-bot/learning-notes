# Supervised fine-tuning: why small amounts of high-quality data are effective

## 1. The role of SFT

The pretraining model will predict natural continuation. SFT teaches it with an explicit prompt-answer pair:

- Distinguish between user request and assistant response;
- Answer instructions directly;
- Use a conversational style;
- Follow safety practices in the initial stages;
- Output expected length and structure.

## 2. Data sources and screening

The authors started with public instruction-tuning data and found that much of the third-party data lacked diversity or conversational quality. Then focus on collecting vendor-based high-quality samples.

The experimental conclusion is that quality is more critical than blind heap quantity: after giving up millions of weaker third-party samples, using tens of thousands of self-collected high-quality annotations actually improves the results. finally in

\[
27{,}540
\]

Stop continuing to collect when there is an SFT annotation.

The paper clearly states that no Meta user data was used.

## 3. Mark content

Annotators write both prompts and ideal answers, divided into helpful and safe scenarios. Safe samples include prompts that may induce inappropriate content and safe answers that comply with the guidelines.

The author randomly checked 180 examples and compared the manual answers with the SFT model samples. He found that the model output could often compete with the manual SFT data, so more subsequent annotation resources were invested in preference comparisons.

## 4. Loss mask

A sample sequence is:

\[
s=[p_1,\ldots,p_m,y_1,\ldots,y_n].
\]

The model forward still reads prompt; loss is only calculated on answer tokens:

\[
\mathcal L_{\mathrm{SFT}}
=
-\sum_{t=1}^{n}
\log p_\theta(y_t\mid p,y_{<t}).
\]

The loss of the prompt token is set to zero to prevent the training goal from wasting on repeating user input.

## 5. Training configuration

- Initial learning rate: \(2\times10^{-5}\);
- cosine schedule；
- weight decay：0.1；
- batch size：64；
- sequence length：4096；
- Train for 2 epochs.

The author concatenates multiple prompts and answers to fill the sequence, and uses special tokens to separate fields.

## 6. Why is RLHF still needed after SFT?

SFT is limited by the writing distribution of human answers:

- Differences in annotators' styles will be imitated as a whole;
- Low-quality tail answers also enter token loss;
- Writing an ideal long answer is more expensive than comparing two answers;
- The model may explore a better expression than the annotator, but SFT will not actively select it.

Preference data allows humans to simply judge “which is better.” The reward model then extends this sequence-level judgment to a large number of model samples.

## 7. “A small amount” needs to be understood in context

27,540 instruction samples are relatively small compared to millions, but it builds on:

- 2T-token pretraining;
- public instruction data bootstrap;
- More than 1.4 million Meta preference comparisons followed;
- Multiple rounds of rejection sampling and PPO;
- Safety specific data.

Therefore, the paper supports "high-quality SFT seeds can be smaller" but does not support "only more than 20,000 samples are needed for the entire dialogue alignment".
